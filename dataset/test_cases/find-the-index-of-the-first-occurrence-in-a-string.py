def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(haystack = "ababcabcabababd",needle = "ababd") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "ababcabcabababd",needle = "ababd") == 10: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcde",needle = "f") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcde",needle = "f") == -1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "mississippi",needle = "issi") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "mississippi",needle = "issi") == 1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "sadbutsad",needle = "sad") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "sadbutsad",needle = "sad") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abababa",needle = "aba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abababa",needle = "aba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcdefgh",needle = "efg") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcdefgh",needle = "efg") == 4: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abc",needle = "c") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abc",needle = "c") == 2: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaaa",needle = "bba") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaaa",needle = "bba") == -1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "mississippi",needle = "issip") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "mississippi",needle = "issip") == 4: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abc",needle = "d") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abc",needle = "d") == -1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "a",needle = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "a",needle = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "hello",needle = "ll") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "hello",needle = "ll") == 2: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "leetcode",needle = "leeto") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "leetcode",needle = "leeto") == -1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "ababababab",needle = "aba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "ababababab",needle = "aba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "randomrandomrandom",needle = "random") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "randomrandomrandom",needle = "random") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcdefgabcdefgabcdefg",needle = "efg") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcdefgabcdefgabcdefg",needle = "efg") == 4: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcdefg",needle = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcdefg",needle = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "a quick brown fox jumps over the lazy dog",needle = "quack") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "a quick brown fox jumps over the lazy dog",needle = "quack") == -1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abracadabra",needle = "cad") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abracadabra",needle = "cad") == 4: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaaaaabc",needle = "aaaaaab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaaaaabc",needle = "aaaaaab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "level",needle = "eve") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "level",needle = "eve") == 1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaaaa",needle = "aaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaaaa",needle = "aaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abababab",needle = "aba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abababab",needle = "aba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcde",needle = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcde",needle = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "xylophone",needle = "phone") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "xylophone",needle = "phone") == 4: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcdeabcdeabcde",needle = "deabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcdeabcdeabcde",needle = "deabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "quickbrownfox",needle = "quick") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "quickbrownfox",needle = "quick") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "repeatedstringrepeatedstring",needle = "string") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "repeatedstringrepeatedstring",needle = "string") == 8: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcde",needle = "abcde") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcde",needle = "abcde") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "noinneedlehere",needle = "needle") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "noinneedlehere",needle = "needle") == 4: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "banana",needle = "ana") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "banana",needle = "ana") == 1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcdefghijklmnopqrstuvwxyz",needle = "mnop") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcdefghijklmnopqrstuvwxyz",needle = "mnop") == 12: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcabcabcabcabcabc",needle = "abcabc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcabcabcabcabcabc",needle = "abcabc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "boundarycase",needle = "boundarycase") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "boundarycase",needle = "boundarycase") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcabcabcabc",needle = "bcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcabcabcabc",needle = "bcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",needle = "mnopqrstuv") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",needle = "mnopqrstuv") == -1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "sequence",needle = "qu") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "sequence",needle = "qu") == 2: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "bananananana",needle = "nan") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "bananananana",needle = "nan") == 2: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaaaaaaaaaaaaaaaa",needle = "aaaaaaaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaaaaaaaaaaaaaaaa",needle = "aaaaaaaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcdefghij",needle = "jihgfedcba") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcdefghij",needle = "jihgfedcba") == -1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcdefghij",needle = "abcdefghij") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcdefghij",needle = "abcdefghij") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "thisisaverylongstringwithsomecharacters",needle = "characters") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "thisisaverylongstringwithsomecharacters",needle = "characters") == 29: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "thisisaverylongstringwithsomerepeatingpatterns",needle = "patterns") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "thisisaverylongstringwithsomerepeatingpatterns",needle = "patterns") == 38: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "thesamethesame",needle = "thesame") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "thesamethesame",needle = "thesame") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "noon",needle = "noon") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "noon",needle = "noon") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "hellohellohellohellohello",needle = "hellohello") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "hellohellohellohellohello",needle = "hellohello") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "nnnnnnnnnn",needle = "nnnn") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "nnnnnnnnnn",needle = "nnnn") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "12345678901234567890",needle = "56789012") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "12345678901234567890",needle = "56789012") == 4: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "12345678901234567890",needle = "56789") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "12345678901234567890",needle = "56789") == 4: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcabcabcabcabc",needle = "cab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcabcabcabcabc",needle = "cab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "thisisaverylonghaystack",needle = "averylong") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "thisisaverylonghaystack",needle = "averylong") == 6: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "hellohellohello",needle = "hellohello") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "hellohellohello",needle = "hellohello") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "singleletter",needle = "a") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "singleletter",needle = "a") == -1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "oneonetwoonethreeonethreeone",needle = "three") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "oneonetwoonethreeonethreeone",needle = "three") == 12: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcabcabcabcabcabc",needle = "cab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcabcabcabcabcabc",needle = "cab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "pythonprogrammingpython",needle = "thonpro") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "pythonprogrammingpython",needle = "thonpro") == 2: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "repeatedcharactersequenceeeeeeeeeeeeeee",needle = "eeeeeeee") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "repeatedcharactersequenceeeeeeeeeeeeeee",needle = "eeeeeeee") == 24: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcdabcyabcdabc",needle = "abcdabc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcdabcyabcdabc",needle = "abcdabc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "mississippi",needle = "issipp") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "mississippi",needle = "issipp") == 4: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaaabaaaabaaaaabaaaabaaaaabaaaabaaaaabaaaab",needle = "baaab") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaaabaaaabaaaaabaaaabaaaaabaaaabaaaaabaaaab",needle = "baaab") == -1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaaaa",needle = "aaaaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaaaa",needle = "aaaaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcdefghijklmnopqrstuvwxyz",needle = "xyz") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcdefghijklmnopqrstuvwxyz",needle = "xyz") == 23: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "overlaplaplaplaplap",needle = "lap") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "overlaplaplaplaplap",needle = "lap") == 4: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaaabaaaaaa",needle = "aaaaab") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaaabaaaaaa",needle = "aaaaab") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "helloworldhelloworld",needle = "worldhello") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "helloworldhelloworld",needle = "worldhello") == 5: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abracadabra",needle = "abra") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abracadabra",needle = "abra") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abababababababababab",needle = "ababab") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abababababababababab",needle = "ababab") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aabbccddeeffgghhiijjkk",needle = "eeffgg") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aabbccddeeffgghhiijjkk",needle = "eeffgg") == 8: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",needle = "mnop") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",needle = "mnop") == -1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "mississippiissippi",needle = "issip") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "mississippiissippi",needle = "issip") == 4: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aquickbrownfoxjumpsoverthelazydog",needle = "dog") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aquickbrownfoxjumpsoverthelazydog",needle = "dog") == 30: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abababababababab",needle = "ababab") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abababababababab",needle = "ababab") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "almostsameprefixalmost",needle = "almost") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "almostsameprefixalmost",needle = "almost") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "qwertyuiopasdfghjklzxcvbnm",needle = "qwertyuiop") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "qwertyuiopasdfghjklzxcvbnm",needle = "qwertyuiop") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "ananananananan",needle = "anana") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "ananananananan",needle = "anana") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "averylongstringwithrepeatedcharactersaaaaaaaaa",needle = "aaaaaaaa") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "averylongstringwithrepeatedcharactersaaaaaaaaa",needle = "aaaaaaaa") == 37: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "",needle = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "",needle = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "findinganoccurrenceinanarray",needle = "anoccurrence") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "findinganoccurrenceinanarray",needle = "anoccurrence") == 7: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "repeatedrepeatedrepeated",needle = "repeated") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "repeatedrepeatedrepeated",needle = "repeated") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "pythonprogramming",needle = "programming") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "pythonprogramming",needle = "programming") == 6: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "palindrome",needle = "alin") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "palindrome",needle = "alin") == 1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "singleletter",needle = "s") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "singleletter",needle = "s") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaaaabaaaaaab",needle = "aaaaaab") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaaaabaaaaaab",needle = "aaaaaab") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "thisisaverylongstringthatwilltestouralgorithm",needle = "longstring") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "thisisaverylongstringthatwilltestouralgorithm",needle = "longstring") == 11: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "this is a simple test",needle = "simple") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "this is a simple test",needle = "simple") == 10: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaaabaaaabaaaaabaaaab",needle = "aaaab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaaabaaaabaaaaabaaaab",needle = "aaaab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",needle = "zzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",needle = "zzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "repeatedrepeatedrepeated",needle = "repeatedre") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "repeatedrepeatedrepeated",needle = "repeatedre") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "thelastwordisneedle",needle = "needle") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "thelastwordisneedle",needle = "needle") == 13: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "hellohellohello",needle = "lohe") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "hellohellohello",needle = "lohe") == 3: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abababababab",needle = "ababab") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abababababab",needle = "ababab") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abababababab",needle = "bababa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abababababab",needle = "bababa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "thisisaverylongstringforatest",needle = "avery") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "thisisaverylongstringforatest",needle = "avery") == 6: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "overlappingoverlap",needle = "lapping") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "overlappingoverlap",needle = "lapping") == 4: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "findthehiddenpattern",needle = "hidden") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "findthehiddenpattern",needle = "hidden") == 7: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "ababababab",needle = "abab") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "ababababab",needle = "abab") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "asubstringrightattheend",needle = "end") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "asubstringrightattheend",needle = "end") == 20: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "longstringthatcontainsavarietyofcharacters",needle = "characters") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "longstringthatcontainsavarietyofcharacters",needle = "characters") == 32: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "bananaanabanana",needle = "anaban") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "bananaanabanana",needle = "anaban") == 6: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "racecar",needle = "race") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "racecar",needle = "race") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "longstringwithnokeyword",needle = "keyword") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "longstringwithnokeyword",needle = "keyword") == 16: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcdefghij",needle = "gh") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcdefghij",needle = "gh") == 6: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "mississippi",needle = "pi") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "mississippi",needle = "pi") == 9: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "verylonghaystackwithrepeatingcharactersaaaaaaaaaaa",needle = "aaaaa") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "verylonghaystackwithrepeatingcharactersaaaaaaaaaaa",needle = "aaaaa") == 39: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "",needle = "a") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "",needle = "a") == -1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "a",needle = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "a",needle = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "09876543210987654321",needle = "654321") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "09876543210987654321",needle = "654321") == 4: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "hellohellohello",needle = "hello") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "hellohellohello",needle = "hello") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaaaaaaaaa",needle = "aaaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaaaaaaaaa",needle = "aaaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "thisisaverylongstringthatcontainsmultiplesubstrings",needle = "substring") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "thisisaverylongstringthatcontainsmultiplesubstrings",needle = "substring") == 41: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "uniquecharacters",needle = "characters") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "uniquecharacters",needle = "characters") == 6: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaaaaab",needle = "aaaab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaaaaab",needle = "aaaab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "almosttherealmost",needle = "almostthere") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "almosttherealmost",needle = "almostthere") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaaaaaaaab",needle = "aaaaaab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaaaaaaaab",needle = "aaaaaab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaaabaaaaabaaaaab",needle = "aaaaab") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaaabaaaaabaaaaab",needle = "aaaaab") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "a quick brown fox jumps over the lazy dog",needle = "quick") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "a quick brown fox jumps over the lazy dog",needle = "quick") == 2: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "thisisaverylongstringwithrepeatedpatterns",needle = "repeated") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "thisisaverylongstringwithrepeatedpatterns",needle = "repeated") == 25: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "thisisaverylonghaystackthatcontainsavariablesubstring",needle = "substring") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "thisisaverylonghaystackthatcontainsavariablesubstring",needle = "substring") == 44: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "xxyyzzxxyyzzxxyyzz",needle = "xxyyzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "xxyyzzxxyyzzxxyyzz",needle = "xxyyzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaaa",needle = "aa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaaa",needle = "aa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "ababababababababa",needle = "abab") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "ababababababababa",needle = "abab") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "a quick brown fox jumps over the lazy dog",needle = "lazy") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "a quick brown fox jumps over the lazy dog",needle = "lazy") == 33: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "needleinthestack",needle = "needle") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "needleinthestack",needle = "needle") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaaaaaaaaaaaaaaaaaa",needle = "aaaaaaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaaaaaaaaaaaaaaaaaa",needle = "aaaaaaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaaaaab",needle = "aaaaaab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaaaaab",needle = "aaaaaab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaa",needle = "aaaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaa",needle = "aaaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "substring",needle = "string") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "substring",needle = "string") == 3: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "xyzxyzxyzxyz",needle = "zyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "xyzxyzxyzxyz",needle = "zyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abababababababababab",needle = "abab") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abababababababababab",needle = "abab") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "oneonetwoonetwothree",needle = "twone") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "oneonetwoonetwothree",needle = "twone") == -1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "bananananana",needle = "anan") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "bananananana",needle = "anan") == 1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "xyxxyxyxyxyxyxyx",needle = "xyxyx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "xyxxyxyxyxyxyxyx",needle = "xyxyx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaaabaaaa",needle = "aaab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaaabaaaa",needle = "aaab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcdefghij",needle = "efgh") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcdefghij",needle = "efgh") == 4: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "overlaplaplaplap",needle = "laplap") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "overlaplaplaplap",needle = "laplap") == 4: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "thisisaverylongstringforsearching",needle = "searching") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "thisisaverylongstringforsearching",needle = "searching") == 24: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "bananabananabanana",needle = "nan") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "bananabananabanana",needle = "nan") == 2: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "longhaystackwithaveryspecificsubstring",needle = "averyspecific") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "longhaystackwithaveryspecificsubstring",needle = "averyspecific") == 16: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaaaaa",needle = "aaaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaaaaa",needle = "aaaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcdefabcdefabcdefabcdef",needle = "cdef") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcdefabcdefabcdefabcdef",needle = "cdef") == 2: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "aaaaabaaaaabaaaaabaaaaab",needle = "aaaab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "aaaaabaaaaabaaaaabaaaaab",needle = "aaaab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "hellohellohello",needle = "lohel") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "hellohellohello",needle = "lohel") == 3: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "abcdabcdabcd",needle = "cdab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "abcdabcdabcd",needle = "cdab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(haystack = "banana",needle = "na") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(haystack = "banana",needle = "na") == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(haystack = "ababcabcabababd",needle = "ababd") == 10
    assert candidate(haystack = "abcde",needle = "f") == -1
    assert candidate(haystack = "mississippi",needle = "issi") == 1
    assert candidate(haystack = "sadbutsad",needle = "sad") == 0
    assert candidate(haystack = "abababa",needle = "aba") == 0
    assert candidate(haystack = "abcdefgh",needle = "efg") == 4
    assert candidate(haystack = "abc",needle = "c") == 2
    assert candidate(haystack = "aaaaa",needle = "bba") == -1
    assert candidate(haystack = "mississippi",needle = "issip") == 4
    assert candidate(haystack = "abc",needle = "d") == -1
    assert candidate(haystack = "a",needle = "a") == 0
    assert candidate(haystack = "hello",needle = "ll") == 2
    assert candidate(haystack = "leetcode",needle = "leeto") == -1
    assert candidate(haystack = "ababababab",needle = "aba") == 0
    assert candidate(haystack = "randomrandomrandom",needle = "random") == 0
    assert candidate(haystack = "abcdefgabcdefgabcdefg",needle = "efg") == 4
    assert candidate(haystack = "abcdefg",needle = "") == 0
    assert candidate(haystack = "a quick brown fox jumps over the lazy dog",needle = "quack") == -1
    assert candidate(haystack = "abracadabra",needle = "cad") == 4
    assert candidate(haystack = "aaaaaaabc",needle = "aaaaaab") == 1
    assert candidate(haystack = "level",needle = "eve") == 1
    assert candidate(haystack = "aaaaaa",needle = "aaa") == 0
    assert candidate(haystack = "abababab",needle = "aba") == 0
    assert candidate(haystack = "abcde",needle = "") == 0
    assert candidate(haystack = "xylophone",needle = "phone") == 4
    assert candidate(haystack = "abcdeabcdeabcde",needle = "deabc") == 3
    assert candidate(haystack = "quickbrownfox",needle = "quick") == 0
    assert candidate(haystack = "repeatedstringrepeatedstring",needle = "string") == 8
    assert candidate(haystack = "abcde",needle = "abcde") == 0
    assert candidate(haystack = "noinneedlehere",needle = "needle") == 4
    assert candidate(haystack = "banana",needle = "ana") == 1
    assert candidate(haystack = "abcdefghijklmnopqrstuvwxyz",needle = "mnop") == 12
    assert candidate(haystack = "abcabcabcabcabcabc",needle = "abcabc") == 0
    assert candidate(haystack = "boundarycase",needle = "boundarycase") == 0
    assert candidate(haystack = "abcabcabcabc",needle = "bcabc") == 1
    assert candidate(haystack = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",needle = "mnopqrstuv") == -1
    assert candidate(haystack = "sequence",needle = "qu") == 2
    assert candidate(haystack = "bananananana",needle = "nan") == 2
    assert candidate(haystack = "aaaaaaaaaaaaaaaaaa",needle = "aaaaaaaaaa") == 0
    assert candidate(haystack = "abcdefghij",needle = "jihgfedcba") == -1
    assert candidate(haystack = "abcdefghij",needle = "abcdefghij") == 0
    assert candidate(haystack = "thisisaverylongstringwithsomecharacters",needle = "characters") == 29
    assert candidate(haystack = "thisisaverylongstringwithsomerepeatingpatterns",needle = "patterns") == 38
    assert candidate(haystack = "thesamethesame",needle = "thesame") == 0
    assert candidate(haystack = "noon",needle = "noon") == 0
    assert candidate(haystack = "hellohellohellohellohello",needle = "hellohello") == 0
    assert candidate(haystack = "nnnnnnnnnn",needle = "nnnn") == 0
    assert candidate(haystack = "12345678901234567890",needle = "56789012") == 4
    assert candidate(haystack = "12345678901234567890",needle = "56789") == 4
    assert candidate(haystack = "abcabcabcabcabc",needle = "cab") == 2
    assert candidate(haystack = "thisisaverylonghaystack",needle = "averylong") == 6
    assert candidate(haystack = "hellohellohello",needle = "hellohello") == 0
    assert candidate(haystack = "singleletter",needle = "a") == -1
    assert candidate(haystack = "oneonetwoonethreeonethreeone",needle = "three") == 12
    assert candidate(haystack = "abcabcabcabcabcabc",needle = "cab") == 2
    assert candidate(haystack = "pythonprogrammingpython",needle = "thonpro") == 2
    assert candidate(haystack = "repeatedcharactersequenceeeeeeeeeeeeeee",needle = "eeeeeeee") == 24
    assert candidate(haystack = "abcdabcyabcdabc",needle = "abcdabc") == 0
    assert candidate(haystack = "mississippi",needle = "issipp") == 4
    assert candidate(haystack = "aaaaabaaaabaaaaabaaaabaaaaabaaaabaaaaabaaaab",needle = "baaab") == -1
    assert candidate(haystack = "aaaaaa",needle = "aaaaaaa") == -1
    assert candidate(haystack = "abcdefghijklmnopqrstuvwxyz",needle = "xyz") == 23
    assert candidate(haystack = "overlaplaplaplaplap",needle = "lap") == 4
    assert candidate(haystack = "aaaaabaaaaaa",needle = "aaaaab") == 0
    assert candidate(haystack = "helloworldhelloworld",needle = "worldhello") == 5
    assert candidate(haystack = "abracadabra",needle = "abra") == 0
    assert candidate(haystack = "abababababababababab",needle = "ababab") == 0
    assert candidate(haystack = "aabbccddeeffgghhiijjkk",needle = "eeffgg") == 8
    assert candidate(haystack = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",needle = "mnop") == -1
    assert candidate(haystack = "mississippiissippi",needle = "issip") == 4
    assert candidate(haystack = "aquickbrownfoxjumpsoverthelazydog",needle = "dog") == 30
    assert candidate(haystack = "abababababababab",needle = "ababab") == 0
    assert candidate(haystack = "almostsameprefixalmost",needle = "almost") == 0
    assert candidate(haystack = "qwertyuiopasdfghjklzxcvbnm",needle = "qwertyuiop") == 0
    assert candidate(haystack = "ananananananan",needle = "anana") == 0
    assert candidate(haystack = "averylongstringwithrepeatedcharactersaaaaaaaaa",needle = "aaaaaaaa") == 37
    assert candidate(haystack = "",needle = "") == 0
    assert candidate(haystack = "findinganoccurrenceinanarray",needle = "anoccurrence") == 7
    assert candidate(haystack = "repeatedrepeatedrepeated",needle = "repeated") == 0
    assert candidate(haystack = "pythonprogramming",needle = "programming") == 6
    assert candidate(haystack = "palindrome",needle = "alin") == 1
    assert candidate(haystack = "singleletter",needle = "s") == 0
    assert candidate(haystack = "aaaaaabaaaaaab",needle = "aaaaaab") == 0
    assert candidate(haystack = "thisisaverylongstringthatwilltestouralgorithm",needle = "longstring") == 11
    assert candidate(haystack = "this is a simple test",needle = "simple") == 10
    assert candidate(haystack = "aaaaabaaaabaaaaabaaaab",needle = "aaaab") == 1
    assert candidate(haystack = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",needle = "zzzzzzzzzz") == 0
    assert candidate(haystack = "repeatedrepeatedrepeated",needle = "repeatedre") == 0
    assert candidate(haystack = "thelastwordisneedle",needle = "needle") == 13
    assert candidate(haystack = "hellohellohello",needle = "lohe") == 3
    assert candidate(haystack = "abababababab",needle = "ababab") == 0
    assert candidate(haystack = "abababababab",needle = "bababa") == 1
    assert candidate(haystack = "thisisaverylongstringforatest",needle = "avery") == 6
    assert candidate(haystack = "overlappingoverlap",needle = "lapping") == 4
    assert candidate(haystack = "findthehiddenpattern",needle = "hidden") == 7
    assert candidate(haystack = "ababababab",needle = "abab") == 0
    assert candidate(haystack = "asubstringrightattheend",needle = "end") == 20
    assert candidate(haystack = "longstringthatcontainsavarietyofcharacters",needle = "characters") == 32
    assert candidate(haystack = "bananaanabanana",needle = "anaban") == 6
    assert candidate(haystack = "racecar",needle = "race") == 0
    assert candidate(haystack = "longstringwithnokeyword",needle = "keyword") == 16
    assert candidate(haystack = "abcdefghij",needle = "gh") == 6
    assert candidate(haystack = "mississippi",needle = "pi") == 9
    assert candidate(haystack = "verylonghaystackwithrepeatingcharactersaaaaaaaaaaa",needle = "aaaaa") == 39
    assert candidate(haystack = "",needle = "a") == -1
    assert candidate(haystack = "a",needle = "") == 0
    assert candidate(haystack = "09876543210987654321",needle = "654321") == 4
    assert candidate(haystack = "hellohellohello",needle = "hello") == 0
    assert candidate(haystack = "aaaaaaaaaaa",needle = "aaaaaa") == 0
    assert candidate(haystack = "thisisaverylongstringthatcontainsmultiplesubstrings",needle = "substring") == 41
    assert candidate(haystack = "uniquecharacters",needle = "characters") == 6
    assert candidate(haystack = "aaaaaaab",needle = "aaaab") == 3
    assert candidate(haystack = "almosttherealmost",needle = "almostthere") == 0
    assert candidate(haystack = "aaaaaaaaaab",needle = "aaaaaab") == 4
    assert candidate(haystack = "aaaaabaaaaabaaaaab",needle = "aaaaab") == 0
    assert candidate(haystack = "a quick brown fox jumps over the lazy dog",needle = "quick") == 2
    assert candidate(haystack = "thisisaverylongstringwithrepeatedpatterns",needle = "repeated") == 25
    assert candidate(haystack = "thisisaverylonghaystackthatcontainsavariablesubstring",needle = "substring") == 44
    assert candidate(haystack = "xxyyzzxxyyzzxxyyzz",needle = "xxyyzz") == 0
    assert candidate(haystack = "aaaaa",needle = "aa") == 0
    assert candidate(haystack = "ababababababababa",needle = "abab") == 0
    assert candidate(haystack = "a quick brown fox jumps over the lazy dog",needle = "lazy") == 33
    assert candidate(haystack = "needleinthestack",needle = "needle") == 0
    assert candidate(haystack = "aaaaaaaaaaaaaaaaaaaa",needle = "aaaaaaaaa") == 0
    assert candidate(haystack = "aaaaaaab",needle = "aaaaaab") == 1
    assert candidate(haystack = "aaaa",needle = "aaaaa") == -1
    assert candidate(haystack = "substring",needle = "string") == 3
    assert candidate(haystack = "xyzxyzxyzxyz",needle = "zyx") == -1
    assert candidate(haystack = "abababababababababab",needle = "abab") == 0
    assert candidate(haystack = "oneonetwoonetwothree",needle = "twone") == -1
    assert candidate(haystack = "bananananana",needle = "anan") == 1
    assert candidate(haystack = "xyxxyxyxyxyxyxyx",needle = "xyxyx") == 3
    assert candidate(haystack = "aaaaabaaaa",needle = "aaab") == 2
    assert candidate(haystack = "abcdefghij",needle = "efgh") == 4
    assert candidate(haystack = "overlaplaplaplap",needle = "laplap") == 4
    assert candidate(haystack = "thisisaverylongstringforsearching",needle = "searching") == 24
    assert candidate(haystack = "bananabananabanana",needle = "nan") == 2
    assert candidate(haystack = "longhaystackwithaveryspecificsubstring",needle = "averyspecific") == 16
    assert candidate(haystack = "aaaaaaa",needle = "aaaaaa") == 0
    assert candidate(haystack = "abcdefabcdefabcdefabcdef",needle = "cdef") == 2
    assert candidate(haystack = "aaaaabaaaaabaaaaabaaaaab",needle = "aaaab") == 1
    assert candidate(haystack = "hellohellohello",needle = "lohel") == 3
    assert candidate(haystack = "abcdabcdabcd",needle = "cdab") == 2
    assert candidate(haystack = "banana",needle = "na") == 2


