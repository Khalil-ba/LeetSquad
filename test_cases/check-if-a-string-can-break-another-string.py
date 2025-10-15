def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s1 = "same",s2 = "same") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "same",s2 = "same") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abc",s2 = "bca") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc",s2 = "bca") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "bello") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "bello") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aazz",s2 = "zzaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aazz",s2 = "zzaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abac",s2 = "baca") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abac",s2 = "baca") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyz",s2 = "wvu") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyz",s2 = "wvu") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abc",s2 = "xya") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc",s2 = "xya") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "abcabc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "abcabc") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "pqrs",s2 = "rstu") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "pqrs",s2 = "rstu") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zyx",s2 = "wvu") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zyx",s2 = "wvu") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "adcb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "adcb") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaa",s2 = "bbb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaa",s2 = "bbb") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "dcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "dcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abe",s2 = "acd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abe",s2 = "acd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "leetcodee",s2 = "interview") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "leetcodee",s2 = "interview") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "python",s2 = "typhon") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "python",s2 = "typhon") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdxyz",s2 = "zyxwvut") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdxyz",s2 = "zyxwvut") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzz",s2 = "zzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzz",s2 = "zzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyz",s2 = "zyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyz",s2 = "zyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzyyxxwwvvuuttrrssqqpponnmlkkjjiihhggeeffddaabbcc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzyyxxwwvvuuttrrssqqpponnmlkkjjiihhggeeffddaabbcc") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "algorithm",s2 = "logarithm") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "algorithm",s2 = "logarithm") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "longerstringwithvariouscharacters",s2 = "variouscharacterswithlongerstring") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "longerstringwithvariouscharacters",s2 = "variouscharacterswithlongerstring") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzzz",s2 = "aaaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzzz",s2 = "aaaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "unbreakable",s2 = "rebreakable") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "unbreakable",s2 = "rebreakable") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcdabcd",s2 = "ddddcccbbbbaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcdabcd",s2 = "ddddcccbbbbaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "ccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "ccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",s2 = "pippiimissi") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",s2 = "pippiimissi") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "almostsame",s2 = "almostsane") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "almostsame",s2 = "almostsane") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzzyyxwwvvuutssrrqqponnmmllkkjjiihhggeeffdccbaaab") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzzyyxwwvvuutssrrqqponnmmllkkjjiihhggeeffdccbaaab") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "racecar",s2 = "carrace") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "racecar",s2 = "carrace") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "thisisaverylongstringthatneedstobecomparesothattwostingsareofthesamelength",s2 = "somuchlongeranddifferentsomenecessarypaddingletterssotheyareofthesame") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "thisisaverylongstringthatneedstobecomparesothattwostingsareofthesamelength",s2 = "somuchlongeranddifferentsomenecessarypaddingletterssotheyareofthesame") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadabacaba",s2 = "zyzxzyzyzxzyzyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadabacaba",s2 = "zyzxzyzyzxzyzyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abracadabra",s2 = "cadabrabara") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abracadabra",s2 = "cadabrabara") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zyxwvutsrqponmlkjihgfedcba",s2 = "abcdefghijklmnopqrstuvwxyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zyxwvutsrqponmlkjihgfedcba",s2 = "abcdefghijklmnopqrstuvwxyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijk",s2 = "fghijklmno") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijk",s2 = "fghijklmno") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abracadabra",s2 = "alakazamazam") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abracadabra",s2 = "alakazamazam") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "randomstringhere",s2 = "somestringrandom") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "randomstringhere",s2 = "somestringrandom") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "uniquechars",s2 = "distinctset") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "uniquechars",s2 = "distinctset") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aazzzzzzzzzzzzzzzz",s2 = "zzzzzzzzzzzzzzaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aazzzzzzzzzzzzzzzz",s2 = "zzzzzzzzzzzzzzaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzzzzz",s2 = "zzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzzzzz",s2 = "zzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbbccc",s2 = "bbbcccaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbbccc",s2 = "bbbcccaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzzzzzzz",s2 = "zzzzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzzzzzzz",s2 = "zzzzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "complex",s2 = "lexicom") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "complex",s2 = "lexicom") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzyyxxwwvvuuttssrrqqppoonnmlkkjjiihhggffeeddccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzyyxxwwvvuuttssrrqqppoonnmlkkjjiihhggffeeddccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdxyzabcdxyz",s2 = "xyzabcdxyzabcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdxyzabcdxyz",s2 = "xyzabcdxyzabcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "hgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "hgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "pppppppppp",s2 = "qqqqqqqqqq") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "pppppppppp",s2 = "qqqqqqqqqq") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "fedcbaghij") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "fedcbaghij") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaabbbbcccccddeeefffffgggghhhiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxxxyyyyyzzzzz",s2 = "zzzzzyyyyyxxxwwwvvvuuutttsssrqqppoonnmlkkkjjjiiihgggfffffeeedddccccbbbaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaabbbbcccccddeeefffffgggghhhiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxxxyyyyyzzzzz",s2 = "zzzzzyyyyyxxxwwwvvvuuutttsssrqqppoonnmlkkkjjjiiihgggfffffeeedddccccbbbaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "programming",s2 = "gnimmargorp") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "programming",s2 = "gnimmargorp") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "permutation",s2 = "reupmttinao") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "permutation",s2 = "reupmttinao") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",s2 = "pppnnnnmsssssiiii") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",s2 = "pppnnnnmsssssiiii") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhii",s2 = "iihhggeeffddccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhii",s2 = "iihhggeeffddccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijk",s2 = "jihgfedcbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijk",s2 = "jihgfedcbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzzzz",s2 = "zzzzxy") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzzzz",s2 = "zzzzxy") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "medium",s2 = "median") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "medium",s2 = "median") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mnopqr",s2 = "qrstuv") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mnopqr",s2 = "qrstuv") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzyzyzyzyzyzyzyz",s2 = "zyxzyxzyxzyxzyxzy") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzyzyzyzyzyzyzyz",s2 = "zyxzyxzyxzyxzyxzy") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaabbbbccccdddd",s2 = "ddddccccbbbbaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaabbbbccccdddd",s2 = "ddddccccbbbbaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "thisisalongstring",s2 = "stringlongthisisalo") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "thisisalongstring",s2 = "stringlongthisisalo") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "abcdefghijklmnopqrstuvwxyzzzyxwvutsrqponmlkjihgfedcbaaabb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "abcdefghijklmnopqrstuvwxyzzzyxwvutsrqponmlkjihgfedcbaaabb") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "algorithm",s2 = "thmalogri") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "algorithm",s2 = "thmalogri") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzz",s2 = "yyzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzz",s2 = "yyzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzzyyxwwvvuttsrrqqponnmlkkjjiihhggffeeeeddccbbaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzzyyxwwvvuttsrrqqponnmlkkjjiihhggffeeeeddccbbaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "bbccaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "bbccaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaabbbbbcccccc",s2 = "bbbbbaaaaacccccb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaabbbbbcccccc",s2 = "bbbbbaaaaacccccb") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnop",s2 = "ponmlkjihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnop",s2 = "ponmlkjihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",s2 = "ppssiiimmm") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",s2 = "ppssiiimmm") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadabacaba",s2 = "zxyzyxzyxzyxzyxzyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadabacaba",s2 = "zxyzyxzyxzyxzyxzyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "ghijkl") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "ghijkl") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbbcccddddeeeeffffgggghhhhiiiiiijjjjjjkkkkkkllllllmmmmmmmnnnnnnnooooooooppppppppqqqqqqqqrrrrrrrrssssssssstttttttttuuuuuuuuuvvvvvvvvvwwwwwwwwwxxxxxxxxxyyyyyyyyyzzzzzzzzz",s2 = "zzzzzzzzzyyyyyyyyyxxxxxxxxxwwwwwwwwwvvvvvvvvvuuuuuuuuutttttttttssssssssrrrrrrrrqqqqqqqqppppppppooooooonnnnnnnmmmmmmmllllllkkkkkkjjjjjjiiiiiiggggffffeeeeeeeeeddddddccccbbbaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbbcccddddeeeeffffgggghhhhiiiiiijjjjjjkkkkkkllllllmmmmmmmnnnnnnnooooooooppppppppqqqqqqqqrrrrrrrrssssssssstttttttttuuuuuuuuuvvvvvvvvvwwwwwwwwwxxxxxxxxxyyyyyyyyyzzzzzzzzz",s2 = "zzzzzzzzzyyyyyyyyyxxxxxxxxxwwwwwwwwwvvvvvvvvvuuuuuuuuutttttttttssssssssrrrrrrrrqqqqqqqqppppppppooooooonnnnnnnmmmmmmmllllllkkkkkkjjjjjjiiiiiiggggffffeeeeeeeeeddddddccccbbbaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaabbbbcccc",s2 = "ccccbbbbaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaabbbbcccc",s2 = "ccccbbbbaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabcc",s2 = "bbdda") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabcc",s2 = "bbdda") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "congratulations",s2 = "stucgnioalort") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "congratulations",s2 = "stucgnioalort") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcdabcd",s2 = "dcbaabcddcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcdabcd",s2 = "dcbaabcddcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "permutation",s2 = "nutationspr") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "permutation",s2 = "nutationspr") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyzz",s2 = "zzzzzyzyxwvutsrqponmlkjihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyzz",s2 = "zzzzzyzyxwvutsrqponmlkjihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaaaab",s2 = "baaaaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaaaab",s2 = "baaaaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "equalstring",s2 = "equalstring") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "equalstring",s2 = "equalstring") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijk",s2 = "zyxwvutsrqz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijk",s2 = "zyxwvutsrqz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaaa",s2 = "bbbbbb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaaa",s2 = "bbbbbb") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcd",s2 = "dcbaabcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcd",s2 = "dcbaabcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "jihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "jihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcdabcdabcdabcd",s2 = "dcbaabdcbaabdcbaabdcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcdabcdabcdabcd",s2 = "dcbaabdcbaabdcbaabdcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "optimization",s2 = "nttimzpiaoos") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "optimization",s2 = "nttimzpiaoos") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "optimization",s2 = "izationoptim") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "optimization",s2 = "izationoptim") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "abcdefghij") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "abcdefghij") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "leetcodeleetcode",s2 = "interviewinterview") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "leetcodeleetcode",s2 = "interviewinterview") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "qwertypoiuytrewq",s2 = "mnbvcxzlkjhgfd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "qwertypoiuytrewq",s2 = "mnbvcxzlkjhgfd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadabacaba",s2 = "zyxzyxzyxzyxzyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadabacaba",s2 = "zyxzyxzyxzyxzyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",s2 = "pississippi") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",s2 = "pississippi") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaaaaaaabbbbbbbbbbcccccccccc",s2 = "ccccccccccbbbbbbbbbbaaaaaaaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaaaaaaabbbbbbbbbbcccccccccc",s2 = "ccccccccccbbbbbbbbbbaaaaaaaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "longerstringexample",s2 = "examplelongerstring") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "longerstringexample",s2 = "examplelongerstring") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabacabacabac",s2 = "zyxzyxzyxzyxzyxzyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabacabacabac",s2 = "zyxzyxzyxzyxzyxzyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabc",s2 = "xyzxyzxyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabc",s2 = "xyzxyzxyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "pqrstuvw",s2 = "qrstuvwp") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "pqrstuvw",s2 = "qrstuvwp") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "fedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "fedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "pqrsrpqrsrpqrsr",s2 = "zyxwzyxwzyxwzyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "pqrsrpqrsrpqrsr",s2 = "zyxwzyxwzyxwzyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcde",s2 = "edcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcde",s2 = "edcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklnmopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklnmopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijabcdefghijabcdefghij",s2 = "zyxwvutsrqzyxwvutsrqzyxwvutsrq") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijabcdefghijabcdefghij",s2 = "zyxwvutsrqzyxwvutsrqzyxwvutsrq") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "interview",s2 = "terviewin") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "interview",s2 = "terviewin") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mnopqr",s2 = "rstuvw") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mnopqr",s2 = "rstuvw") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadabacaba",s2 = "zzzzzzzzzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadabacaba",s2 = "zzzzzzzzzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "break",s2 = "maker") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "break",s2 = "maker") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "qrstuv",s2 = "vwxyza") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "qrstuv",s2 = "vwxyza") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "permutation",s2 = "interwoven") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "permutation",s2 = "interwoven") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdxyz",s2 = "zyxcbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdxyz",s2 = "zyxcbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzz",s2 = "aaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzz",s2 = "aaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbbccc",s2 = "cccbbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbbccc",s2 = "cccbbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "ghijklm") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "ghijklm") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "leetcode",s2 = "docodele") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "leetcode",s2 = "docodele") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzz",s2 = "wxyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzz",s2 = "wxyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",s2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",s2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzzzzzzzzzzzzzzz",s2 = "aaaaaaaaaaaaaaaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzzzzzzzzzzzzzzz",s2 = "aaaaaaaaaaaaaaaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "banana",s2 = "anabna") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "banana",s2 = "anabna") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",s2 = "ppissimiss") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",s2 = "ppissimiss") == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s1 = "same",s2 = "same") == True
    assert candidate(s1 = "abc",s2 = "bca") == True
    assert candidate(s1 = "hello",s2 = "bello") == True
    assert candidate(s1 = "aazz",s2 = "zzaa") == True
    assert candidate(s1 = "abac",s2 = "baca") == True
    assert candidate(s1 = "xyz",s2 = "wvu") == True
    assert candidate(s1 = "abc",s2 = "xya") == True
    assert candidate(s1 = "aabbcc",s2 = "abcabc") == True
    assert candidate(s1 = "pqrs",s2 = "rstu") == True
    assert candidate(s1 = "zyx",s2 = "wvu") == True
    assert candidate(s1 = "abcd",s2 = "adcb") == True
    assert candidate(s1 = "aaa",s2 = "bbb") == True
    assert candidate(s1 = "abcd",s2 = "dcba") == True
    assert candidate(s1 = "abe",s2 = "acd") == False
    assert candidate(s1 = "leetcodee",s2 = "interview") == True
    assert candidate(s1 = "python",s2 = "typhon") == True
    assert candidate(s1 = "abcdxyz",s2 = "zyxwvut") == True
    assert candidate(s1 = "zzzz",s2 = "zzzz") == True
    assert candidate(s1 = "xyz",s2 = "zyx") == True
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzyyxxwwvvuuttrrssqqpponnmlkkjjiihhggeeffddaabbcc") == True
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(s1 = "algorithm",s2 = "logarithm") == True
    assert candidate(s1 = "longerstringwithvariouscharacters",s2 = "variouscharacterswithlongerstring") == True
    assert candidate(s1 = "zzzzzz",s2 = "aaaaaa") == True
    assert candidate(s1 = "unbreakable",s2 = "rebreakable") == True
    assert candidate(s1 = "abcdabcdabcd",s2 = "ddddcccbbbbaaa") == True
    assert candidate(s1 = "aabbcc",s2 = "ccbbaa") == True
    assert candidate(s1 = "mississippi",s2 = "pippiimissi") == True
    assert candidate(s1 = "almostsame",s2 = "almostsane") == True
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzzyyxwwvvuutssrrqqponnmmllkkjjiihhggeeffdccbaaab") == False
    assert candidate(s1 = "racecar",s2 = "carrace") == True
    assert candidate(s1 = "thisisaverylongstringthatneedstobecomparesothattwostingsareofthesamelength",s2 = "somuchlongeranddifferentsomenecessarypaddingletterssotheyareofthesame") == False
    assert candidate(s1 = "abacabadabacaba",s2 = "zyzxzyzyzxzyzyz") == True
    assert candidate(s1 = "abracadabra",s2 = "cadabrabara") == True
    assert candidate(s1 = "zyxwvutsrqponmlkjihgfedcba",s2 = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(s1 = "abcdefghijk",s2 = "fghijklmno") == True
    assert candidate(s1 = "abracadabra",s2 = "alakazamazam") == False
    assert candidate(s1 = "randomstringhere",s2 = "somestringrandom") == True
    assert candidate(s1 = "uniquechars",s2 = "distinctset") == False
    assert candidate(s1 = "aazzzzzzzzzzzzzzzz",s2 = "zzzzzzzzzzzzzzaa") == True
    assert candidate(s1 = "zzzzzzzz",s2 = "zzzzzzzz") == True
    assert candidate(s1 = "aabbbccc",s2 = "bbbcccaaa") == True
    assert candidate(s1 = "zzzzzzzzzz",s2 = "zzzzzzzzzz") == True
    assert candidate(s1 = "complex",s2 = "lexicom") == True
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzyyxxwwvvuuttssrrqqppoonnmlkkjjiihhggffeeddccbbaa") == True
    assert candidate(s1 = "abcdxyzabcdxyz",s2 = "xyzabcdxyzabcd") == True
    assert candidate(s1 = "abcdefgh",s2 = "hgfedcba") == True
    assert candidate(s1 = "pppppppppp",s2 = "qqqqqqqqqq") == True
    assert candidate(s1 = "abcdefghij",s2 = "fedcbaghij") == True
    assert candidate(s1 = "aaaaabbbbcccccddeeefffffgggghhhiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxxxyyyyyzzzzz",s2 = "zzzzzyyyyyxxxwwwvvvuuutttsssrqqppoonnmlkkkjjjiiihgggfffffeeedddccccbbbaaaa") == True
    assert candidate(s1 = "programming",s2 = "gnimmargorp") == True
    assert candidate(s1 = "permutation",s2 = "reupmttinao") == True
    assert candidate(s1 = "mississippi",s2 = "pppnnnnmsssssiiii") == True
    assert candidate(s1 = "aabbccddeeffgghhii",s2 = "iihhggeeffddccbbaa") == True
    assert candidate(s1 = "abcdefghijk",s2 = "jihgfedcbaa") == True
    assert candidate(s1 = "xyzzzz",s2 = "zzzzxy") == True
    assert candidate(s1 = "medium",s2 = "median") == True
    assert candidate(s1 = "mnopqr",s2 = "qrstuv") == True
    assert candidate(s1 = "xyzyzyzyzyzyzyzyz",s2 = "zyxzyxzyxzyxzyxzy") == True
    assert candidate(s1 = "abcdefghijklnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(s1 = "aaaabbbbccccdddd",s2 = "ddddccccbbbbaaaa") == True
    assert candidate(s1 = "thisisalongstring",s2 = "stringlongthisisalo") == True
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "abcdefghijklmnopqrstuvwxyzzzyxwvutsrqponmlkjihgfedcbaaabb") == True
    assert candidate(s1 = "algorithm",s2 = "thmalogri") == True
    assert candidate(s1 = "xyzz",s2 = "yyzz") == True
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzzyyxwwvvuttsrrqqponnmlkkjjiihhggffeeeeddccbbaa") == False
    assert candidate(s1 = "aabbcc",s2 = "bbccaa") == True
    assert candidate(s1 = "aaaaabbbbbcccccc",s2 = "bbbbbaaaaacccccb") == True
    assert candidate(s1 = "abcdefghijklmnop",s2 = "ponmlkjihgfedcba") == True
    assert candidate(s1 = "mississippi",s2 = "ppssiiimmm") == False
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True
    assert candidate(s1 = "abacabadabacaba",s2 = "zxyzyxzyxzyxzyxzyx") == True
    assert candidate(s1 = "abcdef",s2 = "ghijkl") == True
    assert candidate(s1 = "aabbbcccddddeeeeffffgggghhhhiiiiiijjjjjjkkkkkkllllllmmmmmmmnnnnnnnooooooooppppppppqqqqqqqqrrrrrrrrssssssssstttttttttuuuuuuuuuvvvvvvvvvwwwwwwwwwxxxxxxxxxyyyyyyyyyzzzzzzzzz",s2 = "zzzzzzzzzyyyyyyyyyxxxxxxxxxwwwwwwwwwvvvvvvvvvuuuuuuuuutttttttttssssssssrrrrrrrrqqqqqqqqppppppppooooooonnnnnnnmmmmmmmllllllkkkkkkjjjjjjiiiiiiggggffffeeeeeeeeeddddddccccbbbaaa") == True
    assert candidate(s1 = "aaaabbbbcccc",s2 = "ccccbbbbaaaa") == True
    assert candidate(s1 = "aabcc",s2 = "bbdda") == True
    assert candidate(s1 = "congratulations",s2 = "stucgnioalort") == True
    assert candidate(s1 = "abcdabcdabcd",s2 = "dcbaabcddcba") == True
    assert candidate(s1 = "permutation",s2 = "nutationspr") == True
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyzz",s2 = "zzzzzyzyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(s1 = "aaaaaaab",s2 = "baaaaaaa") == True
    assert candidate(s1 = "equalstring",s2 = "equalstring") == True
    assert candidate(s1 = "abcdefghijk",s2 = "zyxwvutsrqz") == True
    assert candidate(s1 = "aaaaaa",s2 = "bbbbbb") == True
    assert candidate(s1 = "abcdabcd",s2 = "dcbaabcd") == True
    assert candidate(s1 = "abcdefghij",s2 = "jihgfedcba") == True
    assert candidate(s1 = "abcdabcdabcdabcdabcd",s2 = "dcbaabdcbaabdcbaabdcba") == True
    assert candidate(s1 = "optimization",s2 = "nttimzpiaoos") == True
    assert candidate(s1 = "optimization",s2 = "izationoptim") == True
    assert candidate(s1 = "abcdefghij",s2 = "abcdefghij") == True
    assert candidate(s1 = "leetcodeleetcode",s2 = "interviewinterview") == True
    assert candidate(s1 = "qwertypoiuytrewq",s2 = "mnbvcxzlkjhgfd") == False
    assert candidate(s1 = "abacabadabacaba",s2 = "zyxzyxzyxzyxzyx") == True
    assert candidate(s1 = "mississippi",s2 = "pississippi") == True
    assert candidate(s1 = "aaaaaaaaaabbbbbbbbbbcccccccccc",s2 = "ccccccccccbbbbbbbbbbaaaaaaaaaa") == True
    assert candidate(s1 = "longerstringexample",s2 = "examplelongerstring") == True
    assert candidate(s1 = "abacabacabacabac",s2 = "zyxzyxzyxzyxzyxzyx") == True
    assert candidate(s1 = "abcabcabc",s2 = "xyzxyzxyz") == True
    assert candidate(s1 = "pqrstuvw",s2 = "qrstuvwp") == True
    assert candidate(s1 = "abcdef",s2 = "fedcba") == True
    assert candidate(s1 = "pqrsrpqrsrpqrsr",s2 = "zyxwzyxwzyxwzyx") == True
    assert candidate(s1 = "abcde",s2 = "edcba") == True
    assert candidate(s1 = "abcdefghijklnmopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(s1 = "abcdefghijabcdefghijabcdefghij",s2 = "zyxwvutsrqzyxwvutsrqzyxwvutsrq") == True
    assert candidate(s1 = "interview",s2 = "terviewin") == True
    assert candidate(s1 = "mnopqr",s2 = "rstuvw") == True
    assert candidate(s1 = "abacabadabacaba",s2 = "zzzzzzzzzzzzzzz") == True
    assert candidate(s1 = "break",s2 = "maker") == True
    assert candidate(s1 = "qrstuv",s2 = "vwxyza") == False
    assert candidate(s1 = "permutation",s2 = "interwoven") == True
    assert candidate(s1 = "abcdxyz",s2 = "zyxcbaa") == True
    assert candidate(s1 = "zzzzz",s2 = "aaaaa") == True
    assert candidate(s1 = "aabbbccc",s2 = "cccbbbaa") == True
    assert candidate(s1 = "abcdefg",s2 = "ghijklm") == True
    assert candidate(s1 = "leetcode",s2 = "docodele") == True
    assert candidate(s1 = "xyzz",s2 = "wxyz") == True
    assert candidate(s1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",s2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True
    assert candidate(s1 = "zzzzzzzzzzzzzzzzzz",s2 = "aaaaaaaaaaaaaaaaaa") == True
    assert candidate(s1 = "banana",s2 = "anabna") == True
    assert candidate(s1 = "mississippi",s2 = "ppissimiss") == True


