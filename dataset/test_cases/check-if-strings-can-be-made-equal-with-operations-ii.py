def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "bbaacc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "bbaacc") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcd",s2 = "dcbadcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcd",s2 = "dcbadcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdba",s2 = "cabdab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdba",s2 = "cabdab") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a",s2 = "a") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a",s2 = "a") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "olelh") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "olelh") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "acbbca") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "acbbca") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "cdab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "cdab") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "fedcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "fedcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyz",s2 = "zyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyz",s2 = "zyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ab",s2 = "ba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ab",s2 = "ba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abe",s2 = "bea") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abe",s2 = "bea") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "dcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "dcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeff",s2 = "ffeeddccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeff",s2 = "ffeeddccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",s2 = "ssimmppiiss") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",s2 = "ssimmppiiss") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzyyxwwvvuuttrrssqqppoonnmmllkkjjiihhggffeeeeddccbbaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzyyxwwvvuuttrrssqqppoonnmmllkkjjiihhggffeeeeddccbbaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "palindrome",s2 = "paldinrome") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "palindrome",s2 = "paldinrome") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "racecar",s2 = "acecarr") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "racecar",s2 = "acecarr") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaabbbccc",s2 = "bbbaaacc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaabbbccc",s2 = "bbbaaacc") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "oddindexedswap",s2 = "doidndexswpoa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "oddindexedswap",s2 = "doidndexswpoa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijabcdefghijabcdefghij",s2 = "abcdefghijabcdefghijabcdefghjk") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijabcdefghijabcdefghij",s2 = "abcdefghijabcdefghijabcdefghjk") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "level",s2 = "level") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "level",s2 = "level") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "deified",s2 = "deified") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "deified",s2 = "deified") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "evenlydistributedstring",s2 = "elvnyeedisutrdstrign") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "evenlydistributedstring",s2 = "elvnyeedisutrdstrign") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "ccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "ccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "pqrstuv",s2 = "upqrsvt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "pqrstuv",s2 = "upqrsvt") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "rotor",s2 = "rotar") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "rotor",s2 = "rotar") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "gfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "gfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "racecar",s2 = "carrace") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "racecar",s2 = "carrace") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abababab",s2 = "babababa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abababab",s2 = "babababa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zxcvbnm",s2 = "mnbvcxz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zxcvbnm",s2 = "mnbvcxz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzyyxwwvvuuttssrrqppoonnllkkjjiihhggeeffdccbbbaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzyyxwwvvuuttssrrqppoonnllkkjjiihhggeeffdccbbbaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "gfehdcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "gfehdcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijabcdefghijabcdefghij",s2 = "bacdfegihjbacdfegihjbacdfegihj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijabcdefghijabcdefghij",s2 = "bacdfegihjbacdfegihjbacdfegihj") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaabbbbccccddddeeeeffffgggghhhh",s2 = "hhhhggggffffeeeeddddbbbbccccaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaabbbbccccddddeeeeffffgggghhhh",s2 = "hhhhggggffffeeeeddddbbbbccccaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hellohello",s2 = "ehlolhloel") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hellohello",s2 = "ehlolhloel") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadabacaba",s2 = "abaabacabadabaaba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadabacaba",s2 = "abaabacabadabaaba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcdabcdabcd",s2 = "bacdbacdbacdbacd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcdabcdabcd",s2 = "bacdbacdbacdbacd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "banana",s2 = "ananab") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "banana",s2 = "ananab") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabcabcabcabcabcabcabcabc",s2 = "bababababababababababababababababa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabcabcabcabcabcabcabcabc",s2 = "bababababababababababababababababa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzzzzzzz",s2 = "zzzzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzzzzzzz",s2 = "zzzzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadabacabad",s2 = "babaacabadabacab") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadabacabad",s2 = "babaacabadabacab") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcdabcdabcd",s2 = "ddddccccbbbbaaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcdabcdabcd",s2 = "ddddccccbbbbaaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeff",s2 = "abbaccddffee") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeff",s2 = "abbaccddffee") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzxyzxyzxyz",s2 = "zyxzyxzyxzyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzxyzxyzxyz",s2 = "zyxzyxzyxzyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyzz",s2 = "zzabcdefghijklmnopqrstuvwxy") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyzz",s2 = "zzabcdefghijklmnopqrstuvwxy") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "thisisaverylongstring",s2 = "tihisrasevylnsgtrnogi") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "thisisaverylongstring",s2 = "tihisrasevylnsgtrnogi") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",s2 = "ppissimissi") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",s2 = "ppissimissi") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaaabbbbbb",s2 = "bbbbbaaaaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaaabbbbbb",s2 = "bbbbbaaaaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadabacaba",s2 = "aabacabadabacab") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadabacaba",s2 = "aabacabadabacab") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijkmnopqrstuvwxyz",s2 = "bacdfeghijkmnopqrstvwxyz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijkmnopqrstuvwxyz",s2 = "bacdfeghijkmnopqrstvwxyz") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadabacabad",s2 = "babaacabdacaba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadabacabad",s2 = "babaacabdacaba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "fdecba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "fdecba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijk",s2 = "jihgfedcbaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijk",s2 = "jihgfedcbaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",s2 = "imississipp") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",s2 = "imississipp") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "qwertqwert",s2 = "wqerqewtqw") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "qwertqwert",s2 = "wqerqewtqw") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",s2 = "ssissimippi") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",s2 = "ssissimippi") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "almostsame",s2 = "lmostsae") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "almostsame",s2 = "lmostsae") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgabcdefg",s2 = "gfedcbagfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgabcdefg",s2 = "gfedcbagfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwx",s2 = "bacdfeghijklmnopqrstuvxw") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwx",s2 = "bacdfeghijklmnopqrstuvxw") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijkll",s2 = "llijkgfhecdba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijkll",s2 = "llijkgfhecdba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabc",s2 = "bcabcbaca") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabc",s2 = "bcabcbaca") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zaybzcyd",s2 = "dzbyazcy") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zaybzcyd",s2 = "dzbyazcy") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghef",s2 = "gdefhabcef") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghef",s2 = "gdefhabcef") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "bbccaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "bbccaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabc",s2 = "cbacbacba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabc",s2 = "cbacbacba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "bbbbccccddddeeeeffffgggghhhhiiijjjkkkllmmnnooppqqrrssttuuvvwwxxyyzz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "bbbbccccddddeeeeffffgggghhhhiiijjjkkkllmmnnooppqqrrssttuuvvwwxxyyzz") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnop",s2 = "ponmlkjihgfedcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnop",s2 = "ponmlkjihgfedcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "programming",s2 = "pgmrnomggin") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "programming",s2 = "pgmrnomggin") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "repaper",s2 = "repaper") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "repaper",s2 = "repaper") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgihjklmnopqrstuvwxyz",s2 = "bacdfegihjklmnopqrstuvwxzy") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgihjklmnopqrstuvwxyz",s2 = "bacdfegihjklmnopqrstuvwxzy") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdeffedcba",s2 = "fedcbaffedcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdeffedcba",s2 = "fedcbaffedcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba",s2 = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba",s2 = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeeeddccbbbaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeeeddccbbbaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "sameorder",s2 = "sameorder") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "sameorder",s2 = "sameorder") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "bbaaccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "bbaaccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcd",s2 = "dcbaabcd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcd",s2 = "dcbaabcd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "jihgfedcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "jihgfedcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "pqrstuvw",s2 = "wvutsrqp") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "pqrstuvw",s2 = "wvutsrqp") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zyxwvutsrqponmlkjihgfedcba",s2 = "yxwvuztsrqponmlkjihgfedcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zyxwvutsrqponmlkjihgfedcba",s2 = "yxwvuztsrqponmlkjihgfedcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "aecgbdfhij") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "aecgbdfhij") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "acdbegfh",s2 = "bfegacdh") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "acdbegfh",s2 = "bfegacdh") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abadecafagbahbbhacdg",s2 = "bdacegafabchbahbadcg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abadecafagbahbbhacdg",s2 = "bdacegafabchbahbadcg") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "abcdefghij") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "abcdefghij") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbaabb",s2 = "bbaabbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbaabb",s2 = "bbaabbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzzyxzyxzyx",s2 = "zyxzyxzyxzyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzzyxzyxzyx",s2 = "zyxzyxzyxzyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzzyyyxxxwwvvuuttssrrqqppoonnllkkjjiihhggeeffddeebbcaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzzyyyxxxwwvvuuttssrrqqppoonnllkkjjiihhggeeffddeebbcaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabcabc",s2 = "cbacbacbacba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabcabc",s2 = "cbacbacbacba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "racecar",s2 = "racecar") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "racecar",s2 = "racecar") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadabacabad",s2 = "badcbadcbadcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadabacabad",s2 = "badcbadcbadcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadabacaba",s2 = "abacabaabacabada") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadabacaba",s2 = "abacabaabacabada") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeff",s2 = "fbeeccddbaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeff",s2 = "fbeeccddbaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "noon",s2 = "noon") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "noon",s2 = "noon") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaabbbcccddd",s2 = "dddcccbbbaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaabbbcccddd",s2 = "dddcccbbbaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zxyxzyzyx",s2 = "yxzyxzyxq") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zxyxzyzyx",s2 = "yxzyxzyxq") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",s2 = "ppimississi") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",s2 = "ppimississi") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "gbihfedcja") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "gbihfedcja") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijj",s2 = "jjiihhggffeeeddccbaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijj",s2 = "jjiihhggffeeeddccbaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzzzzzzzzzzzzzzzzzzzzzzz",s2 = "zzzzzzzzzzzzzzzzzzzzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzzzzzzzzzzzzzzzzzzzzzzz",s2 = "zzzzzzzzzzzzzzzzzzzzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbaabbaabb",s2 = "bbaabbaabbba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbaabbaabb",s2 = "bbaabbaabbba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "afedcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "afedcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabad",s2 = "dcadcbab") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabad",s2 = "dcadcbab") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccdd",s2 = "ddccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccdd",s2 = "ddccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ababababababababababababab",s2 = "bababababababababababababa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ababababababababababababab",s2 = "bababababababababababababa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "noonnoon",s2 = "nnoonnou") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "noonnoon",s2 = "nnoonnou") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ababab",s2 = "bababa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ababab",s2 = "bababa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "abbaccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "abbaccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgihjklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgihjklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "jeihgfedcb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "jeihgfedcb") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijk",s2 = "jihgfedcbak") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijk",s2 = "jihgfedcbak") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "qwertypoiuytrewq",s2 = "qwertyuiytrewpoi") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "qwertypoiuytrewq",s2 = "qwertyuiytrewpoi") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "rotor",s2 = "rotor") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "rotor",s2 = "rotor") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "pneumonoultramicroscopicsilicovolcanoconiosis",s2 = "pneumonoultramicroscopicsilicovolcanoconiosis") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "pneumonoultramicroscopicsilicovolcanoconiosis",s2 = "pneumonoultramicroscopicsilicovolcanoconiosis") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "noonoon",s2 = "nooouon") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "noonoon",s2 = "nooouon") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "detartrated",s2 = "detartrated") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "detartrated",s2 = "detartrated") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcdabcd",s2 = "dcbaabcdabcd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcdabcd",s2 = "dcbaabcdabcd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbaabbaabbaabb",s2 = "bbaabbaabbaabbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbaabbaabbaabb",s2 = "bbaabbaabbaabbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mnopqrstuvwxyzabcdefghijkl",s2 = "onmpqrstuvwxyzabcdefghijkl") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mnopqrstuvwxyzabcdefghijkl",s2 = "onmpqrstuvwxyzabcdefghijkl") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcd",s2 = "cdabcdab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcd",s2 = "cdabcdab") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzyyxxwwvvuuttrrqqppoonnllkkjjiihhggeeffddeeaabbcc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzyyxxwwvvuuttrrqqppoonnllkkjjiihhggeeffddeeaabbcc") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxzyzyx",s2 = "yxzyxzyz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxzyzyx",s2 = "yxzyxzyz") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "pqrstuvwx",s2 = "vutsrqpwx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "pqrstuvwx",s2 = "vutsrqpwx") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadabacabaa",s2 = "abaabacabadabaab") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadabacabaa",s2 = "abaabacabadabaab") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zabcdefghijklmnopqrstuvwxy") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zabcdefghijklmnopqrstuvwxy") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeff",s2 = "bbccddeeffaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeff",s2 = "bbccddeeffaa") == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s1 = "aabbcc",s2 = "bbaacc") == True
    assert candidate(s1 = "abcdabcd",s2 = "dcbadcba") == False
    assert candidate(s1 = "abcdba",s2 = "cabdab") == True
    assert candidate(s1 = "a",s2 = "a") == True
    assert candidate(s1 = "hello",s2 = "olelh") == False
    assert candidate(s1 = "aabbcc",s2 = "acbbca") == True
    assert candidate(s1 = "abcd",s2 = "cdab") == True
    assert candidate(s1 = "abcdef",s2 = "fedcba") == False
    assert candidate(s1 = "xyz",s2 = "zyx") == True
    assert candidate(s1 = "ab",s2 = "ba") == False
    assert candidate(s1 = "abe",s2 = "bea") == False
    assert candidate(s1 = "abcd",s2 = "dcba") == False
    assert candidate(s1 = "aabbccddeeff",s2 = "ffeeddccbbaa") == True
    assert candidate(s1 = "mississippi",s2 = "ssimmppiiss") == False
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzyyxwwvvuuttrrssqqppoonnmmllkkjjiihhggffeeeeddccbbaa") == False
    assert candidate(s1 = "palindrome",s2 = "paldinrome") == False
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(s1 = "racecar",s2 = "acecarr") == False
    assert candidate(s1 = "aaabbbccc",s2 = "bbbaaacc") == False
    assert candidate(s1 = "oddindexedswap",s2 = "doidndexswpoa") == False
    assert candidate(s1 = "abcdefghijabcdefghijabcdefghij",s2 = "abcdefghijabcdefghijabcdefghjk") == False
    assert candidate(s1 = "level",s2 = "level") == True
    assert candidate(s1 = "deified",s2 = "deified") == True
    assert candidate(s1 = "evenlydistributedstring",s2 = "elvnyeedisutrdstrign") == False
    assert candidate(s1 = "aabbcc",s2 = "ccbbaa") == True
    assert candidate(s1 = "pqrstuv",s2 = "upqrsvt") == False
    assert candidate(s1 = "rotor",s2 = "rotar") == False
    assert candidate(s1 = "abcdefg",s2 = "gfedcba") == True
    assert candidate(s1 = "racecar",s2 = "carrace") == False
    assert candidate(s1 = "abababab",s2 = "babababa") == False
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True
    assert candidate(s1 = "zxcvbnm",s2 = "mnbvcxz") == True
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzyyxwwvvuuttssrrqppoonnllkkjjiihhggeeffdccbbbaa") == False
    assert candidate(s1 = "abcdefgh",s2 = "gfehdcba") == False
    assert candidate(s1 = "abcdefghijabcdefghijabcdefghij",s2 = "bacdfegihjbacdfegihjbacdfegihj") == False
    assert candidate(s1 = "aaaabbbbccccddddeeeeffffgggghhhh",s2 = "hhhhggggffffeeeeddddbbbbccccaaaa") == True
    assert candidate(s1 = "hellohello",s2 = "ehlolhloel") == False
    assert candidate(s1 = "abacabadabacaba",s2 = "abaabacabadabaaba") == False
    assert candidate(s1 = "abcdabcdabcdabcd",s2 = "bacdbacdbacdbacd") == False
    assert candidate(s1 = "banana",s2 = "ananab") == False
    assert candidate(s1 = "abcabcabcabcabcabcabcabcabcabc",s2 = "bababababababababababababababababa") == False
    assert candidate(s1 = "zzzzzzzzzz",s2 = "zzzzzzzzzz") == True
    assert candidate(s1 = "abacabadabacabad",s2 = "babaacabadabacab") == False
    assert candidate(s1 = "abcdabcdabcdabcd",s2 = "ddddccccbbbbaaaa") == False
    assert candidate(s1 = "aabbccddeeff",s2 = "abbaccddffee") == True
    assert candidate(s1 = "xyzxyzxyzxyz",s2 = "zyxzyxzyxzyx") == True
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyzz",s2 = "zzabcdefghijklmnopqrstuvwxy") == True
    assert candidate(s1 = "thisisaverylongstring",s2 = "tihisrasevylnsgtrnogi") == False
    assert candidate(s1 = "mississippi",s2 = "ppissimissi") == True
    assert candidate(s1 = "aaaaaabbbbbb",s2 = "bbbbbaaaaaa") == False
    assert candidate(s1 = "abacabadabacaba",s2 = "aabacabadabacab") == False
    assert candidate(s1 = "abcdefghijkmnopqrstuvwxyz",s2 = "bacdfeghijkmnopqrstvwxyz") == False
    assert candidate(s1 = "abacabadabacabad",s2 = "babaacabdacaba") == False
    assert candidate(s1 = "abcdef",s2 = "fdecba") == False
    assert candidate(s1 = "abcdefghijk",s2 = "jihgfedcbaa") == False
    assert candidate(s1 = "mississippi",s2 = "imississipp") == False
    assert candidate(s1 = "qwertqwert",s2 = "wqerqewtqw") == False
    assert candidate(s1 = "mississippi",s2 = "ssissimippi") == True
    assert candidate(s1 = "almostsame",s2 = "lmostsae") == False
    assert candidate(s1 = "abcdefgabcdefg",s2 = "gfedcbagfedcba") == True
    assert candidate(s1 = "abcdefghijklmnopqrstuvwx",s2 = "bacdfeghijklmnopqrstuvxw") == False
    assert candidate(s1 = "abcdefghijkll",s2 = "llijkgfhecdba") == False
    assert candidate(s1 = "abcabcabc",s2 = "bcabcbaca") == False
    assert candidate(s1 = "zaybzcyd",s2 = "dzbyazcy") == False
    assert candidate(s1 = "abcdefghef",s2 = "gdefhabcef") == False
    assert candidate(s1 = "aabbcc",s2 = "bbccaa") == True
    assert candidate(s1 = "abcabcabc",s2 = "cbacbacba") == True
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "bbbbccccddddeeeeffffgggghhhhiiijjjkkkllmmnnooppqqrrssttuuvvwwxxyyzz") == False
    assert candidate(s1 = "abcdefghijklmnop",s2 = "ponmlkjihgfedcba") == False
    assert candidate(s1 = "programming",s2 = "pgmrnomggin") == False
    assert candidate(s1 = "repaper",s2 = "repaper") == True
    assert candidate(s1 = "abcdefgihjklmnopqrstuvwxyz",s2 = "bacdfegihjklmnopqrstuvwxzy") == False
    assert candidate(s1 = "abcdeffedcba",s2 = "fedcbaffedcba") == False
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba",s2 = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeeeddccbbbaa") == False
    assert candidate(s1 = "sameorder",s2 = "sameorder") == True
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "bbaaccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True
    assert candidate(s1 = "abcdabcd",s2 = "dcbaabcd") == False
    assert candidate(s1 = "abcdefghij",s2 = "jihgfedcba") == False
    assert candidate(s1 = "pqrstuvw",s2 = "wvutsrqp") == False
    assert candidate(s1 = "zyxwvutsrqponmlkjihgfedcba",s2 = "yxwvuztsrqponmlkjihgfedcba") == False
    assert candidate(s1 = "abcdefghij",s2 = "aecgbdfhij") == False
    assert candidate(s1 = "acdbegfh",s2 = "bfegacdh") == False
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == False
    assert candidate(s1 = "abadecafagbahbbhacdg",s2 = "bdacegafabchbahbadcg") == False
    assert candidate(s1 = "abcdefghij",s2 = "abcdefghij") == True
    assert candidate(s1 = "aabbaabb",s2 = "bbaabbaa") == True
    assert candidate(s1 = "xyzzyxzyxzyx",s2 = "zyxzyxzyxzyx") == True
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzzyyyxxxwwvvuuttssrrqqppoonnllkkjjiihhggeeffddeebbcaaa") == False
    assert candidate(s1 = "abcabcabcabc",s2 = "cbacbacbacba") == True
    assert candidate(s1 = "racecar",s2 = "racecar") == True
    assert candidate(s1 = "abacabadabacabad",s2 = "badcbadcbadcba") == False
    assert candidate(s1 = "abacabadabacaba",s2 = "abacabaabacabada") == False
    assert candidate(s1 = "aabbccddeeff",s2 = "fbeeccddbaaa") == False
    assert candidate(s1 = "noon",s2 = "noon") == True
    assert candidate(s1 = "aaabbbcccddd",s2 = "dddcccbbbaaa") == False
    assert candidate(s1 = "zxyxzyzyx",s2 = "yxzyxzyxq") == False
    assert candidate(s1 = "mississippi",s2 = "ppimississi") == False
    assert candidate(s1 = "abcdefghij",s2 = "gbihfedcja") == False
    assert candidate(s1 = "aabbccddeeffgghhiijj",s2 = "jjiihhggffeeeddccbaa") == False
    assert candidate(s1 = "zzzzzzzzzzzzzzzzzzzzzzzzzz",s2 = "zzzzzzzzzzzzzzzzzzzzzzzzzz") == True
    assert candidate(s1 = "aabbaabbaabb",s2 = "bbaabbaabbba") == False
    assert candidate(s1 = "abcdefg",s2 = "afedcba") == False
    assert candidate(s1 = "abacabad",s2 = "dcadcbab") == False
    assert candidate(s1 = "aabbccdd",s2 = "ddccbbaa") == True
    assert candidate(s1 = "ababababababababababababab",s2 = "bababababababababababababa") == False
    assert candidate(s1 = "noonnoon",s2 = "nnoonnou") == False
    assert candidate(s1 = "ababab",s2 = "bababa") == False
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "abbaccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == True
    assert candidate(s1 = "abcdefgihjklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(s1 = "abcdefghij",s2 = "jeihgfedcb") == False
    assert candidate(s1 = "abcdefghijk",s2 = "jihgfedcbak") == False
    assert candidate(s1 = "qwertypoiuytrewq",s2 = "qwertyuiytrewpoi") == False
    assert candidate(s1 = "rotor",s2 = "rotor") == True
    assert candidate(s1 = "pneumonoultramicroscopicsilicovolcanoconiosis",s2 = "pneumonoultramicroscopicsilicovolcanoconiosis") == True
    assert candidate(s1 = "noonoon",s2 = "nooouon") == False
    assert candidate(s1 = "detartrated",s2 = "detartrated") == True
    assert candidate(s1 = "abcdabcdabcd",s2 = "dcbaabcdabcd") == False
    assert candidate(s1 = "aabbaabbaabbaabb",s2 = "bbaabbaabbaabbaa") == True
    assert candidate(s1 = "mnopqrstuvwxyzabcdefghijkl",s2 = "onmpqrstuvwxyzabcdefghijkl") == True
    assert candidate(s1 = "abcdabcd",s2 = "cdabcdab") == True
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzyyxxwwvvuuttrrqqppoonnllkkjjiihhggeeffddeeaabbcc") == False
    assert candidate(s1 = "xyxzyzyx",s2 = "yxzyxzyz") == False
    assert candidate(s1 = "pqrstuvwx",s2 = "vutsrqpwx") == True
    assert candidate(s1 = "abacabadabacabaa",s2 = "abaabacabadabaab") == False
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zabcdefghijklmnopqrstuvwxy") == False
    assert candidate(s1 = "aabbccddeeff",s2 = "bbccddeeffaa") == True


