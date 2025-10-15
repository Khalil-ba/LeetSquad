def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3,k = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,k = 125) == 173
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,k = 125) == 173: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,k = 150) == 152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,k = 150) == 152: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,k = 150) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,k = 150) == 76: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 100) == 189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 100) == 189: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,k = 50) == 138
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,k = 50) == 138: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,k = 300) == 265
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,k = 300) == 265: {e}')
    
    total += 1
    try:
        result = candidate(n = 450,k = 450) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450,k = 450) == 87: {e}')
    
    total += 1
    try:
        result = candidate(n = 123,k = 123) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123,k = 123) == 94: {e}')
    
    total += 1
    try:
        result = candidate(n = 499,k = 250) == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 499,k = 250) == 134: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,k = 200) == 139
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,k = 200) == 139: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 13) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 13) == 70: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 1) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 1) == 500: {e}')
    
    total += 1
    try:
        result = candidate(n = 37,k = 37) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37,k = 37) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 250) == 384
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 250) == 384: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 19) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 19) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 199) == 163
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 199) == 163: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 99) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 99) == 88: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 29) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 29) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 2) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 2) == 37: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,k = 89) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,k = 89) == 225: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,k = 3) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,k = 3) == 41: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 10) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 10) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 37) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 37) == 45: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 7) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 7) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 23) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 23) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 19) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 19) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 50) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 50) == 95: {e}')
    
    total += 1
    try:
        result = candidate(n = 123,k = 45) == 116
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123,k = 45) == 116: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 13) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 13) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 2) == 489
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 2) == 489: {e}')
    
    total += 1
    try:
        result = candidate(n = 499,k = 300) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 499,k = 300) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 1) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 1) == 200: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,k = 299) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,k = 299) == 145: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,k = 399) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,k = 399) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 125,k = 124) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125,k = 124) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,k = 75) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,k = 75) == 125: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 350,k = 7) == 211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 350,k = 7) == 211: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,k = 2) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,k = 2) == 45: {e}')
    
    total += 1
    try:
        result = candidate(n = 123,k = 57) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123,k = 57) == 77: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,k = 41) == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,k = 41) == 79: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 67) == 163
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 67) == 163: {e}')
    
    total += 1
    try:
        result = candidate(n = 499,k = 499) == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 499,k = 499) == 122: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 499) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 499) == 121: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 500) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 500) == 69: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,k = 100) == 313
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,k = 100) == 313: {e}')
    
    total += 1
    try:
        result = candidate(n = 499,k = 5) == 327
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 499,k = 5) == 327: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 50) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 50) == 23: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,k = 249) == 204
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,k = 249) == 204: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 13) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 13) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 11) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 11) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 450,k = 3) == 286
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450,k = 3) == 286: {e}')
    
    total += 1
    try:
        result = candidate(n = 450,k = 449) == 143
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450,k = 449) == 143: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 13) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 13) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 11) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 11) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 37,k = 13) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37,k = 13) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 11) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 11) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,k = 100) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,k = 100) == 59: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 19) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 19) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 120,k = 1) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120,k = 1) == 120: {e}')
    
    total += 1
    try:
        result = candidate(n = 299,k = 299) == 146
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 299,k = 299) == 146: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 17) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 17) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,k = 1) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,k = 1) == 150: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,k = 100) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,k = 100) == 23: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 20) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 20) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 373,k = 186) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 373,k = 186) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 499,k = 2) == 487
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 499,k = 2) == 487: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 25) == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3,k = 1) == 3
    assert candidate(n = 3,k = 3) == 2
    assert candidate(n = 5,k = 2) == 3
    assert candidate(n = 7,k = 3) == 4
    assert candidate(n = 7,k = 1) == 7
    assert candidate(n = 6,k = 5) == 1
    assert candidate(n = 7,k = 7) == 5
    assert candidate(n = 1,k = 1) == 1
    assert candidate(n = 4,k = 4) == 2
    assert candidate(n = 10,k = 4) == 5
    assert candidate(n = 10,k = 3) == 4
    assert candidate(n = 250,k = 125) == 173
    assert candidate(n = 300,k = 150) == 152
    assert candidate(n = 250,k = 150) == 76
    assert candidate(n = 200,k = 100) == 189
    assert candidate(n = 150,k = 50) == 138
    assert candidate(n = 300,k = 300) == 265
    assert candidate(n = 450,k = 450) == 87
    assert candidate(n = 123,k = 123) == 94
    assert candidate(n = 499,k = 250) == 134
    assert candidate(n = 300,k = 200) == 139
    assert candidate(n = 100,k = 13) == 70
    assert candidate(n = 500,k = 1) == 500
    assert candidate(n = 37,k = 37) == 16
    assert candidate(n = 500,k = 250) == 384
    assert candidate(n = 20,k = 19) == 11
    assert candidate(n = 200,k = 199) == 163
    assert candidate(n = 100,k = 99) == 88
    assert candidate(n = 30,k = 15) == 4
    assert candidate(n = 50,k = 7) == 1
    assert candidate(n = 30,k = 29) == 25
    assert candidate(n = 50,k = 2) == 37
    assert candidate(n = 250,k = 89) == 225
    assert candidate(n = 250,k = 3) == 41
    assert candidate(n = 50,k = 10) == 36
    assert candidate(n = 100,k = 37) == 45
    assert candidate(n = 40,k = 7) == 24
    assert candidate(n = 45,k = 23) == 36
    assert candidate(n = 45,k = 19) == 14
    assert candidate(n = 100,k = 50) == 95
    assert candidate(n = 123,k = 45) == 116
    assert candidate(n = 45,k = 13) == 36
    assert candidate(n = 500,k = 2) == 489
    assert candidate(n = 499,k = 300) == 36
    assert candidate(n = 200,k = 1) == 200
    assert candidate(n = 300,k = 299) == 145
    assert candidate(n = 400,k = 399) == 30
    assert candidate(n = 125,k = 124) == 31
    assert candidate(n = 150,k = 75) == 125
    assert candidate(n = 20,k = 7) == 3
    assert candidate(n = 350,k = 7) == 211
    assert candidate(n = 150,k = 2) == 45
    assert candidate(n = 123,k = 57) == 77
    assert candidate(n = 150,k = 41) == 79
    assert candidate(n = 200,k = 67) == 163
    assert candidate(n = 499,k = 499) == 122
    assert candidate(n = 500,k = 499) == 121
    assert candidate(n = 500,k = 500) == 69
    assert candidate(n = 400,k = 100) == 313
    assert candidate(n = 499,k = 5) == 327
    assert candidate(n = 200,k = 50) == 23
    assert candidate(n = 20,k = 5) == 7
    assert candidate(n = 250,k = 249) == 204
    assert candidate(n = 40,k = 13) == 14
    assert candidate(n = 50,k = 11) == 10
    assert candidate(n = 450,k = 3) == 286
    assert candidate(n = 450,k = 449) == 143
    assert candidate(n = 50,k = 13) == 5
    assert candidate(n = 15,k = 11) == 12
    assert candidate(n = 37,k = 13) == 14
    assert candidate(n = 15,k = 7) == 5
    assert candidate(n = 30,k = 11) == 28
    assert candidate(n = 300,k = 100) == 59
    assert candidate(n = 40,k = 19) == 6
    assert candidate(n = 120,k = 1) == 120
    assert candidate(n = 299,k = 299) == 146
    assert candidate(n = 50,k = 17) == 8
    assert candidate(n = 150,k = 1) == 150
    assert candidate(n = 250,k = 100) == 23
    assert candidate(n = 45,k = 20) == 29
    assert candidate(n = 373,k = 186) == 14
    assert candidate(n = 499,k = 2) == 487
    assert candidate(n = 50,k = 25) == 5


