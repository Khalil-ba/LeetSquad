def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word1 = "cccddabba",word2 = "babababab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "cccddabba",word2 = "babababab") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaa",word2 = "bbb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaa",word2 = "bbb") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcc",word2 = "ccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcc",word2 = "ccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "abcdefghijklmnopqrstuvwxyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "abcdefghijklmnopqrstuvwxyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "pqrstu",word2 = "utsrpq") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "pqrstu",word2 = "utsrpq") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mnop",word2 = "ponm") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mnop",word2 = "ponm") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabc",word2 = "bcbcbcbcb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabc",word2 = "bcbcbcbcb") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaa",word2 = "bccb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaa",word2 = "bccb") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyz",word2 = "zyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyz",word2 = "zyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdeef",word2 = "abaaacc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdeef",word2 = "abaaacc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abc",word2 = "abc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abc",word2 = "abc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "hello",word2 = "world") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "hello",word2 = "world") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggeeffddccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggeeffddccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabc",word2 = "abcabcabc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabc",word2 = "abcabcabc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzz",word2 = "zzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzz",word2 = "zzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcc",word2 = "bbccdd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcc",word2 = "bbccdd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abc",word2 = "xyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abc",word2 = "xyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzz",word2 = "zzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzz",word2 = "zzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcc",word2 = "abcabc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcc",word2 = "abcabc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdef",word2 = "fedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdef",word2 = "fedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcc",word2 = "abc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcc",word2 = "abc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "dcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "dcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abc",word2 = "def") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abc",word2 = "def") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefg",word2 = "gfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefg",word2 = "gfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "almostequivalent",word2 = "equivalentalmost") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "almostequivalent",word2 = "equivalentalmost") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacabadabacabad",word2 = "babaabacabacabac") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacabadabacabad",word2 = "babaabacabacabac") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijl",word2 = "abcdefghijllll") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijl",word2 = "abcdefghijllll") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbaabbaabb",word2 = "bbaabbaabbab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbaabbaabb",word2 = "bbaabbaabbab") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "hello world",word2 = "world hello") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "hello world",word2 = "world hello") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "frequency",word2 = "requeency") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "frequency",word2 = "requeency") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaabbbbccccddddeeeffffggghhhiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz",word2 = "zzzyyyxxxwwvvvuuuutttsssrqqqpppoonnmmlllkkkjjjiiihhhgggfffffeeedddccccbbbbaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaabbbbccccddddeeeffffggghhhiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz",word2 = "zzzyyyxxxwwvvvuuuutttsssrqqqpppoonnmmlllkkkjjjiiihhhgggfffffeeedddccccbbbbaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzxyzxyzxyzxyz",word2 = "zyxzyxzyxzyxzyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzxyzxyzxyzxyz",word2 = "zyxzyxzyxzyxzyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvttrrppoonnmmllkkjjiihhggeeddbbccaabb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvttrrppoonnmmllkkjjiihhggeeddbbccaabb") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "ssipimisip") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "ssipimisip") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzza") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzza") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzzzyyyxxxwwvvuuttrrssqqpponnmlkkjjiihhggffeeddccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzzzyyyxxxwwvvuuttrrssqqpponnmlkkjjiihhggffeeddccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzxyzxyzxyzxyzxyz",word2 = "xyzxyzxyzxyzxyzxyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzxyzxyzxyzxyzxyz",word2 = "xyzxyzxyzxyzxyzxyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xylophone",word2 = "polyxhnon") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xylophone",word2 = "polyxhnon") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "almost",word2 = "almosttttt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "almost",word2 = "almosttttt") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaabbbb",word2 = "bbbbaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaabbbb",word2 = "bbbbaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "almostequivalent",word2 = "almostequivalen") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "almostequivalent",word2 = "almostequivalen") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "testtesttest",word2 = "setttestsett") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "testtesttest",word2 = "setttestsett") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghij",word2 = "jihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghij",word2 = "jihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaabbbbcccc",word2 = "bbbbbccccddddd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaabbbbcccc",word2 = "bbbbbccccddddd") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaabbbccc",word2 = "bbcccaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaabbbccc",word2 = "bbcccaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abababababababababababababababababababab",word2 = "babababababababababababababababababababaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abababababababababababababababababababab",word2 = "babababababababababababababababababababaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnoooo",word2 = "bbbbaaaaccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooo") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnoooo",word2 = "bbbbaaaaccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooo") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwvwuvttsrqpqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwvwuvttsrqpqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "banana",word2 = "nanaba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "banana",word2 = "nanaba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "python",word2 = "pythooon") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "python",word2 = "pythooon") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacabadabacabad",word2 = "bacadabacadaba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacabadabacabad",word2 = "bacadabacadaba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "almostequivalent",word2 = "quivalentalmosta") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "almostequivalent",word2 = "quivalentalmosta") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "frequency",word2 = "frequncey") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "frequency",word2 = "frequncey") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",word2 = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",word2 = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "frequencycheck",word2 = "checkfrequency") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "frequencycheck",word2 = "checkfrequency") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbbcccddddeee",word2 = "eeeeddddccccbbbbaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbbcccddddeee",word2 = "eeeeddddccccbbbbaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abracadabra",word2 = "alakazam") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abracadabra",word2 = "alakazam") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbbccc",word2 = "bbaaccdd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbbccc",word2 = "bbaaccdd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijlll",word2 = "abcdefghijllll") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijlll",word2 = "abcdefghijllll") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijabcdefghij",word2 = "abcdefghijabcdefghii") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijabcdefghij",word2 = "abcdefghijabcdefghii") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "ppppqqqqrrrrssss",word2 = "ttttuuuuvvvv") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "ppppqqqqrrrrssss",word2 = "ttttuuuuvvvv") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abababababababab",word2 = "babababababababa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abababababababab",word2 = "babababababababa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaaaabbbbbbbbbbcccccccccc",word2 = "ccccccccccbbbbbbbbbbaaaaaaaabbbb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaaaabbbbbbbbbbcccccccccc",word2 = "ccccccccccbbbbbbbbbbaaaaaaaabbbb") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaabbbccc",word2 = "bbbaacccd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaabbbccc",word2 = "bbbaacccd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabcabc",word2 = "bcbcbcbcbcbc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabcabc",word2 = "bcbcbcbcbcbc") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "pississim") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "pississim") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvttrrssqqppoonnmmllkkjjiihhggffeeddccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvttrrssqqppoonnmmllkkjjiihhggffeeddccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaabbbbccccdddd",word2 = "bbbbbccccddddaaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaabbbbccccdddd",word2 = "bbbbbccccddddaaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xylophone",word2 = "polynomial") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xylophone",word2 = "polynomial") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaabbbbcccc",word2 = "cccbbbbaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaabbbbcccc",word2 = "cccbbbbaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "asdfghjkl",word2 = "lkjhgfdsa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "asdfghjkl",word2 = "lkjhgfdsa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "hello",word2 = "yellow") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "hello",word2 = "yellow") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "almostequivalent",word2 = "quivalentalmost") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "almostequivalent",word2 = "quivalentalmost") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghij",word2 = "abcdefghijk") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghij",word2 = "abcdefghijk") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacabadabacaba",word2 = "acabacabacababa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacabadabacaba",word2 = "acabacabacababa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefgabcdefgabcdefgabcdefg",word2 = "gfedcbagfedcbagfedcbagfedcb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefgabcdefgabcdefgabcdefg",word2 = "gfedcbagfedcbagfedcbagfedcb") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvttrrqqppoonnmmllkkjjiihhggeeffeeddccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvttrrqqppoonnmmllkkjjiihhggeeffeeddccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "hellothere",word2 = "heellooerr") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "hellothere",word2 = "heellooerr") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdeffghijklmnopqrstuvwxyz",word2 = "mnopqrstuvwxyzabcdefghijkl") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdeffghijklmnopqrstuvwxyz",word2 = "mnopqrstuvwxyzabcdefghijkl") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabc",word2 = "bcabcbac") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabc",word2 = "bcabcbac") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "abcdefghijklmnopqrstuvwxyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "abcdefghijklmnopqrstuvwxyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "equaldiffffe",word2 = "equaldifffff") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "equaldiffffe",word2 = "equaldifffff") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "racecar",word2 = "carrace") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "racecar",word2 = "carrace") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "bississippi") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "bississippi") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacabadabacabad",word2 = "abcabcabcabc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacabadabacabad",word2 = "abcabcabcabc") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkk",word2 = "ffffgggghhhhiiiijjjjkkkkaaaabbbbccccddddeeee") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkk",word2 = "ffffgggghhhhiiiijjjjkkkkaaaabbbbccccddddeeee") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefg",word2 = "ghfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefg",word2 = "ghfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "pythonprogramming",word2 = "programmingpython") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "pythonprogramming",word2 = "programmingpython") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdabcdabcdabcdabcd",word2 = "abcdabcdabcdabcdabcdabc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdabcdabcdabcdabcd",word2 = "abcdabcdabcdabcdabcdabc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijk",word2 = "abcdefghijl") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijk",word2 = "abcdefghijl") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaaaaaaa",word2 = "bbbbbbbbbbb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaaaaaaa",word2 = "bbbbbbbbbbb") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "ababababababababababababababababababababab",word2 = "bababababababababababababababababababababa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "ababababababababababababababababababababab",word2 = "bababababababababababababababababababababa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbbcccddd",word2 = "aaabbbcc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbbcccddd",word2 = "aaabbbcc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "ssissippi") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "ssissippi") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "programming",word2 = "mmprogain") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "programming",word2 = "mmprogain") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaabbbccc",word2 = "bbbaaacc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaabbbccc",word2 = "bbbaaacc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaabbbbcccccddddd",word2 = "aaabbbcccdddd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaabbbbcccccddddd",word2 = "aaabbbcccdddd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "banana",word2 = "ananaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "banana",word2 = "ananaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacabadabacaba",word2 = "cbacabacabacabc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacabadabacaba",word2 = "cbacabacabacabc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabcabc",word2 = "bcdbcdabcdabcd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabcabc",word2 = "bcdbcdabcdabcd") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaaaabbbbbbbccccccdddddeeeeeffffff",word2 = "ffffffeeeeeee/ddddddccccbbbbbbaaaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaaaabbbbbbbccccccdddddeeeeeffffff",word2 = "ffffffeeeeeee/ddddddccccbbbbbbaaaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdabcdabcd",word2 = "bcdbcdbcdbcdbcdb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdabcdabcd",word2 = "bcdbcdbcdbcdbcdb") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdabcdabcd",word2 = "dcbaabcdabcdabcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdabcdabcd",word2 = "dcbaabcdabcdabcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghij",word2 = "abcdefghix") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghij",word2 = "abcdefghix") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttsrqpponnml lkjihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttsrqpponnml lkjihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghi",word2 = "ihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghi",word2 = "ihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijklmnopqrstuvwxyza",word2 = "bcdefghijklmnopqrstuvwxyzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijklmnopqrstuvwxyza",word2 = "bcdefghijklmnopqrstuvwxyzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "frequency",word2 = "frequnecy") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "frequency",word2 = "frequnecy") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaabbbcccddd",word2 = "aaaabbbbccccdddd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaabbbcccddd",word2 = "aaaabbbbccccdddd") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcde",word2 = "fghij") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcde",word2 = "fghij") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabcabcabc",word2 = "bcbcbcbcbcbcb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabcabcabc",word2 = "bcbcbcbcbcbcb") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdabcdabcd",word2 = "abcdeabcdeabcdeabcde") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdabcdabcd",word2 = "abcdeabcdeabcdeabcde") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijklmnopqrstuvwxyzz",word2 = "abcdefghijklmnopqrstuvwxyyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijklmnopqrstuvwxyzz",word2 = "abcdefghijklmnopqrstuvwxyyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbbcccdddee",word2 = "eeedddcccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbbcccdddee",word2 = "eeedddcccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "uvwxyz",word2 = "vwxyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "uvwxyz",word2 = "vwxyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaabbbbccccc",word2 = "bbbaaaaaccccc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaabbbbccccc",word2 = "bbbaaaaaccccc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzzzyyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzzzyyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "pythonprogramming",word2 = "rogrammingpython") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "pythonprogramming",word2 = "rogrammingpython") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacabadabacaba",word2 = "abacabadabacaba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacabadabacaba",word2 = "abacabadabacaba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaabbbbbbccccccdddddeeeeee",word2 = "eeeeeeaaaaaabbbbbbccccccddddde") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaabbbbbbccccccdddddeeeeee",word2 = "eeeeeeaaaaaabbbbbbccccccddddde") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabcabcabc",word2 = "cccbbbbaaaabcabc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabcabcabc",word2 = "cccbbbbaaaabcabc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttrrssqqppoonnmlkkjjiihhggffeeddccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttrrssqqppoonnmlkkjjiihhggffeeddccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacabadabacaba",word2 = "abcabcabcabcabc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacabadabacaba",word2 = "abcabcabcabcabc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "qwerasdfzxcv",word2 = "asdfzxcvqwer") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "qwerasdfzxcv",word2 = "asdfzxcvqwer") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mnopqr",word2 = "mnopqz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mnopqr",word2 = "mnopqz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mnopqr",word2 = "rqponm") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mnopqr",word2 = "rqponm") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefg",word2 = "ghijklm") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefg",word2 = "ghijklm") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijllll",word2 = "abcdefghijlll") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijllll",word2 = "abcdefghijlll") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaaaaabbbbbbbbbbccccccccccdddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz",word2 = "zzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqpppppppppooooooooollllllllllkkkkkkkkkkjjjjjjjjjiiiiiiiiiijjjjjjjjjjhhhhhhhhhhhggggggggggffffffffeeeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbbbaaaaaaaaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaaaaabbbbbbbbbbccccccccccdddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz",word2 = "zzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqpppppppppooooooooollllllllllkkkkkkkkkkjjjjjjjjjiiiiiiiiiijjjjjjjjjjhhhhhhhhhhhggggggggggffffffffeeeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbbbaaaaaaaaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdabcd",word2 = "dcbaefghefgh") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdabcd",word2 = "dcbaefghefgh") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "missiisssipp") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "missiisssipp") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaabbbbccccdddd",word2 = "bbbaaaacccddde") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaabbbbccccdddd",word2 = "bbbaaaacccddde") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "qwert",word2 = "qwerty") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "qwert",word2 = "qwerty") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaabbbbcccc",word2 = "ddddeeeeffff") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaabbbbcccc",word2 = "ddddeeeeffff") == False: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "programming",word2 = "grammipnorg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "programming",word2 = "grammipnorg") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaabbbbccccdddd",word2 = "ddddccccbbbbaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaabbbbccccdddd",word2 = "ddddccccbbbbaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabccddeeff",word2 = "abccddeeffggh") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabccddeeff",word2 = "abccddeeffggh") == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word1 = "cccddabba",word2 = "babababab") == True
    assert candidate(word1 = "aaa",word2 = "bbb") == True
    assert candidate(word1 = "aabbcc",word2 = "ccbbaa") == True
    assert candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(word1 = "pqrstu",word2 = "utsrpq") == True
    assert candidate(word1 = "mnop",word2 = "ponm") == True
    assert candidate(word1 = "abcabcabc",word2 = "bcbcbcbcb") == True
    assert candidate(word1 = "aaaa",word2 = "bccb") == False
    assert candidate(word1 = "xyz",word2 = "zyx") == True
    assert candidate(word1 = "abcdeef",word2 = "abaaacc") == True
    assert candidate(word1 = "abc",word2 = "abc") == True
    assert candidate(word1 = "hello",word2 = "world") == True
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggeeffddccbbaa") == True
    assert candidate(word1 = "abcabcabc",word2 = "abcabcabc") == True
    assert candidate(word1 = "zzzz",word2 = "zzzz") == True
    assert candidate(word1 = "aabbcc",word2 = "bbccdd") == True
    assert candidate(word1 = "abc",word2 = "xyz") == True
    assert candidate(word1 = "zzz",word2 = "zzz") == True
    assert candidate(word1 = "aabbcc",word2 = "abcabc") == True
    assert candidate(word1 = "abcdef",word2 = "fedcba") == True
    assert candidate(word1 = "aabbcc",word2 = "abc") == True
    assert candidate(word1 = "abcd",word2 = "dcba") == True
    assert candidate(word1 = "abc",word2 = "def") == True
    assert candidate(word1 = "abcdefg",word2 = "gfedcba") == True
    assert candidate(word1 = "almostequivalent",word2 = "equivalentalmost") == True
    assert candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(word1 = "abacabadabacabad",word2 = "babaabacabacabac") == True
    assert candidate(word1 = "abcdefghijl",word2 = "abcdefghijllll") == True
    assert candidate(word1 = "aabbaabbaabb",word2 = "bbaabbaabbab") == True
    assert candidate(word1 = "hello world",word2 = "world hello") == True
    assert candidate(word1 = "frequency",word2 = "requeency") == True
    assert candidate(word1 = "aaaabbbbccccddddeeeffffggghhhiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz",word2 = "zzzyyyxxxwwvvvuuuutttsssrqqqpppoonnmmlllkkkjjjiiihhhgggfffffeeedddccccbbbbaaaa") == True
    assert candidate(word1 = "xyzxyzxyzxyzxyz",word2 = "zyxzyxzyxzyxzyx") == True
    assert candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvttrrppoonnmmllkkjjiihhggeeddbbccaabb") == True
    assert candidate(word1 = "mississippi",word2 = "ssipimisip") == True
    assert candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzza") == True
    assert candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz") == False
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzzzyyyxxxwwvvuuttrrssqqpponnmlkkjjiihhggffeeddccbbaa") == True
    assert candidate(word1 = "xyzxyzxyzxyzxyzxyz",word2 = "xyzxyzxyzxyzxyzxyx") == True
    assert candidate(word1 = "xylophone",word2 = "polyxhnon") == True
    assert candidate(word1 = "almost",word2 = "almosttttt") == False
    assert candidate(word1 = "aaaabbbb",word2 = "bbbbaaaa") == True
    assert candidate(word1 = "almostequivalent",word2 = "almostequivalen") == True
    assert candidate(word1 = "testtesttest",word2 = "setttestsett") == True
    assert candidate(word1 = "abcdefghij",word2 = "jihgfedcba") == True
    assert candidate(word1 = "aaaaabbbbcccc",word2 = "bbbbbccccddddd") == False
    assert candidate(word1 = "aaabbbccc",word2 = "bbcccaaa") == True
    assert candidate(word1 = "abababababababababababababababababababab",word2 = "babababababababababababababababababababaa") == True
    assert candidate(word1 = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnoooo",word2 = "bbbbaaaaccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooo") == True
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwvwuvttsrqpqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(word1 = "banana",word2 = "nanaba") == True
    assert candidate(word1 = "python",word2 = "pythooon") == True
    assert candidate(word1 = "abacabadabacabad",word2 = "bacadabacadaba") == True
    assert candidate(word1 = "almostequivalent",word2 = "quivalentalmosta") == True
    assert candidate(word1 = "frequency",word2 = "frequncey") == True
    assert candidate(word1 = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",word2 = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqz") == True
    assert candidate(word1 = "frequencycheck",word2 = "checkfrequency") == True
    assert candidate(word1 = "aabbbcccddddeee",word2 = "eeeeddddccccbbbbaaa") == True
    assert candidate(word1 = "abracadabra",word2 = "alakazam") == True
    assert candidate(word1 = "aabbbccc",word2 = "bbaaccdd") == True
    assert candidate(word1 = "abcdefghijlll",word2 = "abcdefghijllll") == True
    assert candidate(word1 = "abcdefghijabcdefghij",word2 = "abcdefghijabcdefghii") == True
    assert candidate(word1 = "ppppqqqqrrrrssss",word2 = "ttttuuuuvvvv") == False
    assert candidate(word1 = "abababababababab",word2 = "babababababababa") == True
    assert candidate(word1 = "aaaaaaaabbbbbbbbbbcccccccccc",word2 = "ccccccccccbbbbbbbbbbaaaaaaaabbbb") == False
    assert candidate(word1 = "aaabbbccc",word2 = "bbbaacccd") == True
    assert candidate(word1 = "abcabcabcabc",word2 = "bcbcbcbcbcbc") == False
    assert candidate(word1 = "mississippi",word2 = "pississim") == True
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvttrrssqqppoonnmmllkkjjiihhggffeeddccbbaa") == True
    assert candidate(word1 = "aaaaabbbbccccdddd",word2 = "bbbbbccccddddaaaaa") == True
    assert candidate(word1 = "xylophone",word2 = "polynomial") == True
    assert candidate(word1 = "aaaabbbbcccc",word2 = "cccbbbbaaa") == True
    assert candidate(word1 = "asdfghjkl",word2 = "lkjhgfdsa") == True
    assert candidate(word1 = "hello",word2 = "yellow") == True
    assert candidate(word1 = "almostequivalent",word2 = "quivalentalmost") == True
    assert candidate(word1 = "abcdefghij",word2 = "abcdefghijk") == True
    assert candidate(word1 = "abacabadabacaba",word2 = "acabacabacababa") == True
    assert candidate(word1 = "abcdefgabcdefgabcdefgabcdefg",word2 = "gfedcbagfedcbagfedcbagfedcb") == True
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvttrrqqppoonnmmllkkjjiihhggeeffeeddccbbaa") == True
    assert candidate(word1 = "hellothere",word2 = "heellooerr") == True
    assert candidate(word1 = "abcdeffghijklmnopqrstuvwxyz",word2 = "mnopqrstuvwxyzabcdefghijkl") == True
    assert candidate(word1 = "abcabcabc",word2 = "bcabcbac") == True
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True
    assert candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True
    assert candidate(word1 = "equaldiffffe",word2 = "equaldifffff") == True
    assert candidate(word1 = "racecar",word2 = "carrace") == True
    assert candidate(word1 = "mississippi",word2 = "bississippi") == True
    assert candidate(word1 = "abacabadabacabad",word2 = "abcabcabcabc") == False
    assert candidate(word1 = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkk",word2 = "ffffgggghhhhiiiijjjjkkkkaaaabbbbccccddddeeee") == True
    assert candidate(word1 = "abcdefg",word2 = "ghfedcba") == True
    assert candidate(word1 = "pythonprogramming",word2 = "programmingpython") == True
    assert candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True
    assert candidate(word1 = "abcdabcdabcdabcdabcdabcd",word2 = "abcdabcdabcdabcdabcdabc") == True
    assert candidate(word1 = "abcdefghijk",word2 = "abcdefghijl") == True
    assert candidate(word1 = "aaaaaaaaaaa",word2 = "bbbbbbbbbbb") == False
    assert candidate(word1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True
    assert candidate(word1 = "ababababababababababababababababababababab",word2 = "bababababababababababababababababababababa") == True
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True
    assert candidate(word1 = "aabbbcccddd",word2 = "aaabbbcc") == True
    assert candidate(word1 = "mississippi",word2 = "ssissippi") == True
    assert candidate(word1 = "programming",word2 = "mmprogain") == True
    assert candidate(word1 = "aaabbbccc",word2 = "bbbaaacc") == True
    assert candidate(word1 = "aaaaabbbbcccccddddd",word2 = "aaabbbcccdddd") == True
    assert candidate(word1 = "banana",word2 = "ananaa") == True
    assert candidate(word1 = "abacabadabacaba",word2 = "cbacabacabacabc") == True
    assert candidate(word1 = "abcabcabcabc",word2 = "bcdbcdabcdabcd") == False
    assert candidate(word1 = "aaaaaaaabbbbbbbccccccdddddeeeeeffffff",word2 = "ffffffeeeeeee/ddddddccccbbbbbbaaaaaa") == True
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True
    assert candidate(word1 = "abcdabcdabcdabcd",word2 = "bcdbcdbcdbcdbcdb") == False
    assert candidate(word1 = "abcdabcdabcdabcd",word2 = "dcbaabcdabcdabcd") == True
    assert candidate(word1 = "abcdefghij",word2 = "abcdefghix") == True
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttsrqpponnml lkjihgfedcba") == True
    assert candidate(word1 = "abcdefghi",word2 = "ihgfedcba") == True
    assert candidate(word1 = "abcdefghijklmnopqrstuvwxyza",word2 = "bcdefghijklmnopqrstuvwxyzzz") == True
    assert candidate(word1 = "frequency",word2 = "frequnecy") == True
    assert candidate(word1 = "aaabbbcccddd",word2 = "aaaabbbbccccdddd") == True
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True
    assert candidate(word1 = "abcde",word2 = "fghij") == True
    assert candidate(word1 = "abcabcabcabcabc",word2 = "bcbcbcbcbcbcb") == False
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == False
    assert candidate(word1 = "abcdabcdabcdabcd",word2 = "abcdeabcdeabcdeabcde") == False
    assert candidate(word1 = "abcdefghijklmnopqrstuvwxyzz",word2 = "abcdefghijklmnopqrstuvwxyyz") == True
    assert candidate(word1 = "aabbbcccdddee",word2 = "eeedddcccbbaa") == True
    assert candidate(word1 = "uvwxyz",word2 = "vwxyz") == True
    assert candidate(word1 = "aaaaabbbbccccc",word2 = "bbbaaaaaccccc") == True
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzzzyyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True
    assert candidate(word1 = "pythonprogramming",word2 = "rogrammingpython") == True
    assert candidate(word1 = "abacabadabacaba",word2 = "abacabadabacaba") == True
    assert candidate(word1 = "aaaaaabbbbbbccccccdddddeeeeee",word2 = "eeeeeeaaaaaabbbbbbccccccddddde") == True
    assert candidate(word1 = "abcabcabcabcabc",word2 = "cccbbbbaaaabcabc") == True
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzyyxxwwvvuuttrrssqqppoonnmlkkjjiihhggffeeddccbbaa") == True
    assert candidate(word1 = "abacabadabacaba",word2 = "abcabcabcabcabc") == True
    assert candidate(word1 = "qwerasdfzxcv",word2 = "asdfzxcvqwer") == True
    assert candidate(word1 = "mnopqr",word2 = "mnopqz") == True
    assert candidate(word1 = "mnopqr",word2 = "rqponm") == True
    assert candidate(word1 = "abcdefg",word2 = "ghijklm") == True
    assert candidate(word1 = "abcdefghijllll",word2 = "abcdefghijlll") == True
    assert candidate(word1 = "aaaaaaaaabbbbbbbbbbccccccccccdddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz",word2 = "zzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqpppppppppooooooooollllllllllkkkkkkkkkkjjjjjjjjjiiiiiiiiiijjjjjjjjjjhhhhhhhhhhhggggggggggffffffffeeeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbbbaaaaaaaaaa") == False
    assert candidate(word1 = "abcdabcdabcd",word2 = "dcbaefghefgh") == True
    assert candidate(word1 = "mississippi",word2 = "missiisssipp") == True
    assert candidate(word1 = "aaaabbbbccccdddd",word2 = "bbbaaaacccddde") == True
    assert candidate(word1 = "qwert",word2 = "qwerty") == True
    assert candidate(word1 = "aaaabbbbcccc",word2 = "ddddeeeeffff") == False
    assert candidate(word1 = "programming",word2 = "grammipnorg") == True
    assert candidate(word1 = "aaaabbbbccccdddd",word2 = "ddddccccbbbbaaaa") == True
    assert candidate(word1 = "aabccddeeff",word2 = "abccddeeffggh") == True


