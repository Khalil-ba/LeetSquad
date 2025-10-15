def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(widths = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7],s = "examplestring") == [1, 76]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7],s = "examplestring") == [1, 76]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == [1, 43]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == [1, 43]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "bbbcccdddaaa") == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "bbbcccdddaaa") == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55],s = "abcdefghijklmnopqrstuvwxyz") == [10, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55],s = "abcdefghijklmnopqrstuvwxyz") == [10, 55]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7],s = "akjflsajflsajfljsaljfljsalfjsalkfjsalkfjsalkfjsalkfjsalkfj") == [3, 38]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7],s = "akjflsajflsajfljsaljfljsalfjsalkfjsalkfjsalkfjsalkfjsalkfj") == [3, 38]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [3, 62]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [3, 62]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "a") == [1, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "a") == [1, 10]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7],s = "abcdefghijklmnopqrstuvwxyz") == [2, 38]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7],s = "abcdefghijklmnopqrstuvwxyz") == [2, 38]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6],s = "abcdefghij") == [1, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6],s = "abcdefghij") == [1, 55]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],s = "zyxwvutsrqponmlkjihgfedcba") == [4, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],s = "zyxwvutsrqponmlkjihgfedcba") == [4, 55]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],s = "equalpairsofequalrowsandcolumnsinamatrix") == [2, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],s = "equalpairsofequalrowsandcolumnsinamatrix") == [2, 100]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [4, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [4, 16]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],s = "samewidthforallcharacters") == [2, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],s = "samewidthforallcharacters") == [2, 25]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6],s = "abcdefghijklmnopqrstuvwxyz") == [2, 31]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6],s = "abcdefghijklmnopqrstuvwxyz") == [2, 31]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [5, 7, 9, 3, 5, 7, 9, 3, 5, 7, 9, 3, 5, 7, 9, 3, 5, 7, 9, 3, 5, 7, 9, 3, 5, 7],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [4, 24]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [5, 7, 9, 3, 5, 7, 9, 3, 5, 7, 9, 3, 5, 7, 9, 3, 5, 7, 9, 3, 5, 7, 9, 3, 5, 7],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [4, 24]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6],s = "abacabadabacabad") == [1, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6],s = "abacabadabacabad") == [1, 30]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "abcdefghijklmnopqrstuvwxyz") == [3, 60]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "abcdefghijklmnopqrstuvwxyz") == [3, 60]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8],s = "qwertyuiopasdfghjklzxcvbnm") == [2, 36]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8],s = "qwertyuiopasdfghjklzxcvbnm") == [2, 36]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],s = "equalwidthseachletter") == [1, 63]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],s = "equalwidthseachletter") == [1, 63]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7],s = "thisstringwillhavesomeunevenwidthsandshouldtesttheboundarycases") == [4, 70]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7],s = "thisstringwillhavesomeunevenwidthsandshouldtesttheboundarycases") == [4, 70]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz") == [26, 90]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz") == [26, 90]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "ababababababababababababababababababababababababababababababababababababab") == [8, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "ababababababababababababababababababababababababababababababababababababab") == [8, 40]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [9, 2, 2, 8, 4, 4, 7, 6, 6, 2, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],s = "narrowwidthsshouldwrapquickly") == [2, 76]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [9, 2, 2, 8, 4, 4, 7, 6, 6, 2, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],s = "narrowwidthsshouldwrapquickly") == [2, 76]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == [1, 96]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == [1, 96]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "mississippi") == [2, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "mississippi") == [2, 10]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [8, 6, 10, 10, 5, 5, 7, 3, 7, 2, 8, 10, 4, 4, 3, 3, 6, 14, 8, 5, 11, 11, 5, 10, 4, 10],s = "thisisaverylongstringthatwillrequiremultiplelines") == [4, 64]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [8, 6, 10, 10, 5, 5, 7, 3, 7, 2, 8, 10, 4, 4, 3, 3, 6, 14, 8, 5, 11, 11, 5, 10, 4, 10],s = "thisisaverylongstringthatwillrequiremultiplelines") == [4, 64]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80],s = "abcdefghijklmnopqrstuvwxyza") == [17, 90]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80],s = "abcdefghijklmnopqrstuvwxyza") == [17, 90]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [9, 7, 5, 3, 1, 9, 7, 5, 3, 1, 9, 7, 5, 3, 1, 9, 7, 5, 3, 1, 9, 7, 5, 3, 1, 9],s = "atlasatlasmapping") == [2, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [9, 7, 5, 3, 1, 9, 7, 5, 3, 1, 9, 7, 5, 3, 1, 9, 7, 5, 3, 1, 9, 7, 5, 3, 1, 9],s = "atlasatlasmapping") == [2, 7]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80],s = "zyxwvutsrqponmlkjihgfedcba") == [17, 60]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80],s = "zyxwvutsrqponmlkjihgfedcba") == [17, 60]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [3, 60]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [3, 60]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],s = "aaaaaaaaaabbbbbbbbccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhh") == [2, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],s = "aaaaaaaaaabbbbbbbbccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhh") == [2, 16]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80],s = "abcdefghijabcdefghijabcdefghijabcdefghij") == [24, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80],s = "abcdefghijabcdefghijabcdefghijabcdefghij") == [24, 100]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5],s = "zyxwvutsrqponmlkjihgfedcba") == [2, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5],s = "zyxwvutsrqponmlkjihgfedcba") == [2, 55]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5],s = "thisstringwillalsoneedmultiplelinesandshouldtestvariouscasesontheedges") == [4, 88]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5],s = "thisstringwillalsoneedmultiplelinesandshouldtestvariouscasesontheedges") == [4, 88]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [8, 52]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [8, 52]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [1, 52]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [1, 52]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6],s = "qzweasxcrtyplkjhgfiodnmbvcxz") == [2, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6],s = "qzweasxcrtyplkjhgfiodnmbvcxz") == [2, 40]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == [1, 78]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == [1, 78]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],s = "abcdefghijklmnopqrstuvwxyz") == [4, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],s = "abcdefghijklmnopqrstuvwxyz") == [4, 55]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],s = "wonderfulwizardwithawonderfulwizardofoz") == [1, 78]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],s = "wonderfulwizardwithawonderfulwizardofoz") == [1, 78]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5],s = "shortstringsarefun") == [1, 47]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5],s = "shortstringsarefun") == [1, 47]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == [2, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == [2, 14]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [6, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [6, 20]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [5, 10, 15, 20, 25, 5, 10, 15, 20, 25, 5, 10, 15, 20, 25, 5, 10, 15, 20, 25, 5, 10, 15, 20, 25, 5],s = "optimization") == [3, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [5, 10, 15, 20, 25, 5, 10, 15, 20, 25, 5, 10, 15, 20, 25, 5, 10, 15, 20, 25, 5, 10, 15, 20, 25, 5],s = "optimization") == [3, 20]: {e}')
    
    total += 1
    try:
        result = candidate(widths = [8, 6, 4, 2, 10, 6, 4, 2, 8, 6, 4, 2, 10, 6, 4, 2, 8, 6, 4, 2, 10, 6, 4, 2, 8, 6],s = "algorithmsanddatastructures") == [2, 46]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(widths = [8, 6, 4, 2, 10, 6, 4, 2, 8, 6, 4, 2, 10, 6, 4, 2, 8, 6, 4, 2, 10, 6, 4, 2, 8, 6],s = "algorithmsanddatastructures") == [2, 46]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(widths = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7],s = "examplestring") == [1, 76]
    assert candidate(widths = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == [1, 43]
    assert candidate(widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "bbbcccdddaaa") == [2, 4]
    assert candidate(widths = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55],s = "abcdefghijklmnopqrstuvwxyz") == [10, 55]
    assert candidate(widths = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7],s = "akjflsajflsajfljsaljfljsalfjsalkfjsalkfjsalkfjsalkfjsalkfj") == [3, 38]
    assert candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [3, 62]
    assert candidate(widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "a") == [1, 10]
    assert candidate(widths = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7],s = "abcdefghijklmnopqrstuvwxyz") == [2, 38]
    assert candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6],s = "abcdefghij") == [1, 55]
    assert candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],s = "zyxwvutsrqponmlkjihgfedcba") == [4, 55]
    assert candidate(widths = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],s = "equalpairsofequalrowsandcolumnsinamatrix") == [2, 100]
    assert candidate(widths = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [4, 16]
    assert candidate(widths = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],s = "samewidthforallcharacters") == [2, 25]
    assert candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6],s = "abcdefghijklmnopqrstuvwxyz") == [2, 31]
    assert candidate(widths = [5, 7, 9, 3, 5, 7, 9, 3, 5, 7, 9, 3, 5, 7, 9, 3, 5, 7, 9, 3, 5, 7, 9, 3, 5, 7],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [4, 24]
    assert candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6],s = "abacabadabacabad") == [1, 30]
    assert candidate(widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "abcdefghijklmnopqrstuvwxyz") == [3, 60]
    assert candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8],s = "qwertyuiopasdfghjklzxcvbnm") == [2, 36]
    assert candidate(widths = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],s = "equalwidthseachletter") == [1, 63]
    assert candidate(widths = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7],s = "thisstringwillhavesomeunevenwidthsandshouldtesttheboundarycases") == [4, 70]
    assert candidate(widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz") == [26, 90]
    assert candidate(widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "ababababababababababababababababababababababababababababababababababababab") == [8, 40]
    assert candidate(widths = [9, 2, 2, 8, 4, 4, 7, 6, 6, 2, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],s = "narrowwidthsshouldwrapquickly") == [2, 76]
    assert candidate(widths = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == [1, 96]
    assert candidate(widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "mississippi") == [2, 10]
    assert candidate(widths = [8, 6, 10, 10, 5, 5, 7, 3, 7, 2, 8, 10, 4, 4, 3, 3, 6, 14, 8, 5, 11, 11, 5, 10, 4, 10],s = "thisisaverylongstringthatwillrequiremultiplelines") == [4, 64]
    assert candidate(widths = [10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80],s = "abcdefghijklmnopqrstuvwxyza") == [17, 90]
    assert candidate(widths = [9, 7, 5, 3, 1, 9, 7, 5, 3, 1, 9, 7, 5, 3, 1, 9, 7, 5, 3, 1, 9, 7, 5, 3, 1, 9],s = "atlasatlasmapping") == [2, 7]
    assert candidate(widths = [10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80],s = "zyxwvutsrqponmlkjihgfedcba") == [17, 60]
    assert candidate(widths = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [3, 60]
    assert candidate(widths = [2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],s = "aaaaaaaaaabbbbbbbbccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhh") == [2, 16]
    assert candidate(widths = [10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80],s = "abcdefghijabcdefghijabcdefghijabcdefghij") == [24, 100]
    assert candidate(widths = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5],s = "zyxwvutsrqponmlkjihgfedcba") == [2, 55]
    assert candidate(widths = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5],s = "thisstringwillalsoneedmultiplelinesandshouldtestvariouscasesontheedges") == [4, 88]
    assert candidate(widths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [8, 52]
    assert candidate(widths = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [1, 52]
    assert candidate(widths = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6],s = "qzweasxcrtyplkjhgfiodnmbvcxz") == [2, 40]
    assert candidate(widths = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == [1, 78]
    assert candidate(widths = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],s = "abcdefghijklmnopqrstuvwxyz") == [4, 55]
    assert candidate(widths = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],s = "wonderfulwizardwithawonderfulwizardofoz") == [1, 78]
    assert candidate(widths = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5],s = "shortstringsarefun") == [1, 47]
    assert candidate(widths = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == [2, 14]
    assert candidate(widths = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [2, 4]
    assert candidate(widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [6, 20]
    assert candidate(widths = [5, 10, 15, 20, 25, 5, 10, 15, 20, 25, 5, 10, 15, 20, 25, 5, 10, 15, 20, 25, 5, 10, 15, 20, 25, 5],s = "optimization") == [3, 20]
    assert candidate(widths = [8, 6, 4, 2, 10, 6, 4, 2, 8, 6, 4, 2, 10, 6, 4, 2, 8, 6, 4, 2, 10, 6, 4, 2, 8, 6],s = "algorithmsanddatastructures") == [2, 46]


