def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(divisor1 = 2,divisor2 = 7,uniqueCnt1 = 1,uniqueCnt2 = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 2,divisor2 = 7,uniqueCnt1 = 1,uniqueCnt2 = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 2,divisor2 = 4,uniqueCnt1 = 8,uniqueCnt2 = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 2,divisor2 = 4,uniqueCnt1 = 8,uniqueCnt2 = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 100,divisor2 = 101,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 200019803
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 100,divisor2 = 101,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 200019803: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 100,divisor2 = 200,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 201005025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 100,divisor2 = 200,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 201005025: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 5,divisor2 = 10,uniqueCnt1 = 5,uniqueCnt2 = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 5,divisor2 = 10,uniqueCnt1 = 5,uniqueCnt2 = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 7,divisor2 = 11,uniqueCnt1 = 10,uniqueCnt2 = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 7,divisor2 = 11,uniqueCnt1 = 10,uniqueCnt2 = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 7,divisor2 = 13,uniqueCnt1 = 10,uniqueCnt2 = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 7,divisor2 = 13,uniqueCnt1 = 10,uniqueCnt2 = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 3,divisor2 = 5,uniqueCnt1 = 2,uniqueCnt2 = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 3,divisor2 = 5,uniqueCnt1 = 2,uniqueCnt2 = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 10,divisor2 = 15,uniqueCnt1 = 5,uniqueCnt2 = 6) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 10,divisor2 = 15,uniqueCnt1 = 5,uniqueCnt2 = 6) == 11: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 7,divisor2 = 11,uniqueCnt1 = 3,uniqueCnt2 = 7) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 7,divisor2 = 11,uniqueCnt1 = 3,uniqueCnt2 = 7) == 10: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 100454545
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 100454545: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 89,divisor2 = 97,uniqueCnt1 = 60000000,uniqueCnt2 = 40000000) == 100011584
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 89,divisor2 = 97,uniqueCnt1 = 60000000,uniqueCnt2 = 40000000) == 100011584: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 20,uniqueCnt2 = 25) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 20,uniqueCnt2 = 25) == 45: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 23,divisor2 = 29,uniqueCnt1 = 50000000,uniqueCnt2 = 30000000) == 80120120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 23,divisor2 = 29,uniqueCnt1 = 50000000,uniqueCnt2 = 30000000) == 80120120: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 13,divisor2 = 19,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 200813008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 13,divisor2 = 19,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 200813008: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 2,divisor2 = 3,uniqueCnt1 = 999999999,uniqueCnt2 = 1) == 1999999997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 2,divisor2 = 3,uniqueCnt1 = 999999999,uniqueCnt2 = 1) == 1999999997: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 100000,divisor2 = 10000,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 100001000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 100000,divisor2 = 10000,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 100001000: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 100000,divisor2 = 200000,uniqueCnt1 = 1000000,uniqueCnt2 = 500000) == 1500007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 100000,divisor2 = 200000,uniqueCnt1 = 1000000,uniqueCnt2 = 500000) == 1500007: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 30,divisor2 = 42,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 100478468
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 30,divisor2 = 42,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 100478468: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 10000000,uniqueCnt2 = 20000000) == 30136363
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 10000000,uniqueCnt2 = 20000000) == 30136363: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 45,divisor2 = 18,uniqueCnt1 = 200000000,uniqueCnt2 = 300000000) == 505617977
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 45,divisor2 = 18,uniqueCnt1 = 200000000,uniqueCnt2 = 300000000) == 505617977: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 5,divisor2 = 7,uniqueCnt1 = 1,uniqueCnt2 = 999999999) == 1166666665
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 5,divisor2 = 7,uniqueCnt1 = 1,uniqueCnt2 = 999999999) == 1166666665: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 250000000,uniqueCnt2 = 250000000) == 502272727
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 250000000,uniqueCnt2 = 250000000) == 502272727: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 61,divisor2 = 71,uniqueCnt1 = 70000000,uniqueCnt2 = 30000000) == 100023094
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 61,divisor2 = 71,uniqueCnt1 = 70000000,uniqueCnt2 = 30000000) == 100023094: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 12,divisor2 = 18,uniqueCnt1 = 1000,uniqueCnt2 = 1000) == 2057
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 12,divisor2 = 18,uniqueCnt1 = 1000,uniqueCnt2 = 1000) == 2057: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 2,divisor2 = 5,uniqueCnt1 = 500000000,uniqueCnt2 = 499999999) == 1111111109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 2,divisor2 = 5,uniqueCnt1 = 500000000,uniqueCnt2 = 499999999) == 1111111109: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 4,divisor2 = 6,uniqueCnt1 = 5,uniqueCnt2 = 8) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 4,divisor2 = 6,uniqueCnt1 = 5,uniqueCnt2 = 8) == 14: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 4,divisor2 = 6,uniqueCnt1 = 300000000,uniqueCnt2 = 200000000) == 545454545
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 4,divisor2 = 6,uniqueCnt1 = 300000000,uniqueCnt2 = 200000000) == 545454545: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 10000,divisor2 = 20000,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 100005000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 10000,divisor2 = 20000,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 100005000: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 8,divisor2 = 12,uniqueCnt1 = 40000000,uniqueCnt2 = 60000000) == 104347826
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 8,divisor2 = 12,uniqueCnt1 = 40000000,uniqueCnt2 = 60000000) == 104347826: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 99999,divisor2 = 99998,uniqueCnt1 = 100000,uniqueCnt2 = 100000) == 200000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 99999,divisor2 = 99998,uniqueCnt1 = 100000,uniqueCnt2 = 100000) == 200000: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 50000,divisor2 = 100000,uniqueCnt1 = 10000000,uniqueCnt2 = 10000000) == 20000200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 50000,divisor2 = 100000,uniqueCnt1 = 10000000,uniqueCnt2 = 10000000) == 20000200: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 29,divisor2 = 41,uniqueCnt1 = 60000000,uniqueCnt2 = 40000000) == 100084175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 29,divisor2 = 41,uniqueCnt1 = 60000000,uniqueCnt2 = 40000000) == 100084175: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 15,divisor2 = 20,uniqueCnt1 = 75000000,uniqueCnt2 = 25000000) == 101694915
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 15,divisor2 = 20,uniqueCnt1 = 75000000,uniqueCnt2 = 25000000) == 101694915: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 19,divisor2 = 23,uniqueCnt1 = 150000000,uniqueCnt2 = 150000000) == 300688073
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 19,divisor2 = 23,uniqueCnt1 = 150000000,uniqueCnt2 = 150000000) == 300688073: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 3,divisor2 = 5,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 107142857
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 3,divisor2 = 5,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 107142857: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 50000,divisor2 = 75000,uniqueCnt1 = 60000000,uniqueCnt2 = 40000000) == 100000666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 50000,divisor2 = 75000,uniqueCnt1 = 60000000,uniqueCnt2 = 40000000) == 100000666: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 20,divisor2 = 30,uniqueCnt1 = 500000000,uniqueCnt2 = 400000000) == 915254237
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 20,divisor2 = 30,uniqueCnt1 = 500000000,uniqueCnt2 = 400000000) == 915254237: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 6,divisor2 = 8,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 104347826
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 6,divisor2 = 8,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 104347826: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 100000,divisor2 = 50000,uniqueCnt1 = 50000000,uniqueCnt2 = 40000000) == 90000900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 100000,divisor2 = 50000,uniqueCnt1 = 50000000,uniqueCnt2 = 40000000) == 90000900: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 10,divisor2 = 15,uniqueCnt1 = 75000000,uniqueCnt2 = 25000000) == 103448275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 10,divisor2 = 15,uniqueCnt1 = 75000000,uniqueCnt2 = 25000000) == 103448275: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 100000,divisor2 = 100000,uniqueCnt1 = 450000000,uniqueCnt2 = 450000000) == 900009000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 100000,divisor2 = 100000,uniqueCnt1 = 450000000,uniqueCnt2 = 450000000) == 900009000: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 7,divisor2 = 14,uniqueCnt1 = 900000000,uniqueCnt2 = 900000000) == 1938461538
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 7,divisor2 = 14,uniqueCnt1 = 900000000,uniqueCnt2 = 900000000) == 1938461538: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 23,divisor2 = 37,uniqueCnt1 = 50000000,uniqueCnt2 = 49999999) == 100117646
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 23,divisor2 = 37,uniqueCnt1 = 50000000,uniqueCnt2 = 49999999) == 100117646: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 99999,divisor2 = 100001,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 99999,divisor2 = 100001,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 100000000: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 23,divisor2 = 37,uniqueCnt1 = 45000000,uniqueCnt2 = 55000000) == 100117647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 23,divisor2 = 37,uniqueCnt1 = 45000000,uniqueCnt2 = 55000000) == 100117647: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 11,divisor2 = 13,uniqueCnt1 = 100,uniqueCnt2 = 150) == 251
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 11,divisor2 = 13,uniqueCnt1 = 100,uniqueCnt2 = 150) == 251: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 3,divisor2 = 5,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 214285714
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 3,divisor2 = 5,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 214285714: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 1000,divisor2 = 500,uniqueCnt1 = 40000000,uniqueCnt2 = 60000000) == 100100100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 1000,divisor2 = 500,uniqueCnt1 = 40000000,uniqueCnt2 = 60000000) == 100100100: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 4,divisor2 = 6,uniqueCnt1 = 100000000,uniqueCnt2 = 99999999) == 218181817
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 4,divisor2 = 6,uniqueCnt1 = 100000000,uniqueCnt2 = 99999999) == 218181817: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 5,divisor2 = 7,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 102941176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 5,divisor2 = 7,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 102941176: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 17,divisor2 = 31,uniqueCnt1 = 99999999,uniqueCnt2 = 1) == 106249998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 17,divisor2 = 31,uniqueCnt1 = 99999999,uniqueCnt2 = 1) == 106249998: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 99998,divisor2 = 99999,uniqueCnt1 = 100000,uniqueCnt2 = 100000) == 200000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 99998,divisor2 = 99999,uniqueCnt1 = 100000,uniqueCnt2 = 100000) == 200000: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 10,divisor2 = 15,uniqueCnt1 = 100000000,uniqueCnt2 = 1) == 111111111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 10,divisor2 = 15,uniqueCnt1 = 100000000,uniqueCnt2 = 1) == 111111111: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 4,divisor2 = 6,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 218181818
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 4,divisor2 = 6,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 218181818: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 6,divisor2 = 8,uniqueCnt1 = 75000000,uniqueCnt2 = 25000000) == 104347826
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 6,divisor2 = 8,uniqueCnt1 = 75000000,uniqueCnt2 = 25000000) == 104347826: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 77,divisor2 = 42,uniqueCnt1 = 500,uniqueCnt2 = 500) == 1002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 77,divisor2 = 42,uniqueCnt1 = 500,uniqueCnt2 = 500) == 1002: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 11,divisor2 = 13,uniqueCnt1 = 20000000,uniqueCnt2 = 15000000) == 35246478
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 11,divisor2 = 13,uniqueCnt1 = 20000000,uniqueCnt2 = 15000000) == 35246478: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 7,divisor2 = 14,uniqueCnt1 = 25000000,uniqueCnt2 = 25000000) == 53846153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 7,divisor2 = 14,uniqueCnt1 = 25000000,uniqueCnt2 = 25000000) == 53846153: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 15,divisor2 = 25,uniqueCnt1 = 80000000,uniqueCnt2 = 70000000) == 152027027
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 15,divisor2 = 25,uniqueCnt1 = 80000000,uniqueCnt2 = 70000000) == 152027027: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 11,divisor2 = 13,uniqueCnt1 = 99999999,uniqueCnt2 = 99999999) == 201408448
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 11,divisor2 = 13,uniqueCnt1 = 99999999,uniqueCnt2 = 99999999) == 201408448: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 3,divisor2 = 5,uniqueCnt1 = 100,uniqueCnt2 = 200) == 321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 3,divisor2 = 5,uniqueCnt1 = 100,uniqueCnt2 = 200) == 321: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 25,divisor2 = 40,uniqueCnt1 = 100,uniqueCnt2 = 150) == 251
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 25,divisor2 = 40,uniqueCnt1 = 100,uniqueCnt2 = 150) == 251: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 100001,divisor2 = 100003,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 200000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 100001,divisor2 = 100003,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 200000000: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 6,divisor2 = 9,uniqueCnt1 = 15,uniqueCnt2 = 20) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 6,divisor2 = 9,uniqueCnt1 = 15,uniqueCnt2 = 20) == 37: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 6,divisor2 = 9,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 105882352
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 6,divisor2 = 9,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 105882352: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 23,divisor2 = 31,uniqueCnt1 = 200000000,uniqueCnt2 = 300000000) == 500702247
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 23,divisor2 = 31,uniqueCnt1 = 200000000,uniqueCnt2 = 300000000) == 500702247: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 5,divisor2 = 6,uniqueCnt1 = 1000000,uniqueCnt2 = 500000) == 1551724
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 5,divisor2 = 6,uniqueCnt1 = 1000000,uniqueCnt2 = 500000) == 1551724: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 67,divisor2 = 89,uniqueCnt1 = 400000000,uniqueCnt2 = 400000000) == 800134183
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 67,divisor2 = 89,uniqueCnt1 = 400000000,uniqueCnt2 = 400000000) == 800134183: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 11,divisor2 = 13,uniqueCnt1 = 200000000,uniqueCnt2 = 1) == 219999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 11,divisor2 = 13,uniqueCnt1 = 200000000,uniqueCnt2 = 1) == 219999999: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 37,divisor2 = 41,uniqueCnt1 = 9876543,uniqueCnt2 = 1234567) == 11118439
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 37,divisor2 = 41,uniqueCnt1 = 9876543,uniqueCnt2 = 1234567) == 11118439: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 7,divisor2 = 13,uniqueCnt1 = 300000000,uniqueCnt2 = 300000000) == 606666666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 7,divisor2 = 13,uniqueCnt1 = 300000000,uniqueCnt2 = 300000000) == 606666666: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 5,divisor2 = 7,uniqueCnt1 = 99999999,uniqueCnt2 = 1) == 124999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 5,divisor2 = 7,uniqueCnt1 = 99999999,uniqueCnt2 = 1) == 124999998: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 97,divisor2 = 101,uniqueCnt1 = 1000000,uniqueCnt2 = 500000) == 1500153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 97,divisor2 = 101,uniqueCnt1 = 1000000,uniqueCnt2 = 500000) == 1500153: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 10000,divisor2 = 100000,uniqueCnt1 = 90000000,uniqueCnt2 = 10000000) == 100001000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 10000,divisor2 = 100000,uniqueCnt1 = 90000000,uniqueCnt2 = 10000000) == 100001000: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 5,uniqueCnt2 = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 5,uniqueCnt2 = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 10,divisor2 = 15,uniqueCnt1 = 100000000,uniqueCnt2 = 200000000) == 310344827
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 10,divisor2 = 15,uniqueCnt1 = 100000000,uniqueCnt2 = 200000000) == 310344827: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 100000,divisor2 = 200000,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 100000500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 100000,divisor2 = 200000,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 100000500: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 77,divisor2 = 42,uniqueCnt1 = 33000000,uniqueCnt2 = 66000000) == 99214750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 77,divisor2 = 42,uniqueCnt1 = 33000000,uniqueCnt2 = 66000000) == 99214750: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 6,divisor2 = 8,uniqueCnt1 = 99999999,uniqueCnt2 = 1) == 119999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 6,divisor2 = 8,uniqueCnt1 = 99999999,uniqueCnt2 = 1) == 119999998: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 5,divisor2 = 10,uniqueCnt1 = 50,uniqueCnt2 = 50) == 111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 5,divisor2 = 10,uniqueCnt1 = 50,uniqueCnt2 = 50) == 111: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 101,divisor2 = 103,uniqueCnt1 = 1000000,uniqueCnt2 = 1000000) == 2000192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 101,divisor2 = 103,uniqueCnt1 = 1000000,uniqueCnt2 = 1000000) == 2000192: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 23,divisor2 = 31,uniqueCnt1 = 50000000,uniqueCnt2 = 30000000) == 80112359
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 23,divisor2 = 31,uniqueCnt1 = 50000000,uniqueCnt2 = 30000000) == 80112359: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 11,divisor2 = 22,uniqueCnt1 = 100000000,uniqueCnt2 = 1) == 109999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 11,divisor2 = 22,uniqueCnt1 = 100000000,uniqueCnt2 = 1) == 109999999: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 11,divisor2 = 22,uniqueCnt1 = 300000000,uniqueCnt2 = 300000000) == 628571428
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 11,divisor2 = 22,uniqueCnt1 = 300000000,uniqueCnt2 = 300000000) == 628571428: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 23,divisor2 = 29,uniqueCnt1 = 100000,uniqueCnt2 = 100000) == 200300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 23,divisor2 = 29,uniqueCnt1 = 100000,uniqueCnt2 = 100000) == 200300: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 3,divisor2 = 5,uniqueCnt1 = 100000000,uniqueCnt2 = 50000000) == 160714285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 3,divisor2 = 5,uniqueCnt1 = 100000000,uniqueCnt2 = 50000000) == 160714285: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 5,divisor2 = 3,uniqueCnt1 = 100,uniqueCnt2 = 150) == 267
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 5,divisor2 = 3,uniqueCnt1 = 100,uniqueCnt2 = 150) == 267: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 7,divisor2 = 11,uniqueCnt1 = 10000000,uniqueCnt2 = 10000000) == 20263157
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 7,divisor2 = 11,uniqueCnt1 = 10000000,uniqueCnt2 = 10000000) == 20263157: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 4,divisor2 = 6,uniqueCnt1 = 250000000,uniqueCnt2 = 250000000) == 545454545
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 4,divisor2 = 6,uniqueCnt1 = 250000000,uniqueCnt2 = 250000000) == 545454545: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 8,divisor2 = 9,uniqueCnt1 = 2000000,uniqueCnt2 = 3000000) == 5070422
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 8,divisor2 = 9,uniqueCnt1 = 2000000,uniqueCnt2 = 3000000) == 5070422: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 100000,divisor2 = 99999,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 200000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 100000,divisor2 = 99999,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 200000000: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 10,divisor2 = 25,uniqueCnt1 = 50000000,uniqueCnt2 = 100000000) == 153061224
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 10,divisor2 = 25,uniqueCnt1 = 50000000,uniqueCnt2 = 100000000) == 153061224: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 5,divisor2 = 15,uniqueCnt1 = 100000000,uniqueCnt2 = 50000000) == 160714285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 5,divisor2 = 15,uniqueCnt1 = 100000000,uniqueCnt2 = 50000000) == 160714285: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 5,divisor2 = 10,uniqueCnt1 = 50000000,uniqueCnt2 = 49999999) == 111111109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 5,divisor2 = 10,uniqueCnt1 = 50000000,uniqueCnt2 = 49999999) == 111111109: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 100000,divisor2 = 200000,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 200001000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 100000,divisor2 = 200000,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 200001000: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 100000,divisor2 = 200000,uniqueCnt1 = 100000000,uniqueCnt2 = 50000000) == 150000750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 100000,divisor2 = 200000,uniqueCnt1 = 100000000,uniqueCnt2 = 50000000) == 150000750: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 2,divisor2 = 3,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 239999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 2,divisor2 = 3,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 239999999: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 2,divisor2 = 4,uniqueCnt1 = 99999999,uniqueCnt2 = 1) == 199999997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 2,divisor2 = 4,uniqueCnt1 = 99999999,uniqueCnt2 = 1) == 199999997: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 17,divisor2 = 29,uniqueCnt1 = 150000000,uniqueCnt2 = 150000000) == 300609756
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 17,divisor2 = 29,uniqueCnt1 = 150000000,uniqueCnt2 = 150000000) == 300609756: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 9,divisor2 = 12,uniqueCnt1 = 250000000,uniqueCnt2 = 250000000) == 514285714
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 9,divisor2 = 12,uniqueCnt1 = 250000000,uniqueCnt2 = 250000000) == 514285714: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 300000000,uniqueCnt2 = 200000000) == 502272727
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 300000000,uniqueCnt2 = 200000000) == 502272727: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 3,divisor2 = 5,uniqueCnt1 = 500000000,uniqueCnt2 = 400000000) == 964285714
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 3,divisor2 = 5,uniqueCnt1 = 500000000,uniqueCnt2 = 400000000) == 964285714: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 200909090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 200909090: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 71,divisor2 = 73,uniqueCnt1 = 10000000,uniqueCnt2 = 10000000) == 20003859
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 71,divisor2 = 73,uniqueCnt1 = 10000000,uniqueCnt2 = 10000000) == 20003859: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 99,divisor2 = 101,uniqueCnt1 = 200000000,uniqueCnt2 = 300000000) == 500050010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 99,divisor2 = 101,uniqueCnt1 = 200000000,uniqueCnt2 = 300000000) == 500050010: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 3,divisor2 = 6,uniqueCnt1 = 100,uniqueCnt2 = 200) == 359
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 3,divisor2 = 6,uniqueCnt1 = 100,uniqueCnt2 = 200) == 359: {e}')
    
    total += 1
    try:
        result = candidate(divisor1 = 10,divisor2 = 15,uniqueCnt1 = 80000000,uniqueCnt2 = 20000000) == 103448275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(divisor1 = 10,divisor2 = 15,uniqueCnt1 = 80000000,uniqueCnt2 = 20000000) == 103448275: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(divisor1 = 2,divisor2 = 7,uniqueCnt1 = 1,uniqueCnt2 = 3) == 4
    assert candidate(divisor1 = 2,divisor2 = 4,uniqueCnt1 = 8,uniqueCnt2 = 2) == 15
    assert candidate(divisor1 = 100,divisor2 = 101,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 200019803
    assert candidate(divisor1 = 100,divisor2 = 200,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 201005025
    assert candidate(divisor1 = 5,divisor2 = 10,uniqueCnt1 = 5,uniqueCnt2 = 5) == 11
    assert candidate(divisor1 = 7,divisor2 = 11,uniqueCnt1 = 10,uniqueCnt2 = 10) == 20
    assert candidate(divisor1 = 7,divisor2 = 13,uniqueCnt1 = 10,uniqueCnt2 = 10) == 20
    assert candidate(divisor1 = 3,divisor2 = 5,uniqueCnt1 = 2,uniqueCnt2 = 1) == 3
    assert candidate(divisor1 = 10,divisor2 = 15,uniqueCnt1 = 5,uniqueCnt2 = 6) == 11
    assert candidate(divisor1 = 7,divisor2 = 11,uniqueCnt1 = 3,uniqueCnt2 = 7) == 10
    assert candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 100454545
    assert candidate(divisor1 = 89,divisor2 = 97,uniqueCnt1 = 60000000,uniqueCnt2 = 40000000) == 100011584
    assert candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 20,uniqueCnt2 = 25) == 45
    assert candidate(divisor1 = 23,divisor2 = 29,uniqueCnt1 = 50000000,uniqueCnt2 = 30000000) == 80120120
    assert candidate(divisor1 = 13,divisor2 = 19,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 200813008
    assert candidate(divisor1 = 2,divisor2 = 3,uniqueCnt1 = 999999999,uniqueCnt2 = 1) == 1999999997
    assert candidate(divisor1 = 100000,divisor2 = 10000,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 100001000
    assert candidate(divisor1 = 100000,divisor2 = 200000,uniqueCnt1 = 1000000,uniqueCnt2 = 500000) == 1500007
    assert candidate(divisor1 = 30,divisor2 = 42,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 100478468
    assert candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 10000000,uniqueCnt2 = 20000000) == 30136363
    assert candidate(divisor1 = 45,divisor2 = 18,uniqueCnt1 = 200000000,uniqueCnt2 = 300000000) == 505617977
    assert candidate(divisor1 = 5,divisor2 = 7,uniqueCnt1 = 1,uniqueCnt2 = 999999999) == 1166666665
    assert candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 250000000,uniqueCnt2 = 250000000) == 502272727
    assert candidate(divisor1 = 61,divisor2 = 71,uniqueCnt1 = 70000000,uniqueCnt2 = 30000000) == 100023094
    assert candidate(divisor1 = 12,divisor2 = 18,uniqueCnt1 = 1000,uniqueCnt2 = 1000) == 2057
    assert candidate(divisor1 = 2,divisor2 = 5,uniqueCnt1 = 500000000,uniqueCnt2 = 499999999) == 1111111109
    assert candidate(divisor1 = 4,divisor2 = 6,uniqueCnt1 = 5,uniqueCnt2 = 8) == 14
    assert candidate(divisor1 = 4,divisor2 = 6,uniqueCnt1 = 300000000,uniqueCnt2 = 200000000) == 545454545
    assert candidate(divisor1 = 10000,divisor2 = 20000,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 100005000
    assert candidate(divisor1 = 8,divisor2 = 12,uniqueCnt1 = 40000000,uniqueCnt2 = 60000000) == 104347826
    assert candidate(divisor1 = 99999,divisor2 = 99998,uniqueCnt1 = 100000,uniqueCnt2 = 100000) == 200000
    assert candidate(divisor1 = 50000,divisor2 = 100000,uniqueCnt1 = 10000000,uniqueCnt2 = 10000000) == 20000200
    assert candidate(divisor1 = 29,divisor2 = 41,uniqueCnt1 = 60000000,uniqueCnt2 = 40000000) == 100084175
    assert candidate(divisor1 = 15,divisor2 = 20,uniqueCnt1 = 75000000,uniqueCnt2 = 25000000) == 101694915
    assert candidate(divisor1 = 19,divisor2 = 23,uniqueCnt1 = 150000000,uniqueCnt2 = 150000000) == 300688073
    assert candidate(divisor1 = 3,divisor2 = 5,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 107142857
    assert candidate(divisor1 = 50000,divisor2 = 75000,uniqueCnt1 = 60000000,uniqueCnt2 = 40000000) == 100000666
    assert candidate(divisor1 = 20,divisor2 = 30,uniqueCnt1 = 500000000,uniqueCnt2 = 400000000) == 915254237
    assert candidate(divisor1 = 6,divisor2 = 8,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 104347826
    assert candidate(divisor1 = 100000,divisor2 = 50000,uniqueCnt1 = 50000000,uniqueCnt2 = 40000000) == 90000900
    assert candidate(divisor1 = 10,divisor2 = 15,uniqueCnt1 = 75000000,uniqueCnt2 = 25000000) == 103448275
    assert candidate(divisor1 = 100000,divisor2 = 100000,uniqueCnt1 = 450000000,uniqueCnt2 = 450000000) == 900009000
    assert candidate(divisor1 = 7,divisor2 = 14,uniqueCnt1 = 900000000,uniqueCnt2 = 900000000) == 1938461538
    assert candidate(divisor1 = 23,divisor2 = 37,uniqueCnt1 = 50000000,uniqueCnt2 = 49999999) == 100117646
    assert candidate(divisor1 = 99999,divisor2 = 100001,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 100000000
    assert candidate(divisor1 = 23,divisor2 = 37,uniqueCnt1 = 45000000,uniqueCnt2 = 55000000) == 100117647
    assert candidate(divisor1 = 11,divisor2 = 13,uniqueCnt1 = 100,uniqueCnt2 = 150) == 251
    assert candidate(divisor1 = 3,divisor2 = 5,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 214285714
    assert candidate(divisor1 = 1000,divisor2 = 500,uniqueCnt1 = 40000000,uniqueCnt2 = 60000000) == 100100100
    assert candidate(divisor1 = 4,divisor2 = 6,uniqueCnt1 = 100000000,uniqueCnt2 = 99999999) == 218181817
    assert candidate(divisor1 = 5,divisor2 = 7,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 102941176
    assert candidate(divisor1 = 17,divisor2 = 31,uniqueCnt1 = 99999999,uniqueCnt2 = 1) == 106249998
    assert candidate(divisor1 = 99998,divisor2 = 99999,uniqueCnt1 = 100000,uniqueCnt2 = 100000) == 200000
    assert candidate(divisor1 = 10,divisor2 = 15,uniqueCnt1 = 100000000,uniqueCnt2 = 1) == 111111111
    assert candidate(divisor1 = 4,divisor2 = 6,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 218181818
    assert candidate(divisor1 = 6,divisor2 = 8,uniqueCnt1 = 75000000,uniqueCnt2 = 25000000) == 104347826
    assert candidate(divisor1 = 77,divisor2 = 42,uniqueCnt1 = 500,uniqueCnt2 = 500) == 1002
    assert candidate(divisor1 = 11,divisor2 = 13,uniqueCnt1 = 20000000,uniqueCnt2 = 15000000) == 35246478
    assert candidate(divisor1 = 7,divisor2 = 14,uniqueCnt1 = 25000000,uniqueCnt2 = 25000000) == 53846153
    assert candidate(divisor1 = 15,divisor2 = 25,uniqueCnt1 = 80000000,uniqueCnt2 = 70000000) == 152027027
    assert candidate(divisor1 = 11,divisor2 = 13,uniqueCnt1 = 99999999,uniqueCnt2 = 99999999) == 201408448
    assert candidate(divisor1 = 3,divisor2 = 5,uniqueCnt1 = 100,uniqueCnt2 = 200) == 321
    assert candidate(divisor1 = 25,divisor2 = 40,uniqueCnt1 = 100,uniqueCnt2 = 150) == 251
    assert candidate(divisor1 = 100001,divisor2 = 100003,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 200000000
    assert candidate(divisor1 = 6,divisor2 = 9,uniqueCnt1 = 15,uniqueCnt2 = 20) == 37
    assert candidate(divisor1 = 6,divisor2 = 9,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 105882352
    assert candidate(divisor1 = 23,divisor2 = 31,uniqueCnt1 = 200000000,uniqueCnt2 = 300000000) == 500702247
    assert candidate(divisor1 = 5,divisor2 = 6,uniqueCnt1 = 1000000,uniqueCnt2 = 500000) == 1551724
    assert candidate(divisor1 = 67,divisor2 = 89,uniqueCnt1 = 400000000,uniqueCnt2 = 400000000) == 800134183
    assert candidate(divisor1 = 11,divisor2 = 13,uniqueCnt1 = 200000000,uniqueCnt2 = 1) == 219999999
    assert candidate(divisor1 = 37,divisor2 = 41,uniqueCnt1 = 9876543,uniqueCnt2 = 1234567) == 11118439
    assert candidate(divisor1 = 7,divisor2 = 13,uniqueCnt1 = 300000000,uniqueCnt2 = 300000000) == 606666666
    assert candidate(divisor1 = 5,divisor2 = 7,uniqueCnt1 = 99999999,uniqueCnt2 = 1) == 124999998
    assert candidate(divisor1 = 97,divisor2 = 101,uniqueCnt1 = 1000000,uniqueCnt2 = 500000) == 1500153
    assert candidate(divisor1 = 10000,divisor2 = 100000,uniqueCnt1 = 90000000,uniqueCnt2 = 10000000) == 100001000
    assert candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 5,uniqueCnt2 = 10) == 15
    assert candidate(divisor1 = 10,divisor2 = 15,uniqueCnt1 = 100000000,uniqueCnt2 = 200000000) == 310344827
    assert candidate(divisor1 = 100000,divisor2 = 200000,uniqueCnt1 = 50000000,uniqueCnt2 = 50000000) == 100000500
    assert candidate(divisor1 = 77,divisor2 = 42,uniqueCnt1 = 33000000,uniqueCnt2 = 66000000) == 99214750
    assert candidate(divisor1 = 6,divisor2 = 8,uniqueCnt1 = 99999999,uniqueCnt2 = 1) == 119999998
    assert candidate(divisor1 = 5,divisor2 = 10,uniqueCnt1 = 50,uniqueCnt2 = 50) == 111
    assert candidate(divisor1 = 101,divisor2 = 103,uniqueCnt1 = 1000000,uniqueCnt2 = 1000000) == 2000192
    assert candidate(divisor1 = 23,divisor2 = 31,uniqueCnt1 = 50000000,uniqueCnt2 = 30000000) == 80112359
    assert candidate(divisor1 = 11,divisor2 = 22,uniqueCnt1 = 100000000,uniqueCnt2 = 1) == 109999999
    assert candidate(divisor1 = 11,divisor2 = 22,uniqueCnt1 = 300000000,uniqueCnt2 = 300000000) == 628571428
    assert candidate(divisor1 = 23,divisor2 = 29,uniqueCnt1 = 100000,uniqueCnt2 = 100000) == 200300
    assert candidate(divisor1 = 3,divisor2 = 5,uniqueCnt1 = 100000000,uniqueCnt2 = 50000000) == 160714285
    assert candidate(divisor1 = 5,divisor2 = 3,uniqueCnt1 = 100,uniqueCnt2 = 150) == 267
    assert candidate(divisor1 = 7,divisor2 = 11,uniqueCnt1 = 10000000,uniqueCnt2 = 10000000) == 20263157
    assert candidate(divisor1 = 4,divisor2 = 6,uniqueCnt1 = 250000000,uniqueCnt2 = 250000000) == 545454545
    assert candidate(divisor1 = 8,divisor2 = 9,uniqueCnt1 = 2000000,uniqueCnt2 = 3000000) == 5070422
    assert candidate(divisor1 = 100000,divisor2 = 99999,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 200000000
    assert candidate(divisor1 = 10,divisor2 = 25,uniqueCnt1 = 50000000,uniqueCnt2 = 100000000) == 153061224
    assert candidate(divisor1 = 5,divisor2 = 15,uniqueCnt1 = 100000000,uniqueCnt2 = 50000000) == 160714285
    assert candidate(divisor1 = 5,divisor2 = 10,uniqueCnt1 = 50000000,uniqueCnt2 = 49999999) == 111111109
    assert candidate(divisor1 = 100000,divisor2 = 200000,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 200001000
    assert candidate(divisor1 = 100000,divisor2 = 200000,uniqueCnt1 = 100000000,uniqueCnt2 = 50000000) == 150000750
    assert candidate(divisor1 = 2,divisor2 = 3,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 239999999
    assert candidate(divisor1 = 2,divisor2 = 4,uniqueCnt1 = 99999999,uniqueCnt2 = 1) == 199999997
    assert candidate(divisor1 = 17,divisor2 = 29,uniqueCnt1 = 150000000,uniqueCnt2 = 150000000) == 300609756
    assert candidate(divisor1 = 9,divisor2 = 12,uniqueCnt1 = 250000000,uniqueCnt2 = 250000000) == 514285714
    assert candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 300000000,uniqueCnt2 = 200000000) == 502272727
    assert candidate(divisor1 = 3,divisor2 = 5,uniqueCnt1 = 500000000,uniqueCnt2 = 400000000) == 964285714
    assert candidate(divisor1 = 13,divisor2 = 17,uniqueCnt1 = 100000000,uniqueCnt2 = 100000000) == 200909090
    assert candidate(divisor1 = 71,divisor2 = 73,uniqueCnt1 = 10000000,uniqueCnt2 = 10000000) == 20003859
    assert candidate(divisor1 = 99,divisor2 = 101,uniqueCnt1 = 200000000,uniqueCnt2 = 300000000) == 500050010
    assert candidate(divisor1 = 3,divisor2 = 6,uniqueCnt1 = 100,uniqueCnt2 = 200) == 359
    assert candidate(divisor1 = 10,divisor2 = 15,uniqueCnt1 = 80000000,uniqueCnt2 = 20000000) == 103448275


