def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(ranks = [7, 7, 7, 7, 7],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [7, 7, 7, 7, 7],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [7, 7, 7, 8, 9],suits = ['a', 'b', 'c', 'a', 'd']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [7, 7, 7, 8, 9],suits = ['a', 'b', 'c', 'a', 'd']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [10, 10, 2, 12, 9],suits = ['a', 'b', 'c', 'a', 'd']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [10, 10, 2, 12, 9],suits = ['a', 'b', 'c', 'a', 'd']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [7, 7, 7, 7, 7],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [7, 7, 7, 7, 7],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 1, 2, 2, 3],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 1, 2, 2, 3],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'b', 'c', 'd', 'a']) == "High Card"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'b', 'c', 'd', 'a']) == "High Card": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [13, 2, 3, 1, 9],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [13, 2, 3, 1, 9],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [2, 3, 4, 5, 6],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [2, 3, 4, 5, 6],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [11, 11, 12, 12, 13],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [11, 11, 12, 12, 13],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [4, 4, 2, 4, 4],suits = ['d', 'a', 'a', 'b', 'c']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [4, 4, 2, 4, 4],suits = ['d', 'a', 'a', 'b', 'c']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [10, 10, 11, 11, 12],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [10, 10, 11, 11, 12],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [6, 6, 6, 7, 7],suits = ['d', 'd', 'd', 'c', 'c']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [6, 6, 6, 7, 7],suits = ['d', 'd', 'd', 'c', 'c']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [3, 3, 4, 4, 5],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [3, 3, 4, 4, 5],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [8, 8, 8, 9, 10],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [8, 8, 8, 9, 10],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [5, 6, 7, 8, 9],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [5, 6, 7, 8, 9],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [7, 7, 8, 8, 9],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [7, 7, 8, 8, 9],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [5, 5, 5, 3, 3],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [5, 5, 5, 3, 3],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [11, 12, 13, 13, 13],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [11, 12, 13, 13, 13],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [5, 5, 6, 6, 7],suits = ['a', 'b', 'a', 'b', 'a']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [5, 5, 6, 6, 7],suits = ['a', 'b', 'a', 'b', 'a']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [6, 6, 7, 7, 8],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [6, 6, 7, 7, 8],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 2, 3, 3, 3],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 2, 3, 3, 3],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [4, 4, 5, 5, 6],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [4, 4, 5, 5, 6],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [9, 9, 9, 9, 9],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [9, 9, 9, 9, 9],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 2, 3, 4, 4],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 2, 3, 4, 4],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [8, 8, 9, 9, 10],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [8, 8, 9, 9, 10],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [10, 11, 12, 13, 13],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [10, 11, 12, 13, 13],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [5, 5, 5, 6, 7],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [5, 5, 5, 6, 7],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [6, 6, 6, 7, 8],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [6, 6, 6, 7, 8],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [10, 10, 10, 12, 13],suits = ['a', 'b', 'c', 'a', 'b']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [10, 10, 10, 12, 13],suits = ['a', 'b', 'c', 'a', 'b']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [8, 8, 9, 9, 10],suits = ['a', 'a', 'b', 'b', 'c']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [8, 8, 9, 9, 10],suits = ['a', 'a', 'b', 'b', 'c']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [3, 3, 3, 8, 8],suits = ['a', 'b', 'c', 'a', 'b']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [3, 3, 3, 8, 8],suits = ['a', 'b', 'c', 'a', 'b']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 3, 3, 3, 5],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 3, 3, 3, 5],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [13, 13, 13, 13, 1],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [13, 13, 13, 13, 1],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [6, 6, 6, 7, 8],suits = ['a', 'a', 'a', 'b', 'c']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [6, 6, 6, 7, 8],suits = ['a', 'a', 'a', 'b', 'c']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 1, 2, 3, 4],suits = ['a', 'a', 'b', 'c', 'd']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 1, 2, 3, 4],suits = ['a', 'a', 'b', 'c', 'd']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [13, 13, 13, 13, 13],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [13, 13, 13, 13, 13],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [12, 12, 12, 12, 13],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [12, 12, 12, 12, 13],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [9, 9, 10, 11, 12],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [9, 9, 10, 11, 12],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [8, 8, 10, 10, 10],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [8, 8, 10, 10, 10],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [3, 3, 3, 4, 4],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [3, 3, 3, 4, 4],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [6, 6, 6, 6, 6],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [6, 6, 6, 6, 6],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [8, 8, 8, 9, 9],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [8, 8, 8, 9, 9],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [5, 5, 5, 5, 10],suits = ['a', 'a', 'a', 'a', 'b']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [5, 5, 5, 5, 10],suits = ['a', 'a', 'a', 'a', 'b']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 1, 2, 2, 3],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 1, 2, 2, 3],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [7, 8, 9, 10, 11],suits = ['a', 'b', 'c', 'd', 'a']) == "High Card"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [7, 8, 9, 10, 11],suits = ['a', 'b', 'c', 'd', 'a']) == "High Card": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [13, 12, 11, 10, 9],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [13, 12, 11, 10, 9],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [5, 5, 5, 6, 7],suits = ['a', 'b', 'c', 'a', 'a']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [5, 5, 5, 6, 7],suits = ['a', 'b', 'c', 'a', 'a']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'b', 'c', 'd', 'e']) == "High Card"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'b', 'c', 'd', 'e']) == "High Card": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [2, 2, 3, 3, 4],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [2, 2, 3, 3, 4],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'b', 'c', 'd', 'e']) == "High Card"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'b', 'c', 'd', 'e']) == "High Card": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [6, 6, 6, 7, 8],suits = ['b', 'b', 'b', 'c', 'd']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [6, 6, 6, 7, 8],suits = ['b', 'b', 'b', 'c', 'd']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [8, 8, 8, 9, 9],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [8, 8, 8, 9, 9],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [2, 2, 3, 4, 4],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [2, 2, 3, 4, 4],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [2, 3, 5, 5, 5],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [2, 3, 5, 5, 5],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'a', 'b', 'b', 'c']) == "High Card"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'a', 'b', 'b', 'c']) == "High Card": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [3, 3, 3, 3, 5],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [3, 3, 3, 3, 5],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [6, 6, 7, 7, 8],suits = ['a', 'a', 'b', 'b', 'c']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [6, 6, 7, 7, 8],suits = ['a', 'a', 'b', 'b', 'c']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [2, 2, 2, 2, 2],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [2, 2, 2, 2, 2],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [9, 9, 9, 10, 10],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [9, 9, 9, 10, 10],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [13, 13, 2, 3, 4],suits = ['a', 'b', 'a', 'b', 'a']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [13, 13, 2, 3, 4],suits = ['a', 'b', 'a', 'b', 'a']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [6, 6, 6, 6, 7],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [6, 6, 6, 6, 7],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [11, 11, 12, 12, 13],suits = ['a', 'a', 'b', 'b', 'c']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [11, 11, 12, 12, 13],suits = ['a', 'a', 'b', 'b', 'c']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [10, 10, 11, 11, 12],suits = ['a', 'b', 'a', 'b', 'a']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [10, 10, 11, 11, 12],suits = ['a', 'b', 'a', 'b', 'a']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [5, 6, 7, 8, 9],suits = ['a', 'b', 'c', 'd', 'a']) == "High Card"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [5, 6, 7, 8, 9],suits = ['a', 'b', 'c', 'd', 'a']) == "High Card": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 1, 1, 2, 3],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 1, 1, 2, 3],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [8, 8, 8, 8, 2],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [8, 8, 8, 8, 2],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [13, 12, 11, 10, 9],suits = ['a', 'b', 'c', 'd', 'e']) == "High Card"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [13, 12, 11, 10, 9],suits = ['a', 'b', 'c', 'd', 'e']) == "High Card": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 1, 2, 3, 4],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 1, 2, 3, 4],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 1, 2, 3, 4],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 1, 2, 3, 4],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [2, 3, 4, 5, 6],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [2, 3, 4, 5, 6],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [2, 2, 2, 3, 3],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [2, 2, 2, 3, 3],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 2, 2, 3, 4],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 2, 2, 3, 4],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [13, 13, 13, 12, 12],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [13, 13, 13, 12, 12],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [5, 5, 5, 6, 7],suits = ['a', 'a', 'a', 'b', 'c']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [5, 5, 5, 6, 7],suits = ['a', 'a', 'a', 'b', 'c']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [10, 10, 11, 11, 12],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [10, 10, 11, 11, 12],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [6, 6, 7, 7, 8],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [6, 6, 7, 7, 8],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [2, 2, 3, 4, 5],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [2, 2, 3, 4, 5],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [7, 8, 9, 10, 11],suits = ['a', 'b', 'c', 'd', 'a']) == "High Card"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [7, 8, 9, 10, 11],suits = ['a', 'b', 'c', 'd', 'a']) == "High Card": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'b', 'c', 'd', 'a']) == "High Card"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'b', 'c', 'd', 'a']) == "High Card": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [9, 10, 11, 12, 13],suits = ['a', 'b', 'c', 'd', 'e']) == "High Card"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [9, 10, 11, 12, 13],suits = ['a', 'b', 'c', 'd', 'e']) == "High Card": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [9, 9, 10, 10, 11],suits = ['a', 'b', 'a', 'b', 'c']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [9, 9, 10, 10, 11],suits = ['a', 'b', 'a', 'b', 'c']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [10, 11, 12, 13, 13],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [10, 11, 12, 13, 13],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [3, 3, 4, 4, 5],suits = ['a', 'a', 'b', 'b', 'c']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [3, 3, 4, 4, 5],suits = ['a', 'a', 'b', 'b', 'c']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [9, 9, 9, 9, 10],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [9, 9, 9, 9, 10],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [13, 13, 13, 12, 11],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [13, 13, 13, 12, 11],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [7, 8, 9, 10, 11],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [7, 8, 9, 10, 11],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 1, 2, 2, 3],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 1, 2, 2, 3],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [9, 9, 9, 9, 9],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [9, 9, 9, 9, 9],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [2, 2, 2, 2, 3],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [2, 2, 2, 2, 3],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [13, 13, 13, 1, 1],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [13, 13, 13, 1, 1],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [6, 6, 6, 7, 7],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [6, 6, 6, 7, 7],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [13, 13, 12, 12, 11],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [13, 13, 12, 12, 11],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [5, 5, 10, 10, 10],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [5, 5, 10, 10, 10],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [3, 3, 5, 5, 7],suits = ['a', 'b', 'a', 'b', 'a']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [3, 3, 5, 5, 7],suits = ['a', 'b', 'a', 'b', 'a']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 2, 3, 4, 4],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 2, 3, 4, 4],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [12, 12, 13, 13, 13],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [12, 12, 13, 13, 13],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'a', 'a', 'a', 'd']) == "High Card"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'a', 'a', 'a', 'd']) == "High Card": {e}')
    
    total += 1
    try:
        result = candidate(ranks = [3, 3, 3, 3, 3],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(ranks = [3, 3, 3, 3, 3],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(ranks = [7, 7, 7, 7, 7],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
    assert candidate(ranks = [7, 7, 7, 8, 9],suits = ['a', 'b', 'c', 'a', 'd']) == "Three of a Kind"
    assert candidate(ranks = [10, 10, 2, 12, 9],suits = ['a', 'b', 'c', 'a', 'd']) == "Pair"
    assert candidate(ranks = [7, 7, 7, 7, 7],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
    assert candidate(ranks = [1, 1, 2, 2, 3],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
    assert candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'b', 'c', 'd', 'a']) == "High Card"
    assert candidate(ranks = [13, 2, 3, 1, 9],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
    assert candidate(ranks = [2, 3, 4, 5, 6],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
    assert candidate(ranks = [11, 11, 12, 12, 13],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair"
    assert candidate(ranks = [4, 4, 2, 4, 4],suits = ['d', 'a', 'a', 'b', 'c']) == "Three of a Kind"
    assert candidate(ranks = [10, 10, 11, 11, 12],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair"
    assert candidate(ranks = [6, 6, 6, 7, 7],suits = ['d', 'd', 'd', 'c', 'c']) == "Three of a Kind"
    assert candidate(ranks = [3, 3, 4, 4, 5],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
    assert candidate(ranks = [8, 8, 8, 9, 10],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
    assert candidate(ranks = [5, 6, 7, 8, 9],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
    assert candidate(ranks = [7, 7, 8, 8, 9],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
    assert candidate(ranks = [5, 5, 5, 3, 3],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
    assert candidate(ranks = [11, 12, 13, 13, 13],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
    assert candidate(ranks = [5, 5, 6, 6, 7],suits = ['a', 'b', 'a', 'b', 'a']) == "Pair"
    assert candidate(ranks = [6, 6, 7, 7, 8],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair"
    assert candidate(ranks = [1, 2, 3, 3, 3],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
    assert candidate(ranks = [4, 4, 5, 5, 6],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair"
    assert candidate(ranks = [9, 9, 9, 9, 9],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
    assert candidate(ranks = [1, 2, 3, 4, 4],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair"
    assert candidate(ranks = [8, 8, 9, 9, 10],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair"
    assert candidate(ranks = [10, 11, 12, 13, 13],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
    assert candidate(ranks = [5, 5, 5, 6, 7],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
    assert candidate(ranks = [6, 6, 6, 7, 8],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
    assert candidate(ranks = [10, 10, 10, 12, 13],suits = ['a', 'b', 'c', 'a', 'b']) == "Three of a Kind"
    assert candidate(ranks = [8, 8, 9, 9, 10],suits = ['a', 'a', 'b', 'b', 'c']) == "Pair"
    assert candidate(ranks = [3, 3, 3, 8, 8],suits = ['a', 'b', 'c', 'a', 'b']) == "Three of a Kind"
    assert candidate(ranks = [1, 3, 3, 3, 5],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
    assert candidate(ranks = [13, 13, 13, 13, 1],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
    assert candidate(ranks = [6, 6, 6, 7, 8],suits = ['a', 'a', 'a', 'b', 'c']) == "Three of a Kind"
    assert candidate(ranks = [1, 1, 2, 3, 4],suits = ['a', 'a', 'b', 'c', 'd']) == "Pair"
    assert candidate(ranks = [13, 13, 13, 13, 13],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
    assert candidate(ranks = [12, 12, 12, 12, 13],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
    assert candidate(ranks = [9, 9, 10, 11, 12],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
    assert candidate(ranks = [8, 8, 10, 10, 10],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
    assert candidate(ranks = [3, 3, 3, 4, 4],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
    assert candidate(ranks = [6, 6, 6, 6, 6],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
    assert candidate(ranks = [8, 8, 8, 9, 9],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
    assert candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
    assert candidate(ranks = [5, 5, 5, 5, 10],suits = ['a', 'a', 'a', 'a', 'b']) == "Three of a Kind"
    assert candidate(ranks = [1, 1, 2, 2, 3],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
    assert candidate(ranks = [7, 8, 9, 10, 11],suits = ['a', 'b', 'c', 'd', 'a']) == "High Card"
    assert candidate(ranks = [13, 12, 11, 10, 9],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
    assert candidate(ranks = [5, 5, 5, 6, 7],suits = ['a', 'b', 'c', 'a', 'a']) == "Three of a Kind"
    assert candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'b', 'c', 'd', 'e']) == "High Card"
    assert candidate(ranks = [2, 2, 3, 3, 4],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
    assert candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'b', 'c', 'd', 'e']) == "High Card"
    assert candidate(ranks = [6, 6, 6, 7, 8],suits = ['b', 'b', 'b', 'c', 'd']) == "Three of a Kind"
    assert candidate(ranks = [8, 8, 8, 9, 9],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
    assert candidate(ranks = [2, 2, 3, 4, 4],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
    assert candidate(ranks = [2, 3, 5, 5, 5],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
    assert candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'a', 'b', 'b', 'c']) == "High Card"
    assert candidate(ranks = [3, 3, 3, 3, 5],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
    assert candidate(ranks = [6, 6, 7, 7, 8],suits = ['a', 'a', 'b', 'b', 'c']) == "Pair"
    assert candidate(ranks = [2, 2, 2, 2, 2],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
    assert candidate(ranks = [9, 9, 9, 10, 10],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
    assert candidate(ranks = [13, 13, 2, 3, 4],suits = ['a', 'b', 'a', 'b', 'a']) == "Pair"
    assert candidate(ranks = [6, 6, 6, 6, 7],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
    assert candidate(ranks = [11, 11, 12, 12, 13],suits = ['a', 'a', 'b', 'b', 'c']) == "Pair"
    assert candidate(ranks = [10, 10, 11, 11, 12],suits = ['a', 'b', 'a', 'b', 'a']) == "Pair"
    assert candidate(ranks = [5, 6, 7, 8, 9],suits = ['a', 'b', 'c', 'd', 'a']) == "High Card"
    assert candidate(ranks = [1, 1, 1, 2, 3],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
    assert candidate(ranks = [8, 8, 8, 8, 2],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
    assert candidate(ranks = [13, 12, 11, 10, 9],suits = ['a', 'b', 'c', 'd', 'e']) == "High Card"
    assert candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
    assert candidate(ranks = [1, 1, 2, 3, 4],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair"
    assert candidate(ranks = [1, 1, 2, 3, 4],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
    assert candidate(ranks = [2, 3, 4, 5, 6],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
    assert candidate(ranks = [2, 2, 2, 3, 3],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
    assert candidate(ranks = [1, 2, 2, 3, 4],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
    assert candidate(ranks = [13, 13, 13, 12, 12],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
    assert candidate(ranks = [5, 5, 5, 6, 7],suits = ['a', 'a', 'a', 'b', 'c']) == "Three of a Kind"
    assert candidate(ranks = [10, 10, 11, 11, 12],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
    assert candidate(ranks = [6, 6, 7, 7, 8],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
    assert candidate(ranks = [2, 2, 3, 4, 5],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair"
    assert candidate(ranks = [7, 8, 9, 10, 11],suits = ['a', 'b', 'c', 'd', 'a']) == "High Card"
    assert candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'b', 'c', 'd', 'a']) == "High Card"
    assert candidate(ranks = [9, 10, 11, 12, 13],suits = ['a', 'b', 'c', 'd', 'e']) == "High Card"
    assert candidate(ranks = [9, 9, 10, 10, 11],suits = ['a', 'b', 'a', 'b', 'c']) == "Pair"
    assert candidate(ranks = [10, 11, 12, 13, 13],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
    assert candidate(ranks = [3, 3, 4, 4, 5],suits = ['a', 'a', 'b', 'b', 'c']) == "Pair"
    assert candidate(ranks = [9, 9, 9, 9, 10],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
    assert candidate(ranks = [13, 13, 13, 12, 11],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
    assert candidate(ranks = [7, 8, 9, 10, 11],suits = ['a', 'a', 'a', 'a', 'a']) == "Flush"
    assert candidate(ranks = [1, 1, 2, 2, 3],suits = ['a', 'b', 'c', 'd', 'a']) == "Pair"
    assert candidate(ranks = [9, 9, 9, 9, 9],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
    assert candidate(ranks = [2, 2, 2, 2, 3],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
    assert candidate(ranks = [13, 13, 13, 1, 1],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
    assert candidate(ranks = [6, 6, 6, 7, 7],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"
    assert candidate(ranks = [13, 13, 12, 12, 11],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
    assert candidate(ranks = [5, 5, 10, 10, 10],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
    assert candidate(ranks = [3, 3, 5, 5, 7],suits = ['a', 'b', 'a', 'b', 'a']) == "Pair"
    assert candidate(ranks = [1, 2, 3, 4, 4],suits = ['a', 'b', 'c', 'd', 'e']) == "Pair"
    assert candidate(ranks = [12, 12, 13, 13, 13],suits = ['a', 'b', 'c', 'd', 'a']) == "Three of a Kind"
    assert candidate(ranks = [1, 2, 3, 4, 5],suits = ['a', 'a', 'a', 'a', 'd']) == "High Card"
    assert candidate(ranks = [3, 3, 3, 3, 3],suits = ['a', 'b', 'c', 'd', 'e']) == "Three of a Kind"


