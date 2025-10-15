def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(x = 1,y = 10000) == 9999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1,y = 10000) == 9999: {e}')
    
    total += 1
    try:
        result = candidate(x = 11,y = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 11,y = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(x = 10000,y = 1) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10000,y = 1) == 8: {e}')
    
    total += 1
    try:
        result = candidate(x = 111,y = 11) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 111,y = 11) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 77,y = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 77,y = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 500,y = 20) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 500,y = 20) == 2: {e}')
    
    total += 1
    try:
        result = candidate(x = 25,y = 30) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,y = 30) == 5: {e}')
    
    total += 1
    try:
        result = candidate(x = 11,y = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 11,y = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 55,y = 11) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 55,y = 11) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 2,y = 20) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2,y = 20) == 18: {e}')
    
    total += 1
    try:
        result = candidate(x = 1234,y = 4321) == 3087
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1234,y = 4321) == 3087: {e}')
    
    total += 1
    try:
        result = candidate(x = 100,y = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 100,y = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = 26,y = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 26,y = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 54,y = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 54,y = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = 99,y = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 99,y = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 9999,y = 9999) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9999,y = 9999) == 0: {e}')
    
    total += 1
    try:
        result = candidate(x = 55,y = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 55,y = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(x = 55,y = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 55,y = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 100,y = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 100,y = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 5,y = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,y = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 15,y = 6) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 15,y = 6) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = 1,y = 100) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1,y = 100) == 99: {e}')
    
    total += 1
    try:
        result = candidate(x = 1111,y = 5555) == 4444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1111,y = 5555) == 4444: {e}')
    
    total += 1
    try:
        result = candidate(x = 6666,y = 3333) == 2002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 6666,y = 3333) == 2002: {e}')
    
    total += 1
    try:
        result = candidate(x = 9876,y = 5432) == 3459
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9876,y = 5432) == 3459: {e}')
    
    total += 1
    try:
        result = candidate(x = 8888,y = 111) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8888,y = 111) == 45: {e}')
    
    total += 1
    try:
        result = candidate(x = 3000,y = 2500) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3000,y = 2500) == 500: {e}')
    
    total += 1
    try:
        result = candidate(x = 1111,y = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1111,y = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(x = 7777,y = 6666) == 1111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7777,y = 6666) == 1111: {e}')
    
    total += 1
    try:
        result = candidate(x = 100,y = 2500) == 2400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 100,y = 2500) == 2400: {e}')
    
    total += 1
    try:
        result = candidate(x = 5555,y = 22) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5555,y = 22) == 6: {e}')
    
    total += 1
    try:
        result = candidate(x = 1234,y = 8765) == 7531
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1234,y = 8765) == 7531: {e}')
    
    total += 1
    try:
        result = candidate(x = 7000,y = 3500) == 2101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7000,y = 3500) == 2101: {e}')
    
    total += 1
    try:
        result = candidate(x = 9876,y = 1234) == 339
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9876,y = 1234) == 339: {e}')
    
    total += 1
    try:
        result = candidate(x = 55,y = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 55,y = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(x = 3333,y = 6666) == 3333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3333,y = 6666) == 3333: {e}')
    
    total += 1
    try:
        result = candidate(x = 3333,y = 33) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3333,y = 33) == 12: {e}')
    
    total += 1
    try:
        result = candidate(x = 1010,y = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1010,y = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(x = 550,y = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 550,y = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(x = 100,y = 10000) == 9900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 100,y = 10000) == 9900: {e}')
    
    total += 1
    try:
        result = candidate(x = 6666,y = 66) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 6666,y = 66) == 14: {e}')
    
    total += 1
    try:
        result = candidate(x = 5000,y = 5005) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5000,y = 5005) == 5: {e}')
    
    total += 1
    try:
        result = candidate(x = 5000,y = 50) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5000,y = 50) == 13: {e}')
    
    total += 1
    try:
        result = candidate(x = 441,y = 121) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 441,y = 121) == 35: {e}')
    
    total += 1
    try:
        result = candidate(x = 5000,y = 2500) == 1501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5000,y = 2500) == 1501: {e}')
    
    total += 1
    try:
        result = candidate(x = 330,y = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 330,y = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(x = 9999,y = 10000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9999,y = 10000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 5000,y = 6000) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5000,y = 6000) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(x = 9999,y = 1000) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9999,y = 1000) == 92: {e}')
    
    total += 1
    try:
        result = candidate(x = 500,y = 1000) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 500,y = 1000) == 500: {e}')
    
    total += 1
    try:
        result = candidate(x = 2222,y = 2222) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2222,y = 2222) == 0: {e}')
    
    total += 1
    try:
        result = candidate(x = 9000,y = 9009) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9000,y = 9009) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 1000,y = 345) == 146
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1000,y = 345) == 146: {e}')
    
    total += 1
    try:
        result = candidate(x = 4444,y = 4445) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4444,y = 4445) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 220,y = 385) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 220,y = 385) == 165: {e}')
    
    total += 1
    try:
        result = candidate(x = 300,y = 105) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 300,y = 105) == 46: {e}')
    
    total += 1
    try:
        result = candidate(x = 9999,y = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9999,y = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 1234,y = 654) == 409
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1234,y = 654) == 409: {e}')
    
    total += 1
    try:
        result = candidate(x = 5000,y = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5000,y = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(x = 55,y = 77) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 55,y = 77) == 22: {e}')
    
    total += 1
    try:
        result = candidate(x = 4999,y = 5001) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4999,y = 5001) == 2: {e}')
    
    total += 1
    try:
        result = candidate(x = 1000,y = 10000) == 9000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1000,y = 10000) == 9000: {e}')
    
    total += 1
    try:
        result = candidate(x = 3000,y = 2990) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3000,y = 2990) == 10: {e}')
    
    total += 1
    try:
        result = candidate(x = 300,y = 150) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 300,y = 150) == 91: {e}')
    
    total += 1
    try:
        result = candidate(x = 220,y = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 220,y = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 4567,y = 890) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4567,y = 890) == 26: {e}')
    
    total += 1
    try:
        result = candidate(x = 1111,y = 1000) == 111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1111,y = 1000) == 111: {e}')
    
    total += 1
    try:
        result = candidate(x = 1000,y = 995) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1000,y = 995) == 5: {e}')
    
    total += 1
    try:
        result = candidate(x = 4444,y = 44) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4444,y = 44) == 12: {e}')
    
    total += 1
    try:
        result = candidate(x = 123,y = 321) == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 123,y = 321) == 198: {e}')
    
    total += 1
    try:
        result = candidate(x = 1000,y = 999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1000,y = 999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 6000,y = 1000) == 201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 6000,y = 1000) == 201: {e}')
    
    total += 1
    try:
        result = candidate(x = 880,y = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 880,y = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 880,y = 55) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 880,y = 55) == 23: {e}')
    
    total += 1
    try:
        result = candidate(x = 1100,y = 50) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1100,y = 50) == 8: {e}')
    
    total += 1
    try:
        result = candidate(x = 1331,y = 110) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1331,y = 110) == 12: {e}')
    
    total += 1
    try:
        result = candidate(x = 1000,y = 990) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1000,y = 990) == 10: {e}')
    
    total += 1
    try:
        result = candidate(x = 7777,y = 2222) == 670
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7777,y = 2222) == 670: {e}')
    
    total += 1
    try:
        result = candidate(x = 1100,y = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1100,y = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = 4000,y = 2000) == 1201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4000,y = 2000) == 1201: {e}')
    
    total += 1
    try:
        result = candidate(x = 9876,y = 4321) == 2348
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9876,y = 4321) == 2348: {e}')
    
    total += 1
    try:
        result = candidate(x = 9876,y = 4567) == 2594
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9876,y = 4567) == 2594: {e}')
    
    total += 1
    try:
        result = candidate(x = 1234,y = 5678) == 4444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1234,y = 5678) == 4444: {e}')
    
    total += 1
    try:
        result = candidate(x = 495,y = 660) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 495,y = 660) == 165: {e}')
    
    total += 1
    try:
        result = candidate(x = 6110,y = 55) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 6110,y = 55) == 12: {e}')
    
    total += 1
    try:
        result = candidate(x = 1111,y = 222) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1111,y = 222) == 2: {e}')
    
    total += 1
    try:
        result = candidate(x = 45,y = 33) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 45,y = 33) == 12: {e}')
    
    total += 1
    try:
        result = candidate(x = 9876,y = 11) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9876,y = 11) == 11: {e}')
    
    total += 1
    try:
        result = candidate(x = 5500,y = 220) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5500,y = 220) == 2: {e}')
    
    total += 1
    try:
        result = candidate(x = 1024,y = 128) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1024,y = 128) == 37: {e}')
    
    total += 1
    try:
        result = candidate(x = 24,y = 29) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 24,y = 29) == 5: {e}')
    
    total += 1
    try:
        result = candidate(x = 8000,y = 8008) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8000,y = 8008) == 8: {e}')
    
    total += 1
    try:
        result = candidate(x = 88,y = 22) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 88,y = 22) == 7: {e}')
    
    total += 1
    try:
        result = candidate(x = 495,y = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 495,y = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 7000,y = 7000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7000,y = 7000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(x = 825,y = 17) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 825,y = 17) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = 5555,y = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5555,y = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(x = 1234,y = 88) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1234,y = 88) == 27: {e}')
    
    total += 1
    try:
        result = candidate(x = 1024,y = 512) == 309
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1024,y = 512) == 309: {e}')
    
    total += 1
    try:
        result = candidate(x = 9999,y = 8888) == 1111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9999,y = 8888) == 1111: {e}')
    
    total += 1
    try:
        result = candidate(x = 8000,y = 2000) == 401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8000,y = 2000) == 401: {e}')
    
    total += 1
    try:
        result = candidate(x = 5432,y = 6789) == 1357
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5432,y = 6789) == 1357: {e}')
    
    total += 1
    try:
        result = candidate(x = 111,y = 55) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 111,y = 55) == 35: {e}')
    
    total += 1
    try:
        result = candidate(x = 7500,y = 7400) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7500,y = 7400) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = 242,y = 11) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 242,y = 11) == 7: {e}')
    
    total += 1
    try:
        result = candidate(x = 121,y = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 121,y = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(x = 6105,y = 1221) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 6105,y = 1221) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 3333,y = 999) == 335
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3333,y = 999) == 335: {e}')
    
    total += 1
    try:
        result = candidate(x = 2020,y = 202) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2020,y = 202) == 23: {e}')
    
    total += 1
    try:
        result = candidate(x = 121,y = 110) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 121,y = 110) == 11: {e}')
    
    total += 1
    try:
        result = candidate(x = 4321,y = 9876) == 5555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4321,y = 9876) == 5555: {e}')
    
    total += 1
    try:
        result = candidate(x = 4444,y = 8888) == 4444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4444,y = 8888) == 4444: {e}')
    
    total += 1
    try:
        result = candidate(x = 2222,y = 222) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2222,y = 222) == 21: {e}')
    
    total += 1
    try:
        result = candidate(x = 1234,y = 890) == 344
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1234,y = 890) == 344: {e}')
    
    total += 1
    try:
        result = candidate(x = 7,y = 143) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7,y = 143) == 136: {e}')
    
    total += 1
    try:
        result = candidate(x = 7777,y = 77) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7777,y = 77) == 18: {e}')
    
    total += 1
    try:
        result = candidate(x = 5555,y = 1111) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5555,y = 1111) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 8888,y = 7777) == 1111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8888,y = 7777) == 1111: {e}')
    
    total += 1
    try:
        result = candidate(x = 9876,y = 123) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9876,y = 123) == 48: {e}')
    
    total += 1
    try:
        result = candidate(x = 2000,y = 10000) == 8000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2000,y = 10000) == 8000: {e}')
    
    total += 1
    try:
        result = candidate(x = 8000,y = 8010) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8000,y = 8010) == 10: {e}')
    
    total += 1
    try:
        result = candidate(x = 88,y = 13) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 88,y = 13) == 6: {e}')
    
    total += 1
    try:
        result = candidate(x = 7777,y = 1111) == 405
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7777,y = 1111) == 405: {e}')
    
    total += 1
    try:
        result = candidate(x = 3333,y = 4444) == 1111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3333,y = 4444) == 1111: {e}')
    
    total += 1
    try:
        result = candidate(x = 6000,y = 6005) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 6000,y = 6005) == 5: {e}')
    
    total += 1
    try:
        result = candidate(x = 9999,y = 9990) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9999,y = 9990) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 2222,y = 7777) == 5555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2222,y = 7777) == 5555: {e}')
    
    total += 1
    try:
        result = candidate(x = 77,y = 22) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 77,y = 22) == 10: {e}')
    
    total += 1
    try:
        result = candidate(x = 2000,y = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2000,y = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 1111,y = 9999) == 8888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1111,y = 9999) == 8888: {e}')
    
    total += 1
    try:
        result = candidate(x = 1234,y = 987) == 247
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1234,y = 987) == 247: {e}')
    
    total += 1
    try:
        result = candidate(x = 8888,y = 1111) == 304
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8888,y = 1111) == 304: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(x = 1,y = 10000) == 9999
    assert candidate(x = 11,y = 5) == 5
    assert candidate(x = 10000,y = 1) == 8
    assert candidate(x = 111,y = 11) == 3
    assert candidate(x = 77,y = 7) == 1
    assert candidate(x = 500,y = 20) == 2
    assert candidate(x = 25,y = 30) == 5
    assert candidate(x = 11,y = 1) == 1
    assert candidate(x = 55,y = 11) == 1
    assert candidate(x = 2,y = 20) == 18
    assert candidate(x = 1234,y = 4321) == 3087
    assert candidate(x = 100,y = 1) == 4
    assert candidate(x = 26,y = 1) == 3
    assert candidate(x = 54,y = 2) == 4
    assert candidate(x = 99,y = 9) == 1
    assert candidate(x = 9999,y = 9999) == 0
    assert candidate(x = 55,y = 10) == 2
    assert candidate(x = 10,y = 10) == 0
    assert candidate(x = 55,y = 5) == 1
    assert candidate(x = 100,y = 10) == 3
    assert candidate(x = 5,y = 1) == 1
    assert candidate(x = 15,y = 6) == 4
    assert candidate(x = 1,y = 100) == 99
    assert candidate(x = 1111,y = 5555) == 4444
    assert candidate(x = 6666,y = 3333) == 2002
    assert candidate(x = 9876,y = 5432) == 3459
    assert candidate(x = 8888,y = 111) == 45
    assert candidate(x = 3000,y = 2500) == 500
    assert candidate(x = 1111,y = 100) == 2
    assert candidate(x = 7777,y = 6666) == 1111
    assert candidate(x = 100,y = 2500) == 2400
    assert candidate(x = 5555,y = 22) == 6
    assert candidate(x = 1234,y = 8765) == 7531
    assert candidate(x = 7000,y = 3500) == 2101
    assert candidate(x = 9876,y = 1234) == 339
    assert candidate(x = 55,y = 15) == 5
    assert candidate(x = 3333,y = 6666) == 3333
    assert candidate(x = 3333,y = 33) == 12
    assert candidate(x = 1010,y = 10) == 7
    assert candidate(x = 550,y = 10) == 2
    assert candidate(x = 100,y = 10000) == 9900
    assert candidate(x = 6666,y = 66) == 14
    assert candidate(x = 5000,y = 5005) == 5
    assert candidate(x = 5000,y = 50) == 13
    assert candidate(x = 441,y = 121) == 35
    assert candidate(x = 5000,y = 2500) == 1501
    assert candidate(x = 330,y = 3) == 5
    assert candidate(x = 9999,y = 10000) == 1
    assert candidate(x = 5000,y = 6000) == 1000
    assert candidate(x = 9999,y = 1000) == 92
    assert candidate(x = 500,y = 1000) == 500
    assert candidate(x = 2222,y = 2222) == 0
    assert candidate(x = 9000,y = 9009) == 9
    assert candidate(x = 1000,y = 345) == 146
    assert candidate(x = 4444,y = 4445) == 1
    assert candidate(x = 220,y = 385) == 165
    assert candidate(x = 300,y = 105) == 46
    assert candidate(x = 9999,y = 1) == 9
    assert candidate(x = 1234,y = 654) == 409
    assert candidate(x = 5000,y = 5) == 7
    assert candidate(x = 55,y = 77) == 22
    assert candidate(x = 4999,y = 5001) == 2
    assert candidate(x = 1000,y = 10000) == 9000
    assert candidate(x = 3000,y = 2990) == 10
    assert candidate(x = 300,y = 150) == 91
    assert candidate(x = 220,y = 20) == 1
    assert candidate(x = 4567,y = 890) == 26
    assert candidate(x = 1111,y = 1000) == 111
    assert candidate(x = 1000,y = 995) == 5
    assert candidate(x = 4444,y = 44) == 12
    assert candidate(x = 123,y = 321) == 198
    assert candidate(x = 1000,y = 999) == 1
    assert candidate(x = 6000,y = 1000) == 201
    assert candidate(x = 880,y = 15) == 3
    assert candidate(x = 880,y = 55) == 23
    assert candidate(x = 1100,y = 50) == 8
    assert candidate(x = 1331,y = 110) == 12
    assert candidate(x = 1000,y = 990) == 10
    assert candidate(x = 7777,y = 2222) == 670
    assert candidate(x = 1100,y = 10) == 4
    assert candidate(x = 4000,y = 2000) == 1201
    assert candidate(x = 9876,y = 4321) == 2348
    assert candidate(x = 9876,y = 4567) == 2594
    assert candidate(x = 1234,y = 5678) == 4444
    assert candidate(x = 495,y = 660) == 165
    assert candidate(x = 6110,y = 55) == 12
    assert candidate(x = 1111,y = 222) == 2
    assert candidate(x = 45,y = 33) == 12
    assert candidate(x = 9876,y = 11) == 11
    assert candidate(x = 5500,y = 220) == 2
    assert candidate(x = 1024,y = 128) == 37
    assert candidate(x = 24,y = 29) == 5
    assert candidate(x = 8000,y = 8008) == 8
    assert candidate(x = 88,y = 22) == 7
    assert candidate(x = 495,y = 4) == 3
    assert candidate(x = 7000,y = 7000) == 0
    assert candidate(x = 825,y = 17) == 4
    assert candidate(x = 5555,y = 5) == 6
    assert candidate(x = 1234,y = 88) == 27
    assert candidate(x = 1024,y = 512) == 309
    assert candidate(x = 9999,y = 8888) == 1111
    assert candidate(x = 8000,y = 2000) == 401
    assert candidate(x = 5432,y = 6789) == 1357
    assert candidate(x = 111,y = 55) == 35
    assert candidate(x = 7500,y = 7400) == 100
    assert candidate(x = 242,y = 11) == 7
    assert candidate(x = 121,y = 1) == 2
    assert candidate(x = 6105,y = 1221) == 1
    assert candidate(x = 3333,y = 999) == 335
    assert candidate(x = 2020,y = 202) == 23
    assert candidate(x = 121,y = 110) == 11
    assert candidate(x = 4321,y = 9876) == 5555
    assert candidate(x = 4444,y = 8888) == 4444
    assert candidate(x = 2222,y = 222) == 21
    assert candidate(x = 1234,y = 890) == 344
    assert candidate(x = 7,y = 143) == 136
    assert candidate(x = 7777,y = 77) == 18
    assert candidate(x = 5555,y = 1111) == 1
    assert candidate(x = 8888,y = 7777) == 1111
    assert candidate(x = 9876,y = 123) == 48
    assert candidate(x = 2000,y = 10000) == 8000
    assert candidate(x = 8000,y = 8010) == 10
    assert candidate(x = 88,y = 13) == 6
    assert candidate(x = 7777,y = 1111) == 405
    assert candidate(x = 3333,y = 4444) == 1111
    assert candidate(x = 6000,y = 6005) == 5
    assert candidate(x = 9999,y = 9990) == 9
    assert candidate(x = 2222,y = 7777) == 5555
    assert candidate(x = 77,y = 22) == 10
    assert candidate(x = 2000,y = 10) == 9
    assert candidate(x = 1111,y = 9999) == 8888
    assert candidate(x = 1234,y = 987) == 247
    assert candidate(x = 8888,y = 1111) == 304


