def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "abacabadaba",k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabadaba",k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacabadabacaba",k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabadabacaba",k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyz",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyz",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabc",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabc",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnbvcxzlkjhgfdsapoiuytrewq",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnbvcxzlkjhgfdsapoiuytrewq",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabcaba",k = 0) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabcaba",k = 0) == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "dabdcbdcdcd",k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "dabdcbdcdcd",k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzz",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzz",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaabaaa",k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaabaaa",k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdabcdabcd",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdabcdabcd",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaa",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaa",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyz",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyz",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcde",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcde",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacabadabacaba",k = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabadabacaba",k = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "qqwweerrttyyuuiioopp",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qqwweerrttyyuuiioopp",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabcccdddd",k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabcccdddd",k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyxxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyxxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "lkjghwertyuiopasdfghjklzxcvbnmlkjhgfdwsazxcvbnmlkjhgfdwsazxcvbnmlkjhgfdwsa",k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lkjghwertyuiopasdfghjklzxcvbnmlkjhgfdwsazxcvbnmlkjhgfdwsazxcvbnmlkjhgfdwsa",k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzyyyyyxxxxxwwwwvvvvuttttssssrrrrqqqqppppooooonnnnmmmmmllllkkkkjjjjiiiihhhhggggffffffeeeeee",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzyyyyyxxxxxwwwwvvvvuttttssssrrrrqqqqppppooooonnnnmmmmmllllkkkkjjjjiiiihhhhggggffffffeeeeee",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzzzzzzzzzyxyzzzzzzzzzyxyzzzzzzzzzy",k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzzzzzzzzzyxyzzzzzzzzzyxyzzzzzzzzzy",k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnbvcxzlkjhgfdsapoiuytrewqmnbvcxzlkjhgfdsapoiuytrewqmnbvcxzlkjhgfdsapoiuytrewq",k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnbvcxzlkjhgfdsapoiuytrewqmnbvcxzlkjhgfdsapoiuytrewqmnbvcxzlkjhgfdsapoiuytrewq",k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaabbbcccddddeeeffffffgggggggg",k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaabbbcccddddeeeffffffgggggggg",k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "thisisanexamplestringwithvariousfrequencies",k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "thisisanexamplestringwithvariousfrequencies",k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "almosteveryletterisusedbutnotallabcdefghijklmnopqrstuvwxyzzzzzzzzzzz",k = 2) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "almosteveryletterisusedbutnotallabcdefghijklmnopqrstuvwxyzzzzzzzzzzz",k = 2) == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "thisisaverylongwordthatcontainsmanycharactersandneedscomplexprocessing",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "thisisaverylongwordthatcontainsmanycharactersandneedscomplexprocessing",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbcccccccccccccccc",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbcccccccccccccccc",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaaabbbbbbbbbbbccccccccccdddddddddd",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaaabbbbbbbbbbbccccccccccdddddddddd",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzz",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzz",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyz",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyz",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzzzzzzzzzz",k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzzzzzzzzzz",k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeffffffffggggggghhhhhhhhiiiiiiiiii",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeffffffffggggggghhhhhhhhiiiiiiiiii",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "unevenfrequenciesaxbxcxdxeuxyvxuyvyvxvyvxvyvxvyvxvyvxvyvxyvxyvxyvxyvxyvxyvxyvxyvxyvxyvxyvxy",k = 10) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "unevenfrequenciesaxbxcxdxeuxyvxuyvyvxvyvxvyvxvyvxvyvxvyvxyvxyvxyvxyvxyvxyvxyvxyvxyvxyvxyvxy",k = 10) == 23: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaabbbccccdddddeeeeeffffffffggggghhhhhiiiiijjjjjkkkkklllllmmmmmnnnnnooooo",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaabbbccccdddddeeeeeffffffffggggghhhhhiiiiijjjjjkkkkklllllmmmmmnnnnnooooo",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzz",k = 1) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzz",k = 1) == 17: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghij",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghij",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "ppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwertyuiopasdfghjklzxcvbnm",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwertyuiopasdfghjklzxcvbnm",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "verylongstringwithrepeatingcharactersaaaaaaaaaabbbbbbbbbbcccccccccc",k = 4) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "verylongstringwithrepeatingcharactersaaaaaaaaaabbbbbbbbbbcccccccccc",k = 4) == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "ppppppppppppppppppppppppppppppppppppppppppppppppppppp",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ppppppppppppppppppppppppppppppppppppppppppppppppppppp",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdeabcdabcdeabcdeabcdeabcdeabcde",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdeabcdabcdeabcdeabcdeabcdeabcde",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "ppppqqqqrrrsssttttuuuuvvvvwwwwxxxxxyyyyyzzzzzaaaaabbbbccccddddeeeeffffgggghhhhiiii",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ppppqqqqrrrsssttttuuuuvvvvwwwwxxxxxyyyyyzzzzzaaaaabbbbccccddddeeeeffffgggghhhhiiii",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbaaccddccbbbaaadddcccbbaaa",k = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbaaccddccbbbaaadddcccbbaaa",k = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabcabcabcabcabcabcabc",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabcabcabcabcabcabcabc",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzqqqqqqqqqq",k = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzqqqqqqqqqq",k = 4) == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "abacabadaba",k = 2) == 3
    assert candidate(word = "abacabadabacaba",k = 3) == 4
    assert candidate(word = "xyz",k = 0) == 0
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 10) == 0
    assert candidate(word = "abcabcabc",k = 1) == 0
    assert candidate(word = "mnbvcxzlkjhgfdsapoiuytrewq",k = 5) == 0
    assert candidate(word = "aabcaba",k = 0) == 3
    assert candidate(word = "dabdcbdcdcd",k = 2) == 2
    assert candidate(word = "zzzzz",k = 0) == 0
    assert candidate(word = "aaabaaa",k = 2) == 1
    assert candidate(word = "abcdabcdabcd",k = 1) == 0
    assert candidate(word = "aaaaa",k = 0) == 0
    assert candidate(word = "xyz",k = 1) == 0
    assert candidate(word = "abcde",k = 3) == 0
    assert candidate(word = "abacabadabacaba",k = 1) == 6
    assert candidate(word = "qqwweerrttyyuuiioopp",k = 2) == 0
    assert candidate(word = "aabcccdddd",k = 1) == 2
    assert candidate(word = "xyxxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",k = 2) == 0
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 0) == 0
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 10) == 0
    assert candidate(word = "lkjghwertyuiopasdfghjklzxcvbnmlkjhgfdwsazxcvbnmlkjhgfdwsazxcvbnmlkjhgfdwsa",k = 15) == 0
    assert candidate(word = "zzzzzyyyyyxxxxxwwwwvvvvuttttssssrrrrqqqqppppooooonnnnmmmmmllllkkkkjjjjiiiihhhhggggffffffeeeeee",k = 5) == 0
    assert candidate(word = "xyzzzzzzzzzyxyzzzzzzzzzyxyzzzzzzzzzy",k = 5) == 9
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 3) == 0
    assert candidate(word = "mnbvcxzlkjhgfdsapoiuytrewqmnbvcxzlkjhgfdsapoiuytrewqmnbvcxzlkjhgfdsapoiuytrewq",k = 8) == 0
    assert candidate(word = "aaabbbcccddddeeeffffffgggggggg",k = 4) == 1
    assert candidate(word = "thisisanexamplestringwithvariousfrequencies",k = 3) == 4
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 5) == 0
    assert candidate(word = "almosteveryletterisusedbutnotallabcdefghijklmnopqrstuvwxyzzzzzzzzzzz",k = 2) == 17
    assert candidate(word = "thisisaverylongwordthatcontainsmanycharactersandneedscomplexprocessing",k = 10) == 0
    assert candidate(word = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbcccccccccccccccc",k = 2) == 0
    assert candidate(word = "aaaaaaaaaaabbbbbbbbbbbccccccccccdddddddddd",k = 5) == 0
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 25) == 0
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzz",k = 0) == 0
    assert candidate(word = "abcdefghijklmnopqrstuvwxyz",k = 0) == 0
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzzzzzzzzzz",k = 5) == 4
    assert candidate(word = "aaaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeffffffffggggggghhhhhhhhiiiiiiiiii",k = 3) == 0
    assert candidate(word = "unevenfrequenciesaxbxcxdxeuxyvxuyvyvxvyvxvyvxvyvxvyvxvyvxyvxyvxyvxyvxyvxyvxyvxyvxyvxyvxyvxy",k = 10) == 23
    assert candidate(word = "aaaaaabbbccccdddddeeeeeffffffffggggghhhhhiiiiijjjjjkkkkklllllmmmmmnnnnnooooo",k = 5) == 0
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzz",k = 1) == 17
    assert candidate(word = "abcdefghij",k = 0) == 0
    assert candidate(word = "ppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz",k = 10) == 0
    assert candidate(word = "qwertyuiopasdfghjklzxcvbnm",k = 10) == 0
    assert candidate(word = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 10) == 0
    assert candidate(word = "verylongstringwithrepeatingcharactersaaaaaaaaaabbbbbbbbbbcccccccccc",k = 4) == 20
    assert candidate(word = "ppppppppppppppppppppppppppppppppppppppppppppppppppppp",k = 0) == 0
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 0
    assert candidate(word = "abcdeabcdabcdeabcdeabcdeabcdeabcde",k = 2) == 0
    assert candidate(word = "ppppqqqqrrrsssttttuuuuvvvvwwwwxxxxxyyyyyzzzzzaaaaabbbbccccddddeeeeffffgggghhhhiiii",k = 5) == 0
    assert candidate(word = "aabbaaccddccbbbaaadddcccbbaaa",k = 1) == 6
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 0) == 0
    assert candidate(word = "abcabcabcabcabcabcabcabcabcabc",k = 1) == 0
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzqqqqqqqqqq",k = 4) == 6


