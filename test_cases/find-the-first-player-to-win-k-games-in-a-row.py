def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(skills = [5, 1, 9, 2, 8, 3, 7, 4, 6],k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [5, 1, 9, 2, 8, 3, 7, 4, 6],k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1000000, 999999, 999998, 999997],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1000000, 999999, 999998, 999997],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [2, 5, 4],k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [2, 5, 4],k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 3, 2, 5, 4],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 3, 2, 5, 4],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(skills = [10, 20, 30, 40, 50],k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [10, 20, 30, 40, 50],k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(skills = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1000000, 1, 2, 3, 4],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1000000, 1, 2, 3, 4],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [5, 10, 15, 20, 25, 30],k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [5, 10, 15, 20, 25, 30],k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(skills = [50, 40, 30, 20, 10],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [50, 40, 30, 20, 10],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [4, 2, 6, 3, 9],k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [4, 2, 6, 3, 9],k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(skills = [5, 4, 3, 2, 1],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [5, 4, 3, 2, 1],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 3, 5, 7, 9],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 3, 5, 7, 9],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [3, 1, 2, 5, 4, 6, 7],k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [3, 1, 2, 5, 4, 6, 7],k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(skills = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(skills = [2, 1, 5, 4, 3, 6],k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [2, 1, 5, 4, 3, 6],k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(skills = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9],k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9],k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(skills = [9, 1, 8, 2, 7, 3, 6, 4, 5, 10],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [9, 1, 8, 2, 7, 3, 6, 4, 5, 10],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [500, 400, 300, 200, 100, 600, 700, 800, 900, 1000],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [500, 400, 300, 200, 100, 600, 700, 800, 900, 1000],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 19) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 19) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9],k = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9],k = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 10) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 10) == 14: {e}')
    
    total += 1
    try:
        result = candidate(skills = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 100000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 100000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1000, 100, 10, 1],k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1000, 100, 10, 1],k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [5, 1, 9, 2, 8, 3, 7, 4, 6, 10],k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [5, 1, 9, 2, 8, 3, 7, 4, 6, 10],k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(skills = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 7) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 7) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [5, 3, 1, 4, 2],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [5, 3, 1, 4, 2],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019],k = 10) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019],k = 10) == 19: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 10, 3, 4, 7, 5, 6, 9, 8, 2],k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 10, 3, 4, 7, 5, 6, 9, 8, 2],k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(skills = [8, 4, 6, 2, 7, 3, 9, 1, 5, 10],k = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [8, 4, 6, 2, 7, 3, 9, 1, 5, 10],k = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 10, 3, 8, 5, 6, 7, 2, 4, 9],k = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 10, 3, 8, 5, 6, 7, 2, 4, 9],k = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(skills = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9],k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9],k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(skills = [50, 51, 48, 49, 46, 47, 44, 45, 42, 43, 40, 41, 38, 39, 36, 37, 34, 35, 32, 33],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [50, 51, 48, 49, 46, 47, 44, 45, 42, 43, 40, 41, 38, 39, 36, 37, 34, 35, 32, 33],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [3, 1, 2, 5, 4, 7, 6, 9, 8, 10],k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [3, 1, 2, 5, 4, 7, 6, 9, 8, 10],k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [100000, 99999, 99998, 99997, 99996],k = 100000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [100000, 99999, 99998, 99997, 99996],k = 100000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [23, 45, 12, 56, 89, 43, 21, 67, 8, 90],k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [23, 45, 12, 56, 89, 43, 21, 67, 8, 90],k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(skills = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],k = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],k = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [10, 2, 15, 3, 20, 5, 25, 7, 30, 9],k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [10, 2, 15, 3, 20, 5, 25, 7, 30, 9],k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 1000000],k = 1000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 1000000],k = 1000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(skills = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [500000, 500001, 500002, 500003, 500004, 500005, 500006, 500007, 500008, 500009],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [500000, 500001, 500002, 500003, 500004, 500005, 500006, 500007, 500008, 500009],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(skills = [8, 7, 6, 5, 4, 3, 2, 1],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [8, 7, 6, 5, 4, 3, 2, 1],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [7, 6, 5, 4, 3, 2, 1],k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [7, 6, 5, 4, 3, 2, 1],k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 10) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 10) == 14: {e}')
    
    total += 1
    try:
        result = candidate(skills = [2, 3, 1, 5, 4],k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [2, 3, 1, 5, 4],k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(skills = [20, 30, 10, 40, 50, 60, 70, 80, 90, 100],k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [20, 30, 10, 40, 50, 60, 70, 80, 90, 100],k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11],k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11],k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [999999, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [999999, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [9, 1, 2, 8, 3, 7, 4, 6, 5, 10],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [9, 1, 2, 8, 3, 7, 4, 6, 5, 10],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 50, 40, 30, 20, 10],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 50, 40, 30, 20, 10],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 3, 2, 4, 6, 5, 7, 9, 8, 10],k = 7) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 3, 2, 4, 6, 5, 7, 9, 8, 10],k = 7) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 12) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 12) == 13: {e}')
    
    total += 1
    try:
        result = candidate(skills = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],k = 8) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],k = 8) == 14: {e}')
    
    total += 1
    try:
        result = candidate(skills = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 19: {e}')
    
    total += 1
    try:
        result = candidate(skills = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],k = 8) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],k = 8) == 5: {e}')
    
    total += 1
    try:
        result = candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 10) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 10) == 19: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],k = 999990) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],k = 999990) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == 14: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95],k = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95],k = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 19: {e}')
    
    total += 1
    try:
        result = candidate(skills = [500, 250, 750, 125, 875, 375, 625, 687, 937, 187, 437, 787, 287, 1125, 1062],k = 7) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [500, 250, 750, 125, 875, 375, 625, 687, 937, 187, 437, 787, 287, 1125, 1062],k = 7) == 13: {e}')
    
    total += 1
    try:
        result = candidate(skills = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1000000, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1000000, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(skills = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],k = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],k = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 20) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 20) == 19: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 1, 1, 1, 1, 1, 1, 1, 1, 100],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 1, 1, 1, 1, 1, 1, 1, 1, 100],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [3, 1, 2, 5, 4, 8, 7, 10, 9, 6],k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [3, 1, 2, 5, 4, 8, 7, 10, 9, 6],k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],k = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],k = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [5, 3, 8, 1, 9, 2, 7, 4, 6, 10],k = 7) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [5, 3, 8, 1, 9, 2, 7, 4, 6, 10],k = 7) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91],k = 90) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91],k = 90) == 1: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1000, 100, 10, 1, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 8) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1000, 100, 10, 1, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 8) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 1],k = 9) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 1],k = 9) == 8: {e}')
    
    total += 1
    try:
        result = candidate(skills = [32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [9, 3, 1, 7, 5, 2, 8, 6, 4, 10],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [9, 3, 1, 7, 5, 2, 8, 6, 4, 10],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [3, 1, 2, 5, 4, 6],k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [3, 1, 2, 5, 4, 6],k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],k = 6) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],k = 6) == 13: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 25) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 25) == 29: {e}')
    
    total += 1
    try:
        result = candidate(skills = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == 19: {e}')
    
    total += 1
    try:
        result = candidate(skills = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [4, 1, 3, 2, 5, 7, 6, 8, 10, 9],k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [4, 1, 3, 2, 5, 7, 6, 8, 10, 9],k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(skills = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],k = 8) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],k = 8) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(skills = [7, 3, 9, 2, 8, 4, 6, 1, 5],k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [7, 3, 9, 2, 8, 4, 6, 1, 5],k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(skills = [200, 150, 300, 100, 250, 400, 50, 350, 500],k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [200, 150, 300, 100, 250, 400, 50, 350, 500],k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [100, 101, 99, 102, 98, 103, 97, 104, 96, 105],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [100, 101, 99, 102, 98, 103, 97, 104, 96, 105],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [10, 2, 8, 4, 6, 1, 3, 5, 7, 9],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [10, 2, 8, 4, 6, 1, 3, 5, 7, 9],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 100) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 100) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(skills = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29],k = 15) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29],k = 15) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],k = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],k = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 14: {e}')
    
    total += 1
    try:
        result = candidate(skills = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(skills = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 3) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(skills = [5, 1, 9, 2, 8, 3, 7, 4, 6],k = 3) == 2
    assert candidate(skills = [1000000, 999999, 999998, 999997],k = 4) == 0
    assert candidate(skills = [2, 5, 4],k = 3) == 1
    assert candidate(skills = [1, 3, 2, 5, 4],k = 1) == 1
    assert candidate(skills = [10, 20, 30, 40, 50],k = 5) == 4
    assert candidate(skills = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 0
    assert candidate(skills = [1000000, 1, 2, 3, 4],k = 4) == 0
    assert candidate(skills = [5, 10, 15, 20, 25, 30],k = 2) == 5
    assert candidate(skills = [50, 40, 30, 20, 10],k = 4) == 0
    assert candidate(skills = [4, 2, 6, 3, 9],k = 2) == 2
    assert candidate(skills = [5, 4, 3, 2, 1],k = 5) == 0
    assert candidate(skills = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 9
    assert candidate(skills = [1, 3, 5, 7, 9],k = 1) == 1
    assert candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 9) == 9
    assert candidate(skills = [3, 1, 2, 5, 4, 6, 7],k = 3) == 6
    assert candidate(skills = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 8) == 0
    assert candidate(skills = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],k = 3) == 4
    assert candidate(skills = [2, 1, 5, 4, 3, 6],k = 2) == 2
    assert candidate(skills = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9],k = 2) == 4
    assert candidate(skills = [9, 1, 8, 2, 7, 3, 6, 4, 5, 10],k = 3) == 0
    assert candidate(skills = [500, 400, 300, 200, 100, 600, 700, 800, 900, 1000],k = 4) == 0
    assert candidate(skills = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 19) == 0
    assert candidate(skills = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9],k = 10) == 8
    assert candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 10) == 14
    assert candidate(skills = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 5) == 9
    assert candidate(skills = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 100000) == 9
    assert candidate(skills = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 5) == 5
    assert candidate(skills = [1000, 100, 10, 1],k = 100) == 0
    assert candidate(skills = [5, 1, 9, 2, 8, 3, 7, 4, 6, 10],k = 5) == 2
    assert candidate(skills = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 0
    assert candidate(skills = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 7) == 9
    assert candidate(skills = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 0
    assert candidate(skills = [5, 3, 1, 4, 2],k = 3) == 0
    assert candidate(skills = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 5) == 0
    assert candidate(skills = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019],k = 10) == 19
    assert candidate(skills = [1, 10, 3, 4, 7, 5, 6, 9, 8, 2],k = 4) == 1
    assert candidate(skills = [8, 4, 6, 2, 7, 3, 9, 1, 5, 10],k = 9) == 9
    assert candidate(skills = [1, 10, 3, 8, 5, 6, 7, 2, 4, 9],k = 7) == 1
    assert candidate(skills = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9],k = 4) == 8
    assert candidate(skills = [50, 51, 48, 49, 46, 47, 44, 45, 42, 43, 40, 41, 38, 39, 36, 37, 34, 35, 32, 33],k = 10) == 1
    assert candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 9
    assert candidate(skills = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 9
    assert candidate(skills = [3, 1, 2, 5, 4, 7, 6, 9, 8, 10],k = 3) == 9
    assert candidate(skills = [100000, 99999, 99998, 99997, 99996],k = 100000) == 0
    assert candidate(skills = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 0
    assert candidate(skills = [1000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1000000) == 0
    assert candidate(skills = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 0
    assert candidate(skills = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],k = 5) == 9
    assert candidate(skills = [23, 45, 12, 56, 89, 43, 21, 67, 8, 90],k = 5) == 4
    assert candidate(skills = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],k = 2) == 9
    assert candidate(skills = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 3) == 5
    assert candidate(skills = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],k = 5) == 0
    assert candidate(skills = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 10) == 0
    assert candidate(skills = [10, 2, 15, 3, 20, 5, 25, 7, 30, 9],k = 5) == 8
    assert candidate(skills = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],k = 5) == 0
    assert candidate(skills = [1, 1000000],k = 1000000) == 1
    assert candidate(skills = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 100) == 0
    assert candidate(skills = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 9) == 0
    assert candidate(skills = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15],k = 5) == 0
    assert candidate(skills = [500000, 500001, 500002, 500003, 500004, 500005, 500006, 500007, 500008, 500009],k = 5) == 9
    assert candidate(skills = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 9
    assert candidate(skills = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],k = 5) == 4
    assert candidate(skills = [8, 7, 6, 5, 4, 3, 2, 1],k = 7) == 0
    assert candidate(skills = [7, 6, 5, 4, 3, 2, 1],k = 6) == 0
    assert candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 10) == 14
    assert candidate(skills = [2, 3, 1, 5, 4],k = 4) == 3
    assert candidate(skills = [20, 30, 10, 40, 50, 60, 70, 80, 90, 100],k = 3) == 9
    assert candidate(skills = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11],k = 8) == 0
    assert candidate(skills = [999999, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 9) == 0
    assert candidate(skills = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90],k = 10) == 0
    assert candidate(skills = [9, 1, 2, 8, 3, 7, 4, 6, 5, 10],k = 4) == 0
    assert candidate(skills = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 50, 40, 30, 20, 10],k = 5) == 9
    assert candidate(skills = [1, 3, 2, 4, 6, 5, 7, 9, 8, 10],k = 7) == 9
    assert candidate(skills = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 12) == 13
    assert candidate(skills = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],k = 8) == 14
    assert candidate(skills = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10],k = 5) == 9
    assert candidate(skills = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 19
    assert candidate(skills = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],k = 8) == 5
    assert candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 10) == 19
    assert candidate(skills = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],k = 999990) == 0
    assert candidate(skills = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == 14
    assert candidate(skills = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95],k = 6) == 1
    assert candidate(skills = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 9
    assert candidate(skills = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 19
    assert candidate(skills = [500, 250, 750, 125, 875, 375, 625, 687, 937, 187, 437, 787, 287, 1125, 1062],k = 7) == 13
    assert candidate(skills = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 0
    assert candidate(skills = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5],k = 5) == 0
    assert candidate(skills = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2],k = 1) == 0
    assert candidate(skills = [1000000, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 1) == 0
    assert candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1) == 1
    assert candidate(skills = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],k = 6) == 5
    assert candidate(skills = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 20) == 19
    assert candidate(skills = [1, 1, 1, 1, 1, 1, 1, 1, 1, 100],k = 1) == 0
    assert candidate(skills = [3, 1, 2, 5, 4, 8, 7, 10, 9, 6],k = 3) == 7
    assert candidate(skills = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],k = 10) == 9
    assert candidate(skills = [5, 3, 8, 1, 9, 2, 7, 4, 6, 10],k = 7) == 9
    assert candidate(skills = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91],k = 90) == 1
    assert candidate(skills = [1000, 100, 10, 1, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 8) == 9
    assert candidate(skills = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],k = 6) == 0
    assert candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1) == 1
    assert candidate(skills = [10, 20, 30, 40, 50, 60, 70, 80, 90, 1],k = 9) == 8
    assert candidate(skills = [32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4],k = 7) == 0
    assert candidate(skills = [9, 3, 1, 7, 5, 2, 8, 6, 4, 10],k = 5) == 0
    assert candidate(skills = [3, 1, 2, 5, 4, 6],k = 3) == 5
    assert candidate(skills = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 4) == 1
    assert candidate(skills = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],k = 6) == 13
    assert candidate(skills = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 25) == 29
    assert candidate(skills = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],k = 9) == 0
    assert candidate(skills = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],k = 1) == 0
    assert candidate(skills = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == 19
    assert candidate(skills = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 9
    assert candidate(skills = [4, 1, 3, 2, 5, 7, 6, 8, 10, 9],k = 4) == 8
    assert candidate(skills = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 9) == 9
    assert candidate(skills = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],k = 8) == 1
    assert candidate(skills = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],k = 8) == 9
    assert candidate(skills = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 0
    assert candidate(skills = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],k = 5) == 1
    assert candidate(skills = [7, 3, 9, 2, 8, 4, 6, 1, 5],k = 3) == 2
    assert candidate(skills = [200, 150, 300, 100, 250, 400, 50, 350, 500],k = 5) == 8
    assert candidate(skills = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 9
    assert candidate(skills = [100, 101, 99, 102, 98, 103, 97, 104, 96, 105],k = 5) == 9
    assert candidate(skills = [10, 2, 8, 4, 6, 1, 3, 5, 7, 9],k = 3) == 0
    assert candidate(skills = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 100) == 9
    assert candidate(skills = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 0
    assert candidate(skills = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29],k = 15) == 9
    assert candidate(skills = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],k = 10) == 9
    assert candidate(skills = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 14
    assert candidate(skills = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 3) == 1


