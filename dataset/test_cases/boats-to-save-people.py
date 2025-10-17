def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 11) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 11) == 5: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(people = [3, 2, 2, 1],limit = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [3, 2, 2, 1],limit = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(people = [5, 5, 5, 5, 5],limit = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [5, 5, 5, 5, 5],limit = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(people = [10, 20, 30, 40, 50],limit = 50) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [10, 20, 30, 40, 50],limit = 50) == 3: {e}')
    
    total += 1
    try:
        result = candidate(people = [3, 5, 3, 4],limit = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [3, 5, 3, 4],limit = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2],limit = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2],limit = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(people = [30, 20, 10],limit = 50) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [30, 20, 10],limit = 50) == 2: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 3, 5, 7, 9],limit = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 3, 5, 7, 9],limit = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(people = [3, 2, 3, 2, 2],limit = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [3, 2, 3, 2, 2],limit = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 1, 1, 1, 1, 1],limit = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 1, 1, 1, 1, 1],limit = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(people = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],limit = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],limit = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(people = [10, 20, 30, 40, 50],limit = 60) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [10, 20, 30, 40, 50],limit = 60) == 3: {e}')
    
    total += 1
    try:
        result = candidate(people = [3, 3, 3, 3, 3, 3],limit = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [3, 3, 3, 3, 3, 3],limit = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 3, 4, 5],limit = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 3, 4, 5],limit = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 1, 2, 2, 3, 3],limit = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 1, 2, 2, 3, 3],limit = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18],limit = 19) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18],limit = 19) == 18: {e}')
    
    total += 1
    try:
        result = candidate(people = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],limit = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],limit = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],limit = 30) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],limit = 30) == 16: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92, 9, 91, 10, 90],limit = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92, 9, 91, 10, 90],limit = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],limit = 11) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],limit = 11) == 18: {e}')
    
    total += 1
    try:
        result = candidate(people = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],limit = 6) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],limit = 6) == 10: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],limit = 30) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],limit = 30) == 16: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 10, 100, 1000, 10000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],limit = 10000) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 10, 100, 1000, 10000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],limit = 10000) == 8: {e}')
    
    total += 1
    try:
        result = candidate(people = [15, 20, 15, 25, 30, 35, 5, 10],limit = 40) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [15, 20, 15, 25, 30, 35, 5, 10],limit = 40) == 4: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],limit = 11) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],limit = 11) == 10: {e}')
    
    total += 1
    try:
        result = candidate(people = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],limit = 30) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],limit = 30) == 10: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10],limit = 15) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10],limit = 15) == 26: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 20) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 20) == 16: {e}')
    
    total += 1
    try:
        result = candidate(people = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],limit = 150) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],limit = 150) == 5: {e}')
    
    total += 1
    try:
        result = candidate(people = [29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29],limit = 29) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29],limit = 29) == 20: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 2) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 2) == 49: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],limit = 15) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],limit = 15) == 8: {e}')
    
    total += 1
    try:
        result = candidate(people = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],limit = 150) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],limit = 150) == 5: {e}')
    
    total += 1
    try:
        result = candidate(people = [30, 20, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],limit = 40) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [30, 20, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],limit = 40) == 10: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10],limit = 10) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10],limit = 10) == 34: {e}')
    
    total += 1
    try:
        result = candidate(people = [30000, 30000, 30000, 30000, 30000, 30000, 30000, 30000, 30000, 30000],limit = 30000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [30000, 30000, 30000, 30000, 30000, 30000, 30000, 30000, 30000, 30000],limit = 30000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(people = [20, 40, 20, 40, 10, 30, 20, 10, 50, 30],limit = 60) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [20, 40, 20, 40, 10, 30, 20, 10, 50, 30],limit = 60) == 5: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9],limit = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9],limit = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(people = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],limit = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],limit = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(people = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],limit = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],limit = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(people = [15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000],limit = 30000) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000],limit = 30000) == 8: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(people = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],limit = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],limit = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(people = [30, 40, 50, 20, 10, 60],limit = 80) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [30, 40, 50, 20, 10, 60],limit = 80) == 3: {e}')
    
    total += 1
    try:
        result = candidate(people = [30000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],limit = 30000) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [30000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],limit = 30000) == 11: {e}')
    
    total += 1
    try:
        result = candidate(people = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],limit = 22) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],limit = 22) == 5: {e}')
    
    total += 1
    try:
        result = candidate(people = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],limit = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],limit = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10],limit = 11) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10],limit = 11) == 15: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10],limit = 12) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10],limit = 12) == 6: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],limit = 21) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],limit = 21) == 10: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],limit = 20) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],limit = 20) == 8: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],limit = 26) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],limit = 26) == 13: {e}')
    
    total += 1
    try:
        result = candidate(people = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],limit = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],limit = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(people = [5, 1, 4, 2, 3, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],limit = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [5, 1, 4, 2, 3, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],limit = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(people = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],limit = 80) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],limit = 80) == 10: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],limit = 30) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],limit = 30) == 10: {e}')
    
    total += 1
    try:
        result = candidate(people = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],limit = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],limit = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],limit = 3) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],limit = 3) == 41: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],limit = 21) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],limit = 21) == 10: {e}')
    
    total += 1
    try:
        result = candidate(people = [30, 40, 50, 20, 30, 40, 50, 20, 30, 40, 50],limit = 100) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [30, 40, 50, 20, 30, 40, 50, 20, 30, 40, 50],limit = 100) == 6: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],limit = 16) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],limit = 16) == 8: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],limit = 11) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],limit = 11) == 10: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],limit = 20) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],limit = 20) == 11: {e}')
    
    total += 1
    try:
        result = candidate(people = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],limit = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],limit = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],limit = 6) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],limit = 6) == 11: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 2) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 2) == 67: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9],limit = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9],limit = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(people = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250],limit = 300) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250],limit = 300) == 13: {e}')
    
    total += 1
    try:
        result = candidate(people = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],limit = 190) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],limit = 190) == 5: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17],limit = 18) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17],limit = 18) == 17: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10],limit = 10) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10],limit = 10) == 22: {e}')
    
    total += 1
    try:
        result = candidate(people = [3, 6, 7, 9, 10, 12, 13, 15, 18, 20],limit = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [3, 6, 7, 9, 10, 12, 13, 15, 18, 20],limit = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(people = [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],limit = 25) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],limit = 25) == 11: {e}')
    
    total += 1
    try:
        result = candidate(people = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],limit = 20) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],limit = 20) == 11: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],limit = 25) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],limit = 25) == 13: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],limit = 20) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],limit = 20) == 11: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],limit = 11) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],limit = 11) == 11: {e}')
    
    total += 1
    try:
        result = candidate(people = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],limit = 6) == 133
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],limit = 6) == 133: {e}')
    
    total += 1
    try:
        result = candidate(people = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],limit = 110) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],limit = 110) == 5: {e}')
    
    total += 1
    try:
        result = candidate(people = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],limit = 10) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],limit = 10) == 19: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 2) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 2) == 16: {e}')
    
    total += 1
    try:
        result = candidate(people = [15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000],limit = 30000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000],limit = 30000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(people = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],limit = 30) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],limit = 30) == 11: {e}')
    
    total += 1
    try:
        result = candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],limit = 31) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],limit = 31) == 15: {e}')
    
    total += 1
    try:
        result = candidate(people = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60],limit = 80) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60],limit = 80) == 5: {e}')
    
    total += 1
    try:
        result = candidate(people = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],limit = 25) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(people = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],limit = 25) == 13: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 11) == 5
    assert candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 15) == 5
    assert candidate(people = [3, 2, 2, 1],limit = 3) == 3
    assert candidate(people = [5, 5, 5, 5, 5],limit = 10) == 3
    assert candidate(people = [10, 20, 30, 40, 50],limit = 50) == 3
    assert candidate(people = [3, 5, 3, 4],limit = 5) == 4
    assert candidate(people = [1, 2],limit = 3) == 1
    assert candidate(people = [30, 20, 10],limit = 50) == 2
    assert candidate(people = [1, 3, 5, 7, 9],limit = 10) == 3
    assert candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 2) == 5
    assert candidate(people = [3, 2, 3, 2, 2],limit = 6) == 3
    assert candidate(people = [1, 1, 1, 1, 1, 1],limit = 2) == 3
    assert candidate(people = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],limit = 10) == 5
    assert candidate(people = [10, 20, 30, 40, 50],limit = 60) == 3
    assert candidate(people = [3, 3, 3, 3, 3, 3],limit = 6) == 3
    assert candidate(people = [1, 2, 3, 4, 5],limit = 5) == 3
    assert candidate(people = [1, 1, 2, 2, 3, 3],limit = 4) == 3
    assert candidate(people = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18],limit = 19) == 18
    assert candidate(people = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],limit = 10) == 5
    assert candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],limit = 30) == 16
    assert candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 2) == 15
    assert candidate(people = [1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92, 9, 91, 10, 90],limit = 100) == 10
    assert candidate(people = [1, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],limit = 11) == 18
    assert candidate(people = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],limit = 6) == 10
    assert candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],limit = 30) == 16
    assert candidate(people = [1, 10, 100, 1000, 10000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],limit = 10000) == 8
    assert candidate(people = [15, 20, 15, 25, 30, 35, 5, 10],limit = 40) == 4
    assert candidate(people = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],limit = 11) == 10
    assert candidate(people = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],limit = 30) == 10
    assert candidate(people = [1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10],limit = 15) == 26
    assert candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 20) == 16
    assert candidate(people = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],limit = 150) == 5
    assert candidate(people = [29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29],limit = 29) == 20
    assert candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 2) == 49
    assert candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],limit = 15) == 8
    assert candidate(people = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],limit = 150) == 5
    assert candidate(people = [30, 20, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],limit = 40) == 10
    assert candidate(people = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10],limit = 10) == 34
    assert candidate(people = [30000, 30000, 30000, 30000, 30000, 30000, 30000, 30000, 30000, 30000],limit = 30000) == 10
    assert candidate(people = [20, 40, 20, 40, 10, 30, 20, 10, 50, 30],limit = 60) == 5
    assert candidate(people = [1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9],limit = 10) == 15
    assert candidate(people = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],limit = 6) == 8
    assert candidate(people = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],limit = 6) == 8
    assert candidate(people = [15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000],limit = 30000) == 8
    assert candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 2) == 10
    assert candidate(people = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],limit = 4) == 10
    assert candidate(people = [30, 40, 50, 20, 10, 60],limit = 80) == 3
    assert candidate(people = [30000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],limit = 30000) == 11
    assert candidate(people = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],limit = 22) == 5
    assert candidate(people = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],limit = 5) == 20
    assert candidate(people = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10],limit = 11) == 15
    assert candidate(people = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10],limit = 12) == 6
    assert candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],limit = 21) == 10
    assert candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],limit = 20) == 8
    assert candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],limit = 26) == 13
    assert candidate(people = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],limit = 10) == 15
    assert candidate(people = [5, 1, 4, 2, 3, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],limit = 10) == 8
    assert candidate(people = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],limit = 80) == 10
    assert candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],limit = 30) == 10
    assert candidate(people = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],limit = 10) == 8
    assert candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],limit = 3) == 41
    assert candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],limit = 21) == 10
    assert candidate(people = [30, 40, 50, 20, 30, 40, 50, 20, 30, 40, 50],limit = 100) == 6
    assert candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],limit = 16) == 8
    assert candidate(people = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],limit = 11) == 10
    assert candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],limit = 20) == 11
    assert candidate(people = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],limit = 10) == 8
    assert candidate(people = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],limit = 6) == 11
    assert candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 2) == 67
    assert candidate(people = [1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9],limit = 10) == 10
    assert candidate(people = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250],limit = 300) == 13
    assert candidate(people = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],limit = 190) == 5
    assert candidate(people = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17],limit = 18) == 17
    assert candidate(people = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10],limit = 10) == 22
    assert candidate(people = [3, 6, 7, 9, 10, 12, 13, 15, 18, 20],limit = 25) == 5
    assert candidate(people = [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],limit = 25) == 11
    assert candidate(people = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],limit = 20) == 11
    assert candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],limit = 25) == 13
    assert candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],limit = 20) == 11
    assert candidate(people = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],limit = 11) == 11
    assert candidate(people = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],limit = 6) == 133
    assert candidate(people = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],limit = 110) == 5
    assert candidate(people = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],limit = 10) == 19
    assert candidate(people = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 2) == 16
    assert candidate(people = [15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000],limit = 30000) == 10
    assert candidate(people = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],limit = 30) == 11
    assert candidate(people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],limit = 31) == 15
    assert candidate(people = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60],limit = 80) == 5
    assert candidate(people = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],limit = 25) == 13


