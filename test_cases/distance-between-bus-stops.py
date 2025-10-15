def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(distance = [7, 10, 1, 12, 11, 14, 5, 0],start = 7,destination = 2) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [7, 10, 1, 12, 11, 14, 5, 0],start = 7,destination = 2) == 17: {e}')
    
    total += 1
    try:
        result = candidate(distance = [1, 2, 3, 4],start = 0,destination = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [1, 2, 3, 4],start = 0,destination = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(distance = [4, 3, 2],start = 0,destination = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [4, 3, 2],start = 0,destination = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(distance = [1, 2, 3, 4],start = 0,destination = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [1, 2, 3, 4],start = 0,destination = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(distance = [3, 6, 7, 2, 9, 12, 5, 10, 15, 8],start = 3,destination = 7) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [3, 6, 7, 2, 9, 12, 5, 10, 15, 8],start = 3,destination = 7) == 28: {e}')
    
    total += 1
    try:
        result = candidate(distance = [3, 6, 7, 2, 9, 12, 5, 10, 1],start = 6,destination = 8) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [3, 6, 7, 2, 9, 12, 5, 10, 1],start = 6,destination = 8) == 15: {e}')
    
    total += 1
    try:
        result = candidate(distance = [3, 6, 7, 2, 9, 12, 5, 10, 15, 8],start = 5,destination = 9) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [3, 6, 7, 2, 9, 12, 5, 10, 15, 8],start = 5,destination = 9) == 35: {e}')
    
    total += 1
    try:
        result = candidate(distance = [3, 6, 7, 2, 9, 12, 5, 10, 1],start = 5,destination = 8) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [3, 6, 7, 2, 9, 12, 5, 10, 1],start = 5,destination = 8) == 27: {e}')
    
    total += 1
    try:
        result = candidate(distance = [1, 2, 3, 4],start = 0,destination = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [1, 2, 3, 4],start = 0,destination = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(distance = [3, 4, 5, 1, 2],start = 2,destination = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [3, 4, 5, 1, 2],start = 2,destination = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(distance = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],start = 0,destination = 9) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],start = 0,destination = 9) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(distance = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350],start = 10,destination = 20) == 1950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350],start = 10,destination = 20) == 1950: {e}')
    
    total += 1
    try:
        result = candidate(distance = [5, 8, 12, 4, 6, 7, 9, 3, 10, 1, 11],start = 2,destination = 6) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [5, 8, 12, 4, 6, 7, 9, 3, 10, 1, 11],start = 2,destination = 6) == 29: {e}')
    
    total += 1
    try:
        result = candidate(distance = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],start = 3,destination = 17) == 441
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],start = 3,destination = 17) == 441: {e}')
    
    total += 1
    try:
        result = candidate(distance = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],start = 24,destination = 50) == 1625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],start = 24,destination = 50) == 1625: {e}')
    
    total += 1
    try:
        result = candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],start = 10,destination = 20) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],start = 10,destination = 20) == 155: {e}')
    
    total += 1
    try:
        result = candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],start = 15,destination = 5) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],start = 15,destination = 5) == 105: {e}')
    
    total += 1
    try:
        result = candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],start = 4,destination = 13) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],start = 4,destination = 13) == 39: {e}')
    
    total += 1
    try:
        result = candidate(distance = [5, 8, 12, 15, 20, 25, 30, 35, 40, 45, 50],start = 2,destination = 8) == 137
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [5, 8, 12, 15, 20, 25, 30, 35, 40, 45, 50],start = 2,destination = 8) == 137: {e}')
    
    total += 1
    try:
        result = candidate(distance = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],start = 5,destination = 10) == 230
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],start = 5,destination = 10) == 230: {e}')
    
    total += 1
    try:
        result = candidate(distance = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],start = 12,destination = 5) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],start = 12,destination = 5) == 106: {e}')
    
    total += 1
    try:
        result = candidate(distance = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],start = 7,destination = 3) == 22000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],start = 7,destination = 3) == 22000: {e}')
    
    total += 1
    try:
        result = candidate(distance = [2, 10, 3, 5, 1, 7, 8, 6, 9, 4, 12, 11],start = 4,destination = 11) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [2, 10, 3, 5, 1, 7, 8, 6, 9, 4, 12, 11],start = 4,destination = 11) == 31: {e}')
    
    total += 1
    try:
        result = candidate(distance = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],start = 0,destination = 10) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],start = 0,destination = 10) == 105: {e}')
    
    total += 1
    try:
        result = candidate(distance = [15, 20, 25, 30, 35, 40, 45, 50],start = 0,destination = 7) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [15, 20, 25, 30, 35, 40, 45, 50],start = 0,destination = 7) == 50: {e}')
    
    total += 1
    try:
        result = candidate(distance = [7, 5, 3, 1, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],start = 6,destination = 13) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [7, 5, 3, 1, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],start = 6,destination = 13) == 92: {e}')
    
    total += 1
    try:
        result = candidate(distance = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],start = 8,destination = 17) == 4650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],start = 8,destination = 17) == 4650: {e}')
    
    total += 1
    try:
        result = candidate(distance = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],start = 9,destination = 1) == 1100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],start = 9,destination = 1) == 1100: {e}')
    
    total += 1
    try:
        result = candidate(distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],start = 25,destination = 5) == 1550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],start = 25,destination = 5) == 1550: {e}')
    
    total += 1
    try:
        result = candidate(distance = [100, 200, 150, 100, 50, 250, 300, 50, 100, 200, 150, 250],start = 3,destination = 11) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [100, 200, 150, 100, 50, 250, 300, 50, 100, 200, 150, 250],start = 3,destination = 11) == 700: {e}')
    
    total += 1
    try:
        result = candidate(distance = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],start = 0,destination = 50) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],start = 0,destination = 50) == 75: {e}')
    
    total += 1
    try:
        result = candidate(distance = [100, 200, 300, 400, 500],start = 1,destination = 3) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [100, 200, 300, 400, 500],start = 1,destination = 3) == 500: {e}')
    
    total += 1
    try:
        result = candidate(distance = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],start = 25,destination = 5) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],start = 25,destination = 5) == 50: {e}')
    
    total += 1
    try:
        result = candidate(distance = [7, 3, 8, 4, 2, 9, 1, 6, 5],start = 5,destination = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [7, 3, 8, 4, 2, 9, 1, 6, 5],start = 5,destination = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(distance = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260],start = 5,destination = 18) == 702
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260],start = 5,destination = 18) == 702: {e}')
    
    total += 1
    try:
        result = candidate(distance = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216, 228, 240],start = 10,destination = 18) == 1128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216, 228, 240],start = 10,destination = 18) == 1128: {e}')
    
    total += 1
    try:
        result = candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],start = 12,destination = 7) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],start = 12,destination = 7) == 50: {e}')
    
    total += 1
    try:
        result = candidate(distance = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],start = 18,destination = 3) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],start = 18,destination = 3) == 90: {e}')
    
    total += 1
    try:
        result = candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],start = 0,destination = 19) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],start = 0,destination = 19) == 20: {e}')
    
    total += 1
    try:
        result = candidate(distance = [50, 40, 30, 20, 10, 5, 2, 1, 9, 8, 7, 6, 4, 3, 2],start = 4,destination = 11) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [50, 40, 30, 20, 10, 5, 2, 1, 9, 8, 7, 6, 4, 3, 2],start = 4,destination = 11) == 42: {e}')
    
    total += 1
    try:
        result = candidate(distance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],start = 0,destination = 19) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],start = 0,destination = 19) == 1: {e}')
    
    total += 1
    try:
        result = candidate(distance = [9, 8, 7, 6, 5, 4, 3, 2, 1],start = 3,destination = 7) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [9, 8, 7, 6, 5, 4, 3, 2, 1],start = 3,destination = 7) == 18: {e}')
    
    total += 1
    try:
        result = candidate(distance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],start = 0,destination = 100) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],start = 0,destination = 100) == 30: {e}')
    
    total += 1
    try:
        result = candidate(distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 0,destination = 5) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 0,destination = 5) == 150: {e}')
    
    total += 1
    try:
        result = candidate(distance = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],start = 7,destination = 2) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],start = 7,destination = 2) == 225: {e}')
    
    total += 1
    try:
        result = candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],start = 23,destination = 17) == 123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],start = 23,destination = 17) == 123: {e}')
    
    total += 1
    try:
        result = candidate(distance = [23, 17, 11, 5, 3, 8, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97, 103, 109, 115, 121, 127, 133, 139, 145, 151, 157],start = 15,destination = 25) == 940
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [23, 17, 11, 5, 3, 8, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97, 103, 109, 115, 121, 127, 133, 139, 145, 151, 157],start = 15,destination = 25) == 940: {e}')
    
    total += 1
    try:
        result = candidate(distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 9,destination = 0) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 9,destination = 0) == 100: {e}')
    
    total += 1
    try:
        result = candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],start = 8,destination = 3) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],start = 8,destination = 3) == 25: {e}')
    
    total += 1
    try:
        result = candidate(distance = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],start = 4,destination = 11) == 245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],start = 4,destination = 11) == 245: {e}')
    
    total += 1
    try:
        result = candidate(distance = [9, 8, 7, 6, 5, 4, 3, 2, 1],start = 2,destination = 7) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [9, 8, 7, 6, 5, 4, 3, 2, 1],start = 2,destination = 7) == 20: {e}')
    
    total += 1
    try:
        result = candidate(distance = [123, 456, 789, 101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717],start = 19,destination = 5) == 3388
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [123, 456, 789, 101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717],start = 19,destination = 5) == 3388: {e}')
    
    total += 1
    try:
        result = candidate(distance = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],start = 10,destination = 20) == 185
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],start = 10,destination = 20) == 185: {e}')
    
    total += 1
    try:
        result = candidate(distance = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],start = 6,destination = 13) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],start = 6,destination = 13) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 2,destination = 7) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 2,destination = 7) == 250: {e}')
    
    total += 1
    try:
        result = candidate(distance = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],start = 3,destination = 14) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],start = 3,destination = 14) == 57: {e}')
    
    total += 1
    try:
        result = candidate(distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 2,destination = 6) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 2,destination = 6) == 180: {e}')
    
    total += 1
    try:
        result = candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],start = 14,destination = 6) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],start = 14,destination = 6) == 36: {e}')
    
    total += 1
    try:
        result = candidate(distance = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],start = 2,destination = 9) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],start = 2,destination = 9) == 104: {e}')
    
    total += 1
    try:
        result = candidate(distance = [5, 10, 15, 20, 25, 30, 35, 40],start = 1,destination = 6) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [5, 10, 15, 20, 25, 30, 35, 40],start = 1,destination = 6) == 80: {e}')
    
    total += 1
    try:
        result = candidate(distance = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300],start = 0,destination = 12) == 1300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300],start = 0,destination = 12) == 1300: {e}')
    
    total += 1
    try:
        result = candidate(distance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],start = 0,destination = 29) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],start = 0,destination = 29) == 3: {e}')
    
    total += 1
    try:
        result = candidate(distance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],start = 0,destination = 39) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],start = 0,destination = 39) == 8: {e}')
    
    total += 1
    try:
        result = candidate(distance = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],start = 5,destination = 2) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],start = 5,destination = 2) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 0,destination = 9) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 0,destination = 9) == 100: {e}')
    
    total += 1
    try:
        result = candidate(distance = [7, 3, 5, 2, 8, 6, 4, 1, 9, 11, 13, 15, 17],start = 5,destination = 10) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [7, 3, 5, 2, 8, 6, 4, 1, 9, 11, 13, 15, 17],start = 5,destination = 10) == 31: {e}')
    
    total += 1
    try:
        result = candidate(distance = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],start = 5,destination = 11) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],start = 5,destination = 11) == 54: {e}')
    
    total += 1
    try:
        result = candidate(distance = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77],start = 0,destination = 10) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(distance = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77],start = 0,destination = 10) == 77: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(distance = [7, 10, 1, 12, 11, 14, 5, 0],start = 7,destination = 2) == 17
    assert candidate(distance = [1, 2, 3, 4],start = 0,destination = 2) == 3
    assert candidate(distance = [4, 3, 2],start = 0,destination = 2) == 2
    assert candidate(distance = [1, 2, 3, 4],start = 0,destination = 1) == 1
    assert candidate(distance = [3, 6, 7, 2, 9, 12, 5, 10, 15, 8],start = 3,destination = 7) == 28
    assert candidate(distance = [3, 6, 7, 2, 9, 12, 5, 10, 1],start = 6,destination = 8) == 15
    assert candidate(distance = [3, 6, 7, 2, 9, 12, 5, 10, 15, 8],start = 5,destination = 9) == 35
    assert candidate(distance = [3, 6, 7, 2, 9, 12, 5, 10, 1],start = 5,destination = 8) == 27
    assert candidate(distance = [1, 2, 3, 4],start = 0,destination = 3) == 4
    assert candidate(distance = [3, 4, 5, 1, 2],start = 2,destination = 1) == 4
    assert candidate(distance = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],start = 0,destination = 9) == 1000
    assert candidate(distance = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350],start = 10,destination = 20) == 1950
    assert candidate(distance = [5, 8, 12, 4, 6, 7, 9, 3, 10, 1, 11],start = 2,destination = 6) == 29
    assert candidate(distance = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],start = 3,destination = 17) == 441
    assert candidate(distance = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],start = 24,destination = 50) == 1625
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],start = 10,destination = 20) == 155
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],start = 15,destination = 5) == 105
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],start = 4,destination = 13) == 39
    assert candidate(distance = [5, 8, 12, 15, 20, 25, 30, 35, 40, 45, 50],start = 2,destination = 8) == 137
    assert candidate(distance = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],start = 5,destination = 10) == 230
    assert candidate(distance = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],start = 12,destination = 5) == 106
    assert candidate(distance = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],start = 7,destination = 3) == 22000
    assert candidate(distance = [2, 10, 3, 5, 1, 7, 8, 6, 9, 4, 12, 11],start = 4,destination = 11) == 31
    assert candidate(distance = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],start = 0,destination = 10) == 105
    assert candidate(distance = [15, 20, 25, 30, 35, 40, 45, 50],start = 0,destination = 7) == 50
    assert candidate(distance = [7, 5, 3, 1, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],start = 6,destination = 13) == 92
    assert candidate(distance = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],start = 8,destination = 17) == 4650
    assert candidate(distance = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],start = 9,destination = 1) == 1100
    assert candidate(distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],start = 25,destination = 5) == 1550
    assert candidate(distance = [100, 200, 150, 100, 50, 250, 300, 50, 100, 200, 150, 250],start = 3,destination = 11) == 700
    assert candidate(distance = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],start = 0,destination = 50) == 75
    assert candidate(distance = [100, 200, 300, 400, 500],start = 1,destination = 3) == 500
    assert candidate(distance = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],start = 25,destination = 5) == 50
    assert candidate(distance = [7, 3, 8, 4, 2, 9, 1, 6, 5],start = 5,destination = 3) == 6
    assert candidate(distance = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260],start = 5,destination = 18) == 702
    assert candidate(distance = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216, 228, 240],start = 10,destination = 18) == 1128
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],start = 12,destination = 7) == 50
    assert candidate(distance = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],start = 18,destination = 3) == 90
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],start = 0,destination = 19) == 20
    assert candidate(distance = [50, 40, 30, 20, 10, 5, 2, 1, 9, 8, 7, 6, 4, 3, 2],start = 4,destination = 11) == 42
    assert candidate(distance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],start = 0,destination = 19) == 1
    assert candidate(distance = [9, 8, 7, 6, 5, 4, 3, 2, 1],start = 3,destination = 7) == 18
    assert candidate(distance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],start = 0,destination = 100) == 30
    assert candidate(distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 0,destination = 5) == 150
    assert candidate(distance = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],start = 7,destination = 2) == 225
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],start = 23,destination = 17) == 123
    assert candidate(distance = [23, 17, 11, 5, 3, 8, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97, 103, 109, 115, 121, 127, 133, 139, 145, 151, 157],start = 15,destination = 25) == 940
    assert candidate(distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 9,destination = 0) == 100
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],start = 8,destination = 3) == 25
    assert candidate(distance = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],start = 4,destination = 11) == 245
    assert candidate(distance = [9, 8, 7, 6, 5, 4, 3, 2, 1],start = 2,destination = 7) == 20
    assert candidate(distance = [123, 456, 789, 101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717],start = 19,destination = 5) == 3388
    assert candidate(distance = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],start = 10,destination = 20) == 185
    assert candidate(distance = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],start = 6,destination = 13) == 5000
    assert candidate(distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 2,destination = 7) == 250
    assert candidate(distance = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],start = 3,destination = 14) == 57
    assert candidate(distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 2,destination = 6) == 180
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],start = 14,destination = 6) == 36
    assert candidate(distance = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],start = 2,destination = 9) == 104
    assert candidate(distance = [5, 10, 15, 20, 25, 30, 35, 40],start = 1,destination = 6) == 80
    assert candidate(distance = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300],start = 0,destination = 12) == 1300
    assert candidate(distance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],start = 0,destination = 29) == 3
    assert candidate(distance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],start = 0,destination = 39) == 8
    assert candidate(distance = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],start = 5,destination = 2) == 1200
    assert candidate(distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 0,destination = 9) == 100
    assert candidate(distance = [7, 3, 5, 2, 8, 6, 4, 1, 9, 11, 13, 15, 17],start = 5,destination = 10) == 31
    assert candidate(distance = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],start = 5,destination = 11) == 54
    assert candidate(distance = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77],start = 0,destination = 10) == 77


