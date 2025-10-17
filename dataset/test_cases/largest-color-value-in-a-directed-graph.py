def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(colors = "abcde",edges = []) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcde",edges = []) == 1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcdefghijklmnopqrstuvwxyz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcdefghijklmnopqrstuvwxyz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "zzz",edges = [[0, 1], [1, 2], [2, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "zzz",edges = [[0, 1], [1, 2], [2, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abacabadabacaba",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abacabadabacaba",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(colors = "aaaaa",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "aaaaa",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcdef",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcdef",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcde",edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcde",edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcdef",edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcdef",edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcde",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcde",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "aaaaa",edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "aaaaa",edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(colors = "xyzz",edges = [[0, 1], [1, 2], [2, 3]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "xyzz",edges = [[0, 1], [1, 2], [2, 3]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcabc",edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcabc",edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcdabcdabcd",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcdabcdabcd",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(colors = "xyz",edges = [[0, 1], [1, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "xyz",edges = [[0, 1], [1, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "aabbcc",edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "aabbcc",edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcabcabc",edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcabcabc",edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "aabbcc",edges = [[0, 1], [2, 3], [4, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "aabbcc",edges = [[0, 1], [2, 3], [4, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(colors = "aaabbb",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "aaabbb",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(colors = "zzzzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "zzzzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "aaaa",edges = [[0, 1], [1, 2], [2, 3], [3, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "aaaa",edges = [[0, 1], [1, 2], [2, 3], [3, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "aabbcc",edges = [[0, 1], [1, 2], [2, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "aabbcc",edges = [[0, 1], [1, 2], [2, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "a",edges = []) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "a",edges = []) == 1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcd",edges = [[0, 1], [0, 2], [1, 3], [2, 3]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcd",edges = [[0, 1], [0, 2], [1, 3], [2, 3]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "aabbbbcccc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "aabbbbcccc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(colors = "a",edges = [[0, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "a",edges = [[0, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abaca",edges = [[0, 1], [0, 2], [2, 3], [3, 4]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abaca",edges = [[0, 1], [0, 2], [2, 3], [3, 4]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcd",edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [1, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcd",edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [1, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "ab",edges = [[0, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "ab",edges = [[0, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "aabbcc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "aabbcc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(colors = "zzzzzzzzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "zzzzzzzzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [33, 34], [34, 35]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [33, 34], [34, 35]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcabcabcabcabcabcabcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 10]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcabcabcabcabcabcabcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 10]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "zzzzzzzzzzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "zzzzzzzzzzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcbcbc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcbcbc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [33, 34], [34, 35], [35, 36], [36, 37], [37, 38], [38, 39]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [33, 34], [34, 35], [35, 36], [36, 37], [37, 38], [38, 39]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(colors = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcdef",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcdef",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [33, 34], [34, 35], [35, 36], [36, 37], [37, 38], [38, 39], [39, 40], [40, 41], [41, 42], [42, 43], [43, 44], [44, 45], [45, 46], [46, 47], [47, 48], [48, 49]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [33, 34], [34, 35], [35, 36], [36, 37], [37, 38], [38, 39], [39, 40], [40, 41], [41, 42], [42, 43], [43, 44], [44, 45], [45, 46], [46, 47], [47, 48], [48, 49]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abacabadabe",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abacabadabe",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcde",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2], [1, 3], [2, 4], [3, 0], [4, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcde",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2], [1, 3], [2, 4], [3, 0], [4, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "aaaaaaaaaa",edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 8], [6, 8], [7, 9], [8, 9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "aaaaaaaaaa",edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 8], [6, 8], [7, 9], [8, 9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcdef",edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [2, 5], [3, 5], [4, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcdef",edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [2, 5], [3, 5], [4, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "bbaaabbbaaabbbaaabbbaaa",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "bbaaabbbaaabbbaaabbbaaa",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcdefghijklmnopqrstuvwx",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcdefghijklmnopqrstuvwx",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "ababababa",edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "ababababa",edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "xyzxyzxyz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [0, 2], [1, 3], [4, 6], [5, 7]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "xyzxyzxyz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [0, 2], [1, 3], [4, 6], [5, 7]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcde",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [2, 0], [3, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcde",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [2, 0], [3, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcdef",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcdef",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abacabadabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abacabadabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcdefghijk",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcdefghijk",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abacabadabe",edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abacabadabe",edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcabcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 10]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcabcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 10]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "aaabbbccc",edges = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 8], [8, 4], [1, 3], [3, 5], [5, 7]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "aaabbbccc",edges = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 8], [8, 4], [1, 3], [3, 5], [5, 7]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "ababababc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "ababababc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcdefghij",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 0], [9, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcdefghij",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 0], [9, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "zzzzzzzzzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "zzzzzzzzzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "aaaabbbbccccdddd",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "aaaabbbbccccdddd",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(colors = "zzzzzzzzzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "zzzzzzzzzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(colors = "aabbccddeeff",edges = [[0, 1], [0, 5], [1, 2], [1, 3], [2, 4], [3, 4], [5, 6], [5, 7], [6, 8], [7, 8], [8, 9]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "aabbccddeeff",edges = [[0, 1], [0, 5], [1, 2], [1, 3], [2, 4], [3, 4], [5, 6], [5, 7], [6, 8], [7, 8], [8, 9]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abacabadabe",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abacabadabe",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcde",edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [4, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcde",edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [4, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [1, 3], [3, 5], [5, 7]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [1, 3], [3, 5], [5, 7]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcabcabcabcabcabcabcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 28]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcabcabcabcabcabcabcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 28]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abacbacba",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abacbacba",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abacabadabe",edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 8], [6, 8], [7, 9], [8, 9]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abacabadabe",edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 8], [6, 8], [7, 9], [8, 9]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abacabadaba",edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abacabadaba",edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abacabadaba",edges = [[0, 1], [1, 0], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abacabadaba",edges = [[0, 1], [1, 0], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "ababababab",edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 5], [3, 6], [4, 5], [4, 6], [5, 7], [5, 8], [6, 7], [6, 8], [7, 9], [8, 9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "ababababab",edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 5], [3, 6], [4, 5], [4, 6], [5, 7], [5, 8], [6, 7], [6, 8], [7, 9], [8, 9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abacabadaba",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abacabadaba",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcabcabcabcabcabcabcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcabcabcabcabcabcabcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcdefghij",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcdefghij",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abacabadaba",edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abacabadaba",edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(colors = "aabbaabb",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "aabbaabb",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcdefgabcdefgabcdefgabcdefg",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 7]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcdefgabcdefgabcdefgabcdefg",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 7]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "aaabbbcccdddeeefffggghhh",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "aaabbbcccdddeeefffggghhh",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcdefghijk",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcdefghijk",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "aaaabbbbccccdddd",edges = [[0, 1], [0, 4], [1, 2], [1, 5], [2, 3], [2, 6], [3, 7], [4, 5], [4, 8], [5, 6], [5, 9], [6, 7], [6, 10], [7, 11], [8, 9], [8, 12], [9, 10], [9, 13], [10, 11], [10, 14], [11, 15], [12, 13], [13, 14], [14, 15]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "aaaabbbbccccdddd",edges = [[0, 1], [0, 4], [1, 2], [1, 5], [2, 3], [2, 6], [3, 7], [4, 5], [4, 8], [5, 6], [5, 9], [6, 7], [6, 10], [7, 11], [8, 9], [8, 12], [9, 10], [9, 13], [10, 11], [10, 14], [11, 15], [12, 13], [13, 14], [14, 15]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcabcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcabcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abcde",edges = [[0, 1], [0, 2], [2, 1], [1, 3], [2, 3], [3, 4], [4, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abcde",edges = [[0, 1], [0, 2], [2, 1], [1, 3], [2, 3], [3, 4], [4, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(colors = "zzzzzzyyyyy",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "zzzzzzyyyyy",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(colors = "abacabadabacaba",edges = [[0, 1], [0, 2], [2, 3], [3, 4], [1, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(colors = "abacabadabacaba",edges = [[0, 1], [0, 2], [2, 3], [3, 4], [1, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(colors = "abcde",edges = []) == 1
    assert candidate(colors = "abcdefghijklmnopqrstuvwxyz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25]]) == 1
    assert candidate(colors = "zzz",edges = [[0, 1], [1, 2], [2, 0]]) == -1
    assert candidate(colors = "abacabadabacaba",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 8
    assert candidate(colors = "aaaaa",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == -1
    assert candidate(colors = "abcdef",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 1
    assert candidate(colors = "abcde",edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
    assert candidate(colors = "abcdef",edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5]]) == 1
    assert candidate(colors = "abcde",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == -1
    assert candidate(colors = "aaaaa",edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 5
    assert candidate(colors = "xyzz",edges = [[0, 1], [1, 2], [2, 3]]) == 2
    assert candidate(colors = "abcabc",edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3]]) == -1
    assert candidate(colors = "abcdabcdabcd",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 3
    assert candidate(colors = "xyz",edges = [[0, 1], [1, 2]]) == 1
    assert candidate(colors = "aabbcc",edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3]]) == -1
    assert candidate(colors = "abcabcabc",edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3]]) == -1
    assert candidate(colors = "aabbcc",edges = [[0, 1], [2, 3], [4, 5]]) == 2
    assert candidate(colors = "aaabbb",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 3
    assert candidate(colors = "zzzzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == -1
    assert candidate(colors = "aaaa",edges = [[0, 1], [1, 2], [2, 3], [3, 0]]) == -1
    assert candidate(colors = "aabbcc",edges = [[0, 1], [1, 2], [2, 0]]) == -1
    assert candidate(colors = "a",edges = []) == 1
    assert candidate(colors = "abcd",edges = [[0, 1], [0, 2], [1, 3], [2, 3]]) == 1
    assert candidate(colors = "aabbbbcccc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 4
    assert candidate(colors = "abcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 3
    assert candidate(colors = "a",edges = [[0, 0]]) == -1
    assert candidate(colors = "abaca",edges = [[0, 1], [0, 2], [2, 3], [3, 4]]) == 3
    assert candidate(colors = "abcd",edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [1, 3]]) == -1
    assert candidate(colors = "ab",edges = [[0, 1]]) == 1
    assert candidate(colors = "aabbcc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 2
    assert candidate(colors = "zzzzzzzzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0]]) == -1
    assert candidate(colors = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [33, 34], [34, 35]]) == 2
    assert candidate(colors = "abcabcabcabcabcabcabcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 10]]) == -1
    assert candidate(colors = "zzzzzzzzzzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == -1
    assert candidate(colors = "abcbcbc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 2]]) == -1
    assert candidate(colors = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [33, 34], [34, 35], [35, 36], [36, 37], [37, 38], [38, 39]]) == 2
    assert candidate(colors = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 0]]) == -1
    assert candidate(colors = "abcdef",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == -1
    assert candidate(colors = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [33, 34], [34, 35], [35, 36], [36, 37], [37, 38], [38, 39], [39, 40], [40, 41], [41, 42], [42, 43], [43, 44], [44, 45], [45, 46], [46, 47], [47, 48], [48, 49]]) == 2
    assert candidate(colors = "abacabadabe",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == -1
    assert candidate(colors = "abcde",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 2], [1, 3], [2, 4], [3, 0], [4, 1]]) == -1
    assert candidate(colors = "aaaaaaaaaa",edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 8], [6, 8], [7, 9], [8, 9]]) == 5
    assert candidate(colors = "abcdef",edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [2, 5], [3, 5], [4, 5]]) == 1
    assert candidate(colors = "bbaaabbbaaabbbaaabbbaaa",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 8
    assert candidate(colors = "abcdefghijklmnopqrstuvwx",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23]]) == 1
    assert candidate(colors = "ababababa",edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 3]]) == -1
    assert candidate(colors = "xyzxyzxyz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [0, 2], [1, 3], [4, 6], [5, 7]]) == -1
    assert candidate(colors = "abcde",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [2, 0], [3, 1]]) == -1
    assert candidate(colors = "abcdef",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 2]]) == -1
    assert candidate(colors = "abacabadabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 5
    assert candidate(colors = "abcdefghijk",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 0]]) == -1
    assert candidate(colors = "abacabadabe",edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 3]]) == -1
    assert candidate(colors = "abcabcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 10]]) == -1
    assert candidate(colors = "aaabbbccc",edges = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 8], [8, 4], [1, 3], [3, 5], [5, 7]]) == -1
    assert candidate(colors = "ababababc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0]]) == -1
    assert candidate(colors = "abcdefghij",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 0], [9, 1]]) == -1
    assert candidate(colors = "zzzzzzzzzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == -1
    assert candidate(colors = "aaaabbbbccccdddd",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15]]) == 4
    assert candidate(colors = "zzzzzzzzzz",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10
    assert candidate(colors = "aabbccddeeff",edges = [[0, 1], [0, 5], [1, 2], [1, 3], [2, 4], [3, 4], [5, 6], [5, 7], [6, 8], [7, 8], [8, 9]]) == 2
    assert candidate(colors = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 0]]) == -1
    assert candidate(colors = "abacabadabe",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]]) == 5
    assert candidate(colors = "abcde",edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [4, 0]]) == -1
    assert candidate(colors = "abcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [1, 3], [3, 5], [5, 7]]) == -1
    assert candidate(colors = "abcabcabcabcabcabcabcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 28]]) == -1
    assert candidate(colors = "abcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0]]) == -1
    assert candidate(colors = "abacbacba",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 4
    assert candidate(colors = "abacabadabe",edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 8], [6, 8], [7, 9], [8, 9]]) == 4
    assert candidate(colors = "abacabadaba",edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 9]]) == 5
    assert candidate(colors = "abacabadaba",edges = [[0, 1], [1, 0], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == -1
    assert candidate(colors = "ababababab",edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 5], [3, 6], [4, 5], [4, 6], [5, 7], [5, 8], [6, 7], [6, 8], [7, 9], [8, 9]]) == 5
    assert candidate(colors = "abacabadaba",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 5
    assert candidate(colors = "abcabcabcabcabcabcabcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29]]) == 10
    assert candidate(colors = "abcdefghij",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == -1
    assert candidate(colors = "abacabadaba",edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 5
    assert candidate(colors = "aabbaabb",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]) == -1
    assert candidate(colors = "abcdefgabcdefgabcdefgabcdefg",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 7]]) == -1
    assert candidate(colors = "aaabbbcccdddeeefffggghhh",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23]]) == 3
    assert candidate(colors = "abcdefghijk",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 1
    assert candidate(colors = "aaaabbbbccccdddd",edges = [[0, 1], [0, 4], [1, 2], [1, 5], [2, 3], [2, 6], [3, 7], [4, 5], [4, 8], [5, 6], [5, 9], [6, 7], [6, 10], [7, 11], [8, 9], [8, 12], [9, 10], [9, 13], [10, 11], [10, 14], [11, 15], [12, 13], [13, 14], [14, 15]]) == 4
    assert candidate(colors = "abcabcabcabcabc",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 5
    assert candidate(colors = "abcde",edges = [[0, 1], [0, 2], [2, 1], [1, 3], [2, 3], [3, 4], [4, 0]]) == -1
    assert candidate(colors = "zzzzzzyyyyy",edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 6
    assert candidate(colors = "abacabadabacaba",edges = [[0, 1], [0, 2], [2, 3], [3, 4], [1, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 6


