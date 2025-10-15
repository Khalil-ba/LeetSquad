def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(flowers = [10, 20, 30, 40, 50],newFlowers = 100,target = 25,full = 5,partial = 2) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [10, 20, 30, 40, 50],newFlowers = 100,target = 25,full = 5,partial = 2) == 68: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 1, 1, 1],newFlowers = 15,target = 3,full = 5,partial = 3) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 1, 1, 1],newFlowers = 15,target = 3,full = 5,partial = 3) == 21: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [5, 5, 5, 5],newFlowers = 10,target = 5,full = 10,partial = 5) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [5, 5, 5, 5],newFlowers = 10,target = 5,full = 10,partial = 5) == 40: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [10, 20, 30],newFlowers = 100,target = 25,full = 50,partial = 10) == 340
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [10, 20, 30],newFlowers = 100,target = 25,full = 50,partial = 10) == 340: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [10, 1, 2, 3],newFlowers = 15,target = 10,full = 5,partial = 2) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [10, 1, 2, 3],newFlowers = 15,target = 10,full = 5,partial = 2) == 20: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5],newFlowers = 15,target = 5,full = 10,partial = 5) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5],newFlowers = 15,target = 5,full = 10,partial = 5) == 60: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [5, 5, 5, 5],newFlowers = 10,target = 5,full = 10,partial = 1) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [5, 5, 5, 5],newFlowers = 10,target = 5,full = 10,partial = 1) == 40: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [2, 4, 5, 3],newFlowers = 10,target = 5,full = 2,partial = 6) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [2, 4, 5, 3],newFlowers = 10,target = 5,full = 2,partial = 6) == 30: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [100000, 100000, 100000],newFlowers = 300000,target = 100000,full = 100000,partial = 100000) == 300000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [100000, 100000, 100000],newFlowers = 300000,target = 100000,full = 100000,partial = 100000) == 300000: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5],newFlowers = 15,target = 4,full = 20,partial = 5) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5],newFlowers = 15,target = 4,full = 20,partial = 5) == 100: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [10, 10, 10],newFlowers = 0,target = 10,full = 100,partial = 50) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [10, 10, 10],newFlowers = 0,target = 10,full = 100,partial = 50) == 300: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5],newFlowers = 15,target = 5,full = 10,partial = 3) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5],newFlowers = 15,target = 5,full = 10,partial = 3) == 52: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [5, 5, 5, 5],newFlowers = 10,target = 5,full = 10,partial = 10) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [5, 5, 5, 5],newFlowers = 10,target = 5,full = 10,partial = 10) == 40: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [5, 5, 5, 5],newFlowers = 10,target = 5,full = 2,partial = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [5, 5, 5, 5],newFlowers = 10,target = 5,full = 2,partial = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 1, 1, 1],newFlowers = 20,target = 3,full = 7,partial = 3) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 1, 1, 1],newFlowers = 20,target = 3,full = 7,partial = 3) == 28: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 3, 1, 1],newFlowers = 7,target = 6,full = 12,partial = 1) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 3, 1, 1],newFlowers = 7,target = 6,full = 12,partial = 1) == 14: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],newFlowers = 100,target = 10,full = 100,partial = 1) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],newFlowers = 100,target = 10,full = 100,partial = 1) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],newFlowers = 100,target = 10,full = 30,partial = 20) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],newFlowers = 100,target = 10,full = 30,partial = 20) == 450: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],newFlowers = 1000000,target = 50000,full = 500,partial = 250) == 12504250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],newFlowers = 1000000,target = 50000,full = 500,partial = 250) == 12504250: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [50000, 100000, 25000, 75000],newFlowers = 100000,target = 80000,full = 500,partial = 200) == 16001300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [50000, 100000, 25000, 75000],newFlowers = 100000,target = 80000,full = 500,partial = 200) == 16001300: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],newFlowers = 10000,target = 2000,full = 1000,partial = 500) == 1008500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],newFlowers = 10000,target = 2000,full = 1000,partial = 500) == 1008500: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 7,full = 15,partial = 3) == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 7,full = 15,partial = 3) == 153: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],newFlowers = 10000000000,target = 500000000,full = 100000,partial = 50000) == 25000000850000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],newFlowers = 10000000000,target = 500000000,full = 100000,partial = 50000) == 25000000850000: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 500,target = 55,full = 15,partial = 7) == 513
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 500,target = 55,full = 15,partial = 7) == 513: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],newFlowers = 1000000,target = 90000,full = 1000,partial = 500) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],newFlowers = 1000000,target = 90000,full = 1000,partial = 500) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 10, 100, 1000, 10000, 100000],newFlowers = 100000,target = 50000,full = 1000,partial = 500) == 11112000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 10, 100, 1000, 10000, 100000],newFlowers = 100000,target = 50000,full = 1000,partial = 500) == 11112000: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 5, 9, 13, 17, 21],newFlowers = 25,target = 15,full = 10,partial = 3) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 5, 9, 13, 17, 21],newFlowers = 25,target = 15,full = 10,partial = 3) == 74: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],newFlowers = 1000000,target = 100000,full = 1,partial = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],newFlowers = 1000000,target = 100000,full = 1,partial = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [50, 40, 30, 20, 10, 0, 0, 0, 0, 0],newFlowers = 150,target = 35,full = 100,partial = 20) == 940
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [50, 40, 30, 20, 10, 0, 0, 0, 0, 0],newFlowers = 150,target = 35,full = 100,partial = 20) == 940: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],newFlowers = 10000000000,target = 100000,full = 1000,partial = 500) == 50008500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],newFlowers = 10000000000,target = 100000,full = 1000,partial = 500) == 50008500: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],newFlowers = 5000,target = 500,full = 100,partial = 50) == 25850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],newFlowers = 5000,target = 500,full = 100,partial = 50) == 25850: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],newFlowers = 50,target = 10,full = 15,partial = 5) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],newFlowers = 50,target = 10,full = 15,partial = 5) == 180: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],newFlowers = 50,target = 8,full = 50,partial = 10) == 770
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],newFlowers = 50,target = 8,full = 50,partial = 10) == 770: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],newFlowers = 50,target = 8,full = 20,partial = 5) == 215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],newFlowers = 50,target = 8,full = 20,partial = 5) == 215: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 100,target = 5,full = 20,partial = 15) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 100,target = 5,full = 20,partial = 15) == 240: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],newFlowers = 100,target = 4,full = 100,partial = 50) == 1050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],newFlowers = 100,target = 4,full = 100,partial = 50) == 1050: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1000,target = 5,full = 10,partial = 1) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1000,target = 5,full = 10,partial = 1) == 100: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],newFlowers = 50,target = 5,full = 100,partial = 50) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],newFlowers = 50,target = 5,full = 100,partial = 50) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],newFlowers = 150,target = 35,full = 20,partial = 3) == 249
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],newFlowers = 150,target = 35,full = 20,partial = 3) == 249: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1000,target = 10,full = 20,partial = 10) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1000,target = 10,full = 20,partial = 10) == 270: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],newFlowers = 1000,target = 5,full = 100,partial = 50) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],newFlowers = 1000,target = 5,full = 100,partial = 50) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],newFlowers = 100,target = 10,full = 30,partial = 15) == 555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],newFlowers = 100,target = 10,full = 30,partial = 15) == 555: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],newFlowers = 1000000,target = 100000,full = 100000,partial = 100000) == 8030300000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],newFlowers = 1000000,target = 100000,full = 100000,partial = 100000) == 8030300000: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],newFlowers = 1000,target = 100,full = 50,partial = 25) == 3175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],newFlowers = 1000,target = 100,full = 50,partial = 25) == 3175: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 10000000000,target = 1,full = 100,partial = 50) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 10000000000,target = 1,full = 100,partial = 50) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],newFlowers = 500,target = 20,full = 150,partial = 75) == 5775
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],newFlowers = 500,target = 20,full = 150,partial = 75) == 5775: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],newFlowers = 500,target = 15,full = 25,partial = 10) == 615
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],newFlowers = 500,target = 15,full = 25,partial = 10) == 615: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 5,full = 10,partial = 3) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 5,full = 10,partial = 3) == 102: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [99990, 99991, 99992, 99993, 99994, 99995, 99996, 99997, 99998, 99999],newFlowers = 100000,target = 100000,full = 100000,partial = 100000) == 10000800000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [99990, 99991, 99992, 99993, 99994, 99995, 99996, 99997, 99998, 99999],newFlowers = 100000,target = 100000,full = 100000,partial = 100000) == 10000800000: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],newFlowers = 100,target = 11,full = 50,partial = 25) == 950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],newFlowers = 100,target = 11,full = 50,partial = 25) == 950: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 100,target = 5,full = 50,partial = 20) == 530
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 100,target = 5,full = 50,partial = 20) == 530: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [90, 90, 90, 90, 90, 90, 90, 90, 90, 90],newFlowers = 100,target = 95,full = 1000,partial = 500) == 56000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [90, 90, 90, 90, 90, 90, 90, 90, 90, 90],newFlowers = 100,target = 95,full = 1000,partial = 500) == 56000: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [90000, 80000, 70000, 60000, 50000],newFlowers = 300000,target = 100000,full = 1000,partial = 500) == 50003500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [90000, 80000, 70000, 60000, 50000],newFlowers = 300000,target = 100000,full = 1000,partial = 500) == 50003500: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1,target = 1,full = 100,partial = 50) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1,target = 1,full = 100,partial = 50) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],newFlowers = 300,target = 15,full = 100,partial = 50) == 2600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],newFlowers = 300,target = 15,full = 100,partial = 50) == 2600: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 10,full = 20,partial = 10) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 10,full = 20,partial = 10) == 270: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 10000000000,target = 2,full = 1,partial = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 10000000000,target = 2,full = 1,partial = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 1000,target = 60,full = 50,partial = 25) == 1925
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 1000,target = 60,full = 50,partial = 25) == 1925: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1000,target = 5,full = 100,partial = 10) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1000,target = 5,full = 100,partial = 10) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 1000,target = 55,full = 50,partial = 10) == 990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 1000,target = 55,full = 50,partial = 10) == 990: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 7,full = 20,partial = 5) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 7,full = 20,partial = 5) == 210: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],newFlowers = 100,target = 10,full = 20,partial = 5) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],newFlowers = 100,target = 10,full = 20,partial = 5) == 225: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],newFlowers = 1000000,target = 100000,full = 100000,partial = 50000) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],newFlowers = 1000000,target = 100000,full = 100000,partial = 50000) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],newFlowers = 50,target = 10,full = 20,partial = 10) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],newFlowers = 50,target = 10,full = 20,partial = 10) == 270: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],newFlowers = 500,target = 3,full = 20,partial = 10) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],newFlowers = 500,target = 3,full = 20,partial = 10) == 200: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],newFlowers = 500,target = 45,full = 50,partial = 10) == 890
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],newFlowers = 500,target = 45,full = 50,partial = 10) == 890: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [5, 5, 5, 5, 5],newFlowers = 25,target = 7,full = 50,partial = 5) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [5, 5, 5, 5, 5],newFlowers = 25,target = 7,full = 50,partial = 5) == 250: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],newFlowers = 3000,target = 500,full = 50,partial = 25) == 12925
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],newFlowers = 3000,target = 500,full = 50,partial = 25) == 12925: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],newFlowers = 50,target = 10,full = 10,partial = 1) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],newFlowers = 50,target = 10,full = 10,partial = 1) == 100: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97],newFlowers = 100000,target = 10000,full = 1000,partial = 500) == 5008500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97],newFlowers = 100000,target = 10000,full = 1000,partial = 500) == 5008500: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],newFlowers = 20,target = 6,full = 20,partial = 10) == 230
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],newFlowers = 20,target = 6,full = 20,partial = 10) == 230: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],newFlowers = 5000,target = 500,full = 1000,partial = 100) == 58900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],newFlowers = 5000,target = 500,full = 1000,partial = 100) == 58900: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 1000,target = 60,full = 50,partial = 10) == 1040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 1000,target = 60,full = 50,partial = 10) == 1040: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1000,target = 5,full = 100,partial = 50) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1000,target = 5,full = 100,partial = 50) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [50, 30, 20, 10, 5],newFlowers = 150,target = 25,full = 10,partial = 5) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [50, 30, 20, 10, 5],newFlowers = 150,target = 25,full = 10,partial = 5) == 160: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1000,target = 2,full = 50,partial = 25) == 4250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1000,target = 2,full = 50,partial = 25) == 4250: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 30,target = 6,full = 10,partial = 3) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 30,target = 6,full = 10,partial = 3) == 105: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 0,target = 5,full = 50,partial = 10) == 310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 0,target = 5,full = 50,partial = 10) == 310: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1000,target = 5,full = 100,partial = 50) == 8400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1000,target = 5,full = 100,partial = 50) == 8400: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],newFlowers = 100,target = 10,full = 20,partial = 10) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],newFlowers = 100,target = 10,full = 20,partial = 10) == 270: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],newFlowers = 1000,target = 40,full = 50,partial = 20) == 1230
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],newFlowers = 1000,target = 40,full = 50,partial = 20) == 1230: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20],newFlowers = 200,target = 25,full = 100,partial = 50) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20],newFlowers = 200,target = 25,full = 100,partial = 50) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 500,target = 40,full = 20,partial = 10) == 570
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 500,target = 40,full = 20,partial = 10) == 570: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],newFlowers = 700,target = 20,full = 50,partial = 20) == 1580
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],newFlowers = 700,target = 20,full = 50,partial = 20) == 1580: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [100, 200, 300, 400, 500],newFlowers = 1000,target = 350,full = 15,partial = 5) == 1805
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [100, 200, 300, 400, 500],newFlowers = 1000,target = 350,full = 15,partial = 5) == 1805: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 15,target = 5,full = 100,partial = 10) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 15,target = 5,full = 100,partial = 10) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 150,target = 80,full = 150,partial = 75) == 4950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 150,target = 80,full = 150,partial = 75) == 4950: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 30,target = 7,full = 10,partial = 5) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 30,target = 7,full = 10,partial = 5) == 120: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 1,target = 1,full = 1000,partial = 500) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 1,target = 1,full = 1000,partial = 500) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],newFlowers = 200,target = 55,full = 100,partial = 50) == 3600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],newFlowers = 200,target = 55,full = 100,partial = 50) == 3600: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],newFlowers = 50,target = 10,full = 100,partial = 50) == 1350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],newFlowers = 50,target = 10,full = 100,partial = 50) == 1350: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],newFlowers = 1000000,target = 50000,full = 1000,partial = 500) == 25008500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],newFlowers = 1000000,target = 50000,full = 1000,partial = 500) == 25008500: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 250,target = 5,full = 100,partial = 50) == 1100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 250,target = 5,full = 100,partial = 50) == 1100: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],newFlowers = 500,target = 15,full = 75,partial = 35) == 1915
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],newFlowers = 500,target = 15,full = 75,partial = 35) == 1915: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 8,full = 20,partial = 10) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 8,full = 20,partial = 10) == 250: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 0],newFlowers = 150000,target = 60000,full = 500,partial = 200) == 10002000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 0],newFlowers = 150000,target = 60000,full = 500,partial = 200) == 10002000: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 100,target = 5,full = 100,partial = 50) == 1100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 100,target = 5,full = 100,partial = 50) == 1100: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 7,full = 100,partial = 50) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 7,full = 100,partial = 50) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 100,target = 5,full = 50,partial = 25) == 1050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 100,target = 5,full = 50,partial = 25) == 1050: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],newFlowers = 45,target = 5,full = 15,partial = 10) == 175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],newFlowers = 45,target = 5,full = 15,partial = 10) == 175: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],newFlowers = 250,target = 30,full = 200,partial = 100) == 4700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],newFlowers = 250,target = 30,full = 200,partial = 100) == 4700: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],newFlowers = 100,target = 7,full = 20,partial = 5) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],newFlowers = 100,target = 7,full = 20,partial = 5) == 210: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5],newFlowers = 1000000,target = 10,full = 100000,partial = 10000) == 500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5],newFlowers = 1000000,target = 10,full = 100000,partial = 10000) == 500000: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [2, 4, 6, 8, 10, 12, 14],newFlowers = 30,target = 15,full = 7,partial = 5) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [2, 4, 6, 8, 10, 12, 14],newFlowers = 30,target = 15,full = 7,partial = 5) == 71: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],newFlowers = 10000,target = 995,full = 100,partial = 50) == 50600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],newFlowers = 10000,target = 995,full = 100,partial = 50) == 50600: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 500,target = 75,full = 1000,partial = 100) == 16400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 500,target = 75,full = 1000,partial = 100) == 16400: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],newFlowers = 5000,target = 750,full = 250,partial = 125) == 97125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],newFlowers = 5000,target = 750,full = 250,partial = 125) == 97125: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],newFlowers = 200,target = 10,full = 50,partial = 25) == 925
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],newFlowers = 200,target = 10,full = 50,partial = 25) == 925: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 10,full = 10,partial = 1) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 10,full = 10,partial = 1) == 100: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [100000, 99999, 99998, 99997, 99996, 99995],newFlowers = 150000,target = 100000,full = 100000,partial = 100000) == 10000400000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [100000, 99999, 99998, 99997, 99996, 99995],newFlowers = 150000,target = 100000,full = 100000,partial = 100000) == 10000400000: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 5, 9, 13, 17, 21],newFlowers = 20,target = 15,full = 10,partial = 3) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 5, 9, 13, 17, 21],newFlowers = 20,target = 15,full = 10,partial = 3) == 67: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [50, 40, 30, 20, 10],newFlowers = 100,target = 35,full = 100,partial = 50) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [50, 40, 30, 20, 10],newFlowers = 100,target = 35,full = 100,partial = 50) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 100,target = 5,full = 5,partial = 2) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 100,target = 5,full = 5,partial = 2) == 53: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(flowers = [10, 20, 30, 40, 50],newFlowers = 100,target = 25,full = 5,partial = 2) == 68
    assert candidate(flowers = [1, 1, 1, 1],newFlowers = 15,target = 3,full = 5,partial = 3) == 21
    assert candidate(flowers = [5, 5, 5, 5],newFlowers = 10,target = 5,full = 10,partial = 5) == 40
    assert candidate(flowers = [10, 20, 30],newFlowers = 100,target = 25,full = 50,partial = 10) == 340
    assert candidate(flowers = [10, 1, 2, 3],newFlowers = 15,target = 10,full = 5,partial = 2) == 20
    assert candidate(flowers = [1, 2, 3, 4, 5],newFlowers = 15,target = 5,full = 10,partial = 5) == 60
    assert candidate(flowers = [5, 5, 5, 5],newFlowers = 10,target = 5,full = 10,partial = 1) == 40
    assert candidate(flowers = [2, 4, 5, 3],newFlowers = 10,target = 5,full = 2,partial = 6) == 30
    assert candidate(flowers = [100000, 100000, 100000],newFlowers = 300000,target = 100000,full = 100000,partial = 100000) == 300000
    assert candidate(flowers = [1, 2, 3, 4, 5],newFlowers = 15,target = 4,full = 20,partial = 5) == 100
    assert candidate(flowers = [10, 10, 10],newFlowers = 0,target = 10,full = 100,partial = 50) == 300
    assert candidate(flowers = [1, 2, 3, 4, 5],newFlowers = 15,target = 5,full = 10,partial = 3) == 52
    assert candidate(flowers = [5, 5, 5, 5],newFlowers = 10,target = 5,full = 10,partial = 10) == 40
    assert candidate(flowers = [5, 5, 5, 5],newFlowers = 10,target = 5,full = 2,partial = 6) == 8
    assert candidate(flowers = [1, 1, 1, 1],newFlowers = 20,target = 3,full = 7,partial = 3) == 28
    assert candidate(flowers = [1, 3, 1, 1],newFlowers = 7,target = 6,full = 12,partial = 1) == 14
    assert candidate(flowers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],newFlowers = 100,target = 10,full = 100,partial = 1) == 1000
    assert candidate(flowers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],newFlowers = 100,target = 10,full = 30,partial = 20) == 450
    assert candidate(flowers = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],newFlowers = 1000000,target = 50000,full = 500,partial = 250) == 12504250
    assert candidate(flowers = [50000, 100000, 25000, 75000],newFlowers = 100000,target = 80000,full = 500,partial = 200) == 16001300
    assert candidate(flowers = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],newFlowers = 10000,target = 2000,full = 1000,partial = 500) == 1008500
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 7,full = 15,partial = 3) == 153
    assert candidate(flowers = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],newFlowers = 10000000000,target = 500000000,full = 100000,partial = 50000) == 25000000850000
    assert candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 500,target = 55,full = 15,partial = 7) == 513
    assert candidate(flowers = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],newFlowers = 1000000,target = 90000,full = 1000,partial = 500) == 10000
    assert candidate(flowers = [1, 10, 100, 1000, 10000, 100000],newFlowers = 100000,target = 50000,full = 1000,partial = 500) == 11112000
    assert candidate(flowers = [1, 5, 9, 13, 17, 21],newFlowers = 25,target = 15,full = 10,partial = 3) == 74
    assert candidate(flowers = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],newFlowers = 1000000,target = 100000,full = 1,partial = 1) == 10
    assert candidate(flowers = [50, 40, 30, 20, 10, 0, 0, 0, 0, 0],newFlowers = 150,target = 35,full = 100,partial = 20) == 940
    assert candidate(flowers = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],newFlowers = 10000000000,target = 100000,full = 1000,partial = 500) == 50008500
    assert candidate(flowers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],newFlowers = 5000,target = 500,full = 100,partial = 50) == 25850
    assert candidate(flowers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],newFlowers = 50,target = 10,full = 15,partial = 5) == 180
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],newFlowers = 50,target = 8,full = 50,partial = 10) == 770
    assert candidate(flowers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],newFlowers = 50,target = 8,full = 20,partial = 5) == 215
    assert candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 100,target = 5,full = 20,partial = 15) == 240
    assert candidate(flowers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],newFlowers = 100,target = 4,full = 100,partial = 50) == 1050
    assert candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1000,target = 5,full = 10,partial = 1) == 100
    assert candidate(flowers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],newFlowers = 50,target = 5,full = 100,partial = 50) == 1000
    assert candidate(flowers = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],newFlowers = 150,target = 35,full = 20,partial = 3) == 249
    assert candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1000,target = 10,full = 20,partial = 10) == 270
    assert candidate(flowers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],newFlowers = 1000,target = 5,full = 100,partial = 50) == 1000
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],newFlowers = 100,target = 10,full = 30,partial = 15) == 555
    assert candidate(flowers = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],newFlowers = 1000000,target = 100000,full = 100000,partial = 100000) == 8030300000
    assert candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],newFlowers = 1000,target = 100,full = 50,partial = 25) == 3175
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 10000000000,target = 1,full = 100,partial = 50) == 1000
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],newFlowers = 500,target = 20,full = 150,partial = 75) == 5775
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],newFlowers = 500,target = 15,full = 25,partial = 10) == 615
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 5,full = 10,partial = 3) == 102
    assert candidate(flowers = [99990, 99991, 99992, 99993, 99994, 99995, 99996, 99997, 99998, 99999],newFlowers = 100000,target = 100000,full = 100000,partial = 100000) == 10000800000
    assert candidate(flowers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],newFlowers = 100,target = 11,full = 50,partial = 25) == 950
    assert candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 100,target = 5,full = 50,partial = 20) == 530
    assert candidate(flowers = [90, 90, 90, 90, 90, 90, 90, 90, 90, 90],newFlowers = 100,target = 95,full = 1000,partial = 500) == 56000
    assert candidate(flowers = [90000, 80000, 70000, 60000, 50000],newFlowers = 300000,target = 100000,full = 1000,partial = 500) == 50003500
    assert candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1,target = 1,full = 100,partial = 50) == 1000
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],newFlowers = 300,target = 15,full = 100,partial = 50) == 2600
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 10,full = 20,partial = 10) == 270
    assert candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 10000000000,target = 2,full = 1,partial = 1) == 10
    assert candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 1000,target = 60,full = 50,partial = 25) == 1925
    assert candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1000,target = 5,full = 100,partial = 10) == 1000
    assert candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 1000,target = 55,full = 50,partial = 10) == 990
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 7,full = 20,partial = 5) == 210
    assert candidate(flowers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],newFlowers = 100,target = 10,full = 20,partial = 5) == 225
    assert candidate(flowers = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],newFlowers = 1000000,target = 100000,full = 100000,partial = 50000) == 1000000
    assert candidate(flowers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],newFlowers = 50,target = 10,full = 20,partial = 10) == 270
    assert candidate(flowers = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],newFlowers = 500,target = 3,full = 20,partial = 10) == 200
    assert candidate(flowers = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],newFlowers = 500,target = 45,full = 50,partial = 10) == 890
    assert candidate(flowers = [5, 5, 5, 5, 5],newFlowers = 25,target = 7,full = 50,partial = 5) == 250
    assert candidate(flowers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],newFlowers = 3000,target = 500,full = 50,partial = 25) == 12925
    assert candidate(flowers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],newFlowers = 50,target = 10,full = 10,partial = 1) == 100
    assert candidate(flowers = [50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97],newFlowers = 100000,target = 10000,full = 1000,partial = 500) == 5008500
    assert candidate(flowers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],newFlowers = 20,target = 6,full = 20,partial = 10) == 230
    assert candidate(flowers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],newFlowers = 5000,target = 500,full = 1000,partial = 100) == 58900
    assert candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 1000,target = 60,full = 50,partial = 10) == 1040
    assert candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1000,target = 5,full = 100,partial = 50) == 2100
    assert candidate(flowers = [50, 30, 20, 10, 5],newFlowers = 150,target = 25,full = 10,partial = 5) == 160
    assert candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1000,target = 2,full = 50,partial = 25) == 4250
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 30,target = 6,full = 10,partial = 3) == 105
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 0,target = 5,full = 50,partial = 10) == 310
    assert candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 1000,target = 5,full = 100,partial = 50) == 8400
    assert candidate(flowers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],newFlowers = 100,target = 10,full = 20,partial = 10) == 270
    assert candidate(flowers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],newFlowers = 1000,target = 40,full = 50,partial = 20) == 1230
    assert candidate(flowers = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20],newFlowers = 200,target = 25,full = 100,partial = 50) == 2100
    assert candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 500,target = 40,full = 20,partial = 10) == 570
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],newFlowers = 700,target = 20,full = 50,partial = 20) == 1580
    assert candidate(flowers = [100, 200, 300, 400, 500],newFlowers = 1000,target = 350,full = 15,partial = 5) == 1805
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 15,target = 5,full = 100,partial = 10) == 1000
    assert candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 150,target = 80,full = 150,partial = 75) == 4950
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 30,target = 7,full = 10,partial = 5) == 120
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 1,target = 1,full = 1000,partial = 500) == 10000
    assert candidate(flowers = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],newFlowers = 200,target = 55,full = 100,partial = 50) == 3600
    assert candidate(flowers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],newFlowers = 50,target = 10,full = 100,partial = 50) == 1350
    assert candidate(flowers = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],newFlowers = 1000000,target = 50000,full = 1000,partial = 500) == 25008500
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 250,target = 5,full = 100,partial = 50) == 1100
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],newFlowers = 500,target = 15,full = 75,partial = 35) == 1915
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 8,full = 20,partial = 10) == 250
    assert candidate(flowers = [90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 0],newFlowers = 150000,target = 60000,full = 500,partial = 200) == 10002000
    assert candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 100,target = 5,full = 100,partial = 50) == 1100
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 7,full = 100,partial = 50) == 1200
    assert candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 100,target = 5,full = 50,partial = 25) == 1050
    assert candidate(flowers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],newFlowers = 45,target = 5,full = 15,partial = 10) == 175
    assert candidate(flowers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],newFlowers = 250,target = 30,full = 200,partial = 100) == 4700
    assert candidate(flowers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],newFlowers = 100,target = 7,full = 20,partial = 5) == 210
    assert candidate(flowers = [1, 2, 3, 4, 5],newFlowers = 1000000,target = 10,full = 100000,partial = 10000) == 500000
    assert candidate(flowers = [2, 4, 6, 8, 10, 12, 14],newFlowers = 30,target = 15,full = 7,partial = 5) == 71
    assert candidate(flowers = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],newFlowers = 10000,target = 995,full = 100,partial = 50) == 50600
    assert candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],newFlowers = 500,target = 75,full = 1000,partial = 100) == 16400
    assert candidate(flowers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],newFlowers = 5000,target = 750,full = 250,partial = 125) == 97125
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],newFlowers = 200,target = 10,full = 50,partial = 25) == 925
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],newFlowers = 50,target = 10,full = 10,partial = 1) == 100
    assert candidate(flowers = [100000, 99999, 99998, 99997, 99996, 99995],newFlowers = 150000,target = 100000,full = 100000,partial = 100000) == 10000400000
    assert candidate(flowers = [1, 5, 9, 13, 17, 21],newFlowers = 20,target = 15,full = 10,partial = 3) == 67
    assert candidate(flowers = [50, 40, 30, 20, 10],newFlowers = 100,target = 35,full = 100,partial = 50) == 2100
    assert candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],newFlowers = 100,target = 5,full = 5,partial = 2) == 53


