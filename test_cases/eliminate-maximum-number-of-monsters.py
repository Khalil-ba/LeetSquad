def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(dist = [6, 7, 8],speed = [2, 2, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [6, 7, 8],speed = [2, 2, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3],speed = [3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3],speed = [3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300],speed = [1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300],speed = [1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [7, 14, 21],speed = [1, 2, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [7, 14, 21],speed = [1, 2, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [3, 5, 7, 9],speed = [1, 2, 3, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [3, 5, 7, 9],speed = [1, 2, 3, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 2, 3],speed = [1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 2, 3],speed = [1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500],speed = [50, 40, 30, 20, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500],speed = [50, 40, 30, 20, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [6, 4, 5],speed = [1, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [6, 4, 5],speed = [1, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5],speed = [1, 2, 3, 4, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5],speed = [1, 2, 3, 4, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 3, 4],speed = [1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 3, 4],speed = [1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30],speed = [1, 2, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30],speed = [1, 2, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 10, 15, 20],speed = [5, 4, 3, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 10, 15, 20],speed = [5, 4, 3, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(dist = [3, 2, 4],speed = [5, 3, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [3, 2, 4],speed = [5, 3, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5],speed = [1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5],speed = [1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 5, 6, 12, 3],speed = [2, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 5, 6, 12, 3],speed = [2, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 5, 5],speed = [1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 5, 5],speed = [1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [2, 4, 6],speed = [2, 2, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [2, 4, 6],speed = [2, 2, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1],speed = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1],speed = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500],speed = [10, 20, 30, 40, 50]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500],speed = [10, 20, 30, 40, 50]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 5, 5, 5],speed = [1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 5, 5, 5],speed = [1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(dist = [6, 7, 12, 13, 14],speed = [3, 3, 4, 4, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [6, 7, 12, 13, 14],speed = [3, 3, 4, 4, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [6, 3, 4, 1],speed = [2, 1, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [6, 3, 4, 1],speed = [2, 1, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30],speed = [5, 10, 15]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30],speed = [5, 10, 15]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 15, 20],speed = [2, 3, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 15, 20],speed = [2, 3, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30],speed = [5, 5, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30],speed = [5, 5, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300],speed = [10, 20, 30]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300],speed = [10, 20, 30]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40],speed = [10, 10, 10, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40],speed = [10, 10, 10, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5],speed = [5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5],speed = [5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 10, 10, 10, 10],speed = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 10, 10, 10, 10],speed = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [500, 1000, 1500, 2000, 2500],speed = [50, 100, 150, 200, 250]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [500, 1000, 1500, 2000, 2500],speed = [50, 100, 150, 200, 250]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],speed = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],speed = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500],speed = [1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500],speed = [1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1000, 900, 800, 700, 600],speed = [100, 200, 300, 400, 500]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1000, 900, 800, 700, 600],speed = [100, 200, 300, 400, 500]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [9, 8, 7, 6, 5, 4, 3, 2, 1],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [9, 8, 7, 6, 5, 4, 3, 2, 1],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [2, 3, 4, 5, 6],speed = [2, 2, 2, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [2, 3, 4, 5, 6],speed = [2, 2, 2, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50],speed = [2, 3, 4, 5, 6]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50],speed = [2, 3, 4, 5, 6]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 25, 40, 55, 70, 85],speed = [5, 5, 5, 5, 5, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 25, 40, 55, 70, 85],speed = [5, 5, 5, 5, 5, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 15, 20, 25],speed = [5, 4, 3, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 15, 20, 25],speed = [5, 4, 3, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(dist = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [99, 98, 97, 96, 95],speed = [1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [99, 98, 97, 96, 95],speed = [1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1000, 1500, 2000, 2500, 3000],speed = [100, 200, 300, 400, 500]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1000, 1500, 2000, 2500, 3000],speed = [100, 200, 300, 400, 500]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500],speed = [50, 40, 30, 20, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500],speed = [50, 40, 30, 20, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500],speed = [10, 20, 30, 40, 50]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500],speed = [10, 20, 30, 40, 50]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [15, 15, 20, 25, 30],speed = [1, 2, 1, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [15, 15, 20, 25, 30],speed = [1, 2, 1, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],speed = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],speed = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],speed = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],speed = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 15, 25, 35, 45],speed = [1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 15, 25, 35, 45],speed = [1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50],speed = [5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50],speed = [5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dist = [2, 4, 6, 8, 10],speed = [1, 2, 3, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [2, 4, 6, 8, 10],speed = [1, 2, 3, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],speed = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],speed = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 10, 15, 20, 25, 30],speed = [1, 1, 1, 1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 10, 15, 20, 25, 30],speed = [1, 1, 1, 1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [25, 25, 25, 25, 25],speed = [5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [25, 25, 25, 25, 25],speed = [5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [2, 4, 6, 8, 10],speed = [1, 2, 3, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [2, 4, 6, 8, 10],speed = [1, 2, 3, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 15, 25, 35, 45],speed = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 15, 25, 35, 45],speed = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 10, 15, 20, 25, 30],speed = [1, 2, 3, 4, 5, 6]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 10, 15, 20, 25, 30],speed = [1, 2, 3, 4, 5, 6]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [99, 198, 297, 396, 495, 594, 693, 792, 891, 990],speed = [99, 99, 99, 99, 99, 99, 99, 99, 99, 99]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [99, 198, 297, 396, 495, 594, 693, 792, 891, 990],speed = [99, 99, 99, 99, 99, 99, 99, 99, 99, 99]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [3, 5, 7, 9, 11],speed = [1, 2, 3, 4, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [3, 5, 7, 9, 11],speed = [1, 2, 3, 4, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10000, 20000, 30000, 40000, 50000],speed = [100, 200, 300, 400, 500]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10000, 20000, 30000, 40000, 50000],speed = [100, 200, 300, 400, 500]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [3, 6, 9, 12, 15],speed = [1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [3, 6, 9, 12, 15],speed = [1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5],speed = [5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5],speed = [5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50],speed = [2, 4, 5, 6, 8]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50],speed = [2, 4, 5, 6, 8]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1000, 2000, 3000],speed = [10, 20, 30]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1000, 2000, 3000],speed = [10, 20, 30]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 25, 30, 45, 50, 65, 70, 85, 90, 105],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 25, 30, 45, 50, 65, 70, 85, 90, 105],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [2, 3, 4, 5, 6],speed = [1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [2, 3, 4, 5, 6],speed = [1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50],speed = [10, 20, 30, 40, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50],speed = [10, 20, 30, 40, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50],speed = [2, 2, 2, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50],speed = [2, 2, 2, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [9, 9, 9, 9, 9],speed = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [9, 9, 9, 9, 9],speed = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 150, 200, 250, 300],speed = [25, 50, 75, 100, 125]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 150, 200, 250, 300],speed = [25, 50, 75, 100, 125]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50],speed = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50],speed = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 11, 12, 13, 14],speed = [1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 11, 12, 13, 14],speed = [1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [15, 10, 20, 30, 40],speed = [2, 5, 3, 4, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [15, 10, 20, 30, 40],speed = [2, 5, 3, 4, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(dist = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500],speed = [50, 100, 150, 200, 250]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500],speed = [50, 100, 150, 200, 250]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dist = [3, 6, 9, 12, 15, 18],speed = [1, 2, 3, 4, 5, 6]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [3, 6, 9, 12, 15, 18],speed = [1, 2, 3, 4, 5, 6]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50],speed = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50],speed = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [9, 18, 27, 36, 45],speed = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [9, 18, 27, 36, 45],speed = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [15, 25, 35, 45, 55],speed = [5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [15, 25, 35, 45, 55],speed = [5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500],speed = [50, 50, 50, 50, 50]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500],speed = [50, 50, 50, 50, 50]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(dist = [2, 4, 6, 8, 10],speed = [2, 2, 2, 2, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [2, 4, 6, 8, 10],speed = [2, 2, 2, 2, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [7, 14, 21, 28, 35],speed = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [7, 14, 21, 28, 35],speed = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 150, 200, 250, 300],speed = [5, 10, 15, 20, 25]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 150, 200, 250, 300],speed = [5, 10, 15, 20, 25]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 150, 200, 250, 300, 350, 400, 450, 500],speed = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 150, 200, 250, 300, 350, 400, 450, 500],speed = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 9: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(dist = [6, 7, 8],speed = [2, 2, 2]) == 3
    assert candidate(dist = [1, 2, 3],speed = [3, 2, 1]) == 1
    assert candidate(dist = [100, 200, 300],speed = [1, 1, 1]) == 3
    assert candidate(dist = [7, 14, 21],speed = [1, 2, 3]) == 3
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(dist = [3, 5, 7, 9],speed = [1, 2, 3, 4]) == 3
    assert candidate(dist = [1, 1, 2, 3],speed = [1, 1, 1, 1]) == 1
    assert candidate(dist = [100, 200, 300, 400, 500],speed = [50, 40, 30, 20, 10]) == 5
    assert candidate(dist = [6, 4, 5],speed = [1, 2, 1]) == 3
    assert candidate(dist = [1, 2, 3, 4, 5],speed = [1, 2, 3, 4, 5]) == 1
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(dist = [1, 3, 4],speed = [1, 1, 1]) == 3
    assert candidate(dist = [10, 20, 30],speed = [1, 2, 3]) == 3
    assert candidate(dist = [5, 10, 15, 20],speed = [5, 4, 3, 2]) == 4
    assert candidate(dist = [3, 2, 4],speed = [5, 3, 2]) == 1
    assert candidate(dist = [1, 2, 3, 4, 5],speed = [1, 1, 1, 1, 1]) == 5
    assert candidate(dist = [10, 5, 6, 12, 3],speed = [2, 1, 1, 1, 1]) == 5
    assert candidate(dist = [5, 5, 5],speed = [1, 1, 1]) == 3
    assert candidate(dist = [2, 4, 6],speed = [2, 2, 2]) == 3
    assert candidate(dist = [1],speed = [1]) == 1
    assert candidate(dist = [100, 200, 300, 400, 500],speed = [10, 20, 30, 40, 50]) == 5
    assert candidate(dist = [5, 5, 5, 5],speed = [1, 1, 1, 1]) == 4
    assert candidate(dist = [6, 7, 12, 13, 14],speed = [3, 3, 4, 4, 5]) == 3
    assert candidate(dist = [6, 3, 4, 1],speed = [2, 1, 2, 1]) == 3
    assert candidate(dist = [10, 20, 30],speed = [5, 10, 15]) == 2
    assert candidate(dist = [10, 15, 20],speed = [2, 3, 4]) == 3
    assert candidate(dist = [10, 20, 30],speed = [5, 5, 5]) == 3
    assert candidate(dist = [100, 200, 300],speed = [10, 20, 30]) == 3
    assert candidate(dist = [10, 20, 30, 40],speed = [10, 10, 10, 10]) == 4
    assert candidate(dist = [1, 2, 3, 4, 5],speed = [5, 4, 3, 2, 1]) == 1
    assert candidate(dist = [10, 10, 10, 10, 10],speed = [1, 2, 3, 4, 5]) == 5
    assert candidate(dist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(dist = [500, 1000, 1500, 2000, 2500],speed = [50, 100, 150, 200, 250]) == 5
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(dist = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],speed = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
    assert candidate(dist = [100, 200, 300, 400, 500],speed = [1, 1, 1, 1, 1]) == 5
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(dist = [1000, 900, 800, 700, 600],speed = [100, 200, 300, 400, 500]) == 5
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(dist = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
    assert candidate(dist = [9, 8, 7, 6, 5, 4, 3, 2, 1],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
    assert candidate(dist = [2, 3, 4, 5, 6],speed = [2, 2, 2, 2, 2]) == 2
    assert candidate(dist = [10, 20, 30, 40, 50],speed = [2, 3, 4, 5, 6]) == 5
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
    assert candidate(dist = [10, 25, 40, 55, 70, 85],speed = [5, 5, 5, 5, 5, 5]) == 6
    assert candidate(dist = [10, 15, 20, 25],speed = [5, 4, 3, 2]) == 4
    assert candidate(dist = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(dist = [99, 98, 97, 96, 95],speed = [1, 1, 1, 1, 1]) == 5
    assert candidate(dist = [1000, 1500, 2000, 2500, 3000],speed = [100, 200, 300, 400, 500]) == 5
    assert candidate(dist = [100, 200, 300, 400, 500],speed = [50, 40, 30, 20, 10]) == 5
    assert candidate(dist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(dist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(dist = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(dist = [100, 200, 300, 400, 500],speed = [10, 20, 30, 40, 50]) == 5
    assert candidate(dist = [15, 15, 20, 25, 30],speed = [1, 2, 1, 2, 1]) == 5
    assert candidate(dist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],speed = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 10
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],speed = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(dist = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(dist = [5, 15, 25, 35, 45],speed = [1, 1, 1, 1, 1]) == 5
    assert candidate(dist = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(dist = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(dist = [10, 20, 30, 40, 50],speed = [5, 5, 5, 5, 5]) == 5
    assert candidate(dist = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(dist = [2, 4, 6, 8, 10],speed = [1, 2, 3, 4, 5]) == 2
    assert candidate(dist = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],speed = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
    assert candidate(dist = [5, 10, 15, 20, 25, 30],speed = [1, 1, 1, 1, 1, 1]) == 6
    assert candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(dist = [25, 25, 25, 25, 25],speed = [5, 5, 5, 5, 5]) == 5
    assert candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(dist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 5
    assert candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(dist = [2, 4, 6, 8, 10],speed = [1, 2, 3, 4, 5]) == 2
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 10
    assert candidate(dist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(dist = [5, 15, 25, 35, 45],speed = [1, 2, 3, 4, 5]) == 5
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(dist = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(dist = [5, 10, 15, 20, 25, 30],speed = [1, 2, 3, 4, 5, 6]) == 5
    assert candidate(dist = [99, 198, 297, 396, 495, 594, 693, 792, 891, 990],speed = [99, 99, 99, 99, 99, 99, 99, 99, 99, 99]) == 10
    assert candidate(dist = [3, 5, 7, 9, 11],speed = [1, 2, 3, 4, 5]) == 3
    assert candidate(dist = [10000, 20000, 30000, 40000, 50000],speed = [100, 200, 300, 400, 500]) == 5
    assert candidate(dist = [3, 6, 9, 12, 15],speed = [1, 1, 1, 1, 1]) == 5
    assert candidate(dist = [1, 2, 3, 4, 5],speed = [5, 4, 3, 2, 1]) == 1
    assert candidate(dist = [10, 20, 30, 40, 50],speed = [2, 4, 5, 6, 8]) == 5
    assert candidate(dist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(dist = [1000, 2000, 3000],speed = [10, 20, 30]) == 3
    assert candidate(dist = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3
    assert candidate(dist = [10, 25, 30, 45, 50, 65, 70, 85, 90, 105],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(dist = [2, 3, 4, 5, 6],speed = [1, 1, 1, 1, 1]) == 5
    assert candidate(dist = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(dist = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 15
    assert candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 10
    assert candidate(dist = [10, 20, 30, 40, 50],speed = [10, 20, 30, 40, 50]) == 1
    assert candidate(dist = [10, 20, 30, 40, 50],speed = [2, 2, 2, 2, 1]) == 5
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 1
    assert candidate(dist = [9, 9, 9, 9, 9],speed = [1, 2, 3, 4, 5]) == 5
    assert candidate(dist = [100, 150, 200, 250, 300],speed = [25, 50, 75, 100, 125]) == 3
    assert candidate(dist = [10, 20, 30, 40, 50],speed = [1, 2, 3, 4, 5]) == 5
    assert candidate(dist = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(dist = [10, 11, 12, 13, 14],speed = [1, 1, 1, 1, 1]) == 5
    assert candidate(dist = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(dist = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
    assert candidate(dist = [15, 10, 20, 30, 40],speed = [2, 5, 3, 4, 1]) == 5
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(dist = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(dist = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(dist = [100, 200, 300, 400, 500],speed = [50, 100, 150, 200, 250]) == 2
    assert candidate(dist = [3, 6, 9, 12, 15, 18],speed = [1, 2, 3, 4, 5, 6]) == 3
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
    assert candidate(dist = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(dist = [10, 20, 30, 40, 50],speed = [1, 2, 3, 4, 5]) == 5
    assert candidate(dist = [9, 18, 27, 36, 45],speed = [1, 2, 3, 4, 5]) == 5
    assert candidate(dist = [15, 25, 35, 45, 55],speed = [5, 5, 5, 5, 5]) == 5
    assert candidate(dist = [100, 200, 300, 400, 500],speed = [50, 50, 50, 50, 50]) == 5
    assert candidate(dist = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],speed = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
    assert candidate(dist = [2, 4, 6, 8, 10],speed = [2, 2, 2, 2, 2]) == 5
    assert candidate(dist = [7, 14, 21, 28, 35],speed = [1, 2, 3, 4, 5]) == 5
    assert candidate(dist = [100, 150, 200, 250, 300],speed = [5, 10, 15, 20, 25]) == 5
    assert candidate(dist = [100, 150, 200, 250, 300, 350, 400, 450, 500],speed = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 9


