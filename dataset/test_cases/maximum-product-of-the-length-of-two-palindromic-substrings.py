def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "mnoonmmon") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnoonmmon") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "mamadmim") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mamadmim") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "mamad") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mamad") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghi") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghi") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdfgdcaba") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcaba") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "zaaaxbbby") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zaaaxbbby") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoon") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoon") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababbb") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababbb") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbabcbabcba") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbabcbabcba") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijj") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijj") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnoonmnonoomnm") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnoonmnonoomnm") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeffgg") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeffgg") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccbaabccbaabccba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccbaabccbaabccba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbaaaaa") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbaaaaa") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "nunrunrunrun") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nunrunrunrun") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abaaacbaaaaba") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abaaacbaaaaba") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarlevelnoonracecar") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarlevelnoonracecar") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "deeeeefedeeeed") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deeeeefedeeeed") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorrotor") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorrotor") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaacbabcba") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaacbabcba") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbacbacbacb") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbacbacbacb") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "tattarrattat") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "tattarrattat") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "repaperrelevelrepeepr") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repaperrelevelrepeepr") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "babadabababa") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babadabababa") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "madaminnadammadam") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madaminnadammadam") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabcdcba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabcdcba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaaabaaaabaa") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaaabaaaabaa") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeffedcbaffedcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeffedcbaffedcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabcbaedcbaxyz") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabcbaedcbaxyz") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "levellevellevellevel") == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levellevellevellevel") == 75: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoonnoon") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoonnoon") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippimississippi") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippimississippi") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdfgdcabaxyzzyzyzyzyzx") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcabaxyzzyzyzyzyzx") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbaabbbaabbbaaa") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbaabbbaabbbaaa") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacadaeafagahagaha") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacadaeafagahagaha") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonracecarnoon") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonracecarnoon") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbaaabbbaaabbbaaabbbaaabbba") == 221
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbaaabbbaaabbbaaabbbaaabbba") == 221: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababa") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababa") == 63: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabaabacabaabacaba") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabaabacabaabacaba") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "repel") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repel") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelnoonlevel") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelnoonlevel") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorlevelmadamracecar") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorlevelmadamracecar") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoonnoonnoonnoon") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoonnoonnoonnoon") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "kayak") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "kayak") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvuvwxyzyx") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvuvwxyzyx") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamlevelmadam") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamlevelmadam") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "babcbabcbabcba") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babcbabcbabcba") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacadaeafagaha") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacadaeafagaha") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "leveloneleveleleveldoneleveldot") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leveloneleveleleveldoneleveldot") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzzyzyzyzx") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzzyzyzyzx") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "madaminnadam") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madaminnadam") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababab") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababab") == 63: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarabcdeedcbacar") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarabcdeedcbacar") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "noon") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noon") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbacbacb") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbacbacb") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababab") == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababab") == 81: {e}')
    
    total += 1
    try:
        result = candidate(s = "deeee") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deeee") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "leveloneleveltwo") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leveloneleveltwo") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzbcbzxyxzyzyzyz") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzbcbzxyxzyzyzyz") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefggfedcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefggfedcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbbaaaa") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbbaaaa") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeffedcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeffedcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababcbaababcbaababcba") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababcbaababcbaababcba") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "babcbabcbabcbabcbabcbabcbabcbabcbabcbabcba") == 399
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babcbabcbabcbabcbabcbabcbabcbabcbabcbabcba") == 399: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababaababaababa") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababaababaababa") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbabcbaabcbabcba") == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbabcbaabcbabcba") == 81: {e}')
    
    total += 1
    try:
        result = candidate(s = "mmabccbaakak") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mmabccbaakak") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefedcba") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefedcba") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "palindromeemordnilap") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "palindromeemordnilap") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "level") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "level") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarlevelracecar") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarlevelracecar") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "levellevellevel") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levellevellevel") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabaaaaabaaaaabaaaaab") == 143
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabaaaaabaaaaabaaaaab") == 143: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyxzyxzyx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyxzyxzyx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "nunabannun") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nunabannun") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "deeeeefeeeed") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deeeeefeeeed") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzz") == 143
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzz") == 143: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab") == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab") == 99: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamimadamracecar") == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamimadamracecar") == 77: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbbabbbaaaaaaaabbba") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbbabbbaaaaaaaabbba") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "radar") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "radar") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababa") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababa") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabada") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabada") == 63: {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaananab") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaananab") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggg") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggg") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "redivider") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "redivider") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 99: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabccbaabcabccba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabccbaabcabccba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnbvcxzlkjhgfdsapoiuytrewq") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnbvcxzlkjhgfdsapoiuytrewq") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "deedlevel") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deedlevel") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbabcba") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbabcba") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "deifiedrotatordeified") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deifiedrotatordeified") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoonnoonnoon") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoonnoonnoon") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbadefgfe") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbadefgfe") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "anana") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "anana") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababaabababababa") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababaabababababa") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabraabracadabra") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabraabracadabra") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "detartrated") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "detartrated") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "manamzzamanaplanacanalpanamazzamanaplanacanalpanamazzzzzz") == 529
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "manamzzamanaplanacanalpanamazzamanaplanacanalpanamazzzzzz") == 529: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxyxyxyxyx") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxyxyxyxyx") == 63: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamimadam") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamimadam") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelonelevelonelevel") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelonelevelonelevel") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamracecaramadam") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamracecaramadam") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbaaabbaaa") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbaaabbaaa") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xylophonepiponolyx") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xylophonepiponolyx") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarandracecar") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarandracecar") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaaabaaba") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaaabaaba") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarannakayak") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarannakayak") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "kayakkayakkayakkayak") == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "kayakkayakkayakkayak") == 75: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbaaaaa") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbaaaaa") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "mammadmooommom") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mammadmooommom") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbaaaaaabbbbaaaaa") == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbaaaaaabbbbaaaaa") == 75: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarracecar") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarracecar") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoon") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoon") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "repaper") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repaper") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarlevelrotorkayak") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarlevelrotorkayak") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorrotorrotor") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorrotorrotor") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabaaabaaaabaaaaabaaaa") == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabaaabaaaabaaaaabaaaa") == 99: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababaababab") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababaababab") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonhighnoon") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonhighnoon") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "tacocattacocattaco") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "tacocattacocattaco") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorrotorrotorrotor") == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorrotorrotorrotor") == 75: {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaananananab") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaananananab") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzyzyzyzyzyzyzyzyzyzyzyz") == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzyzyzyzyzyzyzyzyzyzyzyz") == 121: {e}')
    
    total += 1
    try:
        result = candidate(s = "deeddeeddeed") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deeddeeddeed") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbbbbaaaa") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbbbbaaaa") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorresistor") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorresistor") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "xylophonelevel") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xylophonelevel") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaaabaaaaabaaaaaaab") == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaaabaaaaabaaaaaaab") == 77: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffgggzzzzzzzzzzzzzzzzzzzz") == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffgggzzzzzzzzzzzzzzzzzzzz") == 99: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcbaabcdedcbaabcdedcba") == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcbaabcdedcbaabcdedcba") == 81: {e}')
    
    total += 1
    try:
        result = candidate(s = "civic") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "civic") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotor") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotor") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuioplkjhgfdsazxcvbnmnbvcxzasdfghjklpoiuytrewq") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuioplkjhgfdsazxcvbnmnbvcxzasdfghjklpoiuytrewq") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbbaabba") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbbaabba") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghihgfedcba") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghihgfedcba") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "tacocattaco") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "tacocattaco") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "repaperrepaperrepaper") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repaperrepaperrepaper") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaaabaa") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaaabaa") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "reviled") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "reviled") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "amoreroma") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "amoreroma") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggghhhiiiijjjjkkkkllllmmmnnnooopppqqqqrrrrssssttttuuuuvvvvwwwwwxxxxxyyyyyzzzzzzyyyyyxxxwwvvuuttrrqqppoonnmlkkjjiihhggffeeddccbbaa") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggghhhiiiijjjjkkkkllllmmmnnnooopppqqqqrrrrssssttttuuuuvvvvwwwwwxxxxxyyyyyzzzzzzyyyyyxxxwwvvuuttrrqqppoonnmlkkjjiihhggffeeddccbbaa") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyzyzyzyzyzyzyz") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyzyzyzyzyzyzyz") == 63: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyzyzyzyzyzyx") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyzyzyzyzyzyx") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzyyyyyxxxwwvvuuttrrqqppoonnmlkkjjiihhggffeeddccbbaa") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzyyyyyxxxwwvvuuttrrqqppoonnmlkkjjiihhggffeeddccbbaa") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorabcdrotor") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorabcdrotor") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeffgghhiii") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeffgghhiii") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcbabcdedcbabcdedcb") == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcbabcdedcbabcdedcb") == 135: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggghhhiiiijjjjkkkkllllmmmnnnooopppqqqqrrrrssssttttuuuuvvvvwwwwwxxxxxyyyyyzzzzz") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggghhhiiiijjjjkkkkllllmmmnnnooopppqqqqrrrrssssttttuuuuvvvvwwwwwxxxxxyyyyyzzzzz") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "deed") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deed") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbbaaaaa") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbbaaaaa") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelwasracecar") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelwasracecar") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarabcdeedcba") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarabcdeedcba") == 9: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "mnoonmmon") == 1
    assert candidate(s = "mamadmim") == 9
    assert candidate(s = "abcdcba") == 5
    assert candidate(s = "abcdedcba") == 7
    assert candidate(s = "mamad") == 3
    assert candidate(s = "aaaaa") == 3
    assert candidate(s = "abcdefghi") == 1
    assert candidate(s = "abacdfgdcaba") == 9
    assert candidate(s = "zaaaxbbby") == 9
    assert candidate(s = "noonnoon") == 1
    assert candidate(s = "abcde") == 1
    assert candidate(s = "racecar") == 5
    assert candidate(s = "abcdeedcba") == 1
    assert candidate(s = "banana") == 5
    assert candidate(s = "ababbb") == 9
    assert candidate(s = "abc") == 1
    assert candidate(s = "abcbabcbabcba") == 35
    assert candidate(s = "abcdefgh") == 1
    assert candidate(s = "abcd") == 1
    assert candidate(s = "mississippi") == 7
    assert candidate(s = "aabbccddeeffgghhiijj") == 1
    assert candidate(s = "mnoonmnonoomnm") == 15
    assert candidate(s = "abcdefg") == 1
    assert candidate(s = "aabbccddeeeffgg") == 3
    assert candidate(s = "abccbaabccbaabccbaabccba") == 1
    assert candidate(s = "aaaaaabbaaaaa") == 25
    assert candidate(s = "nunrunrunrun") == 3
    assert candidate(s = "abaaacbaaaaba") == 9
    assert candidate(s = "racecarlevelnoonracecar") == 49
    assert candidate(s = "deeeeefedeeeed") == 15
    assert candidate(s = "rotorrotor") == 25
    assert candidate(s = "abracadabra") == 3
    assert candidate(s = "abcabcabcabc") == 1
    assert candidate(s = "abcbaacbabcba") == 25
    assert candidate(s = "abcbacbacbacb") == 5
    assert candidate(s = "tattarrattat") == 9
    assert candidate(s = "repaperrelevelrepeepr") == 35
    assert candidate(s = "babadabababa") == 25
    assert candidate(s = "madaminnadammadam") == 25
    assert candidate(s = "abccbaabcdcba") == 7
    assert candidate(s = "aabaaaabaaaabaa") == 25
    assert candidate(s = "abcdeffedcbaffedcba") == 1
    assert candidate(s = "abccbaabccba") == 1
    assert candidate(s = "xyzabcbaedcbaxyz") == 5
    assert candidate(s = "levellevellevellevel") == 75
    assert candidate(s = "noonnoonnoonnoon") == 1
    assert candidate(s = "mississippimississippi") == 49
    assert candidate(s = "xyzxyzxyzxyz") == 1
    assert candidate(s = "abacdfgdcabaxyzzyzyzyzyzx") == 27
    assert candidate(s = "aabbbaabbbaabbbaaa") == 49
    assert candidate(s = "abacadaeafagahagaha") == 21
    assert candidate(s = "noonracecarnoon") == 13
    assert candidate(s = "aabbbaaabbbaaabbbaaabbbaaabbba") == 221
    assert candidate(s = "ababababababababa") == 63
    assert candidate(s = "abacabaabacabaabacaba") == 49
    assert candidate(s = "repel") == 3
    assert candidate(s = "levelnoonlevel") == 25
    assert candidate(s = "rotorlevelmadamracecar") == 35
    assert candidate(s = "noonnoonnoonnoonnoonnoon") == 1
    assert candidate(s = "kayak") == 3
    assert candidate(s = "mnopqrstuvuvwxyzyx") == 15
    assert candidate(s = "madamlevelmadam") == 25
    assert candidate(s = "babcbabcbabcba") == 35
    assert candidate(s = "abacadaeafagaha") == 9
    assert candidate(s = "leveloneleveleleveldoneleveldot") == 55
    assert candidate(s = "xyzzzzyzyzyzx") == 21
    assert candidate(s = "madaminnadam") == 15
    assert candidate(s = "abababababababab") == 63
    assert candidate(s = "racecarabcdeedcbacar") == 21
    assert candidate(s = "noon") == 1
    assert candidate(s = "abcbacbacb") == 5
    assert candidate(s = "ababababababababab") == 81
    assert candidate(s = "deeee") == 3
    assert candidate(s = "leveloneleveltwo") == 25
    assert candidate(s = "abcabcabcabcabcabc") == 1
    assert candidate(s = "xyzbcbzxyxzyzyzyz") == 35
    assert candidate(s = "abcdefggfedcba") == 1
    assert candidate(s = "aaaaabbbbbbaaaa") == 25
    assert candidate(s = "abcdeffedcba") == 1
    assert candidate(s = "ababcbaababcbaababcba") == 25
    assert candidate(s = "babcbabcbabcbabcbabcbabcbabcbabcbabcbabcba") == 399
    assert candidate(s = "ababaababaababa") == 27
    assert candidate(s = "abcbabcbaabcbabcba") == 81
    assert candidate(s = "mmabccbaakak") == 3
    assert candidate(s = "abcdefedcba") == 9
    assert candidate(s = "palindromeemordnilap") == 1
    assert candidate(s = "level") == 3
    assert candidate(s = "racecarlevelracecar") == 49
    assert candidate(s = "levellevellevel") == 25
    assert candidate(s = "aaaaabaaaaabaaaaabaaaaab") == 143
    assert candidate(s = "xyxzyxzyxzyx") == 3
    assert candidate(s = "nunabannun") == 15
    assert candidate(s = "deeeeefeeeed") == 15
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzz") == 143
    assert candidate(s = "abababababababababab") == 99
    assert candidate(s = "madamimadamracecar") == 77
    assert candidate(s = "abbbbabbbaaaaaaaabbba") == 49
    assert candidate(s = "radar") == 3
    assert candidate(s = "abababa") == 9
    assert candidate(s = "abacabadabacaba") == 49
    assert candidate(s = "abacabadabacabada") == 63
    assert candidate(s = "bananaananab") == 25
    assert candidate(s = "aabbccddeeefffggg") == 9
    assert candidate(s = "redivider") == 7
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 99
    assert candidate(s = "abcabccbaabcabccba") == 1
    assert candidate(s = "mnbvcxzlkjhgfdsapoiuytrewq") == 1
    assert candidate(s = "deedlevel") == 5
    assert candidate(s = "abcbabcba") == 15
    assert candidate(s = "deifiedrotatordeified") == 49
    assert candidate(s = "noonnoonnoonnoonnoon") == 1
    assert candidate(s = "abcbadefgfe") == 25
    assert candidate(s = "anana") == 3
    assert candidate(s = "ababaabababababa") == 55
    assert candidate(s = "abracadabraabracadabra") == 9
    assert candidate(s = "detartrated") == 9
    assert candidate(s = "manamzzamanaplanacanalpanamazzamanaplanacanalpanamazzzzzz") == 529
    assert candidate(s = "xyxyxyxyxyxyxyxyx") == 63
    assert candidate(s = "madamimadam") == 25
    assert candidate(s = "levelonelevelonelevel") == 25
    assert candidate(s = "madamracecaramadam") == 35
    assert candidate(s = "aaabbaaabbaaa") == 21
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1
    assert candidate(s = "xylophonepiponolyx") == 9
    assert candidate(s = "racecarandracecar") == 49
    assert candidate(s = "aabaaaabaaba") == 25
    assert candidate(s = "racecarannakayak") == 35
    assert candidate(s = "kayakkayakkayakkayak") == 75
    assert candidate(s = "aaaaabbbbbaaaaa") == 27
    assert candidate(s = "mammadmooommom") == 15
    assert candidate(s = "aaaaabbbbbaaaaaabbbbaaaaa") == 75
    assert candidate(s = "racecarracecar") == 49
    assert candidate(s = "noonnoonnoon") == 1
    assert candidate(s = "repaper") == 5
    assert candidate(s = "racecarlevelrotorkayak") == 35
    assert candidate(s = "rotorrotorrotor") == 25
    assert candidate(s = "aaaaabaaabaaaabaaaaabaaaa") == 99
    assert candidate(s = "ababaababab") == 25
    assert candidate(s = "noonhighnoon") == 1
    assert candidate(s = "tacocattacocattaco") == 49
    assert candidate(s = "rotorrotorrotorrotor") == 75
    assert candidate(s = "bananaananananab") == 45
    assert candidate(s = "zzzyzyzyzyzyzyzyzyzyzyzyz") == 121
    assert candidate(s = "deeddeeddeed") == 1
    assert candidate(s = "aaaaaabbbbbaaaa") == 35
    assert candidate(s = "rotorresistor") == 15
    assert candidate(s = "xylophonelevel") == 5
    assert candidate(s = "aaabaaaabaaaaabaaaaaaab") == 77
    assert candidate(s = "aabbccddeeefffgggzzzzzzzzzzzzzzzzzzzz") == 99
    assert candidate(s = "abcdedcbaabcdedcbaabcdedcba") == 81
    assert candidate(s = "civic") == 3
    assert candidate(s = "rotor") == 3
    assert candidate(s = "qwertyuioplkjhgfdsazxcvbnmnbvcxzasdfghjklpoiuytrewq") == 49
    assert candidate(s = "abbaabbbaabba") == 11
    assert candidate(s = "abcdefghihgfedcba") == 15
    assert candidate(s = "tacocattaco") == 7
    assert candidate(s = "repaperrepaperrepaper") == 49
    assert candidate(s = "aabaaaabaa") == 25
    assert candidate(s = "reviled") == 1
    assert candidate(s = "amoreroma") == 7
    assert candidate(s = "aabbccddeeefffggghhhiiiijjjjkkkkllllmmmnnnooopppqqqqrrrrssssttttuuuuvvvvwwwwwxxxxxyyyyyzzzzzzyyyyyxxxwwvvuuttrrqqppoonnmlkkjjiihhggffeeddccbbaa") == 25
    assert candidate(s = "xyzyzyzyzyzyzyzyz") == 63
    assert candidate(s = "xyxzyzyzyzyzyzyx") == 35
    assert candidate(s = "zzzzzzyyyyyxxxwwvvuuttrrqqppoonnmlkkjjiihhggffeeddccbbaa") == 25
    assert candidate(s = "rotorabcdrotor") == 25
    assert candidate(s = "aabbccddeeeffgghhiii") == 9
    assert candidate(s = "abcdedcbabcdedcbabcdedcb") == 135
    assert candidate(s = "aabbccddeeefffggghhhiiiijjjjkkkkllllmmmnnnooopppqqqqrrrrssssttttuuuuvvvvwwwwwxxxxxyyyyyzzzzz") == 25
    assert candidate(s = "abcabcabcabcabc") == 1
    assert candidate(s = "deed") == 1
    assert candidate(s = "aaaaabbbbbbaaaaa") == 25
    assert candidate(s = "levelwasracecar") == 35
    assert candidate(s = "racecarabcdeedcba") == 9


