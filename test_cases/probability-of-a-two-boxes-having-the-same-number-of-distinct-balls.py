def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(balls = [6, 6]) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 6]) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 4, 4, 4]) == 0.820979020979021
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 4, 4, 4]) == 0.820979020979021: {e}')
    
    total += 1
    try:
        result = candidate(balls = [2, 1, 1]) == 0.6666666666666666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [2, 1, 1]) == 0.6666666666666666: {e}')
    
    total += 1
    try:
        result = candidate(balls = [1, 2, 2, 2, 2, 2, 2]) == 0.8571428571428571
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [1, 2, 2, 2, 2, 2, 2]) == 0.8571428571428571: {e}')
    
    total += 1
    try:
        result = candidate(balls = [1, 2, 1, 2]) == 0.6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [1, 2, 1, 2]) == 0.6: {e}')
    
    total += 1
    try:
        result = candidate(balls = [2, 2, 2, 2]) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [2, 2, 2, 2]) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6, 1]) == 0.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 1]) == 0.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6]) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6]) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [3, 3]) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [3, 3]) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [1, 2, 3, 4, 5, 6]) == 0.5375089306977852
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [1, 2, 3, 4, 5, 6]) == 0.5375089306977852: {e}')
    
    total += 1
    try:
        result = candidate(balls = [2, 2, 2]) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [2, 2, 2]) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [1, 1, 1, 1, 1, 1, 1, 1]) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [1, 1, 1, 1, 1, 1, 1, 1]) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [2, 1, 1, 1, 1]) == 0.6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [2, 1, 1, 1, 1]) == 0.6: {e}')
    
    total += 1
    try:
        result = candidate(balls = [1, 1]) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [1, 1]) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [3, 2, 1]) == 0.3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [3, 2, 1]) == 0.3: {e}')
    
    total += 1
    try:
        result = candidate(balls = [1, 2, 3]) == 0.3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [1, 2, 3]) == 0.3: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6, 6, 6, 6, 6, 6, 6, 6]) == 0.8557108876701283
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 6, 6, 6, 6, 6, 6, 6]) == 0.8557108876701283: {e}')
    
    total += 1
    try:
        result = candidate(balls = [1, 1, 1, 1]) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [1, 1, 1, 1]) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [1, 1, 2, 2, 3, 3]) == 0.38311688311688313
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [1, 1, 2, 2, 3, 3]) == 0.38311688311688313: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 2]) == 0.6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 2]) == 0.6: {e}')
    
    total += 1
    try:
        result = candidate(balls = [5, 5, 1, 1, 1]) == 0.032467532467532464
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [5, 5, 1, 1, 1]) == 0.032467532467532464: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 3, 2, 1]) == 0.30952380952380953
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 3, 2, 1]) == 0.30952380952380953: {e}')
    
    total += 1
    try:
        result = candidate(balls = [5, 5, 1, 1]) == 0.5454545454545454
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [5, 5, 1, 1]) == 0.5454545454545454: {e}')
    
    total += 1
    try:
        result = candidate(balls = [1, 2, 3, 4]) == 0.30952380952380953
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [1, 2, 3, 4]) == 0.30952380952380953: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6, 2, 2, 2]) == 0.4329004329004329
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 2, 2, 2]) == 0.4329004329004329: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6, 4, 2, 2, 2]) == 0.40792540792540793
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 4, 2, 2, 2]) == 0.40792540792540793: {e}')
    
    total += 1
    try:
        result = candidate(balls = [2, 2, 2, 1, 1]) == 0.5714285714285714
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [2, 2, 2, 1, 1]) == 0.5714285714285714: {e}')
    
    total += 1
    try:
        result = candidate(balls = [5, 1, 1, 1, 1]) == 0.8571428571428571
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [5, 1, 1, 1, 1]) == 0.8571428571428571: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 4, 1]) == 0.11428571428571428
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 4, 1]) == 0.11428571428571428: {e}')
    
    total += 1
    try:
        result = candidate(balls = [2, 2, 2, 2, 2, 2]) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [2, 2, 2, 2, 2, 2]) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6, 6]) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 6]) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6, 1, 1, 1]) == 0.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 1, 1, 1]) == 0.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [3, 2, 1, 1, 1]) == 0.2571428571428571
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [3, 2, 1, 1, 1]) == 0.2571428571428571: {e}')
    
    total += 1
    try:
        result = candidate(balls = [3, 3, 3, 1]) == 0.21428571428571427
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [3, 3, 3, 1]) == 0.21428571428571427: {e}')
    
    total += 1
    try:
        result = candidate(balls = [3, 2, 2, 1]) == 0.37142857142857144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [3, 2, 2, 1]) == 0.37142857142857144: {e}')
    
    total += 1
    try:
        result = candidate(balls = [1, 1, 1, 1, 1, 1]) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [1, 1, 1, 1, 1, 1]) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [1, 1, 1, 1, 1, 1]) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [1, 1, 1, 1, 1, 1]) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [5, 4, 3, 2, 1]) == 0.5474941724941725
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [5, 4, 3, 2, 1]) == 0.5474941724941725: {e}')
    
    total += 1
    try:
        result = candidate(balls = [2, 2, 2, 2, 1]) == 0.8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [2, 2, 2, 2, 1]) == 0.8: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6, 6, 6]) == 0.9777869189633895
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 6, 6]) == 0.9777869189633895: {e}')
    
    total += 1
    try:
        result = candidate(balls = [1, 2, 3, 4]) == 0.30952380952380953
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [1, 2, 3, 4]) == 0.30952380952380953: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 2, 1]) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 2, 1]) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(balls = [1, 2, 2, 1, 1]) == 0.6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [1, 2, 2, 1, 1]) == 0.6: {e}')
    
    total += 1
    try:
        result = candidate(balls = [3, 2, 2, 1, 1, 1]) == 0.30952380952380953
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [3, 2, 2, 1, 1, 1]) == 0.30952380952380953: {e}')
    
    total += 1
    try:
        result = candidate(balls = [5, 3, 2]) == 0.5555555555555556
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [5, 3, 2]) == 0.5555555555555556: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6, 1, 1]) == 0.5714285714285714
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 1, 1]) == 0.5714285714285714: {e}')
    
    total += 1
    try:
        result = candidate(balls = [5, 3, 1]) == 0.21428571428571427
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [5, 3, 1]) == 0.21428571428571427: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 2, 1, 1]) == 0.34285714285714286
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 2, 1, 1]) == 0.34285714285714286: {e}')
    
    total += 1
    try:
        result = candidate(balls = [3, 2, 1, 1]) == 0.7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [3, 2, 1, 1]) == 0.7: {e}')
    
    total += 1
    try:
        result = candidate(balls = [5, 3, 3]) == 1.3531746031746033
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [5, 3, 3]) == 1.3531746031746033: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6, 3, 3]) == 0.7251082251082251
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 3, 3]) == 0.7251082251082251: {e}')
    
    total += 1
    try:
        result = candidate(balls = [5, 1, 1]) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [5, 1, 1]) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 2, 2]) == 0.5142857142857142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 2, 2]) == 0.5142857142857142: {e}')
    
    total += 1
    try:
        result = candidate(balls = [3, 3, 1, 1]) == 0.5714285714285714
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [3, 3, 1, 1]) == 0.5714285714285714: {e}')
    
    total += 1
    try:
        result = candidate(balls = [3, 3, 3, 3, 3, 3]) == 0.6334841628959276
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [3, 3, 3, 3, 3, 3]) == 0.6334841628959276: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 3, 2, 1]) == 0.30952380952380953
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 3, 2, 1]) == 0.30952380952380953: {e}')
    
    total += 1
    try:
        result = candidate(balls = [2, 3, 2, 1]) == 0.37142857142857144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [2, 3, 2, 1]) == 0.37142857142857144: {e}')
    
    total += 1
    try:
        result = candidate(balls = [2, 2, 2, 2]) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [2, 2, 2, 2]) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 2, 2, 1]) == 0.5857142857142857
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 2, 2, 1]) == 0.5857142857142857: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 4, 4, 2]) == 0.5664335664335665
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 4, 4, 2]) == 0.5664335664335665: {e}')
    
    total += 1
    try:
        result = candidate(balls = [1, 2, 2, 3, 3]) == 0.6507936507936508
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [1, 2, 2, 3, 3]) == 0.6507936507936508: {e}')
    
    total += 1
    try:
        result = candidate(balls = [2, 2, 1, 1, 1, 1]) == 0.5142857142857142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [2, 2, 1, 1, 1, 1]) == 0.5142857142857142: {e}')
    
    total += 1
    try:
        result = candidate(balls = [1, 1, 1, 1, 1, 1, 1, 1]) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [1, 1, 1, 1, 1, 1, 1, 1]) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [3, 2, 2]) == 1.1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [3, 2, 2]) == 1.1: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6, 2, 1, 1]) == 0.31746031746031744
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 2, 1, 1]) == 0.31746031746031744: {e}')
    
    total += 1
    try:
        result = candidate(balls = [5, 5, 5]) == 1.7657342657342658
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [5, 5, 5]) == 1.7657342657342658: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 3, 1]) == 0.11428571428571428
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 3, 1]) == 0.11428571428571428: {e}')
    
    total += 1
    try:
        result = candidate(balls = [5, 1, 1, 1, 1, 1]) == 0.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [5, 1, 1, 1, 1, 1]) == 0.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 4, 1, 1]) == 0.5555555555555556
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 4, 1, 1]) == 0.5555555555555556: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6, 2, 2]) == 0.47619047619047616
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 2, 2]) == 0.47619047619047616: {e}')
    
    total += 1
    try:
        result = candidate(balls = [1, 3, 3, 1]) == 0.5714285714285714
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [1, 3, 3, 1]) == 0.5714285714285714: {e}')
    
    total += 1
    try:
        result = candidate(balls = [5, 1, 1, 1]) == 0.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [5, 1, 1, 1]) == 0.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [3, 3, 1, 1]) == 0.5714285714285714
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [3, 3, 1, 1]) == 0.5714285714285714: {e}')
    
    total += 1
    try:
        result = candidate(balls = [3, 3, 3, 3]) == 0.7662337662337663
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [3, 3, 3, 3]) == 0.7662337662337663: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6, 1, 1, 1, 1, 1, 1, 1]) == 0.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 1, 1, 1, 1, 1, 1, 1]) == 0.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [3, 3, 3, 3]) == 0.7662337662337663
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [3, 3, 3, 3]) == 0.7662337662337663: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6, 2, 1, 1, 1]) == 0.4166666666666667
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 2, 1, 1, 1]) == 0.4166666666666667: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 2]) == 0.6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 2]) == 0.6: {e}')
    
    total += 1
    try:
        result = candidate(balls = [5, 1, 1, 1]) == 0.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [5, 1, 1, 1]) == 0.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 2, 2]) == 0.5142857142857142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 2, 2]) == 0.5142857142857142: {e}')
    
    total += 1
    try:
        result = candidate(balls = [2, 2, 1, 1, 1, 1]) == 0.5142857142857142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [2, 2, 1, 1, 1, 1]) == 0.5142857142857142: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 4, 4, 4]) == 0.820979020979021
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 4, 4, 4]) == 0.820979020979021: {e}')
    
    total += 1
    try:
        result = candidate(balls = [1, 1, 2, 2, 3, 3]) == 0.38311688311688313
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [1, 1, 2, 2, 3, 3]) == 0.38311688311688313: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 4, 2, 2]) == 0.5238095238095238
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 4, 2, 2]) == 0.5238095238095238: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6, 1, 1]) == 0.5714285714285714
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 1, 1]) == 0.5714285714285714: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 4, 1]) == 0.11428571428571428
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 4, 1]) == 0.11428571428571428: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6, 6, 1, 1]) == 0.5384615384615384
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 6, 1, 1]) == 0.5384615384615384: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 4, 2]) == 0.6190476190476191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 4, 2]) == 0.6190476190476191: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6, 2, 2, 2, 2, 2, 2]) == 0.38009049773755654
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 2, 2, 2, 2, 2, 2]) == 0.38009049773755654: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 4, 3, 2, 1]) == 0.30186480186480186
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 4, 3, 2, 1]) == 0.30186480186480186: {e}')
    
    total += 1
    try:
        result = candidate(balls = [3, 2, 1, 1, 1]) == 0.2571428571428571
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [3, 2, 1, 1, 1]) == 0.2571428571428571: {e}')
    
    total += 1
    try:
        result = candidate(balls = [4, 4, 4]) == 0.8961038961038961
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [4, 4, 4]) == 0.8961038961038961: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6, 1, 1, 1]) == 0.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 1, 1, 1]) == 0.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [2, 2, 2, 2, 2, 2]) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [2, 2, 2, 2, 2, 2]) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6, 1, 1, 1, 1, 1]) == 0.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 1, 1, 1, 1, 1]) == 0.0: {e}')
    
    total += 1
    try:
        result = candidate(balls = [6, 3, 1, 1, 1, 1]) == 0.6818181818181818
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [6, 3, 1, 1, 1, 1]) == 0.6818181818181818: {e}')
    
    total += 1
    try:
        result = candidate(balls = [1, 2, 3, 2]) == 0.37142857142857144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [1, 2, 3, 2]) == 0.37142857142857144: {e}')
    
    total += 1
    try:
        result = candidate(balls = [5, 2, 2, 1]) == 0.31746031746031744
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [5, 2, 2, 1]) == 0.31746031746031744: {e}')
    
    total += 1
    try:
        result = candidate(balls = [3, 2, 1]) == 0.3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [3, 2, 1]) == 0.3: {e}')
    
    total += 1
    try:
        result = candidate(balls = [3, 2, 1, 1, 1, 1]) == 0.6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [3, 2, 1, 1, 1, 1]) == 0.6: {e}')
    
    total += 1
    try:
        result = candidate(balls = [2, 2, 2, 1, 1]) == 0.5714285714285714
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [2, 2, 2, 1, 1]) == 0.5714285714285714: {e}')
    
    total += 1
    try:
        result = candidate(balls = [3, 2, 2, 1]) == 0.37142857142857144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(balls = [3, 2, 2, 1]) == 0.37142857142857144: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(balls = [6, 6]) == 1.0
    assert candidate(balls = [4, 4, 4, 4]) == 0.820979020979021
    assert candidate(balls = [2, 1, 1]) == 0.6666666666666666
    assert candidate(balls = [1, 2, 2, 2, 2, 2, 2]) == 0.8571428571428571
    assert candidate(balls = [1, 2, 1, 2]) == 0.6
    assert candidate(balls = [2, 2, 2, 2]) == 1.0
    assert candidate(balls = [6, 1]) == 0.0
    assert candidate(balls = [6]) == 1.0
    assert candidate(balls = [3, 3]) == 1.0
    assert candidate(balls = [1, 2, 3, 4, 5, 6]) == 0.5375089306977852
    assert candidate(balls = [2, 2, 2]) == 1.0
    assert candidate(balls = [1, 1, 1, 1, 1, 1, 1, 1]) == 1.0
    assert candidate(balls = [2, 1, 1, 1, 1]) == 0.6
    assert candidate(balls = [1, 1]) == 1.0
    assert candidate(balls = [3, 2, 1]) == 0.3
    assert candidate(balls = [1, 2, 3]) == 0.3
    assert candidate(balls = [6, 6, 6, 6, 6, 6, 6, 6]) == 0.8557108876701283
    assert candidate(balls = [1, 1, 1, 1]) == 1.0
    assert candidate(balls = [1, 1, 2, 2, 3, 3]) == 0.38311688311688313
    assert candidate(balls = [4, 2]) == 0.6
    assert candidate(balls = [5, 5, 1, 1, 1]) == 0.032467532467532464
    assert candidate(balls = [4, 3, 2, 1]) == 0.30952380952380953
    assert candidate(balls = [5, 5, 1, 1]) == 0.5454545454545454
    assert candidate(balls = [1, 2, 3, 4]) == 0.30952380952380953
    assert candidate(balls = [6, 2, 2, 2]) == 0.4329004329004329
    assert candidate(balls = [6, 4, 2, 2, 2]) == 0.40792540792540793
    assert candidate(balls = [2, 2, 2, 1, 1]) == 0.5714285714285714
    assert candidate(balls = [5, 1, 1, 1, 1]) == 0.8571428571428571
    assert candidate(balls = [4, 4, 1]) == 0.11428571428571428
    assert candidate(balls = [2, 2, 2, 2, 2, 2]) == 1.0
    assert candidate(balls = [6, 6]) == 1.0
    assert candidate(balls = [6, 1, 1, 1]) == 0.0
    assert candidate(balls = [3, 2, 1, 1, 1]) == 0.2571428571428571
    assert candidate(balls = [3, 3, 3, 1]) == 0.21428571428571427
    assert candidate(balls = [3, 2, 2, 1]) == 0.37142857142857144
    assert candidate(balls = [1, 1, 1, 1, 1, 1]) == 1.0
    assert candidate(balls = [1, 1, 1, 1, 1, 1]) == 1.0
    assert candidate(balls = [5, 4, 3, 2, 1]) == 0.5474941724941725
    assert candidate(balls = [2, 2, 2, 2, 1]) == 0.8
    assert candidate(balls = [6, 6, 6]) == 0.9777869189633895
    assert candidate(balls = [1, 2, 3, 4]) == 0.30952380952380953
    assert candidate(balls = [4, 2, 1]) == 0.5
    assert candidate(balls = [1, 2, 2, 1, 1]) == 0.6
    assert candidate(balls = [3, 2, 2, 1, 1, 1]) == 0.30952380952380953
    assert candidate(balls = [5, 3, 2]) == 0.5555555555555556
    assert candidate(balls = [6, 1, 1]) == 0.5714285714285714
    assert candidate(balls = [5, 3, 1]) == 0.21428571428571427
    assert candidate(balls = [4, 2, 1, 1]) == 0.34285714285714286
    assert candidate(balls = [3, 2, 1, 1]) == 0.7
    assert candidate(balls = [5, 3, 3]) == 1.3531746031746033
    assert candidate(balls = [6, 3, 3]) == 0.7251082251082251
    assert candidate(balls = [5, 1, 1]) == 1.0
    assert candidate(balls = [4, 2, 2]) == 0.5142857142857142
    assert candidate(balls = [3, 3, 1, 1]) == 0.5714285714285714
    assert candidate(balls = [3, 3, 3, 3, 3, 3]) == 0.6334841628959276
    assert candidate(balls = [4, 3, 2, 1]) == 0.30952380952380953
    assert candidate(balls = [2, 3, 2, 1]) == 0.37142857142857144
    assert candidate(balls = [2, 2, 2, 2]) == 1.0
    assert candidate(balls = [4, 2, 2, 1]) == 0.5857142857142857
    assert candidate(balls = [4, 4, 4, 2]) == 0.5664335664335665
    assert candidate(balls = [1, 2, 2, 3, 3]) == 0.6507936507936508
    assert candidate(balls = [2, 2, 1, 1, 1, 1]) == 0.5142857142857142
    assert candidate(balls = [1, 1, 1, 1, 1, 1, 1, 1]) == 1.0
    assert candidate(balls = [3, 2, 2]) == 1.1
    assert candidate(balls = [6, 2, 1, 1]) == 0.31746031746031744
    assert candidate(balls = [5, 5, 5]) == 1.7657342657342658
    assert candidate(balls = [4, 3, 1]) == 0.11428571428571428
    assert candidate(balls = [5, 1, 1, 1, 1, 1]) == 0.0
    assert candidate(balls = [4, 4, 1, 1]) == 0.5555555555555556
    assert candidate(balls = [6, 2, 2]) == 0.47619047619047616
    assert candidate(balls = [1, 3, 3, 1]) == 0.5714285714285714
    assert candidate(balls = [5, 1, 1, 1]) == 0.0
    assert candidate(balls = [3, 3, 1, 1]) == 0.5714285714285714
    assert candidate(balls = [3, 3, 3, 3]) == 0.7662337662337663
    assert candidate(balls = [6, 1, 1, 1, 1, 1, 1, 1]) == 0.0
    assert candidate(balls = [3, 3, 3, 3]) == 0.7662337662337663
    assert candidate(balls = [6, 2, 1, 1, 1]) == 0.4166666666666667
    assert candidate(balls = [4, 2]) == 0.6
    assert candidate(balls = [5, 1, 1, 1]) == 0.0
    assert candidate(balls = [4, 2, 2]) == 0.5142857142857142
    assert candidate(balls = [2, 2, 1, 1, 1, 1]) == 0.5142857142857142
    assert candidate(balls = [4, 4, 4, 4]) == 0.820979020979021
    assert candidate(balls = [1, 1, 2, 2, 3, 3]) == 0.38311688311688313
    assert candidate(balls = [4, 4, 2, 2]) == 0.5238095238095238
    assert candidate(balls = [6, 1, 1]) == 0.5714285714285714
    assert candidate(balls = [4, 4, 1]) == 0.11428571428571428
    assert candidate(balls = [6, 6, 1, 1]) == 0.5384615384615384
    assert candidate(balls = [4, 4, 2]) == 0.6190476190476191
    assert candidate(balls = [6, 2, 2, 2, 2, 2, 2]) == 0.38009049773755654
    assert candidate(balls = [4, 4, 3, 2, 1]) == 0.30186480186480186
    assert candidate(balls = [3, 2, 1, 1, 1]) == 0.2571428571428571
    assert candidate(balls = [4, 4, 4]) == 0.8961038961038961
    assert candidate(balls = [6, 1, 1, 1]) == 0.0
    assert candidate(balls = [2, 2, 2, 2, 2, 2]) == 1.0
    assert candidate(balls = [6, 1, 1, 1, 1, 1]) == 0.0
    assert candidate(balls = [6, 3, 1, 1, 1, 1]) == 0.6818181818181818
    assert candidate(balls = [1, 2, 3, 2]) == 0.37142857142857144
    assert candidate(balls = [5, 2, 2, 1]) == 0.31746031746031744
    assert candidate(balls = [3, 2, 1]) == 0.3
    assert candidate(balls = [3, 2, 1, 1, 1, 1]) == 0.6
    assert candidate(balls = [2, 2, 2, 1, 1]) == 0.5714285714285714
    assert candidate(balls = [3, 2, 2, 1]) == 0.37142857142857144


