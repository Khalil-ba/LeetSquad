def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(piles = [15, 30, 5, 10, 20, 25]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [15, 30, 5, 10, 20, 25]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [8, 15, 3, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [8, 15, 3, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [7, 3, 8, 5, 12, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [7, 3, 8, 5, 12, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 100, 1, 100, 1, 100, 1, 100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 100, 1, 100, 1, 100, 1, 100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [2, 2, 2, 2, 2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [2, 2, 2, 2, 2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 20, 30, 40, 50, 60]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 20, 30, 40, 50, 60]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [8, 6, 5, 1, 7, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [8, 6, 5, 1, 7, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 20, 30, 40]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 20, 30, 40]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 5, 2, 4, 6, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 5, 2, 4, 6, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [2, 2, 2, 2, 2, 2, 2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [2, 2, 2, 2, 2, 2, 2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 6, 9, 12, 15, 18]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 6, 9, 12, 15, 18]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [8, 9, 7, 6, 5, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [8, 9, 7, 6, 5, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 3, 5, 7, 9, 11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 3, 5, 7, 9, 11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 5, 1, 2, 3, 7, 4, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 5, 1, 2, 3, 7, 4, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4, 5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4, 5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 100, 1, 100, 1, 100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 100, 1, 100, 1, 100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [4, 3, 2, 1, 6, 5, 8, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [4, 3, 2, 1, 6, 5, 8, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [7, 2, 5, 10, 14, 3, 1, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [7, 2, 5, 10, 14, 3, 1, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [8, 9, 7, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [8, 9, 7, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 100, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 100, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [4, 1, 5, 2, 6, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [4, 1, 5, 2, 6, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 5, 4, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 5, 4, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 3, 4, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 3, 4, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [100, 100, 100, 100, 100, 100]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [100, 100, 100, 100, 100, 100]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [2, 4, 6, 8, 10, 12]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [2, 4, 6, 8, 10, 12]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 3, 3, 3, 3, 3, 3, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 3, 3, 3, 3, 3, 3, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 7, 2, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 7, 2, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [100, 1, 100, 1, 100, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [100, 1, 100, 1, 100, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [7, 9, 8, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [7, 9, 8, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [29, 18, 17, 26, 34, 15, 45, 13, 50, 25, 30, 10, 35, 40, 5, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [29, 18, 17, 26, 34, 15, 45, 13, 50, 25, 30, 10, 35, 40, 5, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 1, 100, 4, 10, 8, 6, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 1, 100, 4, 10, 8, 6, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 23, 5, 2, 7, 8, 3, 12, 15, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 23, 5, 2, 7, 8, 3, 12, 15, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 100, 2, 99, 3, 98, 4, 97]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 100, 2, 99, 3, 98, 4, 97]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [8, 15, 3, 7, 6, 9, 5, 10, 4, 12, 11, 14, 2, 13]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [8, 15, 3, 7, 6, 9, 5, 10, 4, 12, 11, 14, 2, 13]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [100, 50, 200, 150, 300, 250, 400, 350, 500, 450]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [100, 50, 200, 150, 300, 250, 400, 350, 500, 450]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [150, 120, 180, 160, 200, 140, 220, 190, 210, 170]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [150, 120, 180, 160, 200, 140, 220, 190, 210, 170]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [50, 100, 75, 25, 120, 150, 80, 60]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [50, 100, 75, 25, 120, 150, 80, 60]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [200, 100, 150, 50, 250, 125, 300, 150, 350, 175, 400, 200, 450, 225, 500, 250]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [200, 100, 150, 50, 250, 125, 300, 150, 350, 175, 400, 200, 450, 225, 500, 250]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [123, 456, 789, 101, 202, 303, 404, 505]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [123, 456, 789, 101, 202, 303, 404, 505]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [12, 34, 56, 78, 90, 23, 45, 67, 89, 101, 123, 145]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [12, 34, 56, 78, 90, 23, 45, 67, 89, 101, 123, 145]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [15, 23, 12, 18, 35, 10, 42, 8, 20, 14]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [15, 23, 12, 18, 35, 10, 42, 8, 20, 14]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 15, 3, 7, 8, 2, 1, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 15, 3, 7, 8, 2, 1, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [8, 9, 5, 7, 2, 3, 4, 6, 1, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [8, 9, 5, 7, 2, 3, 4, 6, 1, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [2, 8, 4, 6, 10, 14, 12, 16, 18, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [2, 8, 4, 6, 10, 14, 12, 16, 18, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5, 994, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5, 994, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [17, 23, 42, 35, 29, 49, 31, 47, 53, 41]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [17, 23, 42, 35, 29, 49, 31, 47, 53, 41]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [23, 45, 12, 34, 56, 78, 90, 12, 34, 56]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [23, 45, 12, 34, 56, 78, 90, 12, 34, 56]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [200, 300, 100, 400, 50, 600, 150, 700, 200, 800, 250, 900, 300, 1000, 350, 1100, 400, 1200, 450, 1300]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [200, 300, 100, 400, 50, 600, 150, 700, 200, 800, 250, 900, 300, 1000, 350, 1100, 400, 1200, 450, 1300]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 1, 2, 5, 4, 6, 9, 7, 8, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 1, 2, 5, 4, 6, 9, 7, 8, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [55, 65, 25, 30, 40, 50, 15, 20, 35, 45]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [55, 65, 25, 30, 40, 50, 15, 20, 35, 45]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [45, 55, 65, 75, 85, 95, 105, 115, 125, 135]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [45, 55, 65, 75, 85, 95, 105, 115, 125, 135]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [500, 1, 500, 1, 500, 1, 500, 1, 500, 1, 500, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [500, 1, 500, 1, 500, 1, 500, 1, 500, 1, 500, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 2, 1, 6, 5, 4, 9, 8, 7, 12, 11, 10, 15, 14, 13, 18, 17, 16, 21, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 2, 1, 6, 5, 4, 9, 8, 7, 12, 11, 10, 15, 14, 13, 18, 17, 16, 21, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [300, 200, 100, 50, 400, 350, 150, 250, 600, 550, 450, 100, 300, 200, 700, 650]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [300, 200, 100, 50, 400, 350, 150, 250, 600, 550, 450, 100, 300, 200, 700, 650]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [400, 10, 300, 20, 200, 30, 100, 40, 150, 50, 250, 60, 500, 5, 1, 800, 350, 450, 15, 25]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [400, 10, 300, 20, 200, 30, 100, 40, 150, 50, 250, 60, 500, 5, 1, 800, 350, 450, 15, 25]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [45, 22, 33, 11, 55, 66, 77, 88, 99, 111, 222, 333]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [45, 22, 33, 11, 55, 66, 77, 88, 99, 111, 222, 333]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [48, 32, 15, 22, 39, 28, 33, 27, 19, 25]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [48, 32, 15, 22, 39, 28, 33, 27, 19, 25]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 23, 15, 70, 6, 18, 40, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 23, 15, 70, 6, 18, 40, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [150, 200, 50, 100, 350, 400, 150, 200, 50, 100, 350, 400, 150, 200, 50, 100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [150, 200, 50, 100, 350, 400, 150, 200, 50, 100, 350, 400, 150, 200, 50, 100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [500, 1, 500, 1, 500, 1, 500, 1, 500, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [500, 1, 500, 1, 500, 1, 500, 1, 500, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [500, 1, 500, 2, 500, 3, 500, 4, 500, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [500, 1, 500, 2, 500, 3, 500, 4, 500, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [9, 3, 15, 2, 11, 8, 6, 10, 5, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [9, 3, 15, 2, 11, 8, 6, 10, 5, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [500, 1, 500, 1, 500, 1, 500, 1, 500, 1, 500, 1, 500, 1, 500, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [500, 1, 500, 1, 500, 1, 500, 1, 500, 1, 500, 1, 500, 1, 500, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 2, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 2, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [23, 34, 56, 45, 78, 89, 12, 11, 22, 33, 44, 55]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [23, 34, 56, 45, 78, 89, 12, 11, 22, 33, 44, 55]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [250, 100, 300, 200, 400, 150, 350, 25]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [250, 100, 300, 200, 400, 150, 350, 25]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 1, 9, 4, 8, 2, 7, 3, 6, 11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 1, 9, 4, 8, 2, 7, 3, 6, 11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 20, 19, 18, 17, 16, 15, 14, 13]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 20, 19, 18, 17, 16, 15, 14, 13]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [150, 100, 50, 200, 25, 300, 75, 175, 125, 120, 60, 180, 220, 30, 240, 80]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [150, 100, 50, 200, 25, 300, 75, 175, 125, 120, 60, 180, 220, 30, 240, 80]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [100, 200, 101, 201, 102, 202, 103, 203, 104, 204]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [100, 200, 101, 201, 102, 202, 103, 203, 104, 204]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 8, 6, 3, 4, 2, 7, 9, 1, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 8, 6, 3, 4, 2, 7, 9, 1, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [20, 40, 30, 60, 50, 70, 80, 100, 90, 110]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [20, 40, 30, 60, 50, 70, 80, 100, 90, 110]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [8, 15, 3, 7, 12, 9, 6, 11, 2, 10, 5, 14]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [8, 15, 3, 7, 12, 9, 6, 11, 2, 10, 5, 14]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [250, 100, 300, 50, 400, 150, 600, 200, 700, 50, 800, 25]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [250, 100, 300, 50, 400, 150, 600, 200, 700, 50, 800, 25]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 3, 2, 4, 5, 7, 6, 8, 9, 11, 10, 12, 13, 15, 14, 16, 17, 19, 18, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 3, 2, 4, 5, 7, 6, 8, 9, 11, 10, 12, 13, 15, 14, 16, 17, 19, 18, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 8, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 8, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [42, 33, 24, 15, 6, 17, 28, 39, 50, 61, 72, 83]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [42, 33, 24, 15, 6, 17, 28, 39, 50, 61, 72, 83]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [12, 22, 32, 42, 52, 62, 72, 82, 92, 102]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [12, 22, 32, 42, 52, 62, 72, 82, 92, 102]) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(piles = [15, 30, 5, 10, 20, 25]) == True
    assert candidate(piles = [8, 15, 3, 7]) == True
    assert candidate(piles = [7, 3, 8, 5, 12, 10]) == True
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8]) == True
    assert candidate(piles = [1, 100, 1, 100, 1, 100, 1, 100]) == True
    assert candidate(piles = [2, 2, 2, 2, 2, 2]) == False
    assert candidate(piles = [10, 20, 30, 40, 50, 60]) == True
    assert candidate(piles = [8, 6, 5, 1, 7, 9]) == True
    assert candidate(piles = [10, 20, 30, 40]) == True
    assert candidate(piles = [1, 5, 2, 4, 6, 3]) == True
    assert candidate(piles = [1, 2, 3, 4]) == True
    assert candidate(piles = [2, 2, 2, 2, 2, 2, 2, 2]) == False
    assert candidate(piles = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
    assert candidate(piles = [3, 6, 9, 12, 15, 18]) == True
    assert candidate(piles = [8, 9, 7, 6, 5, 4]) == True
    assert candidate(piles = [1, 3, 5, 7, 9, 11]) == True
    assert candidate(piles = [10, 5, 1, 2, 3, 7, 4, 8]) == True
    assert candidate(piles = [1, 2, 3, 4, 5, 6]) == True
    assert candidate(piles = [1, 100, 1, 100, 1, 100]) == True
    assert candidate(piles = [4, 3, 2, 1, 6, 5, 8, 7]) == True
    assert candidate(piles = [7, 2, 5, 10, 14, 3, 1, 2]) == True
    assert candidate(piles = [8, 9, 7, 6]) == False
    assert candidate(piles = [1, 2, 100, 3]) == True
    assert candidate(piles = [4, 1, 5, 2, 6, 3]) == True
    assert candidate(piles = [1, 2, 3, 5, 4, 6]) == True
    assert candidate(piles = [5, 3, 4, 5]) == True
    assert candidate(piles = [100, 100, 100, 100, 100, 100]) == False
    assert candidate(piles = [2, 4, 6, 8, 10, 12]) == True
    assert candidate(piles = [3, 3, 3, 3, 3, 3, 3, 3]) == False
    assert candidate(piles = [3, 7, 2, 3]) == True
    assert candidate(piles = [100, 1, 100, 1, 100, 1]) == True
    assert candidate(piles = [7, 9, 8, 6]) == False
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(piles = [29, 18, 17, 26, 34, 15, 45, 13, 50, 25, 30, 10, 35, 40, 5, 20]) == True
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
    assert candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == True
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]) == True
    assert candidate(piles = [5, 1, 100, 4, 10, 8, 6, 2]) == True
    assert candidate(piles = [10, 23, 5, 2, 7, 8, 3, 12, 15, 6]) == True
    assert candidate(piles = [1, 100, 2, 99, 3, 98, 4, 97]) == True
    assert candidate(piles = [8, 15, 3, 7, 6, 9, 5, 10, 4, 12, 11, 14, 2, 13]) == True
    assert candidate(piles = [100, 50, 200, 150, 300, 250, 400, 350, 500, 450]) == True
    assert candidate(piles = [150, 120, 180, 160, 200, 140, 220, 190, 210, 170]) == True
    assert candidate(piles = [50, 100, 75, 25, 120, 150, 80, 60]) == True
    assert candidate(piles = [200, 100, 150, 50, 250, 125, 300, 150, 350, 175, 400, 200, 450, 225, 500, 250]) == True
    assert candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == True
    assert candidate(piles = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == True
    assert candidate(piles = [123, 456, 789, 101, 202, 303, 404, 505]) == True
    assert candidate(piles = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]) == True
    assert candidate(piles = [12, 34, 56, 78, 90, 23, 45, 67, 89, 101, 123, 145]) == True
    assert candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == True
    assert candidate(piles = [15, 23, 12, 18, 35, 10, 42, 8, 20, 14]) == True
    assert candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True
    assert candidate(piles = [10, 15, 3, 7, 8, 2, 1, 5]) == True
    assert candidate(piles = [8, 9, 5, 7, 2, 3, 4, 6, 1, 10]) == True
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == True
    assert candidate(piles = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14]) == True
    assert candidate(piles = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 15, 14, 13, 12, 11, 20, 19, 18, 17, 16]) == True
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
    assert candidate(piles = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == True
    assert candidate(piles = [2, 8, 4, 6, 10, 14, 12, 16, 18, 20]) == True
    assert candidate(piles = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000]) == True
    assert candidate(piles = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5, 994, 6]) == True
    assert candidate(piles = [17, 23, 42, 35, 29, 49, 31, 47, 53, 41]) == True
    assert candidate(piles = [23, 45, 12, 34, 56, 78, 90, 12, 34, 56]) == True
    assert candidate(piles = [200, 300, 100, 400, 50, 600, 150, 700, 200, 800, 250, 900, 300, 1000, 350, 1100, 400, 1200, 450, 1300]) == True
    assert candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == True
    assert candidate(piles = [8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == True
    assert candidate(piles = [3, 1, 2, 5, 4, 6, 9, 7, 8, 10]) == True
    assert candidate(piles = [55, 65, 25, 30, 40, 50, 15, 20, 35, 45]) == True
    assert candidate(piles = [45, 55, 65, 75, 85, 95, 105, 115, 125, 135]) == True
    assert candidate(piles = [500, 1, 500, 1, 500, 1, 500, 1, 500, 1, 500, 1]) == True
    assert candidate(piles = [3, 2, 1, 6, 5, 4, 9, 8, 7, 12, 11, 10, 15, 14, 13, 18, 17, 16, 21, 20]) == True
    assert candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == True
    assert candidate(piles = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == True
    assert candidate(piles = [300, 200, 100, 50, 400, 350, 150, 250, 600, 550, 450, 100, 300, 200, 700, 650]) == True
    assert candidate(piles = [400, 10, 300, 20, 200, 30, 100, 40, 150, 50, 250, 60, 500, 5, 1, 800, 350, 450, 15, 25]) == True
    assert candidate(piles = [45, 22, 33, 11, 55, 66, 77, 88, 99, 111, 222, 333]) == True
    assert candidate(piles = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == True
    assert candidate(piles = [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250]) == False
    assert candidate(piles = [48, 32, 15, 22, 39, 28, 33, 27, 19, 25]) == True
    assert candidate(piles = [150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150]) == False
    assert candidate(piles = [10, 23, 15, 70, 6, 18, 40, 5]) == True
    assert candidate(piles = [150, 200, 50, 100, 350, 400, 150, 200, 50, 100, 350, 400, 150, 200, 50, 100]) == True
    assert candidate(piles = [500, 1, 500, 1, 500, 1, 500, 1, 500, 1]) == True
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == True
    assert candidate(piles = [500, 1, 500, 2, 500, 3, 500, 4, 500, 5]) == True
    assert candidate(piles = [9, 3, 15, 2, 11, 8, 6, 10, 5, 4]) == True
    assert candidate(piles = [500, 1, 500, 1, 500, 1, 500, 1, 500, 1, 500, 1, 500, 1, 500, 1]) == True
    assert candidate(piles = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == True
    assert candidate(piles = [10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100]) == True
    assert candidate(piles = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == True
    assert candidate(piles = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]) == True
    assert candidate(piles = [3, 2, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
    assert candidate(piles = [23, 34, 56, 45, 78, 89, 12, 11, 22, 33, 44, 55]) == True
    assert candidate(piles = [250, 100, 300, 200, 400, 150, 350, 25]) == True
    assert candidate(piles = [5, 1, 9, 4, 8, 2, 7, 3, 6, 11]) == True
    assert candidate(piles = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
    assert candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80]) == True
    assert candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 20, 19, 18, 17, 16, 15, 14, 13]) == True
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == True
    assert candidate(piles = [150, 100, 50, 200, 25, 300, 75, 175, 125, 120, 60, 180, 220, 30, 240, 80]) == True
    assert candidate(piles = [100, 200, 101, 201, 102, 202, 103, 203, 104, 204]) == True
    assert candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16]) == True
    assert candidate(piles = [5, 8, 6, 3, 4, 2, 7, 9, 1, 10]) == True
    assert candidate(piles = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == True
    assert candidate(piles = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996]) == True
    assert candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
    assert candidate(piles = [20, 40, 30, 60, 50, 70, 80, 100, 90, 110]) == True
    assert candidate(piles = [8, 15, 3, 7, 12, 9, 6, 11, 2, 10, 5, 14]) == True
    assert candidate(piles = [250, 100, 300, 50, 400, 150, 600, 200, 700, 50, 800, 25]) == True
    assert candidate(piles = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]) == False
    assert candidate(piles = [1, 3, 2, 4, 5, 7, 6, 8, 9, 11, 10, 12, 13, 15, 14, 16, 17, 19, 18, 20]) == True
    assert candidate(piles = [5, 8, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == True
    assert candidate(piles = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == True
    assert candidate(piles = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14]) == True
    assert candidate(piles = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert candidate(piles = [42, 33, 24, 15, 6, 17, 28, 39, 50, 61, 72, 83]) == True
    assert candidate(piles = [12, 22, 32, 42, 52, 62, 72, 82, 92, 102]) == True


