def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(mass = 1,asteroids = [100000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 1,asteroids = [100000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(mass = 1,asteroids = [1, 2, 3, 4, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 1,asteroids = [1, 2, 3, 4, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 5,asteroids = [4, 9, 23, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 5,asteroids = [4, 9, 23, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(mass = 10,asteroids = [10, 10, 10, 10, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 10,asteroids = [10, 10, 10, 10, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 20,asteroids = [10, 10, 10, 10, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 20,asteroids = [10, 10, 10, 10, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 10,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 10,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 100000,asteroids = [100000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 100000,asteroids = [100000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 10,asteroids = [5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 10,asteroids = [5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 1,asteroids = [1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 1,asteroids = [1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 1,asteroids = [1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 1,asteroids = [1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 10,asteroids = [3, 9, 19, 5, 21]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 10,asteroids = [3, 9, 19, 5, 21]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 1,asteroids = [2, 2, 2, 2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 1,asteroids = [2, 2, 2, 2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(mass = 100,asteroids = [10, 20, 30, 40, 50]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 100,asteroids = [10, 20, 30, 40, 50]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 25,asteroids = [5, 10, 15]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 25,asteroids = [5, 10, 15]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 6,asteroids = [1, 2, 3, 4, 5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 6,asteroids = [1, 2, 3, 4, 5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 30,asteroids = [15, 15, 15, 15, 15]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 30,asteroids = [15, 15, 15, 15, 15]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 100,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 100,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 1000,asteroids = [500, 250, 125, 62, 31, 15, 7, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 1000,asteroids = [500, 250, 125, 62, 31, 15, 7, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 20,asteroids = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 20,asteroids = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 50,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 50,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]) == False: {e}')
    
    total += 1
    try:
        result = candidate(mass = 25,asteroids = [10, 20, 5, 15, 25, 30, 5, 10, 20, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 25,asteroids = [10, 20, 5, 15, 25, 30, 5, 10, 20, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 500,asteroids = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 500,asteroids = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 30,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 30,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 100,asteroids = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 100,asteroids = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 1,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 1,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(mass = 25,asteroids = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 25,asteroids = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 150,asteroids = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 150,asteroids = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 10,asteroids = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 10,asteroids = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 300,asteroids = [250, 200, 150, 100, 50, 300]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 300,asteroids = [250, 200, 150, 100, 50, 300]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 100,asteroids = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 100,asteroids = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 100,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 100,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 9,asteroids = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 9,asteroids = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 50,asteroids = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 50,asteroids = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 25,asteroids = [20, 10, 5, 15, 25, 30, 35, 40, 45, 50]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 25,asteroids = [20, 10, 5, 15, 25, 30, 35, 40, 45, 50]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 1000,asteroids = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 1000,asteroids = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 1,asteroids = [100000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 1,asteroids = [100000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(mass = 1000,asteroids = [900, 800, 700, 600, 500, 400, 300, 200, 100, 50, 25, 10, 5, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 1000,asteroids = [900, 800, 700, 600, 500, 400, 300, 200, 100, 50, 25, 10, 5, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 1,asteroids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 1,asteroids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 1000,asteroids = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 1000,asteroids = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 200,asteroids = [100, 50, 150, 75, 25, 125, 225, 175, 200, 130]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 200,asteroids = [100, 50, 150, 75, 25, 125, 225, 175, 200, 130]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 75,asteroids = [50, 25, 12, 6, 3, 1, 50, 25, 12, 6, 3, 1, 50, 25, 12, 6, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 75,asteroids = [50, 25, 12, 6, 3, 1, 50, 25, 12, 6, 3, 1, 50, 25, 12, 6, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 1,asteroids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 1,asteroids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 5,asteroids = [3, 7, 2, 8, 6, 4, 10, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 5,asteroids = [3, 7, 2, 8, 6, 4, 10, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 15,asteroids = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 15,asteroids = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 5,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 5,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 20,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 20,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 10,asteroids = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 10,asteroids = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 5,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 5,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 30,asteroids = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 30,asteroids = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 25,asteroids = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 25,asteroids = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 75,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 75,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 25,asteroids = [20, 15, 10, 5, 30, 25, 35, 40, 45, 50]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 25,asteroids = [20, 15, 10, 5, 30, 25, 35, 40, 45, 50]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 1,asteroids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 1,asteroids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 10,asteroids = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 10,asteroids = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == False: {e}')
    
    total += 1
    try:
        result = candidate(mass = 10,asteroids = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 10,asteroids = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 50,asteroids = [100, 50, 25, 12, 6, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 50,asteroids = [100, 50, 25, 12, 6, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 200,asteroids = [100, 150, 50, 200, 250, 300, 350, 400, 450, 500]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 200,asteroids = [100, 150, 50, 200, 250, 300, 350, 400, 450, 500]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 10,asteroids = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 10,asteroids = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 1,asteroids = [2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 1,asteroids = [2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 1,asteroids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 1,asteroids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 50,asteroids = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 50,asteroids = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 50000,asteroids = [10000, 20000, 15000, 5000, 25000, 30000, 40000, 60000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 50000,asteroids = [10000, 20000, 15000, 5000, 25000, 30000, 40000, 60000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 500,asteroids = [100, 200, 150, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 500,asteroids = [100, 200, 150, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 5,asteroids = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 5,asteroids = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 50,asteroids = [100, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 50,asteroids = [100, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 100,asteroids = [20, 30, 50, 10, 40, 60, 70]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 100,asteroids = [20, 30, 50, 10, 40, 60, 70]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 10000,asteroids = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 10000,asteroids = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 100,asteroids = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 100,asteroids = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 100,asteroids = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 100,asteroids = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 100,asteroids = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 100,asteroids = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 50,asteroids = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 50,asteroids = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 5,asteroids = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 5,asteroids = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 50000,asteroids = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 50000,asteroids = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 20,asteroids = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 20,asteroids = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 15,asteroids = [20, 25, 30, 5, 10, 15, 35, 40]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 15,asteroids = [20, 25, 30, 5, 10, 15, 35, 40]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 10,asteroids = [1, 100000, 2, 99999, 3, 99998, 4, 99997]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 10,asteroids = [1, 100000, 2, 99999, 3, 99998, 4, 99997]) == False: {e}')
    
    total += 1
    try:
        result = candidate(mass = 15,asteroids = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 15,asteroids = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 120,asteroids = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 120,asteroids = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 50,asteroids = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 50,asteroids = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 15,asteroids = [10, 5, 15, 20, 25, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 15,asteroids = [10, 5, 15, 20, 25, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 25,asteroids = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 25,asteroids = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 100000,asteroids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 100000,asteroids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 50,asteroids = [10, 20, 30, 40, 50]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 50,asteroids = [10, 20, 30, 40, 50]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 100,asteroids = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 100,asteroids = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 15,asteroids = [1, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 15,asteroids = [1, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 25,asteroids = [24, 23, 22, 21, 20, 19, 18, 17, 16, 15]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 25,asteroids = [24, 23, 22, 21, 20, 19, 18, 17, 16, 15]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 5,asteroids = [1, 3, 2, 4, 6, 8, 7, 5, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 5,asteroids = [1, 3, 2, 4, 6, 8, 7, 5, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(mass = 20,asteroids = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mass = 20,asteroids = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(mass = 1,asteroids = [100000]) == False
    assert candidate(mass = 1,asteroids = [1, 2, 3, 4, 5]) == True
    assert candidate(mass = 5,asteroids = [4, 9, 23, 4]) == False
    assert candidate(mass = 10,asteroids = [10, 10, 10, 10, 10]) == True
    assert candidate(mass = 20,asteroids = [10, 10, 10, 10, 10]) == True
    assert candidate(mass = 10,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(mass = 100000,asteroids = [100000]) == True
    assert candidate(mass = 10,asteroids = [5, 5, 5, 5, 5]) == True
    assert candidate(mass = 1,asteroids = [1, 1, 1, 1, 1]) == True
    assert candidate(mass = 1,asteroids = [1, 1, 1, 1]) == True
    assert candidate(mass = 10,asteroids = [3, 9, 19, 5, 21]) == True
    assert candidate(mass = 1,asteroids = [2, 2, 2, 2, 2]) == False
    assert candidate(mass = 100,asteroids = [10, 20, 30, 40, 50]) == True
    assert candidate(mass = 25,asteroids = [5, 10, 15]) == True
    assert candidate(mass = 6,asteroids = [1, 2, 3, 4, 5, 6]) == True
    assert candidate(mass = 30,asteroids = [15, 15, 15, 15, 15]) == True
    assert candidate(mass = 100,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(mass = 1000,asteroids = [500, 250, 125, 62, 31, 15, 7, 3, 1]) == True
    assert candidate(mass = 20,asteroids = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(mass = 50,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]) == False
    assert candidate(mass = 25,asteroids = [10, 20, 5, 15, 25, 30, 5, 10, 20, 5]) == True
    assert candidate(mass = 500,asteroids = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == True
    assert candidate(mass = 30,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == True
    assert candidate(mass = 100,asteroids = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == True
    assert candidate(mass = 1,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100000]) == False
    assert candidate(mass = 25,asteroids = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == True
    assert candidate(mass = 150,asteroids = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == True
    assert candidate(mass = 10,asteroids = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == True
    assert candidate(mass = 300,asteroids = [250, 200, 150, 100, 50, 300]) == True
    assert candidate(mass = 100,asteroids = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == True
    assert candidate(mass = 100,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
    assert candidate(mass = 9,asteroids = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(mass = 50,asteroids = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == True
    assert candidate(mass = 25,asteroids = [20, 10, 5, 15, 25, 30, 35, 40, 45, 50]) == True
    assert candidate(mass = 1000,asteroids = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == True
    assert candidate(mass = 1,asteroids = [100000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
    assert candidate(mass = 1000,asteroids = [900, 800, 700, 600, 500, 400, 300, 200, 100, 50, 25, 10, 5, 1]) == True
    assert candidate(mass = 1,asteroids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(mass = 1000,asteroids = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == True
    assert candidate(mass = 200,asteroids = [100, 50, 150, 75, 25, 125, 225, 175, 200, 130]) == True
    assert candidate(mass = 75,asteroids = [50, 25, 12, 6, 3, 1, 50, 25, 12, 6, 3, 1, 50, 25, 12, 6, 3, 1]) == True
    assert candidate(mass = 1,asteroids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(mass = 5,asteroids = [3, 7, 2, 8, 6, 4, 10, 1]) == True
    assert candidate(mass = 15,asteroids = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(mass = 5,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
    assert candidate(mass = 20,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
    assert candidate(mass = 10,asteroids = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == True
    assert candidate(mass = 5,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
    assert candidate(mass = 30,asteroids = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20]) == True
    assert candidate(mass = 25,asteroids = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == True
    assert candidate(mass = 75,asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
    assert candidate(mass = 25,asteroids = [20, 15, 10, 5, 30, 25, 35, 40, 45, 50]) == True
    assert candidate(mass = 1,asteroids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(mass = 10,asteroids = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == False
    assert candidate(mass = 10,asteroids = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == True
    assert candidate(mass = 50,asteroids = [100, 50, 25, 12, 6, 3, 1]) == True
    assert candidate(mass = 200,asteroids = [100, 150, 50, 200, 250, 300, 350, 400, 450, 500]) == True
    assert candidate(mass = 10,asteroids = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1]) == True
    assert candidate(mass = 1,asteroids = [2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == True
    assert candidate(mass = 1,asteroids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(mass = 50,asteroids = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True
    assert candidate(mass = 50000,asteroids = [10000, 20000, 15000, 5000, 25000, 30000, 40000, 60000]) == True
    assert candidate(mass = 500,asteroids = [100, 200, 150, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]) == True
    assert candidate(mass = 5,asteroids = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(mass = 50,asteroids = [100, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == True
    assert candidate(mass = 100,asteroids = [20, 30, 50, 10, 40, 60, 70]) == True
    assert candidate(mass = 10000,asteroids = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990]) == True
    assert candidate(mass = 100,asteroids = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(mass = 100,asteroids = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True
    assert candidate(mass = 100,asteroids = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True
    assert candidate(mass = 50,asteroids = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == True
    assert candidate(mass = 5,asteroids = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(mass = 50000,asteroids = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == True
    assert candidate(mass = 20,asteroids = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20]) == True
    assert candidate(mass = 15,asteroids = [20, 25, 30, 5, 10, 15, 35, 40]) == True
    assert candidate(mass = 10,asteroids = [1, 100000, 2, 99999, 3, 99998, 4, 99997]) == False
    assert candidate(mass = 15,asteroids = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(mass = 120,asteroids = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == True
    assert candidate(mass = 50,asteroids = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == True
    assert candidate(mass = 15,asteroids = [10, 5, 15, 20, 25, 5]) == True
    assert candidate(mass = 25,asteroids = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == True
    assert candidate(mass = 100000,asteroids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(mass = 50,asteroids = [10, 20, 30, 40, 50]) == True
    assert candidate(mass = 100,asteroids = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]) == True
    assert candidate(mass = 15,asteroids = [1, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
    assert candidate(mass = 25,asteroids = [24, 23, 22, 21, 20, 19, 18, 17, 16, 15]) == True
    assert candidate(mass = 5,asteroids = [1, 3, 2, 4, 6, 8, 7, 5, 9, 10]) == True
    assert candidate(mass = 20,asteroids = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == True


