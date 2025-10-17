def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(books = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1], [2, 2], [3, 3]],shelfWidth = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1], [2, 2], [3, 3]],shelfWidth = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(books = [[10, 1], [2, 2], [3, 3], [4, 4]],shelfWidth = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[10, 1], [2, 2], [3, 3], [4, 4]],shelfWidth = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(books = [[5, 5], [5, 5], [5, 5]],shelfWidth = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[5, 5], [5, 5], [5, 5]],shelfWidth = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(books = [[3, 1], [2, 2], [4, 3], [1, 4], [2, 5]],shelfWidth = 6) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[3, 1], [2, 2], [4, 3], [1, 4], [2, 5]],shelfWidth = 6) == 9: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]],shelfWidth = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]],shelfWidth = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 3], [2, 4], [3, 2]],shelfWidth = 6) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 3], [2, 4], [3, 2]],shelfWidth = 6) == 4: {e}')
    
    total += 1
    try:
        result = candidate(books = [[5, 5], [5, 5], [5, 5], [5, 5]],shelfWidth = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[5, 5], [5, 5], [5, 5], [5, 5]],shelfWidth = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1000], [1, 1000], [1, 1000]],shelfWidth = 3) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1000], [1, 1000], [1, 1000]],shelfWidth = 3) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(books = [[3, 1], [2, 2], [1, 3]],shelfWidth = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[3, 1], [2, 2], [1, 3]],shelfWidth = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 2], [2, 3], [3, 4], [4, 5]],shelfWidth = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 2], [2, 3], [3, 4], [4, 5]],shelfWidth = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(books = [[10, 1], [9, 1], [8, 1], [7, 1], [6, 1], [5, 1], [4, 1], [3, 1], [2, 1], [1, 1]],shelfWidth = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[10, 1], [9, 1], [8, 1], [7, 1], [6, 1], [5, 1], [4, 1], [3, 1], [2, 1], [1, 1]],shelfWidth = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(books = [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5]],shelfWidth = 15) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5]],shelfWidth = 15) == 10: {e}')
    
    total += 1
    try:
        result = candidate(books = [[10, 100], [5, 200], [5, 300], [10, 400], [5, 500], [5, 600], [10, 700], [10, 800], [5, 900], [5, 1000]],shelfWidth = 20) == 2200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[10, 100], [5, 200], [5, 300], [10, 400], [5, 500], [5, 600], [10, 700], [10, 800], [5, 900], [5, 1000]],shelfWidth = 20) == 2200: {e}')
    
    total += 1
    try:
        result = candidate(books = [[2, 1], [3, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]],shelfWidth = 5) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[2, 1], [3, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]],shelfWidth = 5) == 49: {e}')
    
    total += 1
    try:
        result = candidate(books = [[3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10]],shelfWidth = 10) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10]],shelfWidth = 10) == 21: {e}')
    
    total += 1
    try:
        result = candidate(books = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5], [5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],shelfWidth = 15) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5], [5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],shelfWidth = 15) == 10: {e}')
    
    total += 1
    try:
        result = candidate(books = [[500, 1], [500, 2], [500, 3], [500, 4], [500, 5], [500, 6], [500, 7], [500, 8], [500, 9], [500, 10], [500, 11], [500, 12], [500, 13], [500, 14], [500, 15]],shelfWidth = 1000) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[500, 1], [500, 2], [500, 3], [500, 4], [500, 5], [500, 6], [500, 7], [500, 8], [500, 9], [500, 10], [500, 11], [500, 12], [500, 13], [500, 14], [500, 15]],shelfWidth = 1000) == 64: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(books = [[300, 100], [300, 200], [300, 300], [100, 400], [100, 500], [100, 600], [100, 700]],shelfWidth = 600) == 1100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[300, 100], [300, 200], [300, 300], [100, 400], [100, 500], [100, 600], [100, 700]],shelfWidth = 600) == 1100: {e}')
    
    total += 1
    try:
        result = candidate(books = [[3, 1], [2, 5], [4, 7], [1, 2], [5, 3], [3, 4]],shelfWidth = 10) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[3, 1], [2, 5], [4, 7], [1, 2], [5, 3], [3, 4]],shelfWidth = 10) == 11: {e}')
    
    total += 1
    try:
        result = candidate(books = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5], [5, 1], [4, 2], [3, 3], [2, 4], [1, 5], [5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],shelfWidth = 10) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5], [5, 1], [4, 2], [3, 3], [2, 4], [1, 5], [5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],shelfWidth = 10) == 18: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],shelfWidth = 10) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],shelfWidth = 10) == 31: {e}')
    
    total += 1
    try:
        result = candidate(books = [[3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3]],shelfWidth = 6) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3]],shelfWidth = 6) == 15: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 500], [2, 500], [3, 500], [4, 500], [5, 500]],shelfWidth = 5) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 500], [2, 500], [3, 500], [4, 500], [5, 500]],shelfWidth = 5) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],shelfWidth = 10) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],shelfWidth = 10) == 48: {e}')
    
    total += 1
    try:
        result = candidate(books = [[10, 10], [9, 9], [8, 8], [7, 7], [6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]],shelfWidth = 20) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[10, 10], [9, 9], [8, 8], [7, 7], [6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]],shelfWidth = 20) == 25: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(books = [[100, 500], [99, 499], [98, 498], [97, 497], [96, 496], [95, 495]],shelfWidth = 300) == 997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[100, 500], [99, 499], [98, 498], [97, 497], [96, 496], [95, 495]],shelfWidth = 300) == 997: {e}')
    
    total += 1
    try:
        result = candidate(books = [[10, 100], [10, 100], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 20) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[10, 100], [10, 100], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 20) == 101: {e}')
    
    total += 1
    try:
        result = candidate(books = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],shelfWidth = 20) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],shelfWidth = 20) == 19: {e}')
    
    total += 1
    try:
        result = candidate(books = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11]],shelfWidth = 15) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11]],shelfWidth = 15) == 47: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 100], [2, 200], [3, 300], [4, 400], [5, 500], [6, 600], [7, 700], [8, 800], [9, 900], [10, 1000]],shelfWidth = 5) == 5300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 100], [2, 200], [3, 300], [4, 400], [5, 500], [6, 600], [7, 700], [8, 800], [9, 900], [10, 1000]],shelfWidth = 5) == 5300: {e}')
    
    total += 1
    try:
        result = candidate(books = [[2, 1], [3, 2], [4, 3], [5, 4], [6, 5]],shelfWidth = 12) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[2, 1], [3, 2], [4, 3], [5, 4], [6, 5]],shelfWidth = 12) == 8: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5]],shelfWidth = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5]],shelfWidth = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 500], [2, 500], [3, 500], [4, 500], [5, 500]],shelfWidth = 10) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 500], [2, 500], [3, 500], [4, 500], [5, 500]],shelfWidth = 10) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(books = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],shelfWidth = 15) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],shelfWidth = 15) == 21: {e}')
    
    total += 1
    try:
        result = candidate(books = [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10]],shelfWidth = 20) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10]],shelfWidth = 20) == 30: {e}')
    
    total += 1
    try:
        result = candidate(books = [[100, 100], [100, 200], [100, 300], [100, 400], [100, 500], [100, 600], [100, 700], [100, 800], [100, 900], [100, 1000]],shelfWidth = 300) == 2200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[100, 100], [100, 200], [100, 300], [100, 400], [100, 500], [100, 600], [100, 700], [100, 800], [100, 900], [100, 1000]],shelfWidth = 300) == 2200: {e}')
    
    total += 1
    try:
        result = candidate(books = [[5, 10], [10, 5], [15, 10], [20, 5], [25, 10], [30, 5], [35, 10], [40, 5], [45, 10], [50, 5]],shelfWidth = 50) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[5, 10], [10, 5], [15, 10], [20, 5], [25, 10], [30, 5], [35, 10], [40, 5], [45, 10], [50, 5]],shelfWidth = 50) == 55: {e}')
    
    total += 1
    try:
        result = candidate(books = [[100, 100], [90, 90], [80, 80], [70, 70], [60, 60], [50, 50], [40, 40], [30, 30], [20, 20], [10, 10]],shelfWidth = 100) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[100, 100], [90, 90], [80, 80], [70, 70], [60, 60], [50, 50], [40, 40], [30, 30], [20, 20], [10, 10]],shelfWidth = 100) == 480: {e}')
    
    total += 1
    try:
        result = candidate(books = [[500, 500], [500, 400], [300, 300], [200, 200], [100, 100]],shelfWidth = 1000) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[500, 500], [500, 400], [300, 300], [200, 200], [100, 100]],shelfWidth = 1000) == 800: {e}')
    
    total += 1
    try:
        result = candidate(books = [[2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10]],shelfWidth = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10]],shelfWidth = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],shelfWidth = 15) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],shelfWidth = 15) == 41: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13]],shelfWidth = 13) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13]],shelfWidth = 13) == 77: {e}')
    
    total += 1
    try:
        result = candidate(books = [[5, 1], [1, 5], [3, 3], [2, 2], [4, 4], [6, 6], [7, 7]],shelfWidth = 12) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[5, 1], [1, 5], [3, 3], [2, 2], [4, 4], [6, 6], [7, 7]],shelfWidth = 12) == 18: {e}')
    
    total += 1
    try:
        result = candidate(books = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],shelfWidth = 1000) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],shelfWidth = 1000) == 48: {e}')
    
    total += 1
    try:
        result = candidate(books = [[2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [1, 1]],shelfWidth = 15) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [1, 1]],shelfWidth = 15) == 30: {e}')
    
    total += 1
    try:
        result = candidate(books = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],shelfWidth = 15) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],shelfWidth = 15) == 22: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1000], [2, 999], [3, 998], [4, 997], [5, 996], [6, 995], [7, 994], [8, 993], [9, 992], [10, 991]],shelfWidth = 15) == 4971
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1000], [2, 999], [3, 998], [4, 997], [5, 996], [6, 995], [7, 994], [8, 993], [9, 992], [10, 991]],shelfWidth = 15) == 4971: {e}')
    
    total += 1
    try:
        result = candidate(books = [[7, 7], [7, 6], [7, 5], [7, 4], [7, 3], [7, 2], [7, 1]],shelfWidth = 14) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[7, 7], [7, 6], [7, 5], [7, 4], [7, 3], [7, 2], [7, 1]],shelfWidth = 14) == 16: {e}')
    
    total += 1
    try:
        result = candidate(books = [[10, 100], [20, 200], [30, 300], [40, 400], [50, 500], [60, 600], [70, 700], [80, 800], [90, 900]],shelfWidth = 150) == 2600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[10, 100], [20, 200], [30, 300], [40, 400], [50, 500], [60, 600], [70, 700], [80, 800], [90, 900]],shelfWidth = 150) == 2600: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],shelfWidth = 15) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],shelfWidth = 15) == 21: {e}')
    
    total += 1
    try:
        result = candidate(books = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],shelfWidth = 25) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],shelfWidth = 25) == 15: {e}')
    
    total += 1
    try:
        result = candidate(books = [[2, 10], [1, 5], [3, 15], [4, 20], [2, 8]],shelfWidth = 10) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[2, 10], [1, 5], [3, 15], [4, 20], [2, 8]],shelfWidth = 10) == 28: {e}')
    
    total += 1
    try:
        result = candidate(books = [[10, 5], [9, 4], [8, 3], [7, 2], [6, 1], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],shelfWidth = 20) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[10, 5], [9, 4], [8, 3], [7, 2], [6, 1], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],shelfWidth = 20) == 19: {e}')
    
    total += 1
    try:
        result = candidate(books = [[7, 3], [8, 4], [6, 5], [5, 6], [9, 7], [10, 8], [8, 9]],shelfWidth = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[7, 3], [8, 4], [6, 5], [5, 6], [9, 7], [10, 8], [8, 9]],shelfWidth = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 100], [2, 200], [3, 300], [4, 400], [5, 500], [6, 600], [7, 700], [8, 800], [9, 900], [10, 1000]],shelfWidth = 10) == 4800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 100], [2, 200], [3, 300], [4, 400], [5, 500], [6, 600], [7, 700], [8, 800], [9, 900], [10, 1000]],shelfWidth = 10) == 4800: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1000], [2, 999], [3, 998], [4, 997], [5, 996], [6, 995], [7, 994], [8, 993], [9, 992], [10, 991]],shelfWidth = 10) == 6961
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1000], [2, 999], [3, 998], [4, 997], [5, 996], [6, 995], [7, 994], [8, 993], [9, 992], [10, 991]],shelfWidth = 10) == 6961: {e}')
    
    total += 1
    try:
        result = candidate(books = [[250, 500], [500, 250], [250, 750], [750, 250], [500, 500], [500, 500], [250, 250], [250, 250], [250, 250], [250, 250]],shelfWidth = 1000) == 1750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[250, 500], [500, 250], [250, 750], [750, 250], [500, 500], [500, 500], [250, 250], [250, 250], [250, 250], [250, 250]],shelfWidth = 1000) == 1750: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],shelfWidth = 15) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],shelfWidth = 15) == 36: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],shelfWidth = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],shelfWidth = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(books = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],shelfWidth = 60) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],shelfWidth = 60) == 120: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],shelfWidth = 15) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],shelfWidth = 15) == 17: {e}')
    
    total += 1
    try:
        result = candidate(books = [[5, 10], [4, 20], [3, 30], [2, 40], [1, 50], [5, 10], [4, 20], [3, 30], [2, 40], [1, 50]],shelfWidth = 15) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[5, 10], [4, 20], [3, 30], [2, 40], [1, 50], [5, 10], [4, 20], [3, 30], [2, 40], [1, 50]],shelfWidth = 15) == 100: {e}')
    
    total += 1
    try:
        result = candidate(books = [[7, 8], [6, 7], [5, 6], [4, 5], [3, 4], [2, 3], [1, 2]],shelfWidth = 10) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[7, 8], [6, 7], [5, 6], [4, 5], [3, 4], [2, 3], [1, 2]],shelfWidth = 10) == 25: {e}')
    
    total += 1
    try:
        result = candidate(books = [[3, 10], [2, 5], [1, 20], [4, 1], [5, 30], [3, 20], [2, 10], [1, 5], [4, 25], [5, 15]],shelfWidth = 10) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[3, 10], [2, 5], [1, 20], [4, 1], [5, 30], [3, 20], [2, 10], [1, 5], [4, 25], [5, 15]],shelfWidth = 10) == 75: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],shelfWidth = 1) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],shelfWidth = 1) == 55: {e}')
    
    total += 1
    try:
        result = candidate(books = [[5, 10], [4, 8], [3, 6], [2, 4], [1, 2], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10]],shelfWidth = 10) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[5, 10], [4, 8], [3, 6], [2, 4], [1, 2], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10]],shelfWidth = 10) == 32: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1000, 1], [1000, 2], [1000, 3], [1000, 4], [1000, 5], [1000, 6], [1000, 7], [1000, 8], [1000, 9], [1000, 10]],shelfWidth = 1000) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1000, 1], [1000, 2], [1000, 3], [1000, 4], [1000, 5], [1000, 6], [1000, 7], [1000, 8], [1000, 9], [1000, 10]],shelfWidth = 1000) == 55: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 500], [2, 400], [3, 300], [4, 200], [5, 100]],shelfWidth = 15) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 500], [2, 400], [3, 300], [4, 200], [5, 100]],shelfWidth = 15) == 500: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],shelfWidth = 15) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],shelfWidth = 15) == 10: {e}')
    
    total += 1
    try:
        result = candidate(books = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],shelfWidth = 150) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],shelfWidth = 150) == 36: {e}')
    
    total += 1
    try:
        result = candidate(books = [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5]],shelfWidth = 15) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5]],shelfWidth = 15) == 20: {e}')
    
    total += 1
    try:
        result = candidate(books = [[3, 1], [1, 2], [1, 3], [3, 4], [2, 5], [1, 1], [2, 2], [3, 3], [1, 1]],shelfWidth = 5) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[3, 1], [1, 2], [1, 3], [3, 4], [2, 5], [1, 1], [2, 2], [3, 3], [1, 1]],shelfWidth = 5) == 13: {e}')
    
    total += 1
    try:
        result = candidate(books = [[2, 1], [1, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],shelfWidth = 15) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[2, 1], [1, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],shelfWidth = 15) == 36: {e}')
    
    total += 1
    try:
        result = candidate(books = [[3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10]],shelfWidth = 10) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10]],shelfWidth = 10) == 22: {e}')
    
    total += 1
    try:
        result = candidate(books = [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10]],shelfWidth = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10]],shelfWidth = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(books = [[100, 1], [90, 2], [80, 3], [70, 4], [60, 5], [50, 6], [40, 7], [30, 8], [20, 9], [10, 10]],shelfWidth = 150) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[100, 1], [90, 2], [80, 3], [70, 4], [60, 5], [50, 6], [40, 7], [30, 8], [20, 9], [10, 10]],shelfWidth = 150) == 21: {e}')
    
    total += 1
    try:
        result = candidate(books = [[5, 2], [3, 5], [4, 1], [6, 3], [2, 8], [1, 4], [7, 6]],shelfWidth = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[5, 2], [3, 5], [4, 1], [6, 3], [2, 8], [1, 4], [7, 6]],shelfWidth = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],shelfWidth = 5) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],shelfWidth = 5) == 53: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1000], [2, 900], [3, 800], [4, 700], [5, 600], [6, 500], [7, 400], [8, 300], [9, 200], [10, 100]],shelfWidth = 15) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1000], [2, 900], [3, 800], [4, 700], [5, 600], [6, 500], [7, 400], [8, 300], [9, 200], [10, 100]],shelfWidth = 15) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 999], [2, 998], [3, 997], [4, 996], [5, 995], [6, 994], [7, 993], [8, 992], [9, 991], [10, 990]],shelfWidth = 1500) == 999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 999], [2, 998], [3, 997], [4, 996], [5, 995], [6, 994], [7, 993], [8, 992], [9, 991], [10, 990]],shelfWidth = 1500) == 999: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 200], [1, 100], [1, 150], [1, 50], [1, 250], [1, 100]],shelfWidth = 2) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 200], [1, 100], [1, 150], [1, 50], [1, 250], [1, 100]],shelfWidth = 2) == 600: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],shelfWidth = 10) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],shelfWidth = 10) == 29: {e}')
    
    total += 1
    try:
        result = candidate(books = [[5, 10], [10, 5], [5, 5], [5, 10], [10, 5], [5, 5], [5, 10], [10, 5], [5, 5]],shelfWidth = 15) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[5, 10], [10, 5], [5, 5], [5, 10], [10, 5], [5, 5], [5, 10], [10, 5], [5, 5]],shelfWidth = 15) == 40: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 3], [2, 4], [3, 2], [4, 1], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],shelfWidth = 12) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 3], [2, 4], [3, 2], [4, 1], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],shelfWidth = 12) == 44: {e}')
    
    total += 1
    try:
        result = candidate(books = [[3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],shelfWidth = 20) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],shelfWidth = 20) == 23: {e}')
    
    total += 1
    try:
        result = candidate(books = [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5]],shelfWidth = 10) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5]],shelfWidth = 10) == 25: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]],shelfWidth = 10) == 113
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]],shelfWidth = 10) == 113: {e}')
    
    total += 1
    try:
        result = candidate(books = [[2, 10], [3, 9], [4, 8], [5, 7], [6, 6], [7, 5], [8, 4], [9, 3], [10, 2]],shelfWidth = 15) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[2, 10], [3, 9], [4, 8], [5, 7], [6, 6], [7, 5], [8, 4], [9, 3], [10, 2]],shelfWidth = 15) == 25: {e}')
    
    total += 1
    try:
        result = candidate(books = [[3, 5], [2, 8], [1, 7], [4, 4], [5, 6], [6, 3], [7, 2], [8, 9]],shelfWidth = 12) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[3, 5], [2, 8], [1, 7], [4, 4], [5, 6], [6, 3], [7, 2], [8, 9]],shelfWidth = 12) == 25: {e}')
    
    total += 1
    try:
        result = candidate(books = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],shelfWidth = 20) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],shelfWidth = 20) == 30: {e}')
    
    total += 1
    try:
        result = candidate(books = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],shelfWidth = 20) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],shelfWidth = 20) == 18: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000]],shelfWidth = 3) == 7000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000]],shelfWidth = 3) == 7000: {e}')
    
    total += 1
    try:
        result = candidate(books = [[50, 50], [100, 100], [150, 150], [200, 200], [250, 250], [300, 300], [350, 350], [400, 400], [450, 450], [500, 500]],shelfWidth = 1000) == 1250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[50, 50], [100, 100], [150, 150], [200, 200], [250, 250], [300, 300], [350, 350], [400, 400], [450, 450], [500, 500]],shelfWidth = 1000) == 1250: {e}')
    
    total += 1
    try:
        result = candidate(books = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],shelfWidth = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],shelfWidth = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(books = [[7, 8], [6, 9], [5, 10], [4, 11], [3, 12], [2, 13], [1, 14]],shelfWidth = 20) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(books = [[7, 8], [6, 9], [5, 10], [4, 11], [3, 12], [2, 13], [1, 14]],shelfWidth = 20) == 23: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(books = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 1) == 10
    assert candidate(books = [[1, 1], [2, 2], [3, 3]],shelfWidth = 5) == 4
    assert candidate(books = [[10, 1], [2, 2], [3, 3], [4, 4]],shelfWidth = 10) == 5
    assert candidate(books = [[5, 5], [5, 5], [5, 5]],shelfWidth = 10) == 10
    assert candidate(books = [[3, 1], [2, 2], [4, 3], [1, 4], [2, 5]],shelfWidth = 6) == 9
    assert candidate(books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]],shelfWidth = 4) == 6
    assert candidate(books = [[1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 2) == 2
    assert candidate(books = [[1, 3], [2, 4], [3, 2]],shelfWidth = 6) == 4
    assert candidate(books = [[5, 5], [5, 5], [5, 5], [5, 5]],shelfWidth = 10) == 10
    assert candidate(books = [[1, 1000], [1, 1000], [1, 1000]],shelfWidth = 3) == 1000
    assert candidate(books = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 1) == 5
    assert candidate(books = [[3, 1], [2, 2], [1, 3]],shelfWidth = 5) == 4
    assert candidate(books = [[1, 2], [2, 3], [3, 4], [4, 5]],shelfWidth = 10) == 5
    assert candidate(books = [[10, 1], [9, 1], [8, 1], [7, 1], [6, 1], [5, 1], [4, 1], [3, 1], [2, 1], [1, 1]],shelfWidth = 10) == 7
    assert candidate(books = [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5]],shelfWidth = 15) == 10
    assert candidate(books = [[10, 100], [5, 200], [5, 300], [10, 400], [5, 500], [5, 600], [10, 700], [10, 800], [5, 900], [5, 1000]],shelfWidth = 20) == 2200
    assert candidate(books = [[2, 1], [3, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]],shelfWidth = 5) == 49
    assert candidate(books = [[3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10]],shelfWidth = 10) == 21
    assert candidate(books = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5], [5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],shelfWidth = 15) == 10
    assert candidate(books = [[500, 1], [500, 2], [500, 3], [500, 4], [500, 5], [500, 6], [500, 7], [500, 8], [500, 9], [500, 10], [500, 11], [500, 12], [500, 13], [500, 14], [500, 15]],shelfWidth = 1000) == 64
    assert candidate(books = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 1) == 15
    assert candidate(books = [[300, 100], [300, 200], [300, 300], [100, 400], [100, 500], [100, 600], [100, 700]],shelfWidth = 600) == 1100
    assert candidate(books = [[3, 1], [2, 5], [4, 7], [1, 2], [5, 3], [3, 4]],shelfWidth = 10) == 11
    assert candidate(books = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5], [5, 1], [4, 2], [3, 3], [2, 4], [1, 5], [5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],shelfWidth = 10) == 18
    assert candidate(books = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],shelfWidth = 10) == 31
    assert candidate(books = [[3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3]],shelfWidth = 6) == 15
    assert candidate(books = [[1, 500], [2, 500], [3, 500], [4, 500], [5, 500]],shelfWidth = 5) == 2000
    assert candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],shelfWidth = 10) == 48
    assert candidate(books = [[10, 10], [9, 9], [8, 8], [7, 7], [6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]],shelfWidth = 20) == 25
    assert candidate(books = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 3) == 4
    assert candidate(books = [[100, 500], [99, 499], [98, 498], [97, 497], [96, 496], [95, 495]],shelfWidth = 300) == 997
    assert candidate(books = [[10, 100], [10, 100], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 20) == 101
    assert candidate(books = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],shelfWidth = 20) == 19
    assert candidate(books = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11]],shelfWidth = 15) == 47
    assert candidate(books = [[1, 100], [2, 200], [3, 300], [4, 400], [5, 500], [6, 600], [7, 700], [8, 800], [9, 900], [10, 1000]],shelfWidth = 5) == 5300
    assert candidate(books = [[2, 1], [3, 2], [4, 3], [5, 4], [6, 5]],shelfWidth = 12) == 8
    assert candidate(books = [[1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5], [1, 5]],shelfWidth = 5) == 15
    assert candidate(books = [[1, 500], [2, 500], [3, 500], [4, 500], [5, 500]],shelfWidth = 10) == 1000
    assert candidate(books = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],shelfWidth = 15) == 21
    assert candidate(books = [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10]],shelfWidth = 20) == 30
    assert candidate(books = [[100, 100], [100, 200], [100, 300], [100, 400], [100, 500], [100, 600], [100, 700], [100, 800], [100, 900], [100, 1000]],shelfWidth = 300) == 2200
    assert candidate(books = [[5, 10], [10, 5], [15, 10], [20, 5], [25, 10], [30, 5], [35, 10], [40, 5], [45, 10], [50, 5]],shelfWidth = 50) == 55
    assert candidate(books = [[100, 100], [90, 90], [80, 80], [70, 70], [60, 60], [50, 50], [40, 40], [30, 30], [20, 20], [10, 10]],shelfWidth = 100) == 480
    assert candidate(books = [[500, 500], [500, 400], [300, 300], [200, 200], [100, 100]],shelfWidth = 1000) == 800
    assert candidate(books = [[2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10]],shelfWidth = 5) == 30
    assert candidate(books = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],shelfWidth = 15) == 41
    assert candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13]],shelfWidth = 13) == 77
    assert candidate(books = [[5, 1], [1, 5], [3, 3], [2, 2], [4, 4], [6, 6], [7, 7]],shelfWidth = 12) == 18
    assert candidate(books = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],shelfWidth = 1000) == 48
    assert candidate(books = [[2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [1, 1]],shelfWidth = 15) == 30
    assert candidate(books = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],shelfWidth = 15) == 22
    assert candidate(books = [[1, 1000], [2, 999], [3, 998], [4, 997], [5, 996], [6, 995], [7, 994], [8, 993], [9, 992], [10, 991]],shelfWidth = 15) == 4971
    assert candidate(books = [[7, 7], [7, 6], [7, 5], [7, 4], [7, 3], [7, 2], [7, 1]],shelfWidth = 14) == 16
    assert candidate(books = [[10, 100], [20, 200], [30, 300], [40, 400], [50, 500], [60, 600], [70, 700], [80, 800], [90, 900]],shelfWidth = 150) == 2600
    assert candidate(books = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],shelfWidth = 15) == 21
    assert candidate(books = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],shelfWidth = 25) == 15
    assert candidate(books = [[2, 10], [1, 5], [3, 15], [4, 20], [2, 8]],shelfWidth = 10) == 28
    assert candidate(books = [[10, 5], [9, 4], [8, 3], [7, 2], [6, 1], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],shelfWidth = 20) == 19
    assert candidate(books = [[7, 3], [8, 4], [6, 5], [5, 6], [9, 7], [10, 8], [8, 9]],shelfWidth = 20) == 20
    assert candidate(books = [[1, 100], [2, 200], [3, 300], [4, 400], [5, 500], [6, 600], [7, 700], [8, 800], [9, 900], [10, 1000]],shelfWidth = 10) == 4800
    assert candidate(books = [[1, 1000], [2, 999], [3, 998], [4, 997], [5, 996], [6, 995], [7, 994], [8, 993], [9, 992], [10, 991]],shelfWidth = 10) == 6961
    assert candidate(books = [[250, 500], [500, 250], [250, 750], [750, 250], [500, 500], [500, 500], [250, 250], [250, 250], [250, 250], [250, 250]],shelfWidth = 1000) == 1750
    assert candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],shelfWidth = 15) == 36
    assert candidate(books = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],shelfWidth = 5) == 15
    assert candidate(books = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],shelfWidth = 60) == 120
    assert candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],shelfWidth = 15) == 17
    assert candidate(books = [[5, 10], [4, 20], [3, 30], [2, 40], [1, 50], [5, 10], [4, 20], [3, 30], [2, 40], [1, 50]],shelfWidth = 15) == 100
    assert candidate(books = [[7, 8], [6, 7], [5, 6], [4, 5], [3, 4], [2, 3], [1, 2]],shelfWidth = 10) == 25
    assert candidate(books = [[3, 10], [2, 5], [1, 20], [4, 1], [5, 30], [3, 20], [2, 10], [1, 5], [4, 25], [5, 15]],shelfWidth = 10) == 75
    assert candidate(books = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],shelfWidth = 1) == 55
    assert candidate(books = [[5, 10], [4, 8], [3, 6], [2, 4], [1, 2], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10]],shelfWidth = 10) == 32
    assert candidate(books = [[1000, 1], [1000, 2], [1000, 3], [1000, 4], [1000, 5], [1000, 6], [1000, 7], [1000, 8], [1000, 9], [1000, 10]],shelfWidth = 1000) == 55
    assert candidate(books = [[1, 500], [2, 400], [3, 300], [4, 200], [5, 100]],shelfWidth = 15) == 500
    assert candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],shelfWidth = 15) == 10
    assert candidate(books = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],shelfWidth = 150) == 36
    assert candidate(books = [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5]],shelfWidth = 15) == 20
    assert candidate(books = [[3, 1], [1, 2], [1, 3], [3, 4], [2, 5], [1, 1], [2, 2], [3, 3], [1, 1]],shelfWidth = 5) == 13
    assert candidate(books = [[2, 1], [1, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],shelfWidth = 15) == 36
    assert candidate(books = [[3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10]],shelfWidth = 10) == 22
    assert candidate(books = [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10]],shelfWidth = 10) == 55
    assert candidate(books = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],shelfWidth = 5) == 2
    assert candidate(books = [[100, 1], [90, 2], [80, 3], [70, 4], [60, 5], [50, 6], [40, 7], [30, 8], [20, 9], [10, 10]],shelfWidth = 150) == 21
    assert candidate(books = [[5, 2], [3, 5], [4, 1], [6, 3], [2, 8], [1, 4], [7, 6]],shelfWidth = 15) == 15
    assert candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],shelfWidth = 5) == 53
    assert candidate(books = [[1, 1000], [2, 900], [3, 800], [4, 700], [5, 600], [6, 500], [7, 400], [8, 300], [9, 200], [10, 100]],shelfWidth = 15) == 2100
    assert candidate(books = [[1, 999], [2, 998], [3, 997], [4, 996], [5, 995], [6, 994], [7, 993], [8, 992], [9, 991], [10, 990]],shelfWidth = 1500) == 999
    assert candidate(books = [[1, 200], [1, 100], [1, 150], [1, 50], [1, 250], [1, 100]],shelfWidth = 2) == 600
    assert candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],shelfWidth = 10) == 29
    assert candidate(books = [[5, 10], [10, 5], [5, 5], [5, 10], [10, 5], [5, 5], [5, 10], [10, 5], [5, 5]],shelfWidth = 15) == 40
    assert candidate(books = [[1, 3], [2, 4], [3, 2], [4, 1], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],shelfWidth = 12) == 44
    assert candidate(books = [[3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],shelfWidth = 20) == 23
    assert candidate(books = [[5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5]],shelfWidth = 10) == 25
    assert candidate(books = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]],shelfWidth = 10) == 113
    assert candidate(books = [[2, 10], [3, 9], [4, 8], [5, 7], [6, 6], [7, 5], [8, 4], [9, 3], [10, 2]],shelfWidth = 15) == 25
    assert candidate(books = [[3, 5], [2, 8], [1, 7], [4, 4], [5, 6], [6, 3], [7, 2], [8, 9]],shelfWidth = 12) == 25
    assert candidate(books = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],shelfWidth = 20) == 30
    assert candidate(books = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]],shelfWidth = 20) == 18
    assert candidate(books = [[1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000], [1, 1000]],shelfWidth = 3) == 7000
    assert candidate(books = [[50, 50], [100, 100], [150, 150], [200, 200], [250, 250], [300, 300], [350, 350], [400, 400], [450, 450], [500, 500]],shelfWidth = 1000) == 1250
    assert candidate(books = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],shelfWidth = 10) == 10
    assert candidate(books = [[7, 8], [6, 9], [5, 10], [4, 11], [3, 12], [2, 13], [1, 14]],shelfWidth = 20) == 23


