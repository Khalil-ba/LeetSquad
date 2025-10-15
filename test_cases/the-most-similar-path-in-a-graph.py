def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 6,roads = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],names = ['ATL', 'PEK', 'LAX', 'ATL', 'DXB', 'HND'],targetPath = ['ATL', 'DXB', 'HND', 'DXB', 'ATL', 'LAX', 'PEK']) == [3, 4, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,roads = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],names = ['ATL', 'PEK', 'LAX', 'ATL', 'DXB', 'HND'],targetPath = ['ATL', 'DXB', 'HND', 'DXB', 'ATL', 'LAX', 'PEK']) == [3, 4, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,roads = [[0, 2], [0, 3], [1, 2], [1, 3], [1, 4], [2, 4]],names = ['ATL', 'PEK', 'LAX', 'DXB', 'HND'],targetPath = ['ATL', 'DXB', 'HND', 'LAX']) == [0, 3, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,roads = [[0, 2], [0, 3], [1, 2], [1, 3], [1, 4], [2, 4]],names = ['ATL', 'PEK', 'LAX', 'DXB', 'HND'],targetPath = ['ATL', 'DXB', 'HND', 'LAX']) == [0, 3, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,roads = [[1, 0], [2, 0], [3, 0], [2, 1], [3, 1], [3, 2]],names = ['ATL', 'PEK', 'LAX', 'DXB'],targetPath = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX']) == [1, 0, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,roads = [[1, 0], [2, 0], [3, 0], [2, 1], [3, 1], [3, 2]],names = ['ATL', 'PEK', 'LAX', 'DXB'],targetPath = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX']) == [1, 0, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,roads = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14], [11, 15], [12, 16], [13, 17], [14, 18], [15, 19], [16, 19], [17, 19], [18, 19]],names = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR', 'BOS', 'MIA', 'SFO', 'IAD', 'PHL', 'MDW', 'DFW', 'LAX'],targetPath = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR', 'BOS', 'MIA', 'SFO', 'IAD', 'PHL', 'MDW', 'DFW', 'LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR']) == [0, 1, 0, 1, 4, 1, 3, 7, 3, 1, 4, 8, 12, 16, 19, 15, 11, 7, 3, 1, 0, 2, 0, 2, 5, 2, 0, 2, 6, 10, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,roads = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14], [11, 15], [12, 16], [13, 17], [14, 18], [15, 19], [16, 19], [17, 19], [18, 19]],names = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR', 'BOS', 'MIA', 'SFO', 'IAD', 'PHL', 'MDW', 'DFW', 'LAX'],targetPath = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR', 'BOS', 'MIA', 'SFO', 'IAD', 'PHL', 'MDW', 'DFW', 'LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR']) == [0, 1, 0, 1, 4, 1, 3, 7, 3, 1, 4, 8, 12, 16, 19, 15, 11, 7, 3, 1, 0, 2, 0, 2, 5, 2, 0, 2, 6, 10, 6]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,roads = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14], [11, 12], [11, 13], [12, 14], [13, 14]],names = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR', 'BOS', 'MIA', 'SFO'],targetPath = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR', 'BOS', 'MIA', 'SFO', 'LAX', 'HOU', 'ATL', 'DFW', 'DEN']) == [0, 1, 0, 1, 4, 1, 0, 2, 5, 9, 13, 11, 7, 3, 1, 0, 1, 0, 1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,roads = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14], [11, 12], [11, 13], [12, 14], [13, 14]],names = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR', 'BOS', 'MIA', 'SFO'],targetPath = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR', 'BOS', 'MIA', 'SFO', 'LAX', 'HOU', 'ATL', 'DFW', 'DEN']) == [0, 1, 0, 1, 4, 1, 0, 2, 5, 9, 13, 11, 7, 3, 1, 0, 1, 0, 1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,roads = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],names = ['XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ'],targetPath = ['XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ']) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,roads = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],names = ['XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ'],targetPath = ['XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ']) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,roads = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 6], [4, 6], [5, 6]],names = ['LAX', 'ATL', 'DFW', 'DEN', 'PHX', 'ORD', 'JFK'],targetPath = ['LAX', 'ATL', 'DFW', 'DEN', 'PHX', 'ORD', 'JFK', 'LAX', 'ATL', 'DFW']) == [0, 1, 0, 3, 6, 5, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,roads = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 6], [4, 6], [5, 6]],names = ['LAX', 'ATL', 'DFW', 'DEN', 'PHX', 'ORD', 'JFK'],targetPath = ['LAX', 'ATL', 'DFW', 'DEN', 'PHX', 'ORD', 'JFK', 'LAX', 'ATL', 'DFW']) == [0, 1, 0, 3, 6, 5, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,roads = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0], [0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]],names = ['XYZ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZA', 'BCD', 'EFG'],targetPath = ['XYZ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZA', 'BCD', 'EFG', 'XYZ', 'ABC']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,roads = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0], [0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]],names = ['XYZ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZA', 'BCD', 'EFG'],targetPath = ['XYZ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZA', 'BCD', 'EFG', 'XYZ', 'ABC']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,roads = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 7], [6, 7]],names = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'JFK'],targetPath = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'JFK', 'JFK', 'JFK', 'JFK', 'JFK']) == [0, 1, 0, 1, 4, 7, 6, 7, 3, 7, 3, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,roads = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 7], [6, 7]],names = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'JFK'],targetPath = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'JFK', 'JFK', 'JFK', 'JFK', 'JFK']) == [0, 1, 0, 1, 4, 7, 6, 7, 3, 7, 3, 7]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,roads = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]],names = ['XYZ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU'],targetPath = ['XYZ', 'ABC', 'XYZ', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU']) == [0, 1, 0, 2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,roads = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]],names = ['XYZ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU'],targetPath = ['XYZ', 'ABC', 'XYZ', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU']) == [0, 1, 0, 2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,roads = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0], [0, 7], [1, 8], [2, 9], [3, 10], [4, 11], [5, 12], [6, 13], [7, 14]],names = ['XYZ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZA', 'BCD', 'EFG', 'HIJ', 'KLM', 'NOP'],targetPath = ['XYZ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZA', 'BCD', 'EFG', 'HIJ', 'KLM', 'NOP', 'XYZ', 'ABC', 'DEF', 'GHI', 'JKL']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,roads = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0], [0, 7], [1, 8], [2, 9], [3, 10], [4, 11], [5, 12], [6, 13], [7, 14]],names = ['XYZ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZA', 'BCD', 'EFG', 'HIJ', 'KLM', 'NOP'],targetPath = ['XYZ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZA', 'BCD', 'EFG', 'HIJ', 'KLM', 'NOP', 'XYZ', 'ABC', 'DEF', 'GHI', 'JKL']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,roads = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 11], [9, 11], [10, 11]],names = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR'],targetPath = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR', 'LAX', 'HOU', 'ATL']) == [0, 1, 0, 1, 4, 1, 3, 7, 11, 9, 5, 2, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,roads = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 11], [9, 11], [10, 11]],names = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR'],targetPath = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR', 'LAX', 'HOU', 'ATL']) == [0, 1, 0, 1, 4, 1, 3, 7, 11, 9, 5, 2, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,roads = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 7], [7, 8], [8, 9]],names = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK'],targetPath = ['ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'HOU', 'LAX']) == [0, 1, 4, 1, 3, 7, 8, 4, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,roads = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 7], [7, 8], [8, 9]],names = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK'],targetPath = ['ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'HOU', 'LAX']) == [0, 1, 4, 1, 3, 7, 8, 4, 1, 0]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 6,roads = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],names = ['ATL', 'PEK', 'LAX', 'ATL', 'DXB', 'HND'],targetPath = ['ATL', 'DXB', 'HND', 'DXB', 'ATL', 'LAX', 'PEK']) == [3, 4, 5, 4, 3, 2, 1]
    assert candidate(n = 5,roads = [[0, 2], [0, 3], [1, 2], [1, 3], [1, 4], [2, 4]],names = ['ATL', 'PEK', 'LAX', 'DXB', 'HND'],targetPath = ['ATL', 'DXB', 'HND', 'LAX']) == [0, 3, 0, 2]
    assert candidate(n = 4,roads = [[1, 0], [2, 0], [3, 0], [2, 1], [3, 1], [3, 2]],names = ['ATL', 'PEK', 'LAX', 'DXB'],targetPath = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX']) == [1, 0, 1, 0, 1, 0, 1, 0]
    assert candidate(n = 20,roads = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14], [11, 15], [12, 16], [13, 17], [14, 18], [15, 19], [16, 19], [17, 19], [18, 19]],names = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR', 'BOS', 'MIA', 'SFO', 'IAD', 'PHL', 'MDW', 'DFW', 'LAX'],targetPath = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR', 'BOS', 'MIA', 'SFO', 'IAD', 'PHL', 'MDW', 'DFW', 'LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR']) == [0, 1, 0, 1, 4, 1, 3, 7, 3, 1, 4, 8, 12, 16, 19, 15, 11, 7, 3, 1, 0, 2, 0, 2, 5, 2, 0, 2, 6, 10, 6]
    assert candidate(n = 15,roads = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14], [11, 12], [11, 13], [12, 14], [13, 14]],names = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR', 'BOS', 'MIA', 'SFO'],targetPath = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR', 'BOS', 'MIA', 'SFO', 'LAX', 'HOU', 'ATL', 'DFW', 'DEN']) == [0, 1, 0, 1, 4, 1, 0, 2, 5, 9, 13, 11, 7, 3, 1, 0, 1, 0, 1, 4]
    assert candidate(n = 10,roads = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],names = ['XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ'],targetPath = ['XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ', 'XYZ']) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert candidate(n = 7,roads = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 6], [4, 6], [5, 6]],names = ['LAX', 'ATL', 'DFW', 'DEN', 'PHX', 'ORD', 'JFK'],targetPath = ['LAX', 'ATL', 'DFW', 'DEN', 'PHX', 'ORD', 'JFK', 'LAX', 'ATL', 'DFW']) == [0, 1, 0, 3, 6, 5, 1, 0, 1, 0]
    assert candidate(n = 12,roads = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0], [0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]],names = ['XYZ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZA', 'BCD', 'EFG'],targetPath = ['XYZ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZA', 'BCD', 'EFG', 'XYZ', 'ABC']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1]
    assert candidate(n = 8,roads = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 7], [6, 7]],names = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'JFK'],targetPath = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'JFK', 'JFK', 'JFK', 'JFK', 'JFK']) == [0, 1, 0, 1, 4, 7, 6, 7, 3, 7, 3, 7]
    assert candidate(n = 8,roads = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]],names = ['XYZ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU'],targetPath = ['XYZ', 'ABC', 'XYZ', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU']) == [0, 1, 0, 2, 3, 4, 5, 6, 7]
    assert candidate(n = 15,roads = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0], [0, 7], [1, 8], [2, 9], [3, 10], [4, 11], [5, 12], [6, 13], [7, 14]],names = ['XYZ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZA', 'BCD', 'EFG', 'HIJ', 'KLM', 'NOP'],targetPath = ['XYZ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZA', 'BCD', 'EFG', 'HIJ', 'KLM', 'NOP', 'XYZ', 'ABC', 'DEF', 'GHI', 'JKL']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1, 2, 3, 4]
    assert candidate(n = 12,roads = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 11], [9, 11], [10, 11]],names = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR'],targetPath = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'PDX', 'EWR', 'LAX', 'HOU', 'ATL']) == [0, 1, 0, 1, 4, 1, 3, 7, 11, 9, 5, 2, 0, 1, 0]
    assert candidate(n = 10,roads = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 7], [7, 8], [8, 9]],names = ['LAX', 'HOU', 'ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK'],targetPath = ['ATL', 'DFW', 'DEN', 'PHX', 'SEA', 'ORD', 'SLC', 'JFK', 'HOU', 'LAX']) == [0, 1, 4, 1, 3, 7, 8, 4, 1, 0]


