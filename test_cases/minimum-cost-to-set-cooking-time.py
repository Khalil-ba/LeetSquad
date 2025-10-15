def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(startAt = 1,moveCost = 2,pushCost = 1,targetSeconds = 600) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 1,moveCost = 2,pushCost = 1,targetSeconds = 600) == 6: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 0,moveCost = 1,pushCost = 2,targetSeconds = 76) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 0,moveCost = 1,pushCost = 2,targetSeconds = 76) == 6: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 2,moveCost = 2,pushCost = 3,targetSeconds = 599) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 2,moveCost = 2,pushCost = 3,targetSeconds = 599) == 15: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 6,moveCost = 3,pushCost = 2,targetSeconds = 3599) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 6,moveCost = 3,pushCost = 2,targetSeconds = 3599) == 20: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 9,moveCost = 5,pushCost = 10,targetSeconds = 99) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 9,moveCost = 5,pushCost = 10,targetSeconds = 99) == 20: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 5,moveCost = 1,pushCost = 1,targetSeconds = 120) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 5,moveCost = 1,pushCost = 1,targetSeconds = 120) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 3,moveCost = 3,pushCost = 2,targetSeconds = 300) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 3,moveCost = 3,pushCost = 2,targetSeconds = 300) == 12: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 8,moveCost = 2,pushCost = 1,targetSeconds = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 8,moveCost = 2,pushCost = 1,targetSeconds = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 7,moveCost = 4,pushCost = 5,targetSeconds = 180) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 7,moveCost = 4,pushCost = 5,targetSeconds = 180) == 23: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 4,moveCost = 1,pushCost = 1,targetSeconds = 6039) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 4,moveCost = 1,pushCost = 1,targetSeconds = 6039) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 7,moveCost = 6,pushCost = 3,targetSeconds = 59) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 7,moveCost = 6,pushCost = 3,targetSeconds = 59) == 18: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 8,moveCost = 3,pushCost = 5,targetSeconds = 3001) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 8,moveCost = 3,pushCost = 5,targetSeconds = 3001) == 29: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 9,moveCost = 2,pushCost = 1,targetSeconds = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 9,moveCost = 2,pushCost = 1,targetSeconds = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 9,moveCost = 1,pushCost = 10,targetSeconds = 6039) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 9,moveCost = 1,pushCost = 10,targetSeconds = 6039) == 40: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 4,moveCost = 30,pushCost = 20,targetSeconds = 1234) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 4,moveCost = 30,pushCost = 20,targetSeconds = 1234) == 170: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 0,moveCost = 6,pushCost = 5,targetSeconds = 99) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 0,moveCost = 6,pushCost = 5,targetSeconds = 99) == 16: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 6,moveCost = 5,pushCost = 1,targetSeconds = 480) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 6,moveCost = 5,pushCost = 1,targetSeconds = 480) == 13: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 0,moveCost = 1,pushCost = 10,targetSeconds = 1000) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 0,moveCost = 1,pushCost = 10,targetSeconds = 1000) == 44: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 1,moveCost = 8,pushCost = 5,targetSeconds = 1234) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 1,moveCost = 8,pushCost = 5,targetSeconds = 1234) == 36: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 7,moveCost = 200,pushCost = 150,targetSeconds = 99) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 7,moveCost = 200,pushCost = 150,targetSeconds = 99) == 500: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 9,moveCost = 5,pushCost = 2,targetSeconds = 6039) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 9,moveCost = 5,pushCost = 2,targetSeconds = 6039) == 8: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 8,moveCost = 2,pushCost = 2,targetSeconds = 2039) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 8,moveCost = 2,pushCost = 2,targetSeconds = 2039) == 14: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 6,moveCost = 2,pushCost = 1,targetSeconds = 99) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 6,moveCost = 2,pushCost = 1,targetSeconds = 99) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 6,moveCost = 1,pushCost = 1,targetSeconds = 59) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 6,moveCost = 1,pushCost = 1,targetSeconds = 59) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 5,moveCost = 15,pushCost = 25,targetSeconds = 2345) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 5,moveCost = 15,pushCost = 25,targetSeconds = 2345) == 160: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 7,moveCost = 2,pushCost = 1,targetSeconds = 99) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 7,moveCost = 2,pushCost = 1,targetSeconds = 99) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 1,moveCost = 20,pushCost = 5,targetSeconds = 900) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 1,moveCost = 20,pushCost = 5,targetSeconds = 900) == 60: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 2,moveCost = 5,pushCost = 3,targetSeconds = 5999) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 2,moveCost = 5,pushCost = 3,targetSeconds = 5999) == 27: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 9,moveCost = 10,pushCost = 1,targetSeconds = 1234) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 9,moveCost = 10,pushCost = 1,targetSeconds = 1234) == 34: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 2,moveCost = 1,pushCost = 5,targetSeconds = 240) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 2,moveCost = 1,pushCost = 5,targetSeconds = 240) == 17: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 9,moveCost = 5,pushCost = 3,targetSeconds = 6039) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 9,moveCost = 5,pushCost = 3,targetSeconds = 6039) == 12: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 1,moveCost = 4,pushCost = 4,targetSeconds = 3159) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 1,moveCost = 4,pushCost = 4,targetSeconds = 3159) == 28: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 4,moveCost = 3,pushCost = 7,targetSeconds = 60) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 4,moveCost = 3,pushCost = 7,targetSeconds = 60) == 20: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 1,moveCost = 5,pushCost = 1,targetSeconds = 9999) == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 1,moveCost = 5,pushCost = 1,targetSeconds = 9999) == inf: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 8,moveCost = 3,pushCost = 7,targetSeconds = 119) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 8,moveCost = 3,pushCost = 7,targetSeconds = 119) == 30: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 0,moveCost = 20,pushCost = 10,targetSeconds = 3600) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 0,moveCost = 20,pushCost = 10,targetSeconds = 3600) == 80: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 3,moveCost = 2,pushCost = 3,targetSeconds = 3540) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 3,moveCost = 2,pushCost = 3,targetSeconds = 3540) == 18: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 3,moveCost = 5,pushCost = 3,targetSeconds = 5999) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 3,moveCost = 5,pushCost = 3,targetSeconds = 5999) == 27: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 6,moveCost = 3,pushCost = 7,targetSeconds = 2900) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 6,moveCost = 3,pushCost = 7,targetSeconds = 2900) == 40: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 5,moveCost = 5,pushCost = 3,targetSeconds = 5999) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 5,moveCost = 5,pushCost = 3,targetSeconds = 5999) == 27: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 0,moveCost = 7,pushCost = 2,targetSeconds = 4567) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 0,moveCost = 7,pushCost = 2,targetSeconds = 4567) == 36: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 9,moveCost = 10,pushCost = 1,targetSeconds = 6039) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 9,moveCost = 10,pushCost = 1,targetSeconds = 6039) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 5,moveCost = 7,pushCost = 2,targetSeconds = 5432) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 5,moveCost = 7,pushCost = 2,targetSeconds = 5432) == 29: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 1,moveCost = 1,pushCost = 10,targetSeconds = 300) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 1,moveCost = 1,pushCost = 10,targetSeconds = 300) == 32: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 4,moveCost = 10,pushCost = 1,targetSeconds = 1800) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 4,moveCost = 10,pushCost = 1,targetSeconds = 1800) == 24: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 8,moveCost = 10,pushCost = 5,targetSeconds = 900) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 8,moveCost = 10,pushCost = 5,targetSeconds = 900) == 50: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 5,moveCost = 7,pushCost = 4,targetSeconds = 1234) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 5,moveCost = 7,pushCost = 4,targetSeconds = 1234) == 37: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 2,moveCost = 15,pushCost = 3,targetSeconds = 480) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 2,moveCost = 15,pushCost = 3,targetSeconds = 480) == 39: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 1,moveCost = 100,pushCost = 50,targetSeconds = 120) == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 1,moveCost = 100,pushCost = 50,targetSeconds = 120) == 350: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 6,moveCost = 50,pushCost = 25,targetSeconds = 1800) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 6,moveCost = 50,pushCost = 25,targetSeconds = 1800) == 200: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 7,moveCost = 1,pushCost = 2,targetSeconds = 6000) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 7,moveCost = 1,pushCost = 2,targetSeconds = 6000) == 11: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 3,moveCost = 2,pushCost = 3,targetSeconds = 300) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 3,moveCost = 2,pushCost = 3,targetSeconds = 300) == 13: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 2,moveCost = 4,pushCost = 6,targetSeconds = 2345) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 2,moveCost = 4,pushCost = 6,targetSeconds = 2345) == 40: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 0,moveCost = 1,pushCost = 1000,targetSeconds = 60) == 2002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 0,moveCost = 1,pushCost = 1000,targetSeconds = 60) == 2002: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 4,moveCost = 7,pushCost = 4,targetSeconds = 360) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 4,moveCost = 7,pushCost = 4,targetSeconds = 360) == 26: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 5,moveCost = 20,pushCost = 10,targetSeconds = 3540) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 5,moveCost = 20,pushCost = 10,targetSeconds = 3540) == 80: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 9,moveCost = 7,pushCost = 4,targetSeconds = 5999) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 9,moveCost = 7,pushCost = 4,targetSeconds = 5999) == 30: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 4,moveCost = 3,pushCost = 4,targetSeconds = 1000) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 4,moveCost = 3,pushCost = 4,targetSeconds = 1000) == 28: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 1,moveCost = 1,pushCost = 9,targetSeconds = 50) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 1,moveCost = 1,pushCost = 9,targetSeconds = 50) == 20: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 6,moveCost = 2,pushCost = 1,targetSeconds = 59) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 6,moveCost = 2,pushCost = 1,targetSeconds = 59) == 6: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 9,moveCost = 10,pushCost = 2,targetSeconds = 5959) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 9,moveCost = 10,pushCost = 2,targetSeconds = 5959) == 28: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 0,moveCost = 2,pushCost = 1,targetSeconds = 120) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 0,moveCost = 2,pushCost = 1,targetSeconds = 120) == 7: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 4,moveCost = 2,pushCost = 3,targetSeconds = 60) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 4,moveCost = 2,pushCost = 3,targetSeconds = 60) == 10: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 7,moveCost = 4,pushCost = 2,targetSeconds = 60) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 7,moveCost = 4,pushCost = 2,targetSeconds = 60) == 12: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 3,moveCost = 2,pushCost = 3,targetSeconds = 4321) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 3,moveCost = 2,pushCost = 3,targetSeconds = 4321) == 20: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 3,moveCost = 5,pushCost = 3,targetSeconds = 2345) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 3,moveCost = 5,pushCost = 3,targetSeconds = 2345) == 27: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 8,moveCost = 2,pushCost = 3,targetSeconds = 100) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 8,moveCost = 2,pushCost = 3,targetSeconds = 100) == 15: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 7,moveCost = 9,pushCost = 3,targetSeconds = 3598) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 7,moveCost = 9,pushCost = 3,targetSeconds = 3598) == 48: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 8,moveCost = 7,pushCost = 4,targetSeconds = 1000) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 8,moveCost = 7,pushCost = 4,targetSeconds = 1000) == 44: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 2,moveCost = 15,pushCost = 3,targetSeconds = 123) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 2,moveCost = 15,pushCost = 3,targetSeconds = 123) == 39: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 5,moveCost = 10,pushCost = 5,targetSeconds = 3149) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 5,moveCost = 10,pushCost = 5,targetSeconds = 3149) == 40: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 1,moveCost = 9,pushCost = 2,targetSeconds = 999) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 1,moveCost = 9,pushCost = 2,targetSeconds = 999) == 26: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 8,moveCost = 15,pushCost = 8,targetSeconds = 4321) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 8,moveCost = 15,pushCost = 8,targetSeconds = 4321) == 92: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 1,moveCost = 1,pushCost = 1,targetSeconds = 359) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 1,moveCost = 1,pushCost = 1,targetSeconds = 359) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 5,moveCost = 1,pushCost = 10,targetSeconds = 3959) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 5,moveCost = 1,pushCost = 10,targetSeconds = 3959) == 43: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 9,moveCost = 2,pushCost = 4,targetSeconds = 5999) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 9,moveCost = 2,pushCost = 4,targetSeconds = 5999) == 20: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 2,moveCost = 6,pushCost = 2,targetSeconds = 5678) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 2,moveCost = 6,pushCost = 2,targetSeconds = 5678) == 32: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 8,moveCost = 3,pushCost = 4,targetSeconds = 6039) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 8,moveCost = 3,pushCost = 4,targetSeconds = 6039) == 19: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 3,moveCost = 5,pushCost = 3,targetSeconds = 5400) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 3,moveCost = 5,pushCost = 3,targetSeconds = 5400) == 22: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 6,moveCost = 3,pushCost = 4,targetSeconds = 999) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 6,moveCost = 3,pushCost = 4,targetSeconds = 999) == 25: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 3,moveCost = 1,pushCost = 5,targetSeconds = 90) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 3,moveCost = 1,pushCost = 5,targetSeconds = 90) == 12: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 0,moveCost = 10,pushCost = 1,targetSeconds = 5999) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 0,moveCost = 10,pushCost = 1,targetSeconds = 5999) == 34: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 9,moveCost = 1,pushCost = 2,targetSeconds = 123) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 9,moveCost = 1,pushCost = 2,targetSeconds = 123) == 9: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 3,moveCost = 4,pushCost = 2,targetSeconds = 300) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 3,moveCost = 4,pushCost = 2,targetSeconds = 300) == 14: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 5,moveCost = 7,pushCost = 3,targetSeconds = 1234) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 5,moveCost = 7,pushCost = 3,targetSeconds = 1234) == 33: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 8,moveCost = 5,pushCost = 3,targetSeconds = 60) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 8,moveCost = 5,pushCost = 3,targetSeconds = 60) == 16: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 8,moveCost = 3,pushCost = 2,targetSeconds = 99) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 8,moveCost = 3,pushCost = 2,targetSeconds = 99) == 7: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 3,moveCost = 2,pushCost = 3,targetSeconds = 60) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 3,moveCost = 2,pushCost = 3,targetSeconds = 60) == 10: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 9,moveCost = 5,pushCost = 10,targetSeconds = 5999) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 9,moveCost = 5,pushCost = 10,targetSeconds = 5999) == 50: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 8,moveCost = 3,pushCost = 5,targetSeconds = 59) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 8,moveCost = 3,pushCost = 5,targetSeconds = 59) == 16: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 2,moveCost = 4,pushCost = 5,targetSeconds = 720) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 2,moveCost = 4,pushCost = 5,targetSeconds = 720) == 32: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 4,moveCost = 4,pushCost = 4,targetSeconds = 5432) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 4,moveCost = 4,pushCost = 4,targetSeconds = 5432) == 28: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 7,moveCost = 7,pushCost = 8,targetSeconds = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 7,moveCost = 7,pushCost = 8,targetSeconds = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 0,moveCost = 5,pushCost = 10,targetSeconds = 360) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 0,moveCost = 5,pushCost = 10,targetSeconds = 360) == 40: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 0,moveCost = 7,pushCost = 1,targetSeconds = 5999) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 0,moveCost = 7,pushCost = 1,targetSeconds = 5999) == 25: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 6,moveCost = 4,pushCost = 6,targetSeconds = 200) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 6,moveCost = 4,pushCost = 6,targetSeconds = 200) == 30: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 9,moveCost = 10,pushCost = 1,targetSeconds = 5432) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 9,moveCost = 10,pushCost = 1,targetSeconds = 5432) == 34: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 2,moveCost = 2,pushCost = 3,targetSeconds = 3600) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 2,moveCost = 2,pushCost = 3,targetSeconds = 3600) == 16: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 5,moveCost = 10,pushCost = 5,targetSeconds = 3999) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 5,moveCost = 10,pushCost = 5,targetSeconds = 3999) == 50: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 2,moveCost = 10,pushCost = 5,targetSeconds = 3660) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 2,moveCost = 10,pushCost = 5,targetSeconds = 3660) == 50: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 0,moveCost = 3,pushCost = 7,targetSeconds = 90) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 0,moveCost = 3,pushCost = 7,targetSeconds = 90) == 20: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 3,moveCost = 1,pushCost = 1,targetSeconds = 599) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 3,moveCost = 1,pushCost = 1,targetSeconds = 599) == 6: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 7,moveCost = 6,pushCost = 4,targetSeconds = 4567) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 7,moveCost = 6,pushCost = 4,targetSeconds = 4567) == 34: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 3,moveCost = 20,pushCost = 5,targetSeconds = 300) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 3,moveCost = 20,pushCost = 5,targetSeconds = 300) == 55: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 4,moveCost = 6,pushCost = 2,targetSeconds = 900) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 4,moveCost = 6,pushCost = 2,targetSeconds = 900) == 26: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 1,moveCost = 5,pushCost = 1,targetSeconds = 540) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 1,moveCost = 5,pushCost = 1,targetSeconds = 540) == 13: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 6,moveCost = 15,pushCost = 5,targetSeconds = 999) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 6,moveCost = 15,pushCost = 5,targetSeconds = 999) == 65: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 5,moveCost = 1,pushCost = 2,targetSeconds = 480) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 5,moveCost = 1,pushCost = 2,targetSeconds = 480) == 8: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 0,moveCost = 3,pushCost = 2,targetSeconds = 120) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 0,moveCost = 3,pushCost = 2,targetSeconds = 120) == 12: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 2,moveCost = 1,pushCost = 1,targetSeconds = 99) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 2,moveCost = 1,pushCost = 1,targetSeconds = 99) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 1,moveCost = 6,pushCost = 1,targetSeconds = 59) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 1,moveCost = 6,pushCost = 1,targetSeconds = 59) == 14: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 7,moveCost = 2,pushCost = 6,targetSeconds = 1000) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 7,moveCost = 2,pushCost = 6,targetSeconds = 1000) == 32: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 4,moveCost = 4,pushCost = 3,targetSeconds = 1500) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 4,moveCost = 4,pushCost = 3,targetSeconds = 1500) == 24: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 6,moveCost = 2,pushCost = 9,targetSeconds = 9999) == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 6,moveCost = 2,pushCost = 9,targetSeconds = 9999) == inf: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 0,moveCost = 1,pushCost = 1,targetSeconds = 1234) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 0,moveCost = 1,pushCost = 1,targetSeconds = 1234) == 7: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 2,moveCost = 20,pushCost = 10,targetSeconds = 1020) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 2,moveCost = 20,pushCost = 10,targetSeconds = 1020) == 100: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 4,moveCost = 8,pushCost = 2,targetSeconds = 100) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 4,moveCost = 8,pushCost = 2,targetSeconds = 100) == 30: {e}')
    
    total += 1
    try:
        result = candidate(startAt = 7,moveCost = 5,pushCost = 2,targetSeconds = 1234) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startAt = 7,moveCost = 5,pushCost = 2,targetSeconds = 1234) == 23: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(startAt = 1,moveCost = 2,pushCost = 1,targetSeconds = 600) == 6
    assert candidate(startAt = 0,moveCost = 1,pushCost = 2,targetSeconds = 76) == 6
    assert candidate(startAt = 2,moveCost = 2,pushCost = 3,targetSeconds = 599) == 15
    assert candidate(startAt = 6,moveCost = 3,pushCost = 2,targetSeconds = 3599) == 20
    assert candidate(startAt = 9,moveCost = 5,pushCost = 10,targetSeconds = 99) == 20
    assert candidate(startAt = 5,moveCost = 1,pushCost = 1,targetSeconds = 120) == 5
    assert candidate(startAt = 3,moveCost = 3,pushCost = 2,targetSeconds = 300) == 12
    assert candidate(startAt = 8,moveCost = 2,pushCost = 1,targetSeconds = 1) == 3
    assert candidate(startAt = 7,moveCost = 4,pushCost = 5,targetSeconds = 180) == 23
    assert candidate(startAt = 4,moveCost = 1,pushCost = 1,targetSeconds = 6039) == 5
    assert candidate(startAt = 7,moveCost = 6,pushCost = 3,targetSeconds = 59) == 18
    assert candidate(startAt = 8,moveCost = 3,pushCost = 5,targetSeconds = 3001) == 29
    assert candidate(startAt = 9,moveCost = 2,pushCost = 1,targetSeconds = 1) == 3
    assert candidate(startAt = 9,moveCost = 1,pushCost = 10,targetSeconds = 6039) == 40
    assert candidate(startAt = 4,moveCost = 30,pushCost = 20,targetSeconds = 1234) == 170
    assert candidate(startAt = 0,moveCost = 6,pushCost = 5,targetSeconds = 99) == 16
    assert candidate(startAt = 6,moveCost = 5,pushCost = 1,targetSeconds = 480) == 13
    assert candidate(startAt = 0,moveCost = 1,pushCost = 10,targetSeconds = 1000) == 44
    assert candidate(startAt = 1,moveCost = 8,pushCost = 5,targetSeconds = 1234) == 36
    assert candidate(startAt = 7,moveCost = 200,pushCost = 150,targetSeconds = 99) == 500
    assert candidate(startAt = 9,moveCost = 5,pushCost = 2,targetSeconds = 6039) == 8
    assert candidate(startAt = 8,moveCost = 2,pushCost = 2,targetSeconds = 2039) == 14
    assert candidate(startAt = 6,moveCost = 2,pushCost = 1,targetSeconds = 99) == 4
    assert candidate(startAt = 6,moveCost = 1,pushCost = 1,targetSeconds = 59) == 4
    assert candidate(startAt = 5,moveCost = 15,pushCost = 25,targetSeconds = 2345) == 160
    assert candidate(startAt = 7,moveCost = 2,pushCost = 1,targetSeconds = 99) == 4
    assert candidate(startAt = 1,moveCost = 20,pushCost = 5,targetSeconds = 900) == 60
    assert candidate(startAt = 2,moveCost = 5,pushCost = 3,targetSeconds = 5999) == 27
    assert candidate(startAt = 9,moveCost = 10,pushCost = 1,targetSeconds = 1234) == 34
    assert candidate(startAt = 2,moveCost = 1,pushCost = 5,targetSeconds = 240) == 17
    assert candidate(startAt = 9,moveCost = 5,pushCost = 3,targetSeconds = 6039) == 12
    assert candidate(startAt = 1,moveCost = 4,pushCost = 4,targetSeconds = 3159) == 28
    assert candidate(startAt = 4,moveCost = 3,pushCost = 7,targetSeconds = 60) == 20
    assert candidate(startAt = 1,moveCost = 5,pushCost = 1,targetSeconds = 9999) == inf
    assert candidate(startAt = 8,moveCost = 3,pushCost = 7,targetSeconds = 119) == 30
    assert candidate(startAt = 0,moveCost = 20,pushCost = 10,targetSeconds = 3600) == 80
    assert candidate(startAt = 3,moveCost = 2,pushCost = 3,targetSeconds = 3540) == 18
    assert candidate(startAt = 3,moveCost = 5,pushCost = 3,targetSeconds = 5999) == 27
    assert candidate(startAt = 6,moveCost = 3,pushCost = 7,targetSeconds = 2900) == 40
    assert candidate(startAt = 5,moveCost = 5,pushCost = 3,targetSeconds = 5999) == 27
    assert candidate(startAt = 0,moveCost = 7,pushCost = 2,targetSeconds = 4567) == 36
    assert candidate(startAt = 9,moveCost = 10,pushCost = 1,targetSeconds = 6039) == 4
    assert candidate(startAt = 5,moveCost = 7,pushCost = 2,targetSeconds = 5432) == 29
    assert candidate(startAt = 1,moveCost = 1,pushCost = 10,targetSeconds = 300) == 32
    assert candidate(startAt = 4,moveCost = 10,pushCost = 1,targetSeconds = 1800) == 24
    assert candidate(startAt = 8,moveCost = 10,pushCost = 5,targetSeconds = 900) == 50
    assert candidate(startAt = 5,moveCost = 7,pushCost = 4,targetSeconds = 1234) == 37
    assert candidate(startAt = 2,moveCost = 15,pushCost = 3,targetSeconds = 480) == 39
    assert candidate(startAt = 1,moveCost = 100,pushCost = 50,targetSeconds = 120) == 350
    assert candidate(startAt = 6,moveCost = 50,pushCost = 25,targetSeconds = 1800) == 200
    assert candidate(startAt = 7,moveCost = 1,pushCost = 2,targetSeconds = 6000) == 11
    assert candidate(startAt = 3,moveCost = 2,pushCost = 3,targetSeconds = 300) == 13
    assert candidate(startAt = 2,moveCost = 4,pushCost = 6,targetSeconds = 2345) == 40
    assert candidate(startAt = 0,moveCost = 1,pushCost = 1000,targetSeconds = 60) == 2002
    assert candidate(startAt = 4,moveCost = 7,pushCost = 4,targetSeconds = 360) == 26
    assert candidate(startAt = 5,moveCost = 20,pushCost = 10,targetSeconds = 3540) == 80
    assert candidate(startAt = 9,moveCost = 7,pushCost = 4,targetSeconds = 5999) == 30
    assert candidate(startAt = 4,moveCost = 3,pushCost = 4,targetSeconds = 1000) == 28
    assert candidate(startAt = 1,moveCost = 1,pushCost = 9,targetSeconds = 50) == 20
    assert candidate(startAt = 6,moveCost = 2,pushCost = 1,targetSeconds = 59) == 6
    assert candidate(startAt = 9,moveCost = 10,pushCost = 2,targetSeconds = 5959) == 28
    assert candidate(startAt = 0,moveCost = 2,pushCost = 1,targetSeconds = 120) == 7
    assert candidate(startAt = 4,moveCost = 2,pushCost = 3,targetSeconds = 60) == 10
    assert candidate(startAt = 7,moveCost = 4,pushCost = 2,targetSeconds = 60) == 12
    assert candidate(startAt = 3,moveCost = 2,pushCost = 3,targetSeconds = 4321) == 20
    assert candidate(startAt = 3,moveCost = 5,pushCost = 3,targetSeconds = 2345) == 27
    assert candidate(startAt = 8,moveCost = 2,pushCost = 3,targetSeconds = 100) == 15
    assert candidate(startAt = 7,moveCost = 9,pushCost = 3,targetSeconds = 3598) == 48
    assert candidate(startAt = 8,moveCost = 7,pushCost = 4,targetSeconds = 1000) == 44
    assert candidate(startAt = 2,moveCost = 15,pushCost = 3,targetSeconds = 123) == 39
    assert candidate(startAt = 5,moveCost = 10,pushCost = 5,targetSeconds = 3149) == 40
    assert candidate(startAt = 1,moveCost = 9,pushCost = 2,targetSeconds = 999) == 26
    assert candidate(startAt = 8,moveCost = 15,pushCost = 8,targetSeconds = 4321) == 92
    assert candidate(startAt = 1,moveCost = 1,pushCost = 1,targetSeconds = 359) == 5
    assert candidate(startAt = 5,moveCost = 1,pushCost = 10,targetSeconds = 3959) == 43
    assert candidate(startAt = 9,moveCost = 2,pushCost = 4,targetSeconds = 5999) == 20
    assert candidate(startAt = 2,moveCost = 6,pushCost = 2,targetSeconds = 5678) == 32
    assert candidate(startAt = 8,moveCost = 3,pushCost = 4,targetSeconds = 6039) == 19
    assert candidate(startAt = 3,moveCost = 5,pushCost = 3,targetSeconds = 5400) == 22
    assert candidate(startAt = 6,moveCost = 3,pushCost = 4,targetSeconds = 999) == 25
    assert candidate(startAt = 3,moveCost = 1,pushCost = 5,targetSeconds = 90) == 12
    assert candidate(startAt = 0,moveCost = 10,pushCost = 1,targetSeconds = 5999) == 34
    assert candidate(startAt = 9,moveCost = 1,pushCost = 2,targetSeconds = 123) == 9
    assert candidate(startAt = 3,moveCost = 4,pushCost = 2,targetSeconds = 300) == 14
    assert candidate(startAt = 5,moveCost = 7,pushCost = 3,targetSeconds = 1234) == 33
    assert candidate(startAt = 8,moveCost = 5,pushCost = 3,targetSeconds = 60) == 16
    assert candidate(startAt = 8,moveCost = 3,pushCost = 2,targetSeconds = 99) == 7
    assert candidate(startAt = 3,moveCost = 2,pushCost = 3,targetSeconds = 60) == 10
    assert candidate(startAt = 9,moveCost = 5,pushCost = 10,targetSeconds = 5999) == 50
    assert candidate(startAt = 8,moveCost = 3,pushCost = 5,targetSeconds = 59) == 16
    assert candidate(startAt = 2,moveCost = 4,pushCost = 5,targetSeconds = 720) == 32
    assert candidate(startAt = 4,moveCost = 4,pushCost = 4,targetSeconds = 5432) == 28
    assert candidate(startAt = 7,moveCost = 7,pushCost = 8,targetSeconds = 1) == 15
    assert candidate(startAt = 0,moveCost = 5,pushCost = 10,targetSeconds = 360) == 40
    assert candidate(startAt = 0,moveCost = 7,pushCost = 1,targetSeconds = 5999) == 25
    assert candidate(startAt = 6,moveCost = 4,pushCost = 6,targetSeconds = 200) == 30
    assert candidate(startAt = 9,moveCost = 10,pushCost = 1,targetSeconds = 5432) == 34
    assert candidate(startAt = 2,moveCost = 2,pushCost = 3,targetSeconds = 3600) == 16
    assert candidate(startAt = 5,moveCost = 10,pushCost = 5,targetSeconds = 3999) == 50
    assert candidate(startAt = 2,moveCost = 10,pushCost = 5,targetSeconds = 3660) == 50
    assert candidate(startAt = 0,moveCost = 3,pushCost = 7,targetSeconds = 90) == 20
    assert candidate(startAt = 3,moveCost = 1,pushCost = 1,targetSeconds = 599) == 6
    assert candidate(startAt = 7,moveCost = 6,pushCost = 4,targetSeconds = 4567) == 34
    assert candidate(startAt = 3,moveCost = 20,pushCost = 5,targetSeconds = 300) == 55
    assert candidate(startAt = 4,moveCost = 6,pushCost = 2,targetSeconds = 900) == 26
    assert candidate(startAt = 1,moveCost = 5,pushCost = 1,targetSeconds = 540) == 13
    assert candidate(startAt = 6,moveCost = 15,pushCost = 5,targetSeconds = 999) == 65
    assert candidate(startAt = 5,moveCost = 1,pushCost = 2,targetSeconds = 480) == 8
    assert candidate(startAt = 0,moveCost = 3,pushCost = 2,targetSeconds = 120) == 12
    assert candidate(startAt = 2,moveCost = 1,pushCost = 1,targetSeconds = 99) == 3
    assert candidate(startAt = 1,moveCost = 6,pushCost = 1,targetSeconds = 59) == 14
    assert candidate(startAt = 7,moveCost = 2,pushCost = 6,targetSeconds = 1000) == 32
    assert candidate(startAt = 4,moveCost = 4,pushCost = 3,targetSeconds = 1500) == 24
    assert candidate(startAt = 6,moveCost = 2,pushCost = 9,targetSeconds = 9999) == inf
    assert candidate(startAt = 0,moveCost = 1,pushCost = 1,targetSeconds = 1234) == 7
    assert candidate(startAt = 2,moveCost = 20,pushCost = 10,targetSeconds = 1020) == 100
    assert candidate(startAt = 4,moveCost = 8,pushCost = 2,targetSeconds = 100) == 30
    assert candidate(startAt = 7,moveCost = 5,pushCost = 2,targetSeconds = 1234) == 23


