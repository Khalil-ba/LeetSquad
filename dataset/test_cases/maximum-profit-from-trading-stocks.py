def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30],future = [25, 35, 45],budget = 50) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30],future = [25, 35, 45],budget = 50) == 30: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 1, 1, 1, 1],future = [1, 1, 1, 1, 1],budget = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 1, 1, 1, 1],future = [1, 1, 1, 1, 1],budget = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(present = [100, 100, 100],future = [100, 100, 100],budget = 200) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [100, 100, 100],future = [100, 100, 100],budget = 200) == 0: {e}')
    
    total += 1
    try:
        result = candidate(present = [100, 100, 100],future = [90, 90, 90],budget = 300) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [100, 100, 100],future = [90, 90, 90],budget = 300) == 0: {e}')
    
    total += 1
    try:
        result = candidate(present = [2, 2, 5],future = [3, 4, 10],budget = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [2, 2, 5],future = [3, 4, 10],budget = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(present = [100, 0, 100],future = [101, 1, 101],budget = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [100, 0, 100],future = [101, 1, 101],budget = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 1, 1, 1, 1],future = [2, 2, 2, 2, 2],budget = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 1, 1, 1, 1],future = [2, 2, 2, 2, 2],budget = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(present = [5, 4, 6, 2, 3],future = [8, 5, 4, 3, 5],budget = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [5, 4, 6, 2, 3],future = [8, 5, 4, 3, 5],budget = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(present = [3, 3, 12],future = [0, 3, 15],budget = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [3, 3, 12],future = [0, 3, 15],budget = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30],future = [5, 15, 25],budget = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30],future = [5, 15, 25],budget = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(present = [5, 3, 10, 1, 2],future = [7, 5, 15, 2, 3],budget = 12) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [5, 3, 10, 1, 2],future = [7, 5, 15, 2, 3],budget = 12) == 6: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30],future = [25, 30, 40],budget = 50) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30],future = [25, 30, 40],budget = 50) == 25: {e}')
    
    total += 1
    try:
        result = candidate(present = [0, 0, 0],future = [1, 1, 1],budget = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [0, 0, 0],future = [1, 1, 1],budget = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(present = [0, 0, 0],future = [1, 1, 1],budget = 0) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [0, 0, 0],future = [1, 1, 1],budget = 0) == 3: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 2, 3, 4, 5],future = [2, 3, 4, 5, 6],budget = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 2, 3, 4, 5],future = [2, 3, 4, 5, 6],budget = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(present = [50, 50, 50],future = [60, 60, 60],budget = 100) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [50, 50, 50],future = [60, 60, 60],budget = 100) == 20: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 2, 3, 4, 5],future = [6, 7, 8, 9, 10],budget = 15) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 2, 3, 4, 5],future = [6, 7, 8, 9, 10],budget = 15) == 25: {e}')
    
    total += 1
    try:
        result = candidate(present = [100, 100, 100],future = [50, 50, 50],budget = 300) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [100, 100, 100],future = [50, 50, 50],budget = 300) == 0: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30],future = [15, 25, 35],budget = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30],future = [15, 25, 35],budget = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 2, 3, 4, 5],future = [5, 4, 3, 2, 1],budget = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 2, 3, 4, 5],future = [5, 4, 3, 2, 1],budget = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 60],budget = 60) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 60],budget = 60) == 15: {e}')
    
    total += 1
    try:
        result = candidate(present = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],future = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],budget = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],future = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],budget = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(present = [5, 15, 25, 35, 45, 55, 65],future = [10, 20, 30, 40, 50, 60, 70],budget = 200) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [5, 15, 25, 35, 45, 55, 65],future = [10, 20, 30, 40, 50, 60, 70],budget = 200) == 30: {e}')
    
    total += 1
    try:
        result = candidate(present = [50, 40, 30, 20, 10],future = [55, 45, 35, 25, 15],budget = 80) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [50, 40, 30, 20, 10],future = [55, 45, 35, 25, 15],budget = 80) == 15: {e}')
    
    total += 1
    try:
        result = candidate(present = [50, 40, 30, 20, 10],future = [70, 60, 40, 30, 20],budget = 100) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [50, 40, 30, 20, 10],future = [70, 60, 40, 30, 20],budget = 100) == 50: {e}')
    
    total += 1
    try:
        result = candidate(present = [30, 40, 50, 60, 70],future = [25, 35, 45, 55, 65],budget = 150) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [30, 40, 50, 60, 70],future = [25, 35, 45, 55, 65],budget = 150) == 0: {e}')
    
    total += 1
    try:
        result = candidate(present = [90, 80, 70, 60, 50],future = [100, 90, 80, 70, 60],budget = 200) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [90, 80, 70, 60, 50],future = [100, 90, 80, 70, 60],budget = 200) == 30: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],future = [12, 22, 32, 42, 52, 62, 72, 82, 92, 102],budget = 550) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],future = [12, 22, 32, 42, 52, 62, 72, 82, 92, 102],budget = 550) == 20: {e}')
    
    total += 1
    try:
        result = candidate(present = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],future = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 125) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],future = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 125) == 125: {e}')
    
    total += 1
    try:
        result = candidate(present = [80, 60, 40, 20, 0],future = [100, 80, 60, 40, 20],budget = 200) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [80, 60, 40, 20, 0],future = [100, 80, 60, 40, 20],budget = 200) == 100: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 60],budget = 100) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 60],budget = 100) == 20: {e}')
    
    total += 1
    try:
        result = candidate(present = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0],future = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90],budget = 200) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0],future = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90],budget = 200) == 250: {e}')
    
    total += 1
    try:
        result = candidate(present = [90, 80, 70, 60, 50],future = [100, 90, 80, 70, 60],budget = 250) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [90, 80, 70, 60, 50],future = [100, 90, 80, 70, 60],budget = 250) == 30: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 10, 10, 10, 10],future = [20, 20, 20, 20, 20],budget = 40) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 10, 10, 10, 10],future = [20, 20, 20, 20, 20],budget = 40) == 40: {e}')
    
    total += 1
    try:
        result = candidate(present = [5, 15, 25, 35, 45],future = [10, 20, 30, 40, 50],budget = 25) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [5, 15, 25, 35, 45],future = [10, 20, 30, 40, 50],budget = 25) == 10: {e}')
    
    total += 1
    try:
        result = candidate(present = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],future = [60, 60, 60, 60, 60, 60, 60, 60, 60, 60],budget = 450) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],future = [60, 60, 60, 60, 60, 60, 60, 60, 60, 60],budget = 450) == 90: {e}')
    
    total += 1
    try:
        result = candidate(present = [99, 98, 97, 96, 95],future = [100, 101, 102, 103, 104],budget = 400) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [99, 98, 97, 96, 95],future = [100, 101, 102, 103, 104],budget = 400) == 24: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 55],budget = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 55],budget = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(present = [25, 50, 75, 100, 125],future = [50, 75, 100, 125, 150],budget = 300) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [25, 50, 75, 100, 125],future = [50, 75, 100, 125, 150],budget = 300) == 100: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 10, 10, 10, 10],future = [20, 20, 20, 20, 20],budget = 25) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 10, 10, 10, 10],future = [20, 20, 20, 20, 20],budget = 25) == 20: {e}')
    
    total += 1
    try:
        result = candidate(present = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],future = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],budget = 70) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],future = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],budget = 70) == 0: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],future = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 45) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],future = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 45) == 25: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],future = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],budget = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],future = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],budget = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(present = [50, 50, 50, 50, 50],future = [60, 60, 60, 60, 60],budget = 250) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [50, 50, 50, 50, 50],future = [60, 60, 60, 60, 60],budget = 250) == 50: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],budget = 50) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],budget = 50) == 1: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30, 40, 50],future = [20, 30, 40, 50, 60],budget = 150) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30, 40, 50],future = [20, 30, 40, 50, 60],budget = 150) == 50: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],future = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],budget = 30) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],future = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],budget = 30) == 5: {e}')
    
    total += 1
    try:
        result = candidate(present = [50, 60, 70, 80, 90, 100],future = [60, 70, 80, 90, 100, 110],budget = 180) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [50, 60, 70, 80, 90, 100],future = [60, 70, 80, 90, 100, 110],budget = 180) == 30: {e}')
    
    total += 1
    try:
        result = candidate(present = [90, 80, 70, 60, 50],future = [50, 60, 70, 80, 90],budget = 250) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [90, 80, 70, 60, 50],future = [50, 60, 70, 80, 90],budget = 250) == 60: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],future = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],budget = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],future = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],budget = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],future = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],budget = 300) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],future = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],budget = 300) == 35: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 15, 20, 25, 30],future = [25, 20, 35, 40, 30],budget = 60) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 15, 20, 25, 30],future = [25, 20, 35, 40, 30],budget = 60) == 45: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],future = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11],budget = 50) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],future = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11],budget = 50) == 90: {e}')
    
    total += 1
    try:
        result = candidate(present = [50, 60, 70, 80, 90],future = [55, 65, 80, 75, 100],budget = 200) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [50, 60, 70, 80, 90],future = [55, 65, 80, 75, 100],budget = 200) == 20: {e}')
    
    total += 1
    try:
        result = candidate(present = [50, 40, 30, 20, 10],future = [10, 20, 30, 40, 50],budget = 100) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [50, 40, 30, 20, 10],future = [10, 20, 30, 40, 50],budget = 100) == 60: {e}')
    
    total += 1
    try:
        result = candidate(present = [50, 30, 20, 60, 40],future = [60, 40, 30, 80, 50],budget = 150) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [50, 30, 20, 60, 40],future = [60, 40, 30, 80, 50],budget = 150) == 50: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],future = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110],budget = 150) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],future = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110],budget = 150) == 50: {e}')
    
    total += 1
    try:
        result = candidate(present = [20, 30, 20, 30, 20],future = [25, 35, 25, 35, 25],budget = 80) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [20, 30, 20, 30, 20],future = [25, 35, 25, 35, 25],budget = 80) == 15: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],future = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],budget = 50) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],future = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],budget = 50) == 25: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],future = [15, 25, 35, 45, 55, 65, 75, 85, 95, 110],budget = 300) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],future = [15, 25, 35, 45, 55, 65, 75, 85, 95, 110],budget = 300) == 35: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30, 40, 50, 60],future = [15, 25, 35, 45, 60, 70],budget = 100) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30, 40, 50, 60],future = [15, 25, 35, 45, 60, 70],budget = 100) == 20: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],budget = 55) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],budget = 55) == 10: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 55],budget = 60) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 55],budget = 60) == 15: {e}')
    
    total += 1
    try:
        result = candidate(present = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],future = [190, 180, 170, 160, 150, 140, 130, 120, 110, 100],budget = 800) == 570
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],future = [190, 180, 170, 160, 150, 140, 130, 120, 110, 100],budget = 800) == 570: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 1, 1, 1, 1],future = [10, 10, 10, 10, 10],budget = 5) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 1, 1, 1, 1],future = [10, 10, 10, 10, 10],budget = 5) == 45: {e}')
    
    total += 1
    try:
        result = candidate(present = [5, 15, 25, 35, 45],future = [10, 20, 30, 40, 50],budget = 50) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [5, 15, 25, 35, 45],future = [10, 20, 30, 40, 50],budget = 50) == 15: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],future = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],budget = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],future = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],budget = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(present = [50, 50, 50, 50, 50],future = [60, 60, 60, 60, 60],budget = 150) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [50, 50, 50, 50, 50],future = [60, 60, 60, 60, 60],budget = 150) == 30: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],future = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],budget = 5) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],future = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],budget = 5) == 45: {e}')
    
    total += 1
    try:
        result = candidate(present = [100, 100, 100, 100, 100],future = [105, 105, 105, 105, 105],budget = 350) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [100, 100, 100, 100, 100],future = [105, 105, 105, 105, 105],budget = 350) == 15: {e}')
    
    total += 1
    try:
        result = candidate(present = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],future = [3, 5, 8, 10, 14, 16, 20, 22, 26, 32],budget = 50) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],future = [3, 5, 8, 10, 14, 16, 20, 22, 26, 32],budget = 50) == 15: {e}')
    
    total += 1
    try:
        result = candidate(present = [30, 20, 10, 50, 40, 60],future = [40, 30, 20, 60, 50, 70],budget = 120) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [30, 20, 10, 50, 40, 60],future = [40, 30, 20, 60, 50, 70],budget = 120) == 40: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],budget = 30) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],budget = 30) == 70: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 60],budget = 140) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 60],budget = 140) == 25: {e}')
    
    total += 1
    try:
        result = candidate(present = [50, 40, 30, 20, 10],future = [40, 30, 20, 10, 0],budget = 80) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [50, 40, 30, 20, 10],future = [40, 30, 20, 10, 0],budget = 80) == 0: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 55],budget = 150) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 55],budget = 150) == 25: {e}')
    
    total += 1
    try:
        result = candidate(present = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],future = [6, 11, 16, 21, 26, 31, 36, 41, 46, 51],budget = 150) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],future = [6, 11, 16, 21, 26, 31, 36, 41, 46, 51],budget = 150) == 7: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 50) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 50) == 25: {e}')
    
    total += 1
    try:
        result = candidate(present = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],future = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],budget = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],future = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],budget = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(present = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],future = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],budget = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],future = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],budget = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],future = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60],budget = 100) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],future = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60],budget = 100) == 25: {e}')
    
    total += 1
    try:
        result = candidate(present = [90, 80, 70, 60, 50, 40, 30, 20, 10],future = [85, 80, 75, 70, 65, 60, 55, 50, 45],budget = 200) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [90, 80, 70, 60, 50, 40, 30, 20, 10],future = [85, 80, 75, 70, 65, 60, 55, 50, 45],budget = 200) == 125: {e}')
    
    total += 1
    try:
        result = candidate(present = [15, 25, 35, 45, 55],future = [10, 20, 30, 40, 50],budget = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [15, 25, 35, 45, 55],future = [10, 20, 30, 40, 50],budget = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],future = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],budget = 5) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],future = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],budget = 5) == 40: {e}')
    
    total += 1
    try:
        result = candidate(present = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],future = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],budget = 25) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],future = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],budget = 25) == 8: {e}')
    
    total += 1
    try:
        result = candidate(present = [5, 15, 25, 35, 45, 55],future = [10, 25, 30, 40, 50, 60],budget = 90) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [5, 15, 25, 35, 45, 55],future = [10, 25, 30, 40, 50, 60],budget = 90) == 25: {e}')
    
    total += 1
    try:
        result = candidate(present = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],future = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],budget = 250) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],future = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],budget = 250) == 45: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 25, 40, 55, 70],future = [20, 35, 50, 65, 80],budget = 120) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 25, 40, 55, 70],future = [20, 35, 50, 65, 80],budget = 120) == 30: {e}')
    
    total += 1
    try:
        result = candidate(present = [100, 100, 100, 100, 100, 100],future = [110, 120, 130, 140, 150, 160],budget = 500) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [100, 100, 100, 100, 100, 100],future = [110, 120, 130, 140, 150, 160],budget = 500) == 200: {e}')
    
    total += 1
    try:
        result = candidate(present = [30, 20, 10, 5, 1],future = [25, 15, 10, 5, 1],budget = 60) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [30, 20, 10, 5, 1],future = [25, 15, 10, 5, 1],budget = 60) == 0: {e}')
    
    total += 1
    try:
        result = candidate(present = [5, 15, 25, 35, 45],future = [10, 20, 30, 40, 50],budget = 75) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [5, 15, 25, 35, 45],future = [10, 20, 30, 40, 50],budget = 75) == 15: {e}')
    
    total += 1
    try:
        result = candidate(present = [50, 40, 30, 20, 10, 5, 15, 25, 35, 45],future = [10, 20, 30, 40, 50, 15, 25, 35, 45, 55],budget = 150) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [50, 40, 30, 20, 10, 5, 15, 25, 35, 45],future = [10, 20, 30, 40, 50, 15, 25, 35, 45, 55],budget = 150) == 100: {e}')
    
    total += 1
    try:
        result = candidate(present = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],future = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],budget = 900) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],future = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],budget = 900) == 99: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],future = [15, 25, 35, 45, 60, 75, 85, 95, 105, 115],budget = 300) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],future = [15, 25, 35, 45, 60, 75, 85, 95, 105, 115],budget = 300) == 65: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],budget = 45) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],budget = 45) == 9: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],budget = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],budget = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 40, 55, 60],budget = 100) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 40, 55, 60],budget = 100) == 35: {e}')
    
    total += 1
    try:
        result = candidate(present = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],future = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],budget = 200) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],future = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],budget = 200) == 40: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],future = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],budget = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],future = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],budget = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(present = [5, 15, 25, 35, 45],future = [10, 20, 25, 30, 50],budget = 50) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [5, 15, 25, 35, 45],future = [10, 20, 25, 30, 50],budget = 50) == 10: {e}')
    
    total += 1
    try:
        result = candidate(present = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],future = [110, 100, 90, 80, 70, 60, 50, 40, 30, 20],budget = 500) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],future = [110, 100, 90, 80, 70, 60, 50, 40, 30, 20],budget = 500) == 90: {e}')
    
    total += 1
    try:
        result = candidate(present = [80, 85, 90, 95, 100],future = [100, 105, 110, 115, 120],budget = 350) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [80, 85, 90, 95, 100],future = [100, 105, 110, 115, 120],budget = 350) == 80: {e}')
    
    total += 1
    try:
        result = candidate(present = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],future = [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],budget = 300) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],future = [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],budget = 300) == 45: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],future = [25, 35, 45, 55, 65, 75, 85, 95, 105, 115],budget = 300) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],future = [25, 35, 45, 55, 65, 75, 85, 95, 105, 115],budget = 300) == 105: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 5, 10, 15, 20],future = [2, 7, 12, 20, 25],budget = 25) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 5, 10, 15, 20],future = [2, 7, 12, 20, 25],budget = 25) == 8: {e}')
    
    total += 1
    try:
        result = candidate(present = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],future = [55, 55, 55, 55, 55, 55, 55, 55, 55, 55],budget = 200) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],future = [55, 55, 55, 55, 55, 55, 55, 55, 55, 55],budget = 200) == 20: {e}')
    
    total += 1
    try:
        result = candidate(present = [50, 40, 30, 20, 10],future = [60, 50, 40, 30, 20],budget = 150) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [50, 40, 30, 20, 10],future = [60, 50, 40, 30, 20],budget = 150) == 50: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 55],budget = 100) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 55],budget = 100) == 20: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],future = [11, 11, 11, 11, 11, 11, 11, 11, 11, 11],budget = 5) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],future = [11, 11, 11, 11, 11, 11, 11, 11, 11, 11],budget = 5) == 50: {e}')
    
    total += 1
    try:
        result = candidate(present = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],future = [50, 40, 30, 20, 10, 5, 15, 25, 35, 45],budget = 150) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],future = [50, 40, 30, 20, 10, 5, 15, 25, 35, 45],budget = 150) == 90: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],future = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],budget = 50) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],future = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],budget = 50) == 7: {e}')
    
    total += 1
    try:
        result = candidate(present = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],future = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 450) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],future = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 450) == 250: {e}')
    
    total += 1
    try:
        result = candidate(present = [50, 40, 30, 20, 10],future = [60, 50, 40, 30, 20],budget = 150) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [50, 40, 30, 20, 10],future = [60, 50, 40, 30, 20],budget = 150) == 50: {e}')
    
    total += 1
    try:
        result = candidate(present = [10, 10, 10, 10, 10],future = [12, 12, 12, 12, 12],budget = 30) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [10, 10, 10, 10, 10],future = [12, 12, 12, 12, 12],budget = 30) == 6: {e}')
    
    total += 1
    try:
        result = candidate(present = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],future = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],budget = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],future = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],budget = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(present = [50, 25, 75, 100, 50],future = [75, 50, 100, 150, 75],budget = 200) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(present = [50, 25, 75, 100, 50],future = [75, 50, 100, 150, 75],budget = 200) == 100: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(present = [10, 20, 30],future = [25, 35, 45],budget = 50) == 30
    assert candidate(present = [1, 1, 1, 1, 1],future = [1, 1, 1, 1, 1],budget = 5) == 0
    assert candidate(present = [100, 100, 100],future = [100, 100, 100],budget = 200) == 0
    assert candidate(present = [100, 100, 100],future = [90, 90, 90],budget = 300) == 0
    assert candidate(present = [2, 2, 5],future = [3, 4, 10],budget = 6) == 5
    assert candidate(present = [100, 0, 100],future = [101, 1, 101],budget = 100) == 2
    assert candidate(present = [1, 1, 1, 1, 1],future = [2, 2, 2, 2, 2],budget = 5) == 5
    assert candidate(present = [5, 4, 6, 2, 3],future = [8, 5, 4, 3, 5],budget = 10) == 6
    assert candidate(present = [3, 3, 12],future = [0, 3, 15],budget = 10) == 0
    assert candidate(present = [10, 20, 30],future = [5, 15, 25],budget = 20) == 0
    assert candidate(present = [5, 3, 10, 1, 2],future = [7, 5, 15, 2, 3],budget = 12) == 6
    assert candidate(present = [10, 20, 30],future = [25, 30, 40],budget = 50) == 25
    assert candidate(present = [0, 0, 0],future = [1, 1, 1],budget = 5) == 3
    assert candidate(present = [0, 0, 0],future = [1, 1, 1],budget = 0) == 3
    assert candidate(present = [1, 2, 3, 4, 5],future = [2, 3, 4, 5, 6],budget = 15) == 5
    assert candidate(present = [50, 50, 50],future = [60, 60, 60],budget = 100) == 20
    assert candidate(present = [1, 2, 3, 4, 5],future = [6, 7, 8, 9, 10],budget = 15) == 25
    assert candidate(present = [100, 100, 100],future = [50, 50, 50],budget = 300) == 0
    assert candidate(present = [10, 20, 30],future = [15, 25, 35],budget = 25) == 5
    assert candidate(present = [1, 2, 3, 4, 5],future = [5, 4, 3, 2, 1],budget = 15) == 6
    assert candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 60],budget = 60) == 15
    assert candidate(present = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],future = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],budget = 25) == 25
    assert candidate(present = [5, 15, 25, 35, 45, 55, 65],future = [10, 20, 30, 40, 50, 60, 70],budget = 200) == 30
    assert candidate(present = [50, 40, 30, 20, 10],future = [55, 45, 35, 25, 15],budget = 80) == 15
    assert candidate(present = [50, 40, 30, 20, 10],future = [70, 60, 40, 30, 20],budget = 100) == 50
    assert candidate(present = [30, 40, 50, 60, 70],future = [25, 35, 45, 55, 65],budget = 150) == 0
    assert candidate(present = [90, 80, 70, 60, 50],future = [100, 90, 80, 70, 60],budget = 200) == 30
    assert candidate(present = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],future = [12, 22, 32, 42, 52, 62, 72, 82, 92, 102],budget = 550) == 20
    assert candidate(present = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],future = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 125) == 125
    assert candidate(present = [80, 60, 40, 20, 0],future = [100, 80, 60, 40, 20],budget = 200) == 100
    assert candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 60],budget = 100) == 20
    assert candidate(present = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0],future = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90],budget = 200) == 250
    assert candidate(present = [90, 80, 70, 60, 50],future = [100, 90, 80, 70, 60],budget = 250) == 30
    assert candidate(present = [10, 10, 10, 10, 10],future = [20, 20, 20, 20, 20],budget = 40) == 40
    assert candidate(present = [5, 15, 25, 35, 45],future = [10, 20, 30, 40, 50],budget = 25) == 10
    assert candidate(present = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],future = [60, 60, 60, 60, 60, 60, 60, 60, 60, 60],budget = 450) == 90
    assert candidate(present = [99, 98, 97, 96, 95],future = [100, 101, 102, 103, 104],budget = 400) == 24
    assert candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 55],budget = 0) == 0
    assert candidate(present = [25, 50, 75, 100, 125],future = [50, 75, 100, 125, 150],budget = 300) == 100
    assert candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 25) == 25
    assert candidate(present = [10, 10, 10, 10, 10],future = [20, 20, 20, 20, 20],budget = 25) == 20
    assert candidate(present = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],future = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],budget = 70) == 0
    assert candidate(present = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],future = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 45) == 25
    assert candidate(present = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],future = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],budget = 100) == 0
    assert candidate(present = [50, 50, 50, 50, 50],future = [60, 60, 60, 60, 60],budget = 250) == 50
    assert candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],budget = 50) == 1
    assert candidate(present = [10, 20, 30, 40, 50],future = [20, 30, 40, 50, 60],budget = 150) == 50
    assert candidate(present = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],future = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],budget = 30) == 5
    assert candidate(present = [50, 60, 70, 80, 90, 100],future = [60, 70, 80, 90, 100, 110],budget = 180) == 30
    assert candidate(present = [90, 80, 70, 60, 50],future = [50, 60, 70, 80, 90],budget = 250) == 60
    assert candidate(present = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],future = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],budget = 25) == 5
    assert candidate(present = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],future = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],budget = 300) == 35
    assert candidate(present = [10, 15, 20, 25, 30],future = [25, 20, 35, 40, 30],budget = 60) == 45
    assert candidate(present = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],future = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11],budget = 50) == 90
    assert candidate(present = [50, 60, 70, 80, 90],future = [55, 65, 80, 75, 100],budget = 200) == 20
    assert candidate(present = [50, 40, 30, 20, 10],future = [10, 20, 30, 40, 50],budget = 100) == 60
    assert candidate(present = [50, 30, 20, 60, 40],future = [60, 40, 30, 80, 50],budget = 150) == 50
    assert candidate(present = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],future = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110],budget = 150) == 50
    assert candidate(present = [20, 30, 20, 30, 20],future = [25, 35, 25, 35, 25],budget = 80) == 15
    assert candidate(present = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],future = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],budget = 50) == 25
    assert candidate(present = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],future = [15, 25, 35, 45, 55, 65, 75, 85, 95, 110],budget = 300) == 35
    assert candidate(present = [10, 20, 30, 40, 50, 60],future = [15, 25, 35, 45, 60, 70],budget = 100) == 20
    assert candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],budget = 55) == 10
    assert candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 55],budget = 60) == 15
    assert candidate(present = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],future = [190, 180, 170, 160, 150, 140, 130, 120, 110, 100],budget = 800) == 570
    assert candidate(present = [1, 1, 1, 1, 1],future = [10, 10, 10, 10, 10],budget = 5) == 45
    assert candidate(present = [5, 15, 25, 35, 45],future = [10, 20, 30, 40, 50],budget = 50) == 15
    assert candidate(present = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],future = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],budget = 50) == 0
    assert candidate(present = [50, 50, 50, 50, 50],future = [60, 60, 60, 60, 60],budget = 150) == 30
    assert candidate(present = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],future = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],budget = 5) == 45
    assert candidate(present = [100, 100, 100, 100, 100],future = [105, 105, 105, 105, 105],budget = 350) == 15
    assert candidate(present = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],future = [3, 5, 8, 10, 14, 16, 20, 22, 26, 32],budget = 50) == 15
    assert candidate(present = [30, 20, 10, 50, 40, 60],future = [40, 30, 20, 60, 50, 70],budget = 120) == 40
    assert candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],budget = 30) == 70
    assert candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 60],budget = 140) == 25
    assert candidate(present = [50, 40, 30, 20, 10],future = [40, 30, 20, 10, 0],budget = 80) == 0
    assert candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 55],budget = 150) == 25
    assert candidate(present = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],future = [6, 11, 16, 21, 26, 31, 36, 41, 46, 51],budget = 150) == 7
    assert candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 50) == 25
    assert candidate(present = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],future = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],budget = 20) == 4
    assert candidate(present = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],future = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],budget = 20) == 20
    assert candidate(present = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],future = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60],budget = 100) == 25
    assert candidate(present = [90, 80, 70, 60, 50, 40, 30, 20, 10],future = [85, 80, 75, 70, 65, 60, 55, 50, 45],budget = 200) == 125
    assert candidate(present = [15, 25, 35, 45, 55],future = [10, 20, 30, 40, 50],budget = 100) == 0
    assert candidate(present = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],future = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],budget = 5) == 40
    assert candidate(present = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],future = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],budget = 25) == 8
    assert candidate(present = [5, 15, 25, 35, 45, 55],future = [10, 25, 30, 40, 50, 60],budget = 90) == 25
    assert candidate(present = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],future = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],budget = 250) == 45
    assert candidate(present = [10, 25, 40, 55, 70],future = [20, 35, 50, 65, 80],budget = 120) == 30
    assert candidate(present = [100, 100, 100, 100, 100, 100],future = [110, 120, 130, 140, 150, 160],budget = 500) == 200
    assert candidate(present = [30, 20, 10, 5, 1],future = [25, 15, 10, 5, 1],budget = 60) == 0
    assert candidate(present = [5, 15, 25, 35, 45],future = [10, 20, 30, 40, 50],budget = 75) == 15
    assert candidate(present = [50, 40, 30, 20, 10, 5, 15, 25, 35, 45],future = [10, 20, 30, 40, 50, 15, 25, 35, 45, 55],budget = 150) == 100
    assert candidate(present = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],future = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],budget = 900) == 99
    assert candidate(present = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],future = [15, 25, 35, 45, 60, 75, 85, 95, 105, 115],budget = 300) == 65
    assert candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],budget = 45) == 9
    assert candidate(present = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],future = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],budget = 5) == 2
    assert candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 40, 55, 60],budget = 100) == 35
    assert candidate(present = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],future = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],budget = 200) == 40
    assert candidate(present = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],future = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],budget = 5) == 5
    assert candidate(present = [5, 15, 25, 35, 45],future = [10, 20, 25, 30, 50],budget = 50) == 10
    assert candidate(present = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],future = [110, 100, 90, 80, 70, 60, 50, 40, 30, 20],budget = 500) == 90
    assert candidate(present = [80, 85, 90, 95, 100],future = [100, 105, 110, 115, 120],budget = 350) == 80
    assert candidate(present = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],future = [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],budget = 300) == 45
    assert candidate(present = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],future = [25, 35, 45, 55, 65, 75, 85, 95, 105, 115],budget = 300) == 105
    assert candidate(present = [1, 5, 10, 15, 20],future = [2, 7, 12, 20, 25],budget = 25) == 8
    assert candidate(present = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],future = [55, 55, 55, 55, 55, 55, 55, 55, 55, 55],budget = 200) == 20
    assert candidate(present = [50, 40, 30, 20, 10],future = [60, 50, 40, 30, 20],budget = 150) == 50
    assert candidate(present = [10, 20, 30, 40, 50],future = [15, 25, 35, 45, 55],budget = 100) == 20
    assert candidate(present = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],future = [11, 11, 11, 11, 11, 11, 11, 11, 11, 11],budget = 5) == 50
    assert candidate(present = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],future = [50, 40, 30, 20, 10, 5, 15, 25, 35, 45],budget = 150) == 90
    assert candidate(present = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],future = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],budget = 50) == 7
    assert candidate(present = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],future = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 450) == 250
    assert candidate(present = [50, 40, 30, 20, 10],future = [60, 50, 40, 30, 20],budget = 150) == 50
    assert candidate(present = [10, 10, 10, 10, 10],future = [12, 12, 12, 12, 12],budget = 30) == 6
    assert candidate(present = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],future = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],budget = 5) == 5
    assert candidate(present = [50, 25, 75, 100, 50],future = [75, 50, 100, 150, 75],budget = 200) == 100


