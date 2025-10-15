def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word1 = "abcde",word2 = "fghij") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcde",word2 = "fghij") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyz",word2 = "zyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyz",word2 = "zyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaa",word2 = "bbb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaa",word2 = "bbb") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "ac",word2 = "b") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "ac",word2 = "b") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "unique",word2 = "letters") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "unique",word2 = "letters") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcc",word2 = "aab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcc",word2 = "aab") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabb",word2 = "ccdd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabb",word2 = "ccdd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "hello",word2 = "world") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "hello",word2 = "world") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "ab",word2 = "cd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "ab",word2 = "cd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyz",word2 = "xyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyz",word2 = "xyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "efgh") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "efgh") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcc",word2 = "xyz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcc",word2 = "xyz") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "dcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "dcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "same",word2 = "same") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "same",word2 = "same") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcc",word2 = "xxxyyzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcc",word2 = "xxxyyzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaa",word2 = "bbbb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaa",word2 = "bbbb") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "qrstuvwxyz",word2 = "abcdefghijklmnopqrstuvwxyz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "qrstuvwxyz",word2 = "abcdefghijklmnopqrstuvwxyz") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "single",word2 = "letter") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "single",word2 = "letter") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "missouri") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "missouri") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "penelope") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "penelope") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzz",word2 = "zzxx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzz",word2 = "zzxx") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaaa",word2 = "bbbbbbb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaaa",word2 = "bbbbbbb") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "oneonetwo",word2 = "twotwoone") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "oneonetwo",word2 = "twotwoone") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "uniquecharacters",word2 = "distinctcharacters") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "uniquecharacters",word2 = "distinctcharacters") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaabbbbbaaaa",word2 = "cccccbccccbcccc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaabbbbbaaaa",word2 = "cccccbccccbcccc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "abcdefghijlkmnopqrstuvwxyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "abcdefghijlkmnopqrstuvwxyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeff",word2 = "aabbccddeeff") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeff",word2 = "aabbccddeeff") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "repeatedletters",word2 = "differentletters") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "repeatedletters",word2 = "differentletters") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "unique",word2 = "distinct") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "unique",word2 = "distinct") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaabbbbbccccc",word2 = "dddddeeeeeffffff") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaabbbbbccccc",word2 = "dddddeeeeeffffff") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "onetwothreefour",word2 = "five") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "onetwothreefour",word2 = "five") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "almost",word2 = "almost") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "almost",word2 = "almost") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaabbbb",word2 = "cccddd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaabbbb",word2 = "cccddd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacabadabacaba",word2 = "bacbabacbacbacb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacabadabacaba",word2 = "bacbabacbacbacb") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaabbbb",word2 = "ccccc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaabbbb",word2 = "ccccc") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "efghijklmnopqrstuvwxyz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "efghijklmnopqrstuvwxyz") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvttrrssppoonnmmllkkjjiihhggffeeddccbbaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvttrrssppoonnmmllkkjjiihhggffeeddccbbaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijklmnopqrstuvwxy",word2 = "zyxwvutsrqponmlkjihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijklmnopqrstuvwxy",word2 = "zyxwvutsrqponmlkjihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "samechars",word2 = "samechars") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "samechars",word2 = "samechars") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghij",word2 = "jihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghij",word2 = "jihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefg",word2 = "hijklmnopqrstuv") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefg",word2 = "hijklmnopqrstuv") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "longerstringwithrepeatedcharacters",word2 = "short") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "longerstringwithrepeatedcharacters",word2 = "short") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyz",word2 = "zyxwvut") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyz",word2 = "zyxwvut") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefgh",word2 = "hgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefgh",word2 = "hgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdef",word2 = "ghijklmnopqrstuvwxyz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdef",word2 = "ghijklmnopqrstuvwxyz") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefg",word2 = "hijklmnop") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefg",word2 = "hijklmnop") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacabadabacaba",word2 = "bcadcbadcbadcbc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacabadabacaba",word2 = "bcadcbadcbadcbc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyxzyzxzyx",word2 = "zyxzyzxzyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyxzyzxzyx",word2 = "zyxzyzxzyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdabcd",word2 = "dcbaabcdabcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdabcd",word2 = "dcbaabcdabcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzz",word2 = "xxxyyyzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzz",word2 = "xxxyyyzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abracadabra",word2 = "alakazam") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abracadabra",word2 = "alakazam") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijj",word2 = "zzzzzyyyxxwwvvuuttssrrqqppoonnmmllijkkihgfedcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijj",word2 = "zzzzzyyyxxwwvvuuttssrrqqppoonnmmllijkkihgfedcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacabadabacaba",word2 = "zzzzzzzzzzzzzzzzz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacabadabacaba",word2 = "zzzzzzzzzzzzzzzzz") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabcabc",word2 = "abcabcabcabc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabcabc",word2 = "abcabcabcabc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaa",word2 = "bbbbbb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaa",word2 = "bbbbbb") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "almost",word2 = "equal") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "almost",word2 = "equal") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabc",word2 = "defdefdef") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabc",word2 = "defdefdef") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "ababababab",word2 = "bababababa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "ababababab",word2 = "bababababa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "almostthesame",word2 = "almostthesamee") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "almostthesame",word2 = "almostthesamee") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghij",word2 = "mnopqrstuv") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghij",word2 = "mnopqrstuv") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzzzzzzzzz",word2 = "aaaaaaaaaaab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzzzzzzzzz",word2 = "aaaaaaaaaaab") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "almostthesame",word2 = "almostthesame") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "almostthesame",word2 = "almostthesame") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzz",word2 = "xyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzz",word2 = "xyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "thisisaverylongwordwithrepeatedcharacters",word2 = "anotherlongwordwithdifferentcharacters") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "thisisaverylongwordwithrepeatedcharacters",word2 = "anotherlongwordwithdifferentcharacters") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "unique",word2 = "words") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "unique",word2 = "words") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "unique",word2 = "characters") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "unique",word2 = "characters") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcc",word2 = "aabbcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcc",word2 = "aabbcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdef",word2 = "ghijkl") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdef",word2 = "ghijkl") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "thisisaverylongword",word2 = "whichhasmanycharacters") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "thisisaverylongword",word2 = "whichhasmanycharacters") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mnopqr",word2 = "rstuvw") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mnopqr",word2 = "rstuvw") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaaaabbbbbbb",word2 = "ccccccccddddd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaaaabbbbbbb",word2 = "ccccccccddddd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "louisiana") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "louisiana") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcceeddee",word2 = "fghhiijjkk") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcceeddee",word2 = "fghhiijjkk") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijklmnop",word2 = "qrstuvwxyz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijklmnop",word2 = "qrstuvwxyz") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaabbbbcccc",word2 = "bbbbccccdddd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaabbbbcccc",word2 = "bbbbccccdddd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaaaa",word2 = "bbbbbbbb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaaaa",word2 = "bbbbbbbb") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaabbbbbcccccdddddeeeee",word2 = "eeeeeaaaaabbbbbcccccddddd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaabbbbbcccccdddddeeeee",word2 = "eeeeeaaaaabbbbbcccccddddd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "pennsylvania") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "pennsylvania") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzz",word2 = "zzxy") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzz",word2 = "zzxy") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccdd",word2 = "efgghhii") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccdd",word2 = "efgghhii") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaabbbbbcccccdddddeeeee",word2 = "fffffggggghhhhhiiiii") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaabbbbbcccccdddddeeeee",word2 = "fffffggggghhhhhiiiii") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefgh",word2 = "ijklmnop") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefgh",word2 = "ijklmnop") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "repeatrepeat",word2 = "repeatrepeat") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "repeatrepeat",word2 = "repeatrepeat") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcc",word2 = "ddeeff") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcc",word2 = "ddeeff") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijk",word2 = "klmnopqrstu") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijk",word2 = "klmnopqrstu") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbc",word2 = "ccdde") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbc",word2 = "ccdde") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "complex",word2 = "inputs") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "complex",word2 = "inputs") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdabcd",word2 = "dcbaabcdabdc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdabcd",word2 = "dcbaabcdabdc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzzyyxxwwvvuuttoosssrrqqppoonnmlkkjjiihhggffeeddccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzzyyxxwwvvuuttoosssrrqqppoonnmlkkjjiihhggffeeddccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "one",word2 = "twothreefour") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "one",word2 = "twothreefour") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzz",word2 = "yzxx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzz",word2 = "yzxx") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "singlechar",word2 = "different") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "singlechar",word2 = "different") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcc",word2 = "ddeeffgghhiijj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcc",word2 = "ddeeffgghhiijj") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefg",word2 = "abcdefg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefg",word2 = "abcdefg") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "characters",word2 = "words") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "characters",word2 = "words") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "banana") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "banana") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "hellohello",word2 = "worldworld") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "hellohello",word2 = "worldworld") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeff",word2 = "ggffeeddccbaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeff",word2 = "ggffeeddccbaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "python",word2 = "programming") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "python",word2 = "programming") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaa",word2 = "bbbbbbbbb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaa",word2 = "bbbbbbbbb") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaaaaaa",word2 = "bbbbbbbbbb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaaaaaa",word2 = "bbbbbbbbbb") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzzxyzz",word2 = "mnopmnop") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzzxyzz",word2 = "mnopmnop") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "elephant") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "elephant") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "qqqq",word2 = "pppq") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "qqqq",word2 = "pppq") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcc",word2 = "xxxyyy") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcc",word2 = "xxxyyy") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcc",word2 = "bbccdd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcc",word2 = "bbccdd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "a",word2 = "b") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "a",word2 = "b") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbaa",word2 = "aabbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbaa",word2 = "aabbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabcabc",word2 = "defdefdefdef") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabcabc",word2 = "defdefdefdef") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcc",word2 = "abc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcc",word2 = "abc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbbcc",word2 = "dddeeefff") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbbcc",word2 = "dddeeefff") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacabadaba",word2 = "acaacaaca") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacabadaba",word2 = "acaacaaca") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcd",word2 = "abcdabcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcd",word2 = "abcdabcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghh",word2 = "iiiiijjjjjkkkkkk") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghh",word2 = "iiiiijjjjjkkkkkk") == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word1 = "abcde",word2 = "fghij") == True
    assert candidate(word1 = "xyz",word2 = "zyx") == True
    assert candidate(word1 = "aaa",word2 = "bbb") == True
    assert candidate(word1 = "ac",word2 = "b") == False
    assert candidate(word1 = "unique",word2 = "letters") == True
    assert candidate(word1 = "abcc",word2 = "aab") == True
    assert candidate(word1 = "aabb",word2 = "ccdd") == True
    assert candidate(word1 = "hello",word2 = "world") == True
    assert candidate(word1 = "ab",word2 = "cd") == True
    assert candidate(word1 = "xyz",word2 = "xyz") == True
    assert candidate(word1 = "abcd",word2 = "efgh") == True
    assert candidate(word1 = "aabbcc",word2 = "xyz") == False
    assert candidate(word1 = "abcd",word2 = "dcba") == True
    assert candidate(word1 = "same",word2 = "same") == True
    assert candidate(word1 = "aabbcc",word2 = "xxxyyzz") == True
    assert candidate(word1 = "aaaa",word2 = "bbbb") == True
    assert candidate(word1 = "qrstuvwxyz",word2 = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(word1 = "single",word2 = "letter") == True
    assert candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(word1 = "mississippi",word2 = "missouri") == True
    assert candidate(word1 = "mississippi",word2 = "penelope") == True
    assert candidate(word1 = "xyzz",word2 = "zzxx") == True
    assert candidate(word1 = "aaaaaaa",word2 = "bbbbbbb") == True
    assert candidate(word1 = "oneonetwo",word2 = "twotwoone") == True
    assert candidate(word1 = "uniquecharacters",word2 = "distinctcharacters") == True
    assert candidate(word1 = "aaaaabbbbbaaaa",word2 = "cccccbccccbcccc") == True
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "abcdefghijlkmnopqrstuvwxyz") == True
    assert candidate(word1 = "aabbccddeeff",word2 = "aabbccddeeff") == True
    assert candidate(word1 = "repeatedletters",word2 = "differentletters") == True
    assert candidate(word1 = "unique",word2 = "distinct") == True
    assert candidate(word1 = "aaaaabbbbbccccc",word2 = "dddddeeeeeffffff") == True
    assert candidate(word1 = "onetwothreefour",word2 = "five") == False
    assert candidate(word1 = "almost",word2 = "almost") == True
    assert candidate(word1 = "aaaabbbb",word2 = "cccddd") == True
    assert candidate(word1 = "abacabadabacaba",word2 = "bacbabacbacbacb") == False
    assert candidate(word1 = "aaaaabbbb",word2 = "ccccc") == False
    assert candidate(word1 = "abcd",word2 = "efghijklmnopqrstuvwxyz") == False
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvttrrssppoonnmmllkkjjiihhggffeeddccbbaa") == False
    assert candidate(word1 = "abcdefghijklmnopqrstuvwxy",word2 = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(word1 = "samechars",word2 = "samechars") == True
    assert candidate(word1 = "abcdefghij",word2 = "jihgfedcba") == True
    assert candidate(word1 = "abcdefg",word2 = "hijklmnopqrstuv") == False
    assert candidate(word1 = "longerstringwithrepeatedcharacters",word2 = "short") == False
    assert candidate(word1 = "xyz",word2 = "zyxwvut") == False
    assert candidate(word1 = "abcdefgh",word2 = "hgfedcba") == True
    assert candidate(word1 = "abcdef",word2 = "ghijklmnopqrstuvwxyz") == False
    assert candidate(word1 = "abcdefg",word2 = "hijklmnop") == False
    assert candidate(word1 = "abacabadabacaba",word2 = "bcadcbadcbadcbc") == True
    assert candidate(word1 = "xyxzyzxzyx",word2 = "zyxzyzxzyz") == True
    assert candidate(word1 = "abcdabcdabcd",word2 = "dcbaabcdabcd") == True
    assert candidate(word1 = "xyzz",word2 = "xxxyyyzzzz") == True
    assert candidate(word1 = "abracadabra",word2 = "alakazam") == True
    assert candidate(word1 = "aabbccddeeffgghhiijj",word2 = "zzzzzyyyxxwwvvuuttssrrqqppoonnmmllijkkihgfedcba") == False
    assert candidate(word1 = "abacabadabacaba",word2 = "zzzzzzzzzzzzzzzzz") == False
    assert candidate(word1 = "abcabcabcabc",word2 = "abcabcabcabc") == True
    assert candidate(word1 = "aaaaaa",word2 = "bbbbbb") == True
    assert candidate(word1 = "almost",word2 = "equal") == True
    assert candidate(word1 = "abcabcabc",word2 = "defdefdef") == True
    assert candidate(word1 = "ababababab",word2 = "bababababa") == True
    assert candidate(word1 = "almostthesame",word2 = "almostthesamee") == True
    assert candidate(word1 = "abcdefghij",word2 = "mnopqrstuv") == True
    assert candidate(word1 = "zzzzzzzzzzzz",word2 = "aaaaaaaaaaab") == True
    assert candidate(word1 = "almostthesame",word2 = "almostthesame") == True
    assert candidate(word1 = "xyzz",word2 = "xyz") == True
    assert candidate(word1 = "thisisaverylongwordwithrepeatedcharacters",word2 = "anotherlongwordwithdifferentcharacters") == True
    assert candidate(word1 = "unique",word2 = "words") == True
    assert candidate(word1 = "unique",word2 = "characters") == False
    assert candidate(word1 = "aabbcc",word2 = "aabbcd") == True
    assert candidate(word1 = "abcdef",word2 = "ghijkl") == True
    assert candidate(word1 = "thisisaverylongword",word2 = "whichhasmanycharacters") == False
    assert candidate(word1 = "mnopqr",word2 = "rstuvw") == True
    assert candidate(word1 = "aaaaaaaabbbbbbb",word2 = "ccccccccddddd") == True
    assert candidate(word1 = "mississippi",word2 = "louisiana") == False
    assert candidate(word1 = "aabbcceeddee",word2 = "fghhiijjkk") == True
    assert candidate(word1 = "abcdefghijklmnop",word2 = "qrstuvwxyz") == False
    assert candidate(word1 = "aaaaabbbbcccc",word2 = "bbbbccccdddd") == True
    assert candidate(word1 = "aaaaaaaa",word2 = "bbbbbbbb") == True
    assert candidate(word1 = "aaaaaabbbbbcccccdddddeeeee",word2 = "eeeeeaaaaabbbbbcccccddddd") == True
    assert candidate(word1 = "mississippi",word2 = "pennsylvania") == False
    assert candidate(word1 = "xyzz",word2 = "zzxy") == True
    assert candidate(word1 = "aabbccdd",word2 = "efgghhii") == True
    assert candidate(word1 = "aaaaabbbbbcccccdddddeeeee",word2 = "fffffggggghhhhhiiiii") == False
    assert candidate(word1 = "abcdefgh",word2 = "ijklmnop") == True
    assert candidate(word1 = "repeatrepeat",word2 = "repeatrepeat") == True
    assert candidate(word1 = "aabbcc",word2 = "ddeeff") == True
    assert candidate(word1 = "abcdefghijk",word2 = "klmnopqrstu") == True
    assert candidate(word1 = "aabbc",word2 = "ccdde") == True
    assert candidate(word1 = "complex",word2 = "inputs") == True
    assert candidate(word1 = "abcdabcdabcd",word2 = "dcbaabcdabdc") == True
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzzyyxxwwvvuuttoosssrrqqppoonnmlkkjjiihhggffeeddccbbaa") == True
    assert candidate(word1 = "one",word2 = "twothreefour") == False
    assert candidate(word1 = "xyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(word1 = "xyzz",word2 = "yzxx") == True
    assert candidate(word1 = "singlechar",word2 = "different") == False
    assert candidate(word1 = "aabbcc",word2 = "ddeeffgghhiijj") == False
    assert candidate(word1 = "abcdefg",word2 = "abcdefg") == True
    assert candidate(word1 = "characters",word2 = "words") == False
    assert candidate(word1 = "mississippi",word2 = "banana") == True
    assert candidate(word1 = "hellohello",word2 = "worldworld") == True
    assert candidate(word1 = "aabbccddeeff",word2 = "ggffeeddccbaaa") == True
    assert candidate(word1 = "python",word2 = "programming") == False
    assert candidate(word1 = "aaaaaa",word2 = "bbbbbbbbb") == True
    assert candidate(word1 = "aaaaaaaaaa",word2 = "bbbbbbbbbb") == True
    assert candidate(word1 = "xyzzxyzz",word2 = "mnopmnop") == False
    assert candidate(word1 = "mississippi",word2 = "elephant") == False
    assert candidate(word1 = "qqqq",word2 = "pppq") == True
    assert candidate(word1 = "aabbcc",word2 = "xxxyyy") == False
    assert candidate(word1 = "aabbcc",word2 = "bbccdd") == True
    assert candidate(word1 = "zzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzz") == True
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True
    assert candidate(word1 = "a",word2 = "b") == True
    assert candidate(word1 = "aabbaa",word2 = "aabbaa") == True
    assert candidate(word1 = "abcabcabcabc",word2 = "defdefdefdef") == True
    assert candidate(word1 = "aabbcc",word2 = "abc") == True
    assert candidate(word1 = "aabbbcc",word2 = "dddeeefff") == True
    assert candidate(word1 = "abacabadaba",word2 = "acaacaaca") == True
    assert candidate(word1 = "abcdabcd",word2 = "abcdabcd") == True
    assert candidate(word1 = "aabbccddeeffgghh",word2 = "iiiiijjjjjkkkkkk") == False


