def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(name = "zzzzzzzz",typed = "zzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "zzzzzzzz",typed = "zzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "abcd",typed = "abcde") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "abcd",typed = "abcde") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "test",typed = "ttest") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "test",typed = "ttest") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "dfuyalc",typed = "fuuyallc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "dfuyalc",typed = "fuuyallc") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "zzzyyyyy",typed = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "zzzyyyyy",typed = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "abcd",typed = "abcddcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "abcd",typed = "abcddcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "alex",typed = "aaleexa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "alex",typed = "aaleexa") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "kikcxmvzi",typed = "kiikcxxmmvvzzz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "kikcxmvzi",typed = "kiikcxxmmvvzzz") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "pyplrz",typed = "ppyypllrz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "pyplrz",typed = "ppyypllrz") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "ggggggg",typed = "ggggggg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "ggggggg",typed = "ggggggg") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "laiden",typed = "laiden") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "laiden",typed = "laiden") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "saeed",typed = "ssaaedd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "saeed",typed = "ssaaedd") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "a",typed = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "a",typed = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "a",typed = "b") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "a",typed = "b") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "abcd",typed = "abc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "abcd",typed = "abc") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "pyplrz",typed = "ppyypllr") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "pyplrz",typed = "ppyypllr") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "a",typed = "aaaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "a",typed = "aaaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "leelee",typed = "lleeelee") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "leelee",typed = "lleeelee") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "zzzaaa",typed = "zzzzzaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "zzzaaa",typed = "zzzzzaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "alex",typed = "aaleex") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "alex",typed = "aaleex") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "vtkgn",typed = "vttkgnn") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "vtkgn",typed = "vttkgnn") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "alex",typed = "ale") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "alex",typed = "ale") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "hello",typed = "hheeelllloo") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "hello",typed = "hheeelllloo") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "mississippi",typed = "miiiiiiissssssippiiiiii") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "mississippi",typed = "miiiiiiissssssippiiiiii") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",typed = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",typed = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "repeated",typed = "repeeeaatteedd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "repeated",typed = "repeeeaatteedd") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "testing",typed = "testings") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "testing",typed = "testings") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "mississippi",typed = "mmiissssippip") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "mississippi",typed = "mmiissssippip") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "aabbcc",typed = "aaabbbccc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "aabbcc",typed = "aaabbbccc") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "abcdefghij",typed = "aabbccddeeffgghhiijj") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "abcdefghij",typed = "aabbccddeeffgghhiijj") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "mississippi",typed = "mmiiisssssiiiippp") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "mississippi",typed = "mmiiisssssiiiippp") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "flower",typed = "ffflowweerrr") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "flower",typed = "ffflowweerrr") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "consistent",typed = "cccooonnsisstiisstteeennnttt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "consistent",typed = "cccooonnsisstiisstteeennnttt") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "algorithm",typed = "aaalgggggorithm") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "algorithm",typed = "aaalgggggorithm") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "programming",typed = "pprooggrammmiinngg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "programming",typed = "pprooggrammmiinngg") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "mississippi",typed = "mmiiississipppi") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "mississippi",typed = "mmiiississipppi") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "friend",typed = "ffriiieeeennnd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "friend",typed = "ffriiieeeennnd") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "longpressed",typed = "lllooonngggppprrreeesssppeeeedd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "longpressed",typed = "lllooonngggppprrreeesssppeeeedd") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "longpressed",typed = "lllongggppppreeesssssssedd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "longpressed",typed = "lllongggppppreeesssssssedd") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "polygon",typed = "pppollooogooonnnggg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "polygon",typed = "pppollooogooonnnggg") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "unique",typed = "uuunnnnuuuuuuuuqeeeuuuuuuuuuueee") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "unique",typed = "uuunnnnuuuuuuuuqeeeuuuuuuuuuueee") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "consistent",typed = "ccoonnsissssttttiinnnsss") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "consistent",typed = "ccoonnsissssttttiinnnsss") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "mississippi",typed = "mmiississippip") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "mississippi",typed = "mmiississippip") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "xxyyzz",typed = "xxyyzzzxxxyyyzzz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "xxyyzz",typed = "xxyyzzzxxxyyyzzz") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "alexandria",typed = "aaalllexxaandria") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "alexandria",typed = "aaalllexxaandria") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "qwert",typed = "qqqqwweeeerrrttt") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "qwert",typed = "qqqqwweeeerrrttt") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "vtkgn",typed = "vtttkkkgggnnn") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "vtkgn",typed = "vtttkkkgggnnn") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "rhinoceros",typed = "rrrhhiinnoocceerrrsss") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "rhinoceros",typed = "rrrhhiinnoocceerrrsss") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "longpressed",typed = "lllooonngggpppreesssed") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "longpressed",typed = "lllooonngggpppreesssed") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "qwerty",typed = "qqqwwweeeerrrrttyyyy") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "qwerty",typed = "qqqwwweeeerrrrttyyyy") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "xylophone",typed = "xxyyylloophooneee") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "xylophone",typed = "xxyyylloophooneee") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "rhythm",typed = "rhythm") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "rhythm",typed = "rhythm") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "aabbcc",typed = "aaabbcccc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "aabbcc",typed = "aaabbcccc") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "mississippi",typed = "miiisiiisssiiipppii") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "mississippi",typed = "miiisiiisssiiipppii") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "queue",typed = "qqquuuuuuuuueee") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "queue",typed = "qqquuuuuuuuueee") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "abcdefghij",typed = "aabbbbccccddddeeeeffffgggghhhhiiiijjjj") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "abcdefghij",typed = "aabbbbccccddddeeeeffffgggghhhhiiiijjjj") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "ababab",typed = "aabbababb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "ababab",typed = "aabbababb") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "qlssqwwfw",typed = "qqllssqqwwwwwfwf") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "qlssqwwfw",typed = "qqllssqqwwwwwfwf") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "aabbcc",typed = "aabbbcccc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "aabbcc",typed = "aabbbcccc") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "flower",typed = "ffffllllooower") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "flower",typed = "ffffllllooower") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "programming",typed = "ppprroogrraammmmiinngggg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "programming",typed = "ppprroogrraammmmiinngggg") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "mississippi",typed = "mmyisssssippis") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "mississippi",typed = "mmyisssssippis") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "longpress",typed = "lloongggppppreeessss") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "longpress",typed = "lloongggppppreeessss") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "aaaabbbbcccc",typed = "aaaabbbbbbcccc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "aaaabbbbcccc",typed = "aaaabbbbbbcccc") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "xy",typed = "xyxyxyxyxyxyxyxy") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "xy",typed = "xyxyxyxyxyxyxyxy") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "unique",typed = "uunniiquee") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "unique",typed = "uunniiquee") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "longpressed",typed = "lllllooonnggggppprrreeesss") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "longpressed",typed = "lllllooonnggggppprrreeesss") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "abcdefgh",typed = "aabbbcccdddddeeeeeffffffgggghhhh") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "abcdefgh",typed = "aabbbcccdddddeeeeeffffffgggghhhh") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "algorithm",typed = "aalllgggggoooooorrrriiitthhhhhmmmmm") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "algorithm",typed = "aalllgggggoooooorrrriiitthhhhhmmmmm") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "kikcxmvzi",typed = "kiikcxxmmvvvzzzii") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "kikcxmvzi",typed = "kiikcxxmmvvvzzzii") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "abcde",typed = "abcdeabcde") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "abcde",typed = "abcdeabcde") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "keyboard",typed = "kkkkeeyyyboooaarrdd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "keyboard",typed = "kkkkeeyyyboooaarrdd") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "a",typed = "aaaaaaaaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "a",typed = "aaaaaaaaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "qwerty",typed = "qqqqwwwwertyyyyy") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "qwerty",typed = "qqqqwwwwertyyyyy") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "leetcode",typed = "lleettcoodde") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "leetcode",typed = "lleettcoodde") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "laiden",typed = "laidenlaiden") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "laiden",typed = "laidenlaiden") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "aabbcc",typed = "aabbbccc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "aabbcc",typed = "aabbbccc") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "characters",typed = "ccccchaarrrrrttaaaaccchhhhheeeersss") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "characters",typed = "ccccchaarrrrrttaaaaccchhhhheeeersss") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "xylophone",typed = "xyyylloophooneee") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "xylophone",typed = "xyyylloophooneee") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "keyboard",typed = "kkkkeeyyyboaaaarrrddddd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "keyboard",typed = "kkkkeeyyyboaaaarrrddddd") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "elephant",typed = "eleelphhhaannnttt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "elephant",typed = "eleelphhhaannnttt") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "longnamehere",typed = "lllooonnggnnaaammmeehheerrree") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "longnamehere",typed = "lllooonnggnnaaammmeehheerrree") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "zebra",typed = "zzzeebrraaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "zebra",typed = "zzzeebrraaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "function",typed = "fffuunncctttiooonnnn") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "function",typed = "fffuunncctttiooonnnn") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "abcdefg",typed = "abcdeeeefg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "abcdefg",typed = "abcdeeeefg") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "qwertyuiop",typed = "qqqwwweerrttyyuuiioopp") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "qwertyuiop",typed = "qqqwwweerrttyyuuiioopp") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "hello",typed = "heeeelllllooo") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "hello",typed = "heeeelllllooo") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "robert",typed = "rroobbeerrtt") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "robert",typed = "rroobbeerrtt") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "repeated",typed = "rrreeeepppeeeaaatteeeedd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "repeated",typed = "rrreeeepppeeeaaatteeeedd") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "rhell",typed = "rhellllllll") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "rhell",typed = "rhellllllll") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "mississippi",typed = "mmiisssssippppi") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "mississippi",typed = "mmiisssssippppi") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "supercalifragilisticexpialidocious",typed = "ssuupercccaliiifffragggiilissticceexpiialiiddoouuusss") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "supercalifragilisticexpialidocious",typed = "ssuupercccaliiifffragggiilissticceexpiialiiddoouuusss") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "triangle",typed = "tttriiaanngggllee") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "triangle",typed = "tttriiaanngggllee") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "variable",typed = "vvvvvaaarriiiaabbbblllee") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "variable",typed = "vvvvvaaarriiiaabbbblllee") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "aabbc",typed = "aabbbcc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "aabbc",typed = "aabbbcc") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "abcd",typed = "aabbbccccdddd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "abcd",typed = "aabbbccccdddd") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "hello",typed = "heeeelllllllllo") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "hello",typed = "heeeelllllllllo") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "typing",typed = "ttypiinggggg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "typing",typed = "ttypiinggggg") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "longpressed",typed = "lllllonggggppppreeeesssssssppppeeeedd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "longpressed",typed = "lllllonggggppppreeeesssssssppppeeeedd") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "unique",typed = "uunniiqueee") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "unique",typed = "uunniiqueee") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "aaab",typed = "aaaaaabbbb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "aaab",typed = "aaaaaabbbb") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "",typed = "") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "",typed = "") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "elephant",typed = "eeelleeeephhhhaaaalllllltttt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "elephant",typed = "eeelleeeephhhhaaaalllllltttt") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "ggg",typed = "ggggggggggg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "ggg",typed = "ggggggggggg") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "abcd",typed = "aabbccddeeffgg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "abcd",typed = "aabbccddeeffgg") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "testing",typed = "testtinngg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "testing",typed = "testtinngg") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "abcdef",typed = "aabbccddeeffgg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "abcdef",typed = "aabbccddeeffgg") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "sequence",typed = "sseeqqqquuuuuuennnnccccceee") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "sequence",typed = "sseeqqqquuuuuuennnnccccceee") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "carlosgomez",typed = "cccarllloossgggoommezz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "carlosgomez",typed = "cccarllloossgggoommezz") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "elephant",typed = "eeellllepphaaannntt") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "elephant",typed = "eeellllepphaaannntt") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "aaaaaa",typed = "aaaaaaaaaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "aaaaaa",typed = "aaaaaaaaaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "programming",typed = "ppprroogggrraammmiinnnggg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "programming",typed = "ppprroogggrraammmiinnnggg") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "aaabbbccc",typed = "aabbbccc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "aaabbbccc",typed = "aabbbccc") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "algorithm",typed = "aalllggggorrrrithhhoonnmmm") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "algorithm",typed = "aalllggggorrrrithhhoonnmmm") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "abcdabcd",typed = "aabbccddeeffgg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "abcdabcd",typed = "aabbccddeeffgg") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "programming",typed = "pprrrooggggrrraaaaammmmmmiiiiinnnggggggggg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "programming",typed = "pprrrooggggrrraaaaammmmmmiiiiinnnggggggggg") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "sequence",typed = "sseeeequuuuueeeennnnncceeeeee") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "sequence",typed = "sseeeequuuuueeeennnnncceeeeee") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "farruh",typed = "faaarrrruuhhhh") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "farruh",typed = "faaarrrruuhhhh") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "abcdefghijk",typed = "aabbcdddeeeffggghhhiiiijjjkkk") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "abcdefghijk",typed = "aabbcdddeeeffggghhhiiiijjjkkk") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "xylophone",typed = "xyyyylloophooneee") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "xylophone",typed = "xyyyylloophooneee") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "xylophone",typed = "xxxyyylloooophooooneee") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "xylophone",typed = "xxxyyylloooophooooneee") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "abcdefg",typed = "abcdddddeeeffffffggg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "abcdefg",typed = "abcdddddeeeffffffggg") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "carlos",typed = "cccaaarlllooss") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "carlos",typed = "cccaaarlllooss") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "mississippi",typed = "miisissiipppi") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "mississippi",typed = "miisissiipppi") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "challenge",typed = "chhaalllaannggeee") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "challenge",typed = "chhaalllaannggeee") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "abcd",typed = "aabbccdd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "abcd",typed = "aabbccdd") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "consistent",typed = "ccconinnsisttteeennnsssstt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "consistent",typed = "ccconinnsisttteeennnsssstt") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "consistent",typed = "cccooonnsiisstteeeennnttt") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "consistent",typed = "cccooonnsiisstteeeennnttt") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "abababa",typed = "aabbaabbaabbaaba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "abababa",typed = "aabbaabbaabbaaba") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "mississippi",typed = "mmiissssssiiipppp") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "mississippi",typed = "mmiissssssiiipppp") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "example",typed = "eexxaammmppllee") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "example",typed = "eexxaammmppllee") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "testcase",typed = "tteeeessttccaaase") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "testcase",typed = "tteeeessttccaaase") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "aaa",typed = "aaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "aaa",typed = "aaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "friend",typed = "frrriieeedd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "friend",typed = "frrriieeedd") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "algorithm",typed = "aalllgggggoooooorrriiithhhhhmmmmm") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "algorithm",typed = "aalllgggggoooooorrriiithhhhhmmmmm") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "xyz",typed = "xxxyyyzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "xyz",typed = "xxxyyyzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "xyz",typed = "xxyyyzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "xyz",typed = "xxyyyzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "longpressed",typed = "lllllooonngggpppprrreeeesssssseeeedd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "longpressed",typed = "lllllooonngggpppprrreeeesssssseeeedd") == True: {e}')
    
    total += 1
    try:
        result = candidate(name = "complexity",typed = "cccomppplleexxiittiityyy") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "complexity",typed = "cccomppplleexxiittiityyy") == False: {e}')
    
    total += 1
    try:
        result = candidate(name = "zebra",typed = "zzzeeebrrraa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(name = "zebra",typed = "zzzeeebrrraa") == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(name = "zzzzzzzz",typed = "zzzzzzzz") == True
    assert candidate(name = "abcd",typed = "abcde") == False
    assert candidate(name = "test",typed = "ttest") == True
    assert candidate(name = "dfuyalc",typed = "fuuyallc") == False
    assert candidate(name = "zzzyyyyy",typed = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == False
    assert candidate(name = "abcd",typed = "abcddcba") == False
    assert candidate(name = "alex",typed = "aaleexa") == False
    assert candidate(name = "kikcxmvzi",typed = "kiikcxxmmvvzzz") == False
    assert candidate(name = "pyplrz",typed = "ppyypllrz") == True
    assert candidate(name = "ggggggg",typed = "ggggggg") == True
    assert candidate(name = "laiden",typed = "laiden") == True
    assert candidate(name = "saeed",typed = "ssaaedd") == False
    assert candidate(name = "a",typed = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == True
    assert candidate(name = "a",typed = "b") == False
    assert candidate(name = "abcd",typed = "abc") == False
    assert candidate(name = "pyplrz",typed = "ppyypllr") == False
    assert candidate(name = "a",typed = "aaaaaa") == True
    assert candidate(name = "leelee",typed = "lleeelee") == True
    assert candidate(name = "zzzaaa",typed = "zzzzzaaaa") == True
    assert candidate(name = "alex",typed = "aaleex") == True
    assert candidate(name = "vtkgn",typed = "vttkgnn") == True
    assert candidate(name = "alex",typed = "ale") == False
    assert candidate(name = "hello",typed = "hheeelllloo") == True
    assert candidate(name = "mississippi",typed = "miiiiiiissssssippiiiiii") == False
    assert candidate(name = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",typed = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == True
    assert candidate(name = "repeated",typed = "repeeeaatteedd") == True
    assert candidate(name = "testing",typed = "testings") == False
    assert candidate(name = "mississippi",typed = "mmiissssippip") == False
    assert candidate(name = "aabbcc",typed = "aaabbbccc") == True
    assert candidate(name = "abcdefghij",typed = "aabbccddeeffgghhiijj") == True
    assert candidate(name = "mississippi",typed = "mmiiisssssiiiippp") == False
    assert candidate(name = "flower",typed = "ffflowweerrr") == True
    assert candidate(name = "consistent",typed = "cccooonnsisstiisstteeennnttt") == False
    assert candidate(name = "algorithm",typed = "aaalgggggorithm") == True
    assert candidate(name = "programming",typed = "pprooggrammmiinngg") == True
    assert candidate(name = "mississippi",typed = "mmiiississipppi") == True
    assert candidate(name = "friend",typed = "ffriiieeeennnd") == True
    assert candidate(name = "longpressed",typed = "lllooonngggppprrreeesssppeeeedd") == False
    assert candidate(name = "longpressed",typed = "lllongggppppreeesssssssedd") == True
    assert candidate(name = "polygon",typed = "pppollooogooonnnggg") == False
    assert candidate(name = "unique",typed = "uuunnnnuuuuuuuuqeeeuuuuuuuuuueee") == False
    assert candidate(name = "consistent",typed = "ccoonnsissssttttiinnnsss") == False
    assert candidate(name = "mississippi",typed = "mmiississippip") == False
    assert candidate(name = "xxyyzz",typed = "xxyyzzzxxxyyyzzz") == False
    assert candidate(name = "alexandria",typed = "aaalllexxaandria") == True
    assert candidate(name = "qwert",typed = "qqqqwweeeerrrttt") == True
    assert candidate(name = "vtkgn",typed = "vtttkkkgggnnn") == True
    assert candidate(name = "rhinoceros",typed = "rrrhhiinnoocceerrrsss") == False
    assert candidate(name = "longpressed",typed = "lllooonngggpppreesssed") == True
    assert candidate(name = "qwerty",typed = "qqqwwweeeerrrrttyyyy") == True
    assert candidate(name = "xylophone",typed = "xxyyylloophooneee") == True
    assert candidate(name = "rhythm",typed = "rhythm") == True
    assert candidate(name = "aabbcc",typed = "aaabbcccc") == True
    assert candidate(name = "mississippi",typed = "miiisiiisssiiipppii") == False
    assert candidate(name = "queue",typed = "qqquuuuuuuuueee") == False
    assert candidate(name = "abcdefghij",typed = "aabbbbccccddddeeeeffffgggghhhhiiiijjjj") == True
    assert candidate(name = "ababab",typed = "aabbababb") == True
    assert candidate(name = "qlssqwwfw",typed = "qqllssqqwwwwwfwf") == False
    assert candidate(name = "aabbcc",typed = "aabbbcccc") == True
    assert candidate(name = "flower",typed = "ffffllllooower") == True
    assert candidate(name = "programming",typed = "ppprroogrraammmmiinngggg") == True
    assert candidate(name = "mississippi",typed = "mmyisssssippis") == False
    assert candidate(name = "longpress",typed = "lloongggppppreeessss") == True
    assert candidate(name = "aaaabbbbcccc",typed = "aaaabbbbbbcccc") == True
    assert candidate(name = "xy",typed = "xyxyxyxyxyxyxyxy") == False
    assert candidate(name = "unique",typed = "uunniiquee") == True
    assert candidate(name = "longpressed",typed = "lllllooonnggggppprrreeesss") == False
    assert candidate(name = "abcdefgh",typed = "aabbbcccdddddeeeeeffffffgggghhhh") == True
    assert candidate(name = "algorithm",typed = "aalllgggggoooooorrrriiitthhhhhmmmmm") == True
    assert candidate(name = "kikcxmvzi",typed = "kiikcxxmmvvvzzzii") == True
    assert candidate(name = "abcde",typed = "abcdeabcde") == False
    assert candidate(name = "keyboard",typed = "kkkkeeyyyboooaarrdd") == True
    assert candidate(name = "a",typed = "aaaaaaaaaaa") == True
    assert candidate(name = "qwerty",typed = "qqqqwwwwertyyyyy") == True
    assert candidate(name = "leetcode",typed = "lleettcoodde") == True
    assert candidate(name = "laiden",typed = "laidenlaiden") == False
    assert candidate(name = "aabbcc",typed = "aabbbccc") == True
    assert candidate(name = "characters",typed = "ccccchaarrrrrttaaaaccchhhhheeeersss") == False
    assert candidate(name = "xylophone",typed = "xyyylloophooneee") == True
    assert candidate(name = "keyboard",typed = "kkkkeeyyyboaaaarrrddddd") == True
    assert candidate(name = "elephant",typed = "eleelphhhaannnttt") == False
    assert candidate(name = "longnamehere",typed = "lllooonnggnnaaammmeehheerrree") == True
    assert candidate(name = "zebra",typed = "zzzeebrraaa") == True
    assert candidate(name = "function",typed = "fffuunncctttiooonnnn") == True
    assert candidate(name = "abcdefg",typed = "abcdeeeefg") == True
    assert candidate(name = "qwertyuiop",typed = "qqqwwweerrttyyuuiioopp") == True
    assert candidate(name = "hello",typed = "heeeelllllooo") == True
    assert candidate(name = "robert",typed = "rroobbeerrtt") == True
    assert candidate(name = "repeated",typed = "rrreeeepppeeeaaatteeeedd") == True
    assert candidate(name = "rhell",typed = "rhellllllll") == True
    assert candidate(name = "mississippi",typed = "mmiisssssippppi") == False
    assert candidate(name = "supercalifragilisticexpialidocious",typed = "ssuupercccaliiifffragggiilissticceexpiialiiddoouuusss") == False
    assert candidate(name = "triangle",typed = "tttriiaanngggllee") == True
    assert candidate(name = "variable",typed = "vvvvvaaarriiiaabbbblllee") == True
    assert candidate(name = "aabbc",typed = "aabbbcc") == True
    assert candidate(name = "abcd",typed = "aabbbccccdddd") == True
    assert candidate(name = "hello",typed = "heeeelllllllllo") == True
    assert candidate(name = "typing",typed = "ttypiinggggg") == True
    assert candidate(name = "longpressed",typed = "lllllonggggppppreeeesssssssppppeeeedd") == False
    assert candidate(name = "unique",typed = "uunniiqueee") == True
    assert candidate(name = "aaab",typed = "aaaaaabbbb") == True
    assert candidate(name = "",typed = "") == True
    assert candidate(name = "elephant",typed = "eeelleeeephhhhaaaalllllltttt") == False
    assert candidate(name = "ggg",typed = "ggggggggggg") == True
    assert candidate(name = "abcd",typed = "aabbccddeeffgg") == False
    assert candidate(name = "testing",typed = "testtinngg") == True
    assert candidate(name = "abcdef",typed = "aabbccddeeffgg") == False
    assert candidate(name = "sequence",typed = "sseeqqqquuuuuuennnnccccceee") == True
    assert candidate(name = "carlosgomez",typed = "cccarllloossgggoommezz") == True
    assert candidate(name = "elephant",typed = "eeellllepphaaannntt") == True
    assert candidate(name = "aaaaaa",typed = "aaaaaaaaaaaa") == True
    assert candidate(name = "programming",typed = "ppprroogggrraammmiinnnggg") == True
    assert candidate(name = "aaabbbccc",typed = "aabbbccc") == False
    assert candidate(name = "algorithm",typed = "aalllggggorrrrithhhoonnmmm") == False
    assert candidate(name = "abcdabcd",typed = "aabbccddeeffgg") == False
    assert candidate(name = "programming",typed = "pprrrooggggrrraaaaammmmmmiiiiinnnggggggggg") == True
    assert candidate(name = "sequence",typed = "sseeeequuuuueeeennnnncceeeeee") == True
    assert candidate(name = "farruh",typed = "faaarrrruuhhhh") == True
    assert candidate(name = "abcdefghijk",typed = "aabbcdddeeeffggghhhiiiijjjkkk") == True
    assert candidate(name = "xylophone",typed = "xyyyylloophooneee") == True
    assert candidate(name = "xylophone",typed = "xxxyyylloooophooooneee") == True
    assert candidate(name = "abcdefg",typed = "abcdddddeeeffffffggg") == True
    assert candidate(name = "carlos",typed = "cccaaarlllooss") == True
    assert candidate(name = "mississippi",typed = "miisissiipppi") == False
    assert candidate(name = "challenge",typed = "chhaalllaannggeee") == False
    assert candidate(name = "abcd",typed = "aabbccdd") == True
    assert candidate(name = "consistent",typed = "ccconinnsisttteeennnsssstt") == False
    assert candidate(name = "consistent",typed = "cccooonnsiisstteeeennnttt") == True
    assert candidate(name = "abababa",typed = "aabbaabbaabbaaba") == False
    assert candidate(name = "mississippi",typed = "mmiissssssiiipppp") == False
    assert candidate(name = "example",typed = "eexxaammmppllee") == True
    assert candidate(name = "testcase",typed = "tteeeessttccaaase") == True
    assert candidate(name = "aaa",typed = "aaaaa") == True
    assert candidate(name = "friend",typed = "frrriieeedd") == False
    assert candidate(name = "algorithm",typed = "aalllgggggoooooorrriiithhhhhmmmmm") == True
    assert candidate(name = "xyz",typed = "xxxyyyzzz") == True
    assert candidate(name = "xyz",typed = "xxyyyzzz") == True
    assert candidate(name = "longpressed",typed = "lllllooonngggpppprrreeeesssssseeeedd") == True
    assert candidate(name = "complexity",typed = "cccomppplleexxiittiityyy") == False
    assert candidate(name = "zebra",typed = "zzzeeebrrraa") == True


