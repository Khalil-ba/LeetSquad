def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(width = 4,height = 4,sideLength = 3,maxOnes = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 4,height = 4,sideLength = 3,maxOnes = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(width = 6,height = 6,sideLength = 3,maxOnes = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 6,height = 6,sideLength = 3,maxOnes = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(width = 10,height = 10,sideLength = 5,maxOnes = 6) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 10,height = 10,sideLength = 5,maxOnes = 6) == 24: {e}')
    
    total += 1
    try:
        result = candidate(width = 5,height = 5,sideLength = 3,maxOnes = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 5,height = 5,sideLength = 3,maxOnes = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(width = 4,height = 4,sideLength = 2,maxOnes = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 4,height = 4,sideLength = 2,maxOnes = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(width = 3,height = 3,sideLength = 2,maxOnes = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 3,height = 3,sideLength = 2,maxOnes = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(width = 3,height = 3,sideLength = 2,maxOnes = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 3,height = 3,sideLength = 2,maxOnes = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(width = 6,height = 6,sideLength = 2,maxOnes = 4) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 6,height = 6,sideLength = 2,maxOnes = 4) == 36: {e}')
    
    total += 1
    try:
        result = candidate(width = 100,height = 100,sideLength = 10,maxOnes = 25) == 2500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 100,height = 100,sideLength = 10,maxOnes = 25) == 2500: {e}')
    
    total += 1
    try:
        result = candidate(width = 6,height = 6,sideLength = 3,maxOnes = 4) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 6,height = 6,sideLength = 3,maxOnes = 4) == 16: {e}')
    
    total += 1
    try:
        result = candidate(width = 5,height = 5,sideLength = 3,maxOnes = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 5,height = 5,sideLength = 3,maxOnes = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(width = 4,height = 4,sideLength = 2,maxOnes = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 4,height = 4,sideLength = 2,maxOnes = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(width = 30,height = 25,sideLength = 7,maxOnes = 10) == 192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 30,height = 25,sideLength = 7,maxOnes = 10) == 192: {e}')
    
    total += 1
    try:
        result = candidate(width = 70,height = 70,sideLength = 25,maxOnes = 50) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 70,height = 70,sideLength = 25,maxOnes = 50) == 450: {e}')
    
    total += 1
    try:
        result = candidate(width = 80,height = 40,sideLength = 16,maxOnes = 6) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 80,height = 40,sideLength = 16,maxOnes = 6) == 90: {e}')
    
    total += 1
    try:
        result = candidate(width = 50,height = 30,sideLength = 12,maxOnes = 15) == 216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 50,height = 30,sideLength = 12,maxOnes = 15) == 216: {e}')
    
    total += 1
    try:
        result = candidate(width = 70,height = 60,sideLength = 12,maxOnes = 18) == 540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 70,height = 60,sideLength = 12,maxOnes = 18) == 540: {e}')
    
    total += 1
    try:
        result = candidate(width = 8,height = 16,sideLength = 5,maxOnes = 4) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 8,height = 16,sideLength = 5,maxOnes = 4) == 30: {e}')
    
    total += 1
    try:
        result = candidate(width = 21,height = 21,sideLength = 7,maxOnes = 12) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 21,height = 21,sideLength = 7,maxOnes = 12) == 108: {e}')
    
    total += 1
    try:
        result = candidate(width = 90,height = 45,sideLength = 9,maxOnes = 8) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 90,height = 45,sideLength = 9,maxOnes = 8) == 400: {e}')
    
    total += 1
    try:
        result = candidate(width = 12,height = 9,sideLength = 3,maxOnes = 4) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 12,height = 9,sideLength = 3,maxOnes = 4) == 48: {e}')
    
    total += 1
    try:
        result = candidate(width = 25,height = 35,sideLength = 8,maxOnes = 5) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 25,height = 35,sideLength = 8,maxOnes = 5) == 92: {e}')
    
    total += 1
    try:
        result = candidate(width = 20,height = 10,sideLength = 5,maxOnes = 6) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 20,height = 10,sideLength = 5,maxOnes = 6) == 48: {e}')
    
    total += 1
    try:
        result = candidate(width = 50,height = 50,sideLength = 8,maxOnes = 3) == 147
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 50,height = 50,sideLength = 8,maxOnes = 3) == 147: {e}')
    
    total += 1
    try:
        result = candidate(width = 8,height = 12,sideLength = 4,maxOnes = 4) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 8,height = 12,sideLength = 4,maxOnes = 4) == 24: {e}')
    
    total += 1
    try:
        result = candidate(width = 75,height = 100,sideLength = 15,maxOnes = 12) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 75,height = 100,sideLength = 15,maxOnes = 12) == 420: {e}')
    
    total += 1
    try:
        result = candidate(width = 40,height = 35,sideLength = 9,maxOnes = 18) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 40,height = 35,sideLength = 9,maxOnes = 18) == 360: {e}')
    
    total += 1
    try:
        result = candidate(width = 30,height = 40,sideLength = 12,maxOnes = 6) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 30,height = 40,sideLength = 12,maxOnes = 6) == 72: {e}')
    
    total += 1
    try:
        result = candidate(width = 100,height = 100,sideLength = 10,maxOnes = 5) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 100,height = 100,sideLength = 10,maxOnes = 5) == 500: {e}')
    
    total += 1
    try:
        result = candidate(width = 15,height = 20,sideLength = 5,maxOnes = 4) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 15,height = 20,sideLength = 5,maxOnes = 4) == 48: {e}')
    
    total += 1
    try:
        result = candidate(width = 7,height = 9,sideLength = 3,maxOnes = 2) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 7,height = 9,sideLength = 3,maxOnes = 2) == 18: {e}')
    
    total += 1
    try:
        result = candidate(width = 18,height = 15,sideLength = 3,maxOnes = 2) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 18,height = 15,sideLength = 3,maxOnes = 2) == 60: {e}')
    
    total += 1
    try:
        result = candidate(width = 90,height = 90,sideLength = 18,maxOnes = 27) == 675
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 90,height = 90,sideLength = 18,maxOnes = 27) == 675: {e}')
    
    total += 1
    try:
        result = candidate(width = 90,height = 50,sideLength = 10,maxOnes = 7) == 315
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 90,height = 50,sideLength = 10,maxOnes = 7) == 315: {e}')
    
    total += 1
    try:
        result = candidate(width = 7,height = 8,sideLength = 2,maxOnes = 1) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 7,height = 8,sideLength = 2,maxOnes = 1) == 16: {e}')
    
    total += 1
    try:
        result = candidate(width = 100,height = 100,sideLength = 10,maxOnes = 9) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 100,height = 100,sideLength = 10,maxOnes = 9) == 900: {e}')
    
    total += 1
    try:
        result = candidate(width = 70,height = 80,sideLength = 7,maxOnes = 10) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 70,height = 80,sideLength = 7,maxOnes = 10) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(width = 99,height = 100,sideLength = 10,maxOnes = 15) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 99,height = 100,sideLength = 10,maxOnes = 15) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(width = 16,height = 18,sideLength = 5,maxOnes = 6) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 16,height = 18,sideLength = 5,maxOnes = 6) == 84: {e}')
    
    total += 1
    try:
        result = candidate(width = 80,height = 70,sideLength = 14,maxOnes = 20) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 80,height = 70,sideLength = 14,maxOnes = 20) == 600: {e}')
    
    total += 1
    try:
        result = candidate(width = 30,height = 25,sideLength = 5,maxOnes = 15) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 30,height = 25,sideLength = 5,maxOnes = 15) == 450: {e}')
    
    total += 1
    try:
        result = candidate(width = 18,height = 18,sideLength = 6,maxOnes = 9) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 18,height = 18,sideLength = 6,maxOnes = 9) == 81: {e}')
    
    total += 1
    try:
        result = candidate(width = 12,height = 15,sideLength = 4,maxOnes = 3) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 12,height = 15,sideLength = 4,maxOnes = 3) == 36: {e}')
    
    total += 1
    try:
        result = candidate(width = 100,height = 100,sideLength = 50,maxOnes = 1500) == 6000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 100,height = 100,sideLength = 50,maxOnes = 1500) == 6000: {e}')
    
    total += 1
    try:
        result = candidate(width = 95,height = 65,sideLength = 13,maxOnes = 9) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 95,height = 65,sideLength = 13,maxOnes = 9) == 360: {e}')
    
    total += 1
    try:
        result = candidate(width = 60,height = 70,sideLength = 10,maxOnes = 8) == 336
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 60,height = 70,sideLength = 10,maxOnes = 8) == 336: {e}')
    
    total += 1
    try:
        result = candidate(width = 100,height = 100,sideLength = 25,maxOnes = 10) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 100,height = 100,sideLength = 25,maxOnes = 10) == 160: {e}')
    
    total += 1
    try:
        result = candidate(width = 20,height = 15,sideLength = 4,maxOnes = 5) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 20,height = 15,sideLength = 4,maxOnes = 5) == 100: {e}')
    
    total += 1
    try:
        result = candidate(width = 75,height = 45,sideLength = 10,maxOnes = 4) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 75,height = 45,sideLength = 10,maxOnes = 4) == 160: {e}')
    
    total += 1
    try:
        result = candidate(width = 16,height = 16,sideLength = 8,maxOnes = 16) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 16,height = 16,sideLength = 8,maxOnes = 16) == 64: {e}')
    
    total += 1
    try:
        result = candidate(width = 50,height = 40,sideLength = 10,maxOnes = 15) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 50,height = 40,sideLength = 10,maxOnes = 15) == 300: {e}')
    
    total += 1
    try:
        result = candidate(width = 15,height = 15,sideLength = 5,maxOnes = 8) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 15,height = 15,sideLength = 5,maxOnes = 8) == 72: {e}')
    
    total += 1
    try:
        result = candidate(width = 9,height = 6,sideLength = 2,maxOnes = 2) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 9,height = 6,sideLength = 2,maxOnes = 2) == 30: {e}')
    
    total += 1
    try:
        result = candidate(width = 120,height = 120,sideLength = 25,maxOnes = 30) == 750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 120,height = 120,sideLength = 25,maxOnes = 30) == 750: {e}')
    
    total += 1
    try:
        result = candidate(width = 50,height = 50,sideLength = 13,maxOnes = 10) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 50,height = 50,sideLength = 13,maxOnes = 10) == 160: {e}')
    
    total += 1
    try:
        result = candidate(width = 80,height = 70,sideLength = 7,maxOnes = 20) == 2400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 80,height = 70,sideLength = 7,maxOnes = 20) == 2400: {e}')
    
    total += 1
    try:
        result = candidate(width = 75,height = 75,sideLength = 12,maxOnes = 7) == 343
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 75,height = 75,sideLength = 12,maxOnes = 7) == 343: {e}')
    
    total += 1
    try:
        result = candidate(width = 10,height = 8,sideLength = 3,maxOnes = 5) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 10,height = 8,sideLength = 3,maxOnes = 5) == 51: {e}')
    
    total += 1
    try:
        result = candidate(width = 60,height = 70,sideLength = 14,maxOnes = 8) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 60,height = 70,sideLength = 14,maxOnes = 8) == 200: {e}')
    
    total += 1
    try:
        result = candidate(width = 60,height = 60,sideLength = 12,maxOnes = 10) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 60,height = 60,sideLength = 12,maxOnes = 10) == 250: {e}')
    
    total += 1
    try:
        result = candidate(width = 15,height = 15,sideLength = 4,maxOnes = 5) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 15,height = 15,sideLength = 4,maxOnes = 5) == 80: {e}')
    
    total += 1
    try:
        result = candidate(width = 20,height = 20,sideLength = 7,maxOnes = 10) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 20,height = 20,sideLength = 7,maxOnes = 10) == 90: {e}')
    
    total += 1
    try:
        result = candidate(width = 40,height = 30,sideLength = 6,maxOnes = 9) == 315
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 40,height = 30,sideLength = 6,maxOnes = 9) == 315: {e}')
    
    total += 1
    try:
        result = candidate(width = 70,height = 30,sideLength = 14,maxOnes = 4) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 70,height = 30,sideLength = 14,maxOnes = 4) == 60: {e}')
    
    total += 1
    try:
        result = candidate(width = 9,height = 12,sideLength = 4,maxOnes = 4) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 9,height = 12,sideLength = 4,maxOnes = 4) == 36: {e}')
    
    total += 1
    try:
        result = candidate(width = 18,height = 12,sideLength = 6,maxOnes = 6) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 18,height = 12,sideLength = 6,maxOnes = 6) == 36: {e}')
    
    total += 1
    try:
        result = candidate(width = 22,height = 18,sideLength = 6,maxOnes = 10) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 22,height = 18,sideLength = 6,maxOnes = 10) == 120: {e}')
    
    total += 1
    try:
        result = candidate(width = 15,height = 20,sideLength = 5,maxOnes = 7) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 15,height = 20,sideLength = 5,maxOnes = 7) == 84: {e}')
    
    total += 1
    try:
        result = candidate(width = 75,height = 85,sideLength = 8,maxOnes = 25) == 2649
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 75,height = 85,sideLength = 8,maxOnes = 25) == 2649: {e}')
    
    total += 1
    try:
        result = candidate(width = 100,height = 100,sideLength = 20,maxOnes = 25) == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 100,height = 100,sideLength = 20,maxOnes = 25) == 625: {e}')
    
    total += 1
    try:
        result = candidate(width = 9,height = 12,sideLength = 4,maxOnes = 3) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 9,height = 12,sideLength = 4,maxOnes = 3) == 27: {e}')
    
    total += 1
    try:
        result = candidate(width = 60,height = 60,sideLength = 10,maxOnes = 5) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 60,height = 60,sideLength = 10,maxOnes = 5) == 180: {e}')
    
    total += 1
    try:
        result = candidate(width = 25,height = 25,sideLength = 6,maxOnes = 9) == 185
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 25,height = 25,sideLength = 6,maxOnes = 9) == 185: {e}')
    
    total += 1
    try:
        result = candidate(width = 9,height = 10,sideLength = 4,maxOnes = 3) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 9,height = 10,sideLength = 4,maxOnes = 3) == 24: {e}')
    
    total += 1
    try:
        result = candidate(width = 100,height = 100,sideLength = 15,maxOnes = 30) == 1470
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 100,height = 100,sideLength = 15,maxOnes = 30) == 1470: {e}')
    
    total += 1
    try:
        result = candidate(width = 90,height = 80,sideLength = 16,maxOnes = 25) == 750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 90,height = 80,sideLength = 16,maxOnes = 25) == 750: {e}')
    
    total += 1
    try:
        result = candidate(width = 8,height = 10,sideLength = 3,maxOnes = 2) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 8,height = 10,sideLength = 3,maxOnes = 2) == 24: {e}')
    
    total += 1
    try:
        result = candidate(width = 100,height = 90,sideLength = 18,maxOnes = 30) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 100,height = 90,sideLength = 18,maxOnes = 30) == 900: {e}')
    
    total += 1
    try:
        result = candidate(width = 8,height = 6,sideLength = 4,maxOnes = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 8,height = 6,sideLength = 4,maxOnes = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(width = 30,height = 20,sideLength = 6,maxOnes = 10) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 30,height = 20,sideLength = 6,maxOnes = 10) == 200: {e}')
    
    total += 1
    try:
        result = candidate(width = 97,height = 83,sideLength = 13,maxOnes = 20) == 1120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 97,height = 83,sideLength = 13,maxOnes = 20) == 1120: {e}')
    
    total += 1
    try:
        result = candidate(width = 15,height = 20,sideLength = 5,maxOnes = 8) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 15,height = 20,sideLength = 5,maxOnes = 8) == 96: {e}')
    
    total += 1
    try:
        result = candidate(width = 90,height = 90,sideLength = 11,maxOnes = 22) == 1620
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 90,height = 90,sideLength = 11,maxOnes = 22) == 1620: {e}')
    
    total += 1
    try:
        result = candidate(width = 50,height = 50,sideLength = 20,maxOnes = 15) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 50,height = 50,sideLength = 20,maxOnes = 15) == 135: {e}')
    
    total += 1
    try:
        result = candidate(width = 11,height = 11,sideLength = 4,maxOnes = 2) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 11,height = 11,sideLength = 4,maxOnes = 2) == 18: {e}')
    
    total += 1
    try:
        result = candidate(width = 90,height = 50,sideLength = 15,maxOnes = 8) == 192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 90,height = 50,sideLength = 15,maxOnes = 8) == 192: {e}')
    
    total += 1
    try:
        result = candidate(width = 60,height = 45,sideLength = 5,maxOnes = 12) == 1296
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 60,height = 45,sideLength = 5,maxOnes = 12) == 1296: {e}')
    
    total += 1
    try:
        result = candidate(width = 60,height = 50,sideLength = 8,maxOnes = 12) == 644
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 60,height = 50,sideLength = 8,maxOnes = 12) == 644: {e}')
    
    total += 1
    try:
        result = candidate(width = 15,height = 20,sideLength = 7,maxOnes = 5) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 15,height = 20,sideLength = 7,maxOnes = 5) == 45: {e}')
    
    total += 1
    try:
        result = candidate(width = 55,height = 55,sideLength = 5,maxOnes = 3) == 363
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 55,height = 55,sideLength = 5,maxOnes = 3) == 363: {e}')
    
    total += 1
    try:
        result = candidate(width = 15,height = 12,sideLength = 5,maxOnes = 7) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 15,height = 12,sideLength = 5,maxOnes = 7) == 63: {e}')
    
    total += 1
    try:
        result = candidate(width = 14,height = 14,sideLength = 7,maxOnes = 9) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 14,height = 14,sideLength = 7,maxOnes = 9) == 36: {e}')
    
    total += 1
    try:
        result = candidate(width = 14,height = 14,sideLength = 6,maxOnes = 9) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 14,height = 14,sideLength = 6,maxOnes = 9) == 66: {e}')
    
    total += 1
    try:
        result = candidate(width = 100,height = 50,sideLength = 20,maxOnes = 18) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 100,height = 50,sideLength = 20,maxOnes = 18) == 270: {e}')
    
    total += 1
    try:
        result = candidate(width = 85,height = 75,sideLength = 15,maxOnes = 20) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 85,height = 75,sideLength = 15,maxOnes = 20) == 600: {e}')
    
    total += 1
    try:
        result = candidate(width = 99,height = 99,sideLength = 17,maxOnes = 12) == 432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 99,height = 99,sideLength = 17,maxOnes = 12) == 432: {e}')
    
    total += 1
    try:
        result = candidate(width = 60,height = 60,sideLength = 12,maxOnes = 16) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 60,height = 60,sideLength = 12,maxOnes = 16) == 400: {e}')
    
    total += 1
    try:
        result = candidate(width = 85,height = 65,sideLength = 20,maxOnes = 25) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 85,height = 65,sideLength = 20,maxOnes = 25) == 500: {e}')
    
    total += 1
    try:
        result = candidate(width = 25,height = 25,sideLength = 5,maxOnes = 12) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 25,height = 25,sideLength = 5,maxOnes = 12) == 300: {e}')
    
    total += 1
    try:
        result = candidate(width = 45,height = 55,sideLength = 18,maxOnes = 9) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 45,height = 55,sideLength = 18,maxOnes = 9) == 108: {e}')
    
    total += 1
    try:
        result = candidate(width = 80,height = 80,sideLength = 15,maxOnes = 10) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 80,height = 80,sideLength = 15,maxOnes = 10) == 360: {e}')
    
    total += 1
    try:
        result = candidate(width = 60,height = 60,sideLength = 15,maxOnes = 20) == 320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 60,height = 60,sideLength = 15,maxOnes = 20) == 320: {e}')
    
    total += 1
    try:
        result = candidate(width = 8,height = 12,sideLength = 4,maxOnes = 3) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 8,height = 12,sideLength = 4,maxOnes = 3) == 18: {e}')
    
    total += 1
    try:
        result = candidate(width = 11,height = 11,sideLength = 4,maxOnes = 3) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 11,height = 11,sideLength = 4,maxOnes = 3) == 27: {e}')
    
    total += 1
    try:
        result = candidate(width = 85,height = 55,sideLength = 11,maxOnes = 7) == 280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 85,height = 55,sideLength = 11,maxOnes = 7) == 280: {e}')
    
    total += 1
    try:
        result = candidate(width = 25,height = 30,sideLength = 7,maxOnes = 10) == 192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 25,height = 30,sideLength = 7,maxOnes = 10) == 192: {e}')
    
    total += 1
    try:
        result = candidate(width = 25,height = 30,sideLength = 4,maxOnes = 5) == 258
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 25,height = 30,sideLength = 4,maxOnes = 5) == 258: {e}')
    
    total += 1
    try:
        result = candidate(width = 45,height = 55,sideLength = 17,maxOnes = 20) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 45,height = 55,sideLength = 17,maxOnes = 20) == 240: {e}')
    
    total += 1
    try:
        result = candidate(width = 70,height = 70,sideLength = 7,maxOnes = 12) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 70,height = 70,sideLength = 7,maxOnes = 12) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(width = 45,height = 55,sideLength = 11,maxOnes = 12) == 295
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(width = 45,height = 55,sideLength = 11,maxOnes = 12) == 295: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(width = 4,height = 4,sideLength = 3,maxOnes = 2) == 6
    assert candidate(width = 6,height = 6,sideLength = 3,maxOnes = 3) == 12
    assert candidate(width = 10,height = 10,sideLength = 5,maxOnes = 6) == 24
    assert candidate(width = 5,height = 5,sideLength = 3,maxOnes = 3) == 12
    assert candidate(width = 4,height = 4,sideLength = 2,maxOnes = 3) == 12
    assert candidate(width = 3,height = 3,sideLength = 2,maxOnes = 1) == 4
    assert candidate(width = 3,height = 3,sideLength = 2,maxOnes = 2) == 6
    assert candidate(width = 6,height = 6,sideLength = 2,maxOnes = 4) == 36
    assert candidate(width = 100,height = 100,sideLength = 10,maxOnes = 25) == 2500
    assert candidate(width = 6,height = 6,sideLength = 3,maxOnes = 4) == 16
    assert candidate(width = 5,height = 5,sideLength = 3,maxOnes = 2) == 8
    assert candidate(width = 4,height = 4,sideLength = 2,maxOnes = 1) == 4
    assert candidate(width = 30,height = 25,sideLength = 7,maxOnes = 10) == 192
    assert candidate(width = 70,height = 70,sideLength = 25,maxOnes = 50) == 450
    assert candidate(width = 80,height = 40,sideLength = 16,maxOnes = 6) == 90
    assert candidate(width = 50,height = 30,sideLength = 12,maxOnes = 15) == 216
    assert candidate(width = 70,height = 60,sideLength = 12,maxOnes = 18) == 540
    assert candidate(width = 8,height = 16,sideLength = 5,maxOnes = 4) == 30
    assert candidate(width = 21,height = 21,sideLength = 7,maxOnes = 12) == 108
    assert candidate(width = 90,height = 45,sideLength = 9,maxOnes = 8) == 400
    assert candidate(width = 12,height = 9,sideLength = 3,maxOnes = 4) == 48
    assert candidate(width = 25,height = 35,sideLength = 8,maxOnes = 5) == 92
    assert candidate(width = 20,height = 10,sideLength = 5,maxOnes = 6) == 48
    assert candidate(width = 50,height = 50,sideLength = 8,maxOnes = 3) == 147
    assert candidate(width = 8,height = 12,sideLength = 4,maxOnes = 4) == 24
    assert candidate(width = 75,height = 100,sideLength = 15,maxOnes = 12) == 420
    assert candidate(width = 40,height = 35,sideLength = 9,maxOnes = 18) == 360
    assert candidate(width = 30,height = 40,sideLength = 12,maxOnes = 6) == 72
    assert candidate(width = 100,height = 100,sideLength = 10,maxOnes = 5) == 500
    assert candidate(width = 15,height = 20,sideLength = 5,maxOnes = 4) == 48
    assert candidate(width = 7,height = 9,sideLength = 3,maxOnes = 2) == 18
    assert candidate(width = 18,height = 15,sideLength = 3,maxOnes = 2) == 60
    assert candidate(width = 90,height = 90,sideLength = 18,maxOnes = 27) == 675
    assert candidate(width = 90,height = 50,sideLength = 10,maxOnes = 7) == 315
    assert candidate(width = 7,height = 8,sideLength = 2,maxOnes = 1) == 16
    assert candidate(width = 100,height = 100,sideLength = 10,maxOnes = 9) == 900
    assert candidate(width = 70,height = 80,sideLength = 7,maxOnes = 10) == 1200
    assert candidate(width = 99,height = 100,sideLength = 10,maxOnes = 15) == 1500
    assert candidate(width = 16,height = 18,sideLength = 5,maxOnes = 6) == 84
    assert candidate(width = 80,height = 70,sideLength = 14,maxOnes = 20) == 600
    assert candidate(width = 30,height = 25,sideLength = 5,maxOnes = 15) == 450
    assert candidate(width = 18,height = 18,sideLength = 6,maxOnes = 9) == 81
    assert candidate(width = 12,height = 15,sideLength = 4,maxOnes = 3) == 36
    assert candidate(width = 100,height = 100,sideLength = 50,maxOnes = 1500) == 6000
    assert candidate(width = 95,height = 65,sideLength = 13,maxOnes = 9) == 360
    assert candidate(width = 60,height = 70,sideLength = 10,maxOnes = 8) == 336
    assert candidate(width = 100,height = 100,sideLength = 25,maxOnes = 10) == 160
    assert candidate(width = 20,height = 15,sideLength = 4,maxOnes = 5) == 100
    assert candidate(width = 75,height = 45,sideLength = 10,maxOnes = 4) == 160
    assert candidate(width = 16,height = 16,sideLength = 8,maxOnes = 16) == 64
    assert candidate(width = 50,height = 40,sideLength = 10,maxOnes = 15) == 300
    assert candidate(width = 15,height = 15,sideLength = 5,maxOnes = 8) == 72
    assert candidate(width = 9,height = 6,sideLength = 2,maxOnes = 2) == 30
    assert candidate(width = 120,height = 120,sideLength = 25,maxOnes = 30) == 750
    assert candidate(width = 50,height = 50,sideLength = 13,maxOnes = 10) == 160
    assert candidate(width = 80,height = 70,sideLength = 7,maxOnes = 20) == 2400
    assert candidate(width = 75,height = 75,sideLength = 12,maxOnes = 7) == 343
    assert candidate(width = 10,height = 8,sideLength = 3,maxOnes = 5) == 51
    assert candidate(width = 60,height = 70,sideLength = 14,maxOnes = 8) == 200
    assert candidate(width = 60,height = 60,sideLength = 12,maxOnes = 10) == 250
    assert candidate(width = 15,height = 15,sideLength = 4,maxOnes = 5) == 80
    assert candidate(width = 20,height = 20,sideLength = 7,maxOnes = 10) == 90
    assert candidate(width = 40,height = 30,sideLength = 6,maxOnes = 9) == 315
    assert candidate(width = 70,height = 30,sideLength = 14,maxOnes = 4) == 60
    assert candidate(width = 9,height = 12,sideLength = 4,maxOnes = 4) == 36
    assert candidate(width = 18,height = 12,sideLength = 6,maxOnes = 6) == 36
    assert candidate(width = 22,height = 18,sideLength = 6,maxOnes = 10) == 120
    assert candidate(width = 15,height = 20,sideLength = 5,maxOnes = 7) == 84
    assert candidate(width = 75,height = 85,sideLength = 8,maxOnes = 25) == 2649
    assert candidate(width = 100,height = 100,sideLength = 20,maxOnes = 25) == 625
    assert candidate(width = 9,height = 12,sideLength = 4,maxOnes = 3) == 27
    assert candidate(width = 60,height = 60,sideLength = 10,maxOnes = 5) == 180
    assert candidate(width = 25,height = 25,sideLength = 6,maxOnes = 9) == 185
    assert candidate(width = 9,height = 10,sideLength = 4,maxOnes = 3) == 24
    assert candidate(width = 100,height = 100,sideLength = 15,maxOnes = 30) == 1470
    assert candidate(width = 90,height = 80,sideLength = 16,maxOnes = 25) == 750
    assert candidate(width = 8,height = 10,sideLength = 3,maxOnes = 2) == 24
    assert candidate(width = 100,height = 90,sideLength = 18,maxOnes = 30) == 900
    assert candidate(width = 8,height = 6,sideLength = 4,maxOnes = 5) == 20
    assert candidate(width = 30,height = 20,sideLength = 6,maxOnes = 10) == 200
    assert candidate(width = 97,height = 83,sideLength = 13,maxOnes = 20) == 1120
    assert candidate(width = 15,height = 20,sideLength = 5,maxOnes = 8) == 96
    assert candidate(width = 90,height = 90,sideLength = 11,maxOnes = 22) == 1620
    assert candidate(width = 50,height = 50,sideLength = 20,maxOnes = 15) == 135
    assert candidate(width = 11,height = 11,sideLength = 4,maxOnes = 2) == 18
    assert candidate(width = 90,height = 50,sideLength = 15,maxOnes = 8) == 192
    assert candidate(width = 60,height = 45,sideLength = 5,maxOnes = 12) == 1296
    assert candidate(width = 60,height = 50,sideLength = 8,maxOnes = 12) == 644
    assert candidate(width = 15,height = 20,sideLength = 7,maxOnes = 5) == 45
    assert candidate(width = 55,height = 55,sideLength = 5,maxOnes = 3) == 363
    assert candidate(width = 15,height = 12,sideLength = 5,maxOnes = 7) == 63
    assert candidate(width = 14,height = 14,sideLength = 7,maxOnes = 9) == 36
    assert candidate(width = 14,height = 14,sideLength = 6,maxOnes = 9) == 66
    assert candidate(width = 100,height = 50,sideLength = 20,maxOnes = 18) == 270
    assert candidate(width = 85,height = 75,sideLength = 15,maxOnes = 20) == 600
    assert candidate(width = 99,height = 99,sideLength = 17,maxOnes = 12) == 432
    assert candidate(width = 60,height = 60,sideLength = 12,maxOnes = 16) == 400
    assert candidate(width = 85,height = 65,sideLength = 20,maxOnes = 25) == 500
    assert candidate(width = 25,height = 25,sideLength = 5,maxOnes = 12) == 300
    assert candidate(width = 45,height = 55,sideLength = 18,maxOnes = 9) == 108
    assert candidate(width = 80,height = 80,sideLength = 15,maxOnes = 10) == 360
    assert candidate(width = 60,height = 60,sideLength = 15,maxOnes = 20) == 320
    assert candidate(width = 8,height = 12,sideLength = 4,maxOnes = 3) == 18
    assert candidate(width = 11,height = 11,sideLength = 4,maxOnes = 3) == 27
    assert candidate(width = 85,height = 55,sideLength = 11,maxOnes = 7) == 280
    assert candidate(width = 25,height = 30,sideLength = 7,maxOnes = 10) == 192
    assert candidate(width = 25,height = 30,sideLength = 4,maxOnes = 5) == 258
    assert candidate(width = 45,height = 55,sideLength = 17,maxOnes = 20) == 240
    assert candidate(width = 70,height = 70,sideLength = 7,maxOnes = 12) == 1200
    assert candidate(width = 45,height = 55,sideLength = 11,maxOnes = 12) == 295


