def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "a",k = 2) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",k = 2) == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",k = 2) == "m"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",k = 2) == "m": {e}')
    
    total += 1
    try:
        result = candidate(s = "deeedbbcccbdaa",k = 3) == "aa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deeedbbcccbdaa",k = 3) == "aa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",k = 2) == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",k = 2) == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",k = 5) == "abcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",k = 5) == "abcde": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcd",k = 4) == "abcdabcdabcdabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcd",k = 4) == "abcdabcdabcdabcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeee",k = 3) == "aabbccdd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeee",k = 3) == "aabbccdd": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbccc",k = 4) == "bbbccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbccc",k = 4) == "bbbccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "pbbcggttciiippooaais",k = 2) == "ps"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pbbcggttciiippooaais",k = 2) == "ps": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzz",k = 5) == "zzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzz",k = 5) == "zzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeee",k = 2) == "e"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeee",k = 2) == "e": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",k = 3) == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",k = 3) == "z": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababab",k = 2) == "abababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababab",k = 2) == "abababababababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz",k = 10) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz",k = 10) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",k = 3) == "abcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",k = 3) == "abcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "a",k = 1) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",k = 1) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccddd",k = 3) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccddd",k = 3) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",k = 4) == "abcdabcdabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",k = 4) == "abcdabcdabcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",k = 2) == "abcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",k = 2) == "abcde": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbccc",k = 3) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbccc",k = 3) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "nnnnttttuuuu",k = 4) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nnnnttttuuuu",k = 4) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",k = 2) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",k = 2) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaabaaaabbbbccccdddd",k = 3) == "bbaababcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaabaaaabbbbccccdddd",k = 3) == "bbaababcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",k = 5) == "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",k = 5) == "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijaaaabbbbccccddddeeeeffffgggghhhhiiii",k = 4) == "abcdefghij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijaaaabbbbccccddddeeeeffffgggghhhhiiii",k = 4) == "abcdefghij": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba",k = 26) == "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba",k = 26) == "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "mmnnmmllooonnmmllooonn",k = 3) == "mmnnmmllnnmmllnn"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mmnnmmllooonnmmllooonn",k = 3) == "mmnnmmllnnmmllnn": {e}')
    
    total += 1
    try:
        result = candidate(s = "pppppqqqppppqqqqqqqqq",k = 5) == "qqqppppqqqq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pppppqqqppppqqqqqqqqq",k = 5) == "qqqppppqqqq": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggghhhiiiijjjkkklllmmmnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzzzzzzz",k = 4) == "aabbccddeeefffggghhhjjjkkklllmmmnnooopppqqqrrrssstttuuuvvvwwwxxxyyy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggghhhiiiijjjkkklllmmmnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzzzzzzz",k = 4) == "aabbccddeeefffggghhhjjjkkklllmmmnnooopppqqqrrrssstttuuuvvvwwwxxxyyy": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx",k = 3) == "xyxxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx",k = 3) == "xyxxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddeeefffggghhhiiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxxxyyyyyzzzzz",k = 3) == "ixxyyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddeeefffggghhhiiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxxxyyyyyzzzzz",k = 3) == "ixxyyzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "nnnnooooffffgggg",k = 4) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nnnnooooffffgggg",k = 4) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbccddeeefffggghhhiiijjjkkklllmmmnnooopppqqqrrrssstttuuuuvvvwwwxxyyzz",k = 3) == "aaccddnnuxxyyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbccddeeefffggghhhiiijjjkkklllmmmnnooopppqqqrrrssstttuuuuvvvwwwxxyyzz",k = 3) == "aaccddnnuxxyyzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "ppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz",k = 5) == "ppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz",k = 5) == "ppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippiiiiiiiiii",k = 5) == "mississipp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippiiiiiiiiii",k = 5) == "mississipp": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggghhhiiiijjjkkklllmmmnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz",k = 3) == "aabbccddinn"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggghhhiiiijjjkkklllmmmnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz",k = 3) == "aabbccddinn": {e}')
    
    total += 1
    try:
        result = candidate(s = "pppqqqrrrssstttuuuvvvwwwww",k = 5) == "pppqqqrrrssstttuuuvvv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pppqqqrrrssstttuuuvvvwwwww",k = 5) == "pppqqqrrrssstttuuuvvv": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqq",k = 4) == "aabbccddeeefffggghhh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqq",k = 4) == "aabbccddeeefffggghhh": {e}')
    
    total += 1
    try:
        result = candidate(s = "ppppqqqrrrssstttuuuvvvwwwwwxxxxyyyyzzzz",k = 4) == "qqqrrrssstttuuuvvvw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ppppqqqrrrssstttuuuvvvwwwwwxxxxyyyyzzzz",k = 4) == "qqqrrrssstttuuuvvvw": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababab",k = 3) == "abababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababab",k = 3) == "abababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippiississi",k = 3) == "mississippiississi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippiississi",k = 3) == "mississippiississi": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",k = 4) == "abcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",k = 4) == "abcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzyyyyyyyyyzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 7) == "zzzzyy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzyyyyyyyyyzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 7) == "zzzzyy": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababab",k = 3) == "abababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababab",k = 3) == "abababababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "mmnnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz",k = 3) == "mm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mmnnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz",k = 3) == "mm": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijkllllllllllllmnopqrstuvwxyz",k = 10) == "abcdefghijkllmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijkllllllllllllmnopqrstuvwxyz",k = 10) == "abcdefghijkllmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 26) == "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 26) == "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzzzzzzxy",k = 6) == "xyzzxy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzzzzzzxy",k = 6) == "xyzzxy": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefggggggfedcba",k = 5) == "abcdefgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefggggggfedcba",k = 5) == "abcdefgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababababababababababababababab",k = 20) == "ababababababababababababababababababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababababababababababababababab",k = 20) == "ababababababababababababababababababababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",k = 10) == "qqqq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",k = 10) == "qqqq": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzyzzzz",k = 5) == "yzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzyzzzz",k = 5) == "yzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "wwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzz",k = 6) == "wwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "wwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzz",k = 6) == "wwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "pppppaaaabbbbcccccccdddddddd",k = 4) == "pccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pppppaaaabbbbcccccccdddddddd",k = 4) == "pccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaaacccaaabbbcccbbccaa",k = 3) == "aababbccaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaaacccaaabbbcccbbccaa",k = 3) == "aababbccaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijkllllllllllllmnopqrstuv",k = 11) == "abcdefghijklmnopqrstuv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijkllllllllllllmnopqrstuv",k = 11) == "abcdefghijklmnopqrstuv": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz",k = 10) == "hhhhhhhhxxx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz",k = 10) == "hhhhhhhhxxx": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzz",k = 6) == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzz",k = 6) == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcd",k = 6) == "abcdabcdabcdabcdabcdabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcd",k = 6) == "abcdabcdabcdabcdabcdabcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzy",k = 5) == "xyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzy",k = 5) == "xyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzy": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggghhhiiiijjjjkkkk",k = 4) == "aabbccddeeefffggghhh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggghhhiiiijjjjkkkk",k = 4) == "aabbccddeeefffggghhh": {e}')
    
    total += 1
    try:
        result = candidate(s = "pppppppppaaaabbbbccccdddd",k = 4) == "p"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pppppppppaaaabbbbccccdddd",k = 4) == "p": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc",k = 10) == "abcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc",k = 10) == "abcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggghhhiiijjjkkklllmnnnooopppqqqrrrssstttuuuvvvwwxxyyzz",k = 3) == "aabbccddmwwxxyyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggghhhiiijjjkkklllmnnnooopppqqqrrrssstttuuuvvvwwxxyyzz",k = 3) == "aabbccddmwwxxyyzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzzzzzzzzzyyxwwwwwwwwwwwwwxvvvvvvvvvvvvvuuuuuuuuuuuuuutttttttttttttsssssssssssssrrrrrrrrrrrrrqqqqqqqqqqqqqpnnnnnnnnnnnnnoommmmmmmmmmmmmllllllllllllllkkkkkkkkkkkkkkjjjjjjjjjjjjjjiiiiiiiiiiiiiiiihhhhhhhhhhhhhhhhhgggggggggggggggggffffffffffffffffeeeeeeeeeeeeeeeeedddddddddddddddddccccccccccccccccccbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaa",k = 20) == "xyzzzzzzzzzzzyyxwwwwwwwwwwwwwxvvvvvvvvvvvvvuuuuuuuuuuuuuutttttttttttttsssssssssssssrrrrrrrrrrrrrqqqqqqqqqqqqqpnnnnnnnnnnnnnoommmmmmmmmmmmmllllllllllllllkkkkkkkkkkkkkkjjjjjjjjjjjjjjiiiiiiiiiiiiiiiihhhhhhhhhhhhhhhhhgggggggggggggggggffffffffffffffffeeeeeeeeeeeeeeeeedddddddddddddddddccccccccccccccccccbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzzzzzzzzzyyxwwwwwwwwwwwwwxvvvvvvvvvvvvvuuuuuuuuuuuuuutttttttttttttsssssssssssssrrrrrrrrrrrrrqqqqqqqqqqqqqpnnnnnnnnnnnnnoommmmmmmmmmmmmllllllllllllllkkkkkkkkkkkkkkjjjjjjjjjjjjjjiiiiiiiiiiiiiiiihhhhhhhhhhhhhhhhhgggggggggggggggggffffffffffffffffeeeeeeeeeeeeeeeeedddddddddddddddddccccccccccccccccccbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaa",k = 20) == "xyzzzzzzzzzzzyyxwwwwwwwwwwwwwxvvvvvvvvvvvvvuuuuuuuuuuuuuutttttttttttttsssssssssssssrrrrrrrrrrrrrqqqqqqqqqqqqqpnnnnnnnnnnnnnoommmmmmmmmmmmmllllllllllllllkkkkkkkkkkkkkkjjjjjjjjjjjjjjiiiiiiiiiiiiiiiihhhhhhhhhhhhhhhhhgggggggggggggggggffffffffffffffffeeeeeeeeeeeeeeeeedddddddddddddddddccccccccccccccccccbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba",k = 2) == "lkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba",k = 2) == "lkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippiissiippiiissipiissipiissipiissipiissipiissipiissipiissipiis",k = 3) == "mississippiissiippssipiissipiissipiissipiissipiissipiissipiissipiis"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippiissiippiiissipiissipiissipiissipiissipiissipiissipiissipiis",k = 3) == "mississippiissiippssipiissipiissipiissipiissipiissipiissipiissipiis": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaaabbbaaa",k = 3) == "ba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaaabbbaaa",k = 3) == "ba": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccdddd",k = 4) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccdddd",k = 4) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzyyyxx",k = 4) == "zyyyxx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzyyyxx",k = 4) == "zyyyxx": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzz",k = 5) == "zz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzz",k = 5) == "zz": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzyyyyyxxxwwwwvvvvuuuuuuttttssssrrrrqqqqppppooooonnnnmmmmmllllkkkkjjjjiiihhhhggggffffeeee",k = 5) == "xxxwwwwvvvvuttttssssrrrrqqqqppppnnnnllllkkkkjjjjiiihhhhggggffffeeee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzyyyyyxxxwwwwvvvvuuuuuuttttssssrrrrqqqqppppooooonnnnmmmmmllllkkkkjjjjiiihhhhggggffffeeee",k = 5) == "xxxwwwwvvvvuttttssssrrrrqqqqppppnnnnllllkkkkjjjjiiihhhhggggffffeeee": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyxyzyxyzyxyzyxyzy",k = 3) == "xyzyxyzyxyzyxyzyxyzy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyxyzyxyzyxyzyxyzy",k = 3) == "xyzyxyzyxyzyxyzyxyzy": {e}')
    
    total += 1
    try:
        result = candidate(s = "ppppppqqqqqqrrrrrr",k = 6) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ppppppqqqqqqrrrrrr",k = 6) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabad",k = 4) == "abacabadabacabadabacabadabacabad"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabad",k = 4) == "abacabadabacabadabacabadabacabad": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzzxyzzzz",k = 5) == "xyzzzzxyzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzzxyzzzz",k = 5) == "xyzzzzxyzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababab",k = 7) == "abababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababab",k = 7) == "abababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccbaabccba",k = 3) == "abccbaabccbaabccba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccbaabccba",k = 3) == "abccbaabccbaabccba": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbbccccddddaaaabbbbccccddddaaaabbbbccccdddd",k = 4) == "aa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbbccccddddaaaabbbbccccddddaaaabbbbccccdddd",k = 4) == "aa": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffgghhiiijjjkkklllmmmnnooopppqqqrrrssstttuuuvvvwww",k = 5) == "aabbccddeeefffgghhiiijjjkkklllmmmnnooopppqqqrrrssstttuuuvvvwww"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffgghhiiijjjkkklllmmmnnooopppqqqrrrssstttuuuvvvwww",k = 5) == "aabbccddeeefffgghhiiijjjkkklllmmmnnooopppqqqrrrssstttuuuvvvwww": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabaaaabaaaabaaaab",k = 4) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabaaaabaaaabaaaab",k = 4) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefff",k = 2) == "ef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefff",k = 2) == "ef": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeeefffffffff",k = 10) == "bbbbbbbbccccccccddddddddeeeeeeeeefffffffff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeeefffffffff",k = 10) == "bbbbbbbbccccccccddddddddeeeeeeeeefffffffff": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzyyyyyxxxxxxwwwwvvvvvuuuuu",k = 5) == "xwwww"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzyyyyyxxxxxxwwwwvvvvvuuuuu",k = 5) == "xwwww": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnoooo",k = 4) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnoooo",k = 4) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccccddeeeeffffgggghhhiiijjjkkk",k = 4) == "aabbddhhhiiijjjkkk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccccddeeeeffffgggghhhiiijjjkkk",k = 4) == "aabbddhhhiiijjjkkk": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvw",k = 2) == "mnopqrstuvw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvw",k = 2) == "mnopqrstuvw": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzxxxyyyzzzxxxyyy",k = 3) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzxxxyyyzzzxxxyyy",k = 3) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbb",k = 10) == "abcdefghijklabbbbbbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbb",k = 10) == "abcdefghijklabbbbbbbb": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggg",k = 3) == "aabbccdd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggg",k = 3) == "aabbccdd": {e}')
    
    total += 1
    try:
        result = candidate(s = "qqqqwwwwrrrreeee",k = 4) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qqqqwwwwrrrreeee",k = 4) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippiissippi",k = 4) == "mississippiissippi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippiissippi",k = 4) == "mississippiissippi": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzyyyyxxxxwwwwvvvvuuuu",k = 5) == "yyyyxxxxwwwwvvvvuuuu"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzyyyyxxxxwwwwvvvvuuuu",k = 5) == "yyyyxxxxwwwwvvvvuuuu": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijkllllllllllmnopqrstuvwxyz",k = 10) == "abcdefghijkmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijkllllllllllmnopqrstuvwxyz",k = 10) == "abcdefghijkmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",k = 4) == "zz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",k = 4) == "zz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab",k = 5) == "abababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab",k = 5) == "abababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "qqwweerrttyyuuiiooppaassddffgghhjjkkllzzxciwoqjfqioejqwojfioqwjfiqwjefioqwjfeiqwjeofiqwjeofiqwjefiqwjf",k = 2) == "xciwoqjfqioejqwojfioqwjfiqwjefioqwjfeiqwjeofiqwjeofiqwjefiqwjf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qqwweerrttyyuuiiooppaassddffgghhjjkkllzzxciwoqjfqioejqwojfioqwjfiqwjefioqwjfeiqwjeofiqwjeofiqwjefiqwjf",k = 2) == "xciwoqjfqioejqwojfioqwjfiqwjefioqwjfeiqwjeofiqwjeofiqwjefiqwjf": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 10) == "zzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 10) == "zzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "mmnnnnoooopprrrssstttuuuuvvvvwwxxxyyyzzzzzz",k = 6) == "mmnnnnoooopprrrssstttuuuuvvvvwwxxxyyy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mmnnnnoooopprrrssstttuuuuvvvvwwxxxyyyzzzzzz",k = 6) == "mmnnnnoooopprrrssstttuuuuvvvvwwxxxyyy": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaabbbbbbbbccccccccddddddddd",k = 8) == "ad"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaabbbbbbbbccccccccddddddddd",k = 8) == "ad": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijaaaaklmnopqrstuuvwxyz",k = 3) == "abcdefghijaklmnopqrstuuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijaaaaklmnopqrstuuvwxyz",k = 3) == "abcdefghijaklmnopqrstuuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnoooopppp",k = 5) == "aabbccddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnoooopppp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnoooopppp",k = 5) == "aabbccddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnoooopppp": {e}')
    
    total += 1
    try:
        result = candidate(s = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",k = 20) == "qqqqqqqqqqqqqq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",k = 20) == "qqqqqqqqqqqqqq": {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaccccbaa",k = 4) == "abbabaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaccccbaa",k = 4) == "abbabaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghij",k = 10) == "abcdefghijabcdefghijabcdefghij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghij",k = 10) == "abcdefghijabcdefghijabcdefghij": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 2) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 2) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcd",k = 3) == "abcdabcdabcdabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcd",k = 3) == "abcdabcdabcdabcd": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "a",k = 2) == "a"
    assert candidate(s = "mississippi",k = 2) == "m"
    assert candidate(s = "deeedbbcccbdaa",k = 3) == "aa"
    assert candidate(s = "abcd",k = 2) == "abcd"
    assert candidate(s = "abcde",k = 5) == "abcde"
    assert candidate(s = "abcdabcdabcdabcd",k = 4) == "abcdabcdabcdabcd"
    assert candidate(s = "aabbccddeee",k = 3) == "aabbccdd"
    assert candidate(s = "aaaabbbccc",k = 4) == "bbbccc"
    assert candidate(s = "pbbcggttciiippooaais",k = 2) == "ps"
    assert candidate(s = "zzzzzzzzzzzzzzzzzz",k = 5) == "zzz"
    assert candidate(s = "aabbccddeee",k = 2) == "e"
    assert candidate(s = "zzzzzzzzzz",k = 3) == "z"
    assert candidate(s = "abababababababab",k = 2) == "abababababababab"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz",k = 10) == ""
    assert candidate(s = "abcabcabc",k = 3) == "abcabcabc"
    assert candidate(s = "a",k = 1) == ""
    assert candidate(s = "aaabbbcccddd",k = 3) == ""
    assert candidate(s = "abcdabcdabcd",k = 4) == "abcdabcdabcd"
    assert candidate(s = "abcde",k = 2) == "abcde"
    assert candidate(s = "aaabbbccc",k = 3) == ""
    assert candidate(s = "nnnnttttuuuu",k = 4) == ""
    assert candidate(s = "aabbcc",k = 2) == ""
    assert candidate(s = "bbaabaaaabbbbccccdddd",k = 3) == "bbaababcd"
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",k = 5) == "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
    assert candidate(s = "abcdefghijaaaabbbbccccddddeeeeffffgggghhhhiiii",k = 4) == "abcdefghij"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba",k = 26) == "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba"
    assert candidate(s = "mmnnmmllooonnmmllooonn",k = 3) == "mmnnmmllnnmmllnn"
    assert candidate(s = "pppppqqqppppqqqqqqqqq",k = 5) == "qqqppppqqqq"
    assert candidate(s = "aabbccddeeefffggghhhiiiijjjkkklllmmmnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzzzzzzz",k = 4) == "aabbccddeeefffggghhhjjjkkklllmmmnnooopppqqqrrrssstttuuuvvvwwwxxxyyy"
    assert candidate(s = "xyxxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx",k = 3) == "xyxxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx"
    assert candidate(s = "aaabbbcccdddeeefffggghhhiiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxxxyyyyyzzzzz",k = 3) == "ixxyyzz"
    assert candidate(s = "nnnnooooffffgggg",k = 4) == ""
    assert candidate(s = "aabbbccddeeefffggghhhiiijjjkkklllmmmnnooopppqqqrrrssstttuuuuvvvwwwxxyyzz",k = 3) == "aaccddnnuxxyyzz"
    assert candidate(s = "ppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz",k = 5) == "ppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz"
    assert candidate(s = "mississippiiiiiiiiii",k = 5) == "mississipp"
    assert candidate(s = "aabbccddeeefffggghhhiiiijjjkkklllmmmnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz",k = 3) == "aabbccddinn"
    assert candidate(s = "pppqqqrrrssstttuuuvvvwwwww",k = 5) == "pppqqqrrrssstttuuuvvv"
    assert candidate(s = "aabbccddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqq",k = 4) == "aabbccddeeefffggghhh"
    assert candidate(s = "ppppqqqrrrssstttuuuvvvwwwwwxxxxyyyyzzzz",k = 4) == "qqqrrrssstttuuuvvvw"
    assert candidate(s = "abababababababababababababababab",k = 3) == "abababababababababababababababab"
    assert candidate(s = "mississippiississi",k = 3) == "mississippiississi"
    assert candidate(s = "abcabcabcabc",k = 4) == "abcabcabcabc"
    assert candidate(s = "zzzzyyyyyyyyyzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 7) == "zzzzyy"
    assert candidate(s = "abababababab",k = 3) == "abababababab"
    assert candidate(s = "mmnnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz",k = 3) == "mm"
    assert candidate(s = "abcdefghijkllllllllllllmnopqrstuvwxyz",k = 10) == "abcdefghijkllmnopqrstuvwxyz"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 26) == "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    assert candidate(s = "xyzzzzzzzzxy",k = 6) == "xyzzxy"
    assert candidate(s = "abcdefggggggfedcba",k = 5) == "abcdefgfedcba"
    assert candidate(s = "ababababababababababababababababababababababababababababababababababababab",k = 20) == "ababababababababababababababababababababababababababababababababababababab"
    assert candidate(s = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",k = 10) == "qqqq"
    assert candidate(s = "zzzzzyzzzz",k = 5) == "yzzzz"
    assert candidate(s = "wwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzz",k = 6) == "wwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzzwwzzzzz"
    assert candidate(s = "pppppaaaabbbbcccccccdddddddd",k = 4) == "pccc"
    assert candidate(s = "aabaaaacccaaabbbcccbbccaa",k = 3) == "aababbccaa"
    assert candidate(s = "abcdefghijkllllllllllllmnopqrstuv",k = 11) == "abcdefghijklmnopqrstuv"
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz",k = 10) == "hhhhhhhhxxx"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzz",k = 6) == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy"
    assert candidate(s = "abcdabcdabcdabcdabcdabcd",k = 6) == "abcdabcdabcdabcdabcdabcd"
    assert candidate(s = "xyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzy",k = 5) == "xyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzy"
    assert candidate(s = "aabbccddeeefffggghhhiiiijjjjkkkk",k = 4) == "aabbccddeeefffggghhh"
    assert candidate(s = "pppppppppaaaabbbbccccdddd",k = 4) == "p"
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc",k = 10) == "abcabcabcabcabcabcabcabcabcabc"
    assert candidate(s = "aabbccddeeefffggghhhiiijjjkkklllmnnnooopppqqqrrrssstttuuuvvvwwxxyyzz",k = 3) == "aabbccddmwwxxyyzz"
    assert candidate(s = "xyzzzzzzzzzzzyyxwwwwwwwwwwwwwxvvvvvvvvvvvvvuuuuuuuuuuuuuutttttttttttttsssssssssssssrrrrrrrrrrrrrqqqqqqqqqqqqqpnnnnnnnnnnnnnoommmmmmmmmmmmmllllllllllllllkkkkkkkkkkkkkkjjjjjjjjjjjjjjiiiiiiiiiiiiiiiihhhhhhhhhhhhhhhhhgggggggggggggggggffffffffffffffffeeeeeeeeeeeeeeeeedddddddddddddddddccccccccccccccccccbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaa",k = 20) == "xyzzzzzzzzzzzyyxwwwwwwwwwwwwwxvvvvvvvvvvvvvuuuuuuuuuuuuuutttttttttttttsssssssssssssrrrrrrrrrrrrrqqqqqqqqqqqqqpnnnnnnnnnnnnnoommmmmmmmmmmmmllllllllllllllkkkkkkkkkkkkkkjjjjjjjjjjjjjjiiiiiiiiiiiiiiiihhhhhhhhhhhhhhhhhgggggggggggggggggffffffffffffffffeeeeeeeeeeeeeeeeedddddddddddddddddccccccccccccccccccbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaa"
    assert candidate(s = "mnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba",k = 2) == "lkjihgfedcba"
    assert candidate(s = "mississippiissiippiiissipiissipiissipiissipiissipiissipiissipiissipiis",k = 3) == "mississippiissiippssipiissipiissipiissipiissipiissipiissipiissipiis"
    assert candidate(s = "aaabaaaabbbaaa",k = 3) == "ba"
    assert candidate(s = "aaaabbbbccccdddd",k = 4) == ""
    assert candidate(s = "zzzzzyyyxx",k = 4) == "zyyyxx"
    assert candidate(s = "zzzzzzzzzzzz",k = 5) == "zz"
    assert candidate(s = "zzzzzyyyyyxxxwwwwvvvvuuuuuuttttssssrrrrqqqqppppooooonnnnmmmmmllllkkkkjjjjiiihhhhggggffffeeee",k = 5) == "xxxwwwwvvvvuttttssssrrrrqqqqppppnnnnllllkkkkjjjjiiihhhhggggffffeeee"
    assert candidate(s = "xyzyxyzyxyzyxyzyxyzy",k = 3) == "xyzyxyzyxyzyxyzyxyzy"
    assert candidate(s = "ppppppqqqqqqrrrrrr",k = 6) == ""
    assert candidate(s = "abacabadabacabadabacabadabacabad",k = 4) == "abacabadabacabadabacabadabacabad"
    assert candidate(s = "xyzzzzxyzzzz",k = 5) == "xyzzzzxyzzzz"
    assert candidate(s = "abababababababababababababababab",k = 7) == "abababababababababababababababab"
    assert candidate(s = "abccbaabccbaabccba",k = 3) == "abccbaabccbaabccba"
    assert candidate(s = "aabbbbccccddddaaaabbbbccccddddaaaabbbbccccdddd",k = 4) == "aa"
    assert candidate(s = "aabbccddeeefffgghhiiijjjkkklllmmmnnooopppqqqrrrssstttuuuvvvwww",k = 5) == "aabbccddeeefffgghhiiijjjkkklllmmmnnooopppqqqrrrssstttuuuvvvwww"
    assert candidate(s = "aaaabaaaabaaaabaaaab",k = 4) == ""
    assert candidate(s = "aabbccddeeefff",k = 2) == "ef"
    assert candidate(s = "aaaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeeefffffffff",k = 10) == "bbbbbbbbccccccccddddddddeeeeeeeeefffffffff"
    assert candidate(s = "zzzzzyyyyyxxxxxxwwwwvvvvvuuuuu",k = 5) == "xwwww"
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnoooo",k = 4) == ""
    assert candidate(s = "aabbccccddeeeeffffgggghhhiiijjjkkk",k = 4) == "aabbddhhhiiijjjkkk"
    assert candidate(s = "mnopqrstuvw",k = 2) == "mnopqrstuvw"
    assert candidate(s = "zzzxxxyyyzzzxxxyyy",k = 3) == ""
    assert candidate(s = "abcdefghijklaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbb",k = 10) == "abcdefghijklabbbbbbbb"
    assert candidate(s = "aabbccddeeefffggg",k = 3) == "aabbccdd"
    assert candidate(s = "qqqqwwwwrrrreeee",k = 4) == ""
    assert candidate(s = "mississippiissippi",k = 4) == "mississippiissippi"
    assert candidate(s = "zzzzzyyyyxxxxwwwwvvvvuuuu",k = 5) == "yyyyxxxxwwwwvvvvuuuu"
    assert candidate(s = "abcdefghijkllllllllllmnopqrstuvwxyz",k = 10) == "abcdefghijkmnopqrstuvwxyz"
    assert candidate(s = "zzzzzzzzzz",k = 4) == "zz"
    assert candidate(s = "abababababababababab",k = 5) == "abababababababababab"
    assert candidate(s = "qqwweerrttyyuuiiooppaassddffgghhjjkkllzzxciwoqjfqioejqwojfioqwjfiqwjefioqwjfeiqwjeofiqwjeofiqwjefiqwjf",k = 2) == "xciwoqjfqioejqwojfioqwjfiqwjefioqwjfeiqwjeofiqwjeofiqwjefiqwjf"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 10) == "zzzz"
    assert candidate(s = "mmnnnnoooopprrrssstttuuuuvvvvwwxxxyyyzzzzzz",k = 6) == "mmnnnnoooopprrrssstttuuuuvvvvwwxxxyyy"
    assert candidate(s = "aaaaaaaaabbbbbbbbccccccccddddddddd",k = 8) == "ad"
    assert candidate(s = "abcdefghijaaaaklmnopqrstuuvwxyz",k = 3) == "abcdefghijaklmnopqrstuuvwxyz"
    assert candidate(s = "aabbccddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnoooopppp",k = 5) == "aabbccddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnoooopppp"
    assert candidate(s = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",k = 20) == "qqqqqqqqqqqqqq"
    assert candidate(s = "abbaccccbaa",k = 4) == "abbabaa"
    assert candidate(s = "abcdefghijabcdefghijabcdefghij",k = 10) == "abcdefghijabcdefghijabcdefghij"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 2) == ""
    assert candidate(s = "abcdabcdabcdabcd",k = 3) == "abcdabcdabcdabcd"


