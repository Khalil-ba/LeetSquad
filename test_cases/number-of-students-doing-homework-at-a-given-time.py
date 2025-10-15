def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(startTime = [9, 8, 7, 6],endTime = [10, 9, 8, 7],queryTime = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [9, 8, 7, 6],endTime = [10, 9, 8, 7],queryTime = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5],endTime = [5, 4, 3, 2, 1],queryTime = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5],endTime = [5, 4, 3, 2, 1],queryTime = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [5, 5, 5, 5],endTime = [10, 10, 10, 10],queryTime = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [5, 5, 5, 5],endTime = [10, 10, 10, 10],queryTime = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [9, 8, 7, 6, 5, 4, 3, 2, 1],endTime = [10, 9, 8, 7, 6, 5, 4, 3, 2],queryTime = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [9, 8, 7, 6, 5, 4, 3, 2, 1],endTime = [10, 9, 8, 7, 6, 5, 4, 3, 2],queryTime = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [4],endTime = [4],queryTime = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [4],endTime = [4],queryTime = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3],endTime = [3, 2, 7],queryTime = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3],endTime = [3, 2, 7],queryTime = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300],endTime = [150, 250, 350],queryTime = 225) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300],endTime = [150, 250, 350],queryTime = 225) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 6, 7, 9],endTime = [2, 5, 8, 10, 12],queryTime = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 6, 7, 9],endTime = [2, 5, 8, 10, 12],queryTime = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [9, 8, 7, 6, 5, 4, 3, 2, 1],endTime = [10, 9, 8, 7, 6, 5, 4, 3, 2],queryTime = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [9, 8, 7, 6, 5, 4, 3, 2, 1],endTime = [10, 9, 8, 7, 6, 5, 4, 3, 2],queryTime = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 1, 1, 1],endTime = [2, 2, 2, 2],queryTime = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 1, 1, 1],endTime = [2, 2, 2, 2],queryTime = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 5, 7],endTime = [2, 4, 6, 8],queryTime = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 5, 7],endTime = [2, 4, 6, 8],queryTime = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [10, 20, 30],endTime = [15, 25, 35],queryTime = 22) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [10, 20, 30],endTime = [15, 25, 35],queryTime = 22) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [5, 5, 5, 5],endTime = [6, 6, 6, 6],queryTime = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [5, 5, 5, 5],endTime = [6, 6, 6, 6],queryTime = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300],endTime = [150, 250, 350],queryTime = 225) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300],endTime = [150, 250, 350],queryTime = 225) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 1, 1, 1, 1],endTime = [2, 2, 2, 2, 2],queryTime = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 1, 1, 1, 1],endTime = [2, 2, 2, 2, 2],queryTime = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300, 400],endTime = [199, 299, 399, 499],queryTime = 250) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300, 400],endTime = [199, 299, 399, 499],queryTime = 250) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],queryTime = 500) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],queryTime = 500) == 6: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950],endTime = [550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],queryTime = 725) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950],endTime = [550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],queryTime = 725) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [10, 15, 20, 25, 30, 35, 40, 45, 50],endTime = [14, 19, 24, 29, 34, 39, 44, 49, 54],queryTime = 22) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [10, 15, 20, 25, 30, 35, 40, 45, 50],endTime = [14, 19, 24, 29, 34, 39, 44, 49, 54],queryTime = 22) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [50, 100, 150, 200, 250],endTime = [75, 125, 175, 225, 275],queryTime = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [50, 100, 150, 200, 250],endTime = [75, 125, 175, 225, 275],queryTime = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 1, 1, 1, 1, 1],endTime = [10, 20, 30, 40, 50, 60],queryTime = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 1, 1, 1, 1, 1],endTime = [10, 20, 30, 40, 50, 60],queryTime = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [250, 500, 750],endTime = [260, 510, 760],queryTime = 255) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [250, 500, 750],endTime = [260, 510, 760],queryTime = 255) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],endTime = [350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250],queryTime = 625) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],endTime = [350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250],queryTime = 625) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5],endTime = [5, 4, 3, 2, 1],queryTime = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5],endTime = [5, 4, 3, 2, 1],queryTime = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],endTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queryTime = 55) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],endTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queryTime = 55) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [19, 29, 39, 49, 59, 69, 79, 89, 99, 109],queryTime = 55) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [19, 29, 39, 49, 59, 69, 79, 89, 99, 109],queryTime = 55) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [10, 20, 30, 40, 50],endTime = [15, 25, 35, 45, 55],queryTime = 28) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [10, 20, 30, 40, 50],endTime = [15, 25, 35, 45, 55],queryTime = 28) == 0: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 5, 7, 9],endTime = [10, 8, 6, 4, 2],queryTime = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 5, 7, 9],endTime = [10, 8, 6, 4, 2],queryTime = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],endTime = [55, 105, 155, 205, 255, 305, 355, 405, 455, 505],queryTime = 102) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],endTime = [55, 105, 155, 205, 255, 305, 355, 405, 455, 505],queryTime = 102) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 1, 1, 1, 1],endTime = [5, 5, 5, 5, 5],queryTime = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 1, 1, 1, 1],endTime = [5, 5, 5, 5, 5],queryTime = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queryTime = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queryTime = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queryTime = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queryTime = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 10, 20, 30, 40, 50],endTime = [10, 20, 30, 40, 50, 60],queryTime = 55) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 10, 20, 30, 40, 50],endTime = [10, 20, 30, 40, 50, 60],queryTime = 55) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [10, 20, 30, 40, 50],endTime = [15, 25, 35, 45, 55],queryTime = 33) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [10, 20, 30, 40, 50],endTime = [15, 25, 35, 45, 55],queryTime = 33) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [300, 300, 300, 300],endTime = [600, 600, 600, 600],queryTime = 400) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [300, 300, 300, 300],endTime = [600, 600, 600, 600],queryTime = 400) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [10, 20, 30, 40, 50],endTime = [10, 20, 30, 40, 50],queryTime = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [10, 20, 30, 40, 50],endTime = [10, 20, 30, 40, 50],queryTime = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5],endTime = [10, 11, 12, 13, 14],queryTime = 8) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5],endTime = [10, 11, 12, 13, 14],queryTime = 8) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 1, 1, 1, 1, 1],endTime = [6, 7, 8, 9, 10, 11],queryTime = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 1, 1, 1, 1, 1],endTime = [6, 7, 8, 9, 10, 11],queryTime = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 1, 1, 1],endTime = [1000, 1000, 1000, 1000],queryTime = 500) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 1, 1, 1],endTime = [1000, 1000, 1000, 1000],queryTime = 500) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [5, 10, 15, 20, 25],endTime = [14, 19, 24, 29, 34],queryTime = 22) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [5, 10, 15, 20, 25],endTime = [14, 19, 24, 29, 34],queryTime = 22) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queryTime = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queryTime = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300, 400],endTime = [150, 250, 350, 450],queryTime = 225) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300, 400],endTime = [150, 250, 350, 450],queryTime = 225) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5],endTime = [10, 20, 30, 40, 50],queryTime = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5],endTime = [10, 20, 30, 40, 50],queryTime = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300, 400, 500],endTime = [150, 250, 350, 450, 550],queryTime = 225) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300, 400, 500],endTime = [150, 250, 350, 450, 550],queryTime = 225) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],endTime = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],queryTime = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],endTime = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],queryTime = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],queryTime = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],queryTime = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300, 400, 500],endTime = [100, 200, 300, 400, 500],queryTime = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300, 400, 500],endTime = [100, 200, 300, 400, 500],queryTime = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [10, 20, 30, 40],endTime = [100, 200, 300, 400],queryTime = 150) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [10, 20, 30, 40],endTime = [100, 200, 300, 400],queryTime = 150) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [900, 905, 910, 915],endTime = [909, 914, 919, 924],queryTime = 907) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [900, 905, 910, 915],endTime = [909, 914, 919, 924],queryTime = 907) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 6, 8, 10],endTime = [2, 5, 7, 10, 12],queryTime = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 6, 8, 10],endTime = [2, 5, 7, 10, 12],queryTime = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 1, 1, 1, 1],endTime = [1, 1, 1, 1, 1],queryTime = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 1, 1, 1, 1],endTime = [1, 1, 1, 1, 1],queryTime = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [2, 2, 2, 2, 2],endTime = [10, 10, 10, 10, 10],queryTime = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [2, 2, 2, 2, 2],endTime = [10, 10, 10, 10, 10],queryTime = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300, 400, 500],endTime = [200, 300, 400, 500, 600],queryTime = 350) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300, 400, 500],endTime = [200, 300, 400, 500, 600],queryTime = 350) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 5, 7, 9],endTime = [2, 4, 6, 8, 10],queryTime = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 5, 7, 9],endTime = [2, 4, 6, 8, 10],queryTime = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300, 400, 500],endTime = [150, 250, 350, 450, 550],queryTime = 275) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300, 400, 500],endTime = [150, 250, 350, 450, 550],queryTime = 275) == 0: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300, 400],endTime = [101, 201, 301, 401],queryTime = 200) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300, 400],endTime = [101, 201, 301, 401],queryTime = 200) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],queryTime = 63) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],queryTime = 63) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 150, 200, 250],endTime = [149, 199, 249, 299],queryTime = 175) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 150, 200, 250],endTime = [149, 199, 249, 299],queryTime = 175) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [50, 100, 150, 200, 250],endTime = [99, 199, 299, 399, 499],queryTime = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [50, 100, 150, 200, 250],endTime = [99, 199, 299, 399, 499],queryTime = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],endTime = [14, 24, 34, 44, 54, 64, 74, 84, 94, 104],queryTime = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],endTime = [14, 24, 34, 44, 54, 64, 74, 84, 94, 104],queryTime = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],endTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queryTime = 50) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],endTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queryTime = 50) == 6: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],queryTime = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],queryTime = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],endTime = [110, 210, 310, 410, 510, 610, 710, 810, 910, 1010],queryTime = 305) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],endTime = [110, 210, 310, 410, 510, 610, 710, 810, 910, 1010],queryTime = 305) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queryTime = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queryTime = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300, 400, 500],endTime = [500, 400, 300, 200, 100],queryTime = 300) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300, 400, 500],endTime = [500, 400, 300, 200, 100],queryTime = 300) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5],endTime = [10, 9, 8, 7, 6],queryTime = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5],endTime = [10, 9, 8, 7, 6],queryTime = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [200, 200, 300, 300],endTime = [200, 400, 400, 500],queryTime = 200) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [200, 200, 300, 300],endTime = [200, 400, 400, 500],queryTime = 200) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [10, 10, 10, 10, 10],endTime = [15, 15, 15, 15, 15],queryTime = 12) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [10, 10, 10, 10, 10],endTime = [15, 15, 15, 15, 15],queryTime = 12) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 10, 20, 30, 40, 50],endTime = [10, 20, 30, 40, 50, 60],queryTime = 25) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 10, 20, 30, 40, 50],endTime = [10, 20, 30, 40, 50, 60],queryTime = 25) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [999, 998, 997, 996, 995],endTime = [1000, 1000, 1000, 1000, 1000],queryTime = 999) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [999, 998, 997, 996, 995],endTime = [1000, 1000, 1000, 1000, 1000],queryTime = 999) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300, 400, 500],endTime = [150, 250, 350, 450, 550],queryTime = 325) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300, 400, 500],endTime = [150, 250, 350, 450, 550],queryTime = 325) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0],queryTime = 55) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0],queryTime = 55) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 1, 1, 1, 1],endTime = [1000, 1000, 1000, 1000, 1000],queryTime = 500) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 1, 1, 1, 1],endTime = [1000, 1000, 1000, 1000, 1000],queryTime = 500) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300, 400, 500],endTime = [200, 300, 400, 500, 600],queryTime = 250) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300, 400, 500],endTime = [200, 300, 400, 500, 600],queryTime = 250) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5],endTime = [5, 10, 15, 20, 25],queryTime = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5],endTime = [5, 10, 15, 20, 25],queryTime = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [9, 10, 11, 12, 13],endTime = [10, 12, 14, 16, 18],queryTime = 12) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [9, 10, 11, 12, 13],endTime = [10, 12, 14, 16, 18],queryTime = 12) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],endTime = [101, 201, 301, 401, 501, 601, 701, 801, 901, 1001],queryTime = 500) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],endTime = [101, 201, 301, 401, 501, 601, 701, 801, 901, 1001],queryTime = 500) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5],endTime = [10, 20, 30, 40, 50],queryTime = 25) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5],endTime = [10, 20, 30, 40, 50],queryTime = 25) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300, 400, 500],endTime = [199, 299, 399, 499, 599],queryTime = 450) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300, 400, 500],endTime = [199, 299, 399, 499, 599],queryTime = 450) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29],endTime = [4, 7, 10, 13, 16, 19, 22, 25, 28, 31],queryTime = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29],endTime = [4, 7, 10, 13, 16, 19, 22, 25, 28, 31],queryTime = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],queryTime = 55) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],queryTime = 55) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],endTime = [1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],queryTime = 1500) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],endTime = [1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],queryTime = 1500) == 6: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],endTime = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],queryTime = 550) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],endTime = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],queryTime = 550) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [10, 20, 30, 40, 50],endTime = [100, 110, 120, 130, 140],queryTime = 60) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [10, 20, 30, 40, 50],endTime = [100, 110, 120, 130, 140],queryTime = 60) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 3, 5, 7, 9, 11],endTime = [2, 4, 6, 8, 10, 12],queryTime = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 3, 5, 7, 9, 11],endTime = [2, 4, 6, 8, 10, 12],queryTime = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300, 400, 500],endTime = [150, 250, 350, 450, 550],queryTime = 400) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300, 400, 500],endTime = [150, 250, 350, 450, 550],queryTime = 400) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [500, 501, 502, 503, 504, 505],endTime = [500, 501, 502, 503, 504, 505],queryTime = 505) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [500, 501, 502, 503, 504, 505],endTime = [500, 501, 502, 503, 504, 505],queryTime = 505) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],endTime = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],queryTime = 7) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],endTime = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],queryTime = 7) == 10: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [500, 600, 700, 800],endTime = [599, 699, 799, 899],queryTime = 750) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [500, 600, 700, 800],endTime = [599, 699, 799, 899],queryTime = 750) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 100, 200, 300, 400],endTime = [100, 200, 300, 400, 500],queryTime = 150) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 100, 200, 300, 400],endTime = [100, 200, 300, 400, 500],queryTime = 150) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],queryTime = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],queryTime = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [500, 550, 600, 650],endTime = [501, 551, 601, 651],queryTime = 550) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [500, 550, 600, 650],endTime = [501, 551, 601, 651],queryTime = 550) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],endTime = [5, 6, 6, 7, 7, 8, 8, 9, 9, 10],queryTime = 6) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],endTime = [5, 6, 6, 7, 7, 8, 8, 9, 9, 10],queryTime = 6) == 9: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [100, 200, 300, 400, 500],endTime = [1000, 1000, 1000, 1000, 1000],queryTime = 500) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [100, 200, 300, 400, 500],endTime = [1000, 1000, 1000, 1000, 1000],queryTime = 500) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startTime = [10, 20, 30, 40],endTime = [15, 25, 35, 45],queryTime = 22) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startTime = [10, 20, 30, 40],endTime = [15, 25, 35, 45],queryTime = 22) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(startTime = [9, 8, 7, 6],endTime = [10, 9, 8, 7],queryTime = 8) == 2
    assert candidate(startTime = [1, 2, 3, 4, 5],endTime = [5, 4, 3, 2, 1],queryTime = 3) == 3
    assert candidate(startTime = [5, 5, 5, 5],endTime = [10, 10, 10, 10],queryTime = 7) == 4
    assert candidate(startTime = [9, 8, 7, 6, 5, 4, 3, 2, 1],endTime = [10, 9, 8, 7, 6, 5, 4, 3, 2],queryTime = 5) == 2
    assert candidate(startTime = [4],endTime = [4],queryTime = 4) == 1
    assert candidate(startTime = [1, 2, 3],endTime = [3, 2, 7],queryTime = 4) == 1
    assert candidate(startTime = [100, 200, 300],endTime = [150, 250, 350],queryTime = 225) == 1
    assert candidate(startTime = [1, 3, 6, 7, 9],endTime = [2, 5, 8, 10, 12],queryTime = 6) == 1
    assert candidate(startTime = [9, 8, 7, 6, 5, 4, 3, 2, 1],endTime = [10, 9, 8, 7, 6, 5, 4, 3, 2],queryTime = 6) == 2
    assert candidate(startTime = [1, 1, 1, 1],endTime = [2, 2, 2, 2],queryTime = 1) == 4
    assert candidate(startTime = [1, 3, 5, 7],endTime = [2, 4, 6, 8],queryTime = 5) == 1
    assert candidate(startTime = [10, 20, 30],endTime = [15, 25, 35],queryTime = 22) == 1
    assert candidate(startTime = [5, 5, 5, 5],endTime = [6, 6, 6, 6],queryTime = 5) == 4
    assert candidate(startTime = [100, 200, 300],endTime = [150, 250, 350],queryTime = 225) == 1
    assert candidate(startTime = [1, 1, 1, 1, 1],endTime = [2, 2, 2, 2, 2],queryTime = 1) == 5
    assert candidate(startTime = [100, 200, 300, 400],endTime = [199, 299, 399, 499],queryTime = 250) == 1
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],queryTime = 500) == 6
    assert candidate(startTime = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950],endTime = [550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],queryTime = 725) == 1
    assert candidate(startTime = [10, 15, 20, 25, 30, 35, 40, 45, 50],endTime = [14, 19, 24, 29, 34, 39, 44, 49, 54],queryTime = 22) == 1
    assert candidate(startTime = [50, 100, 150, 200, 250],endTime = [75, 125, 175, 225, 275],queryTime = 100) == 1
    assert candidate(startTime = [1, 1, 1, 1, 1, 1],endTime = [10, 20, 30, 40, 50, 60],queryTime = 5) == 6
    assert candidate(startTime = [250, 500, 750],endTime = [260, 510, 760],queryTime = 255) == 1
    assert candidate(startTime = [300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],endTime = [350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250],queryTime = 625) == 1
    assert candidate(startTime = [1, 2, 3, 4, 5],endTime = [5, 4, 3, 2, 1],queryTime = 3) == 3
    assert candidate(startTime = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],endTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queryTime = 55) == 5
    assert candidate(startTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [19, 29, 39, 49, 59, 69, 79, 89, 99, 109],queryTime = 55) == 1
    assert candidate(startTime = [10, 20, 30, 40, 50],endTime = [15, 25, 35, 45, 55],queryTime = 28) == 0
    assert candidate(startTime = [1, 3, 5, 7, 9],endTime = [10, 8, 6, 4, 2],queryTime = 5) == 3
    assert candidate(startTime = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],endTime = [55, 105, 155, 205, 255, 305, 355, 405, 455, 505],queryTime = 102) == 1
    assert candidate(startTime = [1, 1, 1, 1, 1],endTime = [5, 5, 5, 5, 5],queryTime = 3) == 5
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queryTime = 5) == 5
    assert candidate(startTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queryTime = 10) == 1
    assert candidate(startTime = [1, 10, 20, 30, 40, 50],endTime = [10, 20, 30, 40, 50, 60],queryTime = 55) == 1
    assert candidate(startTime = [10, 20, 30, 40, 50],endTime = [15, 25, 35, 45, 55],queryTime = 33) == 1
    assert candidate(startTime = [300, 300, 300, 300],endTime = [600, 600, 600, 600],queryTime = 400) == 4
    assert candidate(startTime = [10, 20, 30, 40, 50],endTime = [10, 20, 30, 40, 50],queryTime = 10) == 1
    assert candidate(startTime = [1, 2, 3, 4, 5],endTime = [10, 11, 12, 13, 14],queryTime = 8) == 5
    assert candidate(startTime = [1, 1, 1, 1, 1, 1],endTime = [6, 7, 8, 9, 10, 11],queryTime = 5) == 6
    assert candidate(startTime = [1, 1, 1, 1],endTime = [1000, 1000, 1000, 1000],queryTime = 500) == 4
    assert candidate(startTime = [5, 10, 15, 20, 25],endTime = [14, 19, 24, 29, 34],queryTime = 22) == 2
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queryTime = 6) == 5
    assert candidate(startTime = [100, 200, 300, 400],endTime = [150, 250, 350, 450],queryTime = 225) == 1
    assert candidate(startTime = [1, 2, 3, 4, 5],endTime = [10, 20, 30, 40, 50],queryTime = 1) == 1
    assert candidate(startTime = [100, 200, 300, 400, 500],endTime = [150, 250, 350, 450, 550],queryTime = 225) == 1
    assert candidate(startTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],endTime = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],queryTime = 5) == 10
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],queryTime = 10) == 2
    assert candidate(startTime = [100, 200, 300, 400, 500],endTime = [100, 200, 300, 400, 500],queryTime = 100) == 1
    assert candidate(startTime = [10, 20, 30, 40],endTime = [100, 200, 300, 400],queryTime = 150) == 3
    assert candidate(startTime = [900, 905, 910, 915],endTime = [909, 914, 919, 924],queryTime = 907) == 2
    assert candidate(startTime = [1, 3, 6, 8, 10],endTime = [2, 5, 7, 10, 12],queryTime = 4) == 1
    assert candidate(startTime = [1, 1, 1, 1, 1],endTime = [1, 1, 1, 1, 1],queryTime = 1) == 5
    assert candidate(startTime = [2, 2, 2, 2, 2],endTime = [10, 10, 10, 10, 10],queryTime = 6) == 5
    assert candidate(startTime = [100, 200, 300, 400, 500],endTime = [200, 300, 400, 500, 600],queryTime = 350) == 1
    assert candidate(startTime = [1, 3, 5, 7, 9],endTime = [2, 4, 6, 8, 10],queryTime = 5) == 1
    assert candidate(startTime = [100, 200, 300, 400, 500],endTime = [150, 250, 350, 450, 550],queryTime = 275) == 0
    assert candidate(startTime = [100, 200, 300, 400],endTime = [101, 201, 301, 401],queryTime = 200) == 1
    assert candidate(startTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],queryTime = 63) == 1
    assert candidate(startTime = [100, 150, 200, 250],endTime = [149, 199, 249, 299],queryTime = 175) == 1
    assert candidate(startTime = [50, 100, 150, 200, 250],endTime = [99, 199, 299, 399, 499],queryTime = 100) == 1
    assert candidate(startTime = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],endTime = [14, 24, 34, 44, 54, 64, 74, 84, 94, 104],queryTime = 100) == 1
    assert candidate(startTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],endTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queryTime = 50) == 6
    assert candidate(startTime = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],endTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],queryTime = 10) == 1
    assert candidate(startTime = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],endTime = [110, 210, 310, 410, 510, 610, 710, 810, 910, 1010],queryTime = 305) == 1
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queryTime = 5) == 1
    assert candidate(startTime = [100, 200, 300, 400, 500],endTime = [500, 400, 300, 200, 100],queryTime = 300) == 3
    assert candidate(startTime = [1, 2, 3, 4, 5],endTime = [10, 9, 8, 7, 6],queryTime = 6) == 5
    assert candidate(startTime = [200, 200, 300, 300],endTime = [200, 400, 400, 500],queryTime = 200) == 2
    assert candidate(startTime = [10, 10, 10, 10, 10],endTime = [15, 15, 15, 15, 15],queryTime = 12) == 5
    assert candidate(startTime = [1, 10, 20, 30, 40, 50],endTime = [10, 20, 30, 40, 50, 60],queryTime = 25) == 1
    assert candidate(startTime = [999, 998, 997, 996, 995],endTime = [1000, 1000, 1000, 1000, 1000],queryTime = 999) == 5
    assert candidate(startTime = [100, 200, 300, 400, 500],endTime = [150, 250, 350, 450, 550],queryTime = 325) == 1
    assert candidate(startTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0],queryTime = 55) == 4
    assert candidate(startTime = [1, 1, 1, 1, 1],endTime = [1000, 1000, 1000, 1000, 1000],queryTime = 500) == 5
    assert candidate(startTime = [100, 200, 300, 400, 500],endTime = [200, 300, 400, 500, 600],queryTime = 250) == 1
    assert candidate(startTime = [1, 2, 3, 4, 5],endTime = [5, 10, 15, 20, 25],queryTime = 3) == 3
    assert candidate(startTime = [9, 10, 11, 12, 13],endTime = [10, 12, 14, 16, 18],queryTime = 12) == 3
    assert candidate(startTime = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],endTime = [101, 201, 301, 401, 501, 601, 701, 801, 901, 1001],queryTime = 500) == 1
    assert candidate(startTime = [1, 2, 3, 4, 5],endTime = [10, 20, 30, 40, 50],queryTime = 25) == 3
    assert candidate(startTime = [100, 200, 300, 400, 500],endTime = [199, 299, 399, 499, 599],queryTime = 450) == 1
    assert candidate(startTime = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29],endTime = [4, 7, 10, 13, 16, 19, 22, 25, 28, 31],queryTime = 15) == 1
    assert candidate(startTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],endTime = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],queryTime = 55) == 1
    assert candidate(startTime = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],endTime = [1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],queryTime = 1500) == 6
    assert candidate(startTime = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],endTime = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],queryTime = 550) == 5
    assert candidate(startTime = [10, 20, 30, 40, 50],endTime = [100, 110, 120, 130, 140],queryTime = 60) == 5
    assert candidate(startTime = [1, 3, 5, 7, 9, 11],endTime = [2, 4, 6, 8, 10, 12],queryTime = 6) == 1
    assert candidate(startTime = [100, 200, 300, 400, 500],endTime = [150, 250, 350, 450, 550],queryTime = 400) == 1
    assert candidate(startTime = [500, 501, 502, 503, 504, 505],endTime = [500, 501, 502, 503, 504, 505],queryTime = 505) == 1
    assert candidate(startTime = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],endTime = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],queryTime = 7) == 10
    assert candidate(startTime = [500, 600, 700, 800],endTime = [599, 699, 799, 899],queryTime = 750) == 1
    assert candidate(startTime = [1, 100, 200, 300, 400],endTime = [100, 200, 300, 400, 500],queryTime = 150) == 1
    assert candidate(startTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],endTime = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],queryTime = 15) == 6
    assert candidate(startTime = [500, 550, 600, 650],endTime = [501, 551, 601, 651],queryTime = 550) == 1
    assert candidate(startTime = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],endTime = [5, 6, 6, 7, 7, 8, 8, 9, 9, 10],queryTime = 6) == 9
    assert candidate(startTime = [100, 200, 300, 400, 500],endTime = [1000, 1000, 1000, 1000, 1000],queryTime = 500) == 5
    assert candidate(startTime = [10, 20, 30, 40],endTime = [15, 25, 35, 45],queryTime = 22) == 1


