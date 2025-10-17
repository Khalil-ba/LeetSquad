def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word1 = "leetcode",word2 = "coeddlet") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "leetcode",word2 = "coeddlet") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaa",word2 = "bbb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaa",word2 = "bbb") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaabbbbccdddd",word2 = "bbbbaacdddd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaabbbbccdddd",word2 = "bbbbaacdddd") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcc",word2 = "ccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcc",word2 = "ccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abc",word2 = "bca") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abc",word2 = "bca") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabc",word2 = "bcbcbcbcb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabc",word2 = "bcbcbcbcb") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcde",word2 = "edcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcde",word2 = "edcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "cabbba",word2 = "abbccc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "cabbba",word2 = "abbccc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzz",word2 = "zzxy") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzz",word2 = "zzxy") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyz",word2 = "zyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyz",word2 = "zyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "abce") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "abce") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaabbbbcc",word2 = "bbbcccaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaabbbbcc",word2 = "bbbcccaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "uau",word2 = "ssx") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "uau",word2 = "ssx") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaabbbbccddd",word2 = "bbbccdddcccc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaabbbbccddd",word2 = "bbbccdddcccc") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbbbccc",word2 = "bbcccaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbbbccc",word2 = "bbcccaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abab",word2 = "baba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abab",word2 = "baba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaabbbbcc",word2 = "aaaabbbcc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaabbbbcc",word2 = "aaaabbbcc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "a",word2 = "aa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "a",word2 = "aa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aab",word2 = "bba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aab",word2 = "bba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "dcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "dcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaabbbbccccdddd",word2 = "ddddeeeeffffgggg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaabbbbccccdddd",word2 = "ddddeeeeffffgggg") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaabbcccddeeefffggghhhhiiiii",word2 = "iiiiihhhgggfffeeedddcccbbaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaabbcccddeeefffggghhhhiiiii",word2 = "iiiiihhhgggfffeeedddcccbbaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzxyzxyz",word2 = "zyxzyxzyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzxyzxyz",word2 = "zyxzyxzyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacabadabacaba",word2 = "bbacabadabacaba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacabadabacaba",word2 = "bbacabadabacaba") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaabbcccddddeeeeeffffffgggggghhhhhiiiijjjjkkkkklllllmmmmnnooooppqqrrsstttuuuuuvvvvvvvwwxxxxxyyyyzzzzz",word2 = "zzzzzyyyyxxxwwwvvvvvvuuuuutttssrrqqppoonnmmllkkjjiihhhgggfffddddccccbbbbaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaabbcccddddeeeeeffffffgggggghhhhhiiiijjjjkkkkklllllmmmmnnooooppqqrrsstttuuuuuvvvvvvvwwxxxxxyyyyzzzzz",word2 = "zzzzzyyyyxxxwwwvvvvvvuuuuutttssrrqqppoonnmmllkkjjiihhhgggfffddddccccbbbbaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeff",word2 = "ffeeddccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeff",word2 = "ffeeddccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaabbbcccdddeeefff",word2 = "ffeeeedddcccbbbaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaabbbcccdddeeefff",word2 = "ffeeeedddcccbbbaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "ppissimissi") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "ppissimissi") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcabcabcd",word2 = "dcbaababdcbaabab") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcabcabcd",word2 = "dcbaababdcbaabab") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacabadabacaba",word2 = "bacabacababacab") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacabadabacaba",word2 = "bacabacababacab") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxyywwvvuuttssrrqqppoonnmmllkkjjiihhggffeeeeddccbbaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxyywwvvuuttssrrqqppoonnmmllkkjjiihhggffeeeeddccbbaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "ppppoooonnnnmmmlllkkeeeeeddcccbbbaaa",word2 = "aaaaaaaaabbbbbbccccdddddeeeeeeeekkkkkklllllmmmmmmmnnnnnnnnoooooooooppppppp") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "ppppoooonnnnmmmlllkkeeeeeddcccbbbaaa",word2 = "aaaaaaaaabbbbbbccccdddddeeeeeeeekkkkkklllllmmmmmmmnnnnnnnnoooooooooppppppp") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "qqqwwwweeerrrttt",word2 = "tttwwweerrrqqq") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "qqqwwwweeerrrttt",word2 = "tttwwweerrrqqq") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabc",word2 = "ccbbbaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabc",word2 = "ccbbbaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "qwertypoiuytrewq",word2 = "poiuytrewqqwertypo") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "qwertypoiuytrewq",word2 = "poiuytrewqqwertypo") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefabcdefabcdef",word2 = "fedcbafedcbafedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefabcdefabcdef",word2 = "fedcbafedcbafedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghij",word2 = "jihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghij",word2 = "jihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefgh",word2 = "hgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefgh",word2 = "hgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacabadabacaba",word2 = "cbacbacbcacbacb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacabadabacaba",word2 = "cbacbacbcacbacb") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefg",word2 = "gfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefg",word2 = "gfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "loooooonnnngggggwwwoooorrrrddddsssaaammmmeeeerrttttyyyyyyyyyyyynnnnnnnnnn",word2 = "nnnnnnnnnnyyyyyyyyyyyttttyyyyymmmeeraatttddddsssaaawwwggggnnnllllloooooo") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "loooooonnnngggggwwwoooorrrrddddsssaaammmmeeeerrttttyyyyyyyyyyyynnnnnnnnnn",word2 = "nnnnnnnnnnyyyyyyyyyyyttttyyyyymmmeeraatttddddsssaaawwwggggnnnllllloooooo") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xylophone",word2 = "phonexylo") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xylophone",word2 = "phonexylo") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijklopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijklopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "abcdefghijklmnopqrstuvwxyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "abcdefghijklmnopqrstuvwxyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefabcabc",word2 = "abcabcabcdef") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefabcabc",word2 = "abcabcabcdef") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaabbbbcccccccdddddddd",word2 = "ddddddddcccccccbbbbaaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaabbbbcccccccdddddddd",word2 = "ddddddddcccccccbbbbaaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mnopqr",word2 = "rpqomn") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mnopqr",word2 = "rpqomn") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "ppiimssisss") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "ppiimssisss") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttssrrqppoonnmlkkjjiihhggffeeeeddccbbaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttssrrqppoonnmlkkjjiihhggffeeeeddccbbaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "anotherexample",word2 = "mpleaxarnothee") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "anotherexample",word2 = "mpleaxarnothee") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaabbbbbccccc",word2 = "bbbbbcccccaaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaabbbbbccccc",word2 = "bbbbbcccccaaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzzzyyyxxx",word2 = "yyyxxxzzzzzy") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzzzyyyxxx",word2 = "yyyxxxzzzzzy") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "yzxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "yzxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzxyzxyzxyzxyzxyzxyz",word2 = "zyxzyxzyxzyxzyxzyxzyxzyxzyx") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzxyzxyzxyzxyzxyzxyz",word2 = "zyxzyxzyxzyxzyxzyxzyxzyxzyx") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabccddddeeeeefffffff",word2 = "eeeeeeffffffdddddcccbaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabccddddeeeeefffffff",word2 = "eeeeeeffffffdddddcccbaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mnopqr",word2 = "rstuvw") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mnopqr",word2 = "rstuvw") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeff",word2 = "abcdeffedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeff",word2 = "abcdeffedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "abcdefghijklmnopqrstuvxyzmnopqrstuvwxyzabcdefg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "abcdefghijklmnopqrstuvxyzmnopqrstuvwxyzabcdefg") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "uniqueletters",word2 = "letterniquesu") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "uniqueletters",word2 = "letterniquesu") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxyywwvvuuttssrrqqlloonnmmllkkjjiihhggeeddbbaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxyywwvvuuttssrrqqlloonnmmllkkjjiihhggeeddbbaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabcabcabcabcabcabcabcabc",word2 = "bcabacabcabacabcabacabcabacabcabac") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabcabcabcabcabcabcabcabc",word2 = "bcabacabcabacabcabacabcabacabcabac") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijk",word2 = "abcdefghijl") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijk",word2 = "abcdefghijl") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "thisisatest",word2 = "esttasisthi") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "thisisatest",word2 = "esttasisthi") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "qqwweerrttyyuuiiooppllaaassddffgg",word2 = "ggffddssaallooppuiiyyttreeewwqq") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "qqwweerrttyyuuiiooppllaaassddffgg",word2 = "ggffddssaallooppuiiyyttreeewwqq") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacabadaba",word2 = "dabacababad") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacabadaba",word2 = "dabacababad") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "oconsinolpnacirosccvilcooimmutapernovulcrosmicn") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "oconsinolpnacirosccvilcooimmutapernovulcrosmicn") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabcabc",word2 = "cccbbbaaabbb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabcabc",word2 = "cccbbbaaabbb") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "leetcode",word2 = "codeleet") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "leetcode",word2 = "codeleet") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "z",word2 = "z") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "z",word2 = "z") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbaa",word2 = "bbaabb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbaa",word2 = "bbaabb") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaabbbccc",word2 = "bbbaaacc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaabbbccc",word2 = "bbbaaacc") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "transform",word2 = "rmorfnapt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "transform",word2 = "rmorfnapt") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaabbbbccccddddeeeeeffffffgggggg",word2 = "ggggggffffffeeeeeeeeeccccbbbbaaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaabbbbccccddddeeeeeffffffgggggg",word2 = "ggggggffffffeeeeeeeeeccccbbbbaaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacabadabacabad",word2 = "badacabdacabad") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacabadabacabad",word2 = "badacabdacabad") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "hello",word2 = "ollhe") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "hello",word2 = "ollhe") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "uniquestring",word2 = "stringunique") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "uniquestring",word2 = "stringunique") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdef",word2 = "gfedcb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdef",word2 = "gfedcb") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyxyxyxyxyxyxyxyxyxy",word2 = "yyxyxyxyxyxyxyxyxyxxyx") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyxyxyxyxyxyxyxyxyxy",word2 = "yyxyxyxyxyxyxyxyxyxxyx") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaabbbbccccdddd",word2 = "ddddccccbbbbaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaabbbbccccdddd",word2 = "ddddccccbbbbaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcde",word2 = "fghij") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcde",word2 = "fghij") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",word2 = "ddddccccbbbbaaaaaaddddccccbbbbaaaaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",word2 = "ddddccccbbbbaaaaaaddddccccbbbbaaaaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbbcccc",word2 = "cccbbbaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbbcccc",word2 = "cccbbbaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeee",word2 = "eeeedddccbbbaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeee",word2 = "eeeedddccbbbaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "thisisatest",word2 = "esttisita") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "thisisatest",word2 = "esttisita") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaabbbcccddd",word2 = "ddddcccbbbbaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaabbbcccddd",word2 = "ddddcccbbbbaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijabcdefghijabcdefghij",word2 = "abcdefghijabcdefghijabcdefghij") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijabcdefghijabcdefghij",word2 = "abcdefghijabcdefghijabcdefghij") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzzzzzzz",word2 = "zzzzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzzzzzzz",word2 = "zzzzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdeabcde",word2 = "edcbaedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdeabcde",word2 = "edcbaedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdabcdabcdabcdabcd",word2 = "dcbaabcdabcdabcdabcdabcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdabcdabcdabcdabcd",word2 = "dcbaabcdabcdabcdabcdabcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzzyyxwwvvuuttrrqqppoonnmmllkkiijjgghhffeeeeddccbbaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzzyyxwwvvuuttrrqqppoonnmmllkkiijjgghhffeeeeddccbbaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdexyz",word2 = "zyxwvuts") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdexyz",word2 = "zyxwvuts") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "qqwweerrttyyuuiiooppaassddffgg",word2 = "ggffddssaappoouuiittyyerrrwwqq") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "qqwweerrttyyuuiiooppaassddffgg",word2 = "ggffddssaappoouuiittyyerrrwwqq") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefg",word2 = "ghijklm") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefg",word2 = "ghijklm") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvuuttssrrqqlloonnmmllkkjjiihhggeeddbbaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvuuttssrrqqlloonnmmllkkjjiihhggeeddbbaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaabbbbccccddddeee",word2 = "eeedddccccbbbbaaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaabbbbccccddddeee",word2 = "eeedddccccbbbbaaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcd",word2 = "dcbaabcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcd",word2 = "dcbaabcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "closestrings",word2 = "stringsclose") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "closestrings",word2 = "stringsclose") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaabbbbccccdddd",word2 = "ddddccccbbbbaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaabbbbccccdddd",word2 = "ddddccccbbbbaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzzzz",word2 = "zzzzxy") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzzzz",word2 = "zzzzxy") == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word1 = "leetcode",word2 = "coeddlet") == False
    assert candidate(word1 = "aaa",word2 = "bbb") == False
    assert candidate(word1 = "aaabbbbccdddd",word2 = "bbbbaacdddd") == False
    assert candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(word1 = "aabbcc",word2 = "ccbbaa") == True
    assert candidate(word1 = "abc",word2 = "bca") == True
    assert candidate(word1 = "abcabcabc",word2 = "bcbcbcbcb") == False
    assert candidate(word1 = "abcde",word2 = "edcba") == True
    assert candidate(word1 = "cabbba",word2 = "abbccc") == True
    assert candidate(word1 = "xyzz",word2 = "zzxy") == True
    assert candidate(word1 = "xyz",word2 = "zyx") == True
    assert candidate(word1 = "abcd",word2 = "abce") == False
    assert candidate(word1 = "aaabbbbcc",word2 = "bbbcccaaa") == False
    assert candidate(word1 = "uau",word2 = "ssx") == False
    assert candidate(word1 = "aaabbbbccddd",word2 = "bbbccdddcccc") == False
    assert candidate(word1 = "aabbbbccc",word2 = "bbcccaaaa") == True
    assert candidate(word1 = "abab",word2 = "baba") == True
    assert candidate(word1 = "aaabbbbcc",word2 = "aaaabbbcc") == True
    assert candidate(word1 = "a",word2 = "aa") == False
    assert candidate(word1 = "aab",word2 = "bba") == True
    assert candidate(word1 = "abcd",word2 = "dcba") == True
    assert candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy") == False
    assert candidate(word1 = "aaaabbbbccccdddd",word2 = "ddddeeeeffffgggg") == False
    assert candidate(word1 = "aaabbcccddeeefffggghhhhiiiii",word2 = "iiiiihhhgggfffeeedddcccbbaaa") == False
    assert candidate(word1 = "xyzxyzxyz",word2 = "zyxzyxzyx") == True
    assert candidate(word1 = "abacabadabacaba",word2 = "bbacabadabacaba") == False
    assert candidate(word1 = "aaabbcccddddeeeeeffffffgggggghhhhhiiiijjjjkkkkklllllmmmmnnooooppqqrrsstttuuuuuvvvvvvvwwxxxxxyyyyzzzzz",word2 = "zzzzzyyyyxxxwwwvvvvvvuuuuutttssrrqqppoonnmmllkkjjiihhhgggfffddddccccbbbbaaa") == False
    assert candidate(word1 = "aabbccddeeff",word2 = "ffeeddccbbaa") == True
    assert candidate(word1 = "aaabbbcccdddeeefff",word2 = "ffeeeedddcccbbbaaa") == False
    assert candidate(word1 = "mississippi",word2 = "ppissimissi") == True
    assert candidate(word1 = "abcdabcabcabcd",word2 = "dcbaababdcbaabab") == False
    assert candidate(word1 = "abacabadabacaba",word2 = "bacabacababacab") == False
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxyywwvvuuttssrrqqppoonnmmllkkjjiihhggffeeeeddccbbaa") == False
    assert candidate(word1 = "ppppoooonnnnmmmlllkkeeeeeddcccbbbaaa",word2 = "aaaaaaaaabbbbbbccccdddddeeeeeeeekkkkkklllllmmmmmmmnnnnnnnnoooooooooppppppp") == False
    assert candidate(word1 = "qqqwwwweeerrrttt",word2 = "tttwwweerrrqqq") == False
    assert candidate(word1 = "abcabcabc",word2 = "ccbbbaaa") == False
    assert candidate(word1 = "qwertypoiuytrewq",word2 = "poiuytrewqqwertypo") == False
    assert candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == False
    assert candidate(word1 = "abcdefabcdefabcdef",word2 = "fedcbafedcbafedcba") == True
    assert candidate(word1 = "abcdefghij",word2 = "jihgfedcba") == True
    assert candidate(word1 = "abcdefgh",word2 = "hgfedcba") == True
    assert candidate(word1 = "abacabadabacaba",word2 = "cbacbacbcacbacb") == False
    assert candidate(word1 = "abcdefg",word2 = "gfedcba") == True
    assert candidate(word1 = "loooooonnnngggggwwwoooorrrrddddsssaaammmmeeeerrttttyyyyyyyyyyyynnnnnnnnnn",word2 = "nnnnnnnnnnyyyyyyyyyyyttttyyyyymmmeeraatttddddsssaaawwwggggnnnllllloooooo") == False
    assert candidate(word1 = "xylophone",word2 = "phonexylo") == True
    assert candidate(word1 = "abcdefghijklopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(word1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(word1 = "abcdefabcabc",word2 = "abcabcabcdef") == True
    assert candidate(word1 = "aaaaabbbbcccccccdddddddd",word2 = "ddddddddcccccccbbbbaaaaa") == True
    assert candidate(word1 = "mnopqr",word2 = "rpqomn") == True
    assert candidate(word1 = "mississippi",word2 = "ppiimssisss") == False
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttssrrqppoonnmlkkjjiihhggffeeeeddccbbaa") == False
    assert candidate(word1 = "anotherexample",word2 = "mpleaxarnothee") == True
    assert candidate(word1 = "aaaaabbbbbccccc",word2 = "bbbbbcccccaaaaa") == True
    assert candidate(word1 = "zzzzzzyyyxxx",word2 = "yyyxxxzzzzzy") == False
    assert candidate(word1 = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "yzxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy") == False
    assert candidate(word1 = "xyzxyzxyzxyzxyzxyzxyz",word2 = "zyxzyxzyxzyxzyxzyxzyxzyxzyx") == False
    assert candidate(word1 = "aabccddddeeeeefffffff",word2 = "eeeeeeffffffdddddcccbaaa") == False
    assert candidate(word1 = "mnopqr",word2 = "rstuvw") == False
    assert candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == False
    assert candidate(word1 = "aabbccddeeff",word2 = "abcdeffedcba") == True
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "abcdefghijklmnopqrstuvxyzmnopqrstuvwxyzabcdefg") == False
    assert candidate(word1 = "uniqueletters",word2 = "letterniquesu") == True
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxyywwvvuuttssrrqqlloonnmmllkkjjiihhggeeddbbaa") == False
    assert candidate(word1 = "abcabcabcabcabcabcabcabcabcabc",word2 = "bcabacabcabacabcabacabcabacabcabac") == False
    assert candidate(word1 = "abcdefghijk",word2 = "abcdefghijl") == False
    assert candidate(word1 = "thisisatest",word2 = "esttasisthi") == True
    assert candidate(word1 = "qqwweerrttyyuuiiooppllaaassddffgg",word2 = "ggffddssaallooppuiiyyttreeewwqq") == False
    assert candidate(word1 = "abacabadaba",word2 = "dabacababad") == False
    assert candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "oconsinolpnacirosccvilcooimmutapernovulcrosmicn") == False
    assert candidate(word1 = "abcabcabcabc",word2 = "cccbbbaaabbb") == False
    assert candidate(word1 = "leetcode",word2 = "codeleet") == True
    assert candidate(word1 = "z",word2 = "z") == True
    assert candidate(word1 = "aabbaa",word2 = "bbaabb") == True
    assert candidate(word1 = "aaabbbccc",word2 = "bbbaaacc") == False
    assert candidate(word1 = "transform",word2 = "rmorfnapt") == False
    assert candidate(word1 = "aaaabbbbccccddddeeeeeffffffgggggg",word2 = "ggggggffffffeeeeeeeeeccccbbbbaaaa") == False
    assert candidate(word1 = "abacabadabacabad",word2 = "badacabdacabad") == False
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True
    assert candidate(word1 = "hello",word2 = "ollhe") == True
    assert candidate(word1 = "uniquestring",word2 = "stringunique") == True
    assert candidate(word1 = "abcdef",word2 = "gfedcb") == False
    assert candidate(word1 = "xyxyxyxyxyxyxyxyxyxy",word2 = "yyxyxyxyxyxyxyxyxyxxyx") == False
    assert candidate(word1 = "aaaaabbbbccccdddd",word2 = "ddddccccbbbbaaa") == False
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True
    assert candidate(word1 = "abcde",word2 = "fghij") == False
    assert candidate(word1 = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",word2 = "ddddccccbbbbaaaaaaddddccccbbbbaaaaaa") == False
    assert candidate(word1 = "aabbbcccc",word2 = "cccbbbaaa") == False
    assert candidate(word1 = "aabbccddeee",word2 = "eeeedddccbbbaaa") == False
    assert candidate(word1 = "thisisatest",word2 = "esttisita") == False
    assert candidate(word1 = "aaabbbcccddd",word2 = "ddddcccbbbbaaa") == False
    assert candidate(word1 = "abcdefghijabcdefghijabcdefghij",word2 = "abcdefghijabcdefghijabcdefghij") == True
    assert candidate(word1 = "zzzzzzzzzz",word2 = "zzzzzzzzzz") == True
    assert candidate(word1 = "abcdeabcde",word2 = "edcbaedcba") == True
    assert candidate(word1 = "abcdabcdabcdabcdabcdabcd",word2 = "dcbaabcdabcdabcdabcdabcd") == True
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzzyyxwwvvuuttrrqqppoonnmmllkkiijjgghhffeeeeddccbbaa") == False
    assert candidate(word1 = "abcdexyz",word2 = "zyxwvuts") == False
    assert candidate(word1 = "qqwweerrttyyuuiiooppaassddffgg",word2 = "ggffddssaappoouuiittyyerrrwwqq") == False
    assert candidate(word1 = "abcdefg",word2 = "ghijklm") == False
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvuuttssrrqqlloonnmmllkkjjiihhggeeddbbaa") == False
    assert candidate(word1 = "aaaabbbbccccddddeee",word2 = "eeedddccccbbbbaaaa") == False
    assert candidate(word1 = "abcdabcd",word2 = "dcbaabcd") == True
    assert candidate(word1 = "closestrings",word2 = "stringsclose") == True
    assert candidate(word1 = "aaaabbbbccccdddd",word2 = "ddddccccbbbbaaaa") == True
    assert candidate(word1 = "xyzzzz",word2 = "zzzzxy") == True


