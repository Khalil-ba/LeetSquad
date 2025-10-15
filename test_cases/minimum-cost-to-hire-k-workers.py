def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(quality = [1, 2, 3, 4, 5],wage = [5, 4, 3, 2, 1],k = 3) == 12.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 2, 3, 4, 5],wage = [5, 4, 3, 2, 1],k = 3) == 12.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 1, 1, 1, 1],wage = [1, 1, 1, 1, 1],k = 2) == 2.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 1, 1, 1, 1],wage = [1, 1, 1, 1, 1],k = 2) == 2.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [100, 200, 300, 400, 500],wage = [1000, 2000, 3000, 4000, 5000],k = 4) == 10000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [100, 200, 300, 400, 500],wage = [1000, 2000, 3000, 4000, 5000],k = 4) == 10000.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 1, 1, 1],wage = [1, 2, 3, 4],k = 2) == 4.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 1, 1, 1],wage = [1, 2, 3, 4],k = 2) == 4.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [100, 200, 300, 400, 500],wage = [500, 400, 300, 200, 100],k = 2) == 450.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [100, 200, 300, 400, 500],wage = [500, 400, 300, 200, 100],k = 2) == 450.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [10, 10, 10, 10],wage = [10, 10, 10, 10],k = 4) == 40.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [10, 10, 10, 10],wage = [10, 10, 10, 10],k = 4) == 40.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [3, 1, 10, 10, 1],wage = [4, 8, 2, 2, 7],k = 3) == 30.666666666666664
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [3, 1, 10, 10, 1],wage = [4, 8, 2, 2, 7],k = 3) == 30.666666666666664: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 2, 3, 4, 5],wage = [1, 2, 3, 4, 5],k = 4) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 2, 3, 4, 5],wage = [1, 2, 3, 4, 5],k = 4) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [10, 10, 10, 10, 10],wage = [10, 10, 10, 10, 10],k = 5) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [10, 10, 10, 10, 10],wage = [10, 10, 10, 10, 10],k = 5) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [4, 1, 3, 2],wage = [20, 10, 30, 20],k = 2) == 30.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [4, 1, 3, 2],wage = [20, 10, 30, 20],k = 2) == 30.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [6, 12, 10, 10],wage = [48, 48, 30, 60],k = 3) == 192.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [6, 12, 10, 10],wage = [48, 48, 30, 60],k = 3) == 192.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [10, 20, 5],wage = [70, 50, 30],k = 2) == 105.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [10, 20, 5],wage = [70, 50, 30],k = 2) == 105.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [15, 10, 25, 5, 30, 20, 35, 40],wage = [150, 100, 250, 50, 300, 200, 350, 400],k = 4) == 500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [15, 10, 25, 5, 30, 20, 35, 40],wage = [150, 100, 250, 50, 300, 200, 350, 400],k = 4) == 500.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [100, 200, 300, 400, 500],wage = [500, 1000, 1500, 2000, 2500],k = 2) == 1500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [100, 200, 300, 400, 500],wage = [500, 1000, 1500, 2000, 2500],k = 2) == 1500.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 6) == 36.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 6) == 36.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [100, 200, 300, 400, 500],wage = [500, 1000, 1500, 2000, 2500],k = 4) == 5000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [100, 200, 300, 400, 500],wage = [500, 1000, 1500, 2000, 2500],k = 4) == 5000.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [7, 5, 3, 8, 2],wage = [70, 50, 30, 80, 20],k = 2) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [7, 5, 3, 8, 2],wage = [70, 50, 30, 80, 20],k = 2) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [12, 15, 18, 21, 24, 27, 30],wage = [60, 75, 90, 105, 120, 135, 150],k = 4) == 330.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [12, 15, 18, 21, 24, 27, 30],wage = [60, 75, 90, 105, 120, 135, 150],k = 4) == 330.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [50, 40, 30, 20, 10],wage = [200, 160, 120, 80, 40],k = 2) == 120.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [50, 40, 30, 20, 10],wage = [200, 160, 120, 80, 40],k = 2) == 120.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],wage = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110],k = 6) == 420.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],wage = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110],k = 6) == 420.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [15, 20, 5, 10, 30],wage = [105, 150, 30, 70, 210],k = 3) == 210.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [15, 20, 5, 10, 30],wage = [105, 150, 30, 70, 210],k = 3) == 210.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],wage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 5) == 250.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],wage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 5) == 250.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [9, 18, 27, 36, 45, 54, 63],wage = [81, 162, 243, 324, 405, 486, 567],k = 5) == 1215.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [9, 18, 27, 36, 45, 54, 63],wage = [81, 162, 243, 324, 405, 486, 567],k = 5) == 1215.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],wage = [32, 32, 32, 32, 32, 32, 32, 32, 32, 32],k = 5) == 160.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],wage = [32, 32, 32, 32, 32, 32, 32, 32, 32, 32],k = 5) == 160.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [5, 15, 25, 35, 45, 55],wage = [35, 105, 175, 245, 315, 385],k = 4) == 560.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [5, 15, 25, 35, 45, 55],wage = [35, 105, 175, 245, 315, 385],k = 4) == 560.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [20, 10, 30, 40, 50, 60, 70, 80, 90, 100],wage = [140, 70, 210, 280, 350, 420, 490, 560, 630, 700],k = 6) == 1470.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [20, 10, 30, 40, 50, 60, 70, 80, 90, 100],wage = [140, 70, 210, 280, 350, 420, 490, 560, 630, 700],k = 6) == 1470.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],wage = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 5) == 15000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],wage = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 5) == 15000.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 100.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 100.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 3, 2, 5, 4, 6],wage = [1, 9, 4, 25, 16, 36],k = 5) == 75.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 3, 2, 5, 4, 6],wage = [1, 9, 4, 25, 16, 36],k = 5) == 75.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [15, 20, 5, 10, 25],wage = [120, 160, 40, 80, 200],k = 5) == 600.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [15, 20, 5, 10, 25],wage = [120, 160, 40, 80, 200],k = 5) == 600.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],wage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 8) == 360.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],wage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 8) == 360.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],wage = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225],k = 7) == 196.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],wage = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225],k = 7) == 196.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 25.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 25.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 3, 5, 7, 9, 11, 13],wage = [2, 6, 10, 14, 18, 22, 26],k = 5) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 3, 5, 7, 9, 11, 13],wage = [2, 6, 10, 14, 18, 22, 26],k = 5) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 49.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 49.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],wage = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 8) == 3600.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],wage = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 8) == 3600.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],wage = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 1500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],wage = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 1500.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 3, 5, 7, 9, 11, 13],wage = [2, 6, 10, 14, 18, 22, 26],k = 4) == 32.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 3, 5, 7, 9, 11, 13],wage = [2, 6, 10, 14, 18, 22, 26],k = 4) == 32.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [4, 7, 2, 5, 6],wage = [32, 56, 16, 40, 48],k = 2) == 48.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [4, 7, 2, 5, 6],wage = [32, 56, 16, 40, 48],k = 2) == 48.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 25.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 25.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],wage = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60],k = 9) == 270.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],wage = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60],k = 9) == 270.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],wage = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 3) == 6.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],wage = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 3) == 6.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [4, 5, 1, 2, 3],wage = [40, 50, 10, 20, 30],k = 2) == 30.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [4, 5, 1, 2, 3],wage = [40, 50, 10, 20, 30],k = 2) == 30.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],wage = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],k = 7) == 700.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],wage = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],k = 7) == 700.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],wage = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 1500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],wage = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 1500.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],wage = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750],k = 8) == 1800.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],wage = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750],k = 8) == 1800.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 28.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 28.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [10, 12, 14, 16, 18, 20],wage = [70, 84, 98, 112, 126, 140],k = 5) == 490.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [10, 12, 14, 16, 18, 20],wage = [70, 84, 98, 112, 126, 140],k = 5) == 490.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [2, 3, 5, 7, 11, 13],wage = [14, 21, 35, 49, 77, 91],k = 4) == 119.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [2, 3, 5, 7, 11, 13],wage = [14, 21, 35, 49, 77, 91],k = 4) == 119.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [30, 10, 40, 20, 50],wage = [90, 30, 120, 60, 150],k = 3) == 180.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [30, 10, 40, 20, 50],wage = [90, 30, 120, 60, 150],k = 3) == 180.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [2, 4, 6, 8, 10],wage = [10, 20, 30, 40, 50],k = 3) == 60.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [2, 4, 6, 8, 10],wage = [10, 20, 30, 40, 50],k = 3) == 60.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [100, 200, 300, 400, 500],wage = [1000, 2000, 3000, 4000, 5000],k = 4) == 10000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [100, 200, 300, 400, 500],wage = [1000, 2000, 3000, 4000, 5000],k = 4) == 10000.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 25.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 25.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [4, 5, 6, 7, 8, 9],wage = [24, 30, 36, 42, 48, 54],k = 4) == 132.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [4, 5, 6, 7, 8, 9],wage = [24, 30, 36, 42, 48, 54],k = 4) == 132.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [4, 3, 2, 1],wage = [16, 12, 8, 4],k = 2) == 12.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [4, 3, 2, 1],wage = [16, 12, 8, 4],k = 2) == 12.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],wage = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1],k = 4) == 34.46153846153846
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],wage = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1],k = 4) == 34.46153846153846: {e}')
    
    total += 1
    try:
        result = candidate(quality = [20, 30, 10, 40, 50],wage = [100, 150, 50, 200, 250],k = 4) == 500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [20, 30, 10, 40, 50],wage = [100, 150, 50, 200, 250],k = 4) == 500.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [15, 25, 35, 45, 55],wage = [105, 175, 245, 315, 385],k = 3) == 525.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [15, 25, 35, 45, 55],wage = [105, 175, 245, 315, 385],k = 3) == 525.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],wage = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 3) == 30.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],wage = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 3) == 30.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],wage = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],k = 5) == 27.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],wage = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],k = 5) == 27.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [7, 14, 21, 28, 35, 42, 49, 56, 63],wage = [14, 28, 42, 56, 70, 84, 98, 112, 126],k = 6) == 294.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [7, 14, 21, 28, 35, 42, 49, 56, 63],wage = [14, 28, 42, 56, 70, 84, 98, 112, 126],k = 6) == 294.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],wage = [70, 140, 210, 280, 350, 420, 490, 560, 630, 700],k = 7) == 1960.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],wage = [70, 140, 210, 280, 350, 420, 490, 560, 630, 700],k = 7) == 1960.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [10, 20, 30, 40, 50],wage = [50, 40, 30, 20, 10],k = 3) == 120.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [10, 20, 30, 40, 50],wage = [50, 40, 30, 20, 10],k = 3) == 120.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [4, 2, 8, 5, 10, 7],wage = [40, 20, 80, 50, 100, 70],k = 4) == 180.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [4, 2, 8, 5, 10, 7],wage = [40, 20, 80, 50, 100, 70],k = 4) == 180.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],wage = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 3) == 33.75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],wage = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 3) == 33.75: {e}')
    
    total += 1
    try:
        result = candidate(quality = [10, 20, 30, 40, 50, 60],wage = [50, 100, 150, 200, 250, 300],k = 6) == 1050.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [10, 20, 30, 40, 50, 60],wage = [50, 100, 150, 200, 250, 300],k = 6) == 1050.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],wage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 6) == 210.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],wage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 6) == 210.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [5, 3, 8, 6, 2],wage = [45, 30, 60, 48, 12],k = 3) == 100.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [5, 3, 8, 6, 2],wage = [45, 30, 60, 48, 12],k = 3) == 100.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],wage = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 25.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],wage = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 25.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [5, 10, 15, 20, 25, 30, 35],wage = [50, 100, 150, 200, 250, 300, 350],k = 4) == 500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [5, 10, 15, 20, 25, 30, 35],wage = [50, 100, 150, 200, 250, 300, 350],k = 4) == 500.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 1, 1, 1, 1, 1, 1, 1],wage = [1, 2, 3, 4, 5, 6, 7, 8],k = 5) == 25.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 1, 1, 1, 1, 1, 1, 1],wage = [1, 2, 3, 4, 5, 6, 7, 8],k = 5) == 25.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],wage = [700, 1400, 2100, 2800, 3500, 4200, 4900, 5600, 6300, 7000],k = 7) == 19600.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],wage = [700, 1400, 2100, 2800, 3500, 4200, 4900, 5600, 6300, 7000],k = 7) == 19600.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [15, 30, 45, 60, 75, 90, 105],wage = [45, 90, 135, 180, 225, 270, 315],k = 5) == 675.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [15, 30, 45, 60, 75, 90, 105],wage = [45, 90, 135, 180, 225, 270, 315],k = 5) == 675.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [5, 2, 10, 15, 20, 1],wage = [100, 60, 200, 300, 400, 50],k = 3) == 400.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [5, 2, 10, 15, 20, 1],wage = [100, 60, 200, 300, 400, 50],k = 3) == 400.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],wage = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 7) == 2800.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],wage = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 7) == 2800.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],wage = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000],k = 5) == 3000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],wage = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000],k = 5) == 3000.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [100, 200, 150, 50, 250],wage = [500, 1000, 750, 250, 1250],k = 3) == 1500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [100, 200, 150, 50, 250],wage = [500, 1000, 750, 250, 1250],k = 3) == 1500.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],wage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 7) == 280.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],wage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 7) == 280.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],wage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 150.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],wage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 150.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],wage = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 6) == 180.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],wage = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 6) == 180.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],wage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 8) == 360.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],wage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 8) == 360.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 3, 2, 4, 5],wage = [3, 9, 6, 12, 15],k = 3) == 18.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 3, 2, 4, 5],wage = [3, 9, 6, 12, 15],k = 3) == 18.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [3, 6, 15, 20, 12],wage = [9, 18, 45, 60, 36],k = 3) == 63.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [3, 6, 15, 20, 12],wage = [9, 18, 45, 60, 36],k = 3) == 63.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 3) == 9.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 3) == 9.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],wage = [14, 28, 42, 56, 70, 84, 98, 112, 126, 140, 154, 168, 182, 196, 210],k = 7) == 392.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],wage = [14, 28, 42, 56, 70, 84, 98, 112, 126, 140, 154, 168, 182, 196, 210],k = 7) == 392.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [5, 15, 10, 20, 25],wage = [75, 225, 150, 300, 375],k = 3) == 450.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [5, 15, 10, 20, 25],wage = [75, 225, 150, 300, 375],k = 3) == 450.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [2, 4, 6, 8, 10],wage = [10, 20, 30, 40, 50],k = 4) == 100.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [2, 4, 6, 8, 10],wage = [10, 20, 30, 40, 50],k = 4) == 100.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],wage = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],k = 6) == 1050.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],wage = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],k = 6) == 1050.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 2, 4, 8, 16, 32, 64],wage = [1, 2, 4, 8, 16, 32, 64],k = 4) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 2, 4, 8, 16, 32, 64],wage = [1, 2, 4, 8, 16, 32, 64],k = 4) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],wage = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60],k = 6) == 126.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],wage = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60],k = 6) == 126.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],wage = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],k = 6) == 180.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],wage = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],k = 6) == 180.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],wage = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 5) == 31.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],wage = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 5) == 31.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 100.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 100.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41],wage = [4, 6, 10, 14, 22, 26, 34, 38, 46, 58, 62, 74, 82],k = 8) == 154.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41],wage = [4, 6, 10, 14, 22, 26, 34, 38, 46, 58, 62, 74, 82],k = 8) == 154.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [5, 8, 12, 15, 20, 25, 30],wage = [10, 16, 24, 30, 40, 50, 60],k = 3) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [5, 8, 12, 15, 20, 25, 30],wage = [10, 16, 24, 30, 40, 50, 60],k = 3) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [15, 10, 5, 25, 20],wage = [90, 60, 30, 150, 120],k = 3) == 180.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [15, 10, 5, 25, 20],wage = [90, 60, 30, 150, 120],k = 3) == 180.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [15, 25, 10, 40, 30],wage = [105, 175, 70, 280, 210],k = 3) == 350.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [15, 25, 10, 40, 30],wage = [105, 175, 70, 280, 210],k = 3) == 350.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60],wage = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120],k = 8) == 432.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60],wage = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120],k = 8) == 432.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],wage = [10, 40, 90, 160, 250, 360, 490, 640, 810, 1000],k = 6) == 1260.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],wage = [10, 40, 90, 160, 250, 360, 490, 640, 810, 1000],k = 6) == 1260.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [8, 6, 4, 2, 10],wage = [96, 72, 48, 24, 120],k = 4) == 240.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [8, 6, 4, 2, 10],wage = [96, 72, 48, 24, 120],k = 4) == 240.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [7, 14, 3, 11, 9],wage = [28, 56, 12, 44, 36],k = 4) == 120.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [7, 14, 3, 11, 9],wage = [28, 56, 12, 44, 36],k = 4) == 120.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [100, 200, 300, 400, 500, 600, 700],wage = [700, 1400, 2100, 2800, 3500, 4200, 4900],k = 5) == 10500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [100, 200, 300, 400, 500, 600, 700],wage = [700, 1400, 2100, 2800, 3500, 4200, 4900],k = 5) == 10500.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [3, 5, 2, 8, 7],wage = [6, 10, 4, 16, 14],k = 3) == 20.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [3, 5, 2, 8, 7],wage = [6, 10, 4, 16, 14],k = 3) == 20.0: {e}')
    
    total += 1
    try:
        result = candidate(quality = [5, 3, 10, 2, 4],wage = [50, 30, 100, 20, 40],k = 3) == 90.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(quality = [5, 3, 10, 2, 4],wage = [50, 30, 100, 20, 40],k = 3) == 90.0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(quality = [1, 2, 3, 4, 5],wage = [5, 4, 3, 2, 1],k = 3) == 12.0
    assert candidate(quality = [1, 1, 1, 1, 1],wage = [1, 1, 1, 1, 1],k = 2) == 2.0
    assert candidate(quality = [100, 200, 300, 400, 500],wage = [1000, 2000, 3000, 4000, 5000],k = 4) == 10000.0
    assert candidate(quality = [1, 1, 1, 1],wage = [1, 2, 3, 4],k = 2) == 4.0
    assert candidate(quality = [100, 200, 300, 400, 500],wage = [500, 400, 300, 200, 100],k = 2) == 450.0
    assert candidate(quality = [10, 10, 10, 10],wage = [10, 10, 10, 10],k = 4) == 40.0
    assert candidate(quality = [3, 1, 10, 10, 1],wage = [4, 8, 2, 2, 7],k = 3) == 30.666666666666664
    assert candidate(quality = [1, 2, 3, 4, 5],wage = [1, 2, 3, 4, 5],k = 4) == 10.0
    assert candidate(quality = [10, 10, 10, 10, 10],wage = [10, 10, 10, 10, 10],k = 5) == 50.0
    assert candidate(quality = [4, 1, 3, 2],wage = [20, 10, 30, 20],k = 2) == 30.0
    assert candidate(quality = [6, 12, 10, 10],wage = [48, 48, 30, 60],k = 3) == 192.0
    assert candidate(quality = [10, 20, 5],wage = [70, 50, 30],k = 2) == 105.0
    assert candidate(quality = [15, 10, 25, 5, 30, 20, 35, 40],wage = [150, 100, 250, 50, 300, 200, 350, 400],k = 4) == 500.0
    assert candidate(quality = [100, 200, 300, 400, 500],wage = [500, 1000, 1500, 2000, 2500],k = 2) == 1500.0
    assert candidate(quality = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 6) == 36.0
    assert candidate(quality = [100, 200, 300, 400, 500],wage = [500, 1000, 1500, 2000, 2500],k = 4) == 5000.0
    assert candidate(quality = [7, 5, 3, 8, 2],wage = [70, 50, 30, 80, 20],k = 2) == 50.0
    assert candidate(quality = [12, 15, 18, 21, 24, 27, 30],wage = [60, 75, 90, 105, 120, 135, 150],k = 4) == 330.0
    assert candidate(quality = [50, 40, 30, 20, 10],wage = [200, 160, 120, 80, 40],k = 2) == 120.0
    assert candidate(quality = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],wage = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110],k = 6) == 420.0
    assert candidate(quality = [15, 20, 5, 10, 30],wage = [105, 150, 30, 70, 210],k = 3) == 210.0
    assert candidate(quality = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],wage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 5) == 250.0
    assert candidate(quality = [9, 18, 27, 36, 45, 54, 63],wage = [81, 162, 243, 324, 405, 486, 567],k = 5) == 1215.0
    assert candidate(quality = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],wage = [32, 32, 32, 32, 32, 32, 32, 32, 32, 32],k = 5) == 160.0
    assert candidate(quality = [5, 15, 25, 35, 45, 55],wage = [35, 105, 175, 245, 315, 385],k = 4) == 560.0
    assert candidate(quality = [20, 10, 30, 40, 50, 60, 70, 80, 90, 100],wage = [140, 70, 210, 280, 350, 420, 490, 560, 630, 700],k = 6) == 1470.0
    assert candidate(quality = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],wage = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 5) == 15000.0
    assert candidate(quality = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 100.0
    assert candidate(quality = [1, 3, 2, 5, 4, 6],wage = [1, 9, 4, 25, 16, 36],k = 5) == 75.0
    assert candidate(quality = [15, 20, 5, 10, 25],wage = [120, 160, 40, 80, 200],k = 5) == 600.0
    assert candidate(quality = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],wage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 8) == 360.0
    assert candidate(quality = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],wage = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225],k = 7) == 196.0
    assert candidate(quality = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 25.0
    assert candidate(quality = [1, 3, 5, 7, 9, 11, 13],wage = [2, 6, 10, 14, 18, 22, 26],k = 5) == 50.0
    assert candidate(quality = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 49.0
    assert candidate(quality = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],wage = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 8) == 3600.0
    assert candidate(quality = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],wage = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 1500.0
    assert candidate(quality = [1, 3, 5, 7, 9, 11, 13],wage = [2, 6, 10, 14, 18, 22, 26],k = 4) == 32.0
    assert candidate(quality = [4, 7, 2, 5, 6],wage = [32, 56, 16, 40, 48],k = 2) == 48.0
    assert candidate(quality = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 25.0
    assert candidate(quality = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],wage = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60],k = 9) == 270.0
    assert candidate(quality = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],wage = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 3) == 6.0
    assert candidate(quality = [4, 5, 1, 2, 3],wage = [40, 50, 10, 20, 30],k = 2) == 30.0
    assert candidate(quality = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],wage = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],k = 7) == 700.0
    assert candidate(quality = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],wage = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 1500.0
    assert candidate(quality = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],wage = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750],k = 8) == 1800.0
    assert candidate(quality = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 28.0
    assert candidate(quality = [10, 12, 14, 16, 18, 20],wage = [70, 84, 98, 112, 126, 140],k = 5) == 490.0
    assert candidate(quality = [2, 3, 5, 7, 11, 13],wage = [14, 21, 35, 49, 77, 91],k = 4) == 119.0
    assert candidate(quality = [30, 10, 40, 20, 50],wage = [90, 30, 120, 60, 150],k = 3) == 180.0
    assert candidate(quality = [2, 4, 6, 8, 10],wage = [10, 20, 30, 40, 50],k = 3) == 60.0
    assert candidate(quality = [100, 200, 300, 400, 500],wage = [1000, 2000, 3000, 4000, 5000],k = 4) == 10000.0
    assert candidate(quality = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 25.0
    assert candidate(quality = [4, 5, 6, 7, 8, 9],wage = [24, 30, 36, 42, 48, 54],k = 4) == 132.0
    assert candidate(quality = [4, 3, 2, 1],wage = [16, 12, 8, 4],k = 2) == 12.0
    assert candidate(quality = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],wage = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1],k = 4) == 34.46153846153846
    assert candidate(quality = [20, 30, 10, 40, 50],wage = [100, 150, 50, 200, 250],k = 4) == 500.0
    assert candidate(quality = [15, 25, 35, 45, 55],wage = [105, 175, 245, 315, 385],k = 3) == 525.0
    assert candidate(quality = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],wage = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 3) == 30.0
    assert candidate(quality = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],wage = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],k = 5) == 27.0
    assert candidate(quality = [7, 14, 21, 28, 35, 42, 49, 56, 63],wage = [14, 28, 42, 56, 70, 84, 98, 112, 126],k = 6) == 294.0
    assert candidate(quality = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],wage = [70, 140, 210, 280, 350, 420, 490, 560, 630, 700],k = 7) == 1960.0
    assert candidate(quality = [10, 20, 30, 40, 50],wage = [50, 40, 30, 20, 10],k = 3) == 120.0
    assert candidate(quality = [4, 2, 8, 5, 10, 7],wage = [40, 20, 80, 50, 100, 70],k = 4) == 180.0
    assert candidate(quality = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],wage = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 3) == 33.75
    assert candidate(quality = [10, 20, 30, 40, 50, 60],wage = [50, 100, 150, 200, 250, 300],k = 6) == 1050.0
    assert candidate(quality = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],wage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 6) == 210.0
    assert candidate(quality = [5, 3, 8, 6, 2],wage = [45, 30, 60, 48, 12],k = 3) == 100.0
    assert candidate(quality = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],wage = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 25.0
    assert candidate(quality = [5, 10, 15, 20, 25, 30, 35],wage = [50, 100, 150, 200, 250, 300, 350],k = 4) == 500.0
    assert candidate(quality = [1, 1, 1, 1, 1, 1, 1, 1],wage = [1, 2, 3, 4, 5, 6, 7, 8],k = 5) == 25.0
    assert candidate(quality = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],wage = [700, 1400, 2100, 2800, 3500, 4200, 4900, 5600, 6300, 7000],k = 7) == 19600.0
    assert candidate(quality = [15, 30, 45, 60, 75, 90, 105],wage = [45, 90, 135, 180, 225, 270, 315],k = 5) == 675.0
    assert candidate(quality = [5, 2, 10, 15, 20, 1],wage = [100, 60, 200, 300, 400, 50],k = 3) == 400.0
    assert candidate(quality = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],wage = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 7) == 2800.0
    assert candidate(quality = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],wage = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000],k = 5) == 3000.0
    assert candidate(quality = [100, 200, 150, 50, 250],wage = [500, 1000, 750, 250, 1250],k = 3) == 1500.0
    assert candidate(quality = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],wage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 7) == 280.0
    assert candidate(quality = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],wage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 150.0
    assert candidate(quality = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],wage = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 6) == 180.0
    assert candidate(quality = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],wage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 8) == 360.0
    assert candidate(quality = [1, 3, 2, 4, 5],wage = [3, 9, 6, 12, 15],k = 3) == 18.0
    assert candidate(quality = [3, 6, 15, 20, 12],wage = [9, 18, 45, 60, 36],k = 3) == 63.0
    assert candidate(quality = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 3) == 9.0
    assert candidate(quality = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],wage = [14, 28, 42, 56, 70, 84, 98, 112, 126, 140, 154, 168, 182, 196, 210],k = 7) == 392.0
    assert candidate(quality = [5, 15, 10, 20, 25],wage = [75, 225, 150, 300, 375],k = 3) == 450.0
    assert candidate(quality = [2, 4, 6, 8, 10],wage = [10, 20, 30, 40, 50],k = 4) == 100.0
    assert candidate(quality = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],wage = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],k = 6) == 1050.0
    assert candidate(quality = [1, 2, 4, 8, 16, 32, 64],wage = [1, 2, 4, 8, 16, 32, 64],k = 4) == 15.0
    assert candidate(quality = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],wage = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60],k = 6) == 126.0
    assert candidate(quality = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],wage = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],k = 6) == 180.0
    assert candidate(quality = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],wage = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 5) == 31.0
    assert candidate(quality = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],wage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 100.0
    assert candidate(quality = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41],wage = [4, 6, 10, 14, 22, 26, 34, 38, 46, 58, 62, 74, 82],k = 8) == 154.0
    assert candidate(quality = [5, 8, 12, 15, 20, 25, 30],wage = [10, 16, 24, 30, 40, 50, 60],k = 3) == 50.0
    assert candidate(quality = [15, 10, 5, 25, 20],wage = [90, 60, 30, 150, 120],k = 3) == 180.0
    assert candidate(quality = [15, 25, 10, 40, 30],wage = [105, 175, 70, 280, 210],k = 3) == 350.0
    assert candidate(quality = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60],wage = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120],k = 8) == 432.0
    assert candidate(quality = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],wage = [10, 40, 90, 160, 250, 360, 490, 640, 810, 1000],k = 6) == 1260.0
    assert candidate(quality = [8, 6, 4, 2, 10],wage = [96, 72, 48, 24, 120],k = 4) == 240.0
    assert candidate(quality = [7, 14, 3, 11, 9],wage = [28, 56, 12, 44, 36],k = 4) == 120.0
    assert candidate(quality = [100, 200, 300, 400, 500, 600, 700],wage = [700, 1400, 2100, 2800, 3500, 4200, 4900],k = 5) == 10500.0
    assert candidate(quality = [3, 5, 2, 8, 7],wage = [6, 10, 4, 16, 14],k = 3) == 20.0
    assert candidate(quality = [5, 3, 10, 2, 4],wage = [50, 30, 100, 20, 40],k = 3) == 90.0


