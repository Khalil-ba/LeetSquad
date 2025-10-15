def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "XXXXXXXXXX") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXXXXXXX") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOOX") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOOX") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOOXOOXO") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOOXOOXO") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXXOOXXOO") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXXOOXXOO") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOX") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOX") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "OXOXOXOXOX") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OXOXOXOXOX") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOOXXOOOX") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOOXXOOOX") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXX") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXX") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOOO") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOOO") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOXOX") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOXOX") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "OXOXOX") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OXOXOX") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOOXXOOOXXOOO") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOOXXOOOXXOOO") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXOXOXO") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXOXOXO") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXXX") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXXX") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOXOOXOOX") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOXOOXOOX") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXXXXXX") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXXXXXX") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXO") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXO") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXXOOX") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXXOOX") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOXO") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOXO") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOOOXOOXOXXXX") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOOOXOOXOXXXX") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOXOXOOXOXOXO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOXOXOOXOXOXO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOXOXXOXXOOXOX") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOXOXXOXXOOXOX") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXOXOXOXO") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXOXOXOXO") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOOXOXOOXOXOXOXOOXOXOXOOXOXOXOOXO") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOOXOXOOXOXOXOXOOXOXOXOOXOXOXOOXO") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOXOXOOXOOXOOXOOXOOXOOXOOXOOX") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOXOXOOXOOXOOXOOXOOXOOXOOXOOX") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXXOOXOXOXXXOXO") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXXOOXOXOXXXOXO") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOXOXOOXOXOOXOXOOX") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOXOXOOXOXOOXOXOOX") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOOXOOXOOXOO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOOXOOXOOXOO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXOXO") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXOXO") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "OXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "OXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOOXOOOXOOOXOOOXOOO") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOOXOOOXOOOXOOOXOOO") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOXOXOXOXOXOXOX") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOXOXOXOXOXOXOX") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOOOOOOOOOOOOOOOO") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOOOOOOOOOOOOOOOO") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOOOOOOOOOOOOOOOOOO") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOOOOOOOOOOOOOOOOOO") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOOOOXXOOOOXXOOOOXXOOOOXXOOOOXXOOOOXXOOOOXX") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOOOOXXOOOOXXOOOOXXOOOOXXOOOOXXOOOOXXOOOOXX") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXXOOXXOOXXXX") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXXOOXXOOXXXX") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOXXOOXXOOXXOOXX") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOXXOOXXOOXXOOXX") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXOXOXOOOXOXO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXOXOXOOOXOXO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXOXOXOXOXO") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXOXOXOXOXO") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOOXOXOXOXOXX") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOOXOXOXOXOXX") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "OXXOXOXOXOXO") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OXXOXOXOXOXO") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXXXXXXXXXXXXXXXX") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXXXXXXXXXXXXXXXX") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOXOXOXOOO") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOXOXOXOOO") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "OXOXOXOXOXOX") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OXOXOXOXOXOX") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOOXOXOXOXOXXOXOXXOXOXXOXOXXOXOXX") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOOXOXOXOXOXXOXOXXOXOXXOXOXXOXOXX") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXOXOXOXO") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXOXOXOXO") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOOXXXXOOOXXXXOOO") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOOXXXXOOOXXXXOOO") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOXOXOXOXOXOXOXOXOXOXOXOX") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOXOXOXOXOXOXOXOXOXOXOXOX") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOOXXOOXXOOXXOOXXOOX") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOOXXOOXXOOXXOOXXOOX") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXXXXXXXXXXXXX") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXXXXXXXXXXXXX") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXOXOXOXOXOXOXO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXOXOXOXOXOXOXO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXXXXXXXXXOXOXOXOXOXOXOXO") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXXXXXXXXXOXOXOXOXOXOXOXO") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXXXXXXXXXOXXXXXXXXXOXXXXXXXXXOXXXXXXXXXO") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXXXXXXXXXOXXXXXXXXXOXXXXXXXXXOXXXXXXXXXO") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOXOXOXOXOXOXO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOXOXOXOXOXOXO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "OXOXOXOXOXOXOXOXOXOXOX") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OXOXOXOXOXOXOXOXOXOXOX") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXXOOXXOOXXOOXXOOXXOO") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXXOOXXOOXXOOXXOOXXOO") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "OXOXOXOXOXOXOXOXOXOXOXOX") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OXOXOXOXOXOXOXOXOXOXOXOX") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXXXXXXOOOOOOOOOXXXXXXXXX") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXXXXXXOOOOOOOOOXXXXXXXXX") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOOXXOOXXOOXXOOXX") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOOXXOOXXOOXXOOXX") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOXOOXOOXOOXOOX") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOXOOXOOXOOXOOX") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOXOXOXOXOXOXOXOXOXOXOXOXOXOOO") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOXOXOXOXOXOXOXOXOXOXOXOXOXOOO") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOOXOOXOOXOOXO") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOOXOOXOOXOOXO") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXXXXXXXXXX") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXXXXXXXXXX") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOOXOXOXOXOXO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOOXOXOXOXOXO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXOOOOXOXOOXOXO") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXOOOOXOXOOXOXO") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXO") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXO") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOOXXOOXXOOXX") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOOXXOOXXOOXX") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOXOOXOOXOXOX") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOXOOXOOXOXOX") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOOXOXOXOXOXOXOXO") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOOXOXOXOXOXOXOXO") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOXOOXOOXOOXOOXOOX") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOXOOXOOXOOXOOXOOX") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOOXXXOOOXXXOOO") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOOXXXOOOXXXOOO") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXOXOXOXXXO") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXOXOXOXXXO") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXXOOXOXO") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXXOOXOXO") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "OXXXXOOOXXXXOOOXXX") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OXXXXOOOXXXXOOOXXX") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOOXOXOXOXOXOXOOOO") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOOXOXOXOXOXOXOOOO") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOXOOXOOXOOXOOXOOXOOX") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOXOOXOOXOOXOOXOOXOOX") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOOXOOXOOXOOXOOXOO") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOOXOOXOOXOOXOOXOO") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOOXOOXOOXOOX") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOOXOOXOOXOOX") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXXXXXXXXXXXXXXXXXXXXX") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXXXXXXXXXXXXXXXXXXXXX") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOXOXOXOXOXOOO") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOXOXOXOXOXOOO") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXXOXXOXXOXXOXX") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXXOXXOXXOXXOXX") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOOXOXOXOXOXOXOXOXX") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOOXOXOXOXOXOXOXOXX") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXO") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXO") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXOXOXOXOXO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXOXOXOXOXO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "OXOXOXOXOXOXOX") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OXOXOXOXOXOXOX") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOXOXOXOXOXOXOXOXOX") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOXOXOXOXOXOXOXOXOX") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXOXXXXOXXXXO") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXOXXXXOXXXXO") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXOXOXO") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXOXOXO") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOXOXOOXOXOOXOXOOXOXOOX") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOXOXOOXOXOOXOXOOXOXOOX") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOOOXXOOXXOOXX") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOOOXXOOXXOOXX") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOOXXOOXXOOXXOOXXOOXXOOXXOOX") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOOXXOOXXOOXXOOXXOOXXOOXXOOX") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXOOXXXXOOXXXXOO") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXOOXXXXOOXXXXOO") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOXXOXXOXXOXX") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOXXOXXOXXOXX") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOOOOOOOOOOOO") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOOOOOOOOOOOO") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXXXXXXOOXXXXXXOOXXXXXX") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXXXXXXOOXXXXXXOOXXXXXX") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXXXOXOXOXXX") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXXXOXOXOXXX") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXOXOXOXOXOXOXO") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXOXOXOXOXOXOXO") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXOOXOXOX") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXOOXOXOX") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOOXXOOXXOOXXOOXXOO") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOOXXOOXXOOXXOOXXOO") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXXXXXXXXXXXXXXX") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXXXXXXXXXXXXXXX") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXXXXXXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXXXXXXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOXOXOXOXOXOXOX") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOXOXOXOXOXOXOX") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOXOOXOOXOOXOOXOOXOOXOOX") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOXOOXOOXOOXOOXOOXOOXOOX") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOOXOOOXOOOXOOO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOOXOOOXOOOXOOO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXXOOXXOOXXOO") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXXOOXXOOXXOO") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXOXOXOXOX") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXOXOXOXOX") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXOXOXOXOXOXOXOXO") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXOXOXOXOXOXOXOXO") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOXOXOXOXOX") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOXOXOXOXOX") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOXOXOXO") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOXOXOXO") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOOXXOOOOXXOOOXXOOO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOOXXOOOOXXOOOXXOOO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOOXOOXOOXOOXOOXOOXOOX") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOOXOOXOOXOOXOOXOOXOOX") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOXOXOXOXOXOX") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOXOXOXOXOXOX") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "OXOXOXOXOXOXOXOXOX") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OXOXOXOXOXOXOXOXOX") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "OXOOXOOXOOXOOXOOXOOXOOX") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OXOOXOOXOOXOOXOOXOOXOOX") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOOXOOXOOXOOXOOXOOXOOXOOXOO") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOOXOOXOOXOOXOOXOOXOOXOOXOO") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "OXXOXOXXOXOXXOXO") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OXXOXOXXOXOXXOXO") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXXXXXOXOXO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXXXXXOXOXO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXXXXXOOOXXXXX") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXXXXXOOOXXXXX") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXXOOXXOOXXOOXXOOXXOOXXOO") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXXOOXXOOXXOOXXOOXXOOXXOO") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOO") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOO") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOXOXXOXOXXOX") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOXOXXOXOXXOX") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOO") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOO") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "OXOXOXOXOXOXOXOXOXO") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OXOXOXOXOXOXOXOXOXO") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "OXOXOXOXOXOXO") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OXOXOXOXOXOXO") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXOXXXXOXXXXOXXXXOXXXXOXXXXOXXXXO") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXOXXXXOXXXXOXXXXOXXXXOXXXXOXXXXO") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXXXXXXXXOXXXXXXXXX") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXXXXXXXXOXXXXXXXXX") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOX") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOX") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOOXXOOOXXOOOXXOOO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOOXXOOOXXOOOXXOOO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOOXOXOXOXOXOXOXOXOXOXOOOO") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOOXOXOXOXOXOXOXOXOXOXOOOO") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXXOXOXXOXOXXOXOXXOXXO") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXXOXOXXOXOXXOXOXXOXXO") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOXOXOXOXOXOXOXOXOXOXOXO") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOXOXOXOXOXOXOXOXOXOXOXO") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOOOOOOOOOOOOO") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOOOOOOOOOOOOO") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOXXOXXOXXO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOXXOXXOXXO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "OXOXOXOXOXOXOXOX") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OXOXOXOXOXOXOXOX") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXXXXXXXXXXXXXXOOOOOOOOOOOO") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXXXXXXXXXXXXXXOOOOOOOOOOOO") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOOOOOOOOOOOOOOOOO") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOOOOOOOOOOOOOOOOO") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXXXXXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXXXXXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXOOXOXOOXOXX") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXOOXOXOOXOXX") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXOXOXOXOXOXO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXOXOXOXOXOXO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOOOXOOOOXOOOOXOOOO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOOOXOOOOXOOOOXOOOO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOXXOOXXOOXXOOX") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOXXOOXXOOXXOOX") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOOXOXOXOXOXOOOO") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOOXOXOXOXOXOOOO") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOX") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOX") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOOOXOOOXOOO") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOOOXOOOXOOO") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXX") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXX") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOXOXOXOXOXOXOXO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOXOXOXOXOXOXOXO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOXOOXOXOXOO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOXOOXOXOXOO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOOOXOOOOXOOOOXOOOOXOOOO") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOOOXOOOOXOOOOXOOOOXOOOO") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOOXOXOXOXOX") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOOXOXOXOXOX") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOXOOOXOOOXOOOXOOOXOOOXOOOXOOOXOOOXOOOXOOO") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOXOOOXOOOXOOOXOOOXOOOXOOOXOOOXOOOXOOOXOOO") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOOXXOOXXOO") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOOXXOOXXOO") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXXXXXOOOOXXXXXXXX") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXXXXXOOOOXXXXXXXX") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXXXXXXXXXXXXXX") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXXXXXXXXXXXXXX") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "XOXOOXOXOOXOXOXO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XOXOOXOXOOXOXOXO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "OXOOXOOOXOXOOXOO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OXOOXOOOXOXOOXOO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXOXOXXOXOXOXXOX") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXOXOXXOXOXOXXOX") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "OOOOOOOOOOOOOOOOOOOOOOOOOOOO") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OOOOOOOOOOOOOOOOOOOOOOOOOOOO") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "XXXXXXXXXXXXXX") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XXXXXXXXXXXXXX") == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "XXXXXXXXXX") == 4
    assert candidate(s = "OOXOOX") == 2
    assert candidate(s = "OOXOOXOOXO") == 3
    assert candidate(s = "OOXXOOXXOO") == 2
    assert candidate(s = "XXOX") == 2
    assert candidate(s = "OXOXOXOXOX") == 3
    assert candidate(s = "XOOOXXOOOX") == 3
    assert candidate(s = "XXX") == 1
    assert candidate(s = "OOOO") == 0
    assert candidate(s = "XOOXOX") == 2
    assert candidate(s = "OXOXOX") == 2
    assert candidate(s = "OOOXXOOOXXOOO") == 2
    assert candidate(s = "XOXOXOXOXO") == 3
    assert candidate(s = "XXXXXX") == 2
    assert candidate(s = "XOOXOOXOOX") == 4
    assert candidate(s = "XXXXXXXXX") == 3
    assert candidate(s = "XOXOXO") == 2
    assert candidate(s = "OOXXOOX") == 2
    assert candidate(s = "OOXOXO") == 1
    assert candidate(s = "XOOOOXOOXOXXXX") == 4
    assert candidate(s = "XOOXOXOOXOXOXO") == 4
    assert candidate(s = "OOXOXOXXOXXOOXOX") == 4
    assert candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXOXOXOXO") == 8
    assert candidate(s = "XOXOOXOXOOXOXOXOXOOXOXOXOOXOXOXOOXO") == 9
    assert candidate(s = "XOOXOXOOXOOXOOXOOXOOXOOXOOXOOX") == 10
    assert candidate(s = "XOXOXXOOXOXOXXXOXO") == 5
    assert candidate(s = "XOOXOXOOXOXOOXOXOOX") == 5
    assert candidate(s = "OOXOOXOOXOOXOO") == 4
    assert candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXOXO") == 7
    assert candidate(s = "OXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX") == 12
    assert candidate(s = "OXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX") == 9
    assert candidate(s = "XOOOXOOOXOOOXOOOXOOO") == 5
    assert candidate(s = "XOOXOXOXOXOXOXOX") == 5
    assert candidate(s = "OOOOOOOOOOOOOOOOO") == 0
    assert candidate(s = "OOOOOOOOOOOOOOOOOOO") == 0
    assert candidate(s = "XXOOOOXXOOOOXXOOOOXXOOOOXXOOOOXXOOOOXXOOOOXX") == 8
    assert candidate(s = "OOXXOOXXOOXXXX") == 4
    assert candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO") == 9
    assert candidate(s = "XOOXXOOXXOOXXOOXX") == 5
    assert candidate(s = "XOXOXOXOXOOOXOXO") == 4
    assert candidate(s = "XXXOXOXOXOXO") == 3
    assert candidate(s = "XXOOXOXOXOXOXX") == 4
    assert candidate(s = "OXXOXOXOXOXO") == 3
    assert candidate(s = "XXXXXXXXXXXXXXXXXXX") == 7
    assert candidate(s = "OOXOXOXOXOOO") == 2
    assert candidate(s = "OXOXOXOXOXOX") == 3
    assert candidate(s = "XXOOXOXOXOXOXXOXOXXOXOXXOXOXXOXOXX") == 10
    assert candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX") == 14
    assert candidate(s = "XOXOXOXOXOXO") == 3
    assert candidate(s = "XOOOXXXXOOOXXXXOOO") == 5
    assert candidate(s = "XXOXOXOXOXOXOXOXOXOXOXOXOX") == 7
    assert candidate(s = "XXOOXXOOXXOOXXOOXXOOX") == 6
    assert candidate(s = "XXXXXXXXXXXXXXXX") == 6
    assert candidate(s = "XXXOXOXOXOXOXOXO") == 4
    assert candidate(s = "XOXXXXXXXXXOXOXOXOXOXOXOXO") == 8
    assert candidate(s = "XOXOXXXXXXXXXOXXXXXXXXXOXXXXXXXXXOXXXXXXXXXO") == 13
    assert candidate(s = "OOXOXOXOXOXOXOXO") == 4
    assert candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO") == 12
    assert candidate(s = "OXOXOXOXOXOXOXOXOXOXOX") == 6
    assert candidate(s = "OOXXOOXXOOXXOOXXOOXXOO") == 5
    assert candidate(s = "OXOXOXOXOXOXOXOXOXOXOXOX") == 6
    assert candidate(s = "XXXXXXXXXOOOOOOOOOXXXXXXXXX") == 6
    assert candidate(s = "XXOOXXOOXXOOXXOOXX") == 5
    assert candidate(s = "XOOXOOXOOXOOXOOX") == 6
    assert candidate(s = "OOXOXOXOXOXOXOXOXOXOXOXOXOXOXOOO") == 7
    assert candidate(s = "OOXOOXOOXOOXOOXO") == 5
    assert candidate(s = "XXXXXXXXXXXXX") == 5
    assert candidate(s = "XXOOXOXOXOXOXO") == 4
    assert candidate(s = "XXXOOOOXOXOOXOXO") == 3
    assert candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXO") == 6
    assert candidate(s = "XXOOXXOOXXOOXX") == 4
    assert candidate(s = "XOOXOOXOOXOXOX") == 5
    assert candidate(s = "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO") == 0
    assert candidate(s = "XXOOXOXOXOXOXOXOXO") == 5
    assert candidate(s = "XOOXOOXOOXOOXOOXOOX") == 7
    assert candidate(s = "OOOXXXOOOXXXOOO") == 2
    assert candidate(s = "XXXOXOXOXXXO") == 3
    assert candidate(s = "XOXOXXOOXOXO") == 3
    assert candidate(s = "OXXXXOOOXXXXOOOXXX") == 5
    assert candidate(s = "OOOXOXOXOXOXOXOOOO") == 3
    assert candidate(s = "XOOXOOXOOXOOXOOXOOXOOX") == 8
    assert candidate(s = "OOXOOXOOXOOXOOXOOXOO") == 6
    assert candidate(s = "OOXOOXOOXOOXOOX") == 5
    assert candidate(s = "XXXXXXXXXXXXXXXXXXXXXXXX") == 8
    assert candidate(s = "OOXOXOXOXOXOXOOO") == 3
    assert candidate(s = "XOXXOXXOXXOXXOXX") == 6
    assert candidate(s = "XXOOXOXOXOXOXOXOXOXX") == 6
    assert candidate(s = "XOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXO") == 13
    assert candidate(s = "XOXOXOXOXOXOXO") == 4
    assert candidate(s = "OXOXOXOXOXOXOX") == 4
    assert candidate(s = "XXOXOXOXOXOXOXOXOXOX") == 6
    assert candidate(s = "XXXXOXXXXOXXXXO") == 5
    assert candidate(s = "XOXOXOXOXOXOXOXOXOXOXOXOXOXO") == 7
    assert candidate(s = "XOOXOXOOXOXOOXOXOOXOXOOX") == 6
    assert candidate(s = "OOOOXXOOXXOOXX") == 3
    assert candidate(s = "XXOOXXOOXXOOXXOOXXOOXXOOXXOOX") == 8
    assert candidate(s = "XXXXOOXXXXOOXXXXOO") == 6
    assert candidate(s = "XXOXXOXXOXXOXX") == 5
    assert candidate(s = "OOOOOOOOOOOOO") == 0
    assert candidate(s = "OOXXXXXXOOXXXXXXOOXXXXXX") == 6
    assert candidate(s = "XOXOXXXOXOXOXXX") == 4
    assert candidate(s = "XOXOXOXOXOXOXOXOXO") == 5
    assert candidate(s = "XOXOXOOXOXOX") == 4
    assert candidate(s = "XXOOXXOOXXOOXXOOXXOO") == 5
    assert candidate(s = "XXXXXXXXXXXXXXXXXX") == 6
    assert candidate(s = "XXXXXXXXXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO") == 13
    assert candidate(s = "XXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX") == 9
    assert candidate(s = "XXOXOXOXOXOXOXOX") == 5
    assert candidate(s = "XOOXOOXOOXOOXOOXOOXOOXOOX") == 9
    assert candidate(s = "XOOOXOOOXOOOXOOO") == 4
    assert candidate(s = "OOXXOOXXOOXXOO") == 3
    assert candidate(s = "XOXOXOXOXOXOX") == 4
    assert candidate(s = "XOXOXOXOXOXOXOXOXOXO") == 5
    assert candidate(s = "XXOXOXOXOXOX") == 4
    assert candidate(s = "OOXOXOXOXO") == 2
    assert candidate(s = "XOOOXXOOOOXXOOOXXOOO") == 4
    assert candidate(s = "OOXOOXOOXOOXOOXOOXOOXOOX") == 8
    assert candidate(s = "XXOXOXOXOXOXOX") == 4
    assert candidate(s = "OXOXOXOXOXOXOXOXOX") == 5
    assert candidate(s = "OXOOXOOXOOXOOXOOXOOXOOX") == 8
    assert candidate(s = "OOXOOXOOXOOXOOXOOXOOXOOXOOXOO") == 9
    assert candidate(s = "OXXOXOXXOXOXXOXO") == 5
    assert candidate(s = "XXXXXXXXOXOXO") == 4
    assert candidate(s = "XXXXXXXXOOOXXXXX") == 5
    assert candidate(s = "OOXXOOXXOOXXOOXXOOXXOOXXOO") == 6
    assert candidate(s = "OOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOO") == 12
    assert candidate(s = "XOOXOXXOXOXXOX") == 5
    assert candidate(s = "OOOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOO") == 9
    assert candidate(s = "OXOXOXOXOXOXOXOXOXO") == 5
    assert candidate(s = "OXOXOXOXOXOXO") == 3
    assert candidate(s = "XXXXOXXXXOXXXXOXXXXOXXXXOXXXXOXXXXO") == 11
    assert candidate(s = "XOXOXXXXXXXXOXXXXXXXXX") == 7
    assert candidate(s = "XOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOX") == 12
    assert candidate(s = "XOOOXXOOOXXOOOXXOOO") == 4
    assert candidate(s = "OOOXOXOXOXOXOXOXOXOXOXOOOO") == 5
    assert candidate(s = "XOXXOXOXXOXOXXOXOXXOXXO") == 7
    assert candidate(s = "OOXOXOXOXOXOXOXOXOXOXOXOXO") == 6
    assert candidate(s = "OOOOOOOOOOOOOO") == 0
    assert candidate(s = "XXOXXOXXOXXO") == 4
    assert candidate(s = "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO") == 0
    assert candidate(s = "OXOXOXOXOXOXOXOX") == 4
    assert candidate(s = "XXXXXXXXXXXXXXXXXOOOOOOOOOOOO") == 6
    assert candidate(s = "OOOOOOOOOOOOOOOOOO") == 0
    assert candidate(s = "XXXXXXXXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX") == 11
    assert candidate(s = "XXXOOXOXOOXOXX") == 4
    assert candidate(s = "XOXOXOXOXOXOXOXO") == 4
    assert candidate(s = "XOOOOXOOOOXOOOOXOOOO") == 4
    assert candidate(s = "XOOXXOOXXOOXXOOX") == 5
    assert candidate(s = "OOOXOXOXOXOXOOOO") == 3
    assert candidate(s = "OOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOXOOX") == 12
    assert candidate(s = "XOOOOXOOOXOOO") == 3
    assert candidate(s = "XXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXX") == 11
    assert candidate(s = "OOXOXOXOXOXOXOXOXO") == 4
    assert candidate(s = "XOXOXOOXOXOXOO") == 4
    assert candidate(s = "XOOOOXOOOOXOOOOXOOOOXOOOO") == 5
    assert candidate(s = "XOOXOXOXOXOX") == 4
    assert candidate(s = "OOXOOOXOOOXOOOXOOOXOOOXOOOXOOOXOOOXOOOXOOO") == 10
    assert candidate(s = "XXOOXXOOXXOO") == 3
    assert candidate(s = "XXXXXXXXOOOOXXXXXXXX") == 6
    assert candidate(s = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") == 14
    assert candidate(s = "XXXXXXXXXXXXXXXXX") == 6
    assert candidate(s = "XOXOOXOXOOXOXOXO") == 4
    assert candidate(s = "OXOOXOOOXOXOOXOO") == 4
    assert candidate(s = "XXOXOXXOXOXOXXOX") == 5
    assert candidate(s = "OOOOOOOOOOOOOOOOOOOOOOOOOOOO") == 0
    assert candidate(s = "XXXXXXXXXXXXXX") == 5


