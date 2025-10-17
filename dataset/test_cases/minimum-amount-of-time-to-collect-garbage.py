def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(garbage = ['M', 'P', 'G', 'M', 'P', 'G'],travel = [1, 2, 3, 4, 5]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['M', 'P', 'G', 'M', 'P', 'G'],travel = [1, 2, 3, 4, 5]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['P', 'G', 'M', 'P'],travel = [1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['P', 'G', 'M', 'P'],travel = [1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GGG', 'PPP', 'MMM', 'GGG', 'PPP', 'MMM'],travel = [10, 10, 10, 10, 10]) == 138
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GGG', 'PPP', 'MMM', 'GGG', 'PPP', 'MMM'],travel = [10, 10, 10, 10, 10]) == 138: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G'],travel = []) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G'],travel = []) == 1: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'P', 'M'],travel = [1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'P', 'M'],travel = [1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['', 'G', '', 'M', 'P'],travel = [2, 3, 2, 5]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['', 'G', '', 'M', 'P'],travel = [2, 3, 2, 5]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['M', 'P', 'G'],travel = [1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['M', 'P', 'G'],travel = [1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GGGG', 'MM', 'PP', 'GG'],travel = [5, 5, 5]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GGGG', 'MM', 'PP', 'GG'],travel = [5, 5, 5]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GGP', 'GGP', 'GGP', 'GGP'],travel = [2, 2, 2]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GGP', 'GGP', 'GGP', 'GGP'],travel = [2, 2, 2]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['', '', '', '', ''],travel = [1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['', '', '', '', ''],travel = [1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['P', 'M', 'G'],travel = [1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['P', 'M', 'G'],travel = [1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['M', 'M', 'M', 'M', 'M'],travel = [1, 1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['M', 'M', 'M', 'M', 'M'],travel = [1, 1, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['', '', '', ''],travel = [1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['', '', '', ''],travel = [1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'P', 'GP', 'GG'],travel = [2, 4, 3]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'P', 'GP', 'GG'],travel = [2, 4, 3]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MMM', 'PGM', 'GP'],travel = [3, 10]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MMM', 'PGM', 'GP'],travel = [3, 10]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GMP', 'GMP', 'GMP'],travel = [10, 10]) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GMP', 'GMP', 'GMP'],travel = [10, 10]) == 69: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MG', 'GP', 'PM', 'MG'],travel = [3, 4, 2]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MG', 'GP', 'PM', 'MG'],travel = [3, 4, 2]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MG', 'GP', 'MM', 'PG', 'GG'],travel = [2, 3, 1, 5]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MG', 'GP', 'MM', 'PG', 'GG'],travel = [2, 3, 1, 5]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MGP', 'MGP', 'MGP', 'MGP'],travel = [5, 5, 5]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MGP', 'MGP', 'MGP', 'MGP'],travel = [5, 5, 5]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GGG', 'MMM', 'PPP'],travel = [5, 5]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GGG', 'MMM', 'PPP'],travel = [5, 5]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GP', 'GP', 'GP', 'GP'],travel = [1, 1, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GP', 'GP', 'GP', 'GP'],travel = [1, 1, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GP', 'MM', 'GG', 'PP', 'GG'],travel = [5, 2, 4, 3]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GP', 'MM', 'GG', 'PP', 'GG'],travel = [5, 2, 4, 3]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['P', 'G', 'M'],travel = [1, 2]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['P', 'G', 'M'],travel = [1, 2]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'M', 'P', '', '', 'G', 'P', 'M', ''],travel = [1, 1, 1, 1, 1, 1, 1, 1]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'M', 'P', '', '', 'G', 'P', 'M', ''],travel = [1, 1, 1, 1, 1, 1, 1, 1]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'P', 'M', 'GP', 'MG', 'PG', 'GMP', 'MGP', 'PMG', 'G'],travel = [2, 3, 1, 5, 4, 2, 3, 1, 4]) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'P', 'M', 'GP', 'MG', 'PG', 'GMP', 'MGP', 'PMG', 'G'],travel = [2, 3, 1, 5, 4, 2, 3, 1, 4]) == 86: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [2, 2, 2, 2, 2, 2, 2, 2]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [2, 2, 2, 2, 2, 2, 2, 2]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'P', 'M', 'GP', 'GM', 'MP', 'PGM', 'MGP', 'GMP', 'PGMG', 'GMPG', 'MPGM'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 228
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'P', 'M', 'GP', 'GM', 'MP', 'PGM', 'MGP', 'GMP', 'PGMG', 'GMPG', 'MPGM'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 228: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MPG', 'G', 'M', 'P', 'G', 'M', 'P', 'G'],travel = [10, 20, 30, 40, 50, 60, 70]) == 650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MPG', 'G', 'M', 'P', 'G', 'M', 'P', 'G'],travel = [10, 20, 30, 40, 50, 60, 70]) == 650: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GGG', 'PPP', 'MMM', 'GPM', 'GPM', 'GPM', 'GPM'],travel = [2, 2, 2, 2, 2, 2]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GGG', 'PPP', 'MMM', 'GPM', 'GPM', 'GPM', 'GPM'],travel = [2, 2, 2, 2, 2, 2]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GGP', 'PGM', 'MG', 'PG', 'GM', 'MP', 'GG', 'PP', 'MM'],travel = [3, 3, 3, 3, 3, 3, 3, 3]) == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GGP', 'PGM', 'MG', 'PG', 'GM', 'MP', 'GG', 'PP', 'MM'],travel = [3, 3, 3, 3, 3, 3, 3, 3]) == 83: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 2, 1, 2, 1, 2, 1, 2]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 2, 1, 2, 1, 2, 1, 2]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GGGPPPMMM', 'GGGPPPMMM', 'GGGPPPMMM', 'GGGPPPMMM'],travel = [10, 10, 10]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GGGPPPMMM', 'GGGPPPMMM', 'GGGPPPMMM', 'GGGPPPMMM'],travel = [10, 10, 10]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['', 'G', 'P', 'M', '', 'GP', 'MG', '', '', 'MG'],travel = [2, 1, 4, 2, 1, 5, 2, 1, 1]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['', 'G', 'P', 'M', '', 'GP', 'MG', '', '', 'MG'],travel = [2, 1, 4, 2, 1, 5, 2, 1, 1]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['M', 'G', 'P', 'MG', 'PG', 'GM', 'GMP', 'P', 'M'],travel = [2, 3, 1, 4, 2, 3, 1, 2]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['M', 'G', 'P', 'MG', 'PG', 'GM', 'GMP', 'P', 'M'],travel = [2, 3, 1, 4, 2, 3, 1, 2]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'M', 'P', 'G', 'M', 'P', 'G', 'M', 'P', 'G', 'M', 'P', 'G', 'M', 'P'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 289
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'M', 'P', 'G', 'M', 'P', 'G', 'M', 'P', 'G', 'M', 'P', 'G', 'M', 'P'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 289: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['M', 'P', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 146
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['M', 'P', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 146: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GGG', 'PPP', 'MMM', 'GGG', 'PPP', 'MMM', 'GGG', 'PPP', 'MMM'],travel = [10, 20, 30, 10, 20, 30, 10, 20]) == 427
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GGG', 'PPP', 'MMM', 'GGG', 'PPP', 'MMM', 'GGG', 'PPP', 'MMM'],travel = [10, 20, 30, 10, 20, 30, 10, 20]) == 427: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MP', 'GP', 'MG', 'PG', 'GM', 'PM', 'MG', 'PG', 'GM', 'PM'],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MP', 'GP', 'MG', 'PG', 'GM', 'PM', 'MG', 'PG', 'GM', 'PM'],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MGP', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'MGP'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MGP', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'MGP'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 58: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP'],travel = [2, 2, 2, 2, 2, 2, 2]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP'],travel = [2, 2, 2, 2, 2, 2, 2]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GMPGMP', 'PMPMPM', 'MGMGMG', 'PGPGPG', 'GMPGMP', 'PMPMPM', 'MGMGMG', 'PGPGPG'],travel = [15, 15, 15, 15, 15, 15, 15]) == 348
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GMPGMP', 'PMPMPM', 'MGMGMG', 'PGPGPG', 'GMPGMP', 'PMPMPM', 'MGMGMG', 'PGPGPG'],travel = [15, 15, 15, 15, 15, 15, 15]) == 348: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'M', 'P', 'G', 'M', 'P', 'G', 'M', 'P'],travel = [1, 2, 3, 4, 5, 6, 7, 8]) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'M', 'P', 'G', 'M', 'P', 'G', 'M', 'P'],travel = [1, 2, 3, 4, 5, 6, 7, 8]) == 94: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['PG', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['PG', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 112: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GMM', 'GGP', 'PPP', 'MMM', 'GGG', 'PPP', 'MMM'],travel = [7, 8, 9, 10, 11, 12]) == 157
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GMM', 'GGP', 'PPP', 'MMM', 'GGG', 'PPP', 'MMM'],travel = [7, 8, 9, 10, 11, 12]) == 157: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GMM', 'GGP', 'PPP', 'MMM', 'GGG', 'PPP', 'MMM', 'GPP', 'MG', 'PGM', 'PG', 'GM', 'MP', 'PGM', 'GMP'],travel = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 608
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GMM', 'GGP', 'PPP', 'MMM', 'GGG', 'PPP', 'MMM', 'GPP', 'MG', 'PGM', 'PG', 'GM', 'MP', 'PGM', 'GMP'],travel = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 608: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['', '', '', '', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['', '', '', '', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GGGG', 'PPPP', 'MMMM', 'PPPP', 'GGGG', 'MMMM'],travel = [3, 4, 5, 6, 7]) == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GGGG', 'PPPP', 'MMMM', 'PPPP', 'GGGG', 'MMMM'],travel = [3, 4, 5, 6, 7]) == 79: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'P', 'M', 'GP', 'MG', 'PG', 'GMP', 'MGP', 'PMG', 'G', 'P', 'M', 'GP', 'MG', 'PG', 'GMP', 'MGP', 'PMG', 'G'],travel = [2, 3, 1, 5, 4, 2, 3, 1, 4, 2, 3, 1, 5, 4, 2, 3, 1, 4]) == 179
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'P', 'M', 'GP', 'MG', 'PG', 'GMP', 'MGP', 'PMG', 'G', 'P', 'M', 'GP', 'MG', 'PG', 'GMP', 'MGP', 'PMG', 'G'],travel = [2, 3, 1, 5, 4, 2, 3, 1, 4, 2, 3, 1, 5, 4, 2, 3, 1, 4]) == 179: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GP', 'MG', 'PM', 'MG', 'PM', 'MG', 'PM', 'MG', 'PM', 'MG'],travel = [5, 10, 5, 10, 5, 10, 5, 10, 5]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GP', 'MG', 'PM', 'MG', 'PM', 'MG', 'PM', 'MG', 'PM', 'MG'],travel = [5, 10, 5, 10, 5, 10, 5, 10, 5]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['P', 'M', 'G', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['P', 'M', 'G', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 130: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GMP', 'P', 'G', 'M', 'P', 'G', 'M', 'P', 'G', 'M'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GMP', 'P', 'G', 'M', 'P', 'G', 'M', 'P', 'G', 'M'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 121: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MPG', 'PGM', 'GMP', 'MGP', 'GPM', 'PGM', 'GMP', 'MGP', 'GPM', 'PGM'],travel = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == 705
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MPG', 'PGM', 'GMP', 'MGP', 'GPM', 'PGM', 'GMP', 'MGP', 'GPM', 'PGM'],travel = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == 705: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['', '', '', '', '', '', '', '', '', 'MGP'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['', '', '', '', '', '', '', '', '', 'MGP'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'M', 'P', 'G', 'M', 'P', 'G', 'M', 'P', 'G'],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'M', 'P', 'G', 'M', 'P', 'G', 'M', 'P', 'G'],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 130: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MGP', 'G', 'P', 'M', 'GP', 'MG', 'PG', 'GM', 'PM'],travel = [10, 5, 7, 6, 8, 9, 2, 3]) == 163
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MGP', 'G', 'P', 'M', 'GP', 'MG', 'PG', 'GM', 'PM'],travel = [10, 5, 7, 6, 8, 9, 2, 3]) == 163: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MMM', 'GGG', 'PPP', 'MMM', 'GGG', 'PPP', 'MMM'],travel = [5, 5, 5, 5, 5, 5]) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MMM', 'GGG', 'PPP', 'MMM', 'GGG', 'PPP', 'MMM'],travel = [5, 5, 5, 5, 5, 5]) == 96: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 513
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 513: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MMG', 'PG', 'MM', 'GGG', 'PP', 'G'],travel = [3, 5, 2, 6, 4]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MMG', 'PG', 'MM', 'GGG', 'PP', 'G'],travel = [3, 5, 2, 6, 4]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GGGG', 'PPPP', 'MMMM', 'GGGG', 'PPPP', 'MMMM'],travel = [1, 2, 3, 4, 5]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GGGG', 'PPPP', 'MMMM', 'GGGG', 'PPPP', 'MMMM'],travel = [1, 2, 3, 4, 5]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'M', 'P', 'GM', 'PG', 'MG', 'GPM', 'PMG', 'MPG', 'GMP'],travel = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 183
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'M', 'P', 'GM', 'PG', 'MG', 'GPM', 'PMG', 'MPG', 'GMP'],travel = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 183: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MGP', '', 'MGP', '', 'MGP', '', 'MGP'],travel = [2, 2, 2, 2, 2, 2]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MGP', '', 'MGP', '', 'MGP', '', 'MGP'],travel = [2, 2, 2, 2, 2, 2]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MGP', 'GP', 'MGG', 'PGG', 'MMM', 'GGP', 'PGM'],travel = [3, 5, 2, 4, 6, 7]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MGP', 'GP', 'MGG', 'PGG', 'MMM', 'GGP', 'PGM'],travel = [3, 5, 2, 4, 6, 7]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP'],travel = [10, 10, 10, 10, 10, 10, 10, 10, 10]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP'],travel = [10, 10, 10, 10, 10, 10, 10, 10, 10]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MMMGGGPPP', 'MMMGGGPPP', 'MMMGGGPPP', 'MMMGGGPPP'],travel = [15, 15, 15]) == 171
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MMMGGGPPP', 'MMMGGGPPP', 'MMMGGGPPP', 'MMMGGGPPP'],travel = [15, 15, 15]) == 171: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['', '', '', '', '', '', '', '', '', '', 'PGM'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['', '', '', '', '', '', '', '', '', '', 'PGM'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 168: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GMP', 'GMP', 'GMP', '', '', '', 'GMP', '', '', 'GMP', 'GMP', 'GMP', '', '', '', 'GMP', 'GMP', 'GMP', ''],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GMP', 'GMP', 'GMP', '', '', '', 'GMP', '', '', 'GMP', 'GMP', 'GMP', '', '', '', 'GMP', 'GMP', 'GMP', ''],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 285: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['', '', '', '', '', '', '', ''],travel = [1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['', '', '', '', '', '', '', ''],travel = [1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MGPG', 'GPMP', 'PGMG', 'P', 'M', 'G', 'MGP', 'P', 'G', 'MP'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 148
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MGPG', 'GPMP', 'PGMG', 'P', 'M', 'G', 'MGP', 'P', 'G', 'MP'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 148: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['', '', 'MGP', '', '', '', '', '', '', 'MGP'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['', '', 'MGP', '', '', '', '', '', '', 'MGP'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 141: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MPG', 'G', 'P', 'M', 'PG', 'GM', 'PGM'],travel = [7, 3, 8, 2, 5, 6]) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MPG', 'G', 'P', 'M', 'PG', 'GM', 'PGM'],travel = [7, 3, 8, 2, 5, 6]) == 106: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 382
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 382: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MMM', 'MMM', 'MMM', 'MMM', 'MMM'],travel = [10, 10, 10, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MMM', 'MMM', 'MMM', 'MMM', 'MMM'],travel = [10, 10, 10, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['', 'MGP', '', 'P', 'G', 'MP', '', 'MGP', '', 'P', 'G', 'MP', '', 'MGP', ''],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['', 'MGP', '', 'P', 'G', 'MP', '', 'MGP', '', 'P', 'G', 'MP', '', 'MGP', ''],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 290: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GMP', 'P', 'M', 'G', 'MPG', 'MG', 'PG', 'GMP', 'GMP', 'P'],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GMP', 'P', 'M', 'G', 'MPG', 'MG', 'PG', 'GMP', 'GMP', 'P'],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 145: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GP', 'GP', 'GP', 'GP', 'GP', 'GP', 'GP'],travel = [1, 1, 1, 1, 1, 1]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GP', 'GP', 'GP', 'GP', 'GP', 'GP', 'GP'],travel = [1, 1, 1, 1, 1, 1]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MMM', 'PPP', 'GGG', 'MMM', 'PPP', 'GGG', 'MMM', 'PPP', 'GGG'],travel = [10, 10, 10, 10, 10, 10, 10, 10]) == 237
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MMM', 'PPP', 'GGG', 'MMM', 'PPP', 'GGG', 'MMM', 'PPP', 'GGG'],travel = [10, 10, 10, 10, 10, 10, 10, 10]) == 237: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MG', 'PGP', 'GGM', 'PPG', 'MMG'],travel = [3, 5, 2, 7]) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MG', 'PGP', 'GGM', 'PPG', 'MMG'],travel = [3, 5, 2, 7]) == 58: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MMM', '', 'GG', '', '', 'P', '', 'G'],travel = [10, 2, 3, 4, 5, 6, 7]) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MMM', '', 'GG', '', '', 'P', '', 'G'],travel = [10, 2, 3, 4, 5, 6, 7]) == 68: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM'],travel = [10, 10, 10, 10, 10, 10, 10, 10]) == 107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM'],travel = [10, 10, 10, 10, 10, 10, 10, 10]) == 107: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP'],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP'],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'P', 'M', 'G', '', 'P', 'M', 'G', '', 'P', 'M', 'G', '', 'P', 'M', 'G', '', 'P', 'M', 'G'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'P', 'M', 'G', '', 'P', 'M', 'G', '', 'P', 'M', 'G', '', 'P', 'M', 'G', '', 'P', 'M', 'G'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 2, 3, 4, 5, 6, 7, 8]) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 2, 3, 4, 5, 6, 7, 8]) == 94: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'P', 'M', '', 'G', 'P', 'M', ''],travel = [1, 2, 3, 4, 5, 6, 7]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'P', 'M', '', 'G', 'P', 'M', ''],travel = [1, 2, 3, 4, 5, 6, 7]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG'],travel = [5, 5, 5, 5, 5, 5, 5]) == 129
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG'],travel = [5, 5, 5, 5, 5, 5, 5]) == 129: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MGP', 'MGP', '', '', '', '', '', 'MGP', 'MGP', 'MGP', '', '', '', '', 'MGP'],travel = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 228
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MGP', 'MGP', '', '', '', '', '', 'MGP', 'MGP', 'MGP', '', '', '', '', 'MGP'],travel = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 228: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['', '', '', '', '', '', '', '', '', 'G'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['', '', '', '', '', '', '', '', '', 'G'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 427
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 427: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MMMM', 'PPPP', 'GGGG', 'MMMM', 'PPPP', 'GGGG'],travel = [10, 10, 10, 10, 10]) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MMMM', 'PPPP', 'GGGG', 'MMMM', 'PPPP', 'GGGG'],travel = [10, 10, 10, 10, 10]) == 144: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MMM', 'PPP', 'GGG', 'MMM', 'PPP', 'GGG', 'MMM'],travel = [10, 10, 10, 10, 10, 10]) == 171
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MMM', 'PPP', 'GGG', 'MMM', 'PPP', 'GGG', 'MMM'],travel = [10, 10, 10, 10, 10, 10]) == 171: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 69: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MMM', 'GGG', 'PPP', 'MGP', 'GMP', 'PMM', 'GGP', 'PPG', 'MPM', 'MGP'],travel = [10, 20, 15, 10, 5, 12, 8, 18, 7]) == 345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MMM', 'GGG', 'PPP', 'MGP', 'GMP', 'PMM', 'GGP', 'PPG', 'MPM', 'MGP'],travel = [10, 20, 15, 10, 5, 12, 8, 18, 7]) == 345: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['M', 'P', 'G', 'MPG', 'GMP', 'PGM'],travel = [1, 3, 2, 4, 5]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['M', 'P', 'G', 'MPG', 'GMP', 'PGM'],travel = [1, 3, 2, 4, 5]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MGP', '', '', 'MGP', '', '', 'MGP', '', '', 'MGP'],travel = [2, 1, 3, 2, 1, 3, 2, 1, 3]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MGP', '', '', 'MGP', '', '', 'MGP', '', '', 'MGP'],travel = [2, 1, 3, 2, 1, 3, 2, 1, 3]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['M', 'P', 'G', 'MP', 'PG', 'GM', 'MG', 'PGM'],travel = [2, 3, 1, 4, 5, 6]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['M', 'P', 'G', 'MP', 'PG', 'GM', 'MG', 'PGM'],travel = [2, 3, 1, 4, 5, 6]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 115: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['MGP', 'MG', 'P', 'G', 'MP', 'GM', 'PG', 'MG', 'PGM'],travel = [5, 5, 5, 5, 5, 5, 5, 5]) == 138
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['MGP', 'MG', 'P', 'G', 'MP', 'GM', 'PG', 'MG', 'PGM'],travel = [5, 5, 5, 5, 5, 5, 5, 5]) == 138: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', '', 'P', '', 'M', '', 'G', '', 'P', '', 'M'],travel = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', '', 'P', '', 'M', '', 'G', '', 'P', '', 'M'],travel = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 289
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 289: {e}')
    
    total += 1
    try:
        result = candidate(garbage = ['G', 'P', 'M', 'PG', 'GM', 'MP', 'PGM'],travel = [1, 2, 3, 4, 5, 6]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(garbage = ['G', 'P', 'M', 'PG', 'GM', 'MP', 'PGM'],travel = [1, 2, 3, 4, 5, 6]) == 75: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(garbage = ['M', 'P', 'G', 'M', 'P', 'G'],travel = [1, 2, 3, 4, 5]) == 37
    assert candidate(garbage = ['P', 'G', 'M', 'P'],travel = [1, 1, 1]) == 10
    assert candidate(garbage = ['GGG', 'PPP', 'MMM', 'GGG', 'PPP', 'MMM'],travel = [10, 10, 10, 10, 10]) == 138
    assert candidate(garbage = ['G'],travel = []) == 1
    assert candidate(garbage = ['G', 'P', 'M'],travel = [1, 1]) == 6
    assert candidate(garbage = ['', 'G', '', 'M', 'P'],travel = [2, 3, 2, 5]) == 24
    assert candidate(garbage = ['M', 'P', 'G'],travel = [1, 1]) == 6
    assert candidate(garbage = ['GGGG', 'MM', 'PP', 'GG'],travel = [5, 5, 5]) == 40
    assert candidate(garbage = ['GGP', 'GGP', 'GGP', 'GGP'],travel = [2, 2, 2]) == 24
    assert candidate(garbage = ['', '', '', '', ''],travel = [1, 1, 1, 1]) == 0
    assert candidate(garbage = ['P', 'M', 'G'],travel = [1]) == 4
    assert candidate(garbage = ['M', 'M', 'M', 'M', 'M'],travel = [1, 1, 1, 1]) == 9
    assert candidate(garbage = ['', '', '', ''],travel = [1, 1, 1]) == 0
    assert candidate(garbage = ['G', 'P', 'GP', 'GG'],travel = [2, 4, 3]) == 21
    assert candidate(garbage = ['MMM', 'PGM', 'GP'],travel = [3, 10]) == 37
    assert candidate(garbage = ['GMP', 'GMP', 'GMP'],travel = [10, 10]) == 69
    assert candidate(garbage = ['MG', 'GP', 'PM', 'MG'],travel = [3, 4, 2]) == 33
    assert candidate(garbage = ['MG', 'GP', 'MM', 'PG', 'GG'],travel = [2, 3, 1, 5]) == 32
    assert candidate(garbage = ['MGP', 'MGP', 'MGP', 'MGP'],travel = [5, 5, 5]) == 57
    assert candidate(garbage = ['GGG', 'MMM', 'PPP'],travel = [5, 5]) == 24
    assert candidate(garbage = ['GP', 'GP', 'GP', 'GP'],travel = [1, 1, 1]) == 14
    assert candidate(garbage = ['GP', 'MM', 'GG', 'PP', 'GG'],travel = [5, 2, 4, 3]) == 40
    assert candidate(garbage = ['P', 'G', 'M'],travel = [1, 2]) == 7
    assert candidate(garbage = ['G', 'M', 'P', '', '', 'G', 'P', 'M', ''],travel = [1, 1, 1, 1, 1, 1, 1, 1]) == 24
    assert candidate(garbage = ['G', 'P', 'M', 'GP', 'MG', 'PG', 'GMP', 'MGP', 'PMG', 'G'],travel = [2, 3, 1, 5, 4, 2, 3, 1, 4]) == 86
    assert candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [2, 2, 2, 2, 2, 2, 2, 2]) == 51
    assert candidate(garbage = ['G', 'P', 'M', 'GP', 'GM', 'MP', 'PGM', 'MGP', 'GMP', 'PGMG', 'GMPG', 'MPGM'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 228
    assert candidate(garbage = ['MPG', 'G', 'M', 'P', 'G', 'M', 'P', 'G'],travel = [10, 20, 30, 40, 50, 60, 70]) == 650
    assert candidate(garbage = ['GGG', 'PPP', 'MMM', 'GPM', 'GPM', 'GPM', 'GPM'],travel = [2, 2, 2, 2, 2, 2]) == 57
    assert candidate(garbage = ['GGP', 'PGM', 'MG', 'PG', 'GM', 'MP', 'GG', 'PP', 'MM'],travel = [3, 3, 3, 3, 3, 3, 3, 3]) == 83
    assert candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 2, 1, 2, 1, 2, 1, 2]) == 40
    assert candidate(garbage = ['GGGPPPMMM', 'GGGPPPMMM', 'GGGPPPMMM', 'GGGPPPMMM'],travel = [10, 10, 10]) == 126
    assert candidate(garbage = ['', 'G', 'P', 'M', '', 'GP', 'MG', '', '', 'MG'],travel = [2, 1, 4, 2, 1, 5, 2, 1, 1]) == 57
    assert candidate(garbage = ['M', 'G', 'P', 'MG', 'PG', 'GM', 'GMP', 'P', 'M'],travel = [2, 3, 1, 4, 2, 3, 1, 2]) == 63
    assert candidate(garbage = ['G', 'M', 'P', 'G', 'M', 'P', 'G', 'M', 'P', 'G', 'M', 'P', 'G', 'M', 'P'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 289
    assert candidate(garbage = ['M', 'P', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 146
    assert candidate(garbage = ['GGG', 'PPP', 'MMM', 'GGG', 'PPP', 'MMM', 'GGG', 'PPP', 'MMM'],travel = [10, 20, 30, 10, 20, 30, 10, 20]) == 427
    assert candidate(garbage = ['MP', 'GP', 'MG', 'PG', 'GM', 'PM', 'MG', 'PG', 'GM', 'PM'],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 150
    assert candidate(garbage = ['MGP', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'MGP'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 6
    assert candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 58
    assert candidate(garbage = ['MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP'],travel = [2, 2, 2, 2, 2, 2, 2]) == 66
    assert candidate(garbage = ['MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 39
    assert candidate(garbage = ['GMPGMP', 'PMPMPM', 'MGMGMG', 'PGPGPG', 'GMPGMP', 'PMPMPM', 'MGMGMG', 'PGPGPG'],travel = [15, 15, 15, 15, 15, 15, 15]) == 348
    assert candidate(garbage = ['G', 'M', 'P', 'G', 'M', 'P', 'G', 'M', 'P'],travel = [1, 2, 3, 4, 5, 6, 7, 8]) == 94
    assert candidate(garbage = ['PG', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 112
    assert candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 66
    assert candidate(garbage = ['GMM', 'GGP', 'PPP', 'MMM', 'GGG', 'PPP', 'MMM'],travel = [7, 8, 9, 10, 11, 12]) == 157
    assert candidate(garbage = ['GMM', 'GGP', 'PPP', 'MMM', 'GGG', 'PPP', 'MMM', 'GPP', 'MG', 'PGM', 'PG', 'GM', 'MP', 'PGM', 'GMP'],travel = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 608
    assert candidate(garbage = ['', '', '', '', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 45
    assert candidate(garbage = ['GGGG', 'PPPP', 'MMMM', 'PPPP', 'GGGG', 'MMMM'],travel = [3, 4, 5, 6, 7]) == 79
    assert candidate(garbage = ['G', 'P', 'M', 'GP', 'MG', 'PG', 'GMP', 'MGP', 'PMG', 'G', 'P', 'M', 'GP', 'MG', 'PG', 'GMP', 'MGP', 'PMG', 'G'],travel = [2, 3, 1, 5, 4, 2, 3, 1, 4, 2, 3, 1, 5, 4, 2, 3, 1, 4]) == 179
    assert candidate(garbage = ['GP', 'MG', 'PM', 'MG', 'PM', 'MG', 'PM', 'MG', 'PM', 'MG'],travel = [5, 10, 5, 10, 5, 10, 5, 10, 5]) == 210
    assert candidate(garbage = ['P', 'M', 'G', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 130
    assert candidate(garbage = ['GMP', 'P', 'G', 'M', 'P', 'G', 'M', 'P', 'G', 'M'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 121
    assert candidate(garbage = ['MPG', 'PGM', 'GMP', 'MGP', 'GPM', 'PGM', 'GMP', 'MGP', 'GPM', 'PGM'],travel = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == 705
    assert candidate(garbage = ['', '', '', '', '', '', '', '', '', 'MGP'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30
    assert candidate(garbage = ['G', 'M', 'P', 'G', 'M', 'P', 'G', 'M', 'P', 'G'],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 130
    assert candidate(garbage = ['MGP', 'G', 'P', 'M', 'GP', 'MG', 'PG', 'GM', 'PM'],travel = [10, 5, 7, 6, 8, 9, 2, 3]) == 163
    assert candidate(garbage = ['MMM', 'GGG', 'PPP', 'MMM', 'GGG', 'PPP', 'MMM'],travel = [5, 5, 5, 5, 5, 5]) == 96
    assert candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 42
    assert candidate(garbage = ['GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 513
    assert candidate(garbage = ['MMG', 'PG', 'MM', 'GGG', 'PP', 'G'],travel = [3, 5, 2, 6, 4]) == 57
    assert candidate(garbage = ['GGGG', 'PPPP', 'MMMM', 'GGGG', 'PPPP', 'MMMM'],travel = [1, 2, 3, 4, 5]) == 55
    assert candidate(garbage = ['G', 'M', 'P', 'GM', 'PG', 'MG', 'GPM', 'PMG', 'MPG', 'GMP'],travel = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 183
    assert candidate(garbage = ['MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 165
    assert candidate(garbage = ['MGP', '', 'MGP', '', 'MGP', '', 'MGP'],travel = [2, 2, 2, 2, 2, 2]) == 48
    assert candidate(garbage = ['MGP', 'GP', 'MGG', 'PGG', 'MMM', 'GGP', 'PGM'],travel = [3, 5, 2, 4, 6, 7]) == 101
    assert candidate(garbage = ['MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP'],travel = [10, 10, 10, 10, 10, 10, 10, 10, 10]) == 300
    assert candidate(garbage = ['MMMGGGPPP', 'MMMGGGPPP', 'MMMGGGPPP', 'MMMGGGPPP'],travel = [15, 15, 15]) == 171
    assert candidate(garbage = ['', '', '', '', '', '', '', '', '', '', 'PGM'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 168
    assert candidate(garbage = ['GMP', 'GMP', 'GMP', '', '', '', 'GMP', '', '', 'GMP', 'GMP', 'GMP', '', '', '', 'GMP', 'GMP', 'GMP', ''],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 285
    assert candidate(garbage = ['', '', '', '', '', '', '', ''],travel = [1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(garbage = ['MGPG', 'GPMP', 'PGMG', 'P', 'M', 'G', 'MGP', 'P', 'G', 'MP'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 148
    assert candidate(garbage = ['', '', 'MGP', '', '', '', '', '', '', 'MGP'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 141
    assert candidate(garbage = ['MPG', 'G', 'P', 'M', 'PG', 'GM', 'PGM'],travel = [7, 3, 8, 2, 5, 6]) == 106
    assert candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 382
    assert candidate(garbage = ['MMM', 'MMM', 'MMM', 'MMM', 'MMM'],travel = [10, 10, 10, 10]) == 55
    assert candidate(garbage = ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 21
    assert candidate(garbage = ['', 'MGP', '', 'P', 'G', 'MP', '', 'MGP', '', 'P', 'G', 'MP', '', 'MGP', ''],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 290
    assert candidate(garbage = ['GMP', 'P', 'M', 'G', 'MPG', 'MG', 'PG', 'GMP', 'GMP', 'P'],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 145
    assert candidate(garbage = ['GP', 'GP', 'GP', 'GP', 'GP', 'GP', 'GP'],travel = [1, 1, 1, 1, 1, 1]) == 26
    assert candidate(garbage = ['MMM', 'PPP', 'GGG', 'MMM', 'PPP', 'GGG', 'MMM', 'PPP', 'GGG'],travel = [10, 10, 10, 10, 10, 10, 10, 10]) == 237
    assert candidate(garbage = ['MG', 'PGP', 'GGM', 'PPG', 'MMG'],travel = [3, 5, 2, 7]) == 58
    assert candidate(garbage = ['MMM', '', 'GG', '', '', 'P', '', 'G'],travel = [10, 2, 3, 4, 5, 6, 7]) == 68
    assert candidate(garbage = ['MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM', 'MMM'],travel = [10, 10, 10, 10, 10, 10, 10, 10]) == 107
    assert candidate(garbage = ['GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP', 'GMP'],travel = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 165
    assert candidate(garbage = ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19
    assert candidate(garbage = ['G', 'P', 'M', 'G', '', 'P', 'M', 'G', '', 'P', 'M', 'G', '', 'P', 'M', 'G', '', 'P', 'M', 'G'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 51
    assert candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 2, 3, 4, 5, 6, 7, 8]) == 94
    assert candidate(garbage = ['G', 'P', 'M', '', 'G', 'P', 'M', ''],travel = [1, 2, 3, 4, 5, 6, 7]) == 52
    assert candidate(garbage = ['MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG'],travel = [5, 5, 5, 5, 5, 5, 5]) == 129
    assert candidate(garbage = ['MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG', 'MPG'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 57
    assert candidate(garbage = ['MGP', 'MGP', '', '', '', '', '', 'MGP', 'MGP', 'MGP', '', '', '', '', 'MGP'],travel = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 228
    assert candidate(garbage = ['', '', '', '', '', '', '', '', '', 'G'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 427
    assert candidate(garbage = ['MMMM', 'PPPP', 'GGGG', 'MMMM', 'PPPP', 'GGGG'],travel = [10, 10, 10, 10, 10]) == 144
    assert candidate(garbage = ['MMM', 'PPP', 'GGG', 'MMM', 'PPP', 'GGG', 'MMM'],travel = [10, 10, 10, 10, 10, 10]) == 171
    assert candidate(garbage = ['MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP', 'MGP'],travel = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 69
    assert candidate(garbage = ['MMM', 'GGG', 'PPP', 'MGP', 'GMP', 'PMM', 'GGP', 'PPG', 'MPM', 'MGP'],travel = [10, 20, 15, 10, 5, 12, 8, 18, 7]) == 345
    assert candidate(garbage = ['M', 'P', 'G', 'MPG', 'GMP', 'PGM'],travel = [1, 3, 2, 4, 5]) == 57
    assert candidate(garbage = ['MGP', '', '', 'MGP', '', '', 'MGP', '', '', 'MGP'],travel = [2, 1, 3, 2, 1, 3, 2, 1, 3]) == 66
    assert candidate(garbage = ['M', 'P', 'G', 'MP', 'PG', 'GM', 'MG', 'PGM'],travel = [2, 3, 1, 4, 5, 6]) == 14
    assert candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 115
    assert candidate(garbage = ['MGP', 'MG', 'P', 'G', 'MP', 'GM', 'PG', 'MG', 'PGM'],travel = [5, 5, 5, 5, 5, 5, 5, 5]) == 138
    assert candidate(garbage = ['G', '', 'P', '', 'M', '', 'G', '', 'P', '', 'M'],travel = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 42
    assert candidate(garbage = ['G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M', 'G', 'P', 'M'],travel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 289
    assert candidate(garbage = ['G', 'P', 'M', 'PG', 'GM', 'MP', 'PGM'],travel = [1, 2, 3, 4, 5, 6]) == 75


