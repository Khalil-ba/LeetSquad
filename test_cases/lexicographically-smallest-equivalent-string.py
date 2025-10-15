def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s1 = "abc",s2 = "bcd",baseStr = "xyz") == "xyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc",s2 = "bcd",baseStr = "xyz") == "xyz": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "leetcode",s2 = "programs",baseStr = "sourcecode") == "aauaaaaada"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "leetcode",s2 = "programs",baseStr = "sourcecode") == "aauaaaaada": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "parker",s2 = "morris",baseStr = "parser") == "makkek"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "parker",s2 = "morris",baseStr = "parser") == "makkek": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abc",s2 = "bcd",baseStr = "zab") == "zaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc",s2 = "bcd",baseStr = "zab") == "zaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abc",s2 = "bcd",baseStr = "ace") == "aae"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc",s2 = "bcd",baseStr = "ace") == "aae": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a",s2 = "b",baseStr = "z") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a",s2 = "b",baseStr = "z") == "z": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaa",s2 = "bbb",baseStr = "ccc") == "ccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaa",s2 = "bbb",baseStr = "ccc") == "ccc": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a",s2 = "z",baseStr = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxya"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a",s2 = "z",baseStr = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxya": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "world",baseStr = "hold") == "hdld"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "world",baseStr = "hold") == "hdld": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abc",s2 = "cde",baseStr = "eed") == "aab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc",s2 = "cde",baseStr = "eed") == "aab": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "abcdefghij",baseStr = "abcdefghij") == "abcdefghij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "abcdefghij",baseStr = "abcdefghij") == "abcdefghij": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbaabbccdd",s2 = "bbaaddeeccff",baseStr = "aabbaabbccdd") == "aaaaaaaaccaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbaabbccdd",s2 = "bbaaddeeccff",baseStr = "aabbaabbccdd") == "aaaaaaaaccaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mnopqrstuvwxyzabcdefghijkl",s2 = "pqrstuvwxyzabcdefghijklmno",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mnopqrstuvwxyzabcdefghijkl",s2 = "pqrstuvwxyzabcdefghijklmno",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacaba",s2 = "zbzbzbz",baseStr = "zzzabzz") == "aaaabaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacaba",s2 = "zbzbzbz",baseStr = "zzzabzz") == "aaaabaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "fedcba",baseStr = "abcdef") == "abccba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "fedcba",baseStr = "abcdef") == "abccba": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadabacaba",s2 = "zzzzzzzzzzzzzzz",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaefghijklmnopqrstuvwxya"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadabacaba",s2 = "zzzzzzzzzzzzzzz",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaefghijklmnopqrstuvwxya": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "qqqqqqqqqq",s2 = "wwwwwwwwww",baseStr = "quicksort") == "quicksort"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "qqqqqqqqqq",s2 = "wwwwwwwwww",baseStr = "quicksort") == "quicksort": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "qwertyuiop",s2 = "asdfghjklz",baseStr = "qwertyuiopasdfghjklz") == "asdfghjilpasdfghjilp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "qwertyuiop",s2 = "asdfghjklz",baseStr = "qwertyuiopasdfghjklz") == "asdfghjilpasdfghjilp": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzaaayyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa",baseStr = "thequickbrownfoxjumpsoverthelazydog") == "ihelhiakaknfnfnejhmmjngekihelaaddng"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzaaayyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa",baseStr = "thequickbrownfoxjumpsoverthelazydog") == "ihelhiakaknfnfnejhmmjngekihelaaddng": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mnopqr",s2 = "nopqrs",baseStr = "mnopqrstuvwxyz") == "mmmmmmmtuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mnopqr",s2 = "nopqrs",baseStr = "mnopqrstuvwxyz") == "mmmmmmmtuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzzz",s2 = "zzzzzz",baseStr = "zzzzzz") == "zzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzzz",s2 = "zzzzzz",baseStr = "zzzzzz") == "zzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "hgfedcba",baseStr = "abcdefgh") == "abcddcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "hgfedcba",baseStr = "abcdefgh") == "abcddcba": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadaba",s2 = "xyzxyzxyzxy",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaefghijklmnopqrstuvwaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadaba",s2 = "xyzxyzxyzxy",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaefghijklmnopqrstuvwaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zyxwvutsrqponmlkjihgfedcba",s2 = "abcdefghijklmnopqrstuvwxyz",baseStr = "basestring") == "bahehgiimg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zyxwvutsrqponmlkjihgfedcba",s2 = "abcdefghijklmnopqrstuvwxyz",baseStr = "basestring") == "bahehgiimg": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ab",s2 = "ba",baseStr = "abcd") == "aacd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ab",s2 = "ba",baseStr = "abcd") == "aacd": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabad",s2 = "pqprpqps",baseStr = "zabcde") == "zabcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabad",s2 = "pqprpqps",baseStr = "zabcde") == "zabcde": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "gfedcba",baseStr = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihabcdcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "gfedcba",baseStr = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihabcdcba": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabc",s2 = "defdefdef",baseStr = "abcdefg") == "abcabcg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabc",s2 = "defdefdef",baseStr = "abcdefg") == "abcabcg": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefabcdefabcdef",s2 = "fedcbafedcbafedcbafedcbafedcba",baseStr = "thisisaverycomplexexample") == "thisisavbrycomplbxbxamplb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefabcdefabcdef",s2 = "fedcbafedcbafedcbafedcbafedcba",baseStr = "thisisaverycomplexexample") == "thisisavbrycomplbxbxamplb": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mnopqr",s2 = "nopqrm",baseStr = "mnopqrstuvwxyz") == "mmmmmmstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mnopqr",s2 = "nopqrm",baseStr = "mnopqrstuvwxyz") == "mmmmmmstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzzxyzz",s2 = "zzxxyyzz",baseStr = "zzzzyyyyxxxxyyyy") == "xxxxxxxxxxxxxxxx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzzxyzz",s2 = "zzxxyyzz",baseStr = "zzzzyyyyxxxxyyyy") == "xxxxxxxxxxxxxxxx": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaabbbbbccccc",s2 = "bbbbbcccccddddd",baseStr = "fedcba") == "feaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaabbbbbccccc",s2 = "bbbbbcccccddddd",baseStr = "fedcba") == "feaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabc",s2 = "cbacbacba",baseStr = "abcdefghi") == "abadefghi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabc",s2 = "cbacbacba",baseStr = "abcdefghi") == "abadefghi": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzaaayyxxwwvvuuttsrrqqppoonnmlkkjjiihhggffeeddccbbaa",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzaaayyxxwwvvuuttsrrqqppoonnmlkkjjiihhggffeeddccbbaa",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzzzzzzz",s2 = "aaaaaaaaaa",baseStr = "zzzzzzzzzz") == "aaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzzzzzzz",s2 = "aaaaaaaaaa",baseStr = "zzzzzzzzzz") == "aaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",s2 = "cbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacb",baseStr = "abcdefghijklmnopqrstuvwxyz") == "abadefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",s2 = "cbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacb",baseStr = "abcdefghijklmnopqrstuvwxyz") == "abadefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "bbccdd",baseStr = "abcabc") == "aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "bbccdd",baseStr = "abcabc") == "aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabad",s2 = "bcbcbcbc",baseStr = "zzzzzzzz") == "zzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabad",s2 = "bcbcbcbc",baseStr = "zzzzzzzz") == "zzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "bbaaccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyza",baseStr = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == "aacdefghijklmnopqrstuvwxyaaacdefghijklmnopqrstuvwxya"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "bbaaccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyza",baseStr = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == "aacdefghijklmnopqrstuvwxyaaacdefghijklmnopqrstuvwxya": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaabbbbbccccc",s2 = "zzzzzyyyyyxxxxx",baseStr = "azbycxdwevfugthsiqjronmpkl") == "aabbccdwevfugthsiqjronmpkl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaabbbbbccccc",s2 = "zzzzzyyyyyxxxxx",baseStr = "azbycxdwevfugthsiqjronmpkl") == "aabbccdwevfugthsiqjronmpkl": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaabbbcccddd",s2 = "bbbaaaccdddbbb",baseStr = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "aaaaaaaaeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaabbbcccddd",s2 = "bbbaaaccdddbbb",baseStr = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "aaaaaaaaeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abababababababab",s2 = "babababababababa",baseStr = "abababababababab") == "aaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abababababababab",s2 = "babababababababa",baseStr = "abababababababab") == "aaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcde",s2 = "vwxyz",baseStr = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcde",s2 = "vwxyz",baseStr = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "acaeac",s2 = "cdcdcd",baseStr = "acaeacdcd") == "aaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "acaeac",s2 = "cdcdcd",baseStr = "acaeacdcd") == "aaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "qponmlkjihgfedcba") == "jklmmlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "qponmlkjihgfedcba") == "jklmmlkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "zyxwvutsrqponmlkjihgfedcba") == "abcdefghijklmmlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "zyxwvutsrqponmlkjihgfedcba") == "abcdefghijklmmlkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mnopqr",s2 = "qrstuv",baseStr = "mnopqrqqqqqq") == "mnopmnmmmmmm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mnopqr",s2 = "qrstuv",baseStr = "mnopqrqqqqqq") == "mnopmnmmmmmm": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdeabcde",s2 = "fghijfghij",baseStr = "abcdefghij") == "abcdeabcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdeabcde",s2 = "fghijfghij",baseStr = "abcdefghij") == "abcdeabcde": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "abcdefghijklmnopqrstuvwxyz",baseStr = "thequickbrownfoxjumpsoverthelazydog") == "thequickbrownfoxjumpsoverthelazydog"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "abcdefghijklmnopqrstuvwxyz",baseStr = "thequickbrownfoxjumpsoverthelazydog") == "thequickbrownfoxjumpsoverthelazydog": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "smallestequivalentstring") == "hmallehgejfiealemghgiimg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "smallestequivalentstring") == "hmallehgejfiealemghgiimg": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "ghijkl",baseStr = "fedcba") == "fedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "ghijkl",baseStr = "fedcba") == "fedcba": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadabacaba",s2 = "zyczyxczyxzyxczyx",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaefghijklmnopqrstuvwaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadabacaba",s2 = "zyczyxczyxzyxczyx",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaefghijklmnopqrstuvwaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzyyxxwwvv",s2 = "xxwwvvuuttss",baseStr = "zyxwvutsrqponmlkjihgfedcba") == "ssssssssrqponmlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzyyxxwwvv",s2 = "xxwwvvuuttss",baseStr = "zyxwvutsrqponmlkjihgfedcba") == "ssssssssrqponmlkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "qwertyuiop",s2 = "asdfghjklz",baseStr = "qazwsxedcrfvtgbyhnumpoi") == "aapssxddcffvggbhhnjmpli"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "qwertyuiop",s2 = "asdfghjklz",baseStr = "qazwsxedcrfvtgbyhnumpoi") == "aapssxddcffvggbhhnjmpli": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaabbbbccccddddeeeeffffgggghhhhiiii",s2 = "ddddccccbbbbaaaahhhhggggffffeeeeiiii",baseStr = "abcdefghi") == "abbaeffei"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaabbbbccccddddeeeeffffgggghhhhiiii",s2 = "ddddccccbbbbaaaahhhhggggffffeeeeiiii",baseStr = "abcdefghi") == "abbaeffei": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadabacaba",s2 = "xyzxyzxyzxyzxyz",baseStr = "zzzzzzzzzzzzzzz") == "aaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadabacaba",s2 = "xyzxyzxyzxyzxyz",baseStr = "zzzzzzzzzzzzzzz") == "aaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "hello") == "helll"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "hello") == "helll": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcdabcd",s2 = "dcbaabdcbaab",baseStr = "abcdefg") == "aaaaefg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcdabcd",s2 = "dcbaabdcbaab",baseStr = "abcdefg") == "aaaaefg": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "fedcba",baseStr = "transform") == "transaorm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "fedcba",baseStr = "transform") == "transaorm": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabcabc",s2 = "defdefdefdef",baseStr = "abcdefabcdef") == "abcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabcabc",s2 = "defdefdefdef",baseStr = "abcdefabcdef") == "abcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "bcdefghijklmnopqrstuvwxyza",baseStr = "zyxwvutsrqponmlkjihgfedcba") == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "bcdefghijklmnopqrstuvwxyza",baseStr = "zyxwvutsrqponmlkjihgfedcba") == "aaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",baseStr = "zzzyyxxwwvvuuttoossrrqqppoonnmmllkkjjiihhggffeeddccbaa") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",baseStr = "zzzyyxxwwvvuuttoossrrqqppoonnmmllkkjjiihhggffeeddccbaa") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabc",s2 = "bcdcbdbcd",baseStr = "abcbcadcb") == "aaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabc",s2 = "bcdcbdbcd",baseStr = "abcbcadcb") == "aaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmmlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmmlkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaaaabbbbbbb",s2 = "bbbbbbbaaaaaaa",baseStr = "algorithm") == "algorithm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaaaabbbbbbb",s2 = "bbbbbbbaaaaaaa",baseStr = "algorithm") == "algorithm": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "bbccdd",baseStr = "abcd") == "aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "bbccdd",baseStr = "abcd") == "aaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mammal",s2 = "walrus",baseStr = "evolve") == "evolve"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mammal",s2 = "walrus",baseStr = "evolve") == "evolve": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaa",s2 = "bbbbb",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aacdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaa",s2 = "bbbbb",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aacdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "pqrstu",s2 = "vwxyzq",baseStr = "python") == "psthon"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "pqrstu",s2 = "vwxyzq",baseStr = "python") == "psthon": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "pqrs",s2 = "qrst",baseStr = "pqrstuvxyzpqrs") == "pppppuvxyzpppp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "pqrs",s2 = "qrst",baseStr = "pqrstuvxyzpqrs") == "pppppuvxyzpppp": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "hgfedcba",baseStr = "abcdefghihgfedcba") == "abcddcbaiabcddcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "hgfedcba",baseStr = "abcdefghihgfedcba") == "abcddcbaiabcddcba": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "pqrstu",s2 = "stuvwp",baseStr = "ppqrstuvwp") == "ppqppqppqp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "pqrstu",s2 = "stuvwp",baseStr = "ppqrstuvwp") == "ppqppqppqp": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "bbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaa",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "bbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaa",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "fghijk",baseStr = "jklmnopqrstuvwxzyz") == "ealmnopqrstuvwxzyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "fghijk",baseStr = "jklmnopqrstuvwxzyz") == "ealmnopqrstuvwxzyz": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "fedcba",baseStr = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgabccba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "fedcba",baseStr = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgabccba": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaaaa",s2 = "bbbbbbb",baseStr = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "aaaaccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaaaa",s2 = "bbbbbbb",baseStr = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "aaaaccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "language") == "lamgfage"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "language") == "lamgfage": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "eqdf",s2 = "wtqu",baseStr = "eqdf") == "eddf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "eqdf",s2 = "wtqu",baseStr = "eqdf") == "eddf": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "bcdefghijklmnopqrstuvwxyza",baseStr = "thequickbrownfoxjumpsoverthelazydog") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "bcdefghijklmnopqrstuvwxyza",baseStr = "thequickbrownfoxjumpsoverthelazydog") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxzyz",s2 = "zyzxzy",baseStr = "xyzzyx") == "xxxxxx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxzyz",s2 = "zyzxzy",baseStr = "xyzzyx") == "xxxxxx": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "thequickbrownfoxjumpsoverthelazydog") == "ghejfickbildmflcjfmkhleeighelaabdlg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "thequickbrownfoxjumpsoverthelazydog") == "ghejfickbildmflcjfmkhleeighelaabdlg": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ababababab",s2 = "bababababa",baseStr = "ababababab") == "aaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ababababab",s2 = "bababababa",baseStr = "ababababab") == "aaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "bcadefghijklmnopqrstuvwxzy",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaadefghijklmnopqrstuvwxyy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "bcadefghijklmnopqrstuvwxzy",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaadefghijklmnopqrstuvwxyy": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "equivalent",s2 = "characters",baseStr = "example") == "axampla"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "equivalent",s2 = "characters",baseStr = "example") == "axampla": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ababababab",s2 = "bcbcbcbcbc",baseStr = "abacabadab") == "aaaaaaadaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ababababab",s2 = "bcbcbcbcbc",baseStr = "abacabadab") == "aaaaaaadaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaabbbcccdddeeefffggghhhiiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxxyyyyzzzz",s2 = "zzzzyyyyxxxxyyyyvvvvwwwxxxxyyyyuuuvvvwwxxyyyytttsssrqqqpppoonnmmlkkkjjjiiiigggfffeeedddcccbbbaaa",baseStr = "thequickbrownfoxjumpsoverthelazydog") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaabbbcccdddeeefffggghhhiiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxxyyyyzzzz",s2 = "zzzzyyyyxxxxyyyyvvvvwwwxxxxyyyyuuuvvvwwxxyyyytttsssrqqqpppoonnmmlkkkjjjiiiigggfffeeedddcccbbbaaa",baseStr = "thequickbrownfoxjumpsoverthelazydog") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadabacaba",s2 = "zxyzxyzxyzxyzxy",baseStr = "abacabadabacaba") == "aaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadabacaba",s2 = "zxyzxyzxyzxyzxy",baseStr = "abacabadabacaba") == "aaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcdabcdabcd",s2 = "dcbaecbaecbaecba",baseStr = "abcdefghijk") == "abbaafghijk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcdabcdabcd",s2 = "dcbaecbaecbaecba",baseStr = "abcdefghijk") == "abbaafghijk": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "leet",s2 = "code",baseStr = "leetcode") == "cdddcddd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "leet",s2 = "code",baseStr = "leetcode") == "cdddcddd": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "bcdefghijklmnopqrstuvwxyza",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "bcdefghijklmnopqrstuvwxyza",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgabcdefgabcdefg",s2 = "hijklmnopqrstuahijklmnopqrstuahijklmnopqrstuahijklmnopqrstuahijklmnopqrstu",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaaaaaaaaaaaaaaaaaavwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgabcdefgabcdefg",s2 = "hijklmnopqrstuahijklmnopqrstuahijklmnopqrstuahijklmnopqrstuahijklmnopqrstu",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaaaaaaaaaaaaaaaaaavwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "ghijklm",baseStr = "abcdefg") == "abcdefa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "ghijklm",baseStr = "abcdefg") == "abcdefa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "qwertyuiopasdfghjklzxcvbnm",s2 = "mlkjihgfedcbazyxwvutsrqpon",baseStr = "zyxwvutsrqponmlkjihgfedcba") == "faaaeafaaeaeeeaeafaafeaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "qwertyuiopasdfghjklzxcvbnm",s2 = "mlkjihgfedcbazyxwvutsrqpon",baseStr = "zyxwvutsrqponmlkjihgfedcba") == "faaaeafaaeaeeeaeafaafeaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabcabc",s2 = "defdefdefdef",baseStr = "complexity") == "complbxity"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabcabc",s2 = "defdefdefdef",baseStr = "complexity") == "complbxity": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "bcdefghijklmnopqrstuvwxyza",baseStr = "thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydog") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "bcdefghijklmnopqrstuvwxyza",baseStr = "thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydog") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "acbacbacbacb",s2 = "zyxzyxzyxzyx",baseStr = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwbca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "acbacbacbacb",s2 = "zyxzyxzyxzyx",baseStr = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwbca": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaaa",s2 = "bbbbbb",baseStr = "ababab") == "aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaaa",s2 = "bbbbbb",baseStr = "ababab") == "aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzzzz",s2 = "zzzzzz",baseStr = "xyzzyx") == "xxxxxx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzzzz",s2 = "zzzzzz",baseStr = "xyzzyx") == "xxxxxx": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s1 = "abc",s2 = "bcd",baseStr = "xyz") == "xyz"
    assert candidate(s1 = "leetcode",s2 = "programs",baseStr = "sourcecode") == "aauaaaaada"
    assert candidate(s1 = "parker",s2 = "morris",baseStr = "parser") == "makkek"
    assert candidate(s1 = "abc",s2 = "bcd",baseStr = "zab") == "zaa"
    assert candidate(s1 = "abc",s2 = "bcd",baseStr = "ace") == "aae"
    assert candidate(s1 = "a",s2 = "b",baseStr = "z") == "z"
    assert candidate(s1 = "aaa",s2 = "bbb",baseStr = "ccc") == "ccc"
    assert candidate(s1 = "a",s2 = "z",baseStr = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxya"
    assert candidate(s1 = "hello",s2 = "world",baseStr = "hold") == "hdld"
    assert candidate(s1 = "abc",s2 = "cde",baseStr = "eed") == "aab"
    assert candidate(s1 = "abcdefghij",s2 = "abcdefghij",baseStr = "abcdefghij") == "abcdefghij"
    assert candidate(s1 = "aabbaabbccdd",s2 = "bbaaddeeccff",baseStr = "aabbaabbccdd") == "aaaaaaaaccaa"
    assert candidate(s1 = "mnopqrstuvwxyzabcdefghijkl",s2 = "pqrstuvwxyzabcdefghijklmno",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s1 = "abacaba",s2 = "zbzbzbz",baseStr = "zzzabzz") == "aaaabaa"
    assert candidate(s1 = "abcdef",s2 = "fedcba",baseStr = "abcdef") == "abccba"
    assert candidate(s1 = "abacabadabacaba",s2 = "zzzzzzzzzzzzzzz",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaefghijklmnopqrstuvwxya"
    assert candidate(s1 = "qqqqqqqqqq",s2 = "wwwwwwwwww",baseStr = "quicksort") == "quicksort"
    assert candidate(s1 = "qwertyuiop",s2 = "asdfghjklz",baseStr = "qwertyuiopasdfghjklz") == "asdfghjilpasdfghjilp"
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzaaayyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa",baseStr = "thequickbrownfoxjumpsoverthelazydog") == "ihelhiakaknfnfnejhmmjngekihelaaddng"
    assert candidate(s1 = "mnopqr",s2 = "nopqrs",baseStr = "mnopqrstuvwxyz") == "mmmmmmmtuvwxyz"
    assert candidate(s1 = "zzzzzz",s2 = "zzzzzz",baseStr = "zzzzzz") == "zzzzzz"
    assert candidate(s1 = "abcdefgh",s2 = "hgfedcba",baseStr = "abcdefgh") == "abcddcba"
    assert candidate(s1 = "abacabadaba",s2 = "xyzxyzxyzxy",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaefghijklmnopqrstuvwaaa"
    assert candidate(s1 = "zyxwvutsrqponmlkjihgfedcba",s2 = "abcdefghijklmnopqrstuvwxyz",baseStr = "basestring") == "bahehgiimg"
    assert candidate(s1 = "ab",s2 = "ba",baseStr = "abcd") == "aacd"
    assert candidate(s1 = "abacabad",s2 = "pqprpqps",baseStr = "zabcde") == "zabcde"
    assert candidate(s1 = "abcdefg",s2 = "gfedcba",baseStr = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihabcdcba"
    assert candidate(s1 = "abcabcabc",s2 = "defdefdef",baseStr = "abcdefg") == "abcabcg"
    assert candidate(s1 = "abcdefabcdefabcdef",s2 = "fedcbafedcbafedcbafedcbafedcba",baseStr = "thisisaverycomplexexample") == "thisisavbrycomplbxbxamplb"
    assert candidate(s1 = "mnopqr",s2 = "nopqrm",baseStr = "mnopqrstuvwxyz") == "mmmmmmstuvwxyz"
    assert candidate(s1 = "xyzzxyzz",s2 = "zzxxyyzz",baseStr = "zzzzyyyyxxxxyyyy") == "xxxxxxxxxxxxxxxx"
    assert candidate(s1 = "aaaaabbbbbccccc",s2 = "bbbbbcccccddddd",baseStr = "fedcba") == "feaaaa"
    assert candidate(s1 = "abcabcabc",s2 = "cbacbacba",baseStr = "abcdefghi") == "abadefghi"
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "zzzaaayyxxwwvvuuttsrrqqppoonnmlkkjjiihhggffeeddccbbaa",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s1 = "zzzzzzzzzz",s2 = "aaaaaaaaaa",baseStr = "zzzzzzzzzz") == "aaaaaaaaaa"
    assert candidate(s1 = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",s2 = "cbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacb",baseStr = "abcdefghijklmnopqrstuvwxyz") == "abadefghijklmnopqrstuvwxyz"
    assert candidate(s1 = "aabbcc",s2 = "bbccdd",baseStr = "abcabc") == "aaaaaa"
    assert candidate(s1 = "abacabad",s2 = "bcbcbcbc",baseStr = "zzzzzzzz") == "zzzzzzzz"
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "bbaaccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyza",baseStr = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == "aacdefghijklmnopqrstuvwxyaaacdefghijklmnopqrstuvwxya"
    assert candidate(s1 = "aaaaabbbbbccccc",s2 = "zzzzzyyyyyxxxxx",baseStr = "azbycxdwevfugthsiqjronmpkl") == "aabbccdwevfugthsiqjronmpkl"
    assert candidate(s1 = "aaabbbcccddd",s2 = "bbbaaaccdddbbb",baseStr = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "aaaaaaaaeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
    assert candidate(s1 = "abababababababab",s2 = "babababababababa",baseStr = "abababababababab") == "aaaaaaaaaaaaaaaa"
    assert candidate(s1 = "abcde",s2 = "vwxyz",baseStr = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
    assert candidate(s1 = "acaeac",s2 = "cdcdcd",baseStr = "acaeacdcd") == "aaaaaaaaa"
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "qponmlkjihgfedcba") == "jklmmlkjihgfedcba"
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "zyxwvutsrqponmlkjihgfedcba") == "abcdefghijklmmlkjihgfedcba"
    assert candidate(s1 = "mnopqr",s2 = "qrstuv",baseStr = "mnopqrqqqqqq") == "mnopmnmmmmmm"
    assert candidate(s1 = "abcdeabcde",s2 = "fghijfghij",baseStr = "abcdefghij") == "abcdeabcde"
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "abcdefghijklmnopqrstuvwxyz",baseStr = "thequickbrownfoxjumpsoverthelazydog") == "thequickbrownfoxjumpsoverthelazydog"
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "smallestequivalentstring") == "hmallehgejfiealemghgiimg"
    assert candidate(s1 = "abcdef",s2 = "ghijkl",baseStr = "fedcba") == "fedcba"
    assert candidate(s1 = "abacabadabacaba",s2 = "zyczyxczyxzyxczyx",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaefghijklmnopqrstuvwaaa"
    assert candidate(s1 = "zzzyyxxwwvv",s2 = "xxwwvvuuttss",baseStr = "zyxwvutsrqponmlkjihgfedcba") == "ssssssssrqponmlkjihgfedcba"
    assert candidate(s1 = "qwertyuiop",s2 = "asdfghjklz",baseStr = "qazwsxedcrfvtgbyhnumpoi") == "aapssxddcffvggbhhnjmpli"
    assert candidate(s1 = "aaaabbbbccccddddeeeeffffgggghhhhiiii",s2 = "ddddccccbbbbaaaahhhhggggffffeeeeiiii",baseStr = "abcdefghi") == "abbaeffei"
    assert candidate(s1 = "abacabadabacaba",s2 = "xyzxyzxyzxyzxyz",baseStr = "zzzzzzzzzzzzzzz") == "aaaaaaaaaaaaaaa"
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "hello") == "helll"
    assert candidate(s1 = "abcdabcdabcd",s2 = "dcbaabdcbaab",baseStr = "abcdefg") == "aaaaefg"
    assert candidate(s1 = "abcdef",s2 = "fedcba",baseStr = "transform") == "transaorm"
    assert candidate(s1 = "abcabcabcabc",s2 = "defdefdefdef",baseStr = "abcdefabcdef") == "abcabcabcabc"
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "bcdefghijklmnopqrstuvwxyza",baseStr = "zyxwvutsrqponmlkjihgfedcba") == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",baseStr = "zzzyyxxwwvvuuttoossrrqqppoonnmmllkkjjiihhggffeeddccbaa") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s1 = "abcabcabc",s2 = "bcdcbdbcd",baseStr = "abcbcadcb") == "aaaaaaaaa"
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmmlkjihgfedcba"
    assert candidate(s1 = "aaaaaaabbbbbbb",s2 = "bbbbbbbaaaaaaa",baseStr = "algorithm") == "algorithm"
    assert candidate(s1 = "aabbcc",s2 = "bbccdd",baseStr = "abcd") == "aaaa"
    assert candidate(s1 = "mammal",s2 = "walrus",baseStr = "evolve") == "evolve"
    assert candidate(s1 = "aaaaa",s2 = "bbbbb",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aacdefghijklmnopqrstuvwxyz"
    assert candidate(s1 = "pqrstu",s2 = "vwxyzq",baseStr = "python") == "psthon"
    assert candidate(s1 = "pqrs",s2 = "qrst",baseStr = "pqrstuvxyzpqrs") == "pppppuvxyzpppp"
    assert candidate(s1 = "abcdefgh",s2 = "hgfedcba",baseStr = "abcdefghihgfedcba") == "abcddcbaiabcddcba"
    assert candidate(s1 = "pqrstu",s2 = "stuvwp",baseStr = "ppqrstuvwp") == "ppqppqppqp"
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",s2 = "bbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaa",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s1 = "abcdef",s2 = "fghijk",baseStr = "jklmnopqrstuvwxzyz") == "ealmnopqrstuvwxzyz"
    assert candidate(s1 = "abcdef",s2 = "fedcba",baseStr = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgabccba"
    assert candidate(s1 = "aaaaaaa",s2 = "bbbbbbb",baseStr = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "aaaaccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "language") == "lamgfage"
    assert candidate(s1 = "eqdf",s2 = "wtqu",baseStr = "eqdf") == "eddf"
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "bcdefghijklmnopqrstuvwxyza",baseStr = "thequickbrownfoxjumpsoverthelazydog") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s1 = "xyxzyz",s2 = "zyzxzy",baseStr = "xyzzyx") == "xxxxxx"
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "zyxwvutsrqponmlkjihgfedcba",baseStr = "thequickbrownfoxjumpsoverthelazydog") == "ghejfickbildmflcjfmkhleeighelaabdlg"
    assert candidate(s1 = "ababababab",s2 = "bababababa",baseStr = "ababababab") == "aaaaaaaaaa"
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "bcadefghijklmnopqrstuvwxzy",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaadefghijklmnopqrstuvwxyy"
    assert candidate(s1 = "equivalent",s2 = "characters",baseStr = "example") == "axampla"
    assert candidate(s1 = "ababababab",s2 = "bcbcbcbcbc",baseStr = "abacabadab") == "aaaaaaadaa"
    assert candidate(s1 = "aaabbbcccdddeeefffggghhhiiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxxyyyyzzzz",s2 = "zzzzyyyyxxxxyyyyvvvvwwwxxxxyyyyuuuvvvwwxxyyyytttsssrqqqpppoonnmmlkkkjjjiiiigggfffeeedddcccbbbaaa",baseStr = "thequickbrownfoxjumpsoverthelazydog") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s1 = "abacabadabacaba",s2 = "zxyzxyzxyzxyzxy",baseStr = "abacabadabacaba") == "aaaaaaaaaaaaaaa"
    assert candidate(s1 = "abcdabcdabcdabcd",s2 = "dcbaecbaecbaecba",baseStr = "abcdefghijk") == "abbaafghijk"
    assert candidate(s1 = "leet",s2 = "code",baseStr = "leetcode") == "cdddcddd"
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "bcdefghijklmnopqrstuvwxyza",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s1 = "abcdefgabcdefgabcdefg",s2 = "hijklmnopqrstuahijklmnopqrstuahijklmnopqrstuahijklmnopqrstuahijklmnopqrstu",baseStr = "abcdefghijklmnopqrstuvwxyz") == "aaaaaaaaaaaaaaaaaaaaavwxyz"
    assert candidate(s1 = "abcdefg",s2 = "ghijklm",baseStr = "abcdefg") == "abcdefa"
    assert candidate(s1 = "qwertyuiopasdfghjklzxcvbnm",s2 = "mlkjihgfedcbazyxwvutsrqpon",baseStr = "zyxwvutsrqponmlkjihgfedcba") == "faaaeafaaeaeeeaeafaafeaaaa"
    assert candidate(s1 = "abcabcabcabc",s2 = "defdefdefdef",baseStr = "complexity") == "complbxity"
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "bcdefghijklmnopqrstuvwxyza",baseStr = "thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydog") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s1 = "acbacbacbacb",s2 = "zyxzyxzyxzyx",baseStr = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwbca"
    assert candidate(s1 = "aaaaaa",s2 = "bbbbbb",baseStr = "ababab") == "aaaaaa"
    assert candidate(s1 = "xyzzzz",s2 = "zzzzzz",baseStr = "xyzzyx") == "xxxxxx"


