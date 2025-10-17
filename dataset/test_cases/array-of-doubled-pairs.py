def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 2, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 2, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 16, 8, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 16, 8, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-5, -2, -10, -1, -1, -5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-5, -2, -10, -1, -1, -5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, -3, 3, -2, 2, -4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, -3, 3, -2, 2, -4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, -2, 2, -4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, -2, 2, -4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 6, 4, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 6, 4, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 16, 8, 32]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 16, 8, 32]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 1, 2, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 1, 2, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-2, 4, -2, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-2, 4, -2, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -2, -3, -6, -6, -12]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -2, -3, -6, -6, -12]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-2, 4, -8, 16, -32, 64]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-2, 4, -8, 16, -32, 64]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 6, 6, 12]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 6, 6, 12]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 3, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 3, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -2, -2, -4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -2, -2, -4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 4, 4, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 4, 4, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 6, 5, 10, 15, 30, 4, 8, 12, 24, 20, 40, 60, 120]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 6, 5, 10, 15, 30, 4, 8, 12, 24, 20, 40, 60, 120]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 18]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 18]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 18, 15, 12, 6, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 18, 15, 12, 6, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 6, 5, 10, 15, 30, 4, 8, 12, 24, 20, 40, 60, 120, 7, 14, 21, 42]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 6, 5, 10, 15, 30, 4, 8, 12, 24, 20, 40, 60, 120, 7, 14, 21, 42]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 10, 20, 25, 50]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 10, 20, 25, 50]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 14, 28, 56, 112, 224, 448, 896, 1792, 3584]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 14, 28, 56, 112, 224, 448, 896, 1792, 3584]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 2, 1, 10, 5, 20, 2, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 2, 1, 10, 5, 20, 2, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 4, 4, 8, 8, 16]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 4, 4, 8, 8, 16]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 1, -1, 1, -2, 2, -2, 2, -4, 4, -4, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 1, -1, 1, -2, 2, -2, 2, -4, 4, -4, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-8, -4, -2, -1, -16, -32, -2, -4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-8, -4, -2, -1, -16, -32, -2, -4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 2, -2, 4, -4, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 2, -2, 4, -4, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -2, -3, -6, -5, -10, -15, -30, -4, -8, -12, -24, -20, -40, -60, -120, -7, -14, -21, -42]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -2, -3, -6, -5, -10, -15, -30, -4, -8, -12, -24, -20, -40, -60, -120, -7, -14, -21, -42]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 3, 6, 12, 24]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 3, 6, 12, 24]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 8, 16, 32]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 8, 16, 32]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 2, -2, 1, -4, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 2, -2, 1, -4, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100000, -100000, 50000, -50000, 25000, -25000, 12500, -12500]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100000, -100000, 50000, -50000, 25000, -25000, 12500, -12500]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 50]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 50]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100000, -100000, 50000, -50000, 25000, -25000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100000, -100000, 50000, -50000, 25000, -25000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-100000, 100000, -50000, 50000, -25000, 25000, -12500, 12500]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-100000, 100000, -50000, 50000, -25000, 25000, -12500, 12500]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 3, 6, 12, 24, 48, 96, 192, 384, 768]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 3, 6, 12, 24, 48, 96, 192, 384, 768]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-2, -4, -8, -16, -32, -64, -128, -256]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-2, -4, -8, -16, -32, -64, -128, -256]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, -5, 10, -10, 20, -20, 40, -40]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, -5, 10, -10, 20, -20, 40, -40]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-5, -10, -15, -20, -25, -50]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-5, -10, -15, -20, -25, -50]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-2, 4, 1, -1, 2, -2, -4, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-2, 4, 1, -1, 2, -2, -4, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 6, 12, 24, 48, 96, 192, 384, 768]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 6, 12, 24, 48, 96, 192, 384, 768]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100000, -100000, 50000, -50000, 25000, -25000, 12500, -12500, 6250, -6250]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100000, -100000, 50000, -50000, 25000, -25000, 12500, -12500, 6250, -6250]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 6, 8, 12, 16, 24, 32]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 6, 8, 12, 16, 24, 32]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 20, 40, 80, 160, 320, 640]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 20, 40, 80, 160, 320, 640]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 2, 8, 4, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 2, 8, 4, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 2, 6, 10, 14, 4, 12]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 2, 6, 10, 14, 4, 12]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-3, 3, -6, 6, -12, 12, -24, 24]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-3, 3, -6, 6, -12, 12, -24, 24]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100000, -100000, 50000, -50000, 25000, -25000, 12500, -12500, 6250, -6250, 3125, -3125, 15625, -15625, 78125, -78125]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100000, -100000, 50000, -50000, 25000, -25000, 12500, -12500, 6250, -6250, 3125, -3125, 15625, -15625, 78125, -78125]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 50, 100, 150, 200, 250]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 50, 100, 150, 200, 250]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 5, 5, 15, 20, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 5, 5, 15, 20, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 6, 4, 8, 9, 18, 12, 24]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 6, 4, 8, 9, 18, 12, 24]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-4, -8, -2, -1, -16, -2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-4, -8, -2, -1, -16, -2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 6, 6, 12, 12]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 6, 6, 12, 12]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 10, 20, 30, 40, 50, 60]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 10, 20, 30, 40, 50, 60]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 5, 20, 10, 40, 20, 80]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 5, 20, 10, 40, 20, 80]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 3, 6, 9, 18, 27, 54]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 3, 6, 9, 18, 27, 54]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -2, -4, -8, -16, -32, -64, -128, -256, -512, -1024, -2048]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -2, -4, -8, -16, -32, -64, -128, -256, -512, -1024, -2048]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 1, 2, 18, 9, 27, 54]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 1, 2, 18, 9, 27, 54]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 3, 3, 12, 2, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 3, 3, 12, 2, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 40, 5, 15, 30, 60]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 40, 5, 15, 30, 60]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 4, 4, 8, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 4, 4, 8, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 6, 4, 8, 5, 10, 7, 14, 9, 18, 11, 22, 12, 24]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 6, 4, 8, 5, 10, 7, 14, 9, 18, 11, 22, 12, 24]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 1, -2, 2, -4, 4, -8, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 1, -2, 2, -4, 4, -8, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 4, 8, 16, 32, 64]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 4, 8, 16, 32, 64]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 2, -2, 1, -4, 4, -8, 8, 16, -16]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 2, -2, 1, -4, 4, -8, 8, 16, -16]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 9, 1, 27, 3, 9, 27, 81]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 9, 1, 27, 3, 9, 27, 81]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -2, -4, -8, -16, -32, -64, -128]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -2, -4, -8, -16, -32, -64, -128]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 2, -2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 2, -2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, -1, 2, -2, 4, -4, 8, -8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, -1, 2, -2, 4, -4, 8, -8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 3, 12, 24, 48, 96, 192, 384, 768, 1536, 3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 3, 12, 24, 48, 96, 192, 384, 768, 1536, 3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-3, -6, -12, -24, -48, -96, -192, -384, -768, -1536]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-3, -6, -12, -24, -48, -96, -192, -384, -768, -1536]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -2, -4, -8, 1, 2, 4, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -2, -4, -8, 1, 2, 4, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 12, 24, 48, 96, 192, 384]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 12, 24, 48, 96, 192, 384]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 9, 18, 27, 54]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 9, 18, 27, 54]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -2, -3, -6, -5, -10, -15, -30, -4, -8, -12, -24, -20, -40, -60, -120]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -2, -3, -6, -5, -10, -15, -30, -4, -8, -12, -24, -20, -40, -60, -120]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-10, 10, -20, 20, -30, 30, -40, 40, -50, 50]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-10, 10, -20, 20, -30, 30, -40, 40, -50, 50]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 2, 2, 4, 4, 8, 8, 16]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 2, 2, 4, 4, 8, 8, 16]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-5, 5, -10, 10, -20, 20, -40, 40, -80, 80]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-5, 5, -10, 10, -20, 20, -40, 40, -80, 80]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-5, -10, -20, -2, -4, -8, -1, -2, -4, -8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-5, -10, -20, -2, -4, -8, -1, -2, -4, -8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 5, 3, 6, 2, 4, 8, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 5, 3, 6, 2, 4, 8, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -2, -3, -6, -4, -8, -9, -18, -12, -24]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -2, -3, -6, -4, -8, -9, -18, -12, -24]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 4, 2, 1, 16, 32, 64, 128, 256, 512]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 4, 2, 1, 16, 32, 64, 128, 256, 512]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 4, 4, 4, 8, 8, 8, 8, 16, 16, 16, 16, 32, 32, 32, 32]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 4, 4, 4, 8, 8, 8, 8, 16, 16, 16, 16, 32, 32, 32, 32]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-2, 4, -8, 16, -32, 64, -128, 256]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-2, 4, -8, 16, -32, 64, -128, 256]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 8, 4, 16, 8, 32, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 8, 4, 16, 8, 32, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -3, -6, -12, -24, -48, -96, -192, -384, -768]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -3, -6, -12, -24, -48, -96, -192, -384, -768]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, 1, -2, 2, -3, 3, -4, 4, -6, 6, -12, 12, -24, 24, -48, 48]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, 1, -2, 2, -3, 3, -4, 4, -6, 6, -12, 12, -24, 24, -48, 48]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 1, 2, 18, 9, 36, 18]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 1, 2, 18, 9, 36, 18]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -18]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -18]) == False: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-1, -2, -3, -6, -3, -6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-1, -2, -3, -6, -3, -6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 30, 60, 120, 240, 480]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 30, 60, 120, 240, 480]) == True: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 6, 4, 12, 8, 24]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 6, 4, 12, 8, 24]) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [1, 4, 2, 2]) == True
    assert candidate(arr = [1, 2, 4, 16, 8, 4]) == False
    assert candidate(arr = [-5, -2, -10, -1, -1, -5]) == False
    assert candidate(arr = [5, -3, 3, -2, 2, -4]) == False
    assert candidate(arr = [0, 0]) == True
    assert candidate(arr = [4, -2, 2, -4]) == True
    assert candidate(arr = [1, 2, 3, 6, 4, 8]) == True
    assert candidate(arr = [1, 2, 4, 16, 8, 32]) == True
    assert candidate(arr = [1, 2, 2, 4]) == True
    assert candidate(arr = [2, 1, 2, 6]) == False
    assert candidate(arr = [0, 0, 0, 0]) == True
    assert candidate(arr = [-2, 4, -2, 4]) == False
    assert candidate(arr = [-1, -2, -3, -6, -6, -12]) == True
    assert candidate(arr = [-2, 4, -8, 16, -32, 64]) == False
    assert candidate(arr = [1, 2, 3, 6, 6, 12]) == True
    assert candidate(arr = [3, 1, 3, 6]) == False
    assert candidate(arr = [1, 2, 3, 6]) == True
    assert candidate(arr = [-1, -2, -2, -4]) == True
    assert candidate(arr = [1, 2, 4, 8]) == True
    assert candidate(arr = [1, 2, 2, 4, 4, 8]) == True
    assert candidate(arr = [1, 2, 3, 6, 5, 10, 15, 30, 4, 8, 12, 24, 20, 40, 60, 120]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 18]) == False
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 18, 15, 12, 6, 10]) == False
    assert candidate(arr = [1, 2, 3, 6, 5, 10, 15, 30, 4, 8, 12, 24, 20, 40, 60, 120, 7, 14, 21, 42]) == True
    assert candidate(arr = [5, 10, 10, 20, 25, 50]) == True
    assert candidate(arr = [7, 14, 28, 56, 112, 224, 448, 896, 1792, 3584]) == True
    assert candidate(arr = [5, 2, 1, 10, 5, 20, 2, 4]) == False
    assert candidate(arr = [1, 2, 2, 4, 4, 8, 8, 16]) == True
    assert candidate(arr = [-1, 1, -1, 1, -2, 2, -2, 2, -4, 4, -4, 4]) == False
    assert candidate(arr = [-8, -4, -2, -1, -16, -32, -2, -4]) == True
    assert candidate(arr = [-1, 2, -2, 4, -4, 8]) == False
    assert candidate(arr = [-1, -2, -3, -6, -5, -10, -15, -30, -4, -8, -12, -24, -20, -40, -60, -120, -7, -14, -21, -42]) == True
    assert candidate(arr = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == True
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == True
    assert candidate(arr = [3, 6, 3, 6, 12, 24]) == True
    assert candidate(arr = [1, 2, 4, 8, 16, 32]) == True
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128]) == True
    assert candidate(arr = [-1, 2, -2, 1, -4, 4]) == False
    assert candidate(arr = [100000, -100000, 50000, -50000, 25000, -25000, 12500, -12500]) == True
    assert candidate(arr = [5, 10, 15, 20, 25, 50]) == False
    assert candidate(arr = [100000, -100000, 50000, -50000, 25000, -25000]) == False
    assert candidate(arr = [-100000, 100000, -50000, 50000, -25000, 25000, -12500, 12500]) == True
    assert candidate(arr = [-1, 3, 6, 12, 24, 48, 96, 192, 384, 768]) == False
    assert candidate(arr = [-2, -4, -8, -16, -32, -64, -128, -256]) == True
    assert candidate(arr = [5, -5, 10, -10, 20, -20, 40, -40]) == True
    assert candidate(arr = [-5, -10, -15, -20, -25, -50]) == False
    assert candidate(arr = [-2, 4, 1, -1, 2, -2, -4, 8]) == True
    assert candidate(arr = [1, 3, 6, 12, 24, 48, 96, 192, 384, 768]) == False
    assert candidate(arr = [100000, -100000, 50000, -50000, 25000, -25000, 12500, -12500, 6250, -6250]) == False
    assert candidate(arr = [0, 0, 0, 0, 0, 0]) == True
    assert candidate(arr = [1, 2, 3, 4, 6, 8, 12, 16, 24, 32]) == True
    assert candidate(arr = [10, 20, 20, 40, 80, 160, 320, 640]) == True
    assert candidate(arr = [1, 4, 2, 8, 4, 2]) == True
    assert candidate(arr = [1, 3, 5, 7, 2, 6, 10, 14, 4, 12]) == False
    assert candidate(arr = [-3, 3, -6, 6, -12, 12, -24, 24]) == True
    assert candidate(arr = [100000, -100000, 50000, -50000, 25000, -25000, 12500, -12500, 6250, -6250, 3125, -3125, 15625, -15625, 78125, -78125]) == False
    assert candidate(arr = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144]) == True
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == True
    assert candidate(arr = [5, 10, 15, 20, 25, 50, 100, 150, 200, 250]) == False
    assert candidate(arr = [10, 5, 5, 15, 20, 10]) == False
    assert candidate(arr = [1, 2, 3, 6, 4, 8, 9, 18, 12, 24]) == True
    assert candidate(arr = [-4, -8, -2, -1, -16, -2]) == True
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 6, 6, 12, 12]) == False
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 10, 20, 30, 40, 50, 60]) == False
    assert candidate(arr = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32]) == True
    assert candidate(arr = [5, 10, 5, 20, 10, 40, 20, 80]) == False
    assert candidate(arr = [1, 3, 3, 6, 9, 18, 27, 54]) == False
    assert candidate(arr = [-1, -2, -4, -8, -16, -32, -64, -128, -256, -512, -1024, -2048]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10, 20]) == False
    assert candidate(arr = [3, 6, 1, 2, 18, 9, 27, 54]) == True
    assert candidate(arr = [6, 3, 3, 12, 2, 4]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 40, 5, 15, 30, 60]) == False
    assert candidate(arr = [1, 1, 2, 2, 4, 4, 8, 8]) == True
    assert candidate(arr = [1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64]) == True
    assert candidate(arr = [1, 3, 2, 6, 4, 8, 5, 10, 7, 14, 9, 18, 11, 22, 12, 24]) == True
    assert candidate(arr = [-1, 1, -2, 2, -4, 4, -8, 8]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 4, 8, 16, 32, 64]) == False
    assert candidate(arr = [-1, 2, -2, 1, -4, 4, -8, 8, 16, -16]) == False
    assert candidate(arr = [3, 9, 1, 27, 3, 9, 27, 81]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == True
    assert candidate(arr = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16]) == False
    assert candidate(arr = [-1, -2, -4, -8, -16, -32, -64, -128]) == True
    assert candidate(arr = [-1, 2, -2, 1]) == True
    assert candidate(arr = [1, -1, 2, -2, 4, -4, 8, -8]) == True
    assert candidate(arr = [6, 3, 12, 24, 48, 96, 192, 384, 768, 1536, 3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]) == True
    assert candidate(arr = [-3, -6, -12, -24, -48, -96, -192, -384, -768, -1536]) == True
    assert candidate(arr = [-1, -2, -4, -8, 1, 2, 4, 8]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(arr = [3, 6, 12, 24, 48, 96, 192, 384]) == True
    assert candidate(arr = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128]) == True
    assert candidate(arr = [3, 6, 9, 18, 27, 54]) == True
    assert candidate(arr = [-1, -2, -3, -6, -5, -10, -15, -30, -4, -8, -12, -24, -20, -40, -60, -120]) == True
    assert candidate(arr = [-10, 10, -20, 20, -30, 30, -40, 40, -50, 50]) == False
    assert candidate(arr = [1, 1, 1, 2, 2, 4, 4, 8, 8, 16]) == False
    assert candidate(arr = [-5, 5, -10, 10, -20, 20, -40, 40, -80, 80]) == False
    assert candidate(arr = [-5, -10, -20, -2, -4, -8, -1, -2, -4, -8]) == False
    assert candidate(arr = [10, 5, 3, 6, 2, 4, 8, 1]) == True
    assert candidate(arr = [-1, -2, -3, -6, -4, -8, -9, -18, -12, -24]) == True
    assert candidate(arr = [8, 4, 2, 1, 16, 32, 64, 128, 256, 512]) == True
    assert candidate(arr = [1, 2, 2, 4, 4, 4, 8, 8, 8, 8, 16, 16, 16, 16, 32, 32, 32, 32]) == False
    assert candidate(arr = [-2, 4, -8, 16, -32, 64, -128, 256]) == False
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == False
    assert candidate(arr = [4, 8, 4, 16, 8, 32, 2, 1]) == True
    assert candidate(arr = [-1, -3, -6, -12, -24, -48, -96, -192, -384, -768]) == False
    assert candidate(arr = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]) == True
    assert candidate(arr = [-1, 1, -2, 2, -3, 3, -4, 4, -6, 6, -12, 12, -24, 24, -48, 48]) == False
    assert candidate(arr = [3, 6, 1, 2, 18, 9, 36, 18]) == True
    assert candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -18]) == False
    assert candidate(arr = [-1, -2, -3, -6, -3, -6]) == True
    assert candidate(arr = [5, 10, 15, 30, 60, 120, 240, 480]) == True
    assert candidate(arr = [1, 3, 2, 6, 4, 12, 8, 24]) == True


