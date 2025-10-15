def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "ihgfedcbaj") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "ihgfedcbaj") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "noon",s2 = "onon") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "noon",s2 = "onon") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abc",s2 = "cab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc",s2 = "cab") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnop",s2 = "ponmlkjihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnop",s2 = "ponmlkjihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcde",s2 = "caebd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcde",s2 = "caebd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijk",s2 = "abcdefghijk") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijk",s2 = "abcdefghijk") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abc",s2 = "bca") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc",s2 = "bca") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "hgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "hgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "ijabcdefgh") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "ijabcdefgh") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "eebaacbcbcadaaedceaaacadccd",s2 = "eadcaacabaddaceacbceaabe") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "eebaacbcbcadaaedceaaacadccd",s2 = "eadcaacabaddaceacbceaabe") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ab",s2 = "ba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ab",s2 = "ba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "jihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "jihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "abcabc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "abcabc") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "ccbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "ccbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "great",s2 = "rgeat") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "great",s2 = "rgeat") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "abcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "abcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "bdac") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "bdac") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "lohel") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "lohel") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "dcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "dcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabb",s2 = "baba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabb",s2 = "baba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "efghabcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "efghabcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "eebaacb",s2 = "aceebbb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "eebaacb",s2 = "aceebbb") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xstjzkfpqczbdy",s2 = "bdyxzcqpzkjfst") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xstjzkfpqczbdy",s2 = "bdyxzcqpzkjfst") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "olelh") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "olelh") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzz",s2 = "zzyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzz",s2 = "zzyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyz",s2 = "zyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyz",s2 = "zyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "efgabcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "efgabcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijk",s2 = "kabcdefghij") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijk",s2 = "kabcdefghij") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a",s2 = "a") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a",s2 = "a") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "algorithm",s2 = "logarithm") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "algorithm",s2 = "logarithm") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "introduction",s2 = "oitrnuduinc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "introduction",s2 = "oitrnuduinc") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcd",s2 = "ddddcccc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcd",s2 = "ddddcccc") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdexyz",s2 = "zyxdecba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdexyz",s2 = "zyxdecba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdxyz",s2 = "yzabcdx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdxyz",s2 = "yzabcdx") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "efghijklabdc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "efghijklabdc") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "recursion",s2 = "rursiicno") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "recursion",s2 = "rursiicno") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "jihgfecdba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "jihgfecdba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "abcdghfe") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "abcdghfe") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "abijhgfedc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "abijhgfedc") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xylophone",s2 = "eponhloxy") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xylophone",s2 = "eponhloxy") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "gfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "gfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "scramble",s2 = "elmacrbs") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "scramble",s2 = "elmacrbs") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "interview",s2 = "wetneivrt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "interview",s2 = "wetneivrt") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abababab",s2 = "babababa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abababab",s2 = "babababa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "backtracking",s2 = "tcgakknbirn") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "backtracking",s2 = "tcgakknbirn") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "ghfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "ghfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdexyz",s2 = "xyzexbcd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdexyz",s2 = "xyzexbcd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "cdabefgh") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "cdabefgh") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "qwertyuiop",s2 = "yuiopqwert") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "qwertyuiop",s2 = "yuiopqwert") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "intention",s2 = "tennotiin") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "intention",s2 = "tennotiin") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "jihgfedabc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "jihgfedabc") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "cdab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "cdab") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "scramble",s2 = "melbrcsa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "scramble",s2 = "melbrcsa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdexyz",s2 = "xyzabcde") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdexyz",s2 = "xyzabcde") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "algorithm",s2 = "rhtaglmoi") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "algorithm",s2 = "rhtaglmoi") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "optimization",s2 = "tivioonpmzas") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "optimization",s2 = "tivioonpmzas") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "interview",s2 = "ewrotnive") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "interview",s2 = "ewrotnive") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "programming",s2 = "gnimmargorp") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "programming",s2 = "gnimmargorp") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "efghabcdij") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "efghabcdij") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "recursion",s2 = "suoncire") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "recursion",s2 = "suoncire") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "abcdjihgfe") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "abcdjihgfe") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "fedcbaighj") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "fedcbaighj") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "waterbottle",s2 = "elbottlewat") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "waterbottle",s2 = "elbottlewat") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "ghfedcbaab") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "ghfedcbaab") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "scramble",s2 = "leacrbms") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "scramble",s2 = "leacrbms") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "scramble",s2 = "rscmable") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "scramble",s2 = "rscmable") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "algorithm",s2 = "rhtlgmaoi") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "algorithm",s2 = "rhtlgmaoi") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "scrambledstring",s2 = "stgimrebldstring") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "scrambledstring",s2 = "stgimrebldstring") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "mnopqrjkl") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "mnopqrjkl") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijk",s2 = "efghijkabcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijk",s2 = "efghijkabcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abracadabra",s2 = "carrabbadaba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abracadabra",s2 = "carrabbadaba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "ihgfedcbaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "ihgfedcbaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "hgfedcbaij") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "hgfedcbaij") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "abcdghfjie") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "abcdghfjie") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "abcdefghij") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "abcdefghij") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "ihgfjedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "ihgfjedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "ijklabefgh") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "ijklabefgh") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "ghijefabcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "ghijefabcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "ihgfjklmno") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "ihgfjklmno") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "interview",s2 = "reterivne") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "interview",s2 = "reterivne") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "python",s2 = "nohtyp") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "python",s2 = "nohtyp") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "bcdefghiaj") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "bcdefghiaj") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "cdabefghij") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "cdabefghij") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcd",s2 = "dcbacabd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcd",s2 = "dcbacabd") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "scramble",s2 = "blecrmas") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "scramble",s2 = "blecrmas") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "cbadefghij") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "cbadefghij") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "optimization",s2 = "nizationopti") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "optimization",s2 = "nizationopti") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "intvw",s2 = "nvtiw") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "intvw",s2 = "nvtiw") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "cdefghijab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "cdefghijab") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "intervw",s2 = "wvnreit") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "intervw",s2 = "wvnreit") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "efghijabcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "efghijabcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "optimization",s2 = "nizaitpmosio") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "optimization",s2 = "nizaitpmosio") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "algorithm",s2 = "rhtgmialo") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "algorithm",s2 = "rhtgmialo") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "interview",s2 = "terviewin") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "interview",s2 = "terviewin") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcd",s2 = "abcdabcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcd",s2 = "abcdabcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "jabcdefghi") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "jabcdefghi") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijk",s2 = "kjiabcdefgh") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijk",s2 = "kjiabcdefgh") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abab",s2 = "baba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abab",s2 = "baba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "scramble",s2 = "melcarbs") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "scramble",s2 = "melcarbs") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "thisisatest",s2 = "tsaistestihis") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "thisisatest",s2 = "tsaistestihis") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "fghebacijd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "fghebacijd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "ijklabcdefgh") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "ijklabcdefgh") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "scramble",s2 = "ercmsbal") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "scramble",s2 = "ercmsbal") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "scramblestring",s2 = "gterinmbscrl") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "scramblestring",s2 = "gterinmbscrl") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "cbadefghji") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "cbadefghji") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "introduction",s2 = "ntrioduicton") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "introduction",s2 = "ntrioduicton") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "abjihgfedc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "abjihgfedc") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "abcdefghijab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "abcdefghijab") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "recursion",s2 = "insrucero") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "recursion",s2 = "insrucero") == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s1 = "abcdefghij",s2 = "ihgfedcbaj") == True
    assert candidate(s1 = "noon",s2 = "onon") == True
    assert candidate(s1 = "abc",s2 = "cab") == True
    assert candidate(s1 = "abcdefghijklmnop",s2 = "ponmlkjihgfedcba") == True
    assert candidate(s1 = "abcde",s2 = "caebd") == False
    assert candidate(s1 = "abcdefghijk",s2 = "abcdefghijk") == True
    assert candidate(s1 = "abc",s2 = "bca") == True
    assert candidate(s1 = "abcdefgh",s2 = "hgfedcba") == True
    assert candidate(s1 = "abcdefghij",s2 = "ijabcdefgh") == True
    assert candidate(s1 = "eebaacbcbcadaaedceaaacadccd",s2 = "eadcaacabaddaceacbceaabe") == False
    assert candidate(s1 = "ab",s2 = "ba") == True
    assert candidate(s1 = "abcdefghij",s2 = "jihgfedcba") == True
    assert candidate(s1 = "aabbcc",s2 = "abcabc") == True
    assert candidate(s1 = "aabbcc",s2 = "ccbbaa") == True
    assert candidate(s1 = "great",s2 = "rgeat") == True
    assert candidate(s1 = "abcd",s2 = "abcd") == True
    assert candidate(s1 = "abcd",s2 = "bdac") == False
    assert candidate(s1 = "hello",s2 = "lohel") == True
    assert candidate(s1 = "abcd",s2 = "dcba") == True
    assert candidate(s1 = "aabb",s2 = "baba") == True
    assert candidate(s1 = "abcdefgh",s2 = "efghabcd") == True
    assert candidate(s1 = "eebaacb",s2 = "aceebbb") == False
    assert candidate(s1 = "xstjzkfpqczbdy",s2 = "bdyxzcqpzkjfst") == True
    assert candidate(s1 = "hello",s2 = "olelh") == True
    assert candidate(s1 = "xyzz",s2 = "zzyx") == True
    assert candidate(s1 = "xyz",s2 = "zyx") == True
    assert candidate(s1 = "abcdefg",s2 = "efgabcd") == True
    assert candidate(s1 = "abcdefghijk",s2 = "kabcdefghij") == True
    assert candidate(s1 = "a",s2 = "a") == True
    assert candidate(s1 = "algorithm",s2 = "logarithm") == True
    assert candidate(s1 = "introduction",s2 = "oitrnuduinc") == False
    assert candidate(s1 = "abcdabcd",s2 = "ddddcccc") == False
    assert candidate(s1 = "abcdexyz",s2 = "zyxdecba") == True
    assert candidate(s1 = "abcdxyz",s2 = "yzabcdx") == True
    assert candidate(s1 = "abcdefghij",s2 = "efghijklabdc") == False
    assert candidate(s1 = "recursion",s2 = "rursiicno") == False
    assert candidate(s1 = "abcdefghij",s2 = "jihgfecdba") == True
    assert candidate(s1 = "abcdefgh",s2 = "abcdghfe") == True
    assert candidate(s1 = "abcdefghij",s2 = "abijhgfedc") == True
    assert candidate(s1 = "xylophone",s2 = "eponhloxy") == True
    assert candidate(s1 = "abcdefg",s2 = "gfedcba") == True
    assert candidate(s1 = "scramble",s2 = "elmacrbs") == True
    assert candidate(s1 = "interview",s2 = "wetneivrt") == False
    assert candidate(s1 = "abababab",s2 = "babababa") == True
    assert candidate(s1 = "backtracking",s2 = "tcgakknbirn") == False
    assert candidate(s1 = "abcdefgh",s2 = "ghfedcba") == True
    assert candidate(s1 = "abcdexyz",s2 = "xyzexbcd") == False
    assert candidate(s1 = "abcdefgh",s2 = "cdabefgh") == True
    assert candidate(s1 = "qwertyuiop",s2 = "yuiopqwert") == True
    assert candidate(s1 = "intention",s2 = "tennotiin") == True
    assert candidate(s1 = "abcdefghij",s2 = "jihgfedabc") == True
    assert candidate(s1 = "abcd",s2 = "cdab") == True
    assert candidate(s1 = "scramble",s2 = "melbrcsa") == True
    assert candidate(s1 = "abcdexyz",s2 = "xyzabcde") == True
    assert candidate(s1 = "algorithm",s2 = "rhtaglmoi") == False
    assert candidate(s1 = "optimization",s2 = "tivioonpmzas") == False
    assert candidate(s1 = "interview",s2 = "ewrotnive") == False
    assert candidate(s1 = "programming",s2 = "gnimmargorp") == True
    assert candidate(s1 = "abcdefghij",s2 = "efghabcdij") == True
    assert candidate(s1 = "recursion",s2 = "suoncire") == False
    assert candidate(s1 = "abcdefghij",s2 = "abcdjihgfe") == True
    assert candidate(s1 = "abcdefghij",s2 = "fedcbaighj") == True
    assert candidate(s1 = "waterbottle",s2 = "elbottlewat") == False
    assert candidate(s1 = "abcdefghij",s2 = "ghfedcbaab") == False
    assert candidate(s1 = "scramble",s2 = "leacrbms") == True
    assert candidate(s1 = "scramble",s2 = "rscmable") == True
    assert candidate(s1 = "algorithm",s2 = "rhtlgmaoi") == False
    assert candidate(s1 = "scrambledstring",s2 = "stgimrebldstring") == False
    assert candidate(s1 = "abcdefghij",s2 = "mnopqrjkl") == False
    assert candidate(s1 = "abcdefghijk",s2 = "efghijkabcd") == True
    assert candidate(s1 = "abracadabra",s2 = "carrabbadaba") == False
    assert candidate(s1 = "abcdefghij",s2 = "ihgfedcbaa") == False
    assert candidate(s1 = "abcdefghij",s2 = "hgfedcbaij") == True
    assert candidate(s1 = "abcdefghij",s2 = "abcdghfjie") == True
    assert candidate(s1 = "abcdefghij",s2 = "abcdefghij") == True
    assert candidate(s1 = "abcdefghij",s2 = "ihgfjedcba") == True
    assert candidate(s1 = "abcdefghij",s2 = "ijklabefgh") == False
    assert candidate(s1 = "abcdefghij",s2 = "ghijefabcd") == True
    assert candidate(s1 = "abcdefghij",s2 = "ihgfjklmno") == False
    assert candidate(s1 = "interview",s2 = "reterivne") == False
    assert candidate(s1 = "python",s2 = "nohtyp") == True
    assert candidate(s1 = "abcdefghij",s2 = "bcdefghiaj") == True
    assert candidate(s1 = "abcdefghij",s2 = "cdabefghij") == True
    assert candidate(s1 = "abcdabcd",s2 = "dcbacabd") == True
    assert candidate(s1 = "scramble",s2 = "blecrmas") == True
    assert candidate(s1 = "abcdefghij",s2 = "cbadefghij") == True
    assert candidate(s1 = "optimization",s2 = "nizationopti") == False
    assert candidate(s1 = "intvw",s2 = "nvtiw") == True
    assert candidate(s1 = "abcdefghij",s2 = "cdefghijab") == True
    assert candidate(s1 = "intervw",s2 = "wvnreit") == False
    assert candidate(s1 = "abcdefghij",s2 = "efghijabcd") == True
    assert candidate(s1 = "optimization",s2 = "nizaitpmosio") == False
    assert candidate(s1 = "algorithm",s2 = "rhtgmialo") == False
    assert candidate(s1 = "interview",s2 = "terviewin") == True
    assert candidate(s1 = "abcdabcd",s2 = "abcdabcd") == True
    assert candidate(s1 = "abcdefghij",s2 = "jabcdefghi") == True
    assert candidate(s1 = "abcdefghijk",s2 = "kjiabcdefgh") == True
    assert candidate(s1 = "abab",s2 = "baba") == True
    assert candidate(s1 = "scramble",s2 = "melcarbs") == False
    assert candidate(s1 = "thisisatest",s2 = "tsaistestihis") == True
    assert candidate(s1 = "abcdefghij",s2 = "fghebacijd") == False
    assert candidate(s1 = "abcdefghij",s2 = "ijklabcdefgh") == False
    assert candidate(s1 = "scramble",s2 = "ercmsbal") == False
    assert candidate(s1 = "scramblestring",s2 = "gterinmbscrl") == False
    assert candidate(s1 = "abcdefghij",s2 = "cbadefghji") == True
    assert candidate(s1 = "introduction",s2 = "ntrioduicton") == True
    assert candidate(s1 = "abcdefghij",s2 = "abjihgfedc") == True
    assert candidate(s1 = "abcdefghij",s2 = "abcdefghijab") == True
    assert candidate(s1 = "recursion",s2 = "insrucero") == False


