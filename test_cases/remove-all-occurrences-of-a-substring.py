def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abcd",part = "efg") == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",part = "efg") == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzz",part = "zz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzz",part = "zz") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",part = "abcd") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",part = "abcd") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",part = "xyz") == "abcdefg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",part = "xyz") == "abcdefg": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",part = "f") == "abcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",part = "f") == "abcde": {e}')
    
    total += 1
    try:
        result = candidate(s = "daabcbaabcbc",part = "abc") == "dab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "daabcbaabcbc",part = "abc") == "dab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",part = "bca") == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",part = "bca") == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "axxxxyyyyb",part = "xy") == "ab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "axxxxyyyyb",part = "xy") == "ab": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",part = "ll") == "heo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",part = "ll") == "heo": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",part = "abc") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",part = "abc") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa",part = "aa") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa",part = "aa") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",part = "issi") == "mssippi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",part = "issi") == "mssippi": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab",part = "aba") == "bb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab",part = "aba") == "bb": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaa",part = "aa") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaa",part = "aa") == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzz",part = "zzz") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzz",part = "zzz") == "z": {e}')
    
    total += 1
    try:
        result = candidate(s = "banana",part = "na") == "ba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana",part = "na") == "ba": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",part = "cab") == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",part = "cab") == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabababa",part = "aba") == "ba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabababa",part = "aba") == "ba": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab",part = "abab") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab",part = "abab") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopqwertyuiopqwertyuiop",part = "erty") == "qwuiopqwuiopqwuiop"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopqwertyuiopqwertyuiop",part = "erty") == "qwuiopqwuiopqwuiop": {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohellohellohello",part = "hello") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohellohellohello",part = "hello") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",part = "xyz") == "abcdefghij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",part = "xyz") == "abcdefghij": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcd",part = "dabc") == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcd",part = "dabc") == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",part = "xyz") == "abcdefghijklmnopqrstuvw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",part = "xyz") == "abcdefghijklmnopqrstuvw": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",part = "bbcc") == "aaddeeff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",part = "bbcc") == "aaddeeff": {e}')
    
    total += 1
    try:
        result = candidate(s = "exampleexampleexampleexample",part = "exampleexample") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "exampleexampleexampleexample",part = "exampleexample") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaabbbbbbbcccccc",part = "abc") == "aaaaaaabbbbbbbcccccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaabbbbbbbcccccc",part = "abc") == "aaaaaaabbbbbbbcccccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbcccc",part = "ab") == "cccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbcccc",part = "ab") == "cccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringthatwillbeusedtocheckthefunctionality",part = "is") == "thaverylongstringthatwillbeusedtocheckthefunctionality"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringthatwillbeusedtocheckthefunctionality",part = "is") == "thaverylongstringthatwillbeusedtocheckthefunctionality": {e}')
    
    total += 1
    try:
        result = candidate(s = "yyyyyyyyyyyyyyyyyyyy",part = "yyyy") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "yyyyyyyyyyyyyyyyyyyy",part = "yyyy") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "lkjhgfedcba",part = "fe") == "lkjhgdcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lkjhgfedcba",part = "fe") == "lkjhgdcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohello",part = "lohe") == "hellllo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohello",part = "lohe") == "hellllo": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcdeabcde",part = "abc") == "dededede"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcdeabcde",part = "abc") == "dededede": {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohellohello",part = "elloh") == "hello"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohellohello",part = "elloh") == "hello": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",part = "abc") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",part = "abc") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabcdeeeeee",part = "aaa") == "abcdeeeeee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabcdeeeeee",part = "aaa") == "abcdeeeeee": {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",part = "qwerty") == "uiopasdfghjklzxcvbnmuiop"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",part = "qwerty") == "uiopasdfghjklzxcvbnmuiop": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",part = "zz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",part = "zz") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "stackoverflow",part = "flow") == "stackover"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "stackoverflow",part = "flow") == "stackover": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaabaaaaa",part = "aaaa") == "aaaba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaabaaaaa",part = "aaaa") == "aaaba": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghij",part = "ghij") == "abcdefabcdefabcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghij",part = "ghij") == "abcdefabcdefabcdef": {e}')
    
    total += 1
    try:
        result = candidate(s = "acabacabacabacabacab",part = "acab") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acabacabacabacabacab",part = "acab") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghij",part = "abcdefghij") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghij",part = "abcdefghij") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbcccccc",part = "abccba") == "aaaaaaaaaabbbbbbbbbbcccccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbcccccc",part = "abccba") == "aaaaaaaaaabbbbbbbbbbcccccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",part = "jihgfedcba") == "abcdefghij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",part = "jihgfedcba") == "abcdefghij": {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopqwertyuiop",part = "rty") == "qweuiopqweuiop"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopqwertyuiop",part = "rty") == "qweuiopqweuiop": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab",part = "aba") == "bbab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab",part = "aba") == "bbab": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg",part = "bbcc") == "aaddeeffgg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg",part = "bbcc") == "aaddeeffgg": {e}')
    
    total += 1
    try:
        result = candidate(s = "racecaracecaracecar",part = "aceca") == "rrrr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecaracecaracecar",part = "aceca") == "rrrr": {e}')
    
    total += 1
    try:
        result = candidate(s = "xylophoneisfunxylophoneisfunxylophoneisfun",part = "xylophoneis") == "funfunfun"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xylophoneisfunxylophoneisfunxylophoneisfun",part = "xylophoneis") == "funfunfun": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",part = "abaca") == "badba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",part = "abaca") == "badba": {e}')
    
    total += 1
    try:
        result = candidate(s = "supercalifragilisticexpialidocious",part = "cious") == "supercalifragilisticexpialido"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "supercalifragilisticexpialidocious",part = "cious") == "supercalifragilisticexpialido": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab",part = "bab") == "aaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab",part = "bab") == "aaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc",part = "abcabc") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc",part = "abcabc") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdef",part = "defabc") == "abcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdef",part = "defabc") == "abcdef": {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra",part = "abra") == "cad"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra",part = "abra") == "cad": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaaabaaa",part = "aab") == "aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaaabaaa",part = "aab") == "aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "longstringwithsomerepeatedpatternpattern",part = "pattern") == "longstringwithsomerepeated"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longstringwithsomerepeatedpatternpattern",part = "pattern") == "longstringwithsomerepeated": {e}')
    
    total += 1
    try:
        result = candidate(s = "programmingprogrammingprogramming",part = "gram") == "promingpromingproming"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programmingprogrammingprogramming",part = "gram") == "promingpromingproming": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabc",part = "abcabc") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabc",part = "abcabc") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabaaaaabaaaaab",part = "ba") == "aaaaaaaaaaaaab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabaaaaabaaaaab",part = "ba") == "aaaaaaaaaaaaab": {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohellohellohellohello",part = "ll") == "heoheoheoheoheoheo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohellohellohellohello",part = "ll") == "heoheoheoheoheoheo": {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",part = "qwerty") == "uiopasdfghjklzxcvbnmuiopasdfghjklzxcvbnm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",part = "qwerty") == "uiopasdfghjklzxcvbnmuiopasdfghjklzxcvbnm": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyz",part = "xyzxyz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyz",part = "xyzxyz") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaapplebanana",part = "an") == "baappleba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaapplebanana",part = "an") == "baappleba": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",part = "mnop") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",part = "mnop") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxy",part = "xyx") == "yyxy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxy",part = "xyx") == "yyxy": {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohellohello",part = "llohe") == "hello"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohellohello",part = "llohe") == "hello": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbcccccd",part = "abc") == "aaaaabbbbbcccccd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbcccccd",part = "abc") == "aaaaabbbbbcccccd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",part = "cdab") == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",part = "cdab") == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyz",part = "xyz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyz",part = "xyz") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",part = "nopqr") == "abcdefghijklmstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",part = "nopqr") == "abcdefghijklmstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyxzyxzyxzyxzyxzyx",part = "zyx") == "xy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyxzyxzyxzyxzyxzyx",part = "zyx") == "xy": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",part = "zzz") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",part = "zzz") == "z": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefg",part = "efgabc") == "abcdddefg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefg",part = "efgabc") == "abcdddefg": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab",part = "abab") == "ab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab",part = "abab") == "ab": {e}')
    
    total += 1
    try:
        result = candidate(s = "xxxxxxxxxxxxxxxxxxxx",part = "xxx") == "xx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xxxxxxxxxxxxxxxxxxxx",part = "xxx") == "xx": {e}')
    
    total += 1
    try:
        result = candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",part = "micro") == "pneumonoultrascopicsilicovolcanoconiosis"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",part = "micro") == "pneumonoultrascopicsilicovolcanoconiosis": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg",part = "def") == "abcgabcg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg",part = "def") == "abcgabcg": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeaabbccddeeaabbccddeeaabbccdd",part = "abcd") == "aabbccddeeaabbccddeeaabbccddeeaabbccdd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeaabbccddeeaabbccddeeaabbccdd",part = "abcd") == "aabbccddeeaabbccddeeaabbccddeeaabbccdd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacaba",part = "abad") == "abacabacabacaba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacaba",part = "abad") == "abacabacabacaba": {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",part = "erty") == "qwuiopasdfghjklzxcvbnmqwuiop"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",part = "erty") == "qwuiopasdfghjklzxcvbnmqwuiop": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdeabcdabcdeabcd",part = "bcde") == "abcdaabcdaabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdeabcdabcdeabcd",part = "bcde") == "abcdaabcdaabcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcd",part = "abcd") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcd",part = "abcd") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababababababababababab",part = "abab") == "ab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababababababababababab",part = "abab") == "ab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcd",part = "abcdabcd") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcd",part = "abcdabcd") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",part = "zyx") == "wvutsrqponmlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",part = "zyx") == "wvutsrqponmlkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmqwerty",part = "erty") == "qwuiopasdfghjklzxcvbnmqw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmqwerty",part = "erty") == "qwuiopasdfghjklzxcvbnmqw": {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoonnoon",part = "noon") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoonnoon",part = "noon") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "oneonetwoonethreeonefouronefiveonesixone",part = "oneone") == "twoonethreeonefouronefiveonesixone"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "oneonetwoonethreeonefouronefiveonesixone",part = "oneone") == "twoonethreeonefouronefiveonesixone": {e}')
    
    total += 1
    try:
        result = candidate(s = "12345678901234567890",part = "345") == "12678901267890"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "12345678901234567890",part = "345") == "12678901267890": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",part = "def") == "abcghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",part = "def") == "abcghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithrepeatedpatterns",part = "pattern") == "thisisaverylongstringwithrepeateds"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithrepeatedpatterns",part = "pattern") == "thisisaverylongstringwithrepeateds": {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",part = "mnop") == "qwertyuiopasdfghjklzxcvbnm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",part = "mnop") == "qwertyuiopasdfghjklzxcvbnm": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghij",part = "cdefg") == "abhijabhij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghij",part = "cdefg") == "abhijabhij": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaabbbbbaaaaaaaaaaabbbbbaaaaaaaaaaabbbbbaaaaaaaaaaabbbbb",part = "aaaabbbb") == "aaaaaaaabaaaaaaabaaaaaaabaaaaaaab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaabbbbbaaaaaaaaaaabbbbbaaaaaaaaaaabbbbbaaaaaaaaaaabbbbb",part = "aaaabbbb") == "aaaaaaaabaaaaaaabaaaaaaabaaaaaaab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghabcdefghabcdefgh",part = "efgh") == "abcdabcdabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghabcdefghabcdefgh",part = "efgh") == "abcdabcdabcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithrepeatedpattern",part = "pattern") == "thisisaverylongstringwithrepeated"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithrepeatedpattern",part = "pattern") == "thisisaverylongstringwithrepeated": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababab",part = "abab") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababab",part = "abab") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcdeabcde",part = "abcde") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcdeabcde",part = "abcde") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab",part = "ababa") == "bbbab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab",part = "ababa") == "bbbab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcde",part = "bcde") == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcde",part = "bcde") == "aaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",part = "gh") == "abcdefij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",part = "gh") == "abcdefij": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",part = "abc") == "aabbccddeeff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",part = "abc") == "aabbccddeeff": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxxyxyxyx",part = "xyx") == "y"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxxyxyxyx",part = "xyx") == "y": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaa",part = "aa") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaa",part = "aa") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdef",part = "defabc") == "abcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdef",part = "defabc") == "abcdef": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzz",part = "zz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzz",part = "zz") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaanananasanananananana",part = "ana") == "bnnasnnna"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaanananasanananananana",part = "ana") == "bnnasnnna": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc",part = "abcabc") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc",part = "abcabc") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaa",part = "a") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaa",part = "a") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",part = "efg") == "abcdhij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",part = "efg") == "abcdhij": {e}')
    
    total += 1
    try:
        result = candidate(s = "onetwothreefourfivesixseveneightnineseven",part = "seven") == "onetwothreefourfivesixeightnine"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "onetwothreefourfivesixseveneightnineseven",part = "seven") == "onetwothreefourfivesixeightnine": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc",part = "ab") == "cccccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc",part = "ab") == "cccccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",part = "iss") == "mippi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",part = "iss") == "mippi": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc",part = "bbcc") == "aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc",part = "bbcc") == "aaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabraabracadabra",part = "bracad") == "aabraaabra"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabraabracadabra",part = "bracad") == "aabraaabra": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",part = "abcdabcd") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",part = "abcdabcd") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababab",part = "aba") == "bbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababab",part = "aba") == "bbbb": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",part = "zzzz") == "zz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",part = "zzzz") == "zz": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyz",part = "xyzxyz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyz",part = "xyzxyz") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaa",part = "aaa") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaa",part = "aaa") == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "repeatedrepeatedrepeatedrepeated",part = "repeated") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeatedrepeatedrepeatedrepeated",part = "repeated") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzz",part = "zzzz") == "zz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzz",part = "zzzz") == "zz": {e}')
    
    total += 1
    try:
        result = candidate(s = "repeatedsubstringrepeatedsubstring",part = "ted") == "repeasubstringrepeasubstring"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeatedsubstringrepeatedsubstring",part = "ted") == "repeasubstringrepeasubstring": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijkabcdefghijkabcdefghijk",part = "efg") == "abcdhijkabcdhijkabcdhijk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijkabcdefghijkabcdefghijk",part = "efg") == "abcdhijkabcdhijkabcdhijk": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrsmnopqrsmnopqrs",part = "mnopqrs") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrsmnopqrsmnopqrs",part = "mnopqrs") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "ananasanananas",part = "ana") == "nasns"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ananasanananas",part = "ana") == "nasns": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzz",part = "zz") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzz",part = "zz") == "z": {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithrepeatedparts",part = "thisis") == "averylongstringwithrepeatedparts"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithrepeatedparts",part = "thisis") == "averylongstringwithrepeatedparts": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abcd",part = "efg") == "abcd"
    assert candidate(s = "zzzz",part = "zz") == ""
    assert candidate(s = "abcdabcdabcd",part = "abcd") == ""
    assert candidate(s = "abcdefg",part = "xyz") == "abcdefg"
    assert candidate(s = "abcde",part = "f") == "abcde"
    assert candidate(s = "daabcbaabcbc",part = "abc") == "dab"
    assert candidate(s = "abcabcabc",part = "bca") == "abc"
    assert candidate(s = "axxxxyyyyb",part = "xy") == "ab"
    assert candidate(s = "hello",part = "ll") == "heo"
    assert candidate(s = "abcabcabc",part = "abc") == ""
    assert candidate(s = "aaaa",part = "aa") == ""
    assert candidate(s = "mississippi",part = "issi") == "mssippi"
    assert candidate(s = "abababab",part = "aba") == "bb"
    assert candidate(s = "aaaaaaa",part = "aa") == "a"
    assert candidate(s = "zzzzzzz",part = "zzz") == "z"
    assert candidate(s = "banana",part = "na") == "ba"
    assert candidate(s = "abcabcabc",part = "cab") == "abc"
    assert candidate(s = "aabababa",part = "aba") == "ba"
    assert candidate(s = "abababababababababab",part = "abab") == ""
    assert candidate(s = "qwertyuiopqwertyuiopqwertyuiop",part = "erty") == "qwuiopqwuiopqwuiop"
    assert candidate(s = "hellohellohellohellohello",part = "hello") == ""
    assert candidate(s = "abcdefghij",part = "xyz") == "abcdefghij"
    assert candidate(s = "abcdabcdabcdabcd",part = "dabc") == "abcd"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",part = "xyz") == "abcdefghijklmnopqrstuvw"
    assert candidate(s = "aabbccddeeff",part = "bbcc") == "aaddeeff"
    assert candidate(s = "exampleexampleexampleexample",part = "exampleexample") == ""
    assert candidate(s = "aaaaaaabbbbbbbcccccc",part = "abc") == "aaaaaaabbbbbbbcccccc"
    assert candidate(s = "aaaaabbbbbcccc",part = "ab") == "cccc"
    assert candidate(s = "thisisaverylongstringthatwillbeusedtocheckthefunctionality",part = "is") == "thaverylongstringthatwillbeusedtocheckthefunctionality"
    assert candidate(s = "yyyyyyyyyyyyyyyyyyyy",part = "yyyy") == ""
    assert candidate(s = "lkjhgfedcba",part = "fe") == "lkjhgdcba"
    assert candidate(s = "hellohellohello",part = "lohe") == "hellllo"
    assert candidate(s = "abcdeabcdeabcdeabcde",part = "abc") == "dededede"
    assert candidate(s = "hellohellohellohello",part = "elloh") == "hello"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",part = "abc") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
    assert candidate(s = "aaaaaaaaaabcdeeeeee",part = "aaa") == "abcdeeeeee"
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",part = "qwerty") == "uiopasdfghjklzxcvbnmuiop"
    assert candidate(s = "zzzzzzzzzz",part = "zz") == ""
    assert candidate(s = "stackoverflow",part = "flow") == "stackover"
    assert candidate(s = "aaaaaaabaaaaa",part = "aaaa") == "aaaba"
    assert candidate(s = "abcdefghijabcdefghijabcdefghij",part = "ghij") == "abcdefabcdefabcdef"
    assert candidate(s = "acabacabacabacabacab",part = "acab") == ""
    assert candidate(s = "abcdefghijabcdefghijabcdefghij",part = "abcdefghij") == ""
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbcccccc",part = "abccba") == "aaaaaaaaaabbbbbbbbbbcccccc"
    assert candidate(s = "abcdefghij",part = "jihgfedcba") == "abcdefghij"
    assert candidate(s = "qwertyuiopqwertyuiop",part = "rty") == "qweuiopqweuiop"
    assert candidate(s = "ababababab",part = "aba") == "bbab"
    assert candidate(s = "aabbccddeeffgg",part = "bbcc") == "aaddeeffgg"
    assert candidate(s = "racecaracecaracecar",part = "aceca") == "rrrr"
    assert candidate(s = "xylophoneisfunxylophoneisfunxylophoneisfun",part = "xylophoneis") == "funfunfun"
    assert candidate(s = "abacabadabacaba",part = "abaca") == "badba"
    assert candidate(s = "supercalifragilisticexpialidocious",part = "cious") == "supercalifragilisticexpialido"
    assert candidate(s = "abababababababababab",part = "bab") == "aaaaa"
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc",part = "abcabc") == ""
    assert candidate(s = "abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdef",part = "defabc") == "abcdef"
    assert candidate(s = "abracadabra",part = "abra") == "cad"
    assert candidate(s = "aaabaaaabaaa",part = "aab") == "aaaaaa"
    assert candidate(s = "longstringwithsomerepeatedpatternpattern",part = "pattern") == "longstringwithsomerepeated"
    assert candidate(s = "programmingprogrammingprogramming",part = "gram") == "promingpromingproming"
    assert candidate(s = "abcabcabcabcabcabcabcabc",part = "abcabc") == ""
    assert candidate(s = "aaaaabaaaaabaaaaab",part = "ba") == "aaaaaaaaaaaaab"
    assert candidate(s = "hellohellohellohellohellohello",part = "ll") == "heoheoheoheoheoheo"
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",part = "qwerty") == "uiopasdfghjklzxcvbnmuiopasdfghjklzxcvbnm"
    assert candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyz",part = "xyzxyz") == ""
    assert candidate(s = "bananaapplebanana",part = "an") == "baappleba"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",part = "mnop") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
    assert candidate(s = "xyxyxyxyxy",part = "xyx") == "yyxy"
    assert candidate(s = "hellohellohellohello",part = "llohe") == "hello"
    assert candidate(s = "aaaaabbbbbcccccd",part = "abc") == "aaaaabbbbbcccccd"
    assert candidate(s = "abcdabcdabcd",part = "cdab") == "abcd"
    assert candidate(s = "xyzxyzxyzxyz",part = "xyz") == ""
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",part = "nopqr") == "abcdefghijklmstuvwxyz"
    assert candidate(s = "xyzyxzyxzyxzyxzyxzyx",part = "zyx") == "xy"
    assert candidate(s = "zzzzzzzzzz",part = "zzz") == "z"
    assert candidate(s = "abcdefgabcdefgabcdefg",part = "efgabc") == "abcdddefg"
    assert candidate(s = "ababababab",part = "abab") == "ab"
    assert candidate(s = "xxxxxxxxxxxxxxxxxxxx",part = "xxx") == "xx"
    assert candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",part = "micro") == "pneumonoultrascopicsilicovolcanoconiosis"
    assert candidate(s = "abcdefgabcdefg",part = "def") == "abcgabcg"
    assert candidate(s = "aabbccddeeaabbccddeeaabbccddeeaabbccdd",part = "abcd") == "aabbccddeeaabbccddeeaabbccddeeaabbccdd"
    assert candidate(s = "abacabadabacabadabacaba",part = "abad") == "abacabacabacaba"
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",part = "erty") == "qwuiopasdfghjklzxcvbnmqwuiop"
    assert candidate(s = "abcdabcdeabcdabcdeabcd",part = "bcde") == "abcdaabcdaabcd"
    assert candidate(s = "abcdabcdabcdabcd",part = "abcd") == ""
    assert candidate(s = "ababababababababababababababababababababababababababababababababab",part = "abab") == "ab"
    assert candidate(s = "abcdabcdabcdabcd",part = "abcdabcd") == ""
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",part = "zyx") == "wvutsrqponmlkjihgfedcba"
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmqwerty",part = "erty") == "qwuiopasdfghjklzxcvbnmqw"
    assert candidate(s = "noonnoonnoonnoon",part = "noon") == ""
    assert candidate(s = "oneonetwoonethreeonefouronefiveonesixone",part = "oneone") == "twoonethreeonefouronefiveonesixone"
    assert candidate(s = "12345678901234567890",part = "345") == "12678901267890"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",part = "def") == "abcghijklmnopqrstuvwxyz"
    assert candidate(s = "thisisaverylongstringwithrepeatedpatterns",part = "pattern") == "thisisaverylongstringwithrepeateds"
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",part = "mnop") == "qwertyuiopasdfghjklzxcvbnm"
    assert candidate(s = "abcdefghijabcdefghij",part = "cdefg") == "abhijabhij"
    assert candidate(s = "aaaaaaaaaaaabbbbbaaaaaaaaaaabbbbbaaaaaaaaaaabbbbbaaaaaaaaaaabbbbb",part = "aaaabbbb") == "aaaaaaaabaaaaaaabaaaaaaabaaaaaaab"
    assert candidate(s = "abcdefghabcdefghabcdefgh",part = "efgh") == "abcdabcdabcd"
    assert candidate(s = "thisisaverylongstringwithrepeatedpattern",part = "pattern") == "thisisaverylongstringwithrepeated"
    assert candidate(s = "abababababababab",part = "abab") == ""
    assert candidate(s = "abcdeabcdeabcdeabcde",part = "abcde") == ""
    assert candidate(s = "abababababababababab",part = "ababa") == "bbbab"
    assert candidate(s = "abcdeabcdeabcde",part = "bcde") == "aaa"
    assert candidate(s = "abcdefghij",part = "gh") == "abcdefij"
    assert candidate(s = "aabbccddeeff",part = "abc") == "aabbccddeeff"
    assert candidate(s = "xyxxyxyxyx",part = "xyx") == "y"
    assert candidate(s = "aaaaaa",part = "aa") == ""
    assert candidate(s = "abcdefabcdef",part = "defabc") == "abcdef"
    assert candidate(s = "zzzzzzzz",part = "zz") == ""
    assert candidate(s = "bananaanananasanananananana",part = "ana") == "bnnasnnna"
    assert candidate(s = "abcabcabcabcabcabc",part = "abcabc") == ""
    assert candidate(s = "aaaaaa",part = "a") == ""
    assert candidate(s = "abcdefghij",part = "efg") == "abcdhij"
    assert candidate(s = "onetwothreefourfivesixseveneightnineseven",part = "seven") == "onetwothreefourfivesixeightnine"
    assert candidate(s = "abcabcabcabcabcabc",part = "ab") == "cccccc"
    assert candidate(s = "mississippi",part = "iss") == "mippi"
    assert candidate(s = "aaaabbbbcccc",part = "bbcc") == "aaaa"
    assert candidate(s = "abracadabraabracadabra",part = "bracad") == "aabraaabra"
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",part = "abcdabcd") == ""
    assert candidate(s = "abababababababab",part = "aba") == "bbbb"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",part = "zzzz") == "zz"
    assert candidate(s = "xyzxyzxyzxyzxyzxyz",part = "xyzxyz") == ""
    assert candidate(s = "aaaaaaaaaa",part = "aaa") == "a"
    assert candidate(s = "repeatedrepeatedrepeatedrepeated",part = "repeated") == ""
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzz",part = "zzzz") == "zz"
    assert candidate(s = "repeatedsubstringrepeatedsubstring",part = "ted") == "repeasubstringrepeasubstring"
    assert candidate(s = "abcdefghijkabcdefghijkabcdefghijk",part = "efg") == "abcdhijkabcdhijkabcdhijk"
    assert candidate(s = "mnopqrsmnopqrsmnopqrs",part = "mnopqrs") == ""
    assert candidate(s = "ananasanananas",part = "ana") == "nasns"
    assert candidate(s = "zzzzz",part = "zz") == "z"
    assert candidate(s = "thisisaverylongstringwithrepeatedparts",part = "thisis") == "averylongstringwithrepeatedparts"


