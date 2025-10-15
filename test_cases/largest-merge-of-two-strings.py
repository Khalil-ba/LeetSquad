def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word1 = "lexicographically",word2 = "largestmerge") == "llexicogrargestmergeaphically"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "lexicographically",word2 = "largestmerge") == "llexicogrargestmergeaphically": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zyxw",word2 = "abcd") == "zyxwabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zyxw",word2 = "abcd") == "zyxwabcd": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcd",word2 = "zyxwzyxw") == "zyxwzyxwabcdabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcd",word2 = "zyxwzyxw") == "zyxwzyxwabcdabcd": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "leetcode",word2 = "challenge") == "leetcodechallenge"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "leetcode",word2 = "challenge") == "leetcodechallenge": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaab",word2 = "aaabb") == "aaabbaaaab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaab",word2 = "aaabb") == "aaabbaaaab": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "lexicographic",word2 = "merge") == "mlexiergecographic"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "lexicographic",word2 = "merge") == "mlexiergecographic": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaa",word2 = "bbbb") == "bbbbaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaa",word2 = "bbbb") == "bbbbaaaa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabc",word2 = "abdcaba") == "abdcabcabcaba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabc",word2 = "abdcaba") == "abdcabcabcaba": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abc",word2 = "defghijklmnopqrstuvwxyz") == "defghijklmnopqrstuvwxyzabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abc",word2 = "defghijklmnopqrstuvwxyz") == "defghijklmnopqrstuvwxyzabc": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "z",word2 = "z") == "zz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "z",word2 = "z") == "zz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "hello",word2 = "world") == "worlhellod"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "hello",word2 = "world") == "worlhellod": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "zyxw") == "zyxwabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "zyxw") == "zyxwabcd": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "leetcode",word2 = "etco") == "leteetcodeco"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "leetcode",word2 = "etco") == "leteetcodeco": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xy",word2 = "xy") == "xyxy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xy",word2 = "xy") == "xyxy": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "cabaa",word2 = "bcaaa") == "cbcabaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "cabaa",word2 = "bcaaa") == "cbcabaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcc",word2 = "bbccdd") == "bbccddaabbcc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcc",word2 = "bbccdd") == "bbccddaabbcc": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzz",word2 = "zzz") == "zzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzz",word2 = "zzz") == "zzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "a",word2 = "b") == "ba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "a",word2 = "b") == "ba": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaa",word2 = "bbbbb") == "bbbbbaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaa",word2 = "bbbbb") == "bbbbbaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcc",word2 = "abcabc") == "abcabcaabbcc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcc",word2 = "abcabc") == "abcabcaabbcc": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyz",word2 = "xyz") == "xyzxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyz",word2 = "xyz") == "xyzxyz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "efgh") == "efghabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "efgh") == "efghabcd": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "dcba") == "dcbabcda"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "dcba") == "dcbabcda": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "same",word2 = "same") == "ssameame"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "same",word2 = "same") == "ssameame": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcd",word2 = "abcde") == "abcdeabcdabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcd",word2 = "abcde") == "abcdeabcdabcd": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "bca",word2 = "cab") == "cbcaba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "bca",word2 = "cab") == "cbcaba": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgfedcbabcdefghijklmnopqrstuvwxyza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgfedcbabcdefghijklmnopqrstuvwxyza": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "missouri") == "mmissourississippii"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "missouri") == "mmissourississippii": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzzzzz",word2 = "zzzzzzzz") == "zzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzzzzz",word2 = "zzzzzzzz") == "zzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "complexity",word2 = "similarity") == "similcomplexityarity"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "complexity",word2 = "similarity") == "similcomplexityarity": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzzzzzzzzzzzzzzzz",word2 = "xyzzzzzzzzzzzzzz") == "xyzzzzzzzzzzzzzzzzxyzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzzzzzzzzzzzzzzzz",word2 = "xyzzzzzzzzzzzzzz") == "xyzzzzzzzzzzzzzzzzxyzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaabbbbccccdddd",word2 = "aaaabbbbccccdddd") == "aaaabbbbccccddddaaaabbbbccccdddd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaabbbbccccdddd",word2 = "aaaabbbbccccdddd") == "aaaabbbbccccddddaaaabbbbccccdddd": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzzzz",word2 = "zzzzzzzz") == "zzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzzzz",word2 = "zzzzzzzz") == "zzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaaa",word2 = "bbbbbbb") == "bbbbbbbaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaaa",word2 = "bbbbbbb") == "bbbbbbbaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzz",word2 = "zzzz") == "zzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzz",word2 = "zzzz") == "zzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzzyyxxwwvvuuttssrrqqponmlkjihgfedcbbaa") == "zzzyyxxwwvvuuttssrrqqponmlkjihgfedcbbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzzyyxxwwvvuuttssrrqqponmlkjihgfedcbbaa") == "zzzyyxxwwvvuuttssrrqqponmlkjihgfedcbbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zyxwvut",word2 = "utsrqponmlkjihgfedcba") == "zyxwvuuttsrqponmlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zyxwvut",word2 = "utsrqponmlkjihgfedcba") == "zyxwvuuttsrqponmlkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "pqrstuvwxyz",word2 = "nopqrstuvwxyz") == "pqrstuvwxyznopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "pqrstuvwxyz",word2 = "nopqrstuvwxyz") == "pqrstuvwxyznopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzzz",word2 = "zzzzzz") == "zzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzzz",word2 = "zzzzzz") == "zzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeff",word2 = "feebdccbaa") == "feebdccbaabbccddeeffaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeff",word2 = "feebdccbaa") == "feebdccbaabbccddeeffaa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "cccccccc",word2 = "dddddddd") == "ddddddddcccccccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "cccccccc",word2 = "dddddddd") == "ddddddddcccccccc": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "a",word2 = "z") == "za"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "a",word2 = "z") == "za": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcc",word2 = "aaabbb") == "aabbccaaabbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcc",word2 = "aaabbb") == "aabbccaaabbb": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdxyz",word2 = "xyzabcd") == "xyzabcdxyzabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdxyz",word2 = "xyzabcd") == "xyzabcdxyzabcd": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "python",word2 = "java") == "pytjhonava"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "python",word2 = "java") == "pytjhonava": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdabcd",word2 = "abcabcabc") == "abcdabcdabcdabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdabcd",word2 = "abcabcabc") == "abcdabcdabcdabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "sameprefix",word2 = "sameprefixsuffix") == "ssameprefixsuffixameprefix"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "sameprefix",word2 = "sameprefixsuffix") == "ssameprefixsuffixameprefix": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghij",word2 = "jihgfedcba") == "jihgfedcbabcdefghija"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghij",word2 = "jihgfedcba") == "jihgfedcbabcdefghija": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "onetwothreefour",word2 = "fivesixseveneightnine") == "onfivetwothresixseveneightnineefoure"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "onetwothreefour",word2 = "fivesixseveneightnine") == "onfivetwothresixseveneightnineefoure": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "racecar",word2 = "racecar") == "rracecaracecar"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "racecar",word2 = "racecar") == "rracecaracecar": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdabcdabcdabcdabcd",word2 = "zyxwzyxwzyxwzyxwzyxwzyxw") == "zyxwzyxwzyxwzyxwzyxwzyxwabcdabcdabcdabcdabcdabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdabcdabcdabcdabcd",word2 = "zyxwzyxwzyxwzyxwzyxwzyxw") == "zyxwzyxwzyxwzyxwzyxwzyxwabcdabcdabcdabcdabcdabcd": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyxzyzyzyx",word2 = "zyzyzyzyxz") == "zyzyzyzyxzxyxzyzyzyx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyxzyzyzyx",word2 = "zyzyzyzyxz") == "zyzyzyzyxzxyxzyzyzyx": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacabadabacaba",word2 = "xyzxyzxyzxyzxyz") == "xyzxyzxyzxyzxyzabacabadabacaba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacabadabacaba",word2 = "xyzxyzxyzxyzxyz") == "xyzxyzxyzxyzxyzabacabadabacaba": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzz",word2 = "yxzz") == "yxzzxyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzz",word2 = "yxzz") == "yxzzxyzz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdabcd",word2 = "zyxwzyxwzyxw") == "zyxwzyxwzyxwabcdabcdabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdabcd",word2 = "zyxwzyxwzyxw") == "zyxwzyxwzyxwabcdabcdabcd": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeff",word2 = "zzzzyyyxxx") == "zzzzyyyxxxaabbccddeeff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeff",word2 = "zzzzyyyxxx") == "zzzzyyyxxxaabbccddeeff": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeff",word2 = "zzyyxxwwvvuu") == "zzyyxxwwvvuuaabbccddeeff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeff",word2 = "zzyyxxwwvvuu") == "zzyyxxwwvvuuaabbccddeeff": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefg",word2 = "hijklmnop") == "hijklmnopabcdefg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefg",word2 = "hijklmnop") == "hijklmnopabcdefg": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "banana",word2 = "bandana") == "bbandanananaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "banana",word2 = "bandana") == "bbandanananaa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdabcd",word2 = "dcbaabcdabcd") == "dcbabcdabcdabcdaabcdabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdabcd",word2 = "dcbaabcdabcd") == "dcbabcdabcdabcdaabcdabcd": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abracadabra",word2 = "alakazam") == "alakazamabracadabra"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abracadabra",word2 = "alakazam") == "alakazamabracadabra": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaabbbbcccc",word2 = "bbbbaaaacccc") == "bbbbaaaaccccaaaabbbbcccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaabbbbcccc",word2 = "bbbbaaaacccc") == "bbbbaaaaccccaaaabbbbcccc": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "leetcode",word2 = "edocteel") == "leetedocteelcode"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "leetcode",word2 = "edocteel") == "leetedocteelcode": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaaaabbbbbbbbcccccccc",word2 = "ccccccccbbbbbbbbbaaaaaaa") == "ccccccccbbbbbbbbbaaaaaaaabbbbbbbbccccccccaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaaaabbbbbbbbcccccccc",word2 = "ccccccccbbbbbbbbbaaaaaaa") == "ccccccccbbbbbbbbbaaaaaaaabbbbbbbbccccccccaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdxyz",word2 = "zyxcba") == "zyxcbabcdxyza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdxyz",word2 = "zyxcba") == "zyxcbabcdxyza": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "ababababab",word2 = "bababababa") == "babababababababababa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "ababababab",word2 = "bababababa") == "babababababababababa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "equalequal",word2 = "equal") == "equequalequalal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "equalequal",word2 = "equal") == "equequalequalal": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabc",word2 = "abcabcabc") == "abcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabc",word2 = "abcabcabc") == "abcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzzzyyyy",word2 = "yyyyzzzzzz") == "zzzzzzyyyyzzzzzzyyyy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzzzyyyy",word2 = "yyyyzzzzzz") == "zzzzzzyyyyzzzzzzyyyy": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "racecar",word2 = "race") == "rracecarace"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "racecar",word2 = "race") == "rracecarace": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "programming",word2 = "challenges") == "progrchammingallenges"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "programming",word2 = "challenges") == "progrchammingallenges": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgfedcbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgfedcbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzza": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdxyz",word2 = "zyxwvut") == "zyxwvutabcdxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdxyz",word2 = "zyxwvut") == "zyxwvutabcdxyz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacaxi",word2 = "abacax") == "abacaxiabacax"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacaxi",word2 = "abacax") == "abacaxiabacax": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaabbbbb",word2 = "cccccdddddeeeee") == "cccccdddddeeeeeaaaaaabbbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaabbbbb",word2 = "cccccdddddeeeee") == "cccccdddddeeeeeaaaaaabbbbb": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefg",word2 = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgfedcbabcdefga"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefg",word2 = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgfedcbabcdefga": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "samecharacters",word2 = "samecharacters") == "ssamecharamecharactersacters"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "samecharacters",word2 = "samecharacters") == "ssamecharamecharactersacters": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abababababab",word2 = "babababababa") == "babababababababababababa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abababababab",word2 = "babababababa") == "babababababababababababa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaab",word2 = "bbbaaa") == "bbbaaaaabaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaab",word2 = "bbbaaa") == "bbbaaaaabaaa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbbccc",word2 = "aabbcc") == "aabbccaabbbccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbbccc",word2 = "aabbcc") == "aabbccaabbbccc": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzz",word2 = "zzzzzz") == "zzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzz",word2 = "zzzzzz") == "zzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "",word2 = "abc") == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "",word2 = "abc") == "abc": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijk",word2 = "abcdefghijl") == "abcdefghijlabcdefghijk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijk",word2 = "abcdefghijl") == "abcdefghijlabcdefghijk": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "nestednested",word2 = "nested") == "nnestesteednestedd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "nestednested",word2 = "nested") == "nnestesteednestedd": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",word2 = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",word2 = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcde",word2 = "edcba") == "edcbabcdea"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcde",word2 = "edcba") == "edcbabcdea": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "supercalifragilisticexpialidocious",word2 = "antidisestablishmentarianism") == "supercantidisestalifragilisticexpialidociousablishmentarianism"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "supercalifragilisticexpialidocious",word2 = "antidisestablishmentarianism") == "supercantidisestalifragilisticexpialidociousablishmentarianism": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzz",word2 = "zzxy") == "zzxyzzxy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzz",word2 = "zzxy") == "zzxyzzxy": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzz",word2 = "zzx") == "zzxyzzx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzz",word2 = "zzx") == "zzxyzzx": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeff",word2 = "zzzzyyyxxxwwvvuuttssrrqqppoonnmmllkkjjiihghffeeddccbbaa") == "zzzzyyyxxxwwvvuuttssrrqqppoonnmmllkkjjiihghffeeddccbbaabbccddeeffaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeff",word2 = "zzzzyyyxxxwwvvuuttssrrqqppoonnmmllkkjjiihghffeeddccbbaa") == "zzzzyyyxxxwwvvuuttssrrqqppoonnmmllkkjjiihghffeeddccbbaabbccddeeffaa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abababab",word2 = "babababa") == "babababababababa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abababab",word2 = "babababa") == "babababababababa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xylophone",word2 = "xylophon") == "xyxyloplophonhone"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xylophone",word2 = "xylophon") == "xyxyloplophonhone": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abc",word2 = "") == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abc",word2 = "") == "abc": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdabcdabcd",word2 = "zyxwzyxwzyxwzyxw") == "zyxwzyxwzyxwzyxwabcdabcdabcdabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdabcdabcd",word2 = "zyxwzyxwzyxwzyxw") == "zyxwzyxwzyxwzyxwabcdabcdabcdabcd": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzz",word2 = "zzzz") == "zzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzz",word2 = "zzzz") == "zzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "longwordone",word2 = "longwordtwo") == "lonlongworgwordtwodone"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "longwordone",word2 = "longwordtwo") == "lonlongworgwordtwodone": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaaaaaaaa",word2 = "bbbbbbbbbbba") == "bbbbbbbbbbbaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaaaaaaaa",word2 = "bbbbbbbbbbba") == "bbbbbbbbbbbaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdabcd",word2 = "dcba") == "dcbabcdabcdabcda"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdabcd",word2 = "dcba") == "dcbabcdabcdabcda": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaabbbbcccc",word2 = "ddddccccbbbaaaa") == "ddddccccbbbaaaabbbbccccaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaabbbbcccc",word2 = "ddddccccbbbaaaa") == "ddddccccbbbaaaabbbbccccaaaa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "leetcode",word2 = "contest") == "leetcontestcode"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "leetcode",word2 = "contest") == "leetcontestcode": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "zoology") == "zpoonlogyeumonoultramicroscopicsilicovolcanoconiosis"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "zoology") == "zpoonlogyeumonoultramicroscopicsilicovolcanoconiosis": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdb",word2 = "abcdabcdb") == "abcdabcdbabcdabcdb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdb",word2 = "abcdabcdb") == "abcdabcdbabcdabcdb": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "amazing",word2 = "algorithm") == "amazingalgorithm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "amazing",word2 = "algorithm") == "amazingalgorithm": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "b",word2 = "a") == "ba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "b",word2 = "a") == "ba": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "qwerqwerqwer",word2 = "qwertyuiop") == "qwqwertyuioperqwerqwer"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "qwerqwerqwer",word2 = "qwertyuiop") == "qwqwertyuioperqwerqwer": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "onesmallstring",word2 = "averylongstringwithmanycharactersandvariouslengthsandcombinations") == "onesmaverylongstringwithmanycharallstringactersandvariouslengthsandcombinations"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "onesmallstring",word2 = "averylongstringwithmanycharactersandvariouslengthsandcombinations") == "onesmaverylongstringwithmanycharallstringactersandvariouslengthsandcombinations": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "banana",word2 = "apple") == "bappleanana"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "banana",word2 = "apple") == "bappleanana": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcde",word2 = "fghij") == "fghijabcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcde",word2 = "fghij") == "fghijabcde": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zyxwvutsrqponmlkjihgfedcba",word2 = "abcdefghijklmnopqrstuvwxyz") == "zyxwvutsrqponmlkjihgfedcbabcdefghijklmnopqrstuvwxyza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zyxwvutsrqponmlkjihgfedcba",word2 = "abcdefghijklmnopqrstuvwxyz") == "zyxwvutsrqponmlkjihgfedcbabcdefghijklmnopqrstuvwxyza": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzyzxzyzxzy",word2 = "xyxyxyxyxyx") == "zzyzxzyzxzyxyxyxyxyxyx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzyzxzyzxzy",word2 = "xyxyxyxyxyx") == "zzyzxzyzxzyxyxyxyxyxyx": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcc",word2 = "bbccaa") == "bbccaabbccaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcc",word2 = "bbccaa") == "bbccaabbccaa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "appleapple",word2 = "banana") == "bappleappleanana"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "appleapple",word2 = "banana") == "bappleappleanana": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdef",word2 = "fghijk") == "fghijkabcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdef",word2 = "fghijk") == "fghijkabcdef": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzyyyyxxx",word2 = "zzzyyyyxx") == "zzzzzzzyyyyyyyyxxxxx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzyyyyxxx",word2 = "zzzyyyyxx") == "zzzzzzzyyyyyyyyxxxxx": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaabbbb",word2 = "bbbbbaaaa") == "bbbbbaaaaaabbbbaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaabbbb",word2 = "bbbbbaaaa") == "bbbbbaaaaaabbbbaaaa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaa",word2 = "bbbbbbbb") == "bbbbbbbbaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaa",word2 = "bbbbbbbb") == "bbbbbbbbaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "lexicographically",word2 = "mergeable") == "mlexiergecographicallyable"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "lexicographically",word2 = "mergeable") == "mlexiergecographicallyable": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabc",word2 = "cbacbacba") == "cbacbacbabcabcabca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabc",word2 = "cbacbacba") == "cbacbacbabcabcabca": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "samestart",word2 = "samestart") == "ssamestartamestart"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "samestart",word2 = "samestart") == "ssamestartamestart": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzzzzzzzz",word2 = "zzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzzzzzzzz",word2 = "zzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdexyz",word2 = "zyxwvuts") == "zyxwvutsabcdexyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdexyz",word2 = "zyxwvuts") == "zyxwvutsabcdexyz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefg",word2 = "ghijklm") == "ghijklmabcdefg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefg",word2 = "ghijklm") == "ghijklmabcdefg": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "longwordone",word2 = "evenlongerwordtwo") == "longworevenlongerwordtwodone"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "longwordone",word2 = "evenlongerwordtwo") == "longworevenlongerwordtwodone": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaab",word2 = "aaabaaa") == "aaabaaaabaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaab",word2 = "aaabaaa") == "aaabaaaabaaa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcd",word2 = "dcbaabcd") == "dcbabcdabcdaabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcd",word2 = "dcbaabcd") == "dcbabcdabcdaabcd": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "supercalifragilisticexpialidocious") == "suppneumonoultrercamicroscopicsilicovolcanoconiosisalifragilisticexpialidocious"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "supercalifragilisticexpialidocious") == "suppneumonoultrercamicroscopicsilicovolcanoconiosisalifragilisticexpialidocious": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeff",word2 = "aabbccddeegf") == "aabbccddeegfaabbccddeeff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeff",word2 = "aabbccddeegf") == "aabbccddeegfaabbccddeeff": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zyxzyxzyx",word2 = "zyxzyxzyx") == "zzyyxzyxzyxzyxzyxx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zyxzyxzyx",word2 = "zyxzyxzyx") == "zzyyxzyxzyxzyxzyxx": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "overlapover",word2 = "overlap") == "ovoverlerlapoverap"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "overlapover",word2 = "overlap") == "ovoverlerlapoverap": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aebcdefghijklmnopqrstuvwxyz",word2 = "zxcvbnmlkjihgfedcbaeb") == "zxcvbnmlkjihgfedcbaebcdefghijklmnopqrstuvwxyzaeb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aebcdefghijklmnopqrstuvwxyz",word2 = "zxcvbnmlkjihgfedcbaeb") == "zxcvbnmlkjihgfedcbaebcdefghijklmnopqrstuvwxyzaeb": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdef",word2 = "fedcba") == "fedcbabcdefa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdef",word2 = "fedcba") == "fedcbabcdefa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaabbbbcccc",word2 = "ddddeeeeffff") == "ddddeeeeffffaaaabbbbcccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaabbbbcccc",word2 = "ddddeeeeffff") == "ddddeeeeffffaaaabbbbcccc": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "hellohellohello",word2 = "worldworld") == "worlhellohellohellodworld"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "hellohellohello",word2 = "worldworld") == "worlhellohellohellodworld": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabcabc",word2 = "abcabc") == "abcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabcabc",word2 = "abcabc") == "abcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzz",word2 = "zzz") == "zzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzz",word2 = "zzz") == "zzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzzzzzzzzzzzz",word2 = "yyyyyyyyyyyyyy") == "yyyyyyyyyyyyyyxyzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzzzzzzzzzzzz",word2 = "yyyyyyyyyyyyyy") == "yyyyyyyyyyyyyyxyzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabaaa",word2 = "baabaa") == "baabaabaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabaaa",word2 = "baabaa") == "baabaabaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaaaaaabbbbbbbbbbcccccccccc",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzaaaaaaaaaabbbbbbbbbbcccccccccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaaaaaabbbbbbbbbbcccccccccc",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzaaaaaaaaaabbbbbbbbbbcccccccccc": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word1 = "lexicographically",word2 = "largestmerge") == "llexicogrargestmergeaphically"
    assert candidate(word1 = "zyxw",word2 = "abcd") == "zyxwabcd"
    assert candidate(word1 = "abcdabcd",word2 = "zyxwzyxw") == "zyxwzyxwabcdabcd"
    assert candidate(word1 = "leetcode",word2 = "challenge") == "leetcodechallenge"
    assert candidate(word1 = "aaaab",word2 = "aaabb") == "aaabbaaaab"
    assert candidate(word1 = "lexicographic",word2 = "merge") == "mlexiergecographic"
    assert candidate(word1 = "aaaa",word2 = "bbbb") == "bbbbaaaa"
    assert candidate(word1 = "abcabc",word2 = "abdcaba") == "abdcabcabcaba"
    assert candidate(word1 = "abc",word2 = "defghijklmnopqrstuvwxyz") == "defghijklmnopqrstuvwxyzabc"
    assert candidate(word1 = "z",word2 = "z") == "zz"
    assert candidate(word1 = "hello",word2 = "world") == "worlhellod"
    assert candidate(word1 = "abcd",word2 = "zyxw") == "zyxwabcd"
    assert candidate(word1 = "leetcode",word2 = "etco") == "leteetcodeco"
    assert candidate(word1 = "xy",word2 = "xy") == "xyxy"
    assert candidate(word1 = "cabaa",word2 = "bcaaa") == "cbcabaaaaa"
    assert candidate(word1 = "aabbcc",word2 = "bbccdd") == "bbccddaabbcc"
    assert candidate(word1 = "zzz",word2 = "zzz") == "zzzzzz"
    assert candidate(word1 = "a",word2 = "b") == "ba"
    assert candidate(word1 = "aaaaa",word2 = "bbbbb") == "bbbbbaaaaa"
    assert candidate(word1 = "aabbcc",word2 = "abcabc") == "abcabcaabbcc"
    assert candidate(word1 = "xyz",word2 = "xyz") == "xyzxyz"
    assert candidate(word1 = "abcd",word2 = "efgh") == "efghabcd"
    assert candidate(word1 = "abcd",word2 = "dcba") == "dcbabcda"
    assert candidate(word1 = "same",word2 = "same") == "ssameame"
    assert candidate(word1 = "abcdabcd",word2 = "abcde") == "abcdeabcdabcd"
    assert candidate(word1 = "bca",word2 = "cab") == "cbcaba"
    assert candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgfedcbabcdefghijklmnopqrstuvwxyza"
    assert candidate(word1 = "mississippi",word2 = "missouri") == "mmissourississippii"
    assert candidate(word1 = "zzzzzzzz",word2 = "zzzzzzzz") == "zzzzzzzzzzzzzzzz"
    assert candidate(word1 = "complexity",word2 = "similarity") == "similcomplexityarity"
    assert candidate(word1 = "xyzzzzzzzzzzzzzzzz",word2 = "xyzzzzzzzzzzzzzz") == "xyzzzzzzzzzzzzzzzzxyzzzzzzzzzzzzzz"
    assert candidate(word1 = "aaaabbbbccccdddd",word2 = "aaaabbbbccccdddd") == "aaaabbbbccccddddaaaabbbbccccdddd"
    assert candidate(word1 = "zzzzzzz",word2 = "zzzzzzzz") == "zzzzzzzzzzzzzzz"
    assert candidate(word1 = "aaaaaaa",word2 = "bbbbbbb") == "bbbbbbbaaaaaaa"
    assert candidate(word1 = "zzzzz",word2 = "zzzz") == "zzzzzzzzz"
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zzzyyxxwwvvuuttssrrqqponmlkjihgfedcbbaa") == "zzzyyxxwwvvuuttssrrqqponmlkjihgfedcbbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaa"
    assert candidate(word1 = "zyxwvut",word2 = "utsrqponmlkjihgfedcba") == "zyxwvuuttsrqponmlkjihgfedcba"
    assert candidate(word1 = "pqrstuvwxyz",word2 = "nopqrstuvwxyz") == "pqrstuvwxyznopqrstuvwxyz"
    assert candidate(word1 = "zzzzzz",word2 = "zzzzzz") == "zzzzzzzzzzzz"
    assert candidate(word1 = "aabbccddeeff",word2 = "feebdccbaa") == "feebdccbaabbccddeeffaa"
    assert candidate(word1 = "cccccccc",word2 = "dddddddd") == "ddddddddcccccccc"
    assert candidate(word1 = "a",word2 = "z") == "za"
    assert candidate(word1 = "aabbcc",word2 = "aaabbb") == "aabbccaaabbb"
    assert candidate(word1 = "abcdxyz",word2 = "xyzabcd") == "xyzabcdxyzabcd"
    assert candidate(word1 = "python",word2 = "java") == "pytjhonava"
    assert candidate(word1 = "abcdabcdabcd",word2 = "abcabcabc") == "abcdabcdabcdabcabcabc"
    assert candidate(word1 = "sameprefix",word2 = "sameprefixsuffix") == "ssameprefixsuffixameprefix"
    assert candidate(word1 = "abcdefghij",word2 = "jihgfedcba") == "jihgfedcbabcdefghija"
    assert candidate(word1 = "onetwothreefour",word2 = "fivesixseveneightnine") == "onfivetwothresixseveneightnineefoure"
    assert candidate(word1 = "racecar",word2 = "racecar") == "rracecaracecar"
    assert candidate(word1 = "abcdabcdabcdabcdabcdabcd",word2 = "zyxwzyxwzyxwzyxwzyxwzyxw") == "zyxwzyxwzyxwzyxwzyxwzyxwabcdabcdabcdabcdabcdabcd"
    assert candidate(word1 = "xyxzyzyzyx",word2 = "zyzyzyzyxz") == "zyzyzyzyxzxyxzyzyzyx"
    assert candidate(word1 = "abacabadabacaba",word2 = "xyzxyzxyzxyzxyz") == "xyzxyzxyzxyzxyzabacabadabacaba"
    assert candidate(word1 = "xyzz",word2 = "yxzz") == "yxzzxyzz"
    assert candidate(word1 = "abcdabcdabcd",word2 = "zyxwzyxwzyxw") == "zyxwzyxwzyxwabcdabcdabcd"
    assert candidate(word1 = "aabbccddeeff",word2 = "zzzzyyyxxx") == "zzzzyyyxxxaabbccddeeff"
    assert candidate(word1 = "aabbccddeeff",word2 = "zzyyxxwwvvuu") == "zzyyxxwwvvuuaabbccddeeff"
    assert candidate(word1 = "abcdefg",word2 = "hijklmnop") == "hijklmnopabcdefg"
    assert candidate(word1 = "banana",word2 = "bandana") == "bbandanananaa"
    assert candidate(word1 = "abcdabcdabcd",word2 = "dcbaabcdabcd") == "dcbabcdabcdabcdaabcdabcd"
    assert candidate(word1 = "abracadabra",word2 = "alakazam") == "alakazamabracadabra"
    assert candidate(word1 = "aaaabbbbcccc",word2 = "bbbbaaaacccc") == "bbbbaaaaccccaaaabbbbcccc"
    assert candidate(word1 = "leetcode",word2 = "edocteel") == "leetedocteelcode"
    assert candidate(word1 = "aaaaaaaabbbbbbbbcccccccc",word2 = "ccccccccbbbbbbbbbaaaaaaa") == "ccccccccbbbbbbbbbaaaaaaaabbbbbbbbccccccccaaaaaaa"
    assert candidate(word1 = "abcdxyz",word2 = "zyxcba") == "zyxcbabcdxyza"
    assert candidate(word1 = "ababababab",word2 = "bababababa") == "babababababababababa"
    assert candidate(word1 = "equalequal",word2 = "equal") == "equequalequalal"
    assert candidate(word1 = "abcabcabc",word2 = "abcabcabc") == "abcabcabcabcabcabc"
    assert candidate(word1 = "zzzzzzyyyy",word2 = "yyyyzzzzzz") == "zzzzzzyyyyzzzzzzyyyy"
    assert candidate(word1 = "racecar",word2 = "race") == "rracecarace"
    assert candidate(word1 = "programming",word2 = "challenges") == "progrchammingallenges"
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgfedcbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzza"
    assert candidate(word1 = "abcdxyz",word2 = "zyxwvut") == "zyxwvutabcdxyz"
    assert candidate(word1 = "abacaxi",word2 = "abacax") == "abacaxiabacax"
    assert candidate(word1 = "aaaaaabbbbb",word2 = "cccccdddddeeeee") == "cccccdddddeeeeeaaaaaabbbbb"
    assert candidate(word1 = "abcdefg",word2 = "zyxwvutsrqponmlkjihgfedcba") == "zyxwvutsrqponmlkjihgfedcbabcdefga"
    assert candidate(word1 = "samecharacters",word2 = "samecharacters") == "ssamecharamecharactersacters"
    assert candidate(word1 = "abababababab",word2 = "babababababa") == "babababababababababababa"
    assert candidate(word1 = "aaaaab",word2 = "bbbaaa") == "bbbaaaaabaaa"
    assert candidate(word1 = "aabbbccc",word2 = "aabbcc") == "aabbccaabbbccc"
    assert candidate(word1 = "zzzzz",word2 = "zzzzzz") == "zzzzzzzzzzz"
    assert candidate(word1 = "",word2 = "abc") == "abc"
    assert candidate(word1 = "abcdefghijk",word2 = "abcdefghijl") == "abcdefghijlabcdefghijk"
    assert candidate(word1 = "nestednested",word2 = "nested") == "nnestesteednestedd"
    assert candidate(word1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",word2 = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(word1 = "abcde",word2 = "edcba") == "edcbabcdea"
    assert candidate(word1 = "supercalifragilisticexpialidocious",word2 = "antidisestablishmentarianism") == "supercantidisestalifragilisticexpialidociousablishmentarianism"
    assert candidate(word1 = "xyzz",word2 = "zzxy") == "zzxyzzxy"
    assert candidate(word1 = "xyzz",word2 = "zzx") == "zzxyzzx"
    assert candidate(word1 = "aabbccddeeff",word2 = "zzzzyyyxxxwwvvuuttssrrqqppoonnmmllkkjjiihghffeeddccbbaa") == "zzzzyyyxxxwwvvuuttssrrqqppoonnmmllkkjjiihghffeeddccbbaabbccddeeffaa"
    assert candidate(word1 = "abababab",word2 = "babababa") == "babababababababa"
    assert candidate(word1 = "xylophone",word2 = "xylophon") == "xyxyloplophonhone"
    assert candidate(word1 = "abc",word2 = "") == "abc"
    assert candidate(word1 = "abcdabcdabcdabcd",word2 = "zyxwzyxwzyxwzyxw") == "zyxwzyxwzyxwzyxwabcdabcdabcdabcd"
    assert candidate(word1 = "zzzz",word2 = "zzzz") == "zzzzzzzz"
    assert candidate(word1 = "longwordone",word2 = "longwordtwo") == "lonlongworgwordtwodone"
    assert candidate(word1 = "aaaaaaaaaaaa",word2 = "bbbbbbbbbbba") == "bbbbbbbbbbbaaaaaaaaaaaaa"
    assert candidate(word1 = "abcdabcdabcd",word2 = "dcba") == "dcbabcdabcdabcda"
    assert candidate(word1 = "aaaabbbbcccc",word2 = "ddddccccbbbaaaa") == "ddddccccbbbaaaabbbbccccaaaa"
    assert candidate(word1 = "leetcode",word2 = "contest") == "leetcontestcode"
    assert candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "zoology") == "zpoonlogyeumonoultramicroscopicsilicovolcanoconiosis"
    assert candidate(word1 = "abcdabcdb",word2 = "abcdabcdb") == "abcdabcdbabcdabcdb"
    assert candidate(word1 = "amazing",word2 = "algorithm") == "amazingalgorithm"
    assert candidate(word1 = "b",word2 = "a") == "ba"
    assert candidate(word1 = "qwerqwerqwer",word2 = "qwertyuiop") == "qwqwertyuioperqwerqwer"
    assert candidate(word1 = "onesmallstring",word2 = "averylongstringwithmanycharactersandvariouslengthsandcombinations") == "onesmaverylongstringwithmanycharallstringactersandvariouslengthsandcombinations"
    assert candidate(word1 = "banana",word2 = "apple") == "bappleanana"
    assert candidate(word1 = "abcde",word2 = "fghij") == "fghijabcde"
    assert candidate(word1 = "zyxwvutsrqponmlkjihgfedcba",word2 = "abcdefghijklmnopqrstuvwxyz") == "zyxwvutsrqponmlkjihgfedcbabcdefghijklmnopqrstuvwxyza"
    assert candidate(word1 = "zzyzxzyzxzy",word2 = "xyxyxyxyxyx") == "zzyzxzyzxzyxyxyxyxyxyx"
    assert candidate(word1 = "aabbcc",word2 = "bbccaa") == "bbccaabbccaa"
    assert candidate(word1 = "appleapple",word2 = "banana") == "bappleappleanana"
    assert candidate(word1 = "abcdef",word2 = "fghijk") == "fghijkabcdef"
    assert candidate(word1 = "zzzzyyyyxxx",word2 = "zzzyyyyxx") == "zzzzzzzyyyyyyyyxxxxx"
    assert candidate(word1 = "aaaaaabbbb",word2 = "bbbbbaaaa") == "bbbbbaaaaaabbbbaaaa"
    assert candidate(word1 = "aaaaaa",word2 = "bbbbbbbb") == "bbbbbbbbaaaaaa"
    assert candidate(word1 = "lexicographically",word2 = "mergeable") == "mlexiergecographicallyable"
    assert candidate(word1 = "abcabcabc",word2 = "cbacbacba") == "cbacbacbabcabcabca"
    assert candidate(word1 = "samestart",word2 = "samestart") == "ssamestartamestart"
    assert candidate(word1 = "zzzzzzzzzz",word2 = "zzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzz"
    assert candidate(word1 = "abcdexyz",word2 = "zyxwvuts") == "zyxwvutsabcdexyz"
    assert candidate(word1 = "abcdefg",word2 = "ghijklm") == "ghijklmabcdefg"
    assert candidate(word1 = "longwordone",word2 = "evenlongerwordtwo") == "longworevenlongerwordtwodone"
    assert candidate(word1 = "aaaab",word2 = "aaabaaa") == "aaabaaaabaaa"
    assert candidate(word1 = "abcdabcd",word2 = "dcbaabcd") == "dcbabcdabcdaabcd"
    assert candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "supercalifragilisticexpialidocious") == "suppneumonoultrercamicroscopicsilicovolcanoconiosisalifragilisticexpialidocious"
    assert candidate(word1 = "aabbccddeeff",word2 = "aabbccddeegf") == "aabbccddeegfaabbccddeeff"
    assert candidate(word1 = "zyxzyxzyx",word2 = "zyxzyxzyx") == "zzyyxzyxzyxzyxzyxx"
    assert candidate(word1 = "overlapover",word2 = "overlap") == "ovoverlerlapoverap"
    assert candidate(word1 = "aebcdefghijklmnopqrstuvwxyz",word2 = "zxcvbnmlkjihgfedcbaeb") == "zxcvbnmlkjihgfedcbaebcdefghijklmnopqrstuvwxyzaeb"
    assert candidate(word1 = "abcdef",word2 = "fedcba") == "fedcbabcdefa"
    assert candidate(word1 = "aaaabbbbcccc",word2 = "ddddeeeeffff") == "ddddeeeeffffaaaabbbbcccc"
    assert candidate(word1 = "hellohellohello",word2 = "worldworld") == "worlhellohellohellodworld"
    assert candidate(word1 = "abcabcabcabc",word2 = "abcabc") == "abcabcabcabcabcabc"
    assert candidate(word1 = "zzzz",word2 = "zzz") == "zzzzzzz"
    assert candidate(word1 = "xyzzzzzzzzzzzz",word2 = "yyyyyyyyyyyyyy") == "yyyyyyyyyyyyyyxyzzzzzzzzzzzz"
    assert candidate(word1 = "aabaaa",word2 = "baabaa") == "baabaabaaaaa"
    assert candidate(word1 = "aaaaaaaaaabbbbbbbbbbcccccccccc",word2 = "zzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzaaaaaaaaaabbbbbbbbbbcccccccccc"


