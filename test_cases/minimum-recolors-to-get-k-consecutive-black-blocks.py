def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(blocks = "WWWW",k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWWW",k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBBWWBBBW",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBBWWBBBW",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBWWBBWBW",k = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBWWBBWBW",k = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBBB",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBBB",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BWBWBWBWBW",k = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BWBWBWBWBW",k = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWWWWW",k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWWWWW",k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWWWWW",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWWWWW",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBB",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBB",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBBBB",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBBBB",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBWBBBW",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBWBBBW",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBWBWBWBWB",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBWBWBWBWB",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBBBB",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBBBB",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBBBBBBBBBBBBBBBBBB",k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBBBBBBBBBBBBBBBBBB",k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBWBBWBBWBBWBBWBBWBBWBBWBBWBBWBBW",k = 14) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBWBBWBBWBBWBBWBBWBBWBBWBBWBBWBBW",k = 14) == 4: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBBWWWWWWBBBWWBB",k = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBBWWWWWWBBBWWBB",k = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBWBWBWBWBWBWBWBWB",k = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBWBWBWBWBWBWBWBWB",k = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBWWBBWWBBWWBBWWBBW",k = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBWWBBWWBBWWBBWWBBW",k = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWB",k = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWB",k = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBWBWBWBWBWBWB",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBWBWBWBWBWBWB",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWBBWWBBWWBBWWBBWWBB",k = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWBBWWBBWWBBWWBBWWBB",k = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BWBWBWBWBWBWBWBWBWBWBWBWBW",k = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BWBWBWBWBWBWBWBWBWBWBWBWBW",k = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBWWBBWWBBW",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBWWBBWWBBW",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BWBWBWBWBWBWBW",k = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BWBWBWBWBWBWBW",k = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBBWWBBBWBBBWWBBB",k = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBBWWBBBWBBBWWBBB",k = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBBBBBBBBBBBBBB",k = 16) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBBBBBBBBBBBBBB",k = 16) == 0: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBBBBWWBBWWBBWWBBWW",k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBBBBWWBBWWBBWWBBWW",k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWBWWBBWWB",k = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWBWWBBWWB",k = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWWWBBWWWBBWWBBWWB",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWWWBBWWWBBWWBBWWB",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBWWWWBBBWBWWBBB",k = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBWWWWBBBWBWWBBB",k = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBWWBBWWBBWWBBWW",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBWWBBWWBBWWBBWW",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BWWBWWBWWBWWBWWBWWBW",k = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BWWBWWBWWBWWBWWBWWBW",k = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BWBWBWBWBWBWBWBWBWBW",k = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BWBWBWBWBWBWBWBWBWBW",k = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWWWWWWWWW",k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWWWWWWWWW",k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWBWWBWWBWWBWWBWWBWWBWWBWWB",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWBWWBWWBWWBWWBWWBWWBWWBWWB",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBBBBBWBBBBBBW",k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBBBBBWBBBBBBW",k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBWBBWWWWBBBWWBBB",k = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBWBBWWWWBBBWWBBB",k = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBBBBBWWWWWWWBBBBBB",k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBBBBBWWWWWWWBBBBBB",k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWWWBWWWWBWWWWBWWWWB",k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWWWBWWWWBWWWWBWWWWB",k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBWBBWBBWBBWBBW",k = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBWBBWBBWBBWBBW",k = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BWBWBWBWBWBWBWBWBW",k = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BWBWBWBWBWBWBWBWBW",k = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BWBWBWBWBW",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BWBWBWBWBW",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBBWWBBBWWBBB",k = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBBWWBBBWWBBB",k = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWWWWBBBWBBBWWWW",k = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWWWWBBBWBBBWWWW",k = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBWWWBBBWWWBBB",k = 9) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBWWWBBBWWWBBB",k = 9) == 3: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBWBWBWBWBWBWBWBW",k = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBWBWBWBWBWBWBWBW",k = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWWWWWWW",k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWWWWWWW",k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBWWBBWWBBWW",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBWWBBWWBBWW",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWBBBWWBBBWWBBBWW",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWBBBWWBBBWWBBBWW",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWWWWWWWWW",k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWWWWWWWWW",k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWWWWWWWWWWWWWWWWWWW",k = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWWWWWWWWWWWWWWWWWWW",k = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBBBBBBBWWWWWWWWW",k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBBBBBBBWWWWWWWWW",k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBBBB",k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBBBB",k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BWBWBWBWBWBWBWBWBWBW",k = 9) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BWBWBWBWBWBWBWBWBWBW",k = 9) == 4: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BWBWBWBWBWBWBWBWBWBWBW",k = 11) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BWBWBWBWBWBWBWBWBWBWBW",k = 11) == 5: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBBBBBBBB",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBBBBBBBB",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBBWWBBBWBWB",k = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBBWWBBBWBWB",k = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBBWBWBWBWBWBWBWB",k = 11) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBBWBWBWBWBWBWBWB",k = 11) == 4: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBBBBBBBBBBBBBBBBBBBBBBBBBW",k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBBBBBBBBBBBBBBBBBBBBBBBBBW",k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBBBBWWWWWW",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBBBBWWWWWW",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBWWBWBWBWBWBW",k = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBWWBWBWBWBWBW",k = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BWBWBWBWBWBWBWBW",k = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BWBWBWBWBWBWBWBW",k = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBWWBBWBWWBBWBBWBWBWBWB",k = 12) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBWWBBWBWWBBWBBWBWBWBWB",k = 12) == 5: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBWWWBBBWWWBBBWWWBB",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBWWWBBBWWWBBBWWWBB",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWBBWWBBWWBBWWBBWW",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWBBWWBBWWBBWWBBWW",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBBBBBWBBB",k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBBBBBWBBB",k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBBWWBBBWWBBB",k = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBBWWBBBWWBBB",k = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBWBBBWWBBBWWBBBWWB",k = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBWBBBWWBBBWWBBBWWB",k = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBWWWWWWWWWW",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBWWWWWWWWWW",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BWBWBWBWBW",k = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BWBWBWBWBW",k = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBBWBWBWBWBBB",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBBWBWBWBWBBB",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWBWBWBWBW",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWBWBWBWBW",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBWWBBWBBWWBBWBBWBBWWBBWB",k = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBWWBBWBBWWBBWBBWBBWWBBWB",k = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBWWBBWWBBWWBBWWBBWWBBWW",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBWWBBWWBBWWBBWWBBWWBBWW",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBBWWBBBWBBBWWBBB",k = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBBWWBBBWBBBWWBBB",k = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBWBWBWBWBWBWBWBWBWB",k = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBWBWBWBWBWBWBWBWBWB",k = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BWBWBWBWBWBWBWBW",k = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BWBWBWBWBWBWBWBW",k = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBWBBWWBBWWBBWBBWBBW",k = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBWBBWWBBWWBBWBBWBBW",k = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBWWBBWBWWBBWBBW",k = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBWWBBWBWWBBWBBW",k = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BWWWWBBWWWWBBWWWW",k = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BWWWWBBWWWWBBWWWW",k = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBWBWBBBBBBBWB",k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBWBWBBBBBBBWB",k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWWWWWWWWWWW",k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWWWWWWWWWWW",k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBWWWWBWBWWB",k = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBWWWWBWBWWB",k = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWBBWWBBWWBBWWBBWWBB",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWBBWWBBWWBBWWBBWWBB",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBWBBWBBWBBWBBWBBWB",k = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBWBBWBBWBBWBBWBBWB",k = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBWWBBWWBBWWBBWWBB",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBWWBBWWBBWWBBWWBB",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BWWBWWBWWBWWBWWBWW",k = 6) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BWWBWWBWWBWWBWWBWW",k = 6) == 4: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWWBWWWWBWBWWB",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWWBWWWWBWBWWB",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBWBWBWBWBWBWBWBWBWB",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBWBWBWBWBWBWBWBWBWB",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBWBBWBBWBBWBBWBBWB",k = 9) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBWBBWBBWBBWBBWBBWB",k = 9) == 3: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBBBBBWWWWWWWWWW",k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBBBBBWWWWWWWWWW",k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWWWWWWWWWWWWWWWWWWW",k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWWWWWWWWWWWWWWWWWWW",k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WBBWWBBWWBBWWBBWWBBWWBBW",k = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WBBWWBBWWBBWWBBWWBBWWBBW",k = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWWWBBWWWWBBWWWWBBWWWWBB",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWWWBBWWWWBBWWWWBBWWWWBB",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWBBWWBBWWBBWW",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWBBWWBBWWBBWW",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWWWBWWWWBWWWWB",k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWWWBWWWWBWWWWB",k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBBBBBBBB",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBBBBBBBB",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBBBBBBBBBBBBBBBBBB",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBBBBBBBBBBBBBBBBBB",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWWWWWWWWWWWWW",k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWWWWWWWWWWWWW",k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "WWBBWWBBWWBBWW",k = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "WWBBWWBBWWBBWW",k = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BBBBBWWBBBWWBBBWWBBBWWBBB",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BBBBBWWBBBWWBBBWWBBBWWBBB",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(blocks = "BWBWBWBWBWBWBWBWBWBWBWBWBWBWBW",k = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocks = "BWBWBWBWBWBWBWBWBWBWBWBWBWBWBW",k = 15) == 7: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(blocks = "WWWW",k = 2) == 2
    assert candidate(blocks = "WBBBWWBBBW",k = 3) == 0
    assert candidate(blocks = "WBBWWBBWBW",k = 7) == 3
    assert candidate(blocks = "BBBBB",k = 3) == 0
    assert candidate(blocks = "BWBWBWBWBW",k = 6) == 3
    assert candidate(blocks = "WWWWWW",k = 4) == 4
    assert candidate(blocks = "WWWWWW",k = 3) == 3
    assert candidate(blocks = "BBBB",k = 4) == 0
    assert candidate(blocks = "BBBBBB",k = 4) == 0
    assert candidate(blocks = "WBWBBBW",k = 2) == 0
    assert candidate(blocks = "WBWBWBWBWB",k = 5) == 2
    assert candidate(blocks = "BBBBBB",k = 3) == 0
    assert candidate(blocks = "BBBBBBBBBBBBBBBBBBBB",k = 20) == 0
    assert candidate(blocks = "BBWBBWBBWBBWBBWBBWBBWBBWBBWBBWBBW",k = 14) == 4
    assert candidate(blocks = "WBBBWWWWWWBBBWWBB",k = 7) == 2
    assert candidate(blocks = "WBWBWBWBWBWBWBWBWB",k = 10) == 5
    assert candidate(blocks = "WBBWWBBWWBBWWBBWWBBW",k = 8) == 4
    assert candidate(blocks = "WBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWB",k = 10) == 5
    assert candidate(blocks = "WBWBWBWBWBWBWB",k = 5) == 2
    assert candidate(blocks = "WWBBWWBBWWBBWWBBWWBB",k = 6) == 2
    assert candidate(blocks = "BWBWBWBWBWBWBWBWBWBWBWBWBW",k = 7) == 3
    assert candidate(blocks = "BBWWBBWWBBW",k = 5) == 2
    assert candidate(blocks = "BWBWBWBWBWBWBW",k = 7) == 3
    assert candidate(blocks = "WBBBWWBBBWBBBWWBBB",k = 7) == 1
    assert candidate(blocks = "BBBBBBBBBBBBBBBB",k = 16) == 0
    assert candidate(blocks = "BBBBBBWWBBWWBBWWBBWW",k = 6) == 0
    assert candidate(blocks = "WWBWWBBWWB",k = 6) == 3
    assert candidate(blocks = "WWWWBBWWWBBWWBBWWB",k = 5) == 2
    assert candidate(blocks = "WBBWWWWBBBWBWWBBB",k = 8) == 3
    assert candidate(blocks = "BBWWBBWWBBWWBBWW",k = 4) == 2
    assert candidate(blocks = "BWWBWWBWWBWWBWWBWWBW",k = 7) == 4
    assert candidate(blocks = "BWBWBWBWBWBWBWBWBWBW",k = 15) == 7
    assert candidate(blocks = "WWWWWWWWWW",k = 10) == 10
    assert candidate(blocks = "WWBWWBWWBWWBWWBWWBWWBWWBWWB",k = 3) == 2
    assert candidate(blocks = "WBBBBBBWBBBBBBW",k = 10) == 1
    assert candidate(blocks = "BBBWBBWWWWBBBWWBBB",k = 6) == 1
    assert candidate(blocks = "BBBBBBBWWWWWWWBBBBBB",k = 8) == 1
    assert candidate(blocks = "WWWWBWWWWBWWWWBWWWWB",k = 4) == 3
    assert candidate(blocks = "WBBWBBWBBWBBWBBW",k = 7) == 2
    assert candidate(blocks = "BWBWBWBWBWBWBWBWBW",k = 10) == 5
    assert candidate(blocks = "BWBWBWBWBW",k = 4) == 2
    assert candidate(blocks = "WBBBWWBBBWWBBB",k = 6) == 2
    assert candidate(blocks = "WWWWWBBBWBBBWWWW",k = 7) == 1
    assert candidate(blocks = "BBBWWWBBBWWWBBB",k = 9) == 3
    assert candidate(blocks = "WBBWBWBWBWBWBWBWBW",k = 8) == 3
    assert candidate(blocks = "WWWWWWWW",k = 4) == 4
    assert candidate(blocks = "BBWWBBWWBBWW",k = 4) == 2
    assert candidate(blocks = "WWBBBWWBBBWWBBBWW",k = 5) == 2
    assert candidate(blocks = "WWWWWWWWWW",k = 5) == 5
    assert candidate(blocks = "WWWWWWWWWWWWWWWWWWWW",k = 15) == 15
    assert candidate(blocks = "BBBBBBBBBWWWWWWWWW",k = 9) == 0
    assert candidate(blocks = "BBBBBB",k = 6) == 0
    assert candidate(blocks = "BWBWBWBWBWBWBWBWBWBW",k = 9) == 4
    assert candidate(blocks = "BWBWBWBWBWBWBWBWBWBWBW",k = 11) == 5
    assert candidate(blocks = "BBBBBBBBBB",k = 5) == 0
    assert candidate(blocks = "BBBBWWBBBWBWB",k = 6) == 2
    assert candidate(blocks = "BBBBWBWBWBWBWBWBWB",k = 11) == 4
    assert candidate(blocks = "WBBBBBBBBBBBBBBBBBBBBBBBBBBW",k = 25) == 0
    assert candidate(blocks = "BBBBBBWWWWWW",k = 4) == 0
    assert candidate(blocks = "BBBWWBWBWBWBWBW",k = 6) == 2
    assert candidate(blocks = "BWBWBWBWBWBWBWBW",k = 8) == 4
    assert candidate(blocks = "WBBWWBBWBWWBBWBBWBWBWBWB",k = 12) == 5
    assert candidate(blocks = "BBBWWWBBBWWWBBBWWWBB",k = 5) == 2
    assert candidate(blocks = "WWBBWWBBWWBBWWBBWW",k = 5) == 2
    assert candidate(blocks = "BBBBBBBWBBB",k = 8) == 1
    assert candidate(blocks = "WBBBWWBBBWWBBB",k = 8) == 2
    assert candidate(blocks = "BBBWBBBWWBBBWWBBBWWB",k = 7) == 1
    assert candidate(blocks = "BBWWWWWWWWWW",k = 3) == 1
    assert candidate(blocks = "BWBWBWBWBW",k = 8) == 4
    assert candidate(blocks = "WBBBWBWBWBWBBB",k = 5) == 1
    assert candidate(blocks = "WWBWBWBWBW",k = 5) == 2
    assert candidate(blocks = "WBBWWBBWBBWWBBWBBWBBWWBBWB",k = 8) == 2
    assert candidate(blocks = "BBWWBBWWBBWWBBWWBBWWBBWW",k = 5) == 2
    assert candidate(blocks = "WBBBWWBBBWBBBWWBBB",k = 6) == 1
    assert candidate(blocks = "WBWBWBWBWBWBWBWBWBWB",k = 10) == 5
    assert candidate(blocks = "BWBWBWBWBWBWBWBW",k = 6) == 3
    assert candidate(blocks = "WBBWBBWWBBWWBBWBBWBBW",k = 8) == 2
    assert candidate(blocks = "WBBWWBBWBWWBBWBBW",k = 10) == 4
    assert candidate(blocks = "BWWWWBBWWWWBBWWWW",k = 7) == 4
    assert candidate(blocks = "BBBWBWBBBBBBBWB",k = 9) == 1
    assert candidate(blocks = "WWWWWWWWWWWW",k = 5) == 5
    assert candidate(blocks = "WBBWWWWBWBWWB",k = 6) == 3
    assert candidate(blocks = "WWBBWWBBWWBBWWBBWWBB",k = 4) == 2
    assert candidate(blocks = "WBBWBBWBBWBBWBBWBBWB",k = 10) == 3
    assert candidate(blocks = "BBWWBBWWBBWWBBWWBB",k = 4) == 2
    assert candidate(blocks = "BWWBWWBWWBWWBWWBWW",k = 6) == 4
    assert candidate(blocks = "WWWBWWWWBWBWWB",k = 4) == 2
    assert candidate(blocks = "WBWBWBWBWBWBWBWBWBWB",k = 5) == 2
    assert candidate(blocks = "WBBWBBWBBWBBWBBWBBWB",k = 9) == 3
    assert candidate(blocks = "BBBBBBBWWWWWWWWWW",k = 7) == 0
    assert candidate(blocks = "WWWWWWWWWWWWWWWWWWWW",k = 1) == 1
    assert candidate(blocks = "WBBWWBBWWBBWWBBWWBBWWBBW",k = 7) == 3
    assert candidate(blocks = "WWWWBBWWWWBBWWWWBBWWWWBB",k = 4) == 2
    assert candidate(blocks = "WWBBWWBBWWBBWW",k = 5) == 2
    assert candidate(blocks = "WWWWBWWWWBWWWWB",k = 4) == 3
    assert candidate(blocks = "BBBBBBBBBB",k = 10) == 0
    assert candidate(blocks = "BBBBBBBBBBBBBBBBBBBB",k = 10) == 0
    assert candidate(blocks = "WWWWWWWWWWWWWW",k = 5) == 5
    assert candidate(blocks = "WWBBWWBBWWBBWW",k = 6) == 2
    assert candidate(blocks = "BBBBBWWBBBWWBBBWWBBBWWBBB",k = 5) == 0
    assert candidate(blocks = "BWBWBWBWBWBWBWBWBWBWBWBWBWBWBW",k = 15) == 7


