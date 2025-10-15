def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128],target = 82) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128],target = 82) == 82: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 0],target = -100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 0],target = -100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -2, -5, -1],target = -12) == -13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -2, -5, -1],target = -12) == -13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1],target = -10) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1],target = -10) == -10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0],target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0],target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1],target = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1],target = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5],target = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5],target = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5],target = -10) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5],target = -10) == -10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 2, -1, -4],target = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 2, -1, -4],target = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, 1, -4],target = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, 1, -4],target = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 3, 4, 2],target = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 3, 4, 2],target = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1],target = 0) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1],target = 0) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],target = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],target = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],target = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],target = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 4, 5],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 4, 5],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, -999, 888, -888, 777, -777, 666, -666, 555, -555, 444, -444, 333, -333, 222, -222, 111, -111],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, -999, 888, -888, 777, -777, 666, -666, 555, -555, 444, -444, 333, -333, 222, -222, 111, -111],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 45) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 45) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 1500) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 1500) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 7, 8, 8, 10, 12, 13, 15, 17, 19, 21, 23, 25, 27],target = 30) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 7, 8, 8, 10, 12, 13, 15, 17, 19, 21, 23, 25, 27],target = 30) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 50) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 50) == 49: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -200, -300, -400, -500, 100, 200, 300, 400, 500],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -200, -300, -400, -500, 100, 200, 300, 400, 500],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 45) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 45) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],target = -100) == -57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],target = -100) == -57: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],target = -30) == -27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],target = -30) == -27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100],target = 150) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100],target = 150) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, 1, 2, 3, 4, 5],target = -150) == -120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, 1, 2, 3, 4, 5],target = -150) == -120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 50) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 50) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, -4, 8, 11, 1, -1, 6],target = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, -4, 8, 11, 1, -1, 6],target = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 500, -500, 250, -250, 125, -125],target = 100) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 500, -500, 250, -250, 125, -125],target = 100) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -1, 0, 2, 4, 6, 9, 12],target = 14) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -1, 0, 2, 4, 6, 9, 12],target = 14) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 2, -1, -4, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 2, -1, -4, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110, -120],target = -300) == -300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110, -120],target = -300) == -300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, 50, 40, 30, 20, 10],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, 50, 40, 30, 20, 10],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 100) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 100) == 57: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -2, -1, 0, 1, 2, 5],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -2, -1, 0, 1, 2, 5],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],target = -5) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],target = -5) == -5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],target = -150) == -150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],target = -150) == -150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],target = -25) == -25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],target = -25) == -25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 8, 9, 15, 1, 7, 6, 4, 10],target = 28) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 8, 9, 15, 1, 7, 6, 4, 10],target = 28) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 500, -500, 250, -250, 0, 1, -1],target = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 500, -500, 250, -250, 0, 1, -1],target = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 55, 77, 99, 111, 133, 155, 177, 199, 221, 243, 265, 287, 309, 331, 353, 375, 397, 419, 441],target = 1200) == 1191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 55, 77, 99, 111, 133, 155, 177, 199, 221, 243, 265, 287, 309, 331, 353, 375, 397, 419, 441],target = 1200) == 1191: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 20, 10, 5, 1],target = 120) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 20, 10, 5, 1],target = 120) == 121: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 0, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 0, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90],target = 100) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90],target = 100) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],target = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],target = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 1000, -1000, 999, -999, 1, -1, 2, -2],target = 3000) == 2998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 1000, -1000, 999, -999, 1, -1, 2, -2],target = 3000) == 2998: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],target = -45) == -42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],target = -45) == -42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -8, 4, 5, -10, 7, 0, 1],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -8, 4, 5, -10, 7, 0, 1],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],target = 300) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],target = 300) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, 1000, -500, 500, -250, 250, 0, 1, -1, 2, -2],target = 1001) == 1001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, 1000, -500, 500, -250, 250, 0, 1, -1, 2, -2],target = 1001) == 1001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -200, -300, 400, 500, 600, 700],target = -150) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -200, -300, 400, 500, 600, 700],target = -150) == -100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0],target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0],target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200, 1300, -1400, 1500],target = 500) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200, 1300, -1400, 1500],target = 500) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, -999, -998, -997, 0, 997, 998, 999, 1000],target = 500) == 995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, -999, -998, -997, 0, 997, 998, 999, 1000],target = 500) == 995: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],target = 50) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],target = 50) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 0, -1, 0],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 0, -1, 0],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -3, -1, 0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -3, -1, 0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],target = 100) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],target = 100) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 500, -500, 250, -250, 125, -125],target = 50) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 500, -500, 250, -250, 125, -125],target = 50) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600],target = 1000) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600],target = 1000) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 1000) == 570
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 1000) == 570: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],target = 50) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],target = 50) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],target = -250) == -250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],target = -250) == -250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, 100, -50, 50, -25, 25, 0],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, 100, -50, 50, -25, 25, 0],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],target = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],target = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, -100, -200, -300, -400, -500],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, -100, -200, -300, -400, -500],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 30) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 30) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-999, -998, -997, -996, -995, -994, -993, -992, -991, -990, -989, -988, -987, -986, -985, -984, -983, -982, -981, -980],target = -3000) == -2994
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-999, -998, -997, -996, -995, -994, -993, -992, -991, -990, -989, -988, -987, -986, -985, -984, -983, -982, -981, -980],target = -3000) == -2994: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 30) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 30) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900],target = 1500) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900],target = 1500) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 15) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 15) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],target = -25) == -25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],target = -25) == -25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -25, -27, -29],target = -45) == -45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -25, -27, -29],target = -45) == -45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-2, 0, 1, 1, 2],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2, 0, 1, 1, 2],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 250) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 250) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],target = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],target = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, -30, -10, 0, 10, 30, 50],target = 40) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, -30, -10, 0, 10, 30, 50],target = 40) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],target = -250) == -250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],target = -250) == -250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 500, -500, 250, -250, 125, -125],target = 0) == -125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 500, -500, 250, -250, 125, -125],target = 0) == -125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 40) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 40) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -2, -1, 0, 1, 2, 3],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -2, -1, 0, 1, 2, 3],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128],target = 100) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128],target = 100) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 15) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 15) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],target = 150) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],target = 150) == 87: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128],target = 82) == 82
    assert candidate(nums = [1, 1, 1, 0],target = -100) == 2
    assert candidate(nums = [-10, -2, -5, -1],target = -12) == -13
    assert candidate(nums = [-5, -4, -3, -2, -1],target = -10) == -10
    assert candidate(nums = [0, 0, 0],target = 1) == 0
    assert candidate(nums = [1, 1, 1, 1],target = 3) == 3
    assert candidate(nums = [5, 5, 5, 5],target = 15) == 15
    assert candidate(nums = [-1, -2, -3, -4, -5],target = -10) == -10
    assert candidate(nums = [-1, 0, 1, 2, -1, -4],target = 1) == 1
    assert candidate(nums = [-1, 2, 1, -4],target = 1) == 2
    assert candidate(nums = [5, 1, 3, 4, 2],target = 7) == 7
    assert candidate(nums = [1, 1, 1, 1],target = 0) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],target = 15) == 15
    assert candidate(nums = [1, 2, 3, 4, 5],target = 10) == 10
    assert candidate(nums = [-5, -4, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 4, 5],target = 0) == 0
    assert candidate(nums = [999, -999, 888, -888, 777, -777, 666, -666, 555, -555, 444, -444, 333, -333, 222, -222, 111, -111],target = 0) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 25) == 25
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 45) == 42
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 1500) == 1500
    assert candidate(nums = [5, 7, 7, 8, 8, 10, 12, 13, 15, 17, 19, 21, 23, 25, 27],target = 30) == 30
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 50) == 49
    assert candidate(nums = [-100, -200, -300, -400, -500, 100, 200, 300, 400, 500],target = 0) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 45) == 45
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 0) == 0
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],target = -100) == -57
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],target = -30) == -27
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100],target = 150) == 150
    assert candidate(nums = [-10, -20, -30, -40, -50, 1, 2, 3, 4, 5],target = -150) == -120
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 50) == 42
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 25) == 25
    assert candidate(nums = [3, 5, -4, 8, 11, 1, -1, 6],target = 10) == 10
    assert candidate(nums = [1000, -1000, 500, -500, 250, -250, 125, -125],target = 100) == 125
    assert candidate(nums = [-3, -1, 0, 2, 4, 6, 9, 12],target = 14) == 14
    assert candidate(nums = [-1, 0, 1, 2, -1, -4, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 15
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110, -120],target = -300) == -300
    assert candidate(nums = [-10, -20, -30, -40, -50, 50, 40, 30, 20, 10],target = 0) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 100) == 57
    assert candidate(nums = [-5, -2, -1, 0, 1, 2, 5],target = 0) == 0
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],target = -5) == -5
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],target = -150) == -150
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],target = -25) == -25
    assert candidate(nums = [3, 5, 8, 9, 15, 1, 7, 6, 4, 10],target = 28) == 28
    assert candidate(nums = [1000, -1000, 500, -500, 250, -250, 0, 1, -1],target = 100) == 1
    assert candidate(nums = [33, 55, 77, 99, 111, 133, 155, 177, 199, 221, 243, 265, 287, 309, 331, 353, 375, 397, 419, 441],target = 1200) == 1191
    assert candidate(nums = [100, 50, 25, 20, 10, 5, 1],target = 120) == 121
    assert candidate(nums = [-1, 0, 1, 0, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6],target = 0) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 15) == 15
    assert candidate(nums = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90],target = 100) == 100
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],target = 20) == 20
    assert candidate(nums = [999, 1000, -1000, 999, -999, 1, -1, 2, -2],target = 3000) == 2998
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],target = -45) == -42
    assert candidate(nums = [-1, 2, -8, 4, 5, -10, 7, 0, 1],target = 0) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],target = 300) == 300
    assert candidate(nums = [-1000, 1000, -500, 500, -250, 250, 0, 1, -1, 2, -2],target = 1001) == 1001
    assert candidate(nums = [-100, -200, -300, 400, 500, 600, 700],target = -150) == -100
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0],target = 1) == 0
    assert candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200, 1300, -1400, 1500],target = 500) == 500
    assert candidate(nums = [-1000, -999, -998, -997, 0, 997, 998, 999, 1000],target = 500) == 995
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],target = 50) == 50
    assert candidate(nums = [-1, 0, 1, 0, -1, 0],target = 0) == 0
    assert candidate(nums = [-5, -3, -1, 0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],target = 0) == 0
    assert candidate(nums = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 1) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],target = 100) == 100
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],target = 0) == 0
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80],target = 0) == 0
    assert candidate(nums = [1000, -1000, 500, -500, 250, -250, 125, -125],target = 50) == 125
    assert candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600],target = 1000) == 1000
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 9) == 9
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 1000) == 570
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],target = 50) == 50
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 15
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],target = -250) == -250
    assert candidate(nums = [-100, 100, -50, 50, -25, 25, 0],target = 0) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],target = 1) == 1
    assert candidate(nums = [100, 200, 300, 400, 500, -100, -200, -300, -400, -500],target = 0) == 0
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 30) == 30
    assert candidate(nums = [-999, -998, -997, -996, -995, -994, -993, -992, -991, -990, -989, -988, -987, -986, -985, -984, -983, -982, -981, -980],target = -3000) == -2994
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 30) == 30
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 0) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 10) == 15
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900],target = 1500) == 1500
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 15) == 9
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],target = -25) == -25
    assert candidate(nums = [-1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -25, -27, -29],target = -45) == -45
    assert candidate(nums = [-2, 0, 1, 1, 2],target = 0) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 250) == 250
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],target = 20) == 20
    assert candidate(nums = [-50, -30, -10, 0, 10, 30, 50],target = 40) == 40
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8],target = 0) == 0
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],target = -250) == -250
    assert candidate(nums = [1000, -1000, 500, -500, 250, -250, 125, -125],target = 0) == -125
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 40) == 40
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 3) == 3
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 15
    assert candidate(nums = [-3, -2, -1, 0, 1, 2, 3],target = 0) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 15
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128],target = 100) == 100
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 15) == 14
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],target = 150) == 87


