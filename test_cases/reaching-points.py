def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(sx = 1,sy = 1,tx = 3,ty = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 1,sy = 1,tx = 3,ty = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 3,sy = 4,tx = 3,ty = 12) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 3,sy = 4,tx = 3,ty = 12) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 3,sy = 7,tx = 31,ty = 19) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 3,sy = 7,tx = 31,ty = 19) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 1,sy = 1,tx = 1000000000,ty = 1000000000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 1,sy = 1,tx = 1000000000,ty = 1000000000) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 5,sy = 5,tx = 5,ty = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 5,sy = 5,tx = 5,ty = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 1,sy = 1,tx = 1,ty = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 1,sy = 1,tx = 1,ty = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 1,sy = 1,tx = 2,ty = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 1,sy = 1,tx = 2,ty = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 2,sy = 3,tx = 8,ty = 11) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 2,sy = 3,tx = 8,ty = 11) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 5,sy = 1,tx = 1000000000,ty = 1000000000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 5,sy = 1,tx = 1000000000,ty = 1000000000) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 2,sy = 3,tx = 10,ty = 15) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 2,sy = 3,tx = 10,ty = 15) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 5,sy = 5,tx = 100,ty = 100) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 5,sy = 5,tx = 100,ty = 100) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 1,sy = 1,tx = 1000000000,ty = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 1,sy = 1,tx = 1000000000,ty = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 2,sy = 3,tx = 10,ty = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 2,sy = 3,tx = 10,ty = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 7,sy = 11,tx = 412,ty = 575) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 7,sy = 11,tx = 412,ty = 575) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 10,sy = 15,tx = 55,ty = 70) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 10,sy = 15,tx = 55,ty = 70) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 2,sy = 5,tx = 27,ty = 35) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 2,sy = 5,tx = 27,ty = 35) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 5,sy = 7,tx = 29,ty = 41) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 5,sy = 7,tx = 29,ty = 41) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 3,sy = 1,tx = 10,ty = 28) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 3,sy = 1,tx = 10,ty = 28) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 3,sy = 10,tx = 81,ty = 270) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 3,sy = 10,tx = 81,ty = 270) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 1,sy = 1,tx = 987654321,ty = 123456789) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 1,sy = 1,tx = 987654321,ty = 123456789) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 15,sy = 10,tx = 225,ty = 150) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 15,sy = 10,tx = 225,ty = 150) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 17,sy = 29,tx = 306,ty = 511) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 17,sy = 29,tx = 306,ty = 511) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 2,sy = 5,tx = 23,ty = 47) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 2,sy = 5,tx = 23,ty = 47) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 7,sy = 9,tx = 161,ty = 208) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 7,sy = 9,tx = 161,ty = 208) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 2,sy = 7,tx = 113,ty = 287) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 2,sy = 7,tx = 113,ty = 287) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 21,sy = 34,tx = 1597,ty = 2584) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 21,sy = 34,tx = 1597,ty = 2584) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 8,sy = 5,tx = 144,ty = 95) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 8,sy = 5,tx = 144,ty = 95) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 3,sy = 3,tx = 18,ty = 27) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 3,sy = 3,tx = 18,ty = 27) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 2,sy = 3,tx = 50,ty = 83) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 2,sy = 3,tx = 50,ty = 83) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 12345,sy = 67890,tx = 56789,ty = 45678) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 12345,sy = 67890,tx = 56789,ty = 45678) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 13,sy = 8,tx = 65,ty = 40) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 13,sy = 8,tx = 65,ty = 40) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 7,sy = 3,tx = 49,ty = 24) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 7,sy = 3,tx = 49,ty = 24) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 5,sy = 5,tx = 35,ty = 35) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 5,sy = 5,tx = 35,ty = 35) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 2,sy = 5,tx = 17,ty = 27) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 2,sy = 5,tx = 17,ty = 27) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 3,sy = 2,tx = 18,ty = 33) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 3,sy = 2,tx = 18,ty = 33) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 999999999,sy = 1,tx = 1000000000,ty = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 999999999,sy = 1,tx = 1000000000,ty = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 7,sy = 17,tx = 128,ty = 17) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 7,sy = 17,tx = 128,ty = 17) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 2,sy = 5,tx = 18,ty = 47) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 2,sy = 5,tx = 18,ty = 47) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 2,sy = 5,tx = 29,ty = 44) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 2,sy = 5,tx = 29,ty = 44) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 2,sy = 7,tx = 10,ty = 17) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 2,sy = 7,tx = 10,ty = 17) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 8,sy = 7,tx = 1000,ty = 875) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 8,sy = 7,tx = 1000,ty = 875) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 13,sy = 21,tx = 286,ty = 455) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 13,sy = 21,tx = 286,ty = 455) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 3,sy = 1,tx = 39,ty = 19) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 3,sy = 1,tx = 39,ty = 19) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 5,sy = 7,tx = 22,ty = 37) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 5,sy = 7,tx = 22,ty = 37) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 6,sy = 19,tx = 114,ty = 175) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 6,sy = 19,tx = 114,ty = 175) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 10,sy = 10,tx = 110,ty = 110) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 10,sy = 10,tx = 110,ty = 110) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 5,sy = 7,tx = 35,ty = 56) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 5,sy = 7,tx = 35,ty = 56) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 1,sy = 1,tx = 19,ty = 29) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 1,sy = 1,tx = 19,ty = 29) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 5,sy = 7,tx = 46,ty = 33) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 5,sy = 7,tx = 46,ty = 33) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 10,sy = 10,tx = 100000000,ty = 100000000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 10,sy = 10,tx = 100000000,ty = 100000000) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 5,sy = 6,tx = 60,ty = 55) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 5,sy = 6,tx = 60,ty = 55) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 10,sy = 4,tx = 100,ty = 64) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 10,sy = 4,tx = 100,ty = 64) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 8,sy = 13,tx = 104,ty = 169) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 8,sy = 13,tx = 104,ty = 169) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 13,sy = 8,tx = 104,ty = 80) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 13,sy = 8,tx = 104,ty = 80) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 7,sy = 17,tx = 119,ty = 203) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 7,sy = 17,tx = 119,ty = 203) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 2,sy = 3,tx = 1046527,ty = 165580141) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 2,sy = 3,tx = 1046527,ty = 165580141) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 4,sy = 9,tx = 100,ty = 225) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 4,sy = 9,tx = 100,ty = 225) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 1,sy = 2,tx = 47,ty = 70) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 1,sy = 2,tx = 47,ty = 70) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 1,sy = 1,tx = 55,ty = 89) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 1,sy = 1,tx = 55,ty = 89) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 3,sy = 9,tx = 27,ty = 81) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 3,sy = 9,tx = 27,ty = 81) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 4,sy = 6,tx = 144,ty = 216) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 4,sy = 6,tx = 144,ty = 216) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 3,sy = 9,tx = 81,ty = 243) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 3,sy = 9,tx = 81,ty = 243) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 8,sy = 13,tx = 233,ty = 377) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 8,sy = 13,tx = 233,ty = 377) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 5,sy = 5,tx = 125,ty = 125) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 5,sy = 5,tx = 125,ty = 125) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 11,sy = 22,tx = 121,ty = 242) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 11,sy = 22,tx = 121,ty = 242) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 13,sy = 21,tx = 34,ty = 55) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 13,sy = 21,tx = 34,ty = 55) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 3,sy = 11,tx = 121,ty = 55) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 3,sy = 11,tx = 121,ty = 55) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 10,sy = 10,tx = 100,ty = 100) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 10,sy = 10,tx = 100,ty = 100) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 12,sy = 18,tx = 108,ty = 162) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 12,sy = 18,tx = 108,ty = 162) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 10,sy = 15,tx = 150,ty = 225) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 10,sy = 15,tx = 150,ty = 225) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 3,sy = 1,tx = 10,ty = 7) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 3,sy = 1,tx = 10,ty = 7) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 11,sy = 23,tx = 132,ty = 303) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 11,sy = 23,tx = 132,ty = 303) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 1,sy = 2,tx = 5,ty = 8) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 1,sy = 2,tx = 5,ty = 8) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 7,sy = 11,tx = 217,ty = 352) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 7,sy = 11,tx = 217,ty = 352) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 7,sy = 3,tx = 31,ty = 9) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 7,sy = 3,tx = 31,ty = 9) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 5,sy = 10,tx = 100,ty = 150) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 5,sy = 10,tx = 100,ty = 150) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 8,sy = 5,tx = 8,ty = 13) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 8,sy = 5,tx = 8,ty = 13) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 12,sy = 18,tx = 324,ty = 486) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 12,sy = 18,tx = 324,ty = 486) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 3,sy = 5,tx = 100,ty = 150) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 3,sy = 5,tx = 100,ty = 150) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 1,sy = 1,tx = 987654321,ty = 987654321) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 1,sy = 1,tx = 987654321,ty = 987654321) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 1,sy = 2,tx = 1,ty = 1046527) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 1,sy = 2,tx = 1,ty = 1046527) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 21,sy = 34,tx = 55,ty = 89) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 21,sy = 34,tx = 55,ty = 89) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 5,sy = 2,tx = 27,ty = 11) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 5,sy = 2,tx = 27,ty = 11) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 2,sy = 5,tx = 29,ty = 37) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 2,sy = 5,tx = 29,ty = 37) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 5,sy = 7,tx = 1235,ty = 1907) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 5,sy = 7,tx = 1235,ty = 1907) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 100,sy = 1,tx = 999999999,ty = 1000000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 100,sy = 1,tx = 999999999,ty = 1000000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 21,sy = 14,tx = 420,ty = 280) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 21,sy = 14,tx = 420,ty = 280) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 3,sy = 3,tx = 99,ty = 99) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 3,sy = 3,tx = 99,ty = 99) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 8,sy = 3,tx = 217,ty = 58) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 8,sy = 3,tx = 217,ty = 58) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 1,sy = 2,tx = 1000000000,ty = 999999999) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 1,sy = 2,tx = 1000000000,ty = 999999999) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 10,sy = 15,tx = 110,ty = 165) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 10,sy = 15,tx = 110,ty = 165) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 5,sy = 8,tx = 165,ty = 280) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 5,sy = 8,tx = 165,ty = 280) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 10,sy = 15,tx = 100,ty = 150) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 10,sy = 15,tx = 100,ty = 150) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 1,sy = 1,tx = 1,ty = 1000000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 1,sy = 1,tx = 1,ty = 1000000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 5,sy = 17,tx = 104,ty = 193) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 5,sy = 17,tx = 104,ty = 193) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 7,sy = 3,tx = 105,ty = 45) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 7,sy = 3,tx = 105,ty = 45) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 8,sy = 13,tx = 184,ty = 299) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 8,sy = 13,tx = 184,ty = 299) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 7,sy = 17,tx = 196,ty = 511) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 7,sy = 17,tx = 196,ty = 511) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 2,sy = 5,tx = 29,ty = 17) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 2,sy = 5,tx = 29,ty = 17) == True: {e}')
    
    total += 1
    try:
        result = candidate(sx = 1,sy = 10,tx = 100,ty = 91) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 1,sy = 10,tx = 100,ty = 91) == False: {e}')
    
    total += 1
    try:
        result = candidate(sx = 2,sy = 1,tx = 1046527,ty = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sx = 2,sy = 1,tx = 1046527,ty = 1) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(sx = 1,sy = 1,tx = 3,ty = 5) == True
    assert candidate(sx = 3,sy = 4,tx = 3,ty = 12) == False
    assert candidate(sx = 3,sy = 7,tx = 31,ty = 19) == False
    assert candidate(sx = 1,sy = 1,tx = 1000000000,ty = 1000000000) == False
    assert candidate(sx = 5,sy = 5,tx = 5,ty = 5) == True
    assert candidate(sx = 1,sy = 1,tx = 1,ty = 1) == True
    assert candidate(sx = 1,sy = 1,tx = 2,ty = 2) == False
    assert candidate(sx = 2,sy = 3,tx = 8,ty = 11) == True
    assert candidate(sx = 5,sy = 1,tx = 1000000000,ty = 1000000000) == False
    assert candidate(sx = 2,sy = 3,tx = 10,ty = 15) == False
    assert candidate(sx = 5,sy = 5,tx = 100,ty = 100) == False
    assert candidate(sx = 1,sy = 1,tx = 1000000000,ty = 1) == True
    assert candidate(sx = 2,sy = 3,tx = 10,ty = 3) == False
    assert candidate(sx = 7,sy = 11,tx = 412,ty = 575) == False
    assert candidate(sx = 10,sy = 15,tx = 55,ty = 70) == True
    assert candidate(sx = 2,sy = 5,tx = 27,ty = 35) == False
    assert candidate(sx = 5,sy = 7,tx = 29,ty = 41) == True
    assert candidate(sx = 3,sy = 1,tx = 10,ty = 28) == False
    assert candidate(sx = 3,sy = 10,tx = 81,ty = 270) == False
    assert candidate(sx = 1,sy = 1,tx = 987654321,ty = 123456789) == False
    assert candidate(sx = 15,sy = 10,tx = 225,ty = 150) == False
    assert candidate(sx = 17,sy = 29,tx = 306,ty = 511) == False
    assert candidate(sx = 2,sy = 5,tx = 23,ty = 47) == False
    assert candidate(sx = 7,sy = 9,tx = 161,ty = 208) == False
    assert candidate(sx = 2,sy = 7,tx = 113,ty = 287) == False
    assert candidate(sx = 21,sy = 34,tx = 1597,ty = 2584) == False
    assert candidate(sx = 8,sy = 5,tx = 144,ty = 95) == False
    assert candidate(sx = 3,sy = 3,tx = 18,ty = 27) == False
    assert candidate(sx = 2,sy = 3,tx = 50,ty = 83) == False
    assert candidate(sx = 12345,sy = 67890,tx = 56789,ty = 45678) == False
    assert candidate(sx = 13,sy = 8,tx = 65,ty = 40) == False
    assert candidate(sx = 7,sy = 3,tx = 49,ty = 24) == False
    assert candidate(sx = 5,sy = 5,tx = 35,ty = 35) == False
    assert candidate(sx = 2,sy = 5,tx = 17,ty = 27) == False
    assert candidate(sx = 3,sy = 2,tx = 18,ty = 33) == False
    assert candidate(sx = 999999999,sy = 1,tx = 1000000000,ty = 1) == True
    assert candidate(sx = 7,sy = 17,tx = 128,ty = 17) == False
    assert candidate(sx = 2,sy = 5,tx = 18,ty = 47) == False
    assert candidate(sx = 2,sy = 5,tx = 29,ty = 44) == False
    assert candidate(sx = 2,sy = 7,tx = 10,ty = 17) == False
    assert candidate(sx = 8,sy = 7,tx = 1000,ty = 875) == False
    assert candidate(sx = 13,sy = 21,tx = 286,ty = 455) == False
    assert candidate(sx = 3,sy = 1,tx = 39,ty = 19) == False
    assert candidate(sx = 5,sy = 7,tx = 22,ty = 37) == False
    assert candidate(sx = 6,sy = 19,tx = 114,ty = 175) == False
    assert candidate(sx = 10,sy = 10,tx = 110,ty = 110) == False
    assert candidate(sx = 5,sy = 7,tx = 35,ty = 56) == False
    assert candidate(sx = 1,sy = 1,tx = 19,ty = 29) == True
    assert candidate(sx = 5,sy = 7,tx = 46,ty = 33) == False
    assert candidate(sx = 10,sy = 10,tx = 100000000,ty = 100000000) == False
    assert candidate(sx = 5,sy = 6,tx = 60,ty = 55) == False
    assert candidate(sx = 10,sy = 4,tx = 100,ty = 64) == False
    assert candidate(sx = 8,sy = 13,tx = 104,ty = 169) == False
    assert candidate(sx = 13,sy = 8,tx = 104,ty = 80) == False
    assert candidate(sx = 7,sy = 17,tx = 119,ty = 203) == False
    assert candidate(sx = 2,sy = 3,tx = 1046527,ty = 165580141) == False
    assert candidate(sx = 4,sy = 9,tx = 100,ty = 225) == False
    assert candidate(sx = 1,sy = 2,tx = 47,ty = 70) == True
    assert candidate(sx = 1,sy = 1,tx = 55,ty = 89) == True
    assert candidate(sx = 3,sy = 9,tx = 27,ty = 81) == False
    assert candidate(sx = 4,sy = 6,tx = 144,ty = 216) == False
    assert candidate(sx = 3,sy = 9,tx = 81,ty = 243) == False
    assert candidate(sx = 8,sy = 13,tx = 233,ty = 377) == False
    assert candidate(sx = 5,sy = 5,tx = 125,ty = 125) == False
    assert candidate(sx = 11,sy = 22,tx = 121,ty = 242) == False
    assert candidate(sx = 13,sy = 21,tx = 34,ty = 55) == True
    assert candidate(sx = 3,sy = 11,tx = 121,ty = 55) == False
    assert candidate(sx = 10,sy = 10,tx = 100,ty = 100) == False
    assert candidate(sx = 12,sy = 18,tx = 108,ty = 162) == False
    assert candidate(sx = 10,sy = 15,tx = 150,ty = 225) == False
    assert candidate(sx = 3,sy = 1,tx = 10,ty = 7) == True
    assert candidate(sx = 11,sy = 23,tx = 132,ty = 303) == False
    assert candidate(sx = 1,sy = 2,tx = 5,ty = 8) == False
    assert candidate(sx = 7,sy = 11,tx = 217,ty = 352) == False
    assert candidate(sx = 7,sy = 3,tx = 31,ty = 9) == False
    assert candidate(sx = 5,sy = 10,tx = 100,ty = 150) == False
    assert candidate(sx = 8,sy = 5,tx = 8,ty = 13) == True
    assert candidate(sx = 12,sy = 18,tx = 324,ty = 486) == False
    assert candidate(sx = 3,sy = 5,tx = 100,ty = 150) == False
    assert candidate(sx = 1,sy = 1,tx = 987654321,ty = 987654321) == False
    assert candidate(sx = 1,sy = 2,tx = 1,ty = 1046527) == True
    assert candidate(sx = 21,sy = 34,tx = 55,ty = 89) == True
    assert candidate(sx = 5,sy = 2,tx = 27,ty = 11) == False
    assert candidate(sx = 2,sy = 5,tx = 29,ty = 37) == False
    assert candidate(sx = 5,sy = 7,tx = 1235,ty = 1907) == False
    assert candidate(sx = 100,sy = 1,tx = 999999999,ty = 1000000000) == True
    assert candidate(sx = 21,sy = 14,tx = 420,ty = 280) == False
    assert candidate(sx = 3,sy = 3,tx = 99,ty = 99) == False
    assert candidate(sx = 8,sy = 3,tx = 217,ty = 58) == False
    assert candidate(sx = 1,sy = 2,tx = 1000000000,ty = 999999999) == True
    assert candidate(sx = 10,sy = 15,tx = 110,ty = 165) == False
    assert candidate(sx = 5,sy = 8,tx = 165,ty = 280) == False
    assert candidate(sx = 10,sy = 15,tx = 100,ty = 150) == False
    assert candidate(sx = 1,sy = 1,tx = 1,ty = 1000000000) == True
    assert candidate(sx = 5,sy = 17,tx = 104,ty = 193) == False
    assert candidate(sx = 7,sy = 3,tx = 105,ty = 45) == False
    assert candidate(sx = 8,sy = 13,tx = 184,ty = 299) == False
    assert candidate(sx = 7,sy = 17,tx = 196,ty = 511) == False
    assert candidate(sx = 2,sy = 5,tx = 29,ty = 17) == True
    assert candidate(sx = 1,sy = 10,tx = 100,ty = 91) == False
    assert candidate(sx = 2,sy = 1,tx = 1046527,ty = 1) == True


