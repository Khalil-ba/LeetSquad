def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 100, 100, 100, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 100, 100, 100, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 50, 50, 50, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 50, 50, 50, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [99, 100, 101]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [99, 100, 101]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 100, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 100, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 99, 98, 97, 96]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 99, 98, 97, 96]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [101, 102, 103, 104, 105]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [101, 102, 103, 104, 105]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [99, 1, 99, 1, 99, 1, 99, 1, 99, 1, 99, 1, 99, 1, 99, 1, 99, 1, 99, 1]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [99, 1, 99, 1, 99, 1, 99, 1, 99, 1, 99, 1, 99, 1, 99, 1, 99, 1, 99, 1]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 462
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 462: {e}')
    
    total += 1
    try:
        result = candidate(arr = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [97, 2, 83, 4, 81, 6, 79, 8, 77, 10, 75, 12, 73, 14, 71, 16, 69, 18, 67, 20]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [97, 2, 83, 4, 81, 6, 79, 8, 77, 10, 75, 12, 73, 14, 71, 16, 69, 18, 67, 20]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(arr = [99, 199, 299, 399, 499, 599, 699, 799, 899, 999]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [99, 199, 299, 399, 499, 599, 699, 799, 899, 999]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [97, 98, 99, 100, 1, 2, 3, 4, 5, 6]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [97, 98, 99, 100, 1, 2, 3, 4, 5, 6]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]) == 98: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(arr = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(arr = [99, 100, 98, 97, 101, 96, 102, 95, 103, 94, 104, 93, 105, 92, 106]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [99, 100, 98, 97, 101, 96, 102, 95, 103, 94, 104, 93, 105, 92, 106]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [101, 201, 301, 401, 501, 601, 701, 801, 901, 1001]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [101, 201, 301, 401, 501, 601, 701, 801, 901, 1001]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 310: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 99, 1, 2, 98, 3, 4, 97, 5, 6]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 99, 1, 2, 98, 3, 4, 97, 5, 6]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 5, 3, 7, 4, 9, 5, 11, 6, 13, 7, 15, 8, 17, 9, 19, 10, 21]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 5, 3, 7, 4, 9, 5, 11, 6, 13, 7, 15, 8, 17, 9, 19, 10, 21]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 420: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0]) == 28: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [2, 4, 6, 8, 10]) == 0
    assert candidate(arr = [100, 100, 100, 100, 100]) == 0
    assert candidate(arr = [50, 50, 50, 50, 50]) == 0
    assert candidate(arr = [1, 2, 3]) == 4
    assert candidate(arr = [2, 2, 2, 2, 2]) == 0
    assert candidate(arr = [1, 2]) == 2
    assert candidate(arr = [99, 100, 101]) == 4
    assert candidate(arr = [100, 100, 100]) == 0
    assert candidate(arr = [2, 4, 6]) == 0
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7]) == 16
    assert candidate(arr = [1]) == 1
    assert candidate(arr = [1, 1, 1, 1, 1]) == 9
    assert candidate(arr = [100, 99, 98, 97, 96]) == 8
    assert candidate(arr = [101, 102, 103, 104, 105]) == 9
    assert candidate(arr = [1, 2, 3, 4, 5]) == 9
    assert candidate(arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 24
    assert candidate(arr = [2]) == 0
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4]) == 14
    assert candidate(arr = [1, 3, 5]) == 4
    assert candidate(arr = [97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78]) == 110
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 0
    assert candidate(arr = [99, 1, 99, 1, 99, 1, 99, 1, 99, 1, 99, 1, 99, 1, 99, 1, 99, 1, 99, 1]) == 110
    assert candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 462
    assert candidate(arr = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 30
    assert candidate(arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 30
    assert candidate(arr = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 30
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 64
    assert candidate(arr = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5]) == 30
    assert candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15]) == 20
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 30
    assert candidate(arr = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 30
    assert candidate(arr = [97, 2, 83, 4, 81, 6, 79, 8, 77, 10, 75, 12, 73, 14, 71, 16, 69, 18, 67, 20]) == 110
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 110
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 0
    assert candidate(arr = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 110
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 30
    assert candidate(arr = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 0
    assert candidate(arr = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 64
    assert candidate(arr = [99, 199, 299, 399, 499, 599, 699, 799, 899, 999]) == 30
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 0
    assert candidate(arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 63
    assert candidate(arr = [1, 3, 5, 7, 9, 11]) == 12
    assert candidate(arr = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 30
    assert candidate(arr = [97, 98, 99, 100, 1, 2, 3, 4, 5, 6]) == 30
    assert candidate(arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 30
    assert candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]) == 60
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 10
    assert candidate(arr = [50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51]) == 110
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 240
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
    assert candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 240
    assert candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == 28
    assert candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 240
    assert candidate(arr = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]) == 0
    assert candidate(arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 110
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 0
    assert candidate(arr = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]) == 36
    assert candidate(arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]) == 98
    assert candidate(arr = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 0
    assert candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 110
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 110
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 0
    assert candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 63
    assert candidate(arr = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 110
    assert candidate(arr = [99, 100, 98, 97, 101, 96, 102, 95, 103, 94, 104, 93, 105, 92, 106]) == 48
    assert candidate(arr = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36]) == 64
    assert candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 30
    assert candidate(arr = [101, 201, 301, 401, 501, 601, 701, 801, 901, 1001]) == 30
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 64
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
    assert candidate(arr = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 110
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 0
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 64
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]) == 0
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 310
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 52
    assert candidate(arr = [100, 99, 1, 2, 98, 3, 4, 97, 5, 6]) == 30
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 110
    assert candidate(arr = [1, 3, 2, 5, 3, 7, 4, 9, 5, 11, 6, 13, 7, 15, 8, 17, 9, 19, 10, 21]) == 110
    assert candidate(arr = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 110
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 420
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 15
    assert candidate(arr = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100]) == 0
    assert candidate(arr = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0]) == 28


