def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "racecar",k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar",k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnoonm",k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnoonm",k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzz",k = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzz",k = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcba",k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcba",k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zz",k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zz",k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "adbcda",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "adbcda",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa",k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa",k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaeaeabba",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaeaeabba",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabba",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabba",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonhighnoon",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonhighnoon",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdfgdcaba",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcaba",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa",k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa",k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcba",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcba",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarannakayak",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarannakayak",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcba",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcba",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abaccdbbd",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abaccdbbd",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaeae",k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaeae",k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "z",k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "z",k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaaabaaaa",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaaabaaaa",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "levellevellevel",k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levellevellevel",k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababa",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababa",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaabccba",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaabccba",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "level",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "level",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxxyxyxyx",k = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxxyxyxyx",k = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaabbbaaaa",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaabbbaaaa",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababab",k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababab",k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorreferredder",k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorreferredder",k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "popopopopopop",k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "popopopopopop",k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abaaaaba",k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abaaaaba",k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyzyzyxzyx",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyzyzyxzyx",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamimadam",k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamimadam",k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaa",k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaa",k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaabba",k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaabba",k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotor",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotor",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcddcbaabcddcba",k = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcddcbaabcddcba",k = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "palindromemordnilap",k = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "palindromemordnilap",k = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggghhhiii",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggghhhiii",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyzyzxzyxzyx",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyzyzxzyxzyx",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaabaaaa",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaabaaaa",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelracecaraabba",k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelracecaraabba",k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarannakayak",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarannakayak",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccba",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccba",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabc",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabc",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcbaedcbba",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcbaedcbba",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoon",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoon",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaaccddccaaabbbcccdd",k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaaccddccaaabbbcccdd",k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbabcba",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbabcba",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbabbaaabbabba",k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbabbaaabbabba",k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaaccddccbaabba",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaaccddccbaabba",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaacccbaaabbcc",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaacccbaaabbcc",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "civiccivic",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "civiccivic",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaaacaaaaaa",k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaaacaaaaaa",k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcbaabcdcba",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcbaabcdcba",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyzyzyzyzyzyzy",k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyzyzyzyzyzyzy",k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamracecarlevel",k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamracecarlevel",k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyzyzyzxzyzyx",k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyzyzyzxzyzyx",k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaabacaxxx",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaabacaxxx",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoon",k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoon",k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzyyyyxxxx",k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzyyyyxxxx",k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccdddd",k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccdddd",k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "civicracecardeified",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "civicracecardeified",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg",k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg",k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamimadam",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamimadam",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabaaaabaaaaabaaabaaa",k = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabaaaabaaaaabaaabaaa",k = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar",k = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar",k = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxxyxyxyxyx",k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxxyxyxyxyx",k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbabcba",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbabcba",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",k = 1) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",k = 1) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgfedcba",k = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgfedcba",k = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "mamadadadadammadam",k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mamadadadadammadam",k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamimadam",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamimadam",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "babaddabba",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babaddabba",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbabaaaabbabaab",k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbabaaaabbabaab",k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "babbbabbbab",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babbbabbbab",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaaabbbaaa",k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaaabbbaaa",k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaaabbbaabbaab",k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaaabbbaabbaab",k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabc",k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabc",k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaabba",k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaabba",k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbbbbbaaaaaabbbbb",k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbbbbbaaaaaabbbbb",k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaabababaabcba",k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaabababaabcba",k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabcabcabcabcba",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabcabcabcabcba",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabcba",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabcba",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbabbaabb",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbabbaabb",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefedcba",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefedcba",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghihgfedcba",k = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghihgfedcba",k = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonmoonnoonmoon",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonmoonnoonmoon",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefedcbafedcbabcdef",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefedcbafedcbabcdef",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabba",k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabba",k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "deeeeinedede",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deeeeinedede",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcba",k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcba",k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeffgg",k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeffgg",k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcbaabacdfgdcaba",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcbaabacdfgdcaba",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzyyyxxxwwvvuuttssrrqqppoonnmmlkkjjiihhggffeeddccbbaaa",k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzyyyxxxwwvvuuttssrrqqppoonnmmlkkjjiihhggffeeddccbbaaa",k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 2) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 2) == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbaaaaa",k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbaaaaa",k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamimadam",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamimadam",k = 4) == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "racecar",k = 2) == 1
    assert candidate(s = "mnoonm",k = 2) == 1
    assert candidate(s = "zzzzzz",k = 1) == 6
    assert candidate(s = "abcde",k = 3) == 0
    assert candidate(s = "abcdeedcba",k = 2) == 1
    assert candidate(s = "zz",k = 1) == 2
    assert candidate(s = "adbcda",k = 2) == 0
    assert candidate(s = "",k = 1) == 0
    assert candidate(s = "abcde",k = 1) == 5
    assert candidate(s = "aaaaa",k = 2) == 2
    assert candidate(s = "racecar",k = 3) == 1
    assert candidate(s = "abbaeaeabba",k = 3) == 3
    assert candidate(s = "abbaabba",k = 3) == 2
    assert candidate(s = "noonhighnoon",k = 4) == 2
    assert candidate(s = "abacdfgdcaba",k = 3) == 2
    assert candidate(s = "aaaa",k = 2) == 2
    assert candidate(s = "a",k = 1) == 1
    assert candidate(s = "abcdedcba",k = 5) == 1
    assert candidate(s = "racecarannakayak",k = 3) == 3
    assert candidate(s = "abcba",k = 5) == 1
    assert candidate(s = "abaccdbbd",k = 3) == 2
    assert candidate(s = "abbaeae",k = 2) == 2
    assert candidate(s = "z",k = 1) == 1
    assert candidate(s = "aaabaaaabaaaa",k = 5) == 2
    assert candidate(s = "levellevellevel",k = 5) == 3
    assert candidate(s = "abcabcabcabc",k = 3) == 0
    assert candidate(s = "ababababa",k = 3) == 3
    assert candidate(s = "abcbaabccba",k = 3) == 2
    assert candidate(s = "level",k = 5) == 1
    assert candidate(s = "xyxxyxyxyx",k = 1) == 10
    assert candidate(s = "aabbaaabbbaaaa",k = 2) == 6
    assert candidate(s = "ababababababab",k = 2) == 4
    assert candidate(s = "rotorreferredder",k = 4) == 3
    assert candidate(s = "popopopopopop",k = 3) == 4
    assert candidate(s = "abaaaaba",k = 4) == 1
    assert candidate(s = "xyxzyzyzyxzyx",k = 3) == 3
    assert candidate(s = "madamimadam",k = 2) == 3
    assert candidate(s = "aaaaaaaaaaaaaaaaaa",k = 10) == 1
    assert candidate(s = "abbaabbaabba",k = 4) == 3
    assert candidate(s = "aabbccddeeff",k = 2) == 6
    assert candidate(s = "rotor",k = 5) == 1
    assert candidate(s = "abcddcbaabcddcba",k = 6) == 2
    assert candidate(s = "palindromemordnilap",k = 6) == 1
    assert candidate(s = "aabbccddeeefffggghhhiii",k = 4) == 0
    assert candidate(s = "xyxzyzyzxzyxzyx",k = 3) == 3
    assert candidate(s = "aaaaaaaabaaaa",k = 5) == 2
    assert candidate(s = "levelracecaraabba",k = 4) == 3
    assert candidate(s = "racecarannakayak",k = 5) == 2
    assert candidate(s = "abccbaabccba",k = 3) == 2
    assert candidate(s = "abcabcabcabcabcabcabc",k = 3) == 0
    assert candidate(s = "abcdedcbaedcbba",k = 5) == 1
    assert candidate(s = "noonnoonnoon",k = 3) == 3
    assert candidate(s = "abbaaccddccaaabbbcccdd",k = 3) == 5
    assert candidate(s = "abcbabcba",k = 5) == 1
    assert candidate(s = "aabbabbaaabbabba",k = 4) == 3
    assert candidate(s = "abbaaccddccbaabba",k = 3) == 3
    assert candidate(s = "abbaacccbaaabbcc",k = 3) == 3
    assert candidate(s = "civiccivic",k = 4) == 2
    assert candidate(s = "aaabaaaacaaaaaa",k = 3) == 4
    assert candidate(s = "abracadabra",k = 3) == 1
    assert candidate(s = "abcdcbaabcdcba",k = 5) == 2
    assert candidate(s = "xyzyzyzyzyzyzyzy",k = 2) == 5
    assert candidate(s = "madamracecarlevel",k = 5) == 3
    assert candidate(s = "xyxzyzyzyzxzyzyx",k = 3) == 5
    assert candidate(s = "bananaabacaxxx",k = 3) == 3
    assert candidate(s = "noonnoonnoon",k = 4) == 3
    assert candidate(s = "abcdefghij",k = 3) == 0
    assert candidate(s = "zzzzyyyyxxxx",k = 4) == 3
    assert candidate(s = "aaaabbbbccccdddd",k = 4) == 4
    assert candidate(s = "civicracecardeified",k = 3) == 3
    assert candidate(s = "aabbccddeeffgg",k = 2) == 7
    assert candidate(s = "madamimadam",k = 5) == 2
    assert candidate(s = "aaaabaaaabaaaaabaaabaaa",k = 2) == 9
    assert candidate(s = "racecar",k = 6) == 1
    assert candidate(s = "xyxxyxyxyxyx",k = 2) == 4
    assert candidate(s = "abcbabcba",k = 3) == 2
    assert candidate(s = "abcabcabcabc",k = 1) == 12
    assert candidate(s = "abcdefgfedcba",k = 7) == 1
    assert candidate(s = "mamadadadadammadam",k = 3) == 5
    assert candidate(s = "madamimadam",k = 3) == 3
    assert candidate(s = "babaddabba",k = 3) == 2
    assert candidate(s = "aabbabaaaabbabaab",k = 3) == 4
    assert candidate(s = "babbbabbbab",k = 3) == 3
    assert candidate(s = "aabaaaabbbaaa",k = 3) == 4
    assert candidate(s = "aabbaabbaaabbbaabbaab",k = 3) == 4
    assert candidate(s = "abccbaabc",k = 4) == 1
    assert candidate(s = "abracadabra",k = 5) == 0
    assert candidate(s = "abbaabbaabba",k = 2) == 5
    assert candidate(s = "aaaaaabbbbbbaaaaaabbbbb",k = 5) == 4
    assert candidate(s = "abcbaabababaabcba",k = 3) == 4
    assert candidate(s = "abcabcabc",k = 2) == 0
    assert candidate(s = "abccbaabcabcabcabcba",k = 5) == 2
    assert candidate(s = "abccbaabcba",k = 5) == 2
    assert candidate(s = "mississippi",k = 3) == 2
    assert candidate(s = "abbaabbabbaabb",k = 2) == 6
    assert candidate(s = "abcdefedcba",k = 5) == 1
    assert candidate(s = "abcdefghihgfedcba",k = 7) == 1
    assert candidate(s = "noonmoonnoonmoon",k = 4) == 2
    assert candidate(s = "abcdefedcbafedcbabcdef",k = 5) == 2
    assert candidate(s = "abbaabba",k = 2) == 3
    assert candidate(s = "deeeeinedede",k = 4) == 2
    assert candidate(s = "abcdedcba",k = 4) == 1
    assert candidate(s = "aabbccddeeeffgg",k = 2) == 7
    assert candidate(s = "abcdedcbaabacdfgdcaba",k = 5) == 1
    assert candidate(s = "zzzzyyyxxxwwvvuuttssrrqqppoonnmmlkkjjiihhggffeeddccbbaaa",k = 4) == 1
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 2) == 26
    assert candidate(s = "aaaaabbbaaaaa",k = 4) == 3
    assert candidate(s = "abacabadabacaba",k = 4) == 2
    assert candidate(s = "madamimadam",k = 4) == 2


