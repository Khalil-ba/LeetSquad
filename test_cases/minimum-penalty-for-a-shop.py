def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(customers = "YNYNYN") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNYNYN") == 1: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNNYNYYNYN") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNNYNYYNYN") == 1: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNYNNYNNYNNYNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNYNNYNNYNNYNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYNNYYYYNNYYYYNNYYYYNNNN") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYNNYYYYNNYYYYNNYYYYNNNN") == 22: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNYYYYYYNY") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNYYYYYYNY") == 8: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNYYYYNNYY") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNYYYYNNYY") == 6: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYYNNYNY") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYYNNYNY") == 3: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNYNNYNYYN") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNYNNYNYYN") == 1: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYYYYYNNNYYYYYYYYYYNNNNN") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYYYYYNNNYYYYYYYYYYNNNNN") == 19: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNYNYNYNYN") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNYNYNYNYN") == 1: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNYNYNYNYNYN") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNYNYNYNYNYN") == 1: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYY") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYY") == 10: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYY") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYY") == 12: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNNNNNNNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNNNNNNNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNYNNYNYN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNYNNYNYN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNNNNNNYN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNNNNNNYN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNNNNNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNNNNNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYNY") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYNY") == 2: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYNNNNYYYY") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYNNNNYYYY") == 4: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYYNNYNYNNY") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYYNNYNYNNY") == 3: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNYNYNYNYNY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNYNYNYNYNY") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNYNYNYNY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNYNYNYNY") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYY") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYY") == 4: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNYYYYYYNYYN") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNYYYYYYNYYN") == 11: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNNYYNYY") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNNYYNYY") == 8: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYNNNNNYYYYYY") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYNNNNNYYYYYY") == 16: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNNYNYY") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNNYNYY") == 1: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNNNNNNNNNNNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNNNNNNNNNNNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYNNYNNYNNYNNY") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYNNYNNYNNYNNY") == 4: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYY") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYY") == 46: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNN") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNN") == 48: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNYNYNYNYNYNYNYNYNY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNYNYNYNYNYNYNYNYNY") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNYYYYYYYYYYYYYY") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNYYYYYYYYYYYYYY") == 20: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNYYYYYYYY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNYYYYYYYY") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNYNYNYNNYNNYNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNYNYNYNNYNNYNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYY") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYY") == 6: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNNNN") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNNNN") == 94: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNYYYYYYYYNYNYYYYYYYYNYNYYYYYYYYNYNYYYYYYYYNYNYYYYYYYY") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNYYYYYYYYNYNYYYYYYYYNYNYYYYYYYYNYNYYYYYYYYNYNYYYYYYYY") == 54: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYNNYNYNYNYNYNYNYNYN") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYNNYNYNYNYNYNYNYNYN") == 2: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNNYYNYNNYYNYNNYYNY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNNYYNYNNYYNYNNYYNY") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 94: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYNNYYYNYYNNYYNNYYNYNNYYNYNYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNYNYNYNNYYNNYYNNYYNNYYNYNYNYNNYYNNYYNNYYNNYYNYNYNY") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYNNYYYNYYNNYYNNYYNYNNYYNYNYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNYNYNYNNYYNNYYNNYYNNYYNYNYNYNNYYNNYYNNYYNNYYNYNYNY") == 12: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNN") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNN") == 2: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYNNNNNYYYYYNNNNNYYYYYNNNNNYYYYYNNNNN") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYNNNNNYYYYYNNNNNYYYYYNNNNNYYYYYNNNNN") == 5: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNN") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNN") == 94: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNNYNYYNYYNNYNNYNYYN") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNNYNYYNYYNNYNNYNYYN") == 10: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYNNYYYYNNYYY") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYNNYYYYNNYYY") == 16: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYNNYYNNYYNNYY") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYNNYYNNYYNNYY") == 2: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 92: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 94: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNYYYYYYYYYY") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNYYYYYYYYYY") == 10: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYNYYNYNYYNNYY") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYNYYNYNYYNNYY") == 10: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYY") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYY") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYY") == 16: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNY") == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNY") == 78: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNYNYNYNYNYNYNY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNYNYNYNYNYNYNY") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 88: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 1: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNN") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNN") == 94: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNY") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNY") == 4: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYNNNNYYYYNNNN") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYNNNNYYYYNNNN") == 4: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYY") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYY") == 41: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYN") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYN") == 1: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYY") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYY") == 3: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 94: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYY") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYY") == 20: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYY") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYY") == 2: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNN") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNN") == 94: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNYNNYNYNYNYNNYNYNNYNYNYNNYNYNNYNYNNYNY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNYNNYNYNYNYNNYNYNNYNYNYNNYNYNNYNYNNYNY") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 64: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNYNYNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNYNYNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNY") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNNYYYN") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNNYYYN") == 41: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYN") == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYN") == 93: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNNYNYNNYNYNNYNYNNYNYNNYNYNNYNYNNYNYNNYNYNNYNYNNYNYNNYN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNNYNYNNYNYNNYNYNNYNYNNYNYNNYNYNNYNYNNYNYNNYNYNNYNYNNYN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNNNNYYYYYYYY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNNNNYYYYYYYY") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNNNNNNNNNNNNNNNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNNNNNNNNNNNNNNNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNYNNYNNYNNYNNYY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNYNNYNNYNNYNNYY") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNN") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNN") == 52: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 44: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNNNNNNNNNNNNNNNNNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNNNNNNNNNNNNNNNNNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNYYNNNNYYNNYYYYNYYY") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNYYNNNNYYNNYYYYNYYY") == 20: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNNYNYYNNYNYYNNYNYYNNYNYYNNYNYYNNYNYYNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNNYNYYNNYNYYNNYNYYNNYNYYNNYNYYNNYNYYNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNNYYNYYNNYYNYYNNYYNYYNNYYNYYNNYYNYYNNYYNYYNN") == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNNYYNYYNNYYNYYNNYYNYYNNYYNYYNNYYNYYNNYYNYYNN") == 43: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNN") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNN") == 94: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 104: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYNNNNNNNNNNN") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYNNNNNNNNNNN") == 5: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYNNYNYNYNYNN") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYNNYNYNYNYNN") == 5: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 1: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYNNNNNNNN") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYNNNNNNNN") == 10: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYY") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYY") == 6: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNNY") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNNY") == 2: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNYYYYYYYYYYYYYYYYYYYY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNYYYYYYYYYYYYYYYYYYYY") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYNNYYYNYYYYNNYYYNYYYYNNYYYNYYYYNNYYYNYYYYNNYYYNYYYY") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYNNYYYNYYYYNNYYYNYYYYNNYYYNYYYYNNYYYNYYYYNNYYYNYYYY") == 54: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNN") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNN") == 2: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYNNNNNNNNNNNNNNNNNNNNYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYNNNNNNNNNNNNNNNNNNNNYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 108: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYYYYY") == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYYYYY") == 96: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNYNYNYNYNYNYNYN") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNYNYNYNYNYNYNYN") == 1: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNYYNNYNYNYYNNYNYNY") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNYYNNYNYNYYNNYNYNY") == 5: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNYNYNYNYNYNYNYN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNYNYNYNYNYNYNYN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 54: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNN") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNN") == 94: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYNNYYYYYYNNYYYYYYNNYYYYYYNNYYYYYYNNYYYYYY") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYNNYYYYYYNNYYYYYYNNYYYYYYNNYYYYYYNNYYYYYY") == 42: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNY") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNY") == 39: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNYYYYYYYNNNN") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNYYYYYYYNNNN") == 12: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYNNNNYYYYYYYYYNNNNNNNYYYYYYYYYNNNNNYYY") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYNNNNYYYYYYYYYNNNNNNNYYYYYYYYYNNNNNYYY") == 34: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNN") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNN") == 10: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNNNNYNNYNYNYNYNNYNNYNNYNYNNYNNYNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNY") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNNNNYNNYNYNYNYNNYNNYNNYNYNNYNNYNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNY") == 1: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYNYNYNYNYNNYNNY") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYNYNYNYNYNNYNNY") == 2: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYYYYYYYYYNNNNNNNNNN") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYYYYYYYYYNNNNNNNNNN") == 10: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNNYYYYYYYYYYYYYY") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNNYYYYYYYYYYYYYY") == 20: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNNNNNN") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNNNNNN") == 94: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYY") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 40: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNN") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNN") == 94: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYNNYYNNYYNN") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYNNYYNNYYNN") == 2: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNYNYNYNYNYNYNNY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNYNYNYNYNYNYNNY") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYN") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYN") == 1: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNN") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNN") == 94: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 1: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNN") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNN") == 10: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYYYYYYYYYYYNN") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYYYYYYYYYYYNN") == 12: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNYYYYNNYYYYNNYYYYNNYYYYNNYYYYNNYYYYNNYYYY") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNYYYYNNYYYYNNYYYYNNYYYYNNYYYYNNYYYYNNYYYY") == 42: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNN") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNN") == 94: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYN") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYN") == 1: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 24: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 1: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYY") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYY") == 4: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNN") == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNN") == 88: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYNYYNYYYNYYNNYYYYNYYYYNYNYNYYYYYYYYYYYYNNNYNYNYYNNYNN") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYNYYNYYYNYYNNYYYYNYYYYNYNYNYYYYYYYYYYYYNNNYNYNYYNNYNN") == 41: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 70: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNNNNNYYYYYYYYYYNNNNNNNNNYYYYYYYYYYNNNNNNNNNYYYYYYYYYYNNNNNNNNNYYYYYYYYYY") == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNNNNNYYYYYYYYYYNNNNNNNNNYYYYYYYYYYNNNNNNNNNYYYYYYYYYYNNNNNNNNNYYYYYYYYYY") == 76: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYY") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYY") == 2: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNNNYNNNYNNNY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNNNYNNNYNNNY") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNNYY") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNNYY") == 39: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNN") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNN") == 0: {e}')
    
    total += 1
    try:
        result = candidate(customers = "YYYYYYYYYYNNNNNNNNNN") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "YYYYYYYYYYNNNNNNNNNN") == 10: {e}')
    
    total += 1
    try:
        result = candidate(customers = "NYNYNYNYNYNYNYNYNYNYNYNNNNNNNNNNNNNNNNNNNNNNNNYYYYYYYYYYYYYYYYYYYY") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(customers = "NYNYNYNYNYNYNYNYNYNYNYNNNNNNNNNNNNNNNNNNNNNNNNYYYYYYYYYYYYYYYYYYYY") == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(customers = "YNYNYN") == 1
    assert candidate(customers = "YNNYNYYNYN") == 1
    assert candidate(customers = "NNYNNYNNYNNYNN") == 0
    assert candidate(customers = "YYYYNNYYYYNNYYYYNNYYYYNNNN") == 22
    assert candidate(customers = "YNYYYYYYNY") == 8
    assert candidate(customers = "YNYYYYNNYY") == 6
    assert candidate(customers = "NYYNNYNY") == 3
    assert candidate(customers = "YNYNNYNYYN") == 1
    assert candidate(customers = "NYYYYYNNNYYYYYYYYYYNNNNN") == 19
    assert candidate(customers = "YNYNYNYNYN") == 1
    assert candidate(customers = "YNYNYNYNYNYN") == 1
    assert candidate(customers = "NNNNN") == 0
    assert candidate(customers = "YYYYYYYYYY") == 10
    assert candidate(customers = "YYYYYYYYYYYY") == 12
    assert candidate(customers = "NNNNNNNNNNNN") == 0
    assert candidate(customers = "NNYNNYNYN") == 0
    assert candidate(customers = "NYNNNNNNYN") == 0
    assert candidate(customers = "NNNNNNNNNN") == 0
    assert candidate(customers = "YYNY") == 2
    assert candidate(customers = "YYYYNNNNYYYY") == 4
    assert candidate(customers = "NYYNNYNYNNY") == 3
    assert candidate(customers = "NYNYNYNYNYNY") == 0
    assert candidate(customers = "NYNYNYNYNY") == 0
    assert candidate(customers = "YYYY") == 4
    assert candidate(customers = "YNYYYYYYNYYN") == 11
    assert candidate(customers = "YNNYYNYY") == 8
    assert candidate(customers = "YYYYYNNNNNYYYYYY") == 16
    assert candidate(customers = "YNNYNYY") == 1
    assert candidate(customers = "NNNNNNNNNNNNNNNN") == 0
    assert candidate(customers = "YYYYNNYNNYNNYNNY") == 4
    assert candidate(customers = "NNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYY") == 46
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNN") == 48
    assert candidate(customers = "NYNYNYNYNYNYNYNYNYNY") == 0
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNYYYYYYYYYYYYYY") == 20
    assert candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNYYYYYYYY") == 0
    assert candidate(customers = "NYNYNYNYNNYNNYNN") == 0
    assert candidate(customers = "YYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYY") == 6
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNNNN") == 94
    assert candidate(customers = "YNYYYYYYYYNYNYYYYYYYYNYNYYYYYYYYNYNYYYYYYYYNYNYYYYYYYY") == 54
    assert candidate(customers = "YYNNYNYNYNYNYNYNYNYN") == 2
    assert candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0
    assert candidate(customers = "NYNNYYNYNNYYNYNNYYNY") == 0
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 94
    assert candidate(customers = "YYYYNNYYYNYYNNYYNNYYNYNNYYNYNYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNYNYNYNNYYNNYYNNYYNNYYNYNYNYNNYYNNYYNNYYNNYYNYNYNY") == 12
    assert candidate(customers = "YYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNN") == 2
    assert candidate(customers = "YYYYYNNNNNYYYYYNNNNNYYYYYNNNNNYYYYYNNNNN") == 5
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNN") == 94
    assert candidate(customers = "NYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 0
    assert candidate(customers = "YNNYNYYNYYNNYNNYNYYN") == 10
    assert candidate(customers = "YYYYYNNYYYYNNYYY") == 16
    assert candidate(customers = "YYNNYYNNYYNNYY") == 2
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 92
    assert candidate(customers = "NYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 94
    assert candidate(customers = "YYYYYYYYYYNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNYYYYYYYYYY") == 10
    assert candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0
    assert candidate(customers = "YYNYYNYNYYNNYY") == 10
    assert candidate(customers = "NYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYY") == 0
    assert candidate(customers = "YYYYYYYYYYYYYYYY") == 16
    assert candidate(customers = "NYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNY") == 78
    assert candidate(customers = "NYNYNYNYNYNYNYNY") == 0
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 88
    assert candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 1
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNN") == 94
    assert candidate(customers = "YYYYNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNY") == 4
    assert candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0
    assert candidate(customers = "YYYYNNNNYYYYNNNN") == 4
    assert candidate(customers = "YYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYY") == 41
    assert candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYN") == 1
    assert candidate(customers = "NYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYY") == 3
    assert candidate(customers = "NNNNNYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 94
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYY") == 20
    assert candidate(customers = "YYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYY") == 2
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNN") == 94
    assert candidate(customers = "NYNYNNYNYNYNYNNYNYNNYNYNYNNYNYNNYNYNNYNY") == 0
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 64
    assert candidate(customers = "NYNYNYNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNY") == 0
    assert candidate(customers = "NYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNNYYYN") == 41
    assert candidate(customers = "NYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYN") == 93
    assert candidate(customers = "NYNNYNYNNYNYNNYNYNNYNYNNYNYNNYNYNNYNYNNYNYNNYNYNNYNYNNYN") == 0
    assert candidate(customers = "NNNNNNNNYYYYYYYY") == 0
    assert candidate(customers = "NNNNNNNNNNNNNNNNNNNN") == 0
    assert candidate(customers = "NNYNNYNNYNNYNNYY") == 0
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNN") == 52
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 44
    assert candidate(customers = "NYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNNNNNNNNNNNNNNNNNN") == 0
    assert candidate(customers = "NNYYNNNNYYNNYYYYNYYY") == 20
    assert candidate(customers = "NYNNYNYYNNYNYYNNYNYYNNYNYYNNYNYYNNYNYYNN") == 0
    assert candidate(customers = "NNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNN") == 0
    assert candidate(customers = "YNNYYNYYNNYYNYYNNYYNYYNNYYNYYNNYYNYYNNYYNYYNN") == 43
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNN") == 94
    assert candidate(customers = "NNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNN") == 0
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 104
    assert candidate(customers = "YYYYYNNNNNNNNNNN") == 5
    assert candidate(customers = "YYYYYNNYNYNYNYNN") == 5
    assert candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 1
    assert candidate(customers = "NNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNN") == 0
    assert candidate(customers = "YYYYYYYYYYNNNNNNNN") == 10
    assert candidate(customers = "YYYYYYNNNNNNYYYYYYNNNNNNYYYYYYNNNNNNYYYYYY") == 6
    assert candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0
    assert candidate(customers = "YYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNNY") == 2
    assert candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNYYYYYYYYYYYYYYYYYYYY") == 0
    assert candidate(customers = "YYYYNNYYYNYYYYNNYYYNYYYYNNYYYNYYYYNNYYYNYYYYNNYYYNYYYY") == 54
    assert candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0
    assert candidate(customers = "YYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNNYYNYNN") == 2
    assert candidate(customers = "YYYYNNNNNNNNNNNNNNNNNNNNYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 108
    assert candidate(customers = "YYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYYYYY") == 96
    assert candidate(customers = "NYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 0
    assert candidate(customers = "YNYNYNYNYNYNYNYN") == 1
    assert candidate(customers = "NYNYYNNYNYNYYNNYNYNY") == 5
    assert candidate(customers = "NNYNYNYNYNYNYNYN") == 0
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 54
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNN") == 94
    assert candidate(customers = "YYNNYYYYYYNNYYYYYYNNYYYYYYNNYYYYYYNNYYYYYY") == 42
    assert candidate(customers = "NYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNY") == 39
    assert candidate(customers = "NNNNNYYYYYYYNNNN") == 12
    assert candidate(customers = "YYYYYNNNNYYYYYYYYYNNNNNNNYYYYYYYYYNNNNNYYY") == 34
    assert candidate(customers = "YYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNN") == 10
    assert candidate(customers = "YNNNNYNNYNYNYNYNNYNNYNNYNYNNYNNYNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNYNNY") == 1
    assert candidate(customers = "YYNYNYNYNYNNYNNY") == 2
    assert candidate(customers = "NYYYYYYYYYNNNNNNNNNN") == 10
    assert candidate(customers = "NNNNNNYYYYYYYYYYYYYY") == 20
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNNNNNN") == 94
    assert candidate(customers = "NNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYYNNNNYYYY") == 0
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 40
    assert candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNN") == 94
    assert candidate(customers = "YYNNYYNNYYNN") == 2
    assert candidate(customers = "NNYNYNYNYNYNYNNY") == 0
    assert candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYN") == 1
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNN") == 94
    assert candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 1
    assert candidate(customers = "YYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNN") == 10
    assert candidate(customers = "NYYYYYYYYYYYNN") == 12
    assert candidate(customers = "NNYYYYNNYYYYNNYYYYNNYYYYNNYYYYNNYYYYNNYYYY") == 42
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNN") == 94
    assert candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYN") == 1
    assert candidate(customers = "NNNNYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 24
    assert candidate(customers = "YNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 1
    assert candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0
    assert candidate(customers = "YYYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYY") == 4
    assert candidate(customers = "NYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNYNY") == 0
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNN") == 88
    assert candidate(customers = "YYYNYYNYYYNYYNNYYYYNYYYYNYNYNYYYYYYYYYYYYNNNYNYNYYNNYNN") == 41
    assert candidate(customers = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY") == 70
    assert candidate(customers = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN") == 0
    assert candidate(customers = "NNNNNNNNNYYYYYYYYYYNNNNNNNNNYYYYYYYYYYNNNNNNNNNYYYYYYYYYYNNNNNNNNNYYYYYYYYYY") == 76
    assert candidate(customers = "YYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYYNNYY") == 2
    assert candidate(customers = "NYNNNYNNNYNNNY") == 0
    assert candidate(customers = "NYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNYYNNYY") == 39
    assert candidate(customers = "NNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNNYYYYYYYYYYNNNNNNNNNN") == 0
    assert candidate(customers = "YYYYYYYYYYNNNNNNNNNN") == 10
    assert candidate(customers = "NYNYNYNYNYNYNYNYNYNYNYNNNNNNNNNNNNNNNNNNNNNNNNYYYYYYYYYYYYYYYYYYYY") == 0


