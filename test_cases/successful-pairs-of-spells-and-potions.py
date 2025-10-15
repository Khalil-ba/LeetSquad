def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(spells = [3, 1, 2],potions = [8, 5, 8],success = 16) == [2, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [3, 1, 2],potions = [8, 5, 8],success = 16) == [2, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 1, 1],potions = [1, 1, 1],success = 2) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 1, 1],potions = [1, 1, 1],success = 2) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [5, 1, 3],potions = [1, 2, 3, 4, 5],success = 7) == [4, 0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [5, 1, 3],potions = [1, 2, 3, 4, 5],success = 7) == [4, 0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 2, 3, 4, 5],potions = [5, 4, 3, 2, 1],success = 10) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 2, 3, 4, 5],potions = [5, 4, 3, 2, 1],success = 10) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [10, 20, 30],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 50) == [6, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [10, 20, 30],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 50) == [6, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100000, 100000, 100000],potions = [100000, 100000, 100000],success = 10000000000) == [3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100000, 100000, 100000],potions = [100000, 100000, 100000],success = 10000000000) == [3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [10, 20, 30],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 100) == [1, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [10, 20, 30],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 100) == [1, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 1, 1],potions = [1, 1, 1, 1],success = 1) == [4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 1, 1],potions = [1, 1, 1, 1],success = 1) == [4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [10, 10, 10],potions = [1, 1, 1, 1, 1],success = 100) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [10, 10, 10],potions = [1, 1, 1, 1, 1],success = 100) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 1, 1, 1],potions = [1, 1, 1, 1],success = 1) == [4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 1, 1, 1],potions = [1, 1, 1, 1],success = 1) == [4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 2, 3, 4, 5],potions = [5, 4, 3, 2, 1],success = 6) == [0, 3, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 2, 3, 4, 5],potions = [5, 4, 3, 2, 1],success = 6) == [0, 3, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [10, 20, 30],potions = [5, 10, 15, 20],success = 100) == [3, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [10, 20, 30],potions = [5, 10, 15, 20],success = 100) == [3, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100000],potions = [100000],success = 10000000000) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100000],potions = [100000],success = 10000000000) == [1]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100, 200, 300, 400, 500],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],success = 500) == [11, 13, 14, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100, 200, 300, 400, 500],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],success = 500) == [11, 13, 14, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991],success = 4999750005) == [2, 2, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991],success = 4999750005) == [2, 2, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],potions = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],success = 100000) == [1, 6, 7, 8, 9, 9, 9, 9, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],potions = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],success = 100000) == [1, 6, 7, 8, 9, 9, 9, 9, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 10000000000) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 10000000000) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [100000, 99999, 99998, 99997, 99996, 99995],success = 9999900000) == [1, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [100000, 99999, 99998, 99997, 99996, 99995],success = 9999900000) == [1, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 1, 1, 1, 1],potions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],success = 2) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 1, 1, 1, 1],potions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],success = 2) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 1, 1, 1, 1],potions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],success = 1) == [10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 1, 1, 1, 1],potions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],success = 1) == [10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],potions = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],success = 50) == [6, 8, 9, 9, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],potions = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],success = 50) == [6, 8, 9, 9, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 10, 100, 1000, 10000],potions = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000],success = 10000) == [0, 1, 4, 7, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 10, 100, 1000, 10000],potions = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000],success = 10000) == [0, 1, 4, 7, 10]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 3, 5, 7, 9],potions = [11, 13, 15, 17, 19, 21, 23, 25, 27, 29],success = 50) == [0, 7, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 3, 5, 7, 9],potions = [11, 13, 15, 17, 19, 21, 23, 25, 27, 29],success = 50) == [0, 7, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [50000, 60000, 70000, 80000, 90000, 100000],potions = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],success = 5000000000) == [5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [50000, 60000, 70000, 80000, 90000, 100000],potions = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],success = 5000000000) == [5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [2, 4, 6, 8, 10],potions = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],success = 100) == [1, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [2, 4, 6, 8, 10],potions = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],success = 100) == [1, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100, 200, 300, 400, 500],potions = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],success = 5000) == [10, 16, 19, 20, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100, 200, 300, 400, 500],potions = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],success = 5000) == [10, 16, 19, 20, 21]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [5, 10, 15, 20, 25],potions = [20, 25, 30, 35, 40, 45, 50, 55, 60],success = 500) == [0, 3, 6, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [5, 10, 15, 20, 25],potions = [20, 25, 30, 35, 40, 45, 50, 55, 60],success = 500) == [0, 3, 6, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1000, 2000, 3000, 4000, 5000],potions = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],success = 10000) == [9, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1000, 2000, 3000, 4000, 5000],potions = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],success = 10000) == [9, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [99999, 99998, 99997, 99996, 99995],success = 99990000025) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [99999, 99998, 99997, 99996, 99995],success = 99990000025) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [5, 10, 15, 20, 25],potions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],success = 50) == [5, 8, 8, 9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [5, 10, 15, 20, 25],potions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],success = 50) == [5, 8, 8, 9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 2, 3, 4, 5],potions = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],success = 100000) == [0, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 2, 3, 4, 5],potions = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],success = 100000) == [0, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [9, 8, 7, 6, 5],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9],success = 20) == [7, 7, 7, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [9, 8, 7, 6, 5],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9],success = 20) == [7, 7, 7, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [33333, 66666, 99999],potions = [33333, 66666, 99999, 133332, 166665, 199998],success = 10000000000) == [0, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [33333, 66666, 99999],potions = [33333, 66666, 99999, 133332, 166665, 199998],success = 10000000000) == [0, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100, 200, 300, 400, 500],potions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],success = 100) == [10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100, 200, 300, 400, 500],potions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],success = 100) == [10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],potions = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],success = 250) == [1, 6, 7, 8, 9, 9, 9, 9, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],potions = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],success = 250) == [1, 6, 7, 8, 9, 9, 9, 9, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [50000, 50000, 50000, 50000],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 100000) == [10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [50000, 50000, 50000, 50000],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 100000) == [10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],potions = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],success = 2500) == [0, 0, 2, 4, 6, 6, 7, 7, 8, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],potions = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],success = 2500) == [0, 0, 2, 4, 6, 6, 7, 7, 8, 8]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [50000, 25000, 12500],potions = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],success = 625000000) == [9, 8, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [50000, 25000, 12500],potions = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],success = 625000000) == [9, 8, 6]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100000, 50000, 25000, 12500, 6250],potions = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],success = 10000000000) == [4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100000, 50000, 25000, 12500, 6250],potions = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],success = 10000000000) == [4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 2, 3, 4, 5],potions = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],success = 25) == [6, 8, 9, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 2, 3, 4, 5],potions = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],success = 25) == [6, 8, 9, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 2, 3, 4, 5],potions = [100000, 200000, 300000, 400000, 500000],success = 1000000) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 2, 3, 4, 5],potions = [100000, 200000, 300000, 400000, 500000],success = 1000000) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100000, 90000, 80000],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 500000) == [6, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100000, 90000, 80000],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 500000) == [6, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 1, 1, 1, 1],potions = [100000, 100000, 100000, 100000, 100000],success = 100000) == [5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 1, 1, 1, 1],potions = [100000, 100000, 100000, 100000, 100000],success = 100000) == [5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [10000, 20000, 30000, 40000, 50000],potions = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000],success = 200000000) == [7, 9, 9, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [10000, 20000, 30000, 40000, 50000],potions = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000],success = 200000000) == [7, 9, 9, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [50000, 50000, 50000, 50000, 50000],potions = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],success = 5000000000) == [4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [50000, 50000, 50000, 50000, 50000],potions = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],success = 5000000000) == [4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [10000, 5000, 2500],potions = [5000, 10000, 15000, 20000, 25000],success = 100000000) == [4, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [10000, 5000, 2500],potions = [5000, 10000, 15000, 20000, 25000],success = 100000000) == [4, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],potions = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],success = 1000000) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],potions = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],success = 1000000) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [5, 15, 25, 35, 45],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 100) == [1, 7, 9, 9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [5, 15, 25, 35, 45],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 100) == [1, 7, 9, 9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100000, 100000, 100000, 100000],potions = [100000, 100000, 100000, 100000, 100000],success = 10000000000) == [5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100000, 100000, 100000, 100000],potions = [100000, 100000, 100000, 100000, 100000],success = 10000000000) == [5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [5, 5, 5, 5, 5],potions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],success = 6) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [5, 5, 5, 5, 5],potions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],success = 6) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 3, 5, 7, 9],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 18) == [2, 8, 9, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 3, 5, 7, 9],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 18) == [2, 8, 9, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 1, 1, 1, 1],potions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],success = 1) == [21, 21, 21, 21, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 1, 1, 1, 1],potions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],success = 1) == [21, 21, 21, 21, 21]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [3, 3, 3, 3, 3],potions = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],success = 10) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [3, 3, 3, 3, 3],potions = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],success = 10) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 3, 5, 7, 9],potions = [9, 7, 5, 3, 1],success = 15) == [0, 3, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 3, 5, 7, 9],potions = [9, 7, 5, 3, 1],success = 15) == [0, 3, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [9, 7, 5, 3, 1],potions = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2],success = 50) == [8, 7, 6, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [9, 7, 5, 3, 1],potions = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2],success = 50) == [8, 7, 6, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 20) == [1, 7, 9, 9, 9, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 20) == [1, 7, 9, 9, 9, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [10000, 20000, 30000, 40000],potions = [25000, 50000, 75000, 100000, 125000, 150000, 175000, 200000],success = 2000000000) == [1, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [10000, 20000, 30000, 40000],potions = [25000, 50000, 75000, 100000, 125000, 150000, 175000, 200000],success = 2000000000) == [1, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100000, 50000, 25000, 12500, 6250],potions = [200000, 100000, 50000, 25000, 12500, 6250],success = 10000000000) == [2, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100000, 50000, 25000, 12500, 6250],potions = [200000, 100000, 50000, 25000, 12500, 6250],success = 10000000000) == [2, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],success = 9999500000) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],success = 9999500000) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [50, 25, 10, 2],potions = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],success = 5000) == [4, 3, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [50, 25, 10, 2],potions = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],success = 5000) == [4, 3, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100000, 50000, 25000, 12500, 6250],potions = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],success = 5000000000) == [5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100000, 50000, 25000, 12500, 6250],potions = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],success = 5000000000) == [5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],potions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],success = 10) == [1, 6, 7, 8, 9, 9, 9, 9, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],potions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],success = 10) == [1, 6, 7, 8, 9, 9, 9, 9, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1000, 2000, 3000, 4000, 5000],potions = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],success = 5000000) == [0, 0, 0, 0, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1000, 2000, 3000, 4000, 5000],potions = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],success = 5000000) == [0, 0, 0, 0, 10]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],success = 9999500000) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],success = 9999500000) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],potions = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],success = 100000) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],potions = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],success = 100000) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [5, 5, 5, 5, 5],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 25) == [6, 6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [5, 5, 5, 5, 5],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 25) == [6, 6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],potions = [100, 200, 300, 400, 500],success = 5000) == [0, 0, 0, 0, 1, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],potions = [100, 200, 300, 400, 500],success = 5000) == [0, 0, 0, 0, 1, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100, 200, 300, 400, 500],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],success = 1000) == [11, 16, 17, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100, 200, 300, 400, 500],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],success = 1000) == [11, 16, 17, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100000, 90000, 80000],potions = [100000, 90000, 80000, 70000, 60000],success = 8100000000) == [2, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100000, 90000, 80000],potions = [100000, 90000, 80000, 70000, 60000],success = 8100000000) == [2, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 1, 1, 1, 1],potions = [100000, 100000, 100000, 100000, 100000],success = 50000) == [5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 1, 1, 1, 1],potions = [100000, 100000, 100000, 100000, 100000],success = 50000) == [5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 3, 5, 7, 9],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 15) == [3, 8, 9, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 3, 5, 7, 9],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 15) == [3, 8, 9, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],potions = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],success = 1000000) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],potions = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],success = 1000000) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],success = 1000) == [1, 11, 14, 16, 17, 17, 18, 18, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],success = 1000) == [1, 11, 14, 16, 17, 17, 18, 18, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100000, 1, 50000, 10000],potions = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],success = 10000000000) == [1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100000, 1, 50000, 10000],potions = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],success = 10000000000) == [1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 1, 1, 1, 1],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 10) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 1, 1, 1, 1],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 10) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],potions = [100000, 50000, 25000, 12500, 6250],success = 10000000000) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],potions = [100000, 50000, 25000, 12500, 6250],success = 10000000000) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [1, 10, 100, 1000, 10000, 100000],success = 9999500000) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [1, 10, 100, 1000, 10000, 100000],success = 9999500000) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [9, 8, 7, 6, 5, 4, 3, 2, 1],potions = [9, 8, 7, 6, 5, 4, 3, 2, 1],success = 36) == [6, 5, 4, 4, 2, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [9, 8, 7, 6, 5, 4, 3, 2, 1],potions = [9, 8, 7, 6, 5, 4, 3, 2, 1],success = 36) == [6, 5, 4, 4, 2, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],success = 9999800001) == [1, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],success = 9999800001) == [1, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [50, 25, 100, 1],potions = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],success = 1000) == [6, 5, 7, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [50, 25, 100, 1],potions = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],success = 1000) == [6, 5, 7, 1]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [10, 20, 30, 40, 50],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 150) == [3, 7, 8, 9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [10, 20, 30, 40, 50],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 150) == [3, 7, 8, 9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100000, 90000, 80000, 70000, 60000],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 54000000) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100000, 90000, 80000, 70000, 60000],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 54000000) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100000, 1, 99999],potions = [1, 100000, 99999, 50000, 25000],success = 9999999999) == [1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100000, 1, 99999],potions = [1, 100000, 99999, 50000, 25000],success = 9999999999) == [1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100000, 100000, 100000],potions = [100000, 100000, 100000, 100000, 100000],success = 10000000000) == [5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100000, 100000, 100000],potions = [100000, 100000, 100000, 100000, 100000],success = 10000000000) == [5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [5, 10, 15, 20, 25],potions = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],success = 800) == [0, 0, 3, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [5, 10, 15, 20, 25],potions = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],success = 800) == [0, 0, 3, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [50, 40, 30, 20, 10],potions = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],success = 200) == [10, 10, 9, 9, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [50, 40, 30, 20, 10],potions = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],success = 200) == [10, 10, 9, 9, 7]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 2, 3, 4, 5],potions = [100000, 200000, 300000, 400000, 500000],success = 500000) == [1, 3, 4, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 2, 3, 4, 5],potions = [100000, 200000, 300000, 400000, 500000],success = 500000) == [1, 3, 4, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100000, 50000, 25000],potions = [1, 10, 100, 1000, 10000, 100000],success = 10000000000) == [1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100000, 50000, 25000],potions = [1, 10, 100, 1000, 10000, 100000],success = 10000000000) == [1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100, 200, 300, 400, 500],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 1500) == [3, 7, 8, 9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100, 200, 300, 400, 500],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 1500) == [3, 7, 8, 9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [50, 50, 50, 50, 50],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],success = 250) == [16, 16, 16, 16, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [50, 50, 50, 50, 50],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],success = 250) == [16, 16, 16, 16, 16]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [99999, 99998, 99997],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 9999800000) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [99999, 99998, 99997],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 9999800000) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],potions = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],success = 1024) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],potions = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],success = 1024) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100000, 50000, 25000, 12500],potions = [1, 10, 100, 1000, 10000, 100000],success = 10000000000) == [1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100000, 50000, 25000, 12500],potions = [1, 10, 100, 1000, 10000, 100000],success = 10000000000) == [1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [100000, 50000, 25000],potions = [50000, 75000, 100000, 125000],success = 5000000000) == [4, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [100000, 50000, 25000],potions = [50000, 75000, 100000, 125000],success = 5000000000) == [4, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 50) == [0, 0, 0, 0, 1, 2, 3, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 50) == [0, 0, 0, 0, 1, 2, 3, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(spells = [10, 20, 30, 40, 50],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 50) == [6, 8, 9, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(spells = [10, 20, 30, 40, 50],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 50) == [6, 8, 9, 9, 10]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(spells = [3, 1, 2],potions = [8, 5, 8],success = 16) == [2, 0, 2]
    assert candidate(spells = [1, 1, 1],potions = [1, 1, 1],success = 2) == [0, 0, 0]
    assert candidate(spells = [5, 1, 3],potions = [1, 2, 3, 4, 5],success = 7) == [4, 0, 3]
    assert candidate(spells = [1, 2, 3, 4, 5],potions = [5, 4, 3, 2, 1],success = 10) == [0, 1, 2, 3, 4]
    assert candidate(spells = [10, 20, 30],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 50) == [6, 8, 9]
    assert candidate(spells = [100000, 100000, 100000],potions = [100000, 100000, 100000],success = 10000000000) == [3, 3, 3]
    assert candidate(spells = [10, 20, 30],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 100) == [1, 6, 7]
    assert candidate(spells = [1, 1, 1],potions = [1, 1, 1, 1],success = 1) == [4, 4, 4]
    assert candidate(spells = [10, 10, 10],potions = [1, 1, 1, 1, 1],success = 100) == [0, 0, 0]
    assert candidate(spells = [1, 1, 1, 1],potions = [1, 1, 1, 1],success = 1) == [4, 4, 4, 4]
    assert candidate(spells = [1, 2, 3, 4, 5],potions = [5, 4, 3, 2, 1],success = 6) == [0, 3, 4, 4, 4]
    assert candidate(spells = [10, 20, 30],potions = [5, 10, 15, 20],success = 100) == [3, 4, 4]
    assert candidate(spells = [100000],potions = [100000],success = 10000000000) == [1]
    assert candidate(spells = [100, 200, 300, 400, 500],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],success = 500) == [11, 13, 14, 14, 15]
    assert candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991],success = 4999750005) == [2, 2, 1, 1, 0]
    assert candidate(spells = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],potions = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],success = 100000) == [1, 6, 7, 8, 9, 9, 9, 9, 9, 10]
    assert candidate(spells = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 10000000000) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [100000, 99999, 99998, 99997, 99996, 99995],success = 9999900000) == [1, 0, 0, 0, 0]
    assert candidate(spells = [1, 1, 1, 1, 1],potions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],success = 2) == [0, 0, 0, 0, 0]
    assert candidate(spells = [1, 1, 1, 1, 1],potions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],success = 1) == [10, 10, 10, 10, 10]
    assert candidate(spells = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],potions = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],success = 50) == [6, 8, 9, 9, 10, 10, 10, 10, 10, 10]
    assert candidate(spells = [1, 10, 100, 1000, 10000],potions = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000],success = 10000) == [0, 1, 4, 7, 10]
    assert candidate(spells = [1, 3, 5, 7, 9],potions = [11, 13, 15, 17, 19, 21, 23, 25, 27, 29],success = 50) == [0, 7, 10, 10, 10]
    assert candidate(spells = [50000, 60000, 70000, 80000, 90000, 100000],potions = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],success = 5000000000) == [5, 5, 5, 5, 5, 5]
    assert candidate(spells = [2, 4, 6, 8, 10],potions = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],success = 100) == [1, 6, 7, 8, 9]
    assert candidate(spells = [100, 200, 300, 400, 500],potions = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],success = 5000) == [10, 16, 19, 20, 21]
    assert candidate(spells = [5, 10, 15, 20, 25],potions = [20, 25, 30, 35, 40, 45, 50, 55, 60],success = 500) == [0, 3, 6, 8, 9]
    assert candidate(spells = [1000, 2000, 3000, 4000, 5000],potions = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],success = 10000) == [9, 10, 10, 10, 10]
    assert candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [99999, 99998, 99997, 99996, 99995],success = 99990000025) == [0, 0, 0, 0, 0]
    assert candidate(spells = [5, 10, 15, 20, 25],potions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],success = 50) == [5, 8, 8, 9, 9]
    assert candidate(spells = [1, 2, 3, 4, 5],potions = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],success = 100000) == [0, 10, 10, 10, 10]
    assert candidate(spells = [9, 8, 7, 6, 5],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9],success = 20) == [7, 7, 7, 6, 6]
    assert candidate(spells = [33333, 66666, 99999],potions = [33333, 66666, 99999, 133332, 166665, 199998],success = 10000000000) == [0, 2, 3]
    assert candidate(spells = [100, 200, 300, 400, 500],potions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],success = 100) == [10, 10, 10, 10, 10]
    assert candidate(spells = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],potions = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],success = 250) == [1, 6, 7, 8, 9, 9, 9, 9, 9, 10]
    assert candidate(spells = [50000, 50000, 50000, 50000],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 100000) == [10, 10, 10, 10]
    assert candidate(spells = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],potions = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],success = 2500) == [0, 0, 2, 4, 6, 6, 7, 7, 8, 8]
    assert candidate(spells = [50000, 25000, 12500],potions = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],success = 625000000) == [9, 8, 6]
    assert candidate(spells = [100000, 50000, 25000, 12500, 6250],potions = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],success = 10000000000) == [4, 3, 2, 1, 0]
    assert candidate(spells = [1, 2, 3, 4, 5],potions = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],success = 25) == [6, 8, 9, 9, 10]
    assert candidate(spells = [1, 2, 3, 4, 5],potions = [100000, 200000, 300000, 400000, 500000],success = 1000000) == [0, 1, 2, 3, 4]
    assert candidate(spells = [100000, 90000, 80000],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 500000) == [6, 5, 4]
    assert candidate(spells = [1, 1, 1, 1, 1],potions = [100000, 100000, 100000, 100000, 100000],success = 100000) == [5, 5, 5, 5, 5]
    assert candidate(spells = [10000, 20000, 30000, 40000, 50000],potions = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000],success = 200000000) == [7, 9, 9, 10, 10]
    assert candidate(spells = [50000, 50000, 50000, 50000, 50000],potions = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],success = 5000000000) == [4, 4, 4, 4, 4]
    assert candidate(spells = [10000, 5000, 2500],potions = [5000, 10000, 15000, 20000, 25000],success = 100000000) == [4, 2, 0]
    assert candidate(spells = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],potions = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],success = 1000000) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert candidate(spells = [5, 15, 25, 35, 45],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 100) == [1, 7, 9, 9, 9]
    assert candidate(spells = [100000, 100000, 100000, 100000],potions = [100000, 100000, 100000, 100000, 100000],success = 10000000000) == [5, 5, 5, 5]
    assert candidate(spells = [5, 5, 5, 5, 5],potions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],success = 6) == [0, 0, 0, 0, 0]
    assert candidate(spells = [1, 3, 5, 7, 9],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 18) == [2, 8, 9, 9, 10]
    assert candidate(spells = [1, 1, 1, 1, 1],potions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],success = 1) == [21, 21, 21, 21, 21]
    assert candidate(spells = [3, 3, 3, 3, 3],potions = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],success = 10) == [0, 0, 0, 0, 0]
    assert candidate(spells = [1, 3, 5, 7, 9],potions = [9, 7, 5, 3, 1],success = 15) == [0, 3, 4, 4, 4]
    assert candidate(spells = [9, 7, 5, 3, 1],potions = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2],success = 50) == [8, 7, 6, 2, 0]
    assert candidate(spells = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 20) == [1, 7, 9, 9, 9, 10, 10, 10, 10, 10]
    assert candidate(spells = [10000, 20000, 30000, 40000],potions = [25000, 50000, 75000, 100000, 125000, 150000, 175000, 200000],success = 2000000000) == [1, 5, 6, 7]
    assert candidate(spells = [100000, 50000, 25000, 12500, 6250],potions = [200000, 100000, 50000, 25000, 12500, 6250],success = 10000000000) == [2, 1, 0, 0, 0]
    assert candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],success = 9999500000) == [0, 0, 0, 0, 0]
    assert candidate(spells = [50, 25, 10, 2],potions = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],success = 5000) == [4, 3, 2, 0]
    assert candidate(spells = [100000, 50000, 25000, 12500, 6250],potions = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],success = 5000000000) == [5, 4, 3, 2, 1]
    assert candidate(spells = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],potions = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],success = 10) == [1, 6, 7, 8, 9, 9, 9, 9, 9, 10]
    assert candidate(spells = [1000, 2000, 3000, 4000, 5000],potions = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],success = 5000000) == [0, 0, 0, 0, 10]
    assert candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],success = 9999500000) == [0, 0, 0, 0, 0]
    assert candidate(spells = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],potions = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],success = 100000) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert candidate(spells = [5, 5, 5, 5, 5],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 25) == [6, 6, 6, 6, 6]
    assert candidate(spells = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],potions = [100, 200, 300, 400, 500],success = 5000) == [0, 0, 0, 0, 1, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(spells = [100, 200, 300, 400, 500],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],success = 1000) == [11, 16, 17, 18, 19]
    assert candidate(spells = [100000, 90000, 80000],potions = [100000, 90000, 80000, 70000, 60000],success = 8100000000) == [2, 2, 0]
    assert candidate(spells = [1, 1, 1, 1, 1],potions = [100000, 100000, 100000, 100000, 100000],success = 50000) == [5, 5, 5, 5, 5]
    assert candidate(spells = [1, 3, 5, 7, 9],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 15) == [3, 8, 9, 9, 10]
    assert candidate(spells = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],potions = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],success = 1000000) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert candidate(spells = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],success = 1000) == [1, 11, 14, 16, 17, 17, 18, 18, 18, 19]
    assert candidate(spells = [100000, 1, 50000, 10000],potions = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],success = 10000000000) == [1, 0, 0, 0]
    assert candidate(spells = [1, 1, 1, 1, 1],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 10) == [1, 1, 1, 1, 1]
    assert candidate(spells = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],potions = [100000, 50000, 25000, 12500, 6250],success = 10000000000) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4]
    assert candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [1, 10, 100, 1000, 10000, 100000],success = 9999500000) == [1, 1, 1, 1, 1]
    assert candidate(spells = [9, 8, 7, 6, 5, 4, 3, 2, 1],potions = [9, 8, 7, 6, 5, 4, 3, 2, 1],success = 36) == [6, 5, 4, 4, 2, 1, 0, 0, 0]
    assert candidate(spells = [99999, 99998, 99997, 99996, 99995],potions = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],success = 9999800001) == [1, 0, 0, 0, 0]
    assert candidate(spells = [50, 25, 100, 1],potions = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],success = 1000) == [6, 5, 7, 1]
    assert candidate(spells = [10, 20, 30, 40, 50],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 150) == [3, 7, 8, 9, 9]
    assert candidate(spells = [100000, 90000, 80000, 70000, 60000],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 54000000) == [0, 0, 0, 0, 0]
    assert candidate(spells = [100000, 1, 99999],potions = [1, 100000, 99999, 50000, 25000],success = 9999999999) == [1, 0, 0]
    assert candidate(spells = [100000, 100000, 100000],potions = [100000, 100000, 100000, 100000, 100000],success = 10000000000) == [5, 5, 5]
    assert candidate(spells = [5, 10, 15, 20, 25],potions = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],success = 800) == [0, 0, 3, 6, 7]
    assert candidate(spells = [50, 40, 30, 20, 10],potions = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],success = 200) == [10, 10, 9, 9, 7]
    assert candidate(spells = [1, 2, 3, 4, 5],potions = [100000, 200000, 300000, 400000, 500000],success = 500000) == [1, 3, 4, 4, 5]
    assert candidate(spells = [100000, 50000, 25000],potions = [1, 10, 100, 1000, 10000, 100000],success = 10000000000) == [1, 0, 0]
    assert candidate(spells = [100, 200, 300, 400, 500],potions = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],success = 1500) == [3, 7, 8, 9, 9]
    assert candidate(spells = [50, 50, 50, 50, 50],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],success = 250) == [16, 16, 16, 16, 16]
    assert candidate(spells = [99999, 99998, 99997],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 9999800000) == [0, 0, 0]
    assert candidate(spells = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],potions = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],success = 1024) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(spells = [100000, 50000, 25000, 12500],potions = [1, 10, 100, 1000, 10000, 100000],success = 10000000000) == [1, 0, 0, 0]
    assert candidate(spells = [100000, 50000, 25000],potions = [50000, 75000, 100000, 125000],success = 5000000000) == [4, 2, 0]
    assert candidate(spells = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 50) == [0, 0, 0, 0, 1, 2, 3, 4, 5, 6]
    assert candidate(spells = [10, 20, 30, 40, 50],potions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],success = 50) == [6, 8, 9, 9, 10]


