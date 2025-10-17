def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(instructions = [100000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [100000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [50000, 50001, 50002, 50003, 50004, 50005, 50006, 50007, 50008, 50009]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [50000, 50001, 50002, 50003, 50004, 50005, 50006, 50007, 50008, 50009]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 3, 6, 5, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 3, 6, 5, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 5, 6, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 5, 6, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 3, 3, 3, 2, 4, 2, 1, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 3, 3, 3, 2, 4, 2, 1, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [5, 1, 3, 2, 4, 6, 8, 7, 10, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [5, 1, 3, 2, 4, 6, 8, 7, 10, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [100000, 1, 100000, 2, 100000, 3, 100000, 4, 100000, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [100000, 1, 100000, 2, 100000, 3, 100000, 4, 100000, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [50000, 40000, 30000, 20000, 10000, 60000, 70000, 80000, 90000, 100000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [50000, 40000, 30000, 20000, 10000, 60000, 70000, 80000, 90000, 100000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [5, 3, 8, 6, 2, 7, 4, 1, 10, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [5, 3, 8, 6, 2, 7, 4, 1, 10, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [9, 3, 8, 3, 7, 3, 6, 3, 5, 3, 4, 3, 2, 3, 1, 3]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [9, 3, 8, 3, 7, 3, 6, 3, 5, 3, 4, 3, 2, 3, 1, 3]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 3, 6, 5, 4, 1, 2, 3, 6, 5, 4]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 3, 6, 5, 4, 1, 2, 3, 6, 5, 4]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 3, 2, 6, 5, 4, 9, 8, 7, 10, 1, 3, 2, 6, 5, 4, 9, 8, 7, 10, 1, 3, 2, 6, 5, 4, 9, 8, 7, 10]) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 3, 2, 6, 5, 4, 9, 8, 7, 10, 1, 3, 2, 6, 5, 4, 9, 8, 7, 10, 1, 3, 2, 6, 5, 4, 9, 8, 7, 10]) == 88: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [10, 20, 30, 40, 50, 40, 30, 20, 10, 10, 20, 30, 40, 50, 40, 30, 20, 10]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [10, 20, 30, 40, 50, 40, 30, 20, 10, 10, 20, 30, 40, 50, 40, 30, 20, 10]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [100000, 99999, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [100000, 99999, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996, 6, 99995, 7, 99994, 8, 99993]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996, 6, 99995, 7, 99994, 8, 99993]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [5, 1, 3, 2, 4, 6, 8, 7, 10, 9, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [5, 1, 3, 2, 4, 6, 8, 7, 10, 9, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 3, 2, 4, 2, 3, 1, 4, 2, 3]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 3, 2, 4, 2, 3, 1, 4, 2, 3]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [3, 1, 2, 5, 4, 6, 9, 7, 10, 8]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [3, 1, 2, 5, 4, 6, 9, 7, 10, 8]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [50000, 50001, 50002, 50003, 50004, 50005, 50006, 50007, 50008, 50009, 50000, 50001, 50002, 50003, 50004, 50005, 50006, 50007, 50008, 50009]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [50000, 50001, 50002, 50003, 50004, 50005, 50006, 50007, 50008, 50009, 50000, 50001, 50002, 50003, 50004, 50005, 50006, 50007, 50008, 50009]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [100000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [100000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 317
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 317: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [100000, 50000, 75000, 25000, 62500, 37500, 87500, 12500, 93750, 43750, 68750, 31250, 81250, 18750, 90625, 46875, 71875, 28125, 89062, 40625, 65625, 34375, 84375, 21875, 82812, 45312, 70312, 29687, 88281, 49218, 74218, 32187, 86171, 42187, 67187, 35156, 83125, 23437, 85937, 50312, 75312, 37812, 81562, 44531, 69531, 33437, 87968, 47968, 72968, 30937, 90468, 52968, 77968, 38906, 85468, 55468, 80468, 43437, 92460, 57460, 82460, 47460, 91718, 61718, 86718, 52656, 94359, 66359, 91359, 57359, 93671, 69671, 94671, 73671, 86913, 64406, 93406, 68406, 92406, 65406, 95507, 70507, 90507, 67507, 92753, 75253, 87753, 62753, 94753, 78753, 83753, 71753, 88281, 53281, 88281, 58281, 83281, 50281, 81281, 45281, 86281, 51281, 82281, 46281, 84281, 48281, 85281, 50281, 87281, 52281, 89281, 54281, 90281, 56281, 91281, 58281, 92281, 60281, 93281, 62281, 94281, 64281, 95281, 66281, 96281, 68281, 97281, 70281, 98281, 72281, 99281, 74281, 100000]) == 2291
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [100000, 50000, 75000, 25000, 62500, 37500, 87500, 12500, 93750, 43750, 68750, 31250, 81250, 18750, 90625, 46875, 71875, 28125, 89062, 40625, 65625, 34375, 84375, 21875, 82812, 45312, 70312, 29687, 88281, 49218, 74218, 32187, 86171, 42187, 67187, 35156, 83125, 23437, 85937, 50312, 75312, 37812, 81562, 44531, 69531, 33437, 87968, 47968, 72968, 30937, 90468, 52968, 77968, 38906, 85468, 55468, 80468, 43437, 92460, 57460, 82460, 47460, 91718, 61718, 86718, 52656, 94359, 66359, 91359, 57359, 93671, 69671, 94671, 73671, 86913, 64406, 93406, 68406, 92406, 65406, 95507, 70507, 90507, 67507, 92753, 75253, 87753, 62753, 94753, 78753, 83753, 71753, 88281, 53281, 88281, 58281, 83281, 50281, 81281, 45281, 86281, 51281, 82281, 46281, 84281, 48281, 85281, 50281, 87281, 52281, 89281, 54281, 90281, 56281, 91281, 58281, 92281, 60281, 93281, 62281, 94281, 64281, 95281, 66281, 96281, 68281, 97281, 70281, 98281, 72281, 99281, 74281, 100000]) == 2291: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [5, 1, 4, 2, 3, 8, 6, 7, 10, 9, 5, 5, 5, 5, 5]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [5, 1, 4, 2, 3, 8, 6, 7, 10, 9, 5, 5, 5, 5, 5]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [2, 3, 1, 4, 5, 1, 3, 2, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [2, 3, 1, 4, 5, 1, 3, 2, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [100000, 100000, 100000, 1, 1, 1, 50000, 50000, 50000, 25000]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [100000, 100000, 100000, 1, 1, 1, 50000, 50000, 50000, 25000]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [1, 2, 3, 4, 5, 100000, 99999, 99998, 99997, 99996]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [1, 2, 3, 4, 5, 100000, 99999, 99998, 99997, 99996]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [5, 4, 3, 2, 1, 100000, 99999, 99998, 99997, 99996]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [5, 4, 3, 2, 1, 100000, 99999, 99998, 99997, 99996]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5, 600, 6, 700, 7, 800, 8, 900, 9, 1000, 10]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5, 600, 6, 700, 7, 800, 8, 900, 9, 1000, 10]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [50000, 50001, 50002, 50003, 50004, 50005, 50006, 50007, 50008, 50009]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [50000, 50001, 50002, 50003, 50004, 50005, 50006, 50007, 50008, 50009]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [5, 3, 1, 2, 4, 6, 8, 7, 10, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [5, 3, 1, 2, 4, 6, 8, 7, 10, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [100, 200, 300, 400, 500, 500, 400, 300, 200, 100]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [100, 200, 300, 400, 500, 500, 400, 300, 200, 100]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 95000, 92500, 90000, 87500, 85000, 82500, 80000, 77500, 75000, 72500]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 95000, 92500, 90000, 87500, 85000, 82500, 80000, 77500, 75000, 72500]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [5, 1, 9, 2, 8, 3, 7, 4, 6, 10]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [5, 1, 9, 2, 8, 3, 7, 4, 6, 10]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(instructions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100000, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(instructions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100000, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 32: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(instructions = [100000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(instructions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(instructions = [50000, 50001, 50002, 50003, 50004, 50005, 50006, 50007, 50008, 50009]) == 0
    assert candidate(instructions = [1, 2, 3, 6, 5, 4]) == 3
    assert candidate(instructions = [1, 5, 6, 2]) == 1
    assert candidate(instructions = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 20
    assert candidate(instructions = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996]) == 20
    assert candidate(instructions = [1, 3, 3, 3, 2, 4, 2, 1, 2]) == 4
    assert candidate(instructions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(instructions = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(instructions = [5, 1, 3, 2, 4, 6, 8, 7, 10, 9]) == 5
    assert candidate(instructions = [100000, 1, 100000, 2, 100000, 3, 100000, 4, 100000, 5]) == 10
    assert candidate(instructions = [50000, 40000, 30000, 20000, 10000, 60000, 70000, 80000, 90000, 100000]) == 0
    assert candidate(instructions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 27
    assert candidate(instructions = [5, 3, 8, 6, 2, 7, 4, 1, 10, 9]) == 5
    assert candidate(instructions = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 0
    assert candidate(instructions = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == 10
    assert candidate(instructions = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == 32
    assert candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 75
    assert candidate(instructions = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 4
    assert candidate(instructions = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990]) == 0
    assert candidate(instructions = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981]) == 0
    assert candidate(instructions = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 27
    assert candidate(instructions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 75
    assert candidate(instructions = [9, 3, 8, 3, 7, 3, 6, 3, 5, 3, 4, 3, 2, 3, 1, 3]) == 18
    assert candidate(instructions = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 24
    assert candidate(instructions = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 75
    assert candidate(instructions = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == 0
    assert candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0
    assert candidate(instructions = [1, 2, 3, 6, 5, 4, 1, 2, 3, 6, 5, 4]) == 14
    assert candidate(instructions = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15]) == 10
    assert candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 75
    assert candidate(instructions = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 30
    assert candidate(instructions = [5, 4, 3, 2, 1]) == 0
    assert candidate(instructions = [1, 3, 2, 6, 5, 4, 9, 8, 7, 10, 1, 3, 2, 6, 5, 4, 9, 8, 7, 10, 1, 3, 2, 6, 5, 4, 9, 8, 7, 10]) == 88
    assert candidate(instructions = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 0
    assert candidate(instructions = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 60
    assert candidate(instructions = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10]) == 16
    assert candidate(instructions = [10, 20, 30, 40, 50, 40, 30, 20, 10, 10, 20, 30, 40, 50, 40, 30, 20, 10]) == 22
    assert candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 75
    assert candidate(instructions = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(instructions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 0
    assert candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 27
    assert candidate(instructions = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 0
    assert candidate(instructions = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45
    assert candidate(instructions = [100000, 99999, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == 33
    assert candidate(instructions = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 27
    assert candidate(instructions = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 14
    assert candidate(instructions = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 36
    assert candidate(instructions = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996, 6, 99995, 7, 99994, 8, 99993]) == 56
    assert candidate(instructions = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0
    assert candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1]) == 0
    assert candidate(instructions = [10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9]) == 0
    assert candidate(instructions = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45
    assert candidate(instructions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 0
    assert candidate(instructions = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996]) == 20
    assert candidate(instructions = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 10
    assert candidate(instructions = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 60
    assert candidate(instructions = [5, 1, 3, 2, 4, 6, 8, 7, 10, 9, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16]) == 25
    assert candidate(instructions = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 0
    assert candidate(instructions = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 0
    assert candidate(instructions = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 0
    assert candidate(instructions = [1, 3, 2, 4, 2, 3, 1, 4, 2, 3]) == 7
    assert candidate(instructions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 0
    assert candidate(instructions = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3, 1]) == 0
    assert candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 75
    assert candidate(instructions = [3, 1, 2, 5, 4, 6, 9, 7, 10, 8]) == 5
    assert candidate(instructions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 30
    assert candidate(instructions = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]) == 0
    assert candidate(instructions = [50000, 50001, 50002, 50003, 50004, 50005, 50006, 50007, 50008, 50009, 50000, 50001, 50002, 50003, 50004, 50005, 50006, 50007, 50008, 50009]) == 27
    assert candidate(instructions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 30
    assert candidate(instructions = [100000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
    assert candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 45
    assert candidate(instructions = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 0
    assert candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 27
    assert candidate(instructions = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 0
    assert candidate(instructions = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 317
    assert candidate(instructions = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0
    assert candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
    assert candidate(instructions = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9]) == 9
    assert candidate(instructions = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 0
    assert candidate(instructions = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 0
    assert candidate(instructions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 27
    assert candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
    assert candidate(instructions = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 21
    assert candidate(instructions = [100000, 50000, 75000, 25000, 62500, 37500, 87500, 12500, 93750, 43750, 68750, 31250, 81250, 18750, 90625, 46875, 71875, 28125, 89062, 40625, 65625, 34375, 84375, 21875, 82812, 45312, 70312, 29687, 88281, 49218, 74218, 32187, 86171, 42187, 67187, 35156, 83125, 23437, 85937, 50312, 75312, 37812, 81562, 44531, 69531, 33437, 87968, 47968, 72968, 30937, 90468, 52968, 77968, 38906, 85468, 55468, 80468, 43437, 92460, 57460, 82460, 47460, 91718, 61718, 86718, 52656, 94359, 66359, 91359, 57359, 93671, 69671, 94671, 73671, 86913, 64406, 93406, 68406, 92406, 65406, 95507, 70507, 90507, 67507, 92753, 75253, 87753, 62753, 94753, 78753, 83753, 71753, 88281, 53281, 88281, 58281, 83281, 50281, 81281, 45281, 86281, 51281, 82281, 46281, 84281, 48281, 85281, 50281, 87281, 52281, 89281, 54281, 90281, 56281, 91281, 58281, 92281, 60281, 93281, 62281, 94281, 64281, 95281, 66281, 96281, 68281, 97281, 70281, 98281, 72281, 99281, 74281, 100000]) == 2291
    assert candidate(instructions = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(instructions = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 65
    assert candidate(instructions = [5, 1, 4, 2, 3, 8, 6, 7, 10, 9, 5, 5, 5, 5, 5]) == 27
    assert candidate(instructions = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 0
    assert candidate(instructions = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 0
    assert candidate(instructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 27
    assert candidate(instructions = [7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(instructions = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 27
    assert candidate(instructions = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 0
    assert candidate(instructions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 84
    assert candidate(instructions = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 15
    assert candidate(instructions = [2, 3, 1, 4, 5, 1, 3, 2, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 27
    assert candidate(instructions = [100000, 100000, 100000, 1, 1, 1, 50000, 50000, 50000, 25000]) == 12
    assert candidate(instructions = [1, 2, 3, 4, 5, 100000, 99999, 99998, 99997, 99996]) == 10
    assert candidate(instructions = [5, 4, 3, 2, 1, 100000, 99999, 99998, 99997, 99996]) == 10
    assert candidate(instructions = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 0
    assert candidate(instructions = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5, 600, 6, 700, 7, 800, 8, 900, 9, 1000, 10]) == 45
    assert candidate(instructions = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 27
    assert candidate(instructions = [50000, 50001, 50002, 50003, 50004, 50005, 50006, 50007, 50008, 50009]) == 0
    assert candidate(instructions = [5, 3, 1, 2, 4, 6, 8, 7, 10, 9]) == 4
    assert candidate(instructions = [100, 200, 300, 400, 500, 500, 400, 300, 200, 100]) == 5
    assert candidate(instructions = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 95000, 92500, 90000, 87500, 85000, 82500, 80000, 77500, 75000, 72500]) == 52
    assert candidate(instructions = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 1]) == 0
    assert candidate(instructions = [5, 1, 9, 2, 8, 3, 7, 4, 6, 10]) == 12
    assert candidate(instructions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(instructions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100000, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 32


