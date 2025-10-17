def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(security = [3, 3, 5, 5, 5, 5, 2, 2, 2, 3],time = 2) == [6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [3, 3, 5, 5, 5, 5, 2, 2, 2, 3],time = 2) == [6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 1, 1, 1, 1],time = 0) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 1, 1, 1, 1],time = 0) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 2, 3, 3, 4, 5, 5, 6, 6],time = 1) == [2, 4, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 2, 3, 3, 4, 5, 5, 6, 6],time = 1) == [2, 4, 7]: {e}')
    
    total += 1
    try:
        result = candidate(security = [6, 5, 4, 3, 2, 1],time = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [6, 5, 4, 3, 2, 1],time = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],time = 1) == [2, 4, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],time = 1) == [2, 4, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],time = 0) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],time = 0) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 2, 3, 3, 4],time = 1) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 2, 3, 3, 4],time = 1) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],time = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],time = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 2, 3, 3, 4, 5],time = 1) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 2, 3, 3, 4, 5],time = 1) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(security = [3, 3, 5, 5, 5, 5, 2, 2, 1, 1],time = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [3, 3, 5, 5, 5, 5, 2, 2, 1, 1],time = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 1, 1, 2, 2, 2, 3, 3, 3],time = 2) == [2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 1, 1, 2, 2, 2, 3, 3, 3],time = 2) == [2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(security = [100, 90, 80, 70, 60, 50, 60, 70, 80, 90, 100],time = 4) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [100, 90, 80, 70, 60, 50, 60, 70, 80, 90, 100],time = 4) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(security = [3, 3, 3, 3, 3, 3, 3],time = 3) == [3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [3, 3, 3, 3, 3, 3, 3],time = 3) == [3]: {e}')
    
    total += 1
    try:
        result = candidate(security = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],time = 4) == [4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],time = 4) == [4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1],time = 0) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1],time = 0) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],time = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],time = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [3, 3, 5, 5, 5, 5, 4, 4, 4, 3],time = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [3, 3, 5, 5, 5, 5, 4, 4, 4, 3],time = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 4, 5, 6],time = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 4, 5, 6],time = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 3, 3, 3, 2, 2, 1],time = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 3, 3, 3, 2, 2, 1],time = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 3, 3, 3, 5, 6, 2],time = 2) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 3, 3, 3, 5, 6, 2],time = 2) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 2, 1, 0, 1, 0, 1, 2, 3],time = 1) == [5, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 2, 1, 0, 1, 0, 1, 2, 3],time = 1) == [5, 7]: {e}')
    
    total += 1
    try:
        result = candidate(security = [6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6],time = 2) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6],time = 2) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 2, 3, 4, 5, 5, 4, 3, 2, 1],time = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 2, 3, 4, 5, 5, 4, 3, 2, 1],time = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [6, 5, 4, 3, 2, 1],time = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [6, 5, 4, 3, 2, 1],time = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],time = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],time = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2],time = 1) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2],time = 1) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [2, 1],time = 1) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [2, 1],time = 1) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 3, 3, 3, 3, 2, 2, 2, 2],time = 2) == [5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 3, 3, 3, 3, 2, 2, 2, 2],time = 2) == [5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],time = 5) == [23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],time = 5) == [23]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],time = 2) == [2, 6, 10, 14, 18, 22, 26]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],time = 2) == [2, 6, 10, 14, 18, 22, 26]: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],time = 10) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],time = 10) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7],time = 2) == [8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7],time = 2) == [8]: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],time = 10) == [10, 11, 12, 13, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],time = 10) == [10, 11, 12, 13, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],time = 5) == [10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],time = 5) == [10]: {e}')
    
    total += 1
    try:
        result = candidate(security = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],time = 0) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],time = 0) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],time = 3) == [11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],time = 3) == [11]: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 3, 3, 3, 3, 5, 6, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],time = 3) == [3, 11, 12, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 3, 3, 3, 3, 5, 6, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],time = 3) == [3, 11, 12, 13]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1],time = 2) == [3, 6, 9, 13, 16, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1],time = 2) == [3, 6, 9, 13, 16, 19]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5],time = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5],time = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],time = 10) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],time = 10) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12],time = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12],time = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 2, 1, 0, 1, 0, 1, 2, 3, 2, 1, 0, 1],time = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 2, 1, 0, 1, 0, 1, 2, 3, 2, 1, 0, 1],time = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5],time = 2) == [8, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5],time = 2) == [8, 16]: {e}')
    
    total += 1
    try:
        result = candidate(security = [7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7],time = 3) == [4, 8, 9, 10, 11, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7],time = 3) == [4, 8, 9, 10, 11, 15]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2],time = 1) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2],time = 1) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6],time = 3) == [11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6],time = 3) == [11]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 3, 2, 2, 2, 1, 2, 2, 2, 3, 1, 1, 1],time = 1) == [2, 3, 5, 7, 8, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 3, 2, 2, 2, 1, 2, 2, 2, 3, 1, 1, 1],time = 1) == [2, 3, 5, 7, 8, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],time = 4) == [8, 9, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],time = 4) == [8, 9, 17]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],time = 2) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],time = 2) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2],time = 2) == [4, 8, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2],time = 2) == [4, 8, 12]: {e}')
    
    total += 1
    try:
        result = candidate(security = [10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],time = 4) == [12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],time = 4) == [12]: {e}')
    
    total += 1
    try:
        result = candidate(security = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],time = 4) == [4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],time = 4) == [4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(security = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],time = 5) == [10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],time = 5) == [10]: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4],time = 5) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4],time = 5) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],time = 6) == [10, 11, 12, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],time = 6) == [10, 11, 12, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 3, 3, 3, 5, 6, 2, 2, 2, 1, 1, 1, 2, 2, 2],time = 3) == [9, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 3, 3, 3, 5, 6, 2, 2, 2, 1, 1, 1, 2, 2, 2],time = 3) == [9, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 2, 1, 0, 0, 1, 1, 2, 2],time = 1) == [4, 5, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 2, 1, 0, 0, 1, 1, 2, 2],time = 1) == [4, 5, 7]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],time = 4) == [19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],time = 4) == [19]: {e}')
    
    total += 1
    try:
        result = candidate(security = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],time = 4) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],time = 4) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 3, 3, 3, 5, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],time = 2) == [2, 3, 7, 8, 9, 10, 11, 12, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 3, 3, 3, 5, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],time = 2) == [2, 3, 7, 8, 9, 10, 11, 12, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(security = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],time = 5) == [5, 6, 7, 8, 9, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],time = 5) == [5, 6, 7, 8, 9, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],time = 5) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],time = 5) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0],time = 4) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0],time = 4) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [2, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 2, 1, 1, 2, 2],time = 2) == [5, 6, 12, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [2, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 2, 1, 1, 2, 2],time = 2) == [5, 6, 12, 13]: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],time = 3) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],time = 3) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],time = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],time = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],time = 4) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],time = 4) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 2, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 9, 8, 9, 10, 11, 10, 11, 12, 11, 12, 13],time = 4) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 2, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 9, 8, 9, 10, 11, 10, 11, 12, 11, 12, 13],time = 4) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],time = 2) == [2, 5, 6, 7, 8, 9, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],time = 2) == [2, 5, 6, 7, 8, 9, 12]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5],time = 3) == [8, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5],time = 3) == [8, 16]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],time = 1) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],time = 1) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]: {e}')
    
    total += 1
    try:
        result = candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],time = 3) == [10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],time = 3) == [10]: {e}')
    
    total += 1
    try:
        result = candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],time = 4) == [10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],time = 4) == [10]: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5],time = 4) == [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5],time = 4) == [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5],time = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5],time = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6],time = 8) == [10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6],time = 8) == [10]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],time = 7) == [7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],time = 7) == [7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],time = 4) == [10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],time = 4) == [10]: {e}')
    
    total += 1
    try:
        result = candidate(security = [3, 2, 1, 2, 1, 0, 1, 0, 1, 2, 3, 2, 1, 2, 1, 0, 1, 0, 1, 2],time = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [3, 2, 1, 2, 1, 0, 1, 0, 1, 2, 3, 2, 1, 2, 1, 0, 1, 0, 1, 2],time = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6],time = 3) == [11, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6],time = 3) == [11, 23]: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],time = 3) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],time = 3) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 1],time = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 1],time = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],time = 5) == [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],time = 5) == [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10],time = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10],time = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],time = 5) == [10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],time = 5) == [10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(security = [9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1],time = 4) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1],time = 4) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1],time = 2) == [4, 5, 8, 9, 12, 13, 16, 17, 20, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1],time = 2) == [4, 5, 8, 9, 12, 13, 16, 17, 20, 21]: {e}')
    
    total += 1
    try:
        result = candidate(security = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5],time = 2) == [2, 5, 6, 7, 8, 9, 12, 13, 14, 17, 18, 19, 22, 23, 24, 27]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5],time = 2) == [2, 5, 6, 7, 8, 9, 12, 13, 14, 17, 18, 19, 22, 23, 24, 27]: {e}')
    
    total += 1
    try:
        result = candidate(security = [3, 3, 5, 5, 4, 4, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],time = 3) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [3, 3, 5, 5, 4, 4, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],time = 3) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(security = [3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0],time = 3) == [4, 8, 12, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0],time = 3) == [4, 8, 12, 13]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2],time = 2) == [4, 5, 6, 10, 11, 12, 16, 17, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2],time = 2) == [4, 5, 6, 10, 11, 12, 16, 17, 18]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11],time = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11],time = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],time = 4) == [5, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],time = 4) == [5, 20]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],time = 7) == [19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],time = 7) == [19]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 2, 1, 2, 1, 2, 3, 4, 3, 2, 1, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],time = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 2, 1, 2, 1, 2, 3, 4, 3, 2, 1, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],time = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],time = 3) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],time = 3) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 3, 2, 3, 1, 2, 3, 2, 1, 2, 1, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 1, 2, 3, 2, 1, 2, 1, 3, 2, 1],time = 2) == [13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 3, 2, 3, 1, 2, 3, 2, 1, 2, 1, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 1, 2, 3, 2, 1, 2, 1, 3, 2, 1],time = 2) == [13]: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],time = 5) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],time = 5) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(security = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],time = 2) == [2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],time = 2) == [2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(security = [10, 9, 8, 7, 6, 5, 5, 5, 6, 7, 8, 9, 10],time = 3) == [5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [10, 9, 8, 7, 6, 5, 5, 5, 6, 7, 8, 9, 10],time = 3) == [5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],time = 5) == [5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],time = 5) == [5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(security = [8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8],time = 2) == [2, 5, 6, 7, 8, 9, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8],time = 2) == [2, 5, 6, 7, 8, 9, 12]: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],time = 10) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],time = 10) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 3, 2, 3, 2, 1, 2, 3, 2, 1],time = 1) == [2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 3, 2, 3, 2, 1, 2, 3, 2, 1],time = 1) == [2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],time = 5) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],time = 5) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 5, 4, 5, 6, 7, 8, 9],time = 2) == [5, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 5, 4, 5, 6, 7, 8, 9],time = 2) == [5, 11]: {e}')
    
    total += 1
    try:
        result = candidate(security = [8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],time = 6) == [7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],time = 6) == [7]: {e}')
    
    total += 1
    try:
        result = candidate(security = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],time = 12) == [12, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],time = 12) == [12, 13]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],time = 7) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],time = 7) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],time = 2) == [3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],time = 2) == [3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(security = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10],time = 2) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10],time = 2) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 5, 4, 4, 4, 5, 6, 7, 8, 8],time = 2) == [2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 5, 4, 4, 4, 5, 6, 7, 8, 8],time = 2) == [2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],time = 2) == [10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],time = 2) == [10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(security = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],time = 3) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],time = 3) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1],time = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1],time = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],time = 5) == [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],time = 5) == [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]: {e}')
    
    total += 1
    try:
        result = candidate(security = [3, 3, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 3, 3, 2, 2, 1, 1, 1],time = 3) == [11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [3, 3, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 3, 3, 2, 2, 1, 1, 1],time = 3) == [11]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3],time = 2) == [4, 8, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3],time = 2) == [4, 8, 12]: {e}')
    
    total += 1
    try:
        result = candidate(security = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],time = 5) == [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],time = 5) == [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],time = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],time = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],time = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],time = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],time = 5) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],time = 5) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]: {e}')
    
    total += 1
    try:
        result = candidate(security = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1],time = 1) == [1, 4, 5, 8, 9, 12, 13, 16, 17, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(security = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1],time = 1) == [1, 4, 5, 8, 9, 12, 13, 16, 17, 20]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(security = [3, 3, 5, 5, 5, 5, 2, 2, 2, 3],time = 2) == [6, 7]
    assert candidate(security = [1, 1, 1, 1, 1],time = 0) == [0, 1, 2, 3, 4]
    assert candidate(security = [1, 2, 2, 3, 3, 4, 5, 5, 6, 6],time = 1) == [2, 4, 7]
    assert candidate(security = [6, 5, 4, 3, 2, 1],time = 2) == []
    assert candidate(security = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],time = 1) == [2, 4, 6, 8]
    assert candidate(security = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],time = 0) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(security = [1, 2, 2, 3, 3, 4],time = 1) == [2, 4]
    assert candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],time = 3) == []
    assert candidate(security = [1, 2, 2, 3, 3, 4, 5],time = 1) == [2, 4]
    assert candidate(security = [3, 3, 5, 5, 5, 5, 2, 2, 1, 1],time = 2) == []
    assert candidate(security = [1, 1, 1, 2, 2, 2, 3, 3, 3],time = 2) == [2, 5]
    assert candidate(security = [100, 90, 80, 70, 60, 50, 60, 70, 80, 90, 100],time = 4) == [5]
    assert candidate(security = [3, 3, 3, 3, 3, 3, 3],time = 3) == [3]
    assert candidate(security = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],time = 4) == [4, 5]
    assert candidate(security = [1],time = 0) == [0]
    assert candidate(security = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],time = 2) == []
    assert candidate(security = [3, 3, 5, 5, 5, 5, 4, 4, 4, 3],time = 3) == []
    assert candidate(security = [1, 2, 3, 4, 5, 6],time = 2) == []
    assert candidate(security = [1, 2, 3, 3, 3, 3, 2, 2, 1],time = 2) == []
    assert candidate(security = [5, 3, 3, 3, 5, 6, 2],time = 2) == [2, 3]
    assert candidate(security = [1, 2, 3, 2, 1, 0, 1, 0, 1, 2, 3],time = 1) == [5, 7]
    assert candidate(security = [6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6],time = 2) == [5]
    assert candidate(security = [1, 2, 2, 3, 4, 5, 5, 4, 3, 2, 1],time = 3) == []
    assert candidate(security = [6, 5, 4, 3, 2, 1],time = 3) == []
    assert candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],time = 3) == []
    assert candidate(security = [1, 2],time = 1) == []
    assert candidate(security = [2, 1],time = 1) == []
    assert candidate(security = [1, 3, 3, 3, 3, 2, 2, 2, 2],time = 2) == [5, 6]
    assert candidate(security = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],time = 5) == [23]
    assert candidate(security = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],time = 2) == [2, 6, 10, 14, 18, 22, 26]
    assert candidate(security = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],time = 10) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert candidate(security = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7],time = 2) == [8]
    assert candidate(security = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],time = 10) == [10, 11, 12, 13, 14, 15]
    assert candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],time = 5) == [10]
    assert candidate(security = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],time = 0) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    assert candidate(security = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],time = 3) == [11]
    assert candidate(security = [5, 3, 3, 3, 3, 5, 6, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],time = 3) == [3, 11, 12, 13]
    assert candidate(security = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1],time = 2) == [3, 6, 9, 13, 16, 19]
    assert candidate(security = [1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5],time = 2) == []
    assert candidate(security = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],time = 10) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert candidate(security = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12],time = 2) == []
    assert candidate(security = [1, 2, 3, 2, 1, 0, 1, 0, 1, 2, 3, 2, 1, 0, 1],time = 2) == []
    assert candidate(security = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5],time = 2) == [8, 16]
    assert candidate(security = [7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7],time = 3) == [4, 8, 9, 10, 11, 15]
    assert candidate(security = [1, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2],time = 1) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
    assert candidate(security = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6],time = 3) == [11]
    assert candidate(security = [1, 3, 2, 2, 2, 1, 2, 2, 2, 3, 1, 1, 1],time = 1) == [2, 3, 5, 7, 8, 10, 11]
    assert candidate(security = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],time = 4) == [8, 9, 17]
    assert candidate(security = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],time = 2) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    assert candidate(security = [1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2],time = 2) == [4, 8, 12]
    assert candidate(security = [10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],time = 4) == [12]
    assert candidate(security = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],time = 4) == [4, 5]
    assert candidate(security = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],time = 5) == [10]
    assert candidate(security = [5, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4],time = 5) == []
    assert candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],time = 6) == [10, 11, 12, 13, 14]
    assert candidate(security = [5, 3, 3, 3, 5, 6, 2, 2, 2, 1, 1, 1, 2, 2, 2],time = 3) == [9, 10, 11]
    assert candidate(security = [1, 2, 2, 1, 0, 0, 1, 1, 2, 2],time = 1) == [4, 5, 7]
    assert candidate(security = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],time = 4) == [19]
    assert candidate(security = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],time = 4) == [9]
    assert candidate(security = [5, 3, 3, 3, 5, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],time = 2) == [2, 3, 7, 8, 9, 10, 11, 12, 13, 14]
    assert candidate(security = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],time = 5) == [5, 6, 7, 8, 9, 10, 11]
    assert candidate(security = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],time = 5) == []
    assert candidate(security = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0],time = 4) == []
    assert candidate(security = [2, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 2, 1, 1, 2, 2],time = 2) == [5, 6, 12, 13]
    assert candidate(security = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],time = 3) == [4]
    assert candidate(security = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],time = 2) == []
    assert candidate(security = [10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],time = 4) == []
    assert candidate(security = [1, 2, 3, 2, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 9, 8, 9, 10, 11, 10, 11, 12, 11, 12, 13],time = 4) == []
    assert candidate(security = [3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],time = 2) == [2, 5, 6, 7, 8, 9, 12]
    assert candidate(security = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5],time = 3) == [8, 16]
    assert candidate(security = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],time = 1) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    assert candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],time = 3) == [10]
    assert candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],time = 4) == [10]
    assert candidate(security = [5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5],time = 4) == [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    assert candidate(security = [1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5],time = 2) == []
    assert candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6],time = 8) == [10]
    assert candidate(security = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],time = 7) == [7, 8, 9]
    assert candidate(security = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],time = 4) == [10]
    assert candidate(security = [3, 2, 1, 2, 1, 0, 1, 0, 1, 2, 3, 2, 1, 2, 1, 0, 1, 0, 1, 2],time = 2) == []
    assert candidate(security = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6],time = 3) == [11, 23]
    assert candidate(security = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],time = 3) == [5]
    assert candidate(security = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 1],time = 3) == []
    assert candidate(security = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],time = 5) == [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert candidate(security = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10],time = 3) == []
    assert candidate(security = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],time = 5) == [10, 11]
    assert candidate(security = [9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1],time = 4) == [4]
    assert candidate(security = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1],time = 2) == [4, 5, 8, 9, 12, 13, 16, 17, 20, 21]
    assert candidate(security = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5],time = 2) == [2, 5, 6, 7, 8, 9, 12, 13, 14, 17, 18, 19, 22, 23, 24, 27]
    assert candidate(security = [3, 3, 5, 5, 4, 4, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],time = 3) == [5]
    assert candidate(security = [3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0],time = 3) == [4, 8, 12, 13]
    assert candidate(security = [1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2],time = 2) == [4, 5, 6, 10, 11, 12, 16, 17, 18]
    assert candidate(security = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11],time = 3) == []
    assert candidate(security = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],time = 4) == [5, 20]
    assert candidate(security = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],time = 7) == [19]
    assert candidate(security = [1, 2, 3, 2, 1, 2, 1, 2, 3, 4, 3, 2, 1, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],time = 3) == []
    assert candidate(security = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],time = 3) == [5]
    assert candidate(security = [1, 3, 2, 3, 1, 2, 3, 2, 1, 2, 1, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 1, 2, 3, 2, 1, 2, 1, 3, 2, 1],time = 2) == [13]
    assert candidate(security = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],time = 5) == [5]
    assert candidate(security = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],time = 2) == [2, 3, 4, 5, 6, 7]
    assert candidate(security = [10, 9, 8, 7, 6, 5, 5, 5, 6, 7, 8, 9, 10],time = 3) == [5, 6, 7]
    assert candidate(security = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],time = 5) == [5, 6, 7, 8, 9, 10]
    assert candidate(security = [8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8],time = 2) == [2, 5, 6, 7, 8, 9, 12]
    assert candidate(security = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],time = 10) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
    assert candidate(security = [1, 3, 2, 3, 2, 1, 2, 3, 2, 1],time = 1) == [2, 5]
    assert candidate(security = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],time = 5) == []
    assert candidate(security = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 5, 4, 5, 6, 7, 8, 9],time = 2) == [5, 11]
    assert candidate(security = [8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],time = 6) == [7]
    assert candidate(security = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],time = 12) == [12, 13]
    assert candidate(security = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],time = 7) == []
    assert candidate(security = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],time = 2) == [3, 4, 5, 6, 7, 8, 9]
    assert candidate(security = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10],time = 2) == [5]
    assert candidate(security = [5, 5, 4, 4, 4, 5, 6, 7, 8, 8],time = 2) == [2, 3, 4]
    assert candidate(security = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],time = 2) == [10, 11]
    assert candidate(security = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],time = 3) == [4]
    assert candidate(security = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1],time = 3) == []
    assert candidate(security = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],time = 5) == [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
    assert candidate(security = [3, 3, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 3, 3, 2, 2, 1, 1, 1],time = 3) == [11]
    assert candidate(security = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3],time = 2) == [4, 8, 12]
    assert candidate(security = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],time = 5) == [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    assert candidate(security = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],time = 2) == []
    assert candidate(security = [1, 3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],time = 2) == []
    assert candidate(security = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],time = 5) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert candidate(security = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1],time = 1) == [1, 4, 5, 8, 9, 12, 13, 16, 17, 20]


