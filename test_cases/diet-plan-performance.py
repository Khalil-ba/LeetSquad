def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(calories = [6, 5, 0, 0],k = 2,lower = 1,upper = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [6, 5, 0, 0],k = 2,lower = 1,upper = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [100, 200, 300, 400, 500, 600, 700],k = 4,lower = 1000,upper = 2000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [100, 200, 300, 400, 500, 600, 700],k = 4,lower = 1000,upper = 2000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(calories = [5000, 5000, 5000, 5000, 5000],k = 5,lower = 20000,upper = 25000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [5000, 5000, 5000, 5000, 5000],k = 5,lower = 20000,upper = 25000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1, 2, 3, 4, 5],k = 1,lower = 3,upper = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1, 2, 3, 4, 5],k = 1,lower = 3,upper = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [7, 7, 7, 7, 7, 7, 7],k = 7,lower = 21,upper = 21) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [7, 7, 7, 7, 7, 7, 7],k = 7,lower = 21,upper = 21) == 1: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1, 3, 2, 4, 3, 1],k = 3,lower = 2,upper = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1, 3, 2, 4, 3, 1],k = 3,lower = 2,upper = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(calories = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5,lower = 20,upper = 30) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5,lower = 20,upper = 30) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3,lower = 15,upper = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3,lower = 15,upper = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3,lower = 10,upper = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3,lower = 10,upper = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(calories = [3, 2],k = 2,lower = 0,upper = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [3, 2],k = 2,lower = 0,upper = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(calories = [10000, 20000, 15000, 5000, 25000],k = 3,lower = 30000,upper = 40000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [10000, 20000, 15000, 5000, 25000],k = 3,lower = 30000,upper = 40000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 5,lower = 15000,upper = 30000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 5,lower = 15000,upper = 30000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(calories = [2000, 1500, 1000, 500, 0, 500, 1000, 1500, 2000, 2500],k = 3,lower = 3000,upper = 4500) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [2000, 1500, 1000, 500, 0, 500, 1000, 1500, 2000, 2500],k = 3,lower = 3000,upper = 4500) == -2: {e}')
    
    total += 1
    try:
        result = candidate(calories = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 0, 1000, 2000, 3000, 4000, 5000],k = 5,lower = 15000,upper = 25000) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 0, 1000, 2000, 3000, 4000, 5000],k = 5,lower = 15000,upper = 25000) == -2: {e}')
    
    total += 1
    try:
        result = candidate(calories = [2000, 1500, 1000, 500, 0, 500, 1000, 1500, 2000, 2500],k = 3,lower = 2500,upper = 4500) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [2000, 1500, 1000, 500, 0, 500, 1000, 1500, 2000, 2500],k = 3,lower = 2500,upper = 4500) == -2: {e}')
    
    total += 1
    try:
        result = candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 10,lower = 15000,upper = 25000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 10,lower = 15000,upper = 25000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 10,lower = 4500,upper = 6000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 10,lower = 4500,upper = 6000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 10,lower = 8000,upper = 12000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 10,lower = 8000,upper = 12000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [0, 20000, 0, 20000, 0, 20000, 0, 20000, 0, 20000],k = 2,lower = 10000,upper = 30000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [0, 20000, 0, 20000, 0, 20000, 0, 20000, 0, 20000],k = 2,lower = 10000,upper = 30000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500],k = 10,lower = 12000,upper = 18000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500],k = 10,lower = 12000,upper = 18000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000],k = 2,lower = 4000,upper = 10000) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000],k = 2,lower = 4000,upper = 10000) == 6: {e}')
    
    total += 1
    try:
        result = candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 5,lower = 10000,upper = 15000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 5,lower = 10000,upper = 15000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 5,lower = 8000,upper = 12000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 5,lower = 8000,upper = 12000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 2,lower = 400,upper = 600) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 2,lower = 400,upper = 600) == 6: {e}')
    
    total += 1
    try:
        result = candidate(calories = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],k = 10,lower = 40000,upper = 60000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],k = 10,lower = 40000,upper = 60000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],k = 3,lower = 3000,upper = 4500) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],k = 3,lower = 3000,upper = 4500) == 6: {e}')
    
    total += 1
    try:
        result = candidate(calories = [500, 1500, 1000, 1500, 500, 1500, 1000, 1500, 500, 1500, 1000, 1500],k = 6,lower = 6000,upper = 9000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [500, 1500, 1000, 1500, 500, 1500, 1000, 1500, 500, 1500, 1000, 1500],k = 6,lower = 6000,upper = 9000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300],k = 2,lower = 500,upper = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300],k = 2,lower = 500,upper = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [10000, 5000, 15000, 10000, 20000, 15000, 25000, 20000, 30000, 25000, 35000, 30000, 40000, 35000, 45000, 40000, 50000, 45000, 55000, 50000],k = 5,lower = 50000,upper = 100000) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [10000, 5000, 15000, 10000, 20000, 15000, 25000, 20000, 30000, 25000, 35000, 30000, 40000, 35000, 45000, 40000, 50000, 45000, 55000, 50000],k = 5,lower = 50000,upper = 100000) == 12: {e}')
    
    total += 1
    try:
        result = candidate(calories = [2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500],k = 10,lower = 50000,upper = 60000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500],k = 10,lower = 50000,upper = 60000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 5,lower = 4000,upper = 6000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 5,lower = 4000,upper = 6000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 3,lower = 5000,upper = 6000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 3,lower = 5000,upper = 6000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [4000, 3000, 2000, 1000, 500, 0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000],k = 5,lower = 10000,upper = 15000) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [4000, 3000, 2000, 1000, 500, 0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000],k = 5,lower = 10000,upper = 15000) == -6: {e}')
    
    total += 1
    try:
        result = candidate(calories = [6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000],k = 5,lower = 40000,upper = 50000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000],k = 5,lower = 40000,upper = 50000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(calories = [8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 500, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5,lower = 25000,upper = 35000) == -14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 500, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5,lower = 25000,upper = 35000) == -14: {e}')
    
    total += 1
    try:
        result = candidate(calories = [20000, 20000, 20000, 20000, 20000, 20000, 20000],k = 7,lower = 140000,upper = 140000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [20000, 20000, 20000, 20000, 20000, 20000, 20000],k = 7,lower = 140000,upper = 140000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [10000, 5000, 15000, 10000, 5000, 15000, 10000, 5000, 15000, 10000],k = 3,lower = 20000,upper = 30000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [10000, 5000, 15000, 10000, 5000, 15000, 10000, 5000, 15000, 10000],k = 3,lower = 20000,upper = 30000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [500, 1500, 1000, 2000, 2500, 1200, 1800, 3000, 1600, 1400, 800, 1000, 600, 1200, 1500, 1300],k = 7,lower = 7000,upper = 10000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [500, 1500, 1000, 2000, 2500, 1200, 1800, 3000, 1600, 1400, 800, 1000, 600, 1200, 1500, 1300],k = 7,lower = 7000,upper = 10000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(calories = [800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700],k = 5,lower = 5000,upper = 7000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700],k = 5,lower = 5000,upper = 7000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(calories = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 1,lower = 5000,upper = 15000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 1,lower = 5000,upper = 15000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],k = 10,lower = 5500,upper = 10500) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],k = 10,lower = 5500,upper = 10500) == 5: {e}')
    
    total += 1
    try:
        result = candidate(calories = [300, 400, 350, 500, 600, 550, 700, 650, 800, 750, 900, 850, 1000, 950, 1100, 1050, 1200],k = 7,lower = 3500,upper = 5500) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [300, 400, 350, 500, 600, 550, 700, 650, 800, 750, 900, 850, 1000, 950, 1100, 1050, 1200],k = 7,lower = 3500,upper = 5500) == 4: {e}')
    
    total += 1
    try:
        result = candidate(calories = [6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000],k = 5,lower = 50000,upper = 60000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000],k = 5,lower = 50000,upper = 60000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3,lower = 10,upper = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3,lower = 10,upper = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(calories = [2000, 1500, 1700, 1600, 1800, 1900, 2100, 2200, 2300, 2400],k = 6,lower = 9000,upper = 12000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [2000, 1500, 1700, 1600, 1800, 1900, 2100, 2200, 2300, 2400],k = 6,lower = 9000,upper = 12000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 20,lower = 38000,upper = 42000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 20,lower = 38000,upper = 42000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 15,lower = 25000,upper = 35000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 15,lower = 25000,upper = 35000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 4,lower = 8000,upper = 12000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 4,lower = 8000,upper = 12000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 3,lower = 15000,upper = 25000) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 3,lower = 15000,upper = 25000) == -2: {e}')
    
    total += 1
    try:
        result = candidate(calories = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000, 100000],k = 10,lower = 450000,upper = 550000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000, 100000],k = 10,lower = 450000,upper = 550000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(calories = [12000, 11000, 13000, 10000, 14000, 9000, 15000, 8000, 16000, 7000],k = 4,lower = 40000,upper = 50000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [12000, 11000, 13000, 10000, 14000, 9000, 15000, 8000, 16000, 7000],k = 4,lower = 40000,upper = 50000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 5,lower = 15000,upper = 25000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 5,lower = 15000,upper = 25000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(calories = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 7,lower = 25000,upper = 35000) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 7,lower = 25000,upper = 35000) == -3: {e}')
    
    total += 1
    try:
        result = candidate(calories = [4000, 3500, 3700, 3600, 3800, 3900, 4100, 4200, 4300, 4400],k = 8,lower = 25000,upper = 30000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [4000, 3500, 3700, 3600, 3800, 3900, 4100, 4200, 4300, 4400],k = 8,lower = 25000,upper = 30000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10,lower = 5,upper = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10,lower = 5,upper = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1000, 1000, 1000, 2000, 2000, 2000, 3000, 3000, 3000, 1000, 1000, 1000],k = 3,lower = 2500,upper = 3500) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1000, 1000, 1000, 2000, 2000, 2000, 3000, 3000, 3000, 1000, 1000, 1000],k = 3,lower = 2500,upper = 3500) == 8: {e}')
    
    total += 1
    try:
        result = candidate(calories = [800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100],k = 5,lower = 4000,upper = 6000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100],k = 5,lower = 4000,upper = 6000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(calories = [2000, 1500, 2500, 3000, 2000, 1000, 3500, 4000, 2500, 1500, 3000, 2000, 1000, 2500, 3000, 2000, 1000, 3500, 4000, 2500],k = 5,lower = 8000,upper = 15000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [2000, 1500, 2500, 3000, 2000, 1000, 3500, 4000, 2500, 1500, 3000, 2000, 1000, 2500, 3000, 2000, 1000, 3500, 4000, 2500],k = 5,lower = 8000,upper = 15000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200],k = 6,lower = 7000,upper = 7200) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200],k = 6,lower = 7000,upper = 7200) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [2000, 2500, 3000, 1500, 3500, 4000, 2000, 1800, 2200, 2700],k = 4,lower = 8000,upper = 12000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [2000, 2500, 3000, 1500, 3500, 4000, 2000, 1800, 2200, 2700],k = 4,lower = 8000,upper = 12000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400],k = 6,lower = 25000,upper = 30000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400],k = 6,lower = 25000,upper = 30000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(calories = [3000, 2500, 2000, 1500, 1000, 500, 0, 500, 1000, 1500],k = 2,lower = 1000,upper = 2000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [3000, 2500, 2000, 1500, 1000, 500, 0, 500, 1000, 1500],k = 2,lower = 1000,upper = 2000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(calories = [3000, 2500, 2700, 2600, 2800, 2900, 3100, 3200, 3300, 3400],k = 7,lower = 18000,upper = 22000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [3000, 2500, 2700, 2600, 2800, 2900, 3100, 3200, 3300, 3400],k = 7,lower = 18000,upper = 22000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [500, 1500, 1000, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000],k = 3,lower = 4000,upper = 6000) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [500, 1500, 1000, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000],k = 3,lower = 4000,upper = 6000) == 6: {e}')
    
    total += 1
    try:
        result = candidate(calories = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400],k = 9,lower = 5000,upper = 10000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400],k = 9,lower = 5000,upper = 10000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5,lower = 40,upper = 60) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5,lower = 40,upper = 60) == 1: {e}')
    
    total += 1
    try:
        result = candidate(calories = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000],k = 6,lower = 20000,upper = 30000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000],k = 6,lower = 20000,upper = 30000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1500, 1200, 2000, 1800, 1900, 1700, 2100, 1600, 1400, 1300],k = 4,lower = 5000,upper = 7000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1500, 1200, 2000, 1800, 1900, 1700, 2100, 1600, 1400, 1300],k = 4,lower = 5000,upper = 7000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(calories = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],k = 10,lower = 50000,upper = 60000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],k = 10,lower = 50000,upper = 60000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1000, 1500, 2000, 2500, 3000, 1000, 1500, 2000, 2500, 3000],k = 3,lower = 4000,upper = 7000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1000, 1500, 2000, 2500, 3000, 1000, 1500, 2000, 2500, 3000],k = 3,lower = 4000,upper = 7000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000],k = 7,lower = 35000,upper = 45000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000],k = 7,lower = 35000,upper = 45000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 5,lower = 2000,upper = 5000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 5,lower = 2000,upper = 5000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1200, 1300, 1100, 1400, 1500, 1600, 1300, 1200, 1100, 1000],k = 4,lower = 5000,upper = 6000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1200, 1300, 1100, 1400, 1500, 1600, 1300, 1200, 1100, 1000],k = 4,lower = 5000,upper = 6000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1200, 1100, 1300, 900, 1400, 1200, 1000, 1100, 1300, 900, 1400, 1200, 1000],k = 4,lower = 4000,upper = 5000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1200, 1100, 1300, 900, 1400, 1200, 1000, 1100, 1300, 900, 1400, 1200, 1000],k = 4,lower = 4000,upper = 5000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 50,lower = 100000,upper = 100000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 50,lower = 100000,upper = 100000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [5000, 10000, 15000, 20000, 25000, 30000, 35000],k = 4,lower = 60000,upper = 80000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [5000, 10000, 15000, 20000, 25000, 30000, 35000],k = 4,lower = 60000,upper = 80000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 3,lower = 5,upper = 15) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 3,lower = 5,upper = 15) == 14: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100],k = 2,lower = 2500,upper = 3000) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100],k = 2,lower = 2500,upper = 3000) == 6: {e}')
    
    total += 1
    try:
        result = candidate(calories = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 3,lower = 25000,upper = 35000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 3,lower = 25000,upper = 35000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 4,lower = 15000,upper = 25000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 4,lower = 15000,upper = 25000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(calories = [3000, 2500, 2000, 1500, 1000, 500, 0, 500, 1000, 1500, 2000, 2500],k = 6,lower = 10000,upper = 15000) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [3000, 2500, 2000, 1500, 1000, 500, 0, 500, 1000, 1500, 2000, 2500],k = 6,lower = 10000,upper = 15000) == -6: {e}')
    
    total += 1
    try:
        result = candidate(calories = [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150],k = 6,lower = 2000,upper = 3000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150],k = 6,lower = 2000,upper = 3000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(calories = [2000, 1800, 2200, 1900, 2100, 1700, 1600, 1500, 2300, 2400, 2500, 2600],k = 5,lower = 10000,upper = 11000) == -4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [2000, 1800, 2200, 1900, 2100, 1700, 1600, 1500, 2300, 2400, 2500, 2600],k = 5,lower = 10000,upper = 11000) == -4: {e}')
    
    total += 1
    try:
        result = candidate(calories = [5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000],k = 5,lower = 35000,upper = 45000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000],k = 5,lower = 35000,upper = 45000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(calories = [2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500],k = 10,lower = 20000,upper = 30000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500],k = 10,lower = 20000,upper = 30000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [12000, 11000, 13000, 14000, 9000, 8000, 15000, 16000, 7000, 6000],k = 4,lower = 40000,upper = 50000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [12000, 11000, 13000, 14000, 9000, 8000, 15000, 16000, 7000, 6000],k = 4,lower = 40000,upper = 50000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(calories = [300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700, 3000, 3300, 3600, 3900, 4200, 4500, 4800, 5100, 5400, 5700, 6000],k = 3,lower = 1500,upper = 2500) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700, 3000, 3300, 3600, 3900, 4200, 4500, 4800, 5100, 5400, 5700, 6000],k = 3,lower = 1500,upper = 2500) == 17: {e}')
    
    total += 1
    try:
        result = candidate(calories = [20000, 15000, 10000, 5000, 25000, 20000, 15000, 10000, 5000, 25000],k = 4,lower = 20000,upper = 40000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [20000, 15000, 10000, 5000, 25000, 20000, 15000, 10000, 5000, 25000],k = 4,lower = 20000,upper = 40000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(calories = [2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500],k = 7,lower = 35000,upper = 45000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500],k = 7,lower = 35000,upper = 45000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(calories = [1000, 2000, 1500, 500, 2500, 3000, 3500, 4000, 4500, 5000],k = 4,lower = 8000,upper = 12000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(calories = [1000, 2000, 1500, 500, 2500, 3000, 3500, 4000, 4500, 5000],k = 4,lower = 8000,upper = 12000) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(calories = [6, 5, 0, 0],k = 2,lower = 1,upper = 5) == 0
    assert candidate(calories = [100, 200, 300, 400, 500, 600, 700],k = 4,lower = 1000,upper = 2000) == 1
    assert candidate(calories = [5000, 5000, 5000, 5000, 5000],k = 5,lower = 20000,upper = 25000) == 0
    assert candidate(calories = [1, 2, 3, 4, 5],k = 1,lower = 3,upper = 3) == 0
    assert candidate(calories = [7, 7, 7, 7, 7, 7, 7],k = 7,lower = 21,upper = 21) == 1
    assert candidate(calories = [1, 3, 2, 4, 3, 1],k = 3,lower = 2,upper = 4) == 4
    assert candidate(calories = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5,lower = 20,upper = 30) == 0
    assert candidate(calories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3,lower = 15,upper = 20) == 0
    assert candidate(calories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3,lower = 10,upper = 20) == 1
    assert candidate(calories = [3, 2],k = 2,lower = 0,upper = 1) == 1
    assert candidate(calories = [10000, 20000, 15000, 5000, 25000],k = 3,lower = 30000,upper = 40000) == 2
    assert candidate(calories = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 5,lower = 15000,upper = 30000) == 2
    assert candidate(calories = [2000, 1500, 1000, 500, 0, 500, 1000, 1500, 2000, 2500],k = 3,lower = 3000,upper = 4500) == -2
    assert candidate(calories = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 0, 1000, 2000, 3000, 4000, 5000],k = 5,lower = 15000,upper = 25000) == -2
    assert candidate(calories = [2000, 1500, 1000, 500, 0, 500, 1000, 1500, 2000, 2500],k = 3,lower = 2500,upper = 4500) == -2
    assert candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 10,lower = 15000,upper = 25000) == 0
    assert candidate(calories = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 10,lower = 4500,upper = 6000) == 0
    assert candidate(calories = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 10,lower = 8000,upper = 12000) == 0
    assert candidate(calories = [0, 20000, 0, 20000, 0, 20000, 0, 20000, 0, 20000],k = 2,lower = 10000,upper = 30000) == 0
    assert candidate(calories = [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500],k = 10,lower = 12000,upper = 18000) == 0
    assert candidate(calories = [2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000],k = 2,lower = 4000,upper = 10000) == 6
    assert candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 5,lower = 10000,upper = 15000) == 0
    assert candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 5,lower = 8000,upper = 12000) == 0
    assert candidate(calories = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 2,lower = 400,upper = 600) == 6
    assert candidate(calories = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],k = 10,lower = 40000,upper = 60000) == 0
    assert candidate(calories = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],k = 3,lower = 3000,upper = 4500) == 6
    assert candidate(calories = [500, 1500, 1000, 1500, 500, 1500, 1000, 1500, 500, 1500, 1000, 1500],k = 6,lower = 6000,upper = 9000) == 0
    assert candidate(calories = [300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300],k = 2,lower = 500,upper = 1000) == 0
    assert candidate(calories = [10000, 5000, 15000, 10000, 20000, 15000, 25000, 20000, 30000, 25000, 35000, 30000, 40000, 35000, 45000, 40000, 50000, 45000, 55000, 50000],k = 5,lower = 50000,upper = 100000) == 12
    assert candidate(calories = [2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500],k = 10,lower = 50000,upper = 60000) == 5
    assert candidate(calories = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 5,lower = 4000,upper = 6000) == 0
    assert candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 3,lower = 5000,upper = 6000) == 0
    assert candidate(calories = [4000, 3000, 2000, 1000, 500, 0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000],k = 5,lower = 10000,upper = 15000) == -6
    assert candidate(calories = [6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000],k = 5,lower = 40000,upper = 50000) == 3
    assert candidate(calories = [8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 500, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5,lower = 25000,upper = 35000) == -14
    assert candidate(calories = [20000, 20000, 20000, 20000, 20000, 20000, 20000],k = 7,lower = 140000,upper = 140000) == 0
    assert candidate(calories = [10000, 5000, 15000, 10000, 5000, 15000, 10000, 5000, 15000, 10000],k = 3,lower = 20000,upper = 30000) == 0
    assert candidate(calories = [500, 1500, 1000, 2000, 2500, 1200, 1800, 3000, 1600, 1400, 800, 1000, 600, 1200, 1500, 1300],k = 7,lower = 7000,upper = 10000) == 7
    assert candidate(calories = [800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700],k = 5,lower = 5000,upper = 7000) == 1
    assert candidate(calories = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 1,lower = 5000,upper = 15000) == 0
    assert candidate(calories = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],k = 10,lower = 5500,upper = 10500) == 5
    assert candidate(calories = [300, 400, 350, 500, 600, 550, 700, 650, 800, 750, 900, 850, 1000, 950, 1100, 1050, 1200],k = 7,lower = 3500,upper = 5500) == 4
    assert candidate(calories = [6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000],k = 5,lower = 50000,upper = 60000) == -1
    assert candidate(calories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3,lower = 10,upper = 20) == 1
    assert candidate(calories = [2000, 1500, 1700, 1600, 1800, 1900, 2100, 2200, 2300, 2400],k = 6,lower = 9000,upper = 12000) == 1
    assert candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 20,lower = 38000,upper = 42000) == 0
    assert candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 15,lower = 25000,upper = 35000) == 0
    assert candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 4,lower = 8000,upper = 12000) == 0
    assert candidate(calories = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 3,lower = 15000,upper = 25000) == -2
    assert candidate(calories = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000, 100000],k = 10,lower = 450000,upper = 550000) == 1
    assert candidate(calories = [12000, 11000, 13000, 10000, 14000, 9000, 15000, 8000, 16000, 7000],k = 4,lower = 40000,upper = 50000) == 0
    assert candidate(calories = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 5,lower = 15000,upper = 25000) == 3
    assert candidate(calories = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 7,lower = 25000,upper = 35000) == -3
    assert candidate(calories = [4000, 3500, 3700, 3600, 3800, 3900, 4100, 4200, 4300, 4400],k = 8,lower = 25000,upper = 30000) == 3
    assert candidate(calories = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10,lower = 5,upper = 10) == 0
    assert candidate(calories = [1000, 1000, 1000, 2000, 2000, 2000, 3000, 3000, 3000, 1000, 1000, 1000],k = 3,lower = 2500,upper = 3500) == 8
    assert candidate(calories = [800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100],k = 5,lower = 4000,upper = 6000) == 7
    assert candidate(calories = [2000, 1500, 2500, 3000, 2000, 1000, 3500, 4000, 2500, 1500, 3000, 2000, 1000, 2500, 3000, 2000, 1000, 3500, 4000, 2500],k = 5,lower = 8000,upper = 15000) == 0
    assert candidate(calories = [1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200],k = 6,lower = 7000,upper = 7200) == 0
    assert candidate(calories = [2000, 2500, 3000, 1500, 3500, 4000, 2000, 1800, 2200, 2700],k = 4,lower = 8000,upper = 12000) == 0
    assert candidate(calories = [4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400],k = 6,lower = 25000,upper = 30000) == 2
    assert candidate(calories = [3000, 2500, 2000, 1500, 1000, 500, 0, 500, 1000, 1500],k = 2,lower = 1000,upper = 2000) == 3
    assert candidate(calories = [3000, 2500, 2700, 2600, 2800, 2900, 3100, 3200, 3300, 3400],k = 7,lower = 18000,upper = 22000) == 0
    assert candidate(calories = [500, 1500, 1000, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000],k = 3,lower = 4000,upper = 6000) == 6
    assert candidate(calories = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400],k = 9,lower = 5000,upper = 10000) == 0
    assert candidate(calories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5,lower = 40,upper = 60) == 1
    assert candidate(calories = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000],k = 6,lower = 20000,upper = 30000) == 4
    assert candidate(calories = [1500, 1200, 2000, 1800, 1900, 1700, 2100, 1600, 1400, 1300],k = 4,lower = 5000,upper = 7000) == 3
    assert candidate(calories = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],k = 10,lower = 50000,upper = 60000) == 0
    assert candidate(calories = [1000, 1500, 2000, 2500, 3000, 1000, 1500, 2000, 2500, 3000],k = 3,lower = 4000,upper = 7000) == 2
    assert candidate(calories = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000],k = 7,lower = 35000,upper = 45000) == 5
    assert candidate(calories = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 5,lower = 2000,upper = 5000) == 0
    assert candidate(calories = [1200, 1300, 1100, 1400, 1500, 1600, 1300, 1200, 1100, 1000],k = 4,lower = 5000,upper = 6000) == -1
    assert candidate(calories = [1200, 1100, 1300, 900, 1400, 1200, 1000, 1100, 1300, 900, 1400, 1200, 1000],k = 4,lower = 4000,upper = 5000) == 0
    assert candidate(calories = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],k = 50,lower = 100000,upper = 100000) == 0
    assert candidate(calories = [5000, 10000, 15000, 20000, 25000, 30000, 35000],k = 4,lower = 60000,upper = 80000) == 1
    assert candidate(calories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 3,lower = 5,upper = 15) == 14
    assert candidate(calories = [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100],k = 2,lower = 2500,upper = 3000) == 6
    assert candidate(calories = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 3,lower = 25000,upper = 35000) == 0
    assert candidate(calories = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 4,lower = 15000,upper = 25000) == 1
    assert candidate(calories = [3000, 2500, 2000, 1500, 1000, 500, 0, 500, 1000, 1500, 2000, 2500],k = 6,lower = 10000,upper = 15000) == -6
    assert candidate(calories = [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150],k = 6,lower = 2000,upper = 3000) == 10
    assert candidate(calories = [2000, 1800, 2200, 1900, 2100, 1700, 1600, 1500, 2300, 2400, 2500, 2600],k = 5,lower = 10000,upper = 11000) == -4
    assert candidate(calories = [5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000],k = 5,lower = 35000,upper = 45000) == 3
    assert candidate(calories = [2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500],k = 10,lower = 20000,upper = 30000) == 0
    assert candidate(calories = [12000, 11000, 13000, 14000, 9000, 8000, 15000, 16000, 7000, 6000],k = 4,lower = 40000,upper = 50000) == 0
    assert candidate(calories = [300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700, 3000, 3300, 3600, 3900, 4200, 4500, 4800, 5100, 5400, 5700, 6000],k = 3,lower = 1500,upper = 2500) == 17
    assert candidate(calories = [20000, 15000, 10000, 5000, 25000, 20000, 15000, 10000, 5000, 25000],k = 4,lower = 20000,upper = 40000) == 7
    assert candidate(calories = [2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500],k = 7,lower = 35000,upper = 45000) == 2
    assert candidate(calories = [1000, 2000, 1500, 500, 2500, 3000, 3500, 4000, 4500, 5000],k = 4,lower = 8000,upper = 12000) == 0


