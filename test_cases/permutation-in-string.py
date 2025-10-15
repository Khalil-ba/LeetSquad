def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s1 = "abc",s2 = "bbbccca") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc",s2 = "bbbccca") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "adc",s2 = "dcda") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "adc",s2 = "dcda") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abc",s2 = "bbbccba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc",s2 = "bbbccba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcde",s2 = "adecb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcde",s2 = "adecb") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "test",s2 = "ttewest") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "test",s2 = "ttewest") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abc",s2 = "cbadef") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc",s2 = "cbadef") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abc",s2 = "defabc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc",s2 = "defabc") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyz",s2 = "zyxwvut") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyz",s2 = "zyxwvut") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "ooollehed") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "ooollehed") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ab",s2 = "eidboaoo") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ab",s2 = "eidboaoo") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "abcabc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "abcabc") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "ooolleoooleh") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "ooolleoooleh") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyz",s2 = "ayzxbcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyz",s2 = "ayzxbcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "ooollehdl") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "ooollehdl") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a",s2 = "ab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a",s2 = "ab") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "z",s2 = "abcz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "z",s2 = "abcz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a",s2 = "b") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a",s2 = "b") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "dcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "dcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ab",s2 = "eidbaooo") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ab",s2 = "eidbaooo") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "dcbaefg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "dcbaefg") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abc",s2 = "cccccbabb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc",s2 = "cccccbabb") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaa",s2 = "aaabaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaa",s2 = "aaabaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "abcdxzyw") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "abcdxzyw") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a",s2 = "a") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a",s2 = "a") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abracadabra",s2 = "cadabraabra") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abracadabra",s2 = "cadabraabra") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "unique",s2 = "enquci") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "unique",s2 = "enquci") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "complexity",s2 = "itpelxcmoytz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "complexity",s2 = "itpelxcmoytz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "python",s2 = "nothpy") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "python",s2 = "nothpy") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "permutation",s2 = "aeronpmutitno") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "permutation",s2 = "aeronpmutitno") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "pqrstuvw",s2 = "stuvwpqrxyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "pqrstuvw",s2 = "stuvwpqrxyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzz",s2 = "zzzzzzzzzzzzzzzzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzz",s2 = "zzzzzzzzzzzzzzzzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeff",s2 = "bbccddeeffaabb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeff",s2 = "bbccddeeffaabb") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyz",s2 = "zyxabcdef") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyz",s2 = "zyxabcdef") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "permutation",s2 = "terumtnipxo") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "permutation",s2 = "terumtnipxo") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "characters",s2 = "trchaesrhc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "characters",s2 = "trchaesrhc") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "baccabdefg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "baccabdefg") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "algorithm",s2 = "logarithma") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "algorithm",s2 = "logarithma") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "fedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "fedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "substring",s2 = "tstringsub") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "substring",s2 = "tstringsub") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mnopqr",s2 = "qrstuvwxyzmnopqr") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mnopqr",s2 = "qrstuvwxyzmnopqr") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeff",s2 = "fedcbazyxwvutsrqponmlkjihgfedcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeff",s2 = "fedcbazyxwvutsrqponmlkjihgfedcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "unique",s2 = "eniquu") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "unique",s2 = "eniquu") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "abcdefghijabcdefghij") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "abcdefghijabcdefghij") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyz",s2 = "axbyczd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyz",s2 = "axbyczd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "jihgfedcbaefghijkl") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "jihgfedcbaefghijkl") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "ohellonow") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "ohellonow") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcbaabcde") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcbaabcde") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "substring",s2 = "stringgnusbs") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "substring",s2 = "stringgnusbs") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "permutation",s2 = "tnuatipremot") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "permutation",s2 = "tnuatipremot") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "testcase",s2 = "stceatcases") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "testcase",s2 = "stceatcases") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "unique",s2 = "euqnieabcd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "unique",s2 = "euqnieabcd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "longstring",s2 = "gnirtsolongstring") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "longstring",s2 = "gnirtsolongstring") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcd",s2 = "dcbaabcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcd",s2 = "dcbaabcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",s2 = "isppiimsss") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",s2 = "isppiimsss") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "ghfedcbijklm") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "ghfedcbijklm") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "substringpermutation",s2 = "permutationsubstring") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "substringpermutation",s2 = "permutationsubstring") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "variation",s2 = "atinoriva") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "variation",s2 = "atinoriva") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijk",s2 = "jihgfedcbaklmnopqrs") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijk",s2 = "jihgfedcbaklmnopqrs") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "dcbaefghijklmnopqrstuvwxyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "dcbaefghijklmnopqrstuvwxyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "permutation",s2 = "tporemutani") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "permutation",s2 = "tporemutani") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "complexity",s2 = "xxlpeicmtostiy") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "complexity",s2 = "xxlpeicmtostiy") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "unique",s2 = "ueiqnunc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "unique",s2 = "ueiqnunc") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "cbacbacbacbacbacbacbacbacb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "cbacbacbacbacbacbacbacbacb") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "ghijklmnopabcdefg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "ghijklmnopabcdefg") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghiklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghiklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeff",s2 = "fedcbafedcbafedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeff",s2 = "fedcbafedcbafedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "challenge",s2 = "hgelangecllon") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "challenge",s2 = "hgelangecllon") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "gfedcbahijklmnopqrstuvwxyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "gfedcbahijklmnopqrstuvwxyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "permutation",s2 = "tpremnoiuat") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "permutation",s2 = "tpremnoiuat") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "oellhworld") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "oellhworld") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "test",s2 = "tsetabcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "test",s2 = "tsetabcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijk",s2 = "kljihgfedcbazyxwvutsrqponml") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijk",s2 = "kljihgfedcbazyxwvutsrqponml") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "fedcbaxyzabcdef") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "fedcbaxyzabcdef") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "example",s2 = "melpaxe") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "example",s2 = "melpaxe") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "interview",s2 = "wterevinirt") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "interview",s2 = "wterevinirt") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zyxw",s2 = "wxyzabcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zyxw",s2 = "wxyzabcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "permutation",s2 = "ttnremuapoi") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "permutation",s2 = "ttnremuapoi") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzz",s2 = "zzzyxzzzzzyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzz",s2 = "zzzyxzzzzzyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "ohellworld") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "ohellworld") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "longstring",s2 = "tgnirlongs") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "longstring",s2 = "tgnirlongs") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "bbccaaabcdef") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "bbccaaabcdef") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaabbbbb",s2 = "ababababab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaabbbbb",s2 = "ababababab") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "complexpermutation",s2 = "xmplxcmpotrenuati") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "complexpermutation",s2 = "xmplxcmpotrenuati") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyz",s2 = "zyxzyxzyxzyxzyx") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyz",s2 = "zyxzyxzyxzyxzyx") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",s2 = "ssippiimis") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",s2 = "ssippiimis") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbbccc",s2 = "cccbbbaaabbbcccaabb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbbccc",s2 = "cccbbbaaabbbcccaabb") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyz",s2 = "zyxwvutsrqponmlkjihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyz",s2 = "zyxwvutsrqponmlkjihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "zyxwvutsrqponmlkjihgfedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "zyxwvutsrqponmlkjihgfedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "permutationexample",s2 = "xamplepermutation") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "permutationexample",s2 = "xamplepermutation") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "substring",s2 = "ggnirtsabcd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "substring",s2 = "ggnirtsabcd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "hgfedcbaijkl") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "hgfedcbaijkl") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadabacaba",s2 = "badacababacabadaba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadabacaba",s2 = "badacababacabadaba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "characters",s2 = "tcsrhaec") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "characters",s2 = "tcsrhaec") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "longerstring",s2 = "stringlongeron") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "longerstring",s2 = "stringlongeron") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "baccab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "baccab") == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s1 = "abc",s2 = "bbbccca") == False
    assert candidate(s1 = "adc",s2 = "dcda") == True
    assert candidate(s1 = "abc",s2 = "bbbccba") == True
    assert candidate(s1 = "abcde",s2 = "adecb") == True
    assert candidate(s1 = "test",s2 = "ttewest") == False
    assert candidate(s1 = "abc",s2 = "cbadef") == True
    assert candidate(s1 = "abc",s2 = "defabc") == True
    assert candidate(s1 = "xyz",s2 = "zyxwvut") == True
    assert candidate(s1 = "hello",s2 = "ooollehed") == True
    assert candidate(s1 = "ab",s2 = "eidboaoo") == False
    assert candidate(s1 = "aabbcc",s2 = "abcabc") == True
    assert candidate(s1 = "hello",s2 = "ooolleoooleh") == False
    assert candidate(s1 = "xyz",s2 = "ayzxbcd") == True
    assert candidate(s1 = "hello",s2 = "ooollehdl") == True
    assert candidate(s1 = "a",s2 = "ab") == True
    assert candidate(s1 = "z",s2 = "abcz") == True
    assert candidate(s1 = "a",s2 = "b") == False
    assert candidate(s1 = "abcd",s2 = "dcba") == True
    assert candidate(s1 = "ab",s2 = "eidbaooo") == True
    assert candidate(s1 = "abcd",s2 = "dcbaefg") == True
    assert candidate(s1 = "abc",s2 = "cccccbabb") == True
    assert candidate(s1 = "aaaa",s2 = "aaabaaaa") == True
    assert candidate(s1 = "abcd",s2 = "abcdxzyw") == True
    assert candidate(s1 = "a",s2 = "a") == True
    assert candidate(s1 = "abracadabra",s2 = "cadabraabra") == True
    assert candidate(s1 = "unique",s2 = "enquci") == False
    assert candidate(s1 = "complexity",s2 = "itpelxcmoytz") == True
    assert candidate(s1 = "python",s2 = "nothpy") == True
    assert candidate(s1 = "permutation",s2 = "aeronpmutitno") == True
    assert candidate(s1 = "pqrstuvw",s2 = "stuvwpqrxyz") == True
    assert candidate(s1 = "zzzzz",s2 = "zzzzzzzzzzzzzzzzzzzzzz") == True
    assert candidate(s1 = "aabbccddeeff",s2 = "bbccddeeffaabb") == True
    assert candidate(s1 = "xyz",s2 = "zyxabcdef") == True
    assert candidate(s1 = "permutation",s2 = "terumtnipxo") == False
    assert candidate(s1 = "characters",s2 = "trchaesrhc") == False
    assert candidate(s1 = "aabbcc",s2 = "baccabdefg") == True
    assert candidate(s1 = "algorithm",s2 = "logarithma") == True
    assert candidate(s1 = "abcdef",s2 = "fedcba") == True
    assert candidate(s1 = "substring",s2 = "tstringsub") == True
    assert candidate(s1 = "mnopqr",s2 = "qrstuvwxyzmnopqr") == True
    assert candidate(s1 = "aabbccddeeff",s2 = "fedcbazyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(s1 = "unique",s2 = "eniquu") == True
    assert candidate(s1 = "abcdefghij",s2 = "abcdefghijabcdefghij") == True
    assert candidate(s1 = "xyz",s2 = "axbyczd") == False
    assert candidate(s1 = "abcdefghij",s2 = "jihgfedcbaefghijkl") == True
    assert candidate(s1 = "hello",s2 = "ohellonow") == True
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcbaabcde") == True
    assert candidate(s1 = "substring",s2 = "stringgnusbs") == False
    assert candidate(s1 = "permutation",s2 = "tnuatipremot") == True
    assert candidate(s1 = "testcase",s2 = "stceatcases") == False
    assert candidate(s1 = "unique",s2 = "euqnieabcd") == False
    assert candidate(s1 = "longstring",s2 = "gnirtsolongstring") == True
    assert candidate(s1 = "abcdabcd",s2 = "dcbaabcd") == True
    assert candidate(s1 = "mississippi",s2 = "isppiimsss") == False
    assert candidate(s1 = "abcdef",s2 = "ghfedcbijklm") == False
    assert candidate(s1 = "substringpermutation",s2 = "permutationsubstring") == True
    assert candidate(s1 = "variation",s2 = "atinoriva") == True
    assert candidate(s1 = "abcdefghijk",s2 = "jihgfedcbaklmnopqrs") == True
    assert candidate(s1 = "abcd",s2 = "dcbaefghijklmnopqrstuvwxyz") == True
    assert candidate(s1 = "permutation",s2 = "tporemutani") == True
    assert candidate(s1 = "complexity",s2 = "xxlpeicmtostiy") == False
    assert candidate(s1 = "unique",s2 = "ueiqnunc") == True
    assert candidate(s1 = "aabbcc",s2 = "cbacbacbacbacbacbacbacbacb") == True
    assert candidate(s1 = "abcdefg",s2 = "ghijklmnopabcdefg") == True
    assert candidate(s1 = "abcdefghiklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == False
    assert candidate(s1 = "aabbccddeeff",s2 = "fedcbafedcbafedcba") == True
    assert candidate(s1 = "challenge",s2 = "hgelangecllon") == False
    assert candidate(s1 = "abcdefg",s2 = "gfedcbahijklmnopqrstuvwxyz") == True
    assert candidate(s1 = "permutation",s2 = "tpremnoiuat") == True
    assert candidate(s1 = "hello",s2 = "oellhworld") == True
    assert candidate(s1 = "test",s2 = "tsetabcd") == True
    assert candidate(s1 = "abcdefghijk",s2 = "kljihgfedcbazyxwvutsrqponml") == False
    assert candidate(s1 = "abcdef",s2 = "fedcbaxyzabcdef") == True
    assert candidate(s1 = "example",s2 = "melpaxe") == True
    assert candidate(s1 = "interview",s2 = "wterevinirt") == True
    assert candidate(s1 = "zyxw",s2 = "wxyzabcd") == True
    assert candidate(s1 = "permutation",s2 = "ttnremuapoi") == True
    assert candidate(s1 = "xyzz",s2 = "zzzyxzzzzzyx") == True
    assert candidate(s1 = "hello",s2 = "ohellworld") == True
    assert candidate(s1 = "longstring",s2 = "tgnirlongs") == True
    assert candidate(s1 = "aabbcc",s2 = "bbccaaabcdef") == True
    assert candidate(s1 = "aaaaabbbbb",s2 = "ababababab") == True
    assert candidate(s1 = "complexpermutation",s2 = "xmplxcmpotrenuati") == False
    assert candidate(s1 = "xyz",s2 = "zyxzyxzyxzyxzyx") == True
    assert candidate(s1 = "mississippi",s2 = "ssippiimis") == False
    assert candidate(s1 = "aabbbccc",s2 = "cccbbbaaabbbcccaabb") == True
    assert candidate(s1 = "xyz",s2 = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(s1 = "abcdefg",s2 = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(s1 = "permutationexample",s2 = "xamplepermutation") == False
    assert candidate(s1 = "substring",s2 = "ggnirtsabcd") == False
    assert candidate(s1 = "abcdefgh",s2 = "hgfedcbaijkl") == True
    assert candidate(s1 = "abacabadabacaba",s2 = "badacababacabadaba") == True
    assert candidate(s1 = "characters",s2 = "tcsrhaec") == False
    assert candidate(s1 = "longerstring",s2 = "stringlongeron") == True
    assert candidate(s1 = "aabbcc",s2 = "baccab") == True


