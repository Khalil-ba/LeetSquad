def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(heroes = [100],monsters = [1, 10, 100],coins = [10, 20, 30]) == [60]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100],monsters = [1, 10, 100],coins = [10, 20, 30]) == [60]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [5],monsters = [2, 3, 1, 2],coins = [10, 6, 5, 2]) == [23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [5],monsters = [2, 3, 1, 2],coins = [10, 6, 5, 2]) == [23]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [10, 10, 10],monsters = [1, 2, 3, 4, 5],coins = [1, 2, 3, 4, 5]) == [15, 15, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [10, 10, 10],monsters = [1, 2, 3, 4, 5],coins = [1, 2, 3, 4, 5]) == [15, 15, 15]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 1, 1, 1],monsters = [1, 1, 1, 1],coins = [1, 1, 1, 1]) == [4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 1, 1, 1],monsters = [1, 1, 1, 1],coins = [1, 1, 1, 1]) == [4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [10, 20, 30],monsters = [5, 15, 25, 35],coins = [3, 6, 9, 12]) == [3, 9, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [10, 20, 30],monsters = [5, 15, 25, 35],coins = [3, 6, 9, 12]) == [3, 9, 18]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1],monsters = [10],coins = [100]) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1],monsters = [10],coins = [100]) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100],monsters = [10, 20, 30, 40, 50],coins = [1, 2, 3, 4, 5]) == [15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100],monsters = [10, 20, 30, 40, 50],coins = [1, 2, 3, 4, 5]) == [15]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [10, 20, 30],monsters = [5, 15, 25, 35],coins = [100, 200, 300, 400]) == [100, 300, 600]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [10, 20, 30],monsters = [5, 15, 25, 35],coins = [100, 200, 300, 400]) == [100, 300, 600]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 2, 3, 4, 5],monsters = [5],coins = [100]) == [0, 0, 0, 0, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 2, 3, 4, 5],monsters = [5],coins = [100]) == [0, 0, 0, 0, 100]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1],monsters = [10, 20, 30],coins = [1, 2, 3]) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1],monsters = [10, 20, 30],coins = [1, 2, 3]) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [4, 4],monsters = [5, 7, 8],coins = [1, 1, 1]) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [4, 4],monsters = [5, 7, 8],coins = [1, 1, 1]) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 1, 1],monsters = [1, 1, 1],coins = [1, 1, 1]) == [3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 1, 1],monsters = [1, 1, 1],coins = [1, 1, 1]) == [3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1000000000],monsters = [1000000000],coins = [1000000000]) == [1000000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1000000000],monsters = [1000000000],coins = [1000000000]) == [1000000000]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 4, 2],monsters = [1, 1, 5, 2, 3],coins = [2, 3, 4, 5, 6]) == [5, 16, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 4, 2],monsters = [1, 1, 5, 2, 3],coins = [2, 3, 4, 5, 6]) == [5, 16, 10]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100],monsters = [1, 10, 100],coins = [100, 100, 100]) == [300]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100],monsters = [1, 10, 100],coins = [100, 100, 100]) == [300]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [10, 20, 30],monsters = [5, 15, 25, 35],coins = [3, 6, 9, 12]) == [3, 9, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [10, 20, 30],monsters = [5, 15, 25, 35],coins = [3, 6, 9, 12]) == [3, 9, 18]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1000000000, 1000000000, 1000000000],monsters = [1, 2, 3, 4, 5],coins = [1, 1, 1, 1, 1]) == [5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1000000000, 1000000000, 1000000000],monsters = [1, 2, 3, 4, 5],coins = [1, 1, 1, 1, 1]) == [5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100, 200, 300, 400, 500],monsters = [1, 10, 100, 1000, 10000],coins = [1, 10, 100, 1000, 10000]) == [111, 111, 111, 111, 111]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100, 200, 300, 400, 500],monsters = [1, 10, 100, 1000, 10000],coins = [1, 10, 100, 1000, 10000]) == [111, 111, 111, 111, 111]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [3, 6, 9, 12],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [60, 210, 450, 550]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [3, 6, 9, 12],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [60, 210, 450, 550]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 2, 3, 4, 5],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 30, 60, 100, 150]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 2, 3, 4, 5],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 30, 60, 100, 150]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100, 100, 100, 100, 100],monsters = [99, 199, 299, 399, 499],coins = [1, 2, 3, 4, 5]) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100, 100, 100, 100, 100],monsters = [99, 199, 299, 399, 499],coins = [1, 2, 3, 4, 5]) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [500, 1000, 1500, 2000],monsters = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == [150, 550, 1200, 1200]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [500, 1000, 1500, 2000],monsters = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == [150, 550, 1200, 1200]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [10, 20, 30, 40, 50],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [550, 550, 550, 550, 550]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [10, 20, 30, 40, 50],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [550, 550, 550, 550, 550]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],monsters = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],coins = [50, 40, 30, 20, 10, 5, 4, 3, 2, 1]) == [90, 140, 155, 162, 165, 165, 165, 165, 165, 165]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],monsters = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],coins = [50, 40, 30, 20, 10, 5, 4, 3, 2, 1]) == [90, 140, 155, 162, 165, 165, 165, 165, 165, 165]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 1, 1, 1, 1],monsters = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],coins = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == [5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 1, 1, 1, 1],monsters = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],coins = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == [5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 1, 1, 1, 1],monsters = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 1, 1, 1, 1],monsters = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1000000000, 500000000, 1500000000],monsters = [1000000000, 500000000, 2000000000, 3000000000],coins = [100, 200, 300, 400]) == [300, 200, 300]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1000000000, 500000000, 1500000000],monsters = [1000000000, 500000000, 2000000000, 3000000000],coins = [100, 200, 300, 400]) == [300, 200, 300]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [50, 100, 150, 200, 250],monsters = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [5, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [50, 100, 150, 200, 250],monsters = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [5, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1000000000, 500000000, 750000000],monsters = [1000000000, 500000000, 750000000, 250000000],coins = [100, 200, 300, 400]) == [1000, 600, 900]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1000000000, 500000000, 750000000],monsters = [1000000000, 500000000, 750000000, 250000000],coins = [100, 200, 300, 400]) == [1000, 600, 900]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [10, 20, 30, 40, 50],monsters = [5, 15, 25, 35, 45, 55],coins = [100, 200, 300, 400, 500, 600]) == [100, 300, 600, 1000, 1500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [10, 20, 30, 40, 50],monsters = [5, 15, 25, 35, 45, 55],coins = [100, 200, 300, 400, 500, 600]) == [100, 300, 600, 1000, 1500]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100, 100, 100, 100, 100],monsters = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [550, 550, 550, 550, 550]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100, 100, 100, 100, 100],monsters = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [550, 550, 550, 550, 550]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100, 200, 300],monsters = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [55, 55, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100, 200, 300],monsters = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [55, 55, 55]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [5500, 5500, 5500, 5500, 5500, 5500, 5500, 5500, 5500, 5500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [5500, 5500, 5500, 5500, 5500, 5500, 5500, 5500, 5500, 5500]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 10, 100, 1000, 10000],monsters = [1, 10, 100, 1000, 10000, 100000],coins = [1, 10, 100, 1000, 10000, 100000]) == [1, 11, 111, 1111, 11111]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 10, 100, 1000, 10000],monsters = [1, 10, 100, 1000, 10000, 100000],coins = [1, 10, 100, 1000, 10000, 100000]) == [1, 11, 111, 1111, 11111]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [10, 20, 30, 40, 50],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],coins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == [275, 600, 600, 600, 600]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [10, 20, 30, 40, 50],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],coins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == [275, 600, 600, 600, 600]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [10, 20, 30, 40, 50],monsters = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [30, 100, 210, 360, 550]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [10, 20, 30, 40, 50],monsters = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [30, 100, 210, 360, 550]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [5, 5, 5, 5, 5],monsters = [1, 2, 3, 4, 5],coins = [1, 2, 3, 4, 5]) == [15, 15, 15, 15, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [5, 5, 5, 5, 5],monsters = [1, 2, 3, 4, 5],coins = [1, 2, 3, 4, 5]) == [15, 15, 15, 15, 15]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [5, 10, 15, 20, 25],monsters = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],coins = [50, 40, 30, 20, 10, 5, 15, 25, 35, 45]) == [50, 90, 120, 140, 150]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [5, 10, 15, 20, 25],monsters = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],coins = [50, 40, 30, 20, 10, 5, 15, 25, 35, 45]) == [50, 90, 120, 140, 150]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [5, 15, 25, 35, 45, 55],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 120, 120, 120, 120, 120]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [5, 15, 25, 35, 45, 55],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 120, 120, 120, 120, 120]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [50, 50, 50, 50, 50],monsters = [1, 2, 3, 4, 5, 49, 48, 47, 46, 45],coins = [1000, 2000, 3000, 4000, 5000, 100, 200, 300, 400, 500]) == [16500, 16500, 16500, 16500, 16500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [50, 50, 50, 50, 50],monsters = [1, 2, 3, 4, 5, 49, 48, 47, 46, 45],coins = [1000, 2000, 3000, 4000, 5000, 100, 200, 300, 400, 500]) == [16500, 16500, 16500, 16500, 16500]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1000, 2000, 3000, 4000, 5000],monsters = [1000, 2000, 3000, 4000, 5000],coins = [100, 200, 300, 400, 500]) == [100, 300, 600, 1000, 1500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1000, 2000, 3000, 4000, 5000],monsters = [1000, 2000, 3000, 4000, 5000],coins = [100, 200, 300, 400, 500]) == [100, 300, 600, 1000, 1500]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],monsters = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],coins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [100, 300, 600, 1000, 1500, 2100, 2800, 3600, 4500, 5500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],monsters = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],coins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [100, 300, 600, 1000, 1500, 2100, 2800, 3600, 4500, 5500]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [5, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [5, 10, 10, 10, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [9, 8, 7, 6, 5, 4, 3, 2, 1],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [4500, 3600, 2800, 2100, 1500, 1000, 600, 300, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [9, 8, 7, 6, 5, 4, 3, 2, 1],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [4500, 3600, 2800, 2100, 1500, 1000, 600, 300, 100]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1000, 2000, 3000],monsters = [1, 10, 100, 1000, 10000, 100000],coins = [1, 10, 100, 1000, 10000, 100000]) == [1111, 1111, 1111]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1000, 2000, 3000],monsters = [1, 10, 100, 1000, 10000, 100000],coins = [1, 10, 100, 1000, 10000, 100000]) == [1111, 1111, 1111]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],monsters = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [3, 10, 21, 36, 55, 55, 55, 55, 55, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],monsters = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [3, 10, 21, 36, 55, 55, 55, 55, 55, 55]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 0, 0, 55, 55, 55, 55, 55, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 0, 0, 55, 55, 55, 55, 55, 55]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],monsters = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == [10, 30, 60, 100, 150, 210, 280, 360, 450, 550]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],monsters = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == [10, 30, 60, 100, 150, 210, 280, 360, 450, 550]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100, 200, 300, 400, 500],monsters = [150, 250, 350, 450, 550],coins = [10, 20, 30, 40, 50]) == [0, 10, 30, 60, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100, 200, 300, 400, 500],monsters = [150, 250, 350, 450, 550],coins = [10, 20, 30, 40, 50]) == [0, 10, 30, 60, 100]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 1, 1, 1, 1],monsters = [1, 1, 1, 1, 1],coins = [1, 2, 3, 4, 5]) == [15, 15, 15, 15, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 1, 1, 1, 1],monsters = [1, 1, 1, 1, 1],coins = [1, 2, 3, 4, 5]) == [15, 15, 15, 15, 15]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [500, 500, 500],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [5500, 5500, 5500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [500, 500, 500],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [5500, 5500, 5500]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [500, 1000, 1500],monsters = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],coins = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == [40000, 55000, 55000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [500, 1000, 1500],monsters = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],coins = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == [40000, 55000, 55000]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [5],coins = [100]) == [0, 0, 0, 0, 100, 100, 100, 100, 100, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [5],coins = [100]) == [0, 0, 0, 0, 100, 100, 100, 100, 100, 100]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1000000000],monsters = [500000000, 600000000, 700000000, 800000000, 900000000],coins = [1, 2, 3, 4, 5]) == [15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1000000000],monsters = [500000000, 600000000, 700000000, 800000000, 900000000],coins = [1, 2, 3, 4, 5]) == [15]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == [10000000000, 10000000000, 10000000000, 10000000000, 10000000000, 10000000000, 10000000000, 10000000000, 10000000000, 10000000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == [10000000000, 10000000000, 10000000000, 10000000000, 10000000000, 10000000000, 10000000000, 10000000000, 10000000000, 10000000000]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1000000000],monsters = [1, 1000000000],coins = [1000000000, 1000000000]) == [2000000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1000000000],monsters = [1, 1000000000],coins = [1000000000, 1000000000]) == [2000000000]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 10, 30, 30, 60, 60, 100, 100, 150, 150]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 10, 30, 30, 60, 60, 100, 100, 150, 150]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100, 200, 300, 400, 500],monsters = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 30, 60, 100, 150]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100, 200, 300, 400, 500],monsters = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 30, 60, 100, 150]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [10, 10, 10, 10, 10],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [55, 55, 55, 55, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [10, 10, 10, 10, 10],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [55, 55, 55, 55, 55]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [50, 100, 150, 200, 250],monsters = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [15, 55, 55, 55, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [50, 100, 150, 200, 250],monsters = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [15, 55, 55, 55, 55]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 1, 1, 1, 1],monsters = [1, 1, 1, 1, 1],coins = [10, 20, 30, 40, 50]) == [150, 150, 150, 150, 150]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 1, 1, 1, 1],monsters = [1, 1, 1, 1, 1],coins = [10, 20, 30, 40, 50]) == [150, 150, 150, 150, 150]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 1, 1, 1, 1],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [100, 100, 100, 100, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 1, 1, 1, 1],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [100, 100, 100, 100, 100]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [5, 10, 15, 20, 25],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [5, 10, 15, 20, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [5, 10, 15, 20, 25],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [5, 10, 15, 20, 20]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100, 200, 300, 400, 500],monsters = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [30, 100, 210, 360, 550]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100, 200, 300, 400, 500],monsters = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [30, 100, 210, 360, 550]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 10, 100, 1000, 10000],monsters = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 55, 55, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 10, 100, 1000, 10000],monsters = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 55, 55, 55]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 2, 3, 4, 5],monsters = [5, 4, 3, 2, 1],coins = [10, 20, 30, 40, 50]) == [50, 90, 120, 140, 150]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 2, 3, 4, 5],monsters = [5, 4, 3, 2, 1],coins = [10, 20, 30, 40, 50]) == [50, 90, 120, 140, 150]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [5, 15, 25],monsters = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [5, 15, 25],monsters = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100, 200, 300, 400, 500],monsters = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [100, 360, 550, 550, 550]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100, 200, 300, 400, 500],monsters = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [100, 360, 550, 550, 550]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100, 200, 300, 400, 500],monsters = [99, 199, 299, 399, 499],coins = [1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100, 200, 300, 400, 500],monsters = [99, 199, 299, 399, 499],coins = [1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 2, 3, 4, 5],monsters = [1, 1, 1, 1, 1],coins = [10, 20, 30, 40, 50]) == [150, 150, 150, 150, 150]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 2, 3, 4, 5],monsters = [1, 1, 1, 1, 1],coins = [10, 20, 30, 40, 50]) == [150, 150, 150, 150, 150]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [10, 20, 30, 40, 50],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [155, 210, 210, 210, 210]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [10, 20, 30, 40, 50],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [155, 210, 210, 210, 210]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],monsters = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [30, 100, 210, 360, 550, 550, 550, 550, 550, 550]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],monsters = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [30, 100, 210, 360, 550, 550, 550, 550, 550, 550]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 10, 100, 1000],monsters = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 55, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 10, 100, 1000],monsters = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 55, 55]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],monsters = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],monsters = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],coins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [0, 0, 0, 0, 100, 100, 100, 100, 100, 300]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],coins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [0, 0, 0, 0, 100, 100, 100, 100, 100, 300]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 1000000000],monsters = [500000000, 600000000, 700000000, 800000000, 900000000],coins = [1, 2, 3, 4, 5]) == [0, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 1000000000],monsters = [500000000, 600000000, 700000000, 800000000, 900000000],coins = [1, 2, 3, 4, 5]) == [0, 15]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [50, 100, 150, 200, 250, 300],monsters = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [55, 210, 210, 210, 210, 210]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [50, 100, 150, 200, 250, 300],monsters = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [55, 210, 210, 210, 210, 210]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [5, 15, 25, 35, 45],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [15, 120, 210, 210, 210]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [5, 15, 25, 35, 45],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [15, 120, 210, 210, 210]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [500000000, 1000000000, 250000000, 750000000],monsters = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000, 1000000000],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [150, 550, 30, 280]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [500000000, 1000000000, 250000000, 750000000],monsters = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000, 1000000000],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [150, 550, 30, 280]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [9, 8, 7, 6, 5, 4, 3, 2, 1],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9],coins = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [45, 44, 42, 39, 35, 30, 24, 17, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [9, 8, 7, 6, 5, 4, 3, 2, 1],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9],coins = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [45, 44, 42, 39, 35, 30, 24, 17, 9]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [3, 1, 2],monsters = [3, 1, 2, 4, 5],coins = [10, 20, 30, 40, 50]) == [60, 20, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [3, 1, 2],monsters = [3, 1, 2, 4, 5],coins = [10, 20, 30, 40, 50]) == [60, 20, 50]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [5],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [5],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [15]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [5, 5, 5, 5, 5],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [5, 5, 5, 5, 5],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [50, 100, 150],monsters = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [15, 55, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [50, 100, 150],monsters = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [15, 55, 55]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 2, 3, 4, 5],monsters = [5, 4, 3, 2, 1],coins = [1, 2, 3, 4, 5]) == [5, 9, 12, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 2, 3, 4, 5],monsters = [5, 4, 3, 2, 1],coins = [1, 2, 3, 4, 5]) == [5, 9, 12, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [5, 15, 25, 35],monsters = [10, 20, 30, 40, 50],coins = [1, 2, 3, 4, 5]) == [0, 1, 3, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [5, 15, 25, 35],monsters = [10, 20, 30, 40, 50],coins = [1, 2, 3, 4, 5]) == [0, 1, 3, 6]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1000000000, 500000000, 250000000],monsters = [1000000000, 750000000, 500000000, 250000000, 100000000],coins = [100, 200, 300, 400, 500]) == [1500, 1200, 900]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1000000000, 500000000, 250000000],monsters = [1000000000, 750000000, 500000000, 250000000, 100000000],coins = [100, 200, 300, 400, 500]) == [1500, 1200, 900]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],monsters = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 0, 0, 1, 3, 6, 10, 15, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],monsters = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 0, 0, 1, 3, 6, 10, 15, 21]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100, 200, 300],monsters = [50, 100, 150, 200, 250, 300, 350],coins = [10, 20, 30, 40, 50, 60, 70]) == [30, 100, 210]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100, 200, 300],monsters = [50, 100, 150, 200, 250, 300, 350],coins = [10, 20, 30, 40, 50, 60, 70]) == [30, 100, 210]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100, 150, 200, 250, 300],monsters = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 21, 36, 55, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100, 150, 200, 250, 300],monsters = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 21, 36, 55, 55]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [10, 20, 30, 40, 50],monsters = [15, 25, 35, 45, 55],coins = [5, 10, 15, 20, 25]) == [0, 5, 15, 30, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [10, 20, 30, 40, 50],monsters = [15, 25, 35, 45, 55],coins = [5, 10, 15, 20, 25]) == [0, 5, 15, 30, 50]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [5, 15, 25, 35],monsters = [1, 5, 10, 15, 20, 25, 30, 35],coins = [1, 2, 3, 4, 5, 6, 7, 8]) == [3, 10, 21, 36]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [5, 15, 25, 35],monsters = [1, 5, 10, 15, 20, 25, 30, 35],coins = [1, 2, 3, 4, 5, 6, 7, 8]) == [3, 10, 21, 36]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [10, 20, 30, 40, 50],monsters = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],coins = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [30, 110, 110, 110, 110]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [10, 20, 30, 40, 50],monsters = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],coins = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [30, 110, 110, 110, 110]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100, 100, 100, 100, 100],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [55, 55, 55, 55, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100, 100, 100, 100, 100],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [55, 55, 55, 55, 55]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100, 200, 300],monsters = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100, 200, 300],monsters = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100, 200, 300, 400, 500],monsters = [50, 150, 250, 350, 450, 550],coins = [10, 20, 30, 40, 50, 60]) == [10, 30, 60, 100, 150]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100, 200, 300, 400, 500],monsters = [50, 150, 250, 350, 450, 550],coins = [10, 20, 30, 40, 50, 60]) == [10, 30, 60, 100, 150]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 2, 3, 4, 5],monsters = [5, 5, 5, 5, 5],coins = [10, 10, 10, 10, 10]) == [0, 0, 0, 0, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 2, 3, 4, 5],monsters = [5, 5, 5, 5, 5],coins = [10, 10, 10, 10, 10]) == [0, 0, 0, 0, 50]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100000, 200000, 300000, 400000],monsters = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],coins = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == [55000, 55000, 55000, 55000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100000, 200000, 300000, 400000],monsters = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],coins = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == [55000, 55000, 55000, 55000]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 30, 60, 100, 150, 210, 280, 360, 450, 550]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 30, 60, 100, 150, 210, 280, 360, 450, 550]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [10, 20, 30, 40, 50],monsters = [50, 40, 30, 20, 10],coins = [100, 200, 300, 400, 500]) == [500, 900, 1200, 1400, 1500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [10, 20, 30, 40, 50],monsters = [50, 40, 30, 20, 10],coins = [100, 200, 300, 400, 500]) == [500, 900, 1200, 1400, 1500]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [1, 1, 1, 1, 1],monsters = [1, 1, 1, 1, 1],coins = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == [5000000000, 5000000000, 5000000000, 5000000000, 5000000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [1, 1, 1, 1, 1],monsters = [1, 1, 1, 1, 1],coins = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == [5000000000, 5000000000, 5000000000, 5000000000, 5000000000]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [10, 10, 10, 10, 10],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [10, 10, 10, 10, 10],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100, 200, 300, 400, 500],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [210, 210, 210, 210, 210]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100, 200, 300, 400, 500],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [210, 210, 210, 210, 210]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [50, 100, 150, 200],monsters = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190],coins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [30, 75, 180, 275]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [50, 100, 150, 200],monsters = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190],coins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [30, 75, 180, 275]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [150, 150, 150, 150, 150, 150, 150, 150, 150, 150]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [150, 150, 150, 150, 150, 150, 150, 150, 150, 150]: {e}')
    
    total += 1
    try:
        result = candidate(heroes = [100, 200, 300, 400],monsters = [50, 150, 250, 350, 450],coins = [5, 10, 15, 20, 25]) == [5, 15, 30, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heroes = [100, 200, 300, 400],monsters = [50, 150, 250, 350, 450],coins = [5, 10, 15, 20, 25]) == [5, 15, 30, 50]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(heroes = [100],monsters = [1, 10, 100],coins = [10, 20, 30]) == [60]
    assert candidate(heroes = [5],monsters = [2, 3, 1, 2],coins = [10, 6, 5, 2]) == [23]
    assert candidate(heroes = [10, 10, 10],monsters = [1, 2, 3, 4, 5],coins = [1, 2, 3, 4, 5]) == [15, 15, 15]
    assert candidate(heroes = [1, 1, 1, 1],monsters = [1, 1, 1, 1],coins = [1, 1, 1, 1]) == [4, 4, 4, 4]
    assert candidate(heroes = [10, 20, 30],monsters = [5, 15, 25, 35],coins = [3, 6, 9, 12]) == [3, 9, 18]
    assert candidate(heroes = [1],monsters = [10],coins = [100]) == [0]
    assert candidate(heroes = [100],monsters = [10, 20, 30, 40, 50],coins = [1, 2, 3, 4, 5]) == [15]
    assert candidate(heroes = [10, 20, 30],monsters = [5, 15, 25, 35],coins = [100, 200, 300, 400]) == [100, 300, 600]
    assert candidate(heroes = [1, 2, 3, 4, 5],monsters = [5],coins = [100]) == [0, 0, 0, 0, 100]
    assert candidate(heroes = [1],monsters = [10, 20, 30],coins = [1, 2, 3]) == [0]
    assert candidate(heroes = [4, 4],monsters = [5, 7, 8],coins = [1, 1, 1]) == [0, 0]
    assert candidate(heroes = [1, 1, 1],monsters = [1, 1, 1],coins = [1, 1, 1]) == [3, 3, 3]
    assert candidate(heroes = [1000000000],monsters = [1000000000],coins = [1000000000]) == [1000000000]
    assert candidate(heroes = [1, 4, 2],monsters = [1, 1, 5, 2, 3],coins = [2, 3, 4, 5, 6]) == [5, 16, 10]
    assert candidate(heroes = [100],monsters = [1, 10, 100],coins = [100, 100, 100]) == [300]
    assert candidate(heroes = [10, 20, 30],monsters = [5, 15, 25, 35],coins = [3, 6, 9, 12]) == [3, 9, 18]
    assert candidate(heroes = [1000000000, 1000000000, 1000000000],monsters = [1, 2, 3, 4, 5],coins = [1, 1, 1, 1, 1]) == [5, 5, 5]
    assert candidate(heroes = [100, 200, 300, 400, 500],monsters = [1, 10, 100, 1000, 10000],coins = [1, 10, 100, 1000, 10000]) == [111, 111, 111, 111, 111]
    assert candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    assert candidate(heroes = [3, 6, 9, 12],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [60, 210, 450, 550]
    assert candidate(heroes = [1, 2, 3, 4, 5],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 30, 60, 100, 150]
    assert candidate(heroes = [100, 100, 100, 100, 100],monsters = [99, 199, 299, 399, 499],coins = [1, 2, 3, 4, 5]) == [1, 1, 1, 1, 1]
    assert candidate(heroes = [500, 1000, 1500, 2000],monsters = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == [150, 550, 1200, 1200]
    assert candidate(heroes = [10, 20, 30, 40, 50],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [550, 550, 550, 550, 550]
    assert candidate(heroes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],monsters = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],coins = [50, 40, 30, 20, 10, 5, 4, 3, 2, 1]) == [90, 140, 155, 162, 165, 165, 165, 165, 165, 165]
    assert candidate(heroes = [1, 1, 1, 1, 1],monsters = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],coins = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == [5, 5, 5, 5, 5]
    assert candidate(heroes = [1, 1, 1, 1, 1],monsters = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [10, 10, 10, 10, 10]
    assert candidate(heroes = [1000000000, 500000000, 1500000000],monsters = [1000000000, 500000000, 2000000000, 3000000000],coins = [100, 200, 300, 400]) == [300, 200, 300]
    assert candidate(heroes = [50, 100, 150, 200, 250],monsters = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [5, 10, 10, 10, 10]
    assert candidate(heroes = [1000000000, 500000000, 750000000],monsters = [1000000000, 500000000, 750000000, 250000000],coins = [100, 200, 300, 400]) == [1000, 600, 900]
    assert candidate(heroes = [10, 20, 30, 40, 50],monsters = [5, 15, 25, 35, 45, 55],coins = [100, 200, 300, 400, 500, 600]) == [100, 300, 600, 1000, 1500]
    assert candidate(heroes = [100, 100, 100, 100, 100],monsters = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [550, 550, 550, 550, 550]
    assert candidate(heroes = [100, 200, 300],monsters = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [55, 55, 55]
    assert candidate(heroes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [5500, 5500, 5500, 5500, 5500, 5500, 5500, 5500, 5500, 5500]
    assert candidate(heroes = [1, 10, 100, 1000, 10000],monsters = [1, 10, 100, 1000, 10000, 100000],coins = [1, 10, 100, 1000, 10000, 100000]) == [1, 11, 111, 1111, 11111]
    assert candidate(heroes = [10, 20, 30, 40, 50],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],coins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == [275, 600, 600, 600, 600]
    assert candidate(heroes = [10, 20, 30, 40, 50],monsters = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [30, 100, 210, 360, 550]
    assert candidate(heroes = [5, 5, 5, 5, 5],monsters = [1, 2, 3, 4, 5],coins = [1, 2, 3, 4, 5]) == [15, 15, 15, 15, 15]
    assert candidate(heroes = [5, 10, 15, 20, 25],monsters = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],coins = [50, 40, 30, 20, 10, 5, 15, 25, 35, 45]) == [50, 90, 120, 140, 150]
    assert candidate(heroes = [5, 15, 25, 35, 45, 55],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [15, 120, 120, 120, 120, 120]
    assert candidate(heroes = [50, 50, 50, 50, 50],monsters = [1, 2, 3, 4, 5, 49, 48, 47, 46, 45],coins = [1000, 2000, 3000, 4000, 5000, 100, 200, 300, 400, 500]) == [16500, 16500, 16500, 16500, 16500]
    assert candidate(heroes = [1000, 2000, 3000, 4000, 5000],monsters = [1000, 2000, 3000, 4000, 5000],coins = [100, 200, 300, 400, 500]) == [100, 300, 600, 1000, 1500]
    assert candidate(heroes = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],monsters = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],coins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [100, 300, 600, 1000, 1500, 2100, 2800, 3600, 4500, 5500]
    assert candidate(heroes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [5, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert candidate(heroes = [9, 8, 7, 6, 5, 4, 3, 2, 1],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [4500, 3600, 2800, 2100, 1500, 1000, 600, 300, 100]
    assert candidate(heroes = [1000, 2000, 3000],monsters = [1, 10, 100, 1000, 10000, 100000],coins = [1, 10, 100, 1000, 10000, 100000]) == [1111, 1111, 1111]
    assert candidate(heroes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],monsters = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [3, 10, 21, 36, 55, 55, 55, 55, 55, 55]
    assert candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 0, 0, 55, 55, 55, 55, 55, 55]
    assert candidate(heroes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],monsters = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == [10, 30, 60, 100, 150, 210, 280, 360, 450, 550]
    assert candidate(heroes = [100, 200, 300, 400, 500],monsters = [150, 250, 350, 450, 550],coins = [10, 20, 30, 40, 50]) == [0, 10, 30, 60, 100]
    assert candidate(heroes = [1, 1, 1, 1, 1],monsters = [1, 1, 1, 1, 1],coins = [1, 2, 3, 4, 5]) == [15, 15, 15, 15, 15]
    assert candidate(heroes = [500, 500, 500],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [5500, 5500, 5500]
    assert candidate(heroes = [500, 1000, 1500],monsters = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],coins = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == [40000, 55000, 55000]
    assert candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [5],coins = [100]) == [0, 0, 0, 0, 100, 100, 100, 100, 100, 100]
    assert candidate(heroes = [1000000000],monsters = [500000000, 600000000, 700000000, 800000000, 900000000],coins = [1, 2, 3, 4, 5]) == [15]
    assert candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == [10000000000, 10000000000, 10000000000, 10000000000, 10000000000, 10000000000, 10000000000, 10000000000, 10000000000, 10000000000]
    assert candidate(heroes = [1000000000],monsters = [1, 1000000000],coins = [1000000000, 1000000000]) == [2000000000]
    assert candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 10, 30, 30, 60, 60, 100, 100, 150, 150]
    assert candidate(heroes = [100, 200, 300, 400, 500],monsters = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 30, 60, 100, 150]
    assert candidate(heroes = [10, 10, 10, 10, 10],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [55, 55, 55, 55, 55]
    assert candidate(heroes = [50, 100, 150, 200, 250],monsters = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [15, 55, 55, 55, 55]
    assert candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert candidate(heroes = [1, 1, 1, 1, 1],monsters = [1, 1, 1, 1, 1],coins = [10, 20, 30, 40, 50]) == [150, 150, 150, 150, 150]
    assert candidate(heroes = [1, 1, 1, 1, 1],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [100, 100, 100, 100, 100]
    assert candidate(heroes = [5, 10, 15, 20, 25],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [5, 10, 15, 20, 20]
    assert candidate(heroes = [100, 200, 300, 400, 500],monsters = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [30, 100, 210, 360, 550]
    assert candidate(heroes = [1, 10, 100, 1000, 10000],monsters = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 55, 55, 55]
    assert candidate(heroes = [1, 2, 3, 4, 5],monsters = [5, 4, 3, 2, 1],coins = [10, 20, 30, 40, 50]) == [50, 90, 120, 140, 150]
    assert candidate(heroes = [5, 15, 25],monsters = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 10, 10]
    assert candidate(heroes = [100, 200, 300, 400, 500],monsters = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [100, 360, 550, 550, 550]
    assert candidate(heroes = [100, 200, 300, 400, 500],monsters = [99, 199, 299, 399, 499],coins = [1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert candidate(heroes = [1, 2, 3, 4, 5],monsters = [1, 1, 1, 1, 1],coins = [10, 20, 30, 40, 50]) == [150, 150, 150, 150, 150]
    assert candidate(heroes = [10, 20, 30, 40, 50],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [155, 210, 210, 210, 210]
    assert candidate(heroes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],monsters = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [30, 100, 210, 360, 550, 550, 550, 550, 550, 550]
    assert candidate(heroes = [1, 10, 100, 1000],monsters = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 55, 55]
    assert candidate(heroes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],monsters = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
    assert candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],coins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [0, 0, 0, 0, 100, 100, 100, 100, 100, 300]
    assert candidate(heroes = [1, 1000000000],monsters = [500000000, 600000000, 700000000, 800000000, 900000000],coins = [1, 2, 3, 4, 5]) == [0, 15]
    assert candidate(heroes = [50, 100, 150, 200, 250, 300],monsters = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [55, 210, 210, 210, 210, 210]
    assert candidate(heroes = [5, 15, 25, 35, 45],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [15, 120, 210, 210, 210]
    assert candidate(heroes = [500000000, 1000000000, 250000000, 750000000],monsters = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000, 1000000000],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [150, 550, 30, 280]
    assert candidate(heroes = [9, 8, 7, 6, 5, 4, 3, 2, 1],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9],coins = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [45, 44, 42, 39, 35, 30, 24, 17, 9]
    assert candidate(heroes = [3, 1, 2],monsters = [3, 1, 2, 4, 5],coins = [10, 20, 30, 40, 50]) == [60, 20, 50]
    assert candidate(heroes = [5],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [15]
    assert candidate(heroes = [5, 5, 5, 5, 5],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [5, 5, 5, 5, 5]
    assert candidate(heroes = [50, 100, 150],monsters = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [15, 55, 55]
    assert candidate(heroes = [1, 2, 3, 4, 5],monsters = [5, 4, 3, 2, 1],coins = [1, 2, 3, 4, 5]) == [5, 9, 12, 14, 15]
    assert candidate(heroes = [5, 15, 25, 35],monsters = [10, 20, 30, 40, 50],coins = [1, 2, 3, 4, 5]) == [0, 1, 3, 6]
    assert candidate(heroes = [1000000000, 500000000, 250000000],monsters = [1000000000, 750000000, 500000000, 250000000, 100000000],coins = [100, 200, 300, 400, 500]) == [1500, 1200, 900]
    assert candidate(heroes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],monsters = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 0, 0, 1, 3, 6, 10, 15, 21]
    assert candidate(heroes = [100, 200, 300],monsters = [50, 100, 150, 200, 250, 300, 350],coins = [10, 20, 30, 40, 50, 60, 70]) == [30, 100, 210]
    assert candidate(heroes = [100, 150, 200, 250, 300],monsters = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 21, 36, 55, 55]
    assert candidate(heroes = [10, 20, 30, 40, 50],monsters = [15, 25, 35, 45, 55],coins = [5, 10, 15, 20, 25]) == [0, 5, 15, 30, 50]
    assert candidate(heroes = [5, 15, 25, 35],monsters = [1, 5, 10, 15, 20, 25, 30, 35],coins = [1, 2, 3, 4, 5, 6, 7, 8]) == [3, 10, 21, 36]
    assert candidate(heroes = [10, 20, 30, 40, 50],monsters = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],coins = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [30, 110, 110, 110, 110]
    assert candidate(heroes = [100, 100, 100, 100, 100],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [55, 55, 55, 55, 55]
    assert candidate(heroes = [100, 200, 300],monsters = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [10, 10, 10]
    assert candidate(heroes = [100, 200, 300, 400, 500],monsters = [50, 150, 250, 350, 450, 550],coins = [10, 20, 30, 40, 50, 60]) == [10, 30, 60, 100, 150]
    assert candidate(heroes = [1, 2, 3, 4, 5],monsters = [5, 5, 5, 5, 5],coins = [10, 10, 10, 10, 10]) == [0, 0, 0, 0, 50]
    assert candidate(heroes = [100000, 200000, 300000, 400000],monsters = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],coins = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == [55000, 55000, 55000, 55000]
    assert candidate(heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 30, 60, 100, 150, 210, 280, 360, 450, 550]
    assert candidate(heroes = [10, 20, 30, 40, 50],monsters = [50, 40, 30, 20, 10],coins = [100, 200, 300, 400, 500]) == [500, 900, 1200, 1400, 1500]
    assert candidate(heroes = [1, 1, 1, 1, 1],monsters = [1, 1, 1, 1, 1],coins = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == [5000000000, 5000000000, 5000000000, 5000000000, 5000000000]
    assert candidate(heroes = [10, 10, 10, 10, 10],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [10, 10, 10, 10, 10]
    assert candidate(heroes = [100, 200, 300, 400, 500],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [210, 210, 210, 210, 210]
    assert candidate(heroes = [50, 100, 150, 200],monsters = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190],coins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [30, 75, 180, 275]
    assert candidate(heroes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],monsters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [150, 150, 150, 150, 150, 150, 150, 150, 150, 150]
    assert candidate(heroes = [100, 200, 300, 400],monsters = [50, 150, 250, 350, 450],coins = [5, 10, 15, 20, 25]) == [5, 15, 30, 50]


