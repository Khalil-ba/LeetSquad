def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(count = [100000],upgrade = [100000],sell = [100000],money = [1000000000]) == [55000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100000],upgrade = [100000],sell = [100000],money = [1000000000]) == [55000]: {e}')
    
    total += 1
    try:
        result = candidate(count = [10, 20, 30],upgrade = [5, 4, 3],sell = [1, 2, 3],money = [50, 100, 150]) == [10, 20, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [10, 20, 30],upgrade = [5, 4, 3],sell = [1, 2, 3],money = [50, 100, 150]) == [10, 20, 30]: {e}')
    
    total += 1
    try:
        result = candidate(count = [10, 20, 30],upgrade = [1, 2, 3],sell = [4, 5, 6],money = [100, 100, 100]) == [10, 20, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [10, 20, 30],upgrade = [1, 2, 3],sell = [4, 5, 6],money = [100, 100, 100]) == [10, 20, 30]: {e}')
    
    total += 1
    try:
        result = candidate(count = [4, 3],upgrade = [3, 5],sell = [4, 2],money = [8, 9]) == [3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [4, 3],upgrade = [3, 5],sell = [4, 2],money = [8, 9]) == [3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(count = [5, 5, 5],upgrade = [10, 20, 30],sell = [5, 10, 15],money = [100, 100, 100]) == [5, 5, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [5, 5, 5],upgrade = [10, 20, 30],sell = [5, 10, 15],money = [100, 100, 100]) == [5, 5, 3]: {e}')
    
    total += 1
    try:
        result = candidate(count = [1],upgrade = [2],sell = [1],money = [1]) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [1],upgrade = [2],sell = [1],money = [1]) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(count = [10, 20, 30],upgrade = [5, 10, 15],sell = [1, 2, 3],money = [100, 200, 300]) == [10, 20, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [10, 20, 30],upgrade = [5, 10, 15],sell = [1, 2, 3],money = [100, 200, 300]) == [10, 20, 21]: {e}')
    
    total += 1
    try:
        result = candidate(count = [10, 20, 30],upgrade = [1, 2, 3],sell = [4, 5, 6],money = [50, 100, 150]) == [10, 20, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [10, 20, 30],upgrade = [1, 2, 3],sell = [4, 5, 6],money = [50, 100, 150]) == [10, 20, 30]: {e}')
    
    total += 1
    try:
        result = candidate(count = [5, 5, 5],upgrade = [10, 20, 30],sell = [5, 15, 25],money = [100, 150, 200]) == [5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [5, 5, 5],upgrade = [10, 20, 30],sell = [5, 15, 25],money = [100, 150, 200]) == [5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(count = [5, 5, 5],upgrade = [1, 2, 3],sell = [3, 2, 1],money = [10, 10, 10]) == [5, 5, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [5, 5, 5],upgrade = [1, 2, 3],sell = [3, 2, 1],money = [10, 10, 10]) == [5, 5, 3]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100, 100, 100],upgrade = [1000, 1000, 1000],sell = [500, 500, 500],money = [50000, 50000, 50000]) == [66, 66, 66]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100, 100, 100],upgrade = [1000, 1000, 1000],sell = [500, 500, 500],money = [50000, 50000, 50000]) == [66, 66, 66]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100],upgrade = [10],sell = [5],money = [500]) == [66]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100],upgrade = [10],sell = [5],money = [500]) == [66]: {e}')
    
    total += 1
    try:
        result = candidate(count = [10, 20, 30],upgrade = [1, 2, 3],sell = [3, 2, 1],money = [100, 200, 300]) == [10, 20, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [10, 20, 30],upgrade = [1, 2, 3],sell = [3, 2, 1],money = [100, 200, 300]) == [10, 20, 30]: {e}')
    
    total += 1
    try:
        result = candidate(count = [5, 5, 5],upgrade = [10, 10, 10],sell = [5, 5, 5],money = [50, 50, 50]) == [5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [5, 5, 5],upgrade = [10, 10, 10],sell = [5, 5, 5],money = [50, 50, 50]) == [5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(count = [5, 5, 5],upgrade = [10, 10, 10],sell = [5, 5, 5],money = [20, 20, 20]) == [3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [5, 5, 5],upgrade = [10, 10, 10],sell = [5, 5, 5],money = [20, 20, 20]) == [3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(count = [2, 4, 6],upgrade = [1, 2, 3],sell = [2, 4, 6],money = [10, 20, 30]) == [2, 4, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [2, 4, 6],upgrade = [1, 2, 3],sell = [2, 4, 6],money = [10, 20, 30]) == [2, 4, 6]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100, 200, 300, 400],upgrade = [5, 10, 15, 20],sell = [20, 15, 10, 5],money = [500, 1000, 1500, 2000]) == [100, 160, 180, 160]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100, 200, 300, 400],upgrade = [5, 10, 15, 20],sell = [20, 15, 10, 5],money = [500, 1000, 1500, 2000]) == [100, 160, 180, 160]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100, 200, 300, 400, 500],upgrade = [5, 10, 15, 20, 25],sell = [20, 15, 10, 5, 1],money = [1000, 2000, 3000, 4000, 5000]) == [100, 200, 240, 240, 211]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100, 200, 300, 400, 500],upgrade = [5, 10, 15, 20, 25],sell = [20, 15, 10, 5, 1],money = [1000, 2000, 3000, 4000, 5000]) == [100, 200, 240, 240, 211]: {e}')
    
    total += 1
    try:
        result = candidate(count = [1, 2, 3, 4, 5],upgrade = [10, 20, 30, 40, 50],sell = [50, 40, 30, 20, 10],money = [100, 200, 300, 400, 500]) == [1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [1, 2, 3, 4, 5],upgrade = [10, 20, 30, 40, 50],sell = [50, 40, 30, 20, 10],money = [100, 200, 300, 400, 500]) == [1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(count = [15, 25, 35, 45],upgrade = [2, 3, 4, 5],sell = [5, 4, 3, 2],money = [150, 250, 350, 450]) == [15, 25, 35, 45]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [15, 25, 35, 45],upgrade = [2, 3, 4, 5],sell = [5, 4, 3, 2],money = [150, 250, 350, 450]) == [15, 25, 35, 45]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100, 50, 25],upgrade = [5, 10, 15],sell = [2, 4, 6],money = [1000, 500, 250]) == [100, 50, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100, 50, 25],upgrade = [5, 10, 15],sell = [2, 4, 6],money = [1000, 500, 250]) == [100, 50, 19]: {e}')
    
    total += 1
    try:
        result = candidate(count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],upgrade = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],sell = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],money = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]) == [1, 2, 3, 4, 5, 5, 5, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],upgrade = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],sell = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],money = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]) == [1, 2, 3, 4, 5, 5, 5, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(count = [30000, 25000, 20000],upgrade = [100, 150, 200],sell = [200, 150, 100],money = [5000000, 4000000, 3000000]) == [30000, 25000, 16666]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [30000, 25000, 20000],upgrade = [100, 150, 200],sell = [200, 150, 100],money = [5000000, 4000000, 3000000]) == [30000, 25000, 16666]: {e}')
    
    total += 1
    try:
        result = candidate(count = [1, 2, 3, 4, 5],upgrade = [1, 2, 3, 4, 5],sell = [5, 4, 3, 2, 1],money = [15, 10, 5, 0, 0]) == [1, 2, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [1, 2, 3, 4, 5],upgrade = [1, 2, 3, 4, 5],sell = [5, 4, 3, 2, 1],money = [15, 10, 5, 0, 0]) == [1, 2, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(count = [333, 666, 999],upgrade = [33, 66, 99],sell = [11, 22, 33],money = [1110, 2220, 3330]) == [108, 191, 274]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [333, 666, 999],upgrade = [33, 66, 99],sell = [11, 22, 33],money = [1110, 2220, 3330]) == [108, 191, 274]: {e}')
    
    total += 1
    try:
        result = candidate(count = [50, 50, 50, 50],upgrade = [2, 3, 4, 5],sell = [3, 2, 1, 4],money = [150, 200, 250, 300]) == [50, 50, 50, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [50, 50, 50, 50],upgrade = [2, 3, 4, 5],sell = [3, 2, 1, 4],money = [150, 200, 250, 300]) == [50, 50, 50, 50]: {e}')
    
    total += 1
    try:
        result = candidate(count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],upgrade = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sell = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],money = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],upgrade = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sell = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],money = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(count = [1000, 2000, 3000],upgrade = [1, 2, 3],sell = [2, 1, 2],money = [5000, 10000, 15000]) == [1000, 2000, 3000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [1000, 2000, 3000],upgrade = [1, 2, 3],sell = [2, 1, 2],money = [5000, 10000, 15000]) == [1000, 2000, 3000]: {e}')
    
    total += 1
    try:
        result = candidate(count = [10, 10, 10, 10, 10],upgrade = [1, 2, 3, 4, 5],sell = [5, 4, 3, 2, 1],money = [50, 40, 30, 20, 10]) == [10, 10, 10, 6, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [10, 10, 10, 10, 10],upgrade = [1, 2, 3, 4, 5],sell = [5, 4, 3, 2, 1],money = [50, 40, 30, 20, 10]) == [10, 10, 10, 6, 3]: {e}')
    
    total += 1
    try:
        result = candidate(count = [20, 25, 30, 35, 40, 45, 50],upgrade = [5, 6, 7, 8, 9, 10, 11],sell = [11, 10, 9, 8, 7, 6, 5],money = [200, 250, 300, 350, 400, 450, 500]) == [20, 25, 30, 35, 40, 45, 46]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [20, 25, 30, 35, 40, 45, 50],upgrade = [5, 6, 7, 8, 9, 10, 11],sell = [11, 10, 9, 8, 7, 6, 5],money = [200, 250, 300, 350, 400, 450, 500]) == [20, 25, 30, 35, 40, 45, 46]: {e}')
    
    total += 1
    try:
        result = candidate(count = [500, 500, 500, 500],upgrade = [10, 20, 30, 40],sell = [20, 10, 40, 30],money = [2000, 1000, 4000, 3000]) == [400, 200, 342, 257]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [500, 500, 500, 500],upgrade = [10, 20, 30, 40],sell = [20, 10, 40, 30],money = [2000, 1000, 4000, 3000]) == [400, 200, 342, 257]: {e}')
    
    total += 1
    try:
        result = candidate(count = [50, 75, 100],upgrade = [2, 3, 4],sell = [1, 2, 3],money = [100, 200, 300]) == [50, 70, 85]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [50, 75, 100],upgrade = [2, 3, 4],sell = [1, 2, 3],money = [100, 200, 300]) == [50, 70, 85]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100, 100, 100, 100],upgrade = [1, 1, 1, 1],sell = [2, 2, 2, 2],money = [1000, 2000, 3000, 4000]) == [100, 100, 100, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100, 100, 100, 100],upgrade = [1, 1, 1, 1],sell = [2, 2, 2, 2],money = [1000, 2000, 3000, 4000]) == [100, 100, 100, 100]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100, 150, 200],upgrade = [10, 15, 20],sell = [5, 10, 15],money = [1000, 1500, 2000]) == [100, 120, 142]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100, 150, 200],upgrade = [10, 15, 20],sell = [5, 10, 15],money = [1000, 1500, 2000]) == [100, 120, 142]: {e}')
    
    total += 1
    try:
        result = candidate(count = [50, 50, 50],upgrade = [10, 20, 30],sell = [15, 25, 35],money = [500, 750, 1000]) == [50, 44, 42]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [50, 50, 50],upgrade = [10, 20, 30],sell = [15, 25, 35],money = [500, 750, 1000]) == [50, 44, 42]: {e}')
    
    total += 1
    try:
        result = candidate(count = [50, 50, 50, 50, 50],upgrade = [10, 20, 30, 40, 50],sell = [5, 10, 15, 20, 25],money = [500, 1000, 1500, 2000, 2500]) == [50, 50, 50, 50, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [50, 50, 50, 50, 50],upgrade = [10, 20, 30, 40, 50],sell = [5, 10, 15, 20, 25],money = [500, 1000, 1500, 2000, 2500]) == [50, 50, 50, 50, 50]: {e}')
    
    total += 1
    try:
        result = candidate(count = [15, 25, 35],upgrade = [4, 6, 8],sell = [7, 5, 3],money = [150, 250, 350]) == [15, 25, 35]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [15, 25, 35],upgrade = [4, 6, 8],sell = [7, 5, 3],money = [150, 250, 350]) == [15, 25, 35]: {e}')
    
    total += 1
    try:
        result = candidate(count = [50, 60, 70, 80, 90],upgrade = [3, 5, 7, 9, 11],sell = [2, 4, 6, 8, 10],money = [250, 500, 750, 1000, 1250]) == [50, 60, 70, 80, 90]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [50, 60, 70, 80, 90],upgrade = [3, 5, 7, 9, 11],sell = [2, 4, 6, 8, 10],money = [250, 500, 750, 1000, 1250]) == [50, 60, 70, 80, 90]: {e}')
    
    total += 1
    try:
        result = candidate(count = [5, 10, 15, 20, 25],upgrade = [2, 4, 6, 8, 10],sell = [1, 2, 3, 4, 5],money = [20, 40, 60, 80, 100]) == [5, 10, 11, 13, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [5, 10, 15, 20, 25],upgrade = [2, 4, 6, 8, 10],sell = [1, 2, 3, 4, 5],money = [20, 40, 60, 80, 100]) == [5, 10, 11, 13, 15]: {e}')
    
    total += 1
    try:
        result = candidate(count = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],upgrade = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sell = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],money = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]) == [10, 20, 30, 40, 50, 55, 60, 65, 70, 75]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],upgrade = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sell = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],money = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]) == [10, 20, 30, 40, 50, 55, 60, 65, 70, 75]: {e}')
    
    total += 1
    try:
        result = candidate(count = [99999, 99998, 99997],upgrade = [99999, 99998, 99997],sell = [99997, 99998, 99999],money = [1000000000, 1000000000, 1000000000]) == [54999, 54999, 54999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [99999, 99998, 99997],upgrade = [99999, 99998, 99997],sell = [99997, 99998, 99999],money = [1000000000, 1000000000, 1000000000]) == [54999, 54999, 54999]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100, 50, 75],upgrade = [10, 5, 20],sell = [5, 15, 25],money = [500, 250, 700]) == [66, 50, 57]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100, 50, 75],upgrade = [10, 5, 20],sell = [5, 15, 25],money = [500, 250, 700]) == [66, 50, 57]: {e}')
    
    total += 1
    try:
        result = candidate(count = [50, 50, 50, 50, 50],upgrade = [10, 20, 30, 40, 50],sell = [5, 15, 25, 35, 45],money = [1000, 2000, 3000, 4000, 5000]) == [50, 50, 50, 50, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [50, 50, 50, 50, 50],upgrade = [10, 20, 30, 40, 50],sell = [5, 15, 25, 35, 45],money = [1000, 2000, 3000, 4000, 5000]) == [50, 50, 50, 50, 50]: {e}')
    
    total += 1
    try:
        result = candidate(count = [1000, 2000, 3000, 4000, 5000],upgrade = [100, 200, 300, 400, 500],sell = [150, 250, 350, 450, 550],money = [10000, 20000, 30000, 40000, 50000]) == [640, 1155, 1661, 2164, 2666]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [1000, 2000, 3000, 4000, 5000],upgrade = [100, 200, 300, 400, 500],sell = [150, 250, 350, 450, 550],money = [10000, 20000, 30000, 40000, 50000]) == [640, 1155, 1661, 2164, 2666]: {e}')
    
    total += 1
    try:
        result = candidate(count = [50, 60, 70],upgrade = [5, 6, 7],sell = [2, 3, 4],money = [250, 300, 350]) == [50, 53, 57]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [50, 60, 70],upgrade = [5, 6, 7],sell = [2, 3, 4],money = [250, 300, 350]) == [50, 53, 57]: {e}')
    
    total += 1
    try:
        result = candidate(count = [1, 2, 3, 4, 5],upgrade = [100000, 90000, 80000, 70000, 60000],sell = [50000, 60000, 70000, 80000, 90000],money = [1000000, 1000000, 1000000, 1000000, 1000000]) == [1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [1, 2, 3, 4, 5],upgrade = [100000, 90000, 80000, 70000, 60000],sell = [50000, 60000, 70000, 80000, 90000],money = [1000000, 1000000, 1000000, 1000000, 1000000]) == [1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(count = [10000, 20000, 30000],upgrade = [1000, 2000, 3000],sell = [3000, 2000, 1000],money = [100000, 200000, 300000]) == [7525, 10050, 7575]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [10000, 20000, 30000],upgrade = [1000, 2000, 3000],sell = [3000, 2000, 1000],money = [100000, 200000, 300000]) == [7525, 10050, 7575]: {e}')
    
    total += 1
    try:
        result = candidate(count = [10000, 20000],upgrade = [100, 200],sell = [50, 100],money = [1000000, 2000000]) == [10000, 13333]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [10000, 20000],upgrade = [100, 200],sell = [50, 100],money = [1000000, 2000000]) == [10000, 13333]: {e}')
    
    total += 1
    try:
        result = candidate(count = [1, 2, 3, 4, 5],upgrade = [1, 1, 1, 1, 1],sell = [1, 1, 1, 1, 1],money = [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [1, 2, 3, 4, 5],upgrade = [1, 1, 1, 1, 1],sell = [1, 1, 1, 1, 1],money = [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100, 200, 300, 400],upgrade = [10, 9, 8, 7],sell = [7, 8, 9, 10],money = [500, 1000, 1500, 2000]) == [70, 152, 247, 352]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100, 200, 300, 400],upgrade = [10, 9, 8, 7],sell = [7, 8, 9, 10],money = [500, 1000, 1500, 2000]) == [70, 152, 247, 352]: {e}')
    
    total += 1
    try:
        result = candidate(count = [30, 60, 90],upgrade = [5, 10, 15],sell = [2, 4, 6],money = [150, 300, 450]) == [30, 38, 47]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [30, 60, 90],upgrade = [5, 10, 15],sell = [2, 4, 6],money = [150, 300, 450]) == [30, 38, 47]: {e}')
    
    total += 1
    try:
        result = candidate(count = [50, 50, 50, 50, 50],upgrade = [10, 15, 20, 25, 30],sell = [3, 6, 9, 12, 15],money = [100, 200, 300, 400, 500]) == [19, 23, 25, 27, 27]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [50, 50, 50, 50, 50],upgrade = [10, 15, 20, 25, 30],sell = [3, 6, 9, 12, 15],money = [100, 200, 300, 400, 500]) == [19, 23, 25, 27, 27]: {e}')
    
    total += 1
    try:
        result = candidate(count = [1, 1, 1, 1, 1],upgrade = [100000, 90000, 80000, 70000, 60000],sell = [50000, 60000, 70000, 80000, 90000],money = [100000, 100000, 100000, 100000, 100000]) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [1, 1, 1, 1, 1],upgrade = [100000, 90000, 80000, 70000, 60000],sell = [50000, 60000, 70000, 80000, 90000],money = [100000, 100000, 100000, 100000, 100000]) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100, 100, 100, 100],upgrade = [1, 1, 1, 1],sell = [1, 1, 1, 1],money = [100, 100, 100, 100]) == [100, 100, 100, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100, 100, 100, 100],upgrade = [1, 1, 1, 1],sell = [1, 1, 1, 1],money = [100, 100, 100, 100]) == [100, 100, 100, 100]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100000],upgrade = [1],sell = [1],money = [100000]) == [100000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100000],upgrade = [1],sell = [1],money = [100000]) == [100000]: {e}')
    
    total += 1
    try:
        result = candidate(count = [25, 50, 75, 100],upgrade = [5, 10, 15, 20],sell = [10, 20, 30, 40],money = [500, 1000, 1500, 2000]) == [25, 50, 75, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [25, 50, 75, 100],upgrade = [5, 10, 15, 20],sell = [10, 20, 30, 40],money = [500, 1000, 1500, 2000]) == [25, 50, 75, 100]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100000, 50000, 25000],upgrade = [1000, 500, 250],sell = [500, 250, 125],money = [10000000, 5000000, 2500000]) == [40000, 23333, 15000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100000, 50000, 25000],upgrade = [1000, 500, 250],sell = [500, 250, 125],money = [10000000, 5000000, 2500000]) == [40000, 23333, 15000]: {e}')
    
    total += 1
    try:
        result = candidate(count = [1000, 2000, 3000],upgrade = [50, 75, 100],sell = [25, 50, 75],money = [50000, 100000, 150000]) == [1000, 1600, 2142]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [1000, 2000, 3000],upgrade = [50, 75, 100],sell = [25, 50, 75],money = [50000, 100000, 150000]) == [1000, 1600, 2142]: {e}')
    
    total += 1
    try:
        result = candidate(count = [15, 25, 35, 45],upgrade = [2, 4, 6, 8],sell = [1, 3, 5, 7],money = [50, 75, 100, 125]) == [15, 21, 25, 29]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [15, 25, 35, 45],upgrade = [2, 4, 6, 8],sell = [1, 3, 5, 7],money = [50, 75, 100, 125]) == [15, 21, 25, 29]: {e}')
    
    total += 1
    try:
        result = candidate(count = [50, 40, 30, 20, 10],upgrade = [10, 20, 30, 40, 50],sell = [5, 10, 15, 20, 25],money = [100, 150, 200, 250, 300]) == [23, 18, 14, 10, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [50, 40, 30, 20, 10],upgrade = [10, 20, 30, 40, 50],sell = [5, 10, 15, 20, 25],money = [100, 150, 200, 250, 300]) == [23, 18, 14, 10, 7]: {e}')
    
    total += 1
    try:
        result = candidate(count = [1, 2, 3, 4, 5, 6],upgrade = [1000, 900, 800, 700, 600, 500],sell = [500, 600, 700, 800, 900, 1000],money = [10000, 20000, 30000, 40000, 50000, 60000]) == [1, 2, 3, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [1, 2, 3, 4, 5, 6],upgrade = [1000, 900, 800, 700, 600, 500],sell = [500, 600, 700, 800, 900, 1000],money = [10000, 20000, 30000, 40000, 50000, 60000]) == [1, 2, 3, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(count = [1000, 2000, 3000],upgrade = [10, 20, 30],sell = [5, 10, 15],money = [10000, 20000, 30000]) == [1000, 1333, 1666]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [1000, 2000, 3000],upgrade = [10, 20, 30],sell = [5, 10, 15],money = [10000, 20000, 30000]) == [1000, 1333, 1666]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100, 100],upgrade = [10, 5],sell = [20, 10],money = [1000, 500]) == [100, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100, 100],upgrade = [10, 5],sell = [20, 10],money = [1000, 500]) == [100, 100]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100000, 100000],upgrade = [1, 1],sell = [1, 1],money = [200000, 200000]) == [100000, 100000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100000, 100000],upgrade = [1, 1],sell = [1, 1],money = [200000, 200000]) == [100000, 100000]: {e}')
    
    total += 1
    try:
        result = candidate(count = [30, 20, 10],upgrade = [1, 2, 3],sell = [3, 2, 1],money = [100, 50, 10]) == [30, 20, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [30, 20, 10],upgrade = [1, 2, 3],sell = [3, 2, 1],money = [100, 50, 10]) == [30, 20, 5]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100, 200, 300, 400],upgrade = [1, 2, 3, 4],sell = [4, 3, 2, 1],money = [1000, 2000, 3000, 4000]) == [100, 200, 300, 400]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100, 200, 300, 400],upgrade = [1, 2, 3, 4],sell = [4, 3, 2, 1],money = [1000, 2000, 3000, 4000]) == [100, 200, 300, 400]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100000],upgrade = [1],sell = [1],money = [50000]) == [75000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100000],upgrade = [1],sell = [1],money = [50000]) == [75000]: {e}')
    
    total += 1
    try:
        result = candidate(count = [500, 500, 500, 500],upgrade = [5, 5, 5, 5],sell = [2, 2, 2, 2],money = [1000, 2000, 3000, 4000]) == [285, 428, 500, 500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [500, 500, 500, 500],upgrade = [5, 5, 5, 5],sell = [2, 2, 2, 2],money = [1000, 2000, 3000, 4000]) == [285, 428, 500, 500]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100000, 100000, 100000],upgrade = [50000, 60000, 70000],sell = [30000, 20000, 10000],money = [900000, 1200000, 1500000]) == [37511, 25015, 12518]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100000, 100000, 100000],upgrade = [50000, 60000, 70000],sell = [30000, 20000, 10000],money = [900000, 1200000, 1500000]) == [37511, 25015, 12518]: {e}')
    
    total += 1
    try:
        result = candidate(count = [1000, 2000, 3000, 4000],upgrade = [100, 200, 300, 400],sell = [10, 20, 30, 40],money = [10000, 20000, 30000, 40000]) == [181, 272, 363, 454]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [1000, 2000, 3000, 4000],upgrade = [100, 200, 300, 400],sell = [10, 20, 30, 40],money = [10000, 20000, 30000, 40000]) == [181, 272, 363, 454]: {e}')
    
    total += 1
    try:
        result = candidate(count = [1000, 2000, 3000],upgrade = [1, 1, 1],sell = [1, 1, 1],money = [1000, 2000, 3000]) == [1000, 2000, 3000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [1000, 2000, 3000],upgrade = [1, 1, 1],sell = [1, 1, 1],money = [1000, 2000, 3000]) == [1000, 2000, 3000]: {e}')
    
    total += 1
    try:
        result = candidate(count = [25, 25, 25, 25],upgrade = [10, 20, 30, 40],sell = [1, 2, 3, 4],money = [500, 750, 1000, 1250]) == [25, 25, 25, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [25, 25, 25, 25],upgrade = [10, 20, 30, 40],sell = [1, 2, 3, 4],money = [500, 750, 1000, 1250]) == [25, 25, 25, 25]: {e}')
    
    total += 1
    try:
        result = candidate(count = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],upgrade = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sell = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],money = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],upgrade = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sell = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],money = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(count = [50, 50, 50, 50, 50],upgrade = [1, 2, 3, 4, 5],sell = [5, 4, 3, 2, 1],money = [250, 200, 150, 100, 50]) == [50, 50, 50, 33, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [50, 50, 50, 50, 50],upgrade = [1, 2, 3, 4, 5],sell = [5, 4, 3, 2, 1],money = [250, 200, 150, 100, 50]) == [50, 50, 50, 33, 16]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],upgrade = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sell = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],money = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],upgrade = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sell = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],money = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]: {e}')
    
    total += 1
    try:
        result = candidate(count = [15, 25, 35],upgrade = [7, 11, 13],sell = [5, 8, 6],money = [150, 250, 350]) == [15, 23, 29]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [15, 25, 35],upgrade = [7, 11, 13],sell = [5, 8, 6],money = [150, 250, 350]) == [15, 23, 29]: {e}')
    
    total += 1
    try:
        result = candidate(count = [10, 20, 30, 40, 50],upgrade = [1, 2, 3, 4, 5],sell = [5, 4, 3, 2, 1],money = [50, 100, 150, 200, 250]) == [10, 20, 30, 40, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [10, 20, 30, 40, 50],upgrade = [1, 2, 3, 4, 5],sell = [5, 4, 3, 2, 1],money = [50, 100, 150, 200, 250]) == [10, 20, 30, 40, 50]: {e}')
    
    total += 1
    try:
        result = candidate(count = [10, 20, 30, 40],upgrade = [5, 4, 3, 2],sell = [2, 3, 4, 5],money = [50, 100, 150, 200]) == [10, 20, 30, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [10, 20, 30, 40],upgrade = [5, 4, 3, 2],sell = [2, 3, 4, 5],money = [50, 100, 150, 200]) == [10, 20, 30, 40]: {e}')
    
    total += 1
    try:
        result = candidate(count = [1000, 2000],upgrade = [50, 75],sell = [25, 35],money = [10000, 20000]) == [466, 818]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [1000, 2000],upgrade = [50, 75],sell = [25, 35],money = [10000, 20000]) == [466, 818]: {e}')
    
    total += 1
    try:
        result = candidate(count = [90000, 10000],upgrade = [9, 1],sell = [1, 9],money = [900000, 100000]) == [90000, 10000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [90000, 10000],upgrade = [9, 1],sell = [1, 9],money = [900000, 100000]) == [90000, 10000]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100, 100, 100, 100],upgrade = [10, 20, 30, 40],sell = [40, 30, 20, 10],money = [1000, 2000, 3000, 4000]) == [100, 100, 100, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100, 100, 100, 100],upgrade = [10, 20, 30, 40],sell = [40, 30, 20, 10],money = [1000, 2000, 3000, 4000]) == [100, 100, 100, 100]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100, 200, 300, 400],upgrade = [15, 25, 35, 45],sell = [5, 10, 15, 20],money = [1000, 2000, 3000, 4000]) == [75, 114, 150, 184]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100, 200, 300, 400],upgrade = [15, 25, 35, 45],sell = [5, 10, 15, 20],money = [1000, 2000, 3000, 4000]) == [75, 114, 150, 184]: {e}')
    
    total += 1
    try:
        result = candidate(count = [1, 2, 3, 4, 5],upgrade = [1, 2, 3, 4, 5],sell = [5, 4, 3, 2, 1],money = [5, 10, 15, 20, 25]) == [1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [1, 2, 3, 4, 5],upgrade = [1, 2, 3, 4, 5],sell = [5, 4, 3, 2, 1],money = [5, 10, 15, 20, 25]) == [1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(count = [50, 50, 50, 50],upgrade = [5, 6, 7, 8],sell = [8, 7, 6, 5],money = [500, 600, 700, 800]) == [50, 50, 50, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [50, 50, 50, 50],upgrade = [5, 6, 7, 8],sell = [8, 7, 6, 5],money = [500, 600, 700, 800]) == [50, 50, 50, 50]: {e}')
    
    total += 1
    try:
        result = candidate(count = [99999, 99998, 99997],upgrade = [99, 98, 97],sell = [97, 96, 95],money = [9999900, 9999800, 9999700]) == [99999, 99998, 99997]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [99999, 99998, 99997],upgrade = [99, 98, 97],sell = [97, 96, 95],money = [9999900, 9999800, 9999700]) == [99999, 99998, 99997]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100, 150, 200],upgrade = [5, 7, 9],sell = [8, 6, 4],money = [300, 450, 600]) == [84, 103, 107]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100, 150, 200],upgrade = [5, 7, 9],sell = [8, 6, 4],money = [300, 450, 600]) == [84, 103, 107]: {e}')
    
    total += 1
    try:
        result = candidate(count = [20, 40, 60, 80, 100],upgrade = [1, 2, 3, 4, 5],sell = [10, 20, 30, 40, 50],money = [500, 1000, 1500, 2000, 2500]) == [20, 40, 60, 80, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [20, 40, 60, 80, 100],upgrade = [1, 2, 3, 4, 5],sell = [10, 20, 30, 40, 50],money = [500, 1000, 1500, 2000, 2500]) == [20, 40, 60, 80, 100]: {e}')
    
    total += 1
    try:
        result = candidate(count = [50000, 50000],upgrade = [2, 2],sell = [1, 1],money = [150000, 150000]) == [50000, 50000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [50000, 50000],upgrade = [2, 2],sell = [1, 1],money = [150000, 150000]) == [50000, 50000]: {e}')
    
    total += 1
    try:
        result = candidate(count = [50, 60, 70],upgrade = [3, 4, 5],sell = [2, 3, 4],money = [150, 200, 250]) == [50, 54, 58]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [50, 60, 70],upgrade = [3, 4, 5],sell = [2, 3, 4],money = [150, 200, 250]) == [50, 54, 58]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100000],upgrade = [1],sell = [10],money = [900000]) == [100000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100000],upgrade = [1],sell = [10],money = [900000]) == [100000]: {e}')
    
    total += 1
    try:
        result = candidate(count = [10, 20, 30, 40, 50],upgrade = [5, 10, 15, 20, 25],sell = [30, 25, 20, 15, 10],money = [1000, 2000, 3000, 4000, 5000]) == [10, 20, 30, 40, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [10, 20, 30, 40, 50],upgrade = [5, 10, 15, 20, 25],sell = [30, 25, 20, 15, 10],money = [1000, 2000, 3000, 4000, 5000]) == [10, 20, 30, 40, 50]: {e}')
    
    total += 1
    try:
        result = candidate(count = [33333, 33333, 33333],upgrade = [1, 1, 1],sell = [1, 1, 1],money = [1000000, 1000000, 1000000]) == [33333, 33333, 33333]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [33333, 33333, 33333],upgrade = [1, 1, 1],sell = [1, 1, 1],money = [1000000, 1000000, 1000000]) == [33333, 33333, 33333]: {e}')
    
    total += 1
    try:
        result = candidate(count = [1000, 2000, 3000],upgrade = [1, 2, 3],sell = [2, 4, 6],money = [20000, 40000, 60000]) == [1000, 2000, 3000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [1000, 2000, 3000],upgrade = [1, 2, 3],sell = [2, 4, 6],money = [20000, 40000, 60000]) == [1000, 2000, 3000]: {e}')
    
    total += 1
    try:
        result = candidate(count = [100, 100, 100, 100],upgrade = [1, 2, 3, 4],sell = [4, 3, 2, 1],money = [100, 200, 300, 400]) == [100, 100, 100, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [100, 100, 100, 100],upgrade = [1, 2, 3, 4],sell = [4, 3, 2, 1],money = [100, 200, 300, 400]) == [100, 100, 100, 100]: {e}')
    
    total += 1
    try:
        result = candidate(count = [1, 2, 3, 4, 5],upgrade = [1, 1, 1, 1, 1],sell = [2, 2, 2, 2, 2],money = [0, 1, 3, 6, 10]) == [0, 1, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(count = [1, 2, 3, 4, 5],upgrade = [1, 1, 1, 1, 1],sell = [2, 2, 2, 2, 2],money = [0, 1, 3, 6, 10]) == [0, 1, 3, 4, 5]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(count = [100000],upgrade = [100000],sell = [100000],money = [1000000000]) == [55000]
    assert candidate(count = [10, 20, 30],upgrade = [5, 4, 3],sell = [1, 2, 3],money = [50, 100, 150]) == [10, 20, 30]
    assert candidate(count = [10, 20, 30],upgrade = [1, 2, 3],sell = [4, 5, 6],money = [100, 100, 100]) == [10, 20, 30]
    assert candidate(count = [4, 3],upgrade = [3, 5],sell = [4, 2],money = [8, 9]) == [3, 2]
    assert candidate(count = [5, 5, 5],upgrade = [10, 20, 30],sell = [5, 10, 15],money = [100, 100, 100]) == [5, 5, 3]
    assert candidate(count = [1],upgrade = [2],sell = [1],money = [1]) == [0]
    assert candidate(count = [10, 20, 30],upgrade = [5, 10, 15],sell = [1, 2, 3],money = [100, 200, 300]) == [10, 20, 21]
    assert candidate(count = [10, 20, 30],upgrade = [1, 2, 3],sell = [4, 5, 6],money = [50, 100, 150]) == [10, 20, 30]
    assert candidate(count = [5, 5, 5],upgrade = [10, 20, 30],sell = [5, 15, 25],money = [100, 150, 200]) == [5, 5, 5]
    assert candidate(count = [5, 5, 5],upgrade = [1, 2, 3],sell = [3, 2, 1],money = [10, 10, 10]) == [5, 5, 3]
    assert candidate(count = [100, 100, 100],upgrade = [1000, 1000, 1000],sell = [500, 500, 500],money = [50000, 50000, 50000]) == [66, 66, 66]
    assert candidate(count = [100],upgrade = [10],sell = [5],money = [500]) == [66]
    assert candidate(count = [10, 20, 30],upgrade = [1, 2, 3],sell = [3, 2, 1],money = [100, 200, 300]) == [10, 20, 30]
    assert candidate(count = [5, 5, 5],upgrade = [10, 10, 10],sell = [5, 5, 5],money = [50, 50, 50]) == [5, 5, 5]
    assert candidate(count = [5, 5, 5],upgrade = [10, 10, 10],sell = [5, 5, 5],money = [20, 20, 20]) == [3, 3, 3]
    assert candidate(count = [2, 4, 6],upgrade = [1, 2, 3],sell = [2, 4, 6],money = [10, 20, 30]) == [2, 4, 6]
    assert candidate(count = [100, 200, 300, 400],upgrade = [5, 10, 15, 20],sell = [20, 15, 10, 5],money = [500, 1000, 1500, 2000]) == [100, 160, 180, 160]
    assert candidate(count = [100, 200, 300, 400, 500],upgrade = [5, 10, 15, 20, 25],sell = [20, 15, 10, 5, 1],money = [1000, 2000, 3000, 4000, 5000]) == [100, 200, 240, 240, 211]
    assert candidate(count = [1, 2, 3, 4, 5],upgrade = [10, 20, 30, 40, 50],sell = [50, 40, 30, 20, 10],money = [100, 200, 300, 400, 500]) == [1, 2, 3, 4, 5]
    assert candidate(count = [15, 25, 35, 45],upgrade = [2, 3, 4, 5],sell = [5, 4, 3, 2],money = [150, 250, 350, 450]) == [15, 25, 35, 45]
    assert candidate(count = [100, 50, 25],upgrade = [5, 10, 15],sell = [2, 4, 6],money = [1000, 500, 250]) == [100, 50, 19]
    assert candidate(count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],upgrade = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],sell = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],money = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]) == [1, 2, 3, 4, 5, 5, 5, 6, 6, 6]
    assert candidate(count = [30000, 25000, 20000],upgrade = [100, 150, 200],sell = [200, 150, 100],money = [5000000, 4000000, 3000000]) == [30000, 25000, 16666]
    assert candidate(count = [1, 2, 3, 4, 5],upgrade = [1, 2, 3, 4, 5],sell = [5, 4, 3, 2, 1],money = [15, 10, 5, 0, 0]) == [1, 2, 2, 1, 0]
    assert candidate(count = [333, 666, 999],upgrade = [33, 66, 99],sell = [11, 22, 33],money = [1110, 2220, 3330]) == [108, 191, 274]
    assert candidate(count = [50, 50, 50, 50],upgrade = [2, 3, 4, 5],sell = [3, 2, 1, 4],money = [150, 200, 250, 300]) == [50, 50, 50, 50]
    assert candidate(count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],upgrade = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sell = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],money = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(count = [1000, 2000, 3000],upgrade = [1, 2, 3],sell = [2, 1, 2],money = [5000, 10000, 15000]) == [1000, 2000, 3000]
    assert candidate(count = [10, 10, 10, 10, 10],upgrade = [1, 2, 3, 4, 5],sell = [5, 4, 3, 2, 1],money = [50, 40, 30, 20, 10]) == [10, 10, 10, 6, 3]
    assert candidate(count = [20, 25, 30, 35, 40, 45, 50],upgrade = [5, 6, 7, 8, 9, 10, 11],sell = [11, 10, 9, 8, 7, 6, 5],money = [200, 250, 300, 350, 400, 450, 500]) == [20, 25, 30, 35, 40, 45, 46]
    assert candidate(count = [500, 500, 500, 500],upgrade = [10, 20, 30, 40],sell = [20, 10, 40, 30],money = [2000, 1000, 4000, 3000]) == [400, 200, 342, 257]
    assert candidate(count = [50, 75, 100],upgrade = [2, 3, 4],sell = [1, 2, 3],money = [100, 200, 300]) == [50, 70, 85]
    assert candidate(count = [100, 100, 100, 100],upgrade = [1, 1, 1, 1],sell = [2, 2, 2, 2],money = [1000, 2000, 3000, 4000]) == [100, 100, 100, 100]
    assert candidate(count = [100, 150, 200],upgrade = [10, 15, 20],sell = [5, 10, 15],money = [1000, 1500, 2000]) == [100, 120, 142]
    assert candidate(count = [50, 50, 50],upgrade = [10, 20, 30],sell = [15, 25, 35],money = [500, 750, 1000]) == [50, 44, 42]
    assert candidate(count = [50, 50, 50, 50, 50],upgrade = [10, 20, 30, 40, 50],sell = [5, 10, 15, 20, 25],money = [500, 1000, 1500, 2000, 2500]) == [50, 50, 50, 50, 50]
    assert candidate(count = [15, 25, 35],upgrade = [4, 6, 8],sell = [7, 5, 3],money = [150, 250, 350]) == [15, 25, 35]
    assert candidate(count = [50, 60, 70, 80, 90],upgrade = [3, 5, 7, 9, 11],sell = [2, 4, 6, 8, 10],money = [250, 500, 750, 1000, 1250]) == [50, 60, 70, 80, 90]
    assert candidate(count = [5, 10, 15, 20, 25],upgrade = [2, 4, 6, 8, 10],sell = [1, 2, 3, 4, 5],money = [20, 40, 60, 80, 100]) == [5, 10, 11, 13, 15]
    assert candidate(count = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],upgrade = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sell = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],money = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]) == [10, 20, 30, 40, 50, 55, 60, 65, 70, 75]
    assert candidate(count = [99999, 99998, 99997],upgrade = [99999, 99998, 99997],sell = [99997, 99998, 99999],money = [1000000000, 1000000000, 1000000000]) == [54999, 54999, 54999]
    assert candidate(count = [100, 50, 75],upgrade = [10, 5, 20],sell = [5, 15, 25],money = [500, 250, 700]) == [66, 50, 57]
    assert candidate(count = [50, 50, 50, 50, 50],upgrade = [10, 20, 30, 40, 50],sell = [5, 15, 25, 35, 45],money = [1000, 2000, 3000, 4000, 5000]) == [50, 50, 50, 50, 50]
    assert candidate(count = [1000, 2000, 3000, 4000, 5000],upgrade = [100, 200, 300, 400, 500],sell = [150, 250, 350, 450, 550],money = [10000, 20000, 30000, 40000, 50000]) == [640, 1155, 1661, 2164, 2666]
    assert candidate(count = [50, 60, 70],upgrade = [5, 6, 7],sell = [2, 3, 4],money = [250, 300, 350]) == [50, 53, 57]
    assert candidate(count = [1, 2, 3, 4, 5],upgrade = [100000, 90000, 80000, 70000, 60000],sell = [50000, 60000, 70000, 80000, 90000],money = [1000000, 1000000, 1000000, 1000000, 1000000]) == [1, 2, 3, 4, 5]
    assert candidate(count = [10000, 20000, 30000],upgrade = [1000, 2000, 3000],sell = [3000, 2000, 1000],money = [100000, 200000, 300000]) == [7525, 10050, 7575]
    assert candidate(count = [10000, 20000],upgrade = [100, 200],sell = [50, 100],money = [1000000, 2000000]) == [10000, 13333]
    assert candidate(count = [1, 2, 3, 4, 5],upgrade = [1, 1, 1, 1, 1],sell = [1, 1, 1, 1, 1],money = [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert candidate(count = [100, 200, 300, 400],upgrade = [10, 9, 8, 7],sell = [7, 8, 9, 10],money = [500, 1000, 1500, 2000]) == [70, 152, 247, 352]
    assert candidate(count = [30, 60, 90],upgrade = [5, 10, 15],sell = [2, 4, 6],money = [150, 300, 450]) == [30, 38, 47]
    assert candidate(count = [50, 50, 50, 50, 50],upgrade = [10, 15, 20, 25, 30],sell = [3, 6, 9, 12, 15],money = [100, 200, 300, 400, 500]) == [19, 23, 25, 27, 27]
    assert candidate(count = [1, 1, 1, 1, 1],upgrade = [100000, 90000, 80000, 70000, 60000],sell = [50000, 60000, 70000, 80000, 90000],money = [100000, 100000, 100000, 100000, 100000]) == [1, 1, 1, 1, 1]
    assert candidate(count = [100, 100, 100, 100],upgrade = [1, 1, 1, 1],sell = [1, 1, 1, 1],money = [100, 100, 100, 100]) == [100, 100, 100, 100]
    assert candidate(count = [100000],upgrade = [1],sell = [1],money = [100000]) == [100000]
    assert candidate(count = [25, 50, 75, 100],upgrade = [5, 10, 15, 20],sell = [10, 20, 30, 40],money = [500, 1000, 1500, 2000]) == [25, 50, 75, 100]
    assert candidate(count = [100000, 50000, 25000],upgrade = [1000, 500, 250],sell = [500, 250, 125],money = [10000000, 5000000, 2500000]) == [40000, 23333, 15000]
    assert candidate(count = [1000, 2000, 3000],upgrade = [50, 75, 100],sell = [25, 50, 75],money = [50000, 100000, 150000]) == [1000, 1600, 2142]
    assert candidate(count = [15, 25, 35, 45],upgrade = [2, 4, 6, 8],sell = [1, 3, 5, 7],money = [50, 75, 100, 125]) == [15, 21, 25, 29]
    assert candidate(count = [50, 40, 30, 20, 10],upgrade = [10, 20, 30, 40, 50],sell = [5, 10, 15, 20, 25],money = [100, 150, 200, 250, 300]) == [23, 18, 14, 10, 7]
    assert candidate(count = [1, 2, 3, 4, 5, 6],upgrade = [1000, 900, 800, 700, 600, 500],sell = [500, 600, 700, 800, 900, 1000],money = [10000, 20000, 30000, 40000, 50000, 60000]) == [1, 2, 3, 4, 5, 6]
    assert candidate(count = [1000, 2000, 3000],upgrade = [10, 20, 30],sell = [5, 10, 15],money = [10000, 20000, 30000]) == [1000, 1333, 1666]
    assert candidate(count = [100, 100],upgrade = [10, 5],sell = [20, 10],money = [1000, 500]) == [100, 100]
    assert candidate(count = [100000, 100000],upgrade = [1, 1],sell = [1, 1],money = [200000, 200000]) == [100000, 100000]
    assert candidate(count = [30, 20, 10],upgrade = [1, 2, 3],sell = [3, 2, 1],money = [100, 50, 10]) == [30, 20, 5]
    assert candidate(count = [100, 200, 300, 400],upgrade = [1, 2, 3, 4],sell = [4, 3, 2, 1],money = [1000, 2000, 3000, 4000]) == [100, 200, 300, 400]
    assert candidate(count = [100000],upgrade = [1],sell = [1],money = [50000]) == [75000]
    assert candidate(count = [500, 500, 500, 500],upgrade = [5, 5, 5, 5],sell = [2, 2, 2, 2],money = [1000, 2000, 3000, 4000]) == [285, 428, 500, 500]
    assert candidate(count = [100000, 100000, 100000],upgrade = [50000, 60000, 70000],sell = [30000, 20000, 10000],money = [900000, 1200000, 1500000]) == [37511, 25015, 12518]
    assert candidate(count = [1000, 2000, 3000, 4000],upgrade = [100, 200, 300, 400],sell = [10, 20, 30, 40],money = [10000, 20000, 30000, 40000]) == [181, 272, 363, 454]
    assert candidate(count = [1000, 2000, 3000],upgrade = [1, 1, 1],sell = [1, 1, 1],money = [1000, 2000, 3000]) == [1000, 2000, 3000]
    assert candidate(count = [25, 25, 25, 25],upgrade = [10, 20, 30, 40],sell = [1, 2, 3, 4],money = [500, 750, 1000, 1250]) == [25, 25, 25, 25]
    assert candidate(count = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],upgrade = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sell = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],money = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert candidate(count = [50, 50, 50, 50, 50],upgrade = [1, 2, 3, 4, 5],sell = [5, 4, 3, 2, 1],money = [250, 200, 150, 100, 50]) == [50, 50, 50, 33, 16]
    assert candidate(count = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],upgrade = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sell = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],money = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    assert candidate(count = [15, 25, 35],upgrade = [7, 11, 13],sell = [5, 8, 6],money = [150, 250, 350]) == [15, 23, 29]
    assert candidate(count = [10, 20, 30, 40, 50],upgrade = [1, 2, 3, 4, 5],sell = [5, 4, 3, 2, 1],money = [50, 100, 150, 200, 250]) == [10, 20, 30, 40, 50]
    assert candidate(count = [10, 20, 30, 40],upgrade = [5, 4, 3, 2],sell = [2, 3, 4, 5],money = [50, 100, 150, 200]) == [10, 20, 30, 40]
    assert candidate(count = [1000, 2000],upgrade = [50, 75],sell = [25, 35],money = [10000, 20000]) == [466, 818]
    assert candidate(count = [90000, 10000],upgrade = [9, 1],sell = [1, 9],money = [900000, 100000]) == [90000, 10000]
    assert candidate(count = [100, 100, 100, 100],upgrade = [10, 20, 30, 40],sell = [40, 30, 20, 10],money = [1000, 2000, 3000, 4000]) == [100, 100, 100, 100]
    assert candidate(count = [100, 200, 300, 400],upgrade = [15, 25, 35, 45],sell = [5, 10, 15, 20],money = [1000, 2000, 3000, 4000]) == [75, 114, 150, 184]
    assert candidate(count = [1, 2, 3, 4, 5],upgrade = [1, 2, 3, 4, 5],sell = [5, 4, 3, 2, 1],money = [5, 10, 15, 20, 25]) == [1, 2, 3, 4, 5]
    assert candidate(count = [50, 50, 50, 50],upgrade = [5, 6, 7, 8],sell = [8, 7, 6, 5],money = [500, 600, 700, 800]) == [50, 50, 50, 50]
    assert candidate(count = [99999, 99998, 99997],upgrade = [99, 98, 97],sell = [97, 96, 95],money = [9999900, 9999800, 9999700]) == [99999, 99998, 99997]
    assert candidate(count = [100, 150, 200],upgrade = [5, 7, 9],sell = [8, 6, 4],money = [300, 450, 600]) == [84, 103, 107]
    assert candidate(count = [20, 40, 60, 80, 100],upgrade = [1, 2, 3, 4, 5],sell = [10, 20, 30, 40, 50],money = [500, 1000, 1500, 2000, 2500]) == [20, 40, 60, 80, 100]
    assert candidate(count = [50000, 50000],upgrade = [2, 2],sell = [1, 1],money = [150000, 150000]) == [50000, 50000]
    assert candidate(count = [50, 60, 70],upgrade = [3, 4, 5],sell = [2, 3, 4],money = [150, 200, 250]) == [50, 54, 58]
    assert candidate(count = [100000],upgrade = [1],sell = [10],money = [900000]) == [100000]
    assert candidate(count = [10, 20, 30, 40, 50],upgrade = [5, 10, 15, 20, 25],sell = [30, 25, 20, 15, 10],money = [1000, 2000, 3000, 4000, 5000]) == [10, 20, 30, 40, 50]
    assert candidate(count = [33333, 33333, 33333],upgrade = [1, 1, 1],sell = [1, 1, 1],money = [1000000, 1000000, 1000000]) == [33333, 33333, 33333]
    assert candidate(count = [1000, 2000, 3000],upgrade = [1, 2, 3],sell = [2, 4, 6],money = [20000, 40000, 60000]) == [1000, 2000, 3000]
    assert candidate(count = [100, 100, 100, 100],upgrade = [1, 2, 3, 4],sell = [4, 3, 2, 1],money = [100, 200, 300, 400]) == [100, 100, 100, 100]
    assert candidate(count = [1, 2, 3, 4, 5],upgrade = [1, 1, 1, 1, 1],sell = [2, 2, 2, 2, 2],money = [0, 1, 3, 6, 10]) == [0, 1, 3, 4, 5]


