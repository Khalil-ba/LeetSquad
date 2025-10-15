def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(costs = [1, 3, 2, 4, 1],coins = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 3, 2, 4, 1],coins = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(costs = [10, 6, 8, 7, 7, 8],coins = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [10, 6, 8, 7, 7, 8],coins = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1],coins = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1],coins = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 6, 3, 1, 2, 5],coins = 20) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 6, 3, 1, 2, 5],coins = 20) == 6: {e}')
    
    total += 1
    try:
        result = candidate(costs = [100000],coins = 100000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [100000],coins = 100000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = 55) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = 55) == 10: {e}')
    
    total += 1
    try:
        result = candidate(costs = [5, 5, 5, 5, 5],coins = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [5, 5, 5, 5, 5],coins = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(costs = [10, 20, 30, 40, 50],coins = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [10, 20, 30, 40, 50],coins = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = 50) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = 50) == 9: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 19) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 19) == 19: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],coins = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],coins = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(costs = [5, 4, 2, 3, 1, 6, 7, 8, 9, 10],coins = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [5, 4, 2, 3, 1, 6, 7, 8, 9, 10],coins = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = 250) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = 250) == 6: {e}')
    
    total += 1
    try:
        result = candidate(costs = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],coins = 25) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],coins = 25) == 12: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = 210) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = 210) == 20: {e}')
    
    total += 1
    try:
        result = candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = 55) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = 55) == 2: {e}')
    
    total += 1
    try:
        result = candidate(costs = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],coins = 40) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],coins = 40) == 8: {e}')
    
    total += 1
    try:
        result = candidate(costs = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],coins = 100) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],coins = 100) == 13: {e}')
    
    total += 1
    try:
        result = candidate(costs = [100000, 99999, 99998, 99997, 99996, 99995],coins = 599985) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [100000, 99999, 99998, 99997, 99996, 99995],coins = 599985) == 6: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],coins = 50) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],coins = 50) == 13: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5, 999996],coins = 1000000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5, 999996],coins = 1000000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(costs = [50, 25, 75, 100, 200, 300, 400, 500, 600, 700],coins = 2000) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [50, 25, 75, 100, 200, 300, 400, 500, 600, 700],coins = 2000) == 8: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],coins = 800) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],coins = 800) == 12: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5, 999996],coins = 5000000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5, 999996],coins = 5000000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(costs = [5, 1, 4, 2, 3],coins = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [5, 1, 4, 2, 3],coins = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1],coins = 1000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1],coins = 1000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(costs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],coins = 8000) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],coins = 8000) == 12: {e}')
    
    total += 1
    try:
        result = candidate(costs = [5, 7, 8, 6, 3, 2, 1, 4, 9, 10],coins = 20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [5, 7, 8, 6, 3, 2, 1, 4, 9, 10],coins = 20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(costs = [50, 20, 30, 10, 40],coins = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [50, 20, 30, 10, 40],coins = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = 1000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = 1000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(costs = [100000, 100000, 100000, 100000, 100000],coins = 500000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [100000, 100000, 100000, 100000, 100000],coins = 500000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(costs = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],coins = 50) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],coins = 50) == 5: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],coins = 300) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],coins = 300) == 24: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],coins = 25) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],coins = 25) == 6: {e}')
    
    total += 1
    try:
        result = candidate(costs = [99999, 1, 99999, 1, 99999, 1, 99999, 1, 99999, 1],coins = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [99999, 1, 99999, 1, 99999, 1, 99999, 1, 99999, 1],coins = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],coins = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],coins = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = 50) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = 50) == 9: {e}')
    
    total += 1
    try:
        result = candidate(costs = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],coins = 50) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],coins = 50) == 10: {e}')
    
    total += 1
    try:
        result = candidate(costs = [9, 8, 7, 6, 5, 4, 3, 2, 1],coins = 25) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [9, 8, 7, 6, 5, 4, 3, 2, 1],coins = 25) == 6: {e}')
    
    total += 1
    try:
        result = candidate(costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],coins = 55) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],coins = 55) == 10: {e}')
    
    total += 1
    try:
        result = candidate(costs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],coins = 1500) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],coins = 1500) == 5: {e}')
    
    total += 1
    try:
        result = candidate(costs = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],coins = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],coins = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(costs = [5, 1, 3, 1, 2, 5, 3, 1, 2, 5],coins = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [5, 1, 3, 1, 2, 5, 3, 1, 2, 5],coins = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(costs = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],coins = 55) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],coins = 55) == 2: {e}')
    
    total += 1
    try:
        result = candidate(costs = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],coins = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],coins = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 3, 2, 4, 1, 3, 2, 4, 1, 3, 2, 4, 1, 3, 2, 4, 1, 3, 2, 4],coins = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 3, 2, 4, 1, 3, 2, 4, 1, 3, 2, 4, 1, 3, 2, 4, 1, 3, 2, 4],coins = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = 550) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = 550) == 10: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = 190) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = 190) == 19: {e}')
    
    total += 1
    try:
        result = candidate(costs = [3, 1, 2, 1, 4, 2, 2, 3, 2, 1, 2, 3, 4, 1, 2],coins = 20) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [3, 1, 2, 1, 4, 2, 2, 3, 2, 1, 2, 3, 4, 1, 2],coins = 20) == 11: {e}')
    
    total += 1
    try:
        result = candidate(costs = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],coins = 300) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],coins = 300) == 10: {e}')
    
    total += 1
    try:
        result = candidate(costs = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31],coins = 100) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31],coins = 100) == 8: {e}')
    
    total += 1
    try:
        result = candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],coins = 1000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],coins = 1000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(costs = [100000, 1, 100000, 1, 100000, 1, 100000],coins = 100003) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [100000, 1, 100000, 1, 100000, 1, 100000],coins = 100003) == 4: {e}')
    
    total += 1
    try:
        result = candidate(costs = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],coins = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],coins = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(costs = [5, 1, 3, 2, 4, 1],coins = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [5, 1, 3, 2, 4, 1],coins = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(costs = [5, 3, 3, 2, 7, 8, 9],coins = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [5, 3, 3, 2, 7, 8, 9],coins = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(costs = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],coins = 500000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],coins = 500000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = 100) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = 100) == 13: {e}')
    
    total += 1
    try:
        result = candidate(costs = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999],coins = 1000000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999],coins = 1000000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(costs = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],coins = 150000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],coins = 150000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(costs = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],coins = 250) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],coins = 250) == 18: {e}')
    
    total += 1
    try:
        result = candidate(costs = [5, 2, 3, 1, 4, 2, 3, 5, 1, 2],coins = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [5, 2, 3, 1, 4, 2, 3, 5, 1, 2],coins = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(costs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],coins = 2500) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],coins = 2500) == 6: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = 30) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = 30) == 7: {e}')
    
    total += 1
    try:
        result = candidate(costs = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],coins = 60) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],coins = 60) == 10: {e}')
    
    total += 1
    try:
        result = candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],coins = 100) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],coins = 100) == 13: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(costs = [1, 3, 2, 4, 1],coins = 7) == 4
    assert candidate(costs = [10, 6, 8, 7, 7, 8],coins = 5) == 0
    assert candidate(costs = [1],coins = 1) == 1
    assert candidate(costs = [1, 6, 3, 1, 2, 5],coins = 20) == 6
    assert candidate(costs = [100000],coins = 100000) == 1
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = 10) == 4
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = 55) == 10
    assert candidate(costs = [5, 5, 5, 5, 5],coins = 15) == 3
    assert candidate(costs = [10, 20, 30, 40, 50],coins = 100) == 4
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = 15) == 5
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = 50) == 9
    assert candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 19) == 19
    assert candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 5) == 5
    assert candidate(costs = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],coins = 15) == 6
    assert candidate(costs = [5, 4, 2, 3, 1, 6, 7, 8, 9, 10],coins = 15) == 5
    assert candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = 250) == 6
    assert candidate(costs = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],coins = 25) == 12
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = 210) == 20
    assert candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = 55) == 2
    assert candidate(costs = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],coins = 40) == 8
    assert candidate(costs = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],coins = 100) == 13
    assert candidate(costs = [100000, 99999, 99998, 99997, 99996, 99995],coins = 599985) == 6
    assert candidate(costs = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],coins = 50) == 13
    assert candidate(costs = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5, 999996],coins = 1000000) == 5
    assert candidate(costs = [50, 25, 75, 100, 200, 300, 400, 500, 600, 700],coins = 2000) == 8
    assert candidate(costs = [1, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 10) == 10
    assert candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],coins = 800) == 12
    assert candidate(costs = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5, 999996],coins = 5000000) == 9
    assert candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 10) == 10
    assert candidate(costs = [5, 1, 4, 2, 3],coins = 10) == 4
    assert candidate(costs = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1],coins = 1000) == 9
    assert candidate(costs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],coins = 8000) == 12
    assert candidate(costs = [5, 7, 8, 6, 3, 2, 1, 4, 9, 10],coins = 20) == 5
    assert candidate(costs = [50, 20, 30, 10, 40],coins = 100) == 4
    assert candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = 1000) == 10
    assert candidate(costs = [100000, 100000, 100000, 100000, 100000],coins = 500000) == 5
    assert candidate(costs = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],coins = 50) == 5
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],coins = 300) == 24
    assert candidate(costs = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],coins = 25) == 6
    assert candidate(costs = [99999, 1, 99999, 1, 99999, 1, 99999, 1, 99999, 1],coins = 5) == 5
    assert candidate(costs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],coins = 20) == 4
    assert candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 10) == 10
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = 50) == 9
    assert candidate(costs = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],coins = 50) == 10
    assert candidate(costs = [9, 8, 7, 6, 5, 4, 3, 2, 1],coins = 25) == 6
    assert candidate(costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],coins = 55) == 10
    assert candidate(costs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],coins = 1500) == 5
    assert candidate(costs = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],coins = 15) == 7
    assert candidate(costs = [5, 1, 3, 1, 2, 5, 3, 1, 2, 5],coins = 15) == 7
    assert candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 10) == 10
    assert candidate(costs = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],coins = 55) == 2
    assert candidate(costs = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],coins = 20) == 4
    assert candidate(costs = [1, 3, 2, 4, 1, 3, 2, 4, 1, 3, 2, 4, 1, 3, 2, 4, 1, 3, 2, 4],coins = 10) == 7
    assert candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = 550) == 10
    assert candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 10) == 10
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = 190) == 19
    assert candidate(costs = [3, 1, 2, 1, 4, 2, 2, 3, 2, 1, 2, 3, 4, 1, 2],coins = 20) == 11
    assert candidate(costs = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],coins = 300) == 10
    assert candidate(costs = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31],coins = 100) == 8
    assert candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],coins = 1000) == 13
    assert candidate(costs = [100000, 1, 100000, 1, 100000, 1, 100000],coins = 100003) == 4
    assert candidate(costs = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],coins = 100) == 10
    assert candidate(costs = [5, 1, 3, 2, 4, 1],coins = 10) == 4
    assert candidate(costs = [5, 3, 3, 2, 7, 8, 9],coins = 15) == 4
    assert candidate(costs = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],coins = 500000) == 9
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = 100) == 13
    assert candidate(costs = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999],coins = 1000000) == 10
    assert candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = 5) == 5
    assert candidate(costs = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],coins = 150000) == 9
    assert candidate(costs = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],coins = 250) == 18
    assert candidate(costs = [5, 2, 3, 1, 4, 2, 3, 5, 1, 2],coins = 15) == 7
    assert candidate(costs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],coins = 2500) == 6
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = 30) == 7
    assert candidate(costs = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],coins = 60) == 10
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],coins = 100) == 13


