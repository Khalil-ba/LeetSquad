def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 8, 16]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 8, 16]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 9, 15]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 9, 15]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 9]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 9]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 10]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 10]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 9, 15, 18]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 9, 15, 18]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 500]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 500]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 2, 4, 8, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 2, 4, 8, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 14, 21, 35]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 14, 21, 35]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 6, 4, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 6, 4, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 10]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 10]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 8, 10, 12]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 8, 10, 12]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 2, 4, 8]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 2, 4, 8]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 50]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 50]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 500, 600]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 500, 600]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 7, 11, 13]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 7, 11, 13]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 2, 4, 6, 10]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 2, 4, 6, 10]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 7, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 7, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 14, 21, 35, 42]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 14, 21, 35, 42]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 12]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 12]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [15, 13, 12]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [15, 13, 12]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 25]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 25]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 25, 30]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 25, 30]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 13, 19, 25, 37, 43, 49]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 13, 19, 25, 37, 43, 49]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 11, 17, 23, 29, 35, 47, 53]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 11, 17, 23, 29, 35, 47, 53]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 11, 15, 19, 27, 31, 35]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 11, 15, 19, 27, 31, 35]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-20, -15, -10, -5, -1, 5, 10, 15, 20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-20, -15, -10, -5, -1, 5, 10, 15, 20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 100]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 100]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 50, 70]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 50, 70]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 70, 80, 90, 100]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 70, 80, 90, 100]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 11, 15, 19, 27, 31, 35]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 11, 15, 19, 27, 31, 35]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 8, 14, 20, 32, 38]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 8, 14, 20, 32, 38]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(arr = [12, 24, 36, 48, 60, 72, 84]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [12, 24, 36, 48, 60, 72, 84]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 30, 40, 45, 50, 55]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 30, 40, 45, 50, 55]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 8, 12, 20, 24, 28, 32]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 8, 12, 20, 24, 28, 32]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 9, 11]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 9, 11]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 8, 12, 16, 20, 24, 28, 32, 36]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 8, 12, 16, 20, 24, 28, 32, 36]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [12, 18, 24, 36, 42, 48]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [12, 18, 24, 36, 42, 48]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 57]) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 57]) == 53: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 500, 600, 700, 800, 900]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 500, 600, 700, 800, 900]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 7, 10, 19, 22, 25, 28]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 7, 10, 19, 22, 25, 28]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 20, 25, 30]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 20, 25, 30]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 7, 13, 16]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 7, 13, 16]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [25, 50, 75, 100, 150, 200, 225]) == 175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [25, 50, 75, 100, 150, 200, 225]) == 175: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 16, 24, 32, 40, 48, 64, 72, 80, 88, 96]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 16, 24, 32, 40, 48, 64, 72, 80, 88, 96]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 12, 18, 24, 30, 36, 42]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 12, 18, 24, 30, 36, 42]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(arr = [15, 30, 45, 60, 75, 90, 105, 120, 150, 165, 180, 195, 210]) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [15, 30, 45, 60, 75, 90, 105, 120, 150, 165, 180, 195, 210]) == 135: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 90, 80, 60, 50]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 90, 80, 60, 50]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 7, 10, 13, 19]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 7, 10, 13, 19]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 12, 14, 16]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 12, 14, 16]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, 950, 900, 800, 750]) == 850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, 950, 900, 800, 750]) == 850: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 106, 112, 124, 130, 136]) == 118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 106, 112, 124, 130, 136]) == 118: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 70, 80, 90]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 70, 80, 90]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 15]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 15]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 7, 10, 13, 19, 22]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 7, 10, 13, 19, 22]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(arr = [11, 22, 33, 44, 55, 66, 88, 99]) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [11, 22, 33, 44, 55, 66, 88, 99]) == 77: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 12, 18, 24, 36, 42, 48]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 12, 18, 24, 36, 42, 48]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 50, 60, 70]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 50, 60, 70]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 9, 12, 15, 21, 24, 27, 30, 33]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 9, 12, 15, 21, 24, 27, 30, 33]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 16, 24, 32, 48, 56, 64]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 16, 24, 32, 48, 56, 64]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 9, 13, 17, 25, 29]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 9, 13, 17, 25, 29]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 9, 12, 18, 21, 24]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 9, 12, 18, 21, 24]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [99, 198, 297, 396, 495, 594, 792, 891]) == 693
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [99, 198, 297, 396, 495, 594, 792, 891]) == 693: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 30, 35, 40, 45, 50, 55]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 30, 35, 40, 45, 50, 55]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 25, 35, 40, 45, 50]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 25, 35, 40, 45, 50]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 8, 11, 17, 20, 23, 26, 29]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 8, 11, 17, 20, 23, 26, 29]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [45, 90, 135, 180, 270, 315, 360]) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [45, 90, 135, 180, 270, 315, 360]) == 225: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 50, 60]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 50, 60]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 16, 18, 20]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 16, 18, 20]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 14, 20, 32, 38, 44]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 14, 20, 32, 38, 44]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 9, 15, 21, 33, 39, 45]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 9, 15, 21, 33, 39, 45]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(arr = [20, 40, 60, 80, 100, 120, 160, 180, 200]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [20, 40, 60, 80, 100, 120, 160, 180, 200]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 16, 24, 32, 40, 56, 64]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 16, 24, 32, 40, 56, 64]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(arr = [77, 88, 99, 121, 132, 143, 154]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [77, 88, 99, 121, 132, 143, 154]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(arr = [12, 18, 24, 30, 36, 48, 54]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [12, 18, 24, 30, 36, 48, 54]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 500, 700, 900]) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 500, 700, 900]) == 800: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 5, 10, 15, 20, 30, 35, 40, 45, 50]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 5, 10, 15, 20, 30, 35, 40, 45, 50]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 80, 90, 100]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 80, 90, 100]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 14, 21, 28, 42, 49, 56, 63]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 14, 21, 28, 42, 49, 56, 63]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 70, 80, 90, 100, 110, 120]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 70, 80, 90, 100, 110, 120]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 500, 600]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 500, 600]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 9, 15, 21, 27, 33, 39, 45]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 9, 15, 21, 27, 33, 39, 45]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 15, 20, 25, 35, 40, 45]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 15, 20, 25, 35, 40, 45]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [25, 35, 45, 55, 65, 85]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [25, 35, 45, 55, 65, 85]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 20, 30]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 20, 30]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 5, 6, 7, 8]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 5, 6, 7, 8]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 11, 13, 15, 17, 19]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 11, 13, 15, 17, 19]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [15, 30, 45, 60, 75, 90, 120, 135, 150]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [15, 30, 45, 60, 75, 90, 120, 135, 150]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 25, 30, 35, 40]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 25, 30, 35, 40]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, 2000, 3000, 4000, 5000, 7000, 8000, 9000, 10000]) == 6000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, 2000, 3000, 4000, 5000, 7000, 8000, 9000, 10000]) == 6000: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, 900, 800, 700, 600, 500, 300, 200]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, 900, 800, 700, 600, 500, 300, 200]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 150, 200, 250, 350, 400]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 150, 200, 250, 350, 400]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(arr = [11, 22, 33, 44, 55, 77, 88]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [11, 22, 33, 44, 55, 77, 88]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 15, 25, 35, 45, 65]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 15, 25, 35, 45, 65]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 50, 70]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 50, 70]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 9, 11, 13]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 9, 11, 13]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 7, 10, 13, 19, 22, 25, 28, 31]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 7, 10, 13, 19, 22, 25, 28, 31]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 17, 27, 37, 47, 57, 67]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 17, 27, 37, 47, 57, 67]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 8, 10, 12, 14, 16]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 8, 10, 12, 14, 16]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 14, 16, 18]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 14, 16, 18]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr = [12, 14, 16, 18, 22, 24, 26]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [12, 14, 16, 18, 22, 24, 26]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 500, 600, 700]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 500, 600, 700]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 9, 15, 21, 27, 39, 45]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 9, 15, 21, 27, 39, 45]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 55]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 55]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 12, 15, 18, 21, 24, 27]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 12, 15, 18, 21, 24, 27]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 25, 40, 60, 75]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 25, 40, 60, 75]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 16, 24, 32, 40, 48, 56]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 16, 24, 32, 40, 48, 56]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 11, 15, 19, 27, 31, 35, 39]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 11, 15, 19, 27, 31, 35, 39]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 18, 27, 36, 45, 63, 72]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 18, 27, 36, 45, 63, 72]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 5, 6, 7, 8]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 5, 6, 7, 8]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 17, 19, 21, 23, 25, 27]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 17, 19, 21, 23, 25, 27]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 9, 11, 13, 15]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 9, 11, 13, 15]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 600, 700, 800]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 600, 700, 800]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 15, 20, 25, 35, 40, 45]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 15, 20, 25, 35, 40, 45]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 15, 17, 19]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 15, 17, 19]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 5, 8, 11, 14, 17, 20, 26]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 5, 8, 11, 14, 17, 20, 26]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 4, 5, 6, 7, 8, 9]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 4, 5, 6, 7, 8, 9]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 6, 9, 12, 21, 24, 27]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 6, 9, 12, 21, 24, 27]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 8, 14, 26, 32]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 8, 14, 26, 32]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 5, 8, 11, 17, 20]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 5, 8, 11, 17, 20]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 16, 22, 34, 40]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 16, 22, 34, 40]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 7, 10, 16, 19]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 7, 10, 16, 19]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 11, 17, 23, 35, 41, 47, 53]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 11, 17, 23, 35, 41, 47, 53]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 9, 11, 13]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 9, 11, 13]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [-10, -5, 0, 5, 15, 20]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [-10, -5, 0, 5, 15, 20]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 12, 14, 16, 18]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 12, 14, 16, 18]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 10, 16, 22, 34, 40, 46, 52]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 10, 16, 22, 34, 40, 46, 52]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 7, 8, 9, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 7, 8, 9, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [20, 30, 40, 60, 70, 80]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [20, 30, 40, 60, 70, 80]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 12, 18, 24, 30, 36, 48, 54, 60, 66, 72, 78]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 12, 18, 24, 30, 36, 48, 54, 60, 66, 72, 78]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 10, 15, 25, 30, 35, 40]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 10, 15, 25, 30, 35, 40]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 16, 24, 32, 48, 56, 64]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 16, 24, 32, 48, 56, 64]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(arr = [11, 22, 33, 44, 66, 77, 88]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [11, 22, 33, 44, 66, 77, 88]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 14, 20, 26, 38, 44, 50]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 14, 20, 26, 38, 44, 50]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 18, 27, 36, 54, 63, 72]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 18, 27, 36, 54, 63, 72]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 12, 14, 16, 18]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 12, 14, 16, 18]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [12, 24, 36, 48, 60, 72, 84, 96, 112, 120, 132, 144]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [12, 24, 36, 48, 60, 72, 84, 96, 112, 120, 132, 144]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 13]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 13]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 6, 10, 14, 22, 26, 30]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 6, 10, 14, 22, 26, 30]) == 18: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [2, 4, 8, 16]) == 15
    assert candidate(arr = [3, 6, 9, 15]) == 12
    assert candidate(arr = [1, 3, 5, 9]) == 7
    assert candidate(arr = [5, 5, 5, 5, 10]) == 15
    assert candidate(arr = [3, 6, 9, 15, 18]) == 12
    assert candidate(arr = [100, 200, 300, 500]) == 400
    assert candidate(arr = [0, 2, 4, 8, 10]) == 6
    assert candidate(arr = [7, 14, 21, 35]) == 28
    assert candidate(arr = [8, 6, 4, 0]) == 2
    assert candidate(arr = [2, 4, 6, 10]) == 8
    assert candidate(arr = [2, 4, 8, 10, 12]) == 6
    assert candidate(arr = [0, 2, 4, 8]) == 6
    assert candidate(arr = [10, 20, 30, 50]) == 40
    assert candidate(arr = [100, 200, 300, 500, 600]) == 400
    assert candidate(arr = [5, 7, 11, 13]) == 9
    assert candidate(arr = [0, 2, 4, 6, 10]) == 8
    assert candidate(arr = [1, 3, 7, 9]) == 5
    assert candidate(arr = [0, 0, 0, 0]) == 0
    assert candidate(arr = [7, 14, 21, 35, 42]) == 28
    assert candidate(arr = [2, 4, 6, 8, 12]) == 10
    assert candidate(arr = [15, 13, 12]) == 14
    assert candidate(arr = [5, 10, 15, 25]) == 20
    assert candidate(arr = [5, 10, 15, 25, 30]) == 20
    assert candidate(arr = [7, 13, 19, 25, 37, 43, 49]) == 31
    assert candidate(arr = [5, 11, 17, 23, 29, 35, 47, 53]) == 41
    assert candidate(arr = [7, 11, 15, 19, 27, 31, 35]) == 23
    assert candidate(arr = [-20, -15, -10, -5, -1, 5, 10, 15, 20]) == 1
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 100]) == 90
    assert candidate(arr = [10, 20, 30, 50, 70]) == 60
    assert candidate(arr = [10, 20, 30, 40, 50, 70, 80, 90, 100]) == 60
    assert candidate(arr = [7, 11, 15, 19, 27, 31, 35]) == 23
    assert candidate(arr = [2, 8, 14, 20, 32, 38]) == 26
    assert candidate(arr = [12, 24, 36, 48, 60, 72, 84]) == 48
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 40, 45, 50, 55]) == 35
    assert candidate(arr = [4, 8, 12, 20, 24, 28, 32]) == 16
    assert candidate(arr = [1, 3, 5, 9, 11]) == 7
    assert candidate(arr = [4, 8, 12, 16, 20, 24, 28, 32, 36]) == 20
    assert candidate(arr = [12, 18, 24, 36, 42, 48]) == 30
    assert candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 57]) == 53
    assert candidate(arr = [100, 200, 300, 500, 600, 700, 800, 900]) == 400
    assert candidate(arr = [1, 4, 7, 10, 19, 22, 25, 28]) == 14
    assert candidate(arr = [5, 10, 20, 25, 30]) == 15
    assert candidate(arr = [1, 4, 7, 13, 16]) == 10
    assert candidate(arr = [25, 50, 75, 100, 150, 200, 225]) == 175
    assert candidate(arr = [8, 16, 24, 32, 40, 48, 64, 72, 80, 88, 96]) == 56
    assert candidate(arr = [6, 12, 18, 24, 30, 36, 42]) == 24
    assert candidate(arr = [15, 30, 45, 60, 75, 90, 105, 120, 150, 165, 180, 195, 210]) == 135
    assert candidate(arr = [100, 90, 80, 60, 50]) == 70
    assert candidate(arr = [1, 4, 7, 10, 13, 19]) == 16
    assert candidate(arr = [2, 4, 6, 8, 12, 14, 16]) == 10
    assert candidate(arr = [1000, 950, 900, 800, 750]) == 850
    assert candidate(arr = [100, 106, 112, 124, 130, 136]) == 118
    assert candidate(arr = [10, 20, 30, 40, 50, 70, 80, 90]) == 60
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 15]) == 13
    assert candidate(arr = [1, 4, 7, 10, 13, 19, 22]) == 16
    assert candidate(arr = [11, 22, 33, 44, 55, 66, 88, 99]) == 77
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800]) == 450
    assert candidate(arr = [6, 12, 18, 24, 36, 42, 48]) == 30
    assert candidate(arr = [10, 20, 30, 50, 60, 70]) == 40
    assert candidate(arr = [3, 6, 9, 12, 15, 21, 24, 27, 30, 33]) == 18
    assert candidate(arr = [8, 16, 24, 32, 48, 56, 64]) == 40
    assert candidate(arr = [1, 5, 9, 13, 17, 25, 29]) == 21
    assert candidate(arr = [3, 6, 9, 12, 18, 21, 24]) == 15
    assert candidate(arr = [99, 198, 297, 396, 495, 594, 792, 891]) == 693
    assert candidate(arr = [5, 10, 15, 20, 30, 35, 40, 45, 50, 55]) == 25
    assert candidate(arr = [5, 10, 15, 20, 25, 35, 40, 45, 50]) == 30
    assert candidate(arr = [5, 8, 11, 17, 20, 23, 26, 29]) == 14
    assert candidate(arr = [45, 90, 135, 180, 270, 315, 360]) == 225
    assert candidate(arr = [10, 20, 30, 50, 60]) == 40
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 16, 18, 20]) == 14
    assert candidate(arr = [8, 14, 20, 32, 38, 44]) == 26
    assert candidate(arr = [2, 4, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 6
    assert candidate(arr = [3, 9, 15, 21, 33, 39, 45]) == 27
    assert candidate(arr = [20, 40, 60, 80, 100, 120, 160, 180, 200]) == 140
    assert candidate(arr = [8, 16, 24, 32, 40, 56, 64]) == 48
    assert candidate(arr = [77, 88, 99, 121, 132, 143, 154]) == 110
    assert candidate(arr = [12, 18, 24, 30, 36, 48, 54]) == 42
    assert candidate(arr = [100, 200, 300, 500, 700, 900]) == 800
    assert candidate(arr = [0, 5, 10, 15, 20, 30, 35, 40, 45, 50]) == 25
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 80, 90, 100]) == 70
    assert candidate(arr = [7, 14, 21, 28, 42, 49, 56, 63]) == 35
    assert candidate(arr = [10, 20, 30, 40, 50, 70, 80, 90, 100, 110, 120]) == 60
    assert candidate(arr = [100, 200, 300, 500, 600]) == 400
    assert candidate(arr = [3, 9, 15, 21, 27, 33, 39, 45]) == 24
    assert candidate(arr = [10, 15, 20, 25, 35, 40, 45]) == 30
    assert candidate(arr = [25, 35, 45, 55, 65, 85]) == 75
    assert candidate(arr = [5, 10, 15, 20, 30]) == 25
    assert candidate(arr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 4
    assert candidate(arr = [1, 2, 3, 5, 6, 7, 8]) == 4
    assert candidate(arr = [1, 3, 5, 7, 11, 13, 15, 17, 19]) == 9
    assert candidate(arr = [15, 30, 45, 60, 75, 90, 120, 135, 150]) == 105
    assert candidate(arr = [5, 10, 15, 25, 30, 35, 40]) == 20
    assert candidate(arr = [1000, 2000, 3000, 4000, 5000, 7000, 8000, 9000, 10000]) == 6000
    assert candidate(arr = [1000, 900, 800, 700, 600, 500, 300, 200]) == 400
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]) == 7
    assert candidate(arr = [100, 150, 200, 250, 350, 400]) == 300
    assert candidate(arr = [11, 22, 33, 44, 55, 77, 88]) == 66
    assert candidate(arr = [5, 15, 25, 35, 45, 65]) == 55
    assert candidate(arr = [10, 20, 30, 50, 70]) == 60
    assert candidate(arr = [1, 3, 5, 9, 11, 13]) == 7
    assert candidate(arr = [1, 4, 7, 10, 13, 19, 22, 25, 28, 31]) == 16
    assert candidate(arr = [7, 17, 27, 37, 47, 57, 67]) == 37
    assert candidate(arr = [2, 4, 8, 10, 12, 14, 16]) == 6
    assert candidate(arr = [2, 4, 6, 8, 14, 16, 18]) == 12
    assert candidate(arr = [12, 14, 16, 18, 22, 24, 26]) == 20
    assert candidate(arr = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11]) == 3
    assert candidate(arr = [100, 200, 300, 500, 600, 700]) == 400
    assert candidate(arr = [3, 9, 15, 21, 27, 39, 45]) == 33
    assert candidate(arr = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 55]) == 51
    assert candidate(arr = [3, 6, 12, 15, 18, 21, 24, 27]) == 9
    assert candidate(arr = [10, 25, 40, 60, 75]) == 45
    assert candidate(arr = [8, 16, 24, 32, 40, 48, 56]) == 32
    assert candidate(arr = [7, 11, 15, 19, 27, 31, 35, 39]) == 23
    assert candidate(arr = [9, 18, 27, 36, 45, 63, 72]) == 54
    assert candidate(arr = [1, 2, 4, 5, 6, 7, 8]) == 3
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 17, 19, 21, 23, 25, 27]) == 15
    assert candidate(arr = [1, 3, 5, 9, 11, 13, 15]) == 7
    assert candidate(arr = [100, 200, 300, 400, 600, 700, 800]) == 500
    assert candidate(arr = [10, 15, 20, 25, 35, 40, 45]) == 30
    assert candidate(arr = [1, 3, 5, 7, 9, 15, 17, 19]) == 14
    assert candidate(arr = [2, 5, 8, 11, 14, 17, 20, 26]) == 23
    assert candidate(arr = [0, 1, 2, 4, 5, 6, 7, 8, 9]) == 3
    assert candidate(arr = [3, 6, 9, 12, 21, 24, 27]) == 18
    assert candidate(arr = [2, 8, 14, 26, 32]) == 20
    assert candidate(arr = [2, 5, 8, 11, 17, 20]) == 14
    assert candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 55
    assert candidate(arr = [10, 16, 22, 34, 40]) == 28
    assert candidate(arr = [1, 4, 7, 10, 16, 19]) == 13
    assert candidate(arr = [5, 11, 17, 23, 35, 41, 47, 53]) == 29
    assert candidate(arr = [1, 3, 5, 9, 11, 13]) == 7
    assert candidate(arr = [-10, -5, 0, 5, 15, 20]) == 10
    assert candidate(arr = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 3
    assert candidate(arr = [2, 4, 6, 8, 12, 14, 16, 18]) == 10
    assert candidate(arr = [4, 10, 16, 22, 34, 40, 46, 52]) == 28
    assert candidate(arr = [1, 2, 3, 4, 5, 7, 8, 9, 10]) == 6
    assert candidate(arr = [20, 30, 40, 60, 70, 80]) == 50
    assert candidate(arr = [6, 12, 18, 24, 30, 36, 48, 54, 60, 66, 72, 78]) == 42
    assert candidate(arr = [5, 10, 15, 25, 30, 35, 40]) == 20
    assert candidate(arr = [8, 16, 24, 32, 48, 56, 64]) == 40
    assert candidate(arr = [11, 22, 33, 44, 66, 77, 88]) == 55
    assert candidate(arr = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]) == 7
    assert candidate(arr = [8, 14, 20, 26, 38, 44, 50]) == 32
    assert candidate(arr = [9, 18, 27, 36, 54, 63, 72]) == 45
    assert candidate(arr = [2, 4, 6, 8, 12, 14, 16, 18]) == 10
    assert candidate(arr = [12, 24, 36, 48, 60, 72, 84, 96, 112, 120, 132, 144]) == 74
    assert candidate(arr = [1, 3, 5, 7, 9, 13]) == 11
    assert candidate(arr = [2, 6, 10, 14, 22, 26, 30]) == 18


