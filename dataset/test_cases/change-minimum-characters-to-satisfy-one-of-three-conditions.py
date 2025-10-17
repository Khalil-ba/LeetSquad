def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(a = "abc",b = "bcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "bcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "aba",b = "caa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aba",b = "caa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyzz",b = "zzzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyzz",b = "zzzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "dcba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "dcba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaabbbb",b = "ccccdddd") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaabbbb",b = "ccccdddd") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyz",b = "abc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyz",b = "abc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "def") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "def") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefghijklmnopqrstuvwxyz",b = "abcdefghijklmnopqrstuvwxyz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefghijklmnopqrstuvwxyz",b = "abcdefghijklmnopqrstuvwxyz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(a = "zzz",b = "aaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "zzz",b = "aaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "abc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "abc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "a",b = "z") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "a",b = "z") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaa",b = "zzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaa",b = "zzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "abacabadabacaba",b = "zzzyzxzyzxzyzxz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abacabadabacaba",b = "zzzyzxzyzxzyzxz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbcc",b = "bbccdd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbcc",b = "bbccdd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyz",b = "xyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyz",b = "xyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefghijklmnopqrstuvwxyz",b = "zyxwvutsrqponmlkjihgfedcba") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefghijklmnopqrstuvwxyz",b = "zyxwvutsrqponmlkjihgfedcba") == 26: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyz",b = "zyx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyz",b = "zyx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaa",b = "bbb") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaa",b = "bbb") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "dabadd",b = "cda") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "dabadd",b = "cda") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "a",b = "b") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "a",b = "b") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaa",b = "bbbb") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaa",b = "bbbb") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaabbbbbccccc",b = "cccccbbaaaa") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaabbbbbccccc",b = "cccccbbaaaa") == 11: {e}')
    
    total += 1
    try:
        result = candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "aaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "aaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zyxwvutsrqponmlkjihgfedcba") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zyxwvutsrqponmlkjihgfedcba") == 27: {e}')
    
    total += 1
    try:
        result = candidate(a = "qwert",b = "asdfg") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "qwert",b = "asdfg") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "ababababababababababababababab",b = "bababababababababababababababa") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "ababababababababababababababab",b = "bababababababababababababababa") == 30: {e}')
    
    total += 1
    try:
        result = candidate(a = "algorithm",b = "datastructure") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "algorithm",b = "datastructure") == 7: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabcabcabcabcabcabcabcabcabc",b = "zzzzyyyxxxwwwwvvvvuuuuttttssssrrrrqqqqppppooooonnnnmmmmmlllllkkkkkjjjjjiiiii") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabcabcabcabcabcabcabcabcabc",b = "zzzzyyyxxxwwwwvvvvuuuuttttssssrrrrqqqqppppooooonnnnmmmmmlllllkkkkkjjjjjiiiii") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",b = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",b = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdabcdabcdabcdabcd",b = "dcbaabcdabcdabcdabcd") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdabcdabcdabcdabcd",b = "dcbaabcdabcdabcdabcd") == 20: {e}')
    
    total += 1
    try:
        result = candidate(a = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcb",b = "abadabadabadabadabadabadabadabadabadabadabadabadabadabadabadabadabadabadabadab") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcb",b = "abadabadabadabadabadabadabadabadabadabadabadabadabadabadabadabadabadabadabadab") == 39: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaabbbcccddd",b = "eefffgggg") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaabbbcccddd",b = "eefffgggg") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaaaaaaabbbbbbbbbbbccccccccc",b = "zzzzzzzzzzzyyyyyyyyyyxxxxxxxxxx") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaaaaaaabbbbbbbbbbbccccccccc",b = "zzzzzzzzzzzyyyyyyyyyyxxxxxxxxxx") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "abababababababababab",b = "babababababababababa") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abababababababababab",b = "babababababababababa") == 20: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 25: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabb",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabb",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",b = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",b = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 52: {e}')
    
    total += 1
    try:
        result = candidate(a = "mnopmnopmnopmnopmnop",b = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "mnopmnopmnopmnopmnop",b = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "abacabadabacabadabacaba",b = "zyxzyxzyxzyxzyxzyxzyxzyx") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abacabadabacabadabacaba",b = "zyxzyxzyxzyxzyxzyxzyxzyx") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaa",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaa",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaaabbbbccccdddd",b = "eeeeefffffggggghhhhh") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaaabbbbccccdddd",b = "eeeeefffffggggghhhhh") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefg",b = "hijklmnopqrstuvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefg",b = "hijklmnopqrstuvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj",b = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj",b = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "mississippi",b = "bababababa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "mississippi",b = "bababababa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",b = "pppppppppppppppppppppppppppppppppppppppppp") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",b = "pppppppppppppppppppppppppppppppppppppppppp") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "mnop",b = "qrst") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "mnop",b = "qrst") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "qazwsxedcrfvtgbyhnujmikolp",b = "ploikmjhunbygvtfredcxswqaz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "qazwsxedcrfvtgbyhnujmikolp",b = "ploikmjhunbygvtfredcxswqaz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(a = "hello",b = "world") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "hello",b = "world") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "mno",b = "jkl") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "mno",b = "jkl") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "hellohellohello",b = "worldworldworld") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "hellohellohello",b = "worldworldworld") == 9: {e}')
    
    total += 1
    try:
        result = candidate(a = "mmmmmmmmmmmmmmmmmmmmmm",b = "nnnnnnnnnnnnnnnnnnnnnn") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "mmmmmmmmmmmmmmmmmmmmmm",b = "nnnnnnnnnnnnnnnnnnnnnn") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabaaaacaba",b = "bcdef") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabaaaacaba",b = "bcdef") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "zzzzzzzzzz",b = "aaaaaaaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "zzzzzzzzzz",b = "aaaaaaaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaaaaaaaaaaabbbbbbbbbbbbbbcccccccccccccccccdddddddddddddddd",b = "eeeeeeeeeeeeeeeeffffffffgggggggggggggggggghhhhhhhhhhhhhhhhhiiiiiiiiiiiiiiiiii") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaaaaaaaaaaabbbbbbbbbbbbbbcccccccccccccccccdddddddddddddddd",b = "eeeeeeeeeeeeeeeeffffffffgggggggggggggggggghhhhhhhhhhhhhhhhhiiiiiiiiiiiiiiiiii") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "qwertqwertqwert",b = "mnbvmnbvmnbv") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "qwertqwertqwert",b = "mnbvmnbvmnbv") == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaabbbbccccddddeeeeffffgggghhhhiiii",b = "jkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaabbbbccccddddeeeeffffgggghhhhiiii",b = "jkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "qwertyuiop",b = "poiuytrewq") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "qwertyuiop",b = "poiuytrewq") == 10: {e}')
    
    total += 1
    try:
        result = candidate(a = "mno",b = "mnpq") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "mno",b = "mnpq") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "llllllllllllllllllllllllllllllllllllllll",b = "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "llllllllllllllllllllllllllllllllllllllll",b = "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "programming",b = "contest") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "programming",b = "contest") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zzxxwwvvutssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zzxxwwvvutssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == 48: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyzzzzzxyzzzzz",b = "zzzzzxyzzzzzxy") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyzzzzzxyzzzzz",b = "zzzzzxyzzzzzxy") == 8: {e}')
    
    total += 1
    try:
        result = candidate(a = "zzzzz",b = "aaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "zzzzz",b = "aaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "zzzzzzzzzzzzzz",b = "aaaaaaaaaaaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "zzzzzzzzzzzzzz",b = "aaaaaaaaaaaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "ababababababababababababababababab",b = "bababababababababababababababababa") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "ababababababababababababababababab",b = "bababababababababababababababababa") == 34: {e}')
    
    total += 1
    try:
        result = candidate(a = "ppppqqqqqqrrrrrrsssssss",b = "tttttuuuuuuuuvvvvvvvvvvvvv") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "ppppqqqqqqrrrrrrsssssss",b = "tttttuuuuuuuuvvvvvvvvvvvvv") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "qwerttyuiiopasdfghjklzzxcvbnm",b = "mnbvcxzlkjhgfdsapoiuytrewq") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "qwerttyuiiopasdfghjklzzxcvbnm",b = "mnbvcxzlkjhgfdsapoiuytrewq") == 26: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "python",b = "java") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "python",b = "java") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "pqrstuv",b = "mnopq") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "pqrstuv",b = "mnopq") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefghijklmnopqrstuvwxyz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefghijklmnopqrstuvwxyz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = "acabcbacbacbacbaca",b = "bdadbdadbdadbdad") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "acabcbacbacbacbaca",b = "bdadbdadbdadbdad") == 8: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefghijklmnopqrstu",b = "vwxyzvwxyzvwxyzvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefghijklmnopqrstu",b = "vwxyzvwxyzvwxyzvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefghijklmnop",b = "zyxwvutsrqponmlkjihgfedcba") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefghijklmnop",b = "zyxwvutsrqponmlkjihgfedcba") == 16: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefghijklmnopqrstuvwxyz",b = "abcdefghijklmnopqrstuvwxy") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefghijklmnopqrstuvwxyz",b = "abcdefghijklmnopqrstuvwxy") == 25: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",b = "defdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdef") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",b = "defdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdef") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabcabcabcabcabcabcabcabcabc",b = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabcabcabcabcabcabcabcabcabc",b = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbaacc",b = "zzzzyyxx") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbaacc",b = "zzzzyyxx") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaabbbbcccc",b = "ccccbbbbaaaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaabbbbcccc",b = "ccccbbbbaaaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefg",b = "zzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefg",b = "zzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefghijklmnopqrstuvwxy",b = "zyxwvutsrqponmlkjihgfedcba") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefghijklmnopqrstuvwxy",b = "zyxwvutsrqponmlkjihgfedcba") == 25: {e}')
    
    total += 1
    try:
        result = candidate(a = "acacacacacacacacacacacacacacaca",b = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "acacacacacacacacacacacacacacaca",b = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc") == 15: {e}')
    
    total += 1
    try:
        result = candidate(a = "mnop",b = "qrstuvwxyza") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "mnop",b = "qrstuvwxyza") == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdabcdabcd",b = "xyzxyzxyzxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdabcdabcd",b = "xyzxyzxyzxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "abacabadabacaba",b = "zyxzyxzyxzyxzyxzyx") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abacabadabacaba",b = "zyxzyxzyxzyxzyxzyx") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "same",b = "same") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "same",b = "same") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "mnopqrstu",b = "vwxyzijkl") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "mnopqrstu",b = "vwxyzijkl") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "abcdefghijklmnopqrstuvwxyz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "abcdefghijklmnopqrstuvwxyz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = "mnopqrstuvwxy",b = "abcdefghijklmnopqrstuvwxyz") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "mnopqrstuvwxy",b = "abcdefghijklmnopqrstuvwxyz") == 14: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdabcabc",b = "zyxzxyzxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdabcabc",b = "zyxzxyzxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "abacabadabacabad",b = "zyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abacabadabacabad",b = "zyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabcabcabcabcabcabcabcabcabc",b = "abcabcabcabcabcabcabcabcabcabc") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabcabcabcabcabcabcabcabcabc",b = "abcabcabcabcabcabcabcabcabcabc") == 30: {e}')
    
    total += 1
    try:
        result = candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefghijklm",b = "nopqrstuvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefghijklm",b = "nopqrstuvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "mnopqrstuvwxyzmnopqrstu",b = "abcdefghijklmnopqrstuabcdefghijklmnopqrstu") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "mnopqrstuvwxyzmnopqrstu",b = "abcdefghijklmnopqrstuabcdefghijklmnopqrstu") == 18: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaabbbcccdddeeefffggghhhhiiiiijjjjjjkkkkkkkllllllllmmmmmmmmmmm",b = "mnopqrstuvwxyzmnopqrstuvwxyzmnopqrstuvwxyzmnopqrstuvwxyz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaabbbcccdddeeefffggghhhhiiiiijjjjjjkkkkkkkllllllllmmmmmmmmmmm",b = "mnopqrstuvwxyzmnopqrstuvwxyzmnopqrstuvwxyzmnopqrstuvwxyz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccdddddddddddddddddddddd",b = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccdddddddddddddddddddddd",b = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyxzyzxzyzxzyzxzyz",b = "zyxzyzxzyzxzyzxzyx") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyxzyzxzyzxzyzxzyz",b = "zyxzyzxzyzxzyzxzyx") == 18: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefghijklmnop",b = "qrstuvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefghijklmnop",b = "qrstuvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyzz",b = "abcd") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyzz",b = "abcd") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "racecar",b = "madam") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "racecar",b = "madam") == 5: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefghijklmnopqrstu",b = "vwxyzabcdefghijklmnopqrstu") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefghijklmnopqrstu",b = "vwxyzabcdefghijklmnopqrstu") == 21: {e}')
    
    total += 1
    try:
        result = candidate(a = "qwe",b = "qwer") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "qwe",b = "qwer") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "pppppppppppppppppppppppppppppppppppppppppp",b = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "pppppppppppppppppppppppppppppppppppppppppp",b = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "mnbvcxzlkjhgfdsapoiuytrewq",b = "qwertyuiopasdfghjklzxcvbnm") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "mnbvcxzlkjhgfdsapoiuytrewq",b = "qwertyuiopasdfghjklzxcvbnm") == 26: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdabcdabcd",b = "dcbaabcdabcd") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdabcdabcd",b = "dcbaabcdabcd") == 12: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaabbbbb",b = "bbbbbccccc") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaabbbbb",b = "bbbbbccccc") == 5: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaabbbcccdddeeefffggghhhiii",b = "kkklllmmmnnnooopppqqqrrrssstttuuuvvv") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaabbbcccdddeeefffggghhhiii",b = "kkklllmmmnnnooopppqqqrrrssstttuuuvvv") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaaaaaaaaaaaaaaaaaaaa",b = "bbbbbbbbbbbbbbbbbbbbbbbbb") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaaaaaaaaaaaaaaaaaaaa",b = "bbbbbbbbbbbbbbbbbbbbbbbbb") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "abacabadabacabadabacabad",b = "zzzzyyyyxxxxyyyyzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abacabadabacabadabacabad",b = "zzzzyyyyxxxxyyyyzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeeeddccbbbaa") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeeeddccbbbaa") == 52: {e}')
    
    total += 1
    try:
        result = candidate(a = "abacabadabacaba",b = "zzzyyyxxxwwwwvvvvuuuuuuttttttsssssrrrrrqqqqqqpppppoonnnnmmmllllkkkkjjjjiiiihhhhhgggggffffffeeeeeeeedddddccccbbbaaaa") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abacabadabacaba",b = "zzzyyyxxxwwwwvvvvuuuuuuttttttsssssrrrrrqqqqqqpppppoonnnnmmmllllkkkkjjjjiiiihhhhhgggggffffffeeeeeeeedddddccccbbbaaaa") == 10: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == 52: {e}')
    
    total += 1
    try:
        result = candidate(a = "mnopqrstuvwxyz",b = "abcdefghijklm") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "mnopqrstuvwxyz",b = "abcdefghijklm") == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = "one",b = "two") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "one",b = "two") == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = "qwertyuiopasdfghjklzxcvbnm",b = "qwertyuiopasdfghjklzxcvbnm") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "qwertyuiopasdfghjklzxcvbnm",b = "qwertyuiopasdfghjklzxcvbnm") == 26: {e}')
    
    total += 1
    try:
        result = candidate(a = "mississippi",b = "delaware") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "mississippi",b = "delaware") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefghijklmnopqrstuvwxyz",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefghijklmnopqrstuvwxyz",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "xyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "xyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "abcdefghijklmnopqrstuvwxyz") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "abcdefghijklmnopqrstuvwxyz") == 27: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",b = "mnopmnopmnopmnopmnopmnopmnopmnopmnopmnopmnopmnopmnop") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",b = "mnopmnopmnopmnopmnopmnopmnopmnopmnopmnopmnopmnopmnop") == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(a = "abc",b = "bcd") == 2
    assert candidate(a = "aba",b = "caa") == 2
    assert candidate(a = "xyzz",b = "zzzz") == 2
    assert candidate(a = "abcd",b = "dcba") == 4
    assert candidate(a = "aaaabbbb",b = "ccccdddd") == 0
    assert candidate(a = "xyz",b = "abc") == 0
    assert candidate(a = "abc",b = "def") == 0
    assert candidate(a = "abcdefghijklmnopqrstuvwxyz",b = "abcdefghijklmnopqrstuvwxyz") == 26
    assert candidate(a = "zzz",b = "aaa") == 0
    assert candidate(a = "abc",b = "abc") == 3
    assert candidate(a = "a",b = "z") == 0
    assert candidate(a = "aaa",b = "zzz") == 0
    assert candidate(a = "abacabadabacaba",b = "zzzyzxzyzxzyzxz") == 0
    assert candidate(a = "aabbcc",b = "bbccdd") == 4
    assert candidate(a = "xyz",b = "xyz") == 3
    assert candidate(a = "abcdefghijklmnopqrstuvwxyz",b = "zyxwvutsrqponmlkjihgfedcba") == 26
    assert candidate(a = "xyz",b = "zyx") == 3
    assert candidate(a = "aaa",b = "bbb") == 0
    assert candidate(a = "dabadd",b = "cda") == 3
    assert candidate(a = "a",b = "b") == 0
    assert candidate(a = "aaaa",b = "bbbb") == 0
    assert candidate(a = "aaaaabbbbbccccc",b = "cccccbbaaaa") == 11
    assert candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "aaaaa") == 0
    assert candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zyxwvutsrqponmlkjihgfedcba") == 27
    assert candidate(a = "qwert",b = "asdfg") == 2
    assert candidate(a = "ababababababababababababababab",b = "bababababababababababababababa") == 30
    assert candidate(a = "algorithm",b = "datastructure") == 7
    assert candidate(a = "abcabcabcabcabcabcabcabcabcabc",b = "zzzzyyyxxxwwwwvvvvuuuuttttssssrrrrqqqqppppooooonnnnmmmmmlllllkkkkkjjjjjiiiii") == 0
    assert candidate(a = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",b = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") == 0
    assert candidate(a = "abcdabcdabcdabcdabcd",b = "dcbaabcdabcdabcdabcd") == 20
    assert candidate(a = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcb",b = "abadabadabadabadabadabadabadabadabadabadabadabadabadabadabadabadabadabadabadab") == 39
    assert candidate(a = "aaabbbcccddd",b = "eefffgggg") == 0
    assert candidate(a = "aaaaaaaaaabbbbbbbbbbbccccccccc",b = "zzzzzzzzzzzyyyyyyyyyyxxxxxxxxxx") == 0
    assert candidate(a = "abababababababababab",b = "babababababababababa") == 20
    assert candidate(a = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 25
    assert candidate(a = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabb",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
    assert candidate(a = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",b = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 52
    assert candidate(a = "mnopmnopmnopmnopmnop",b = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 0
    assert candidate(a = "abacabadabacabadabacaba",b = "zyxzyxzyxzyxzyxzyxzyxzyx") == 0
    assert candidate(a = "aaaaa",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
    assert candidate(a = "aaaaaabbbbccccdddd",b = "eeeeefffffggggghhhhh") == 0
    assert candidate(a = "abcdefg",b = "hijklmnopqrstuvwxyz") == 0
    assert candidate(a = "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj",b = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") == 0
    assert candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 2
    assert candidate(a = "mississippi",b = "bababababa") == 0
    assert candidate(a = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",b = "pppppppppppppppppppppppppppppppppppppppppp") == 0
    assert candidate(a = "mnop",b = "qrst") == 0
    assert candidate(a = "qazwsxedcrfvtgbyhnujmikolp",b = "ploikmjhunbygvtfredcxswqaz") == 26
    assert candidate(a = "hello",b = "world") == 3
    assert candidate(a = "mno",b = "jkl") == 0
    assert candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
    assert candidate(a = "hellohellohello",b = "worldworldworld") == 9
    assert candidate(a = "mmmmmmmmmmmmmmmmmmmmmm",b = "nnnnnnnnnnnnnnnnnnnnnn") == 0
    assert candidate(a = "aabaaaacaba",b = "bcdef") == 2
    assert candidate(a = "zzzzzzzzzz",b = "aaaaaaaaaa") == 0
    assert candidate(a = "aaaaaaaaaaaaaabbbbbbbbbbbbbbcccccccccccccccccdddddddddddddddd",b = "eeeeeeeeeeeeeeeeffffffffgggggggggggggggggghhhhhhhhhhhhhhhhhiiiiiiiiiiiiiiiiii") == 0
    assert candidate(a = "qwertqwertqwert",b = "mnbvmnbvmnbv") == 6
    assert candidate(a = "aaaabbbbccccddddeeeeffffgggghhhhiiii",b = "jkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 0
    assert candidate(a = "qwertyuiop",b = "poiuytrewq") == 10
    assert candidate(a = "mno",b = "mnpq") == 2
    assert candidate(a = "llllllllllllllllllllllllllllllllllllllll",b = "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk") == 0
    assert candidate(a = "programming",b = "contest") == 4
    assert candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zzxxwwvvutssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == 48
    assert candidate(a = "xyzzzzzxyzzzzz",b = "zzzzzxyzzzzzxy") == 8
    assert candidate(a = "zzzzz",b = "aaaaa") == 0
    assert candidate(a = "zzzzzzzzzzzzzz",b = "aaaaaaaaaaaaaa") == 0
    assert candidate(a = "ababababababababababababababababab",b = "bababababababababababababababababa") == 34
    assert candidate(a = "ppppqqqqqqrrrrrrsssssss",b = "tttttuuuuuuuuvvvvvvvvvvvvv") == 0
    assert candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0
    assert candidate(a = "qwerttyuiiopasdfghjklzzxcvbnm",b = "mnbvcxzlkjhgfdsapoiuytrewq") == 26
    assert candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 2
    assert candidate(a = "python",b = "java") == 2
    assert candidate(a = "pqrstuv",b = "mnopq") == 2
    assert candidate(a = "abcdefghijklmnopqrstuvwxyz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
    assert candidate(a = "acabcbacbacbacbaca",b = "bdadbdadbdadbdad") == 8
    assert candidate(a = "abcdefghijklmnopqrstu",b = "vwxyzvwxyzvwxyzvwxyz") == 0
    assert candidate(a = "abcdefghijklmnop",b = "zyxwvutsrqponmlkjihgfedcba") == 16
    assert candidate(a = "abcdefghijklmnopqrstuvwxyz",b = "abcdefghijklmnopqrstuvwxy") == 25
    assert candidate(a = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",b = "defdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdef") == 0
    assert candidate(a = "abcabcabcabcabcabcabcabcabcabc",b = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 0
    assert candidate(a = "aabbaacc",b = "zzzzyyxx") == 0
    assert candidate(a = "aaaabbbbcccc",b = "ccccbbbbaaaa") == 12
    assert candidate(a = "abcdefg",b = "zzzzzzz") == 0
    assert candidate(a = "abcdefghijklmnopqrstuvwxy",b = "zyxwvutsrqponmlkjihgfedcba") == 25
    assert candidate(a = "acacacacacacacacacacacacacacaca",b = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc") == 15
    assert candidate(a = "mnop",b = "qrstuvwxyza") == 1
    assert candidate(a = "abcdabcdabcd",b = "xyzxyzxyzxyz") == 0
    assert candidate(a = "abacabadabacaba",b = "zyxzyxzyxzyxzyxzyx") == 0
    assert candidate(a = "same",b = "same") == 4
    assert candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0
    assert candidate(a = "mnopqrstu",b = "vwxyzijkl") == 4
    assert candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "abcdefghijklmnopqrstuvwxyz") == 1
    assert candidate(a = "mnopqrstuvwxy",b = "abcdefghijklmnopqrstuvwxyz") == 14
    assert candidate(a = "abcdabcabc",b = "zyxzxyzxyz") == 0
    assert candidate(a = "abacabadabacabad",b = "zyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == 0
    assert candidate(a = "abcabcabcabcabcabcabcabcabcabc",b = "abcabcabcabcabcabcabcabcabcabc") == 30
    assert candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
    assert candidate(a = "abcdefghijklm",b = "nopqrstuvwxyz") == 0
    assert candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0
    assert candidate(a = "mnopqrstuvwxyzmnopqrstu",b = "abcdefghijklmnopqrstuabcdefghijklmnopqrstu") == 18
    assert candidate(a = "aaabbbcccdddeeefffggghhhhiiiiijjjjjjkkkkkkkllllllllmmmmmmmmmmm",b = "mnopqrstuvwxyzmnopqrstuvwxyzmnopqrstuvwxyzmnopqrstuvwxyz") == 4
    assert candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0
    assert candidate(a = "aaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccdddddddddddddddddddddd",b = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee") == 0
    assert candidate(a = "xyxzyzxzyzxzyzxzyz",b = "zyxzyzxzyzxzyzxzyx") == 18
    assert candidate(a = "abcdefghijklmnop",b = "qrstuvwxyz") == 0
    assert candidate(a = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
    assert candidate(a = "xyzz",b = "abcd") == 0
    assert candidate(a = "racecar",b = "madam") == 5
    assert candidate(a = "abcdefghijklmnopqrstu",b = "vwxyzabcdefghijklmnopqrstu") == 21
    assert candidate(a = "qwe",b = "qwer") == 3
    assert candidate(a = "pppppppppppppppppppppppppppppppppppppppppp",b = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") == 0
    assert candidate(a = "mnbvcxzlkjhgfdsapoiuytrewq",b = "qwertyuiopasdfghjklzxcvbnm") == 26
    assert candidate(a = "abcdabcdabcd",b = "dcbaabcdabcd") == 12
    assert candidate(a = "aaaaabbbbb",b = "bbbbbccccc") == 5
    assert candidate(a = "aaabbbcccdddeeefffggghhhiii",b = "kkklllmmmnnnooopppqqqrrrssstttuuuvvv") == 0
    assert candidate(a = "aaaaaaaaaaaaaaaaaaaaaaa",b = "bbbbbbbbbbbbbbbbbbbbbbbbb") == 0
    assert candidate(a = "abacabadabacabadabacabad",b = "zzzzyyyyxxxxyyyyzzzz") == 0
    assert candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeeeddccbbbaa") == 52
    assert candidate(a = "abacabadabacaba",b = "zzzyyyxxxwwwwvvvvuuuuuuttttttsssssrrrrrqqqqqqpppppoonnnnmmmllllkkkkjjjjiiiihhhhhgggggffffffeeeeeeeedddddccccbbbaaaa") == 10
    assert candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == 52
    assert candidate(a = "mnopqrstuvwxyz",b = "abcdefghijklm") == 1
    assert candidate(a = "one",b = "two") == 1
    assert candidate(a = "qwertyuiopasdfghjklzxcvbnm",b = "qwertyuiopasdfghjklzxcvbnm") == 26
    assert candidate(a = "mississippi",b = "delaware") == 3
    assert candidate(a = "abcdefghijklmnopqrstuvwxyz",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 1
    assert candidate(a = "abc",b = "xyz") == 0
    assert candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "abcdefghijklmnopqrstuvwxyz") == 27
    assert candidate(a = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",b = "mnopmnopmnopmnopmnopmnopmnopmnopmnopmnopmnopmnopmnop") == 0


