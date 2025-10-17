def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(x = -3,y = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -3,y = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 300,y = 0) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 300,y = 0) == 150: {e}')
    
    total += 1
    try:
        result = candidate(x = -3,y = -2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -3,y = -2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = -200,y = 150) == 118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -200,y = 150) == 118: {e}')
    
    total += 1
    try:
        result = candidate(x = -300,y = 0) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -300,y = 0) == 150: {e}')
    
    total += 1
    try:
        result = candidate(x = 100,y = 100) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 100,y = 100) == 68: {e}')
    
    total += 1
    try:
        result = candidate(x = 0,y = 300) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0,y = 300) == 150: {e}')
    
    total += 1
    try:
        result = candidate(x = 250,y = 250) == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 250,y = 250) == 168: {e}')
    
    total += 1
    try:
        result = candidate(x = -150,y = -150) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -150,y = -150) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = -10,y = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -10,y = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(x = 5,y = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,y = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = 1,y = 0) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1,y = 0) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 299,y = 1) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 299,y = 1) == 150: {e}')
    
    total += 1
    try:
        result = candidate(x = 250,y = -250) == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 250,y = -250) == 168: {e}')
    
    total += 1
    try:
        result = candidate(x = 200,y = 150) == 118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 200,y = 150) == 118: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = -10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = -10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(x = 2,y = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2,y = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = -2,y = -1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -2,y = -1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = -1,y = -2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -1,y = -2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 0,y = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0,y = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(x = -150,y = -200) == 118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -150,y = -200) == 118: {e}')
    
    total += 1
    try:
        result = candidate(x = 100,y = -100) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 100,y = -100) == 68: {e}')
    
    total += 1
    try:
        result = candidate(x = -299,y = -1) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -299,y = -1) == 150: {e}')
    
    total += 1
    try:
        result = candidate(x = -200,y = -200) == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -200,y = -200) == 134: {e}')
    
    total += 1
    try:
        result = candidate(x = 1,y = 299) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1,y = 299) == 150: {e}')
    
    total += 1
    try:
        result = candidate(x = -299,y = 299) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -299,y = 299) == 200: {e}')
    
    total += 1
    try:
        result = candidate(x = -100,y = 200) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -100,y = 200) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = -100,y = -100) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -100,y = -100) == 68: {e}')
    
    total += 1
    try:
        result = candidate(x = 280,y = -280) == 188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 280,y = -280) == 188: {e}')
    
    total += 1
    try:
        result = candidate(x = 20,y = 20) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,y = 20) == 14: {e}')
    
    total += 1
    try:
        result = candidate(x = -130,y = 130) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -130,y = 130) == 88: {e}')
    
    total += 1
    try:
        result = candidate(x = 249,y = 250) == 167
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 249,y = 250) == 167: {e}')
    
    total += 1
    try:
        result = candidate(x = 200,y = -100) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 200,y = -100) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = -250,y = 250) == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -250,y = 250) == 168: {e}')
    
    total += 1
    try:
        result = candidate(x = -456,y = -123) == 229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -456,y = -123) == 229: {e}')
    
    total += 1
    try:
        result = candidate(x = -200,y = 200) == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -200,y = 200) == 134: {e}')
    
    total += 1
    try:
        result = candidate(x = 100,y = 0) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 100,y = 0) == 50: {e}')
    
    total += 1
    try:
        result = candidate(x = -200,y = 50) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -200,y = 50) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = 0,y = 200) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0,y = 200) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = -100,y = 0) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -100,y = 0) == 50: {e}')
    
    total += 1
    try:
        result = candidate(x = -299,y = -299) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -299,y = -299) == 200: {e}')
    
    total += 1
    try:
        result = candidate(x = 150,y = 200) == 118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 150,y = 200) == 118: {e}')
    
    total += 1
    try:
        result = candidate(x = -200,y = -150) == 118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -200,y = -150) == 118: {e}')
    
    total += 1
    try:
        result = candidate(x = 299,y = 299) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 299,y = 299) == 200: {e}')
    
    total += 1
    try:
        result = candidate(x = 0,y = -100) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0,y = -100) == 50: {e}')
    
    total += 1
    try:
        result = candidate(x = -99,y = 100) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -99,y = 100) == 67: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 280) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 280) == 140: {e}')
    
    total += 1
    try:
        result = candidate(x = 200,y = -50) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 200,y = -50) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = -299,y = 1) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -299,y = 1) == 150: {e}')
    
    total += 1
    try:
        result = candidate(x = 40,y = 260) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 40,y = 260) == 130: {e}')
    
    total += 1
    try:
        result = candidate(x = -290,y = -290) == 194
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -290,y = -290) == 194: {e}')
    
    total += 1
    try:
        result = candidate(x = -100,y = 250) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -100,y = 250) == 126: {e}')
    
    total += 1
    try:
        result = candidate(x = -3,y = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -3,y = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(x = -250,y = -100) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -250,y = -100) == 126: {e}')
    
    total += 1
    try:
        result = candidate(x = -200,y = -50) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -200,y = -50) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = 200,y = 50) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 200,y = 50) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = 250,y = -150) == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 250,y = -150) == 134: {e}')
    
    total += 1
    try:
        result = candidate(x = -140,y = -140) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -140,y = -140) == 94: {e}')
    
    total += 1
    try:
        result = candidate(x = 200,y = 100) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 200,y = 100) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = 0,y = -200) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0,y = -200) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = 299,y = -299) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 299,y = -299) == 200: {e}')
    
    total += 1
    try:
        result = candidate(x = 3,y = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3,y = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(x = -100,y = 100) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -100,y = 100) == 68: {e}')
    
    total += 1
    try:
        result = candidate(x = 0,y = -300) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0,y = -300) == 150: {e}')
    
    total += 1
    try:
        result = candidate(x = 250,y = 249) == 167
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 250,y = 249) == 167: {e}')
    
    total += 1
    try:
        result = candidate(x = -250,y = -249) == 167
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -250,y = -249) == 167: {e}')
    
    total += 1
    try:
        result = candidate(x = 270,y = 270) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 270,y = 270) == 180: {e}')
    
    total += 1
    try:
        result = candidate(x = -260,y = 260) == 174
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -260,y = 260) == 174: {e}')
    
    total += 1
    try:
        result = candidate(x = 260,y = 40) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 260,y = 40) == 130: {e}')
    
    total += 1
    try:
        result = candidate(x = 2,y = -2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2,y = -2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = -50,y = -200) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -50,y = -200) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = -249,y = -250) == 167
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -249,y = -250) == 167: {e}')
    
    total += 1
    try:
        result = candidate(x = -200,y = -100) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -200,y = -100) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = -200,y = -199) == 133
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -200,y = -199) == 133: {e}')
    
    total += 1
    try:
        result = candidate(x = 250,y = 100) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 250,y = 100) == 126: {e}')
    
    total += 1
    try:
        result = candidate(x = -10,y = -10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -10,y = -10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(x = 290,y = 290) == 194
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 290,y = 290) == 194: {e}')
    
    total += 1
    try:
        result = candidate(x = 0,y = 100) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0,y = 100) == 50: {e}')
    
    total += 1
    try:
        result = candidate(x = -120,y = -120) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -120,y = -120) == 80: {e}')
    
    total += 1
    try:
        result = candidate(x = 140,y = 140) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 140,y = 140) == 94: {e}')
    
    total += 1
    try:
        result = candidate(x = 200,y = 200) == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 200,y = 200) == 134: {e}')
    
    total += 1
    try:
        result = candidate(x = -456,y = 123) == 229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -456,y = 123) == 229: {e}')
    
    total += 1
    try:
        result = candidate(x = 456,y = 123) == 229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 456,y = 123) == 229: {e}')
    
    total += 1
    try:
        result = candidate(x = 299,y = 0) == 151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 299,y = 0) == 151: {e}')
    
    total += 1
    try:
        result = candidate(x = -280,y = 280) == 188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -280,y = 280) == 188: {e}')
    
    total += 1
    try:
        result = candidate(x = -10,y = -280) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -10,y = -280) == 140: {e}')
    
    total += 1
    try:
        result = candidate(x = 50,y = 50) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 50,y = 50) == 34: {e}')
    
    total += 1
    try:
        result = candidate(x = 100,y = 99) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 100,y = 99) == 67: {e}')
    
    total += 1
    try:
        result = candidate(x = 200,y = -200) == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 200,y = -200) == 134: {e}')
    
    total += 1
    try:
        result = candidate(x = -40,y = -260) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -40,y = -260) == 130: {e}')
    
    total += 1
    try:
        result = candidate(x = 199,y = 200) == 133
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 199,y = 200) == 133: {e}')
    
    total += 1
    try:
        result = candidate(x = 101,y = 101) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 101,y = 101) == 68: {e}')
    
    total += 1
    try:
        result = candidate(x = 1,y = -1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1,y = -1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(x = 200,y = -150) == 118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 200,y = -150) == 118: {e}')
    
    total += 1
    try:
        result = candidate(x = 280,y = 10) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 280,y = 10) == 140: {e}')
    
    total += 1
    try:
        result = candidate(x = -20,y = -20) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -20,y = -20) == 14: {e}')
    
    total += 1
    try:
        result = candidate(x = 150,y = -150) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 150,y = -150) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = 260,y = -260) == 174
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 260,y = -260) == 174: {e}')
    
    total += 1
    try:
        result = candidate(x = 0,y = -299) == 151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0,y = -299) == 151: {e}')
    
    total += 1
    try:
        result = candidate(x = 150,y = 150) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 150,y = 150) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = 250,y = 240) == 164
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 250,y = 240) == 164: {e}')
    
    total += 1
    try:
        result = candidate(x = 123,y = -456) == 229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 123,y = -456) == 229: {e}')
    
    total += 1
    try:
        result = candidate(x = 120,y = 120) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 120,y = 120) == 80: {e}')
    
    total += 1
    try:
        result = candidate(x = -123,y = -456) == 229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -123,y = -456) == 229: {e}')
    
    total += 1
    try:
        result = candidate(x = 130,y = -130) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 130,y = -130) == 88: {e}')
    
    total += 1
    try:
        result = candidate(x = -299,y = 0) == 151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -299,y = 0) == 151: {e}')
    
    total += 1
    try:
        result = candidate(x = 200,y = 0) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 200,y = 0) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = -200,y = 0) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -200,y = 0) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = -1,y = -299) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -1,y = -299) == 150: {e}')
    
    total += 1
    try:
        result = candidate(x = 100,y = -250) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 100,y = -250) == 126: {e}')
    
    total += 1
    try:
        result = candidate(x = 150,y = 140) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 150,y = 140) == 98: {e}')
    
    total += 1
    try:
        result = candidate(x = 123,y = 456) == 229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 123,y = 456) == 229: {e}')
    
    total += 1
    try:
        result = candidate(x = -150,y = 200) == 118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -150,y = 200) == 118: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(x = -150,y = 150) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -150,y = 150) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = -270,y = -270) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -270,y = -270) == 180: {e}')
    
    total += 1
    try:
        result = candidate(x = -101,y = -101) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -101,y = -101) == 68: {e}')
    
    total += 1
    try:
        result = candidate(x = -50,y = -50) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -50,y = -50) == 34: {e}')
    
    total += 1
    try:
        result = candidate(x = 0,y = 299) == 151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0,y = 299) == 151: {e}')
    
    total += 1
    try:
        result = candidate(x = -260,y = -40) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -260,y = -40) == 130: {e}')
    
    total += 1
    try:
        result = candidate(x = 100,y = -200) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 100,y = -200) == 100: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(x = -3,y = 2) == 3
    assert candidate(x = 300,y = 0) == 150
    assert candidate(x = -3,y = -2) == 3
    assert candidate(x = -200,y = 150) == 118
    assert candidate(x = -300,y = 0) == 150
    assert candidate(x = 100,y = 100) == 68
    assert candidate(x = 0,y = 300) == 150
    assert candidate(x = 250,y = 250) == 168
    assert candidate(x = -150,y = -150) == 100
    assert candidate(x = -10,y = 10) == 8
    assert candidate(x = 5,y = 5) == 4
    assert candidate(x = 1,y = 0) == 3
    assert candidate(x = 299,y = 1) == 150
    assert candidate(x = 250,y = -250) == 168
    assert candidate(x = 200,y = 150) == 118
    assert candidate(x = 10,y = -10) == 8
    assert candidate(x = 2,y = 1) == 1
    assert candidate(x = -2,y = -1) == 1
    assert candidate(x = -1,y = -2) == 1
    assert candidate(x = 0,y = 0) == 0
    assert candidate(x = -150,y = -200) == 118
    assert candidate(x = 100,y = -100) == 68
    assert candidate(x = -299,y = -1) == 150
    assert candidate(x = -200,y = -200) == 134
    assert candidate(x = 1,y = 299) == 150
    assert candidate(x = -299,y = 299) == 200
    assert candidate(x = -100,y = 200) == 100
    assert candidate(x = -100,y = -100) == 68
    assert candidate(x = 280,y = -280) == 188
    assert candidate(x = 20,y = 20) == 14
    assert candidate(x = -130,y = 130) == 88
    assert candidate(x = 249,y = 250) == 167
    assert candidate(x = 200,y = -100) == 100
    assert candidate(x = -250,y = 250) == 168
    assert candidate(x = -456,y = -123) == 229
    assert candidate(x = -200,y = 200) == 134
    assert candidate(x = 100,y = 0) == 50
    assert candidate(x = -200,y = 50) == 100
    assert candidate(x = 0,y = 200) == 100
    assert candidate(x = -100,y = 0) == 50
    assert candidate(x = -299,y = -299) == 200
    assert candidate(x = 150,y = 200) == 118
    assert candidate(x = -200,y = -150) == 118
    assert candidate(x = 299,y = 299) == 200
    assert candidate(x = 0,y = -100) == 50
    assert candidate(x = -99,y = 100) == 67
    assert candidate(x = 10,y = 280) == 140
    assert candidate(x = 200,y = -50) == 100
    assert candidate(x = -299,y = 1) == 150
    assert candidate(x = 40,y = 260) == 130
    assert candidate(x = -290,y = -290) == 194
    assert candidate(x = -100,y = 250) == 126
    assert candidate(x = -3,y = 3) == 2
    assert candidate(x = -250,y = -100) == 126
    assert candidate(x = -200,y = -50) == 100
    assert candidate(x = 200,y = 50) == 100
    assert candidate(x = 250,y = -150) == 134
    assert candidate(x = -140,y = -140) == 94
    assert candidate(x = 200,y = 100) == 100
    assert candidate(x = 0,y = -200) == 100
    assert candidate(x = 299,y = -299) == 200
    assert candidate(x = 3,y = 3) == 2
    assert candidate(x = -100,y = 100) == 68
    assert candidate(x = 0,y = -300) == 150
    assert candidate(x = 250,y = 249) == 167
    assert candidate(x = -250,y = -249) == 167
    assert candidate(x = 270,y = 270) == 180
    assert candidate(x = -260,y = 260) == 174
    assert candidate(x = 260,y = 40) == 130
    assert candidate(x = 2,y = -2) == 4
    assert candidate(x = -50,y = -200) == 100
    assert candidate(x = -249,y = -250) == 167
    assert candidate(x = -200,y = -100) == 100
    assert candidate(x = -200,y = -199) == 133
    assert candidate(x = 250,y = 100) == 126
    assert candidate(x = -10,y = -10) == 8
    assert candidate(x = 290,y = 290) == 194
    assert candidate(x = 0,y = 100) == 50
    assert candidate(x = -120,y = -120) == 80
    assert candidate(x = 140,y = 140) == 94
    assert candidate(x = 200,y = 200) == 134
    assert candidate(x = -456,y = 123) == 229
    assert candidate(x = 456,y = 123) == 229
    assert candidate(x = 299,y = 0) == 151
    assert candidate(x = -280,y = 280) == 188
    assert candidate(x = -10,y = -280) == 140
    assert candidate(x = 50,y = 50) == 34
    assert candidate(x = 100,y = 99) == 67
    assert candidate(x = 200,y = -200) == 134
    assert candidate(x = -40,y = -260) == 130
    assert candidate(x = 199,y = 200) == 133
    assert candidate(x = 101,y = 101) == 68
    assert candidate(x = 1,y = -1) == 2
    assert candidate(x = 200,y = -150) == 118
    assert candidate(x = 280,y = 10) == 140
    assert candidate(x = -20,y = -20) == 14
    assert candidate(x = 150,y = -150) == 100
    assert candidate(x = 260,y = -260) == 174
    assert candidate(x = 0,y = -299) == 151
    assert candidate(x = 150,y = 150) == 100
    assert candidate(x = 250,y = 240) == 164
    assert candidate(x = 123,y = -456) == 229
    assert candidate(x = 120,y = 120) == 80
    assert candidate(x = -123,y = -456) == 229
    assert candidate(x = 130,y = -130) == 88
    assert candidate(x = -299,y = 0) == 151
    assert candidate(x = 200,y = 0) == 100
    assert candidate(x = -200,y = 0) == 100
    assert candidate(x = -1,y = -299) == 150
    assert candidate(x = 100,y = -250) == 126
    assert candidate(x = 150,y = 140) == 98
    assert candidate(x = 123,y = 456) == 229
    assert candidate(x = -150,y = 200) == 118
    assert candidate(x = 10,y = 10) == 8
    assert candidate(x = -150,y = 150) == 100
    assert candidate(x = -270,y = -270) == 180
    assert candidate(x = -101,y = -101) == 68
    assert candidate(x = -50,y = -50) == 34
    assert candidate(x = 0,y = 299) == 151
    assert candidate(x = -260,y = -40) == 130
    assert candidate(x = 100,y = -200) == 100


