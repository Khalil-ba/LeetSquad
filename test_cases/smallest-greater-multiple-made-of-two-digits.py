def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(k = 5,digit1 = 5,digit2 = 5) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5,digit1 = 5,digit2 = 5) == 55: {e}')
    
    total += 1
    try:
        result = candidate(k = 2,digit1 = 0,digit2 = 2) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2,digit1 = 0,digit2 = 2) == 20: {e}')
    
    total += 1
    try:
        result = candidate(k = 2,digit1 = 0,digit2 = 0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2,digit1 = 0,digit2 = 0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 10,digit1 = 1,digit2 = 0) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10,digit1 = 1,digit2 = 0) == 100: {e}')
    
    total += 1
    try:
        result = candidate(k = 999,digit1 = 9,digit2 = 9) == 999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 999,digit1 = 9,digit2 = 9) == 999999: {e}')
    
    total += 1
    try:
        result = candidate(k = 3,digit1 = 4,digit2 = 2) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3,digit1 = 4,digit2 = 2) == 24: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000,digit1 = 1,digit2 = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000,digit1 = 1,digit2 = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 100,digit1 = 3,digit2 = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100,digit1 = 3,digit2 = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 1,digit1 = 1,digit2 = 1) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1,digit1 = 1,digit2 = 1) == 11: {e}')
    
    total += 1
    try:
        result = candidate(k = 7,digit1 = 7,digit2 = 1) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7,digit1 = 7,digit2 = 1) == 77: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000,digit1 = 0,digit2 = 0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000,digit1 = 0,digit2 = 0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 7,digit1 = 7,digit2 = 7) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7,digit1 = 7,digit2 = 7) == 77: {e}')
    
    total += 1
    try:
        result = candidate(k = 500,digit1 = 5,digit2 = 0) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500,digit1 = 5,digit2 = 0) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(k = 100,digit1 = 3,digit2 = 9) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100,digit1 = 3,digit2 = 9) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 99,digit1 = 9,digit2 = 1) == 9999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 99,digit1 = 9,digit2 = 1) == 9999: {e}')
    
    total += 1
    try:
        result = candidate(k = 200,digit1 = 2,digit2 = 0) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 200,digit1 = 2,digit2 = 0) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(k = 31,digit1 = 3,digit2 = 1) == 1333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 31,digit1 = 3,digit2 = 1) == 1333: {e}')
    
    total += 1
    try:
        result = candidate(k = 67,digit1 = 6,digit2 = 7) == 6767
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 67,digit1 = 6,digit2 = 7) == 6767: {e}')
    
    total += 1
    try:
        result = candidate(k = 12,digit1 = 1,digit2 = 2) == 1212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 12,digit1 = 1,digit2 = 2) == 1212: {e}')
    
    total += 1
    try:
        result = candidate(k = 404,digit1 = 4,digit2 = 0) == 4040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 404,digit1 = 4,digit2 = 0) == 4040: {e}')
    
    total += 1
    try:
        result = candidate(k = 888,digit1 = 8,digit2 = 8) == 888888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 888,digit1 = 8,digit2 = 8) == 888888: {e}')
    
    total += 1
    try:
        result = candidate(k = 777,digit1 = 7,digit2 = 7) == 777777
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 777,digit1 = 7,digit2 = 7) == 777777: {e}')
    
    total += 1
    try:
        result = candidate(k = 13,digit1 = 5,digit2 = 7) == 5577
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 13,digit1 = 5,digit2 = 7) == 5577: {e}')
    
    total += 1
    try:
        result = candidate(k = 8,digit1 = 8,digit2 = 8) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8,digit1 = 8,digit2 = 8) == 88: {e}')
    
    total += 1
    try:
        result = candidate(k = 234,digit1 = 2,digit2 = 4) == 242424
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 234,digit1 = 2,digit2 = 4) == 242424: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000,digit1 = 8,digit2 = 8) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000,digit1 = 8,digit2 = 8) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 500,digit1 = 5,digit2 = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500,digit1 = 5,digit2 = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 7,digit1 = 3,digit2 = 5) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7,digit1 = 3,digit2 = 5) == 35: {e}')
    
    total += 1
    try:
        result = candidate(k = 101,digit1 = 1,digit2 = 1) == 1111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 101,digit1 = 1,digit2 = 1) == 1111: {e}')
    
    total += 1
    try:
        result = candidate(k = 88,digit1 = 8,digit2 = 9) == 8888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 88,digit1 = 8,digit2 = 9) == 8888: {e}')
    
    total += 1
    try:
        result = candidate(k = 333,digit1 = 3,digit2 = 3) == 333333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 333,digit1 = 3,digit2 = 3) == 333333: {e}')
    
    total += 1
    try:
        result = candidate(k = 5000,digit1 = 0,digit2 = 5) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5000,digit1 = 0,digit2 = 5) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(k = 50,digit1 = 5,digit2 = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50,digit1 = 5,digit2 = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 123,digit1 = 1,digit2 = 3) == 33333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123,digit1 = 1,digit2 = 3) == 33333: {e}')
    
    total += 1
    try:
        result = candidate(k = 47,digit1 = 1,digit2 = 9) == 119991
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 47,digit1 = 1,digit2 = 9) == 119991: {e}')
    
    total += 1
    try:
        result = candidate(k = 333,digit1 = 3,digit2 = 0) == 3330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 333,digit1 = 3,digit2 = 0) == 3330: {e}')
    
    total += 1
    try:
        result = candidate(k = 450,digit1 = 5,digit2 = 0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 450,digit1 = 5,digit2 = 0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 512,digit1 = 5,digit2 = 2) == 55255552
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 512,digit1 = 5,digit2 = 2) == 55255552: {e}')
    
    total += 1
    try:
        result = candidate(k = 56,digit1 = 7,digit2 = 9) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 56,digit1 = 7,digit2 = 9) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 111,digit1 = 1,digit2 = 0) == 1110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 111,digit1 = 1,digit2 = 0) == 1110: {e}')
    
    total += 1
    try:
        result = candidate(k = 99,digit1 = 9,digit2 = 9) == 9999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 99,digit1 = 9,digit2 = 9) == 9999: {e}')
    
    total += 1
    try:
        result = candidate(k = 998,digit1 = 9,digit2 = 8) == 998998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 998,digit1 = 9,digit2 = 8) == 998998: {e}')
    
    total += 1
    try:
        result = candidate(k = 9,digit1 = 9,digit2 = 0) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9,digit1 = 9,digit2 = 0) == 90: {e}')
    
    total += 1
    try:
        result = candidate(k = 31,digit1 = 1,digit2 = 3) == 1333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 31,digit1 = 1,digit2 = 3) == 1333: {e}')
    
    total += 1
    try:
        result = candidate(k = 700,digit1 = 7,digit2 = 0) == 7000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 700,digit1 = 7,digit2 = 0) == 7000: {e}')
    
    total += 1
    try:
        result = candidate(k = 1001,digit1 = 1,digit2 = 0) == 10010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1001,digit1 = 1,digit2 = 0) == 10010: {e}')
    
    total += 1
    try:
        result = candidate(k = 123,digit1 = 3,digit2 = 7) == 33333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123,digit1 = 3,digit2 = 7) == 33333: {e}')
    
    total += 1
    try:
        result = candidate(k = 250,digit1 = 2,digit2 = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 250,digit1 = 2,digit2 = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 999,digit1 = 9,digit2 = 8) == 999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 999,digit1 = 9,digit2 = 8) == 999999: {e}')
    
    total += 1
    try:
        result = candidate(k = 256,digit1 = 2,digit2 = 5) == 55552
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 256,digit1 = 2,digit2 = 5) == 55552: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000,digit1 = 0,digit2 = 1) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000,digit1 = 0,digit2 = 1) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(k = 123,digit1 = 1,digit2 = 2) == 21112212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123,digit1 = 1,digit2 = 2) == 21112212: {e}')
    
    total += 1
    try:
        result = candidate(k = 99,digit1 = 1,digit2 = 2) == 1122222222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 99,digit1 = 1,digit2 = 2) == 1122222222: {e}')
    
    total += 1
    try:
        result = candidate(k = 7,digit1 = 1,digit2 = 7) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7,digit1 = 1,digit2 = 7) == 77: {e}')
    
    total += 1
    try:
        result = candidate(k = 37,digit1 = 3,digit2 = 7) == 333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 37,digit1 = 3,digit2 = 7) == 333: {e}')
    
    total += 1
    try:
        result = candidate(k = 45,digit1 = 5,digit2 = 9) == 555555555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 45,digit1 = 5,digit2 = 9) == 555555555: {e}')
    
    total += 1
    try:
        result = candidate(k = 50,digit1 = 5,digit2 = 0) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50,digit1 = 5,digit2 = 0) == 500: {e}')
    
    total += 1
    try:
        result = candidate(k = 23,digit1 = 7,digit2 = 1) == 1771
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 23,digit1 = 7,digit2 = 1) == 1771: {e}')
    
    total += 1
    try:
        result = candidate(k = 45,digit1 = 6,digit2 = 9) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 45,digit1 = 6,digit2 = 9) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 27,digit1 = 7,digit2 = 9) == 999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 27,digit1 = 7,digit2 = 9) == 999: {e}')
    
    total += 1
    try:
        result = candidate(k = 13,digit1 = 1,digit2 = 9) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 13,digit1 = 1,digit2 = 9) == 91: {e}')
    
    total += 1
    try:
        result = candidate(k = 300,digit1 = 0,digit2 = 1) == 11100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 300,digit1 = 0,digit2 = 1) == 11100: {e}')
    
    total += 1
    try:
        result = candidate(k = 210,digit1 = 2,digit2 = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 210,digit1 = 2,digit2 = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 997,digit1 = 8,digit2 = 9) == 889988999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 997,digit1 = 8,digit2 = 9) == 889988999: {e}')
    
    total += 1
    try:
        result = candidate(k = 45,digit1 = 5,digit2 = 0) == 555555555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 45,digit1 = 5,digit2 = 0) == 555555555: {e}')
    
    total += 1
    try:
        result = candidate(k = 99,digit1 = 9,digit2 = 0) == 990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 99,digit1 = 9,digit2 = 0) == 990: {e}')
    
    total += 1
    try:
        result = candidate(k = 42,digit1 = 7,digit2 = 8) == 8778
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 42,digit1 = 7,digit2 = 8) == 8778: {e}')
    
    total += 1
    try:
        result = candidate(k = 89,digit1 = 8,digit2 = 9) == 8989
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 89,digit1 = 8,digit2 = 9) == 8989: {e}')
    
    total += 1
    try:
        result = candidate(k = 300,digit1 = 0,digit2 = 3) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 300,digit1 = 0,digit2 = 3) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(k = 500,digit1 = 4,digit2 = 8) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500,digit1 = 4,digit2 = 8) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 123,digit1 = 4,digit2 = 3) == 3444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123,digit1 = 4,digit2 = 3) == 3444: {e}')
    
    total += 1
    try:
        result = candidate(k = 600,digit1 = 6,digit2 = 9) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 600,digit1 = 6,digit2 = 9) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 1,digit1 = 9,digit2 = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1,digit1 = 9,digit2 = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(k = 666,digit1 = 6,digit2 = 6) == 666666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 666,digit1 = 6,digit2 = 6) == 666666: {e}')
    
    total += 1
    try:
        result = candidate(k = 999999999,digit1 = 9,digit2 = 9) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 999999999,digit1 = 9,digit2 = 9) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 500,digit1 = 2,digit2 = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500,digit1 = 2,digit2 = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 98,digit1 = 9,digit2 = 8) == 9898
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 98,digit1 = 9,digit2 = 8) == 9898: {e}')
    
    total += 1
    try:
        result = candidate(k = 300,digit1 = 3,digit2 = 0) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 300,digit1 = 3,digit2 = 0) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(k = 500,digit1 = 0,digit2 = 5) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500,digit1 = 0,digit2 = 5) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(k = 25,digit1 = 5,digit2 = 0) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 25,digit1 = 5,digit2 = 0) == 50: {e}')
    
    total += 1
    try:
        result = candidate(k = 750,digit1 = 5,digit2 = 7) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 750,digit1 = 5,digit2 = 7) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 15,digit1 = 5,digit2 = 9) == 555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 15,digit1 = 5,digit2 = 9) == 555: {e}')
    
    total += 1
    try:
        result = candidate(k = 999,digit1 = 9,digit2 = 0) == 9990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 999,digit1 = 9,digit2 = 0) == 9990: {e}')
    
    total += 1
    try:
        result = candidate(k = 25,digit1 = 2,digit2 = 5) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 25,digit1 = 2,digit2 = 5) == 225: {e}')
    
    total += 1
    try:
        result = candidate(k = 17,digit1 = 1,digit2 = 7) == 1717
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 17,digit1 = 1,digit2 = 7) == 1717: {e}')
    
    total += 1
    try:
        result = candidate(k = 1,digit1 = 0,digit2 = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1,digit1 = 0,digit2 = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(k = 137,digit1 = 1,digit2 = 3) == 3111133
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 137,digit1 = 1,digit2 = 3) == 3111133: {e}')
    
    total += 1
    try:
        result = candidate(k = 11,digit1 = 1,digit2 = 1) == 1111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 11,digit1 = 1,digit2 = 1) == 1111: {e}')
    
    total += 1
    try:
        result = candidate(k = 123,digit1 = 3,digit2 = 1) == 33333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123,digit1 = 3,digit2 = 1) == 33333: {e}')
    
    total += 1
    try:
        result = candidate(k = 21,digit1 = 7,digit2 = 1) == 777
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 21,digit1 = 7,digit2 = 1) == 777: {e}')
    
    total += 1
    try:
        result = candidate(k = 1024,digit1 = 1,digit2 = 2) == 12122112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1024,digit1 = 1,digit2 = 2) == 12122112: {e}')
    
    total += 1
    try:
        result = candidate(k = 89,digit1 = 5,digit2 = 7) == 75775757
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 89,digit1 = 5,digit2 = 7) == 75775757: {e}')
    
    total += 1
    try:
        result = candidate(k = 999,digit1 = 1,digit2 = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 999,digit1 = 1,digit2 = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 123,digit1 = 3,digit2 = 2) == 33333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123,digit1 = 3,digit2 = 2) == 33333: {e}')
    
    total += 1
    try:
        result = candidate(k = 111,digit1 = 1,digit2 = 1) == 111111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 111,digit1 = 1,digit2 = 1) == 111111: {e}')
    
    total += 1
    try:
        result = candidate(k = 256,digit1 = 5,digit2 = 6) == 6656
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 256,digit1 = 5,digit2 = 6) == 6656: {e}')
    
    total += 1
    try:
        result = candidate(k = 123,digit1 = 3,digit2 = 6) == 33333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123,digit1 = 3,digit2 = 6) == 33333: {e}')
    
    total += 1
    try:
        result = candidate(k = 666,digit1 = 6,digit2 = 0) == 6660
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 666,digit1 = 6,digit2 = 0) == 6660: {e}')
    
    total += 1
    try:
        result = candidate(k = 999,digit1 = 1,digit2 = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 999,digit1 = 1,digit2 = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 500,digit1 = 3,digit2 = 7) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500,digit1 = 3,digit2 = 7) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 750,digit1 = 7,digit2 = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 750,digit1 = 7,digit2 = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 400,digit1 = 4,digit2 = 0) == 4000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 400,digit1 = 4,digit2 = 0) == 4000: {e}')
    
    total += 1
    try:
        result = candidate(k = 55,digit1 = 0,digit2 = 5) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 55,digit1 = 0,digit2 = 5) == 550: {e}')
    
    total += 1
    try:
        result = candidate(k = 123,digit1 = 2,digit2 = 4) == 42224424
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123,digit1 = 2,digit2 = 4) == 42224424: {e}')
    
    total += 1
    try:
        result = candidate(k = 100,digit1 = 0,digit2 = 0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100,digit1 = 0,digit2 = 0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 43,digit1 = 4,digit2 = 3) == 344
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 43,digit1 = 4,digit2 = 3) == 344: {e}')
    
    total += 1
    try:
        result = candidate(k = 7,digit1 = 5,digit2 = 7) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7,digit1 = 5,digit2 = 7) == 77: {e}')
    
    total += 1
    try:
        result = candidate(k = 45,digit1 = 9,digit2 = 0) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 45,digit1 = 9,digit2 = 0) == 90: {e}')
    
    total += 1
    try:
        result = candidate(k = 12,digit1 = 3,digit2 = 6) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 12,digit1 = 3,digit2 = 6) == 36: {e}')
    
    total += 1
    try:
        result = candidate(k = 150,digit1 = 5,digit2 = 0) == 5550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 150,digit1 = 5,digit2 = 0) == 5550: {e}')
    
    total += 1
    try:
        result = candidate(k = 888,digit1 = 8,digit2 = 0) == 8880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 888,digit1 = 8,digit2 = 0) == 8880: {e}')
    
    total += 1
    try:
        result = candidate(k = 200,digit1 = 5,digit2 = 6) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 200,digit1 = 5,digit2 = 6) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 7,digit1 = 5,digit2 = 9) == 595
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7,digit1 = 5,digit2 = 9) == 595: {e}')
    
    total += 1
    try:
        result = candidate(k = 64,digit1 = 6,digit2 = 4) == 6464
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 64,digit1 = 6,digit2 = 4) == 6464: {e}')
    
    total += 1
    try:
        result = candidate(k = 5,digit1 = 5,digit2 = 7) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5,digit1 = 5,digit2 = 7) == 55: {e}')
    
    total += 1
    try:
        result = candidate(k = 314,digit1 = 1,digit2 = 4) == 14444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 314,digit1 = 1,digit2 = 4) == 14444: {e}')
    
    total += 1
    try:
        result = candidate(k = 33,digit1 = 3,digit2 = 3) == 3333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 33,digit1 = 3,digit2 = 3) == 3333: {e}')
    
    total += 1
    try:
        result = candidate(k = 15,digit1 = 5,digit2 = 3) == 555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 15,digit1 = 5,digit2 = 3) == 555: {e}')
    
    total += 1
    try:
        result = candidate(k = 34,digit1 = 4,digit2 = 3) == 3434
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 34,digit1 = 4,digit2 = 3) == 3434: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(k = 5,digit1 = 5,digit2 = 5) == 55
    assert candidate(k = 2,digit1 = 0,digit2 = 2) == 20
    assert candidate(k = 2,digit1 = 0,digit2 = 0) == -1
    assert candidate(k = 10,digit1 = 1,digit2 = 0) == 100
    assert candidate(k = 999,digit1 = 9,digit2 = 9) == 999999
    assert candidate(k = 3,digit1 = 4,digit2 = 2) == 24
    assert candidate(k = 1000,digit1 = 1,digit2 = 2) == -1
    assert candidate(k = 100,digit1 = 3,digit2 = 3) == -1
    assert candidate(k = 1,digit1 = 1,digit2 = 1) == 11
    assert candidate(k = 7,digit1 = 7,digit2 = 1) == 77
    assert candidate(k = 1000,digit1 = 0,digit2 = 0) == -1
    assert candidate(k = 7,digit1 = 7,digit2 = 7) == 77
    assert candidate(k = 500,digit1 = 5,digit2 = 0) == 5000
    assert candidate(k = 100,digit1 = 3,digit2 = 9) == -1
    assert candidate(k = 99,digit1 = 9,digit2 = 1) == 9999
    assert candidate(k = 200,digit1 = 2,digit2 = 0) == 2000
    assert candidate(k = 31,digit1 = 3,digit2 = 1) == 1333
    assert candidate(k = 67,digit1 = 6,digit2 = 7) == 6767
    assert candidate(k = 12,digit1 = 1,digit2 = 2) == 1212
    assert candidate(k = 404,digit1 = 4,digit2 = 0) == 4040
    assert candidate(k = 888,digit1 = 8,digit2 = 8) == 888888
    assert candidate(k = 777,digit1 = 7,digit2 = 7) == 777777
    assert candidate(k = 13,digit1 = 5,digit2 = 7) == 5577
    assert candidate(k = 8,digit1 = 8,digit2 = 8) == 88
    assert candidate(k = 234,digit1 = 2,digit2 = 4) == 242424
    assert candidate(k = 1000,digit1 = 8,digit2 = 8) == -1
    assert candidate(k = 500,digit1 = 5,digit2 = 5) == -1
    assert candidate(k = 7,digit1 = 3,digit2 = 5) == 35
    assert candidate(k = 101,digit1 = 1,digit2 = 1) == 1111
    assert candidate(k = 88,digit1 = 8,digit2 = 9) == 8888
    assert candidate(k = 333,digit1 = 3,digit2 = 3) == 333333
    assert candidate(k = 5000,digit1 = 0,digit2 = 5) == 50000
    assert candidate(k = 50,digit1 = 5,digit2 = 5) == -1
    assert candidate(k = 123,digit1 = 1,digit2 = 3) == 33333
    assert candidate(k = 47,digit1 = 1,digit2 = 9) == 119991
    assert candidate(k = 333,digit1 = 3,digit2 = 0) == 3330
    assert candidate(k = 450,digit1 = 5,digit2 = 0) == -1
    assert candidate(k = 512,digit1 = 5,digit2 = 2) == 55255552
    assert candidate(k = 56,digit1 = 7,digit2 = 9) == -1
    assert candidate(k = 111,digit1 = 1,digit2 = 0) == 1110
    assert candidate(k = 99,digit1 = 9,digit2 = 9) == 9999
    assert candidate(k = 998,digit1 = 9,digit2 = 8) == 998998
    assert candidate(k = 9,digit1 = 9,digit2 = 0) == 90
    assert candidate(k = 31,digit1 = 1,digit2 = 3) == 1333
    assert candidate(k = 700,digit1 = 7,digit2 = 0) == 7000
    assert candidate(k = 1001,digit1 = 1,digit2 = 0) == 10010
    assert candidate(k = 123,digit1 = 3,digit2 = 7) == 33333
    assert candidate(k = 250,digit1 = 2,digit2 = 5) == -1
    assert candidate(k = 999,digit1 = 9,digit2 = 8) == 999999
    assert candidate(k = 256,digit1 = 2,digit2 = 5) == 55552
    assert candidate(k = 1000,digit1 = 0,digit2 = 1) == 10000
    assert candidate(k = 123,digit1 = 1,digit2 = 2) == 21112212
    assert candidate(k = 99,digit1 = 1,digit2 = 2) == 1122222222
    assert candidate(k = 7,digit1 = 1,digit2 = 7) == 77
    assert candidate(k = 37,digit1 = 3,digit2 = 7) == 333
    assert candidate(k = 45,digit1 = 5,digit2 = 9) == 555555555
    assert candidate(k = 50,digit1 = 5,digit2 = 0) == 500
    assert candidate(k = 23,digit1 = 7,digit2 = 1) == 1771
    assert candidate(k = 45,digit1 = 6,digit2 = 9) == -1
    assert candidate(k = 27,digit1 = 7,digit2 = 9) == 999
    assert candidate(k = 13,digit1 = 1,digit2 = 9) == 91
    assert candidate(k = 300,digit1 = 0,digit2 = 1) == 11100
    assert candidate(k = 210,digit1 = 2,digit2 = 1) == -1
    assert candidate(k = 997,digit1 = 8,digit2 = 9) == 889988999
    assert candidate(k = 45,digit1 = 5,digit2 = 0) == 555555555
    assert candidate(k = 99,digit1 = 9,digit2 = 0) == 990
    assert candidate(k = 42,digit1 = 7,digit2 = 8) == 8778
    assert candidate(k = 89,digit1 = 8,digit2 = 9) == 8989
    assert candidate(k = 300,digit1 = 0,digit2 = 3) == 3000
    assert candidate(k = 500,digit1 = 4,digit2 = 8) == -1
    assert candidate(k = 123,digit1 = 4,digit2 = 3) == 3444
    assert candidate(k = 600,digit1 = 6,digit2 = 9) == -1
    assert candidate(k = 1,digit1 = 9,digit2 = 9) == 9
    assert candidate(k = 666,digit1 = 6,digit2 = 6) == 666666
    assert candidate(k = 999999999,digit1 = 9,digit2 = 9) == -1
    assert candidate(k = 500,digit1 = 2,digit2 = 3) == -1
    assert candidate(k = 98,digit1 = 9,digit2 = 8) == 9898
    assert candidate(k = 300,digit1 = 3,digit2 = 0) == 3000
    assert candidate(k = 500,digit1 = 0,digit2 = 5) == 5000
    assert candidate(k = 25,digit1 = 5,digit2 = 0) == 50
    assert candidate(k = 750,digit1 = 5,digit2 = 7) == -1
    assert candidate(k = 15,digit1 = 5,digit2 = 9) == 555
    assert candidate(k = 999,digit1 = 9,digit2 = 0) == 9990
    assert candidate(k = 25,digit1 = 2,digit2 = 5) == 225
    assert candidate(k = 17,digit1 = 1,digit2 = 7) == 1717
    assert candidate(k = 1,digit1 = 0,digit2 = 1) == 10
    assert candidate(k = 137,digit1 = 1,digit2 = 3) == 3111133
    assert candidate(k = 11,digit1 = 1,digit2 = 1) == 1111
    assert candidate(k = 123,digit1 = 3,digit2 = 1) == 33333
    assert candidate(k = 21,digit1 = 7,digit2 = 1) == 777
    assert candidate(k = 1024,digit1 = 1,digit2 = 2) == 12122112
    assert candidate(k = 89,digit1 = 5,digit2 = 7) == 75775757
    assert candidate(k = 999,digit1 = 1,digit2 = 2) == -1
    assert candidate(k = 123,digit1 = 3,digit2 = 2) == 33333
    assert candidate(k = 111,digit1 = 1,digit2 = 1) == 111111
    assert candidate(k = 256,digit1 = 5,digit2 = 6) == 6656
    assert candidate(k = 123,digit1 = 3,digit2 = 6) == 33333
    assert candidate(k = 666,digit1 = 6,digit2 = 0) == 6660
    assert candidate(k = 999,digit1 = 1,digit2 = 1) == -1
    assert candidate(k = 500,digit1 = 3,digit2 = 7) == -1
    assert candidate(k = 750,digit1 = 7,digit2 = 5) == -1
    assert candidate(k = 400,digit1 = 4,digit2 = 0) == 4000
    assert candidate(k = 55,digit1 = 0,digit2 = 5) == 550
    assert candidate(k = 123,digit1 = 2,digit2 = 4) == 42224424
    assert candidate(k = 100,digit1 = 0,digit2 = 0) == -1
    assert candidate(k = 43,digit1 = 4,digit2 = 3) == 344
    assert candidate(k = 7,digit1 = 5,digit2 = 7) == 77
    assert candidate(k = 45,digit1 = 9,digit2 = 0) == 90
    assert candidate(k = 12,digit1 = 3,digit2 = 6) == 36
    assert candidate(k = 150,digit1 = 5,digit2 = 0) == 5550
    assert candidate(k = 888,digit1 = 8,digit2 = 0) == 8880
    assert candidate(k = 200,digit1 = 5,digit2 = 6) == -1
    assert candidate(k = 7,digit1 = 5,digit2 = 9) == 595
    assert candidate(k = 64,digit1 = 6,digit2 = 4) == 6464
    assert candidate(k = 5,digit1 = 5,digit2 = 7) == 55
    assert candidate(k = 314,digit1 = 1,digit2 = 4) == 14444
    assert candidate(k = 33,digit1 = 3,digit2 = 3) == 3333
    assert candidate(k = 15,digit1 = 5,digit2 = 3) == 555
    assert candidate(k = 34,digit1 = 4,digit2 = 3) == 3434


