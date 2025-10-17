def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "pqrspqrspqr") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pqrspqrspqr") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonappa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonappa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "mamad") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mamad") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "dcbccacdb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "dcbccacdb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbccc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbccc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdfgdcaba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcaba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "nnnnaaaaammmm") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nnnnaaaaammmm") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghihgfedcba") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghihgfedcba") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabb") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabb") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "noon") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noon") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxzyxzyx") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxzyxzyx") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "deeee") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deeee") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzazzazz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzazzazz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbabbaaabbaabbbbabbbbaaaabbbaabbabbabbabbababaabaaaabbbaabbabbabbabbababaabaaaabbbbaabbabbabbabbbbaabbabbabbabbbbaabbabbaaabbaabbbbabbbbaaaabbbaabbabbabbabbababaabaaaabbbaabbabbabbabbababaabaaaabbbbaabbabbabbabbbbaabbabbabbabbababaabaaaabbbaabbabbabbabbababaabaaaa") == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbabbaaabbaabbbbabbbbaaaabbbaabbabbabbabbababaabaaaabbbaabbabbabbabbababaabaaaabbbbaabbabbabbabbbbaabbabbabbabbbbaabbabbaaabbaabbbbabbbbaaaabbbaabbabbabbabbababaabaaaabbbaabbabbabbabbababaabaaaabbbbaabbabbabbabbbbaabbabbabbabbababaabaaaabbbaabbabbabbabbababaabaaaa") == 144: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefedcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefedcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccdd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccdd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "level") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "level") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbabab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbabab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzxxzzz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzxxzzz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiii") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiii") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaabaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaabaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffaabbccddeeffaabbccddeeff") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffaabbccddeeffaabbccddeeff") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabaaaabaaaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabaaaabaaaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzyyyyyxxxxxwwwwwvvvvvuuuuutttttssssssrrrrqqqqpppplllloooonnnnmmmmmllllkkkkjjjjihhhhhgggggfffffeeee") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzyyyyyxxxxxwwwwwvvvvvuuuuutttttssssssrrrrqqqqpppplllloooonnnnmmmmmllllkkkkjjjjihhhhhgggggfffffeeee") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabacabacabacabacabacabacabacabacabacabacabacaba") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabacabacabacabacabacabacabacabacabacabacabacaba") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijjiabcdefghij") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijjiabcdefghij") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffggffeeddccbaaabbccddeeffgg") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffggffeeddccbaaabbccddeeffgg") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "deifiedcivicdeified") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deifiedcivicdeified") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoon") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoon") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghihgfedcbaabcdefghihgfedcba") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghihgfedcbaabcdefghihgfedcba") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabad") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabad") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcbe") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcbe") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdeedcbadcb") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdeedcbadcb") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabb") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabb") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcddcbaabcddcbaabcddcba") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcddcbaabcddcbaabcddcba") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdedcabacdedcab") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdedcabacdedcab") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "zxcvbnmlkjihgfedcba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxcvbnmlkjihgfedcba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaabbaabba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaabbaabba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzyzzzzyzzzzyzzzzyzzzzyzzzz") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzyzzzzyzzzzyzzzzyzzzzyzzzz") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeffdcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeffdcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababcbababcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababcbababcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnonopqponomn") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnonopqponomn") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffgghhiiijjjkkklllmmmnnooppqqrrssttuuvvwwxxyyzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffgghhiiijjjkkklllmmmnnooppqqrrssttuuvvwwxxyyzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababab") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababab") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababa") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababa") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaxb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaxb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyx") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyx") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababab") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababab") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "xzyyzxzyyzxzyyz") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xzyyzxzyyzxzyyz") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhii") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhii") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabaaaabaaaabaaaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabaaaabaaaabaaaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeffedcba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeffedcba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcd") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcd") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqponmlkjihgfedcba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqponmlkjihgfedcba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarlevelracecar") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarlevelracecar") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbaaabbbaaabbbaaabbb") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbaaabbbaaabbbaaabbb") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijjihgfedcba") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijjihgfedcba") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcd") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcd") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabacabacab") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabacabacab") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddccbaa") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddccbaa") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdeabcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdeabcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcaabcdccba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcaabcdccba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcbafgfedcba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcbafgfedcba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgfedcba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgfedcba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcbabcdeedcb") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcbabcdeedcb") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababccba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababccba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeaabbccddeeff") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeaabbccddeeff") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzyzzyzzyzzyzzyz") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzyzzyzzyzzyzzyz") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcbafedcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcbafedcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbacbacbacbacbacb") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbacbacbacbacbacb") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgihgfedcbaz") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgihgfedcbaz") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffaabbccddeeff") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffaabbccddeeff") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabad") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabad") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababcbabcbabcbab") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababcbabcbabcbab") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcaaacba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcaaacba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaeabcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaeabcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaabbbaaaabbaaabbbaaaabbaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaabbbaaaabbaaabbbaaaabbaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonhighnoon") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonhighnoon") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijkllkjihgfedcba") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijkllkjihgfedcba") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "zxyzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxz") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxyzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxz") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeffaabbccddeeff") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeffaabbccddeeff") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzyyyyxxxxwwwwvvvuuuutttsssrqqppoonnmmllkkjjiihhggffeeddccbbaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzyyyyxxxxwwwwvvvuuuutttsssrqqppoonnmmllkkjjiihhggffeeddccbbaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababab") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababab") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghihgfedcbaghfedcba") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghihgfedcbaghfedcba") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcddcba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcddcba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyxzyxzyxzyxyzzyx") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxzyxzyxzyxyzzyx") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyxzyzyx") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxzyzyx") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeaabbccddee") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeaabbccddee") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "refercivicrefer") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "refercivicrefer") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvutsrqponmlkjihgfedcbaedcba") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvutsrqponmlkjihgfedcbaedcba") == 18: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "pqrspqrspqr") == 4
    assert candidate(s = "aabbaa") == 4
    assert candidate(s = "abcdcba") == 6
    assert candidate(s = "noonappa") == 4
    assert candidate(s = "abcdedcba") == 8
    assert candidate(s = "abababab") == 6
    assert candidate(s = "mamad") == 2
    assert candidate(s = "dcbccacdb") == 4
    assert candidate(s = "a") == 0
    assert candidate(s = "aabbbccc") == 2
    assert candidate(s = "abacdfgdcaba") == 10
    assert candidate(s = "aa") == 2
    assert candidate(s = "nnnnaaaaammmm") == 2
    assert candidate(s = "racecar") == 6
    assert candidate(s = "abcdefghihgfedcba") == 16
    assert candidate(s = "aabb") == 2
    assert candidate(s = "zzzzzzzzzz") == 2
    assert candidate(s = "noon") == 4
    assert candidate(s = "abcdabcdabcd") == 4
    assert candidate(s = "banana") == 4
    assert candidate(s = "zyxzyxzyx") == 4
    assert candidate(s = "deeee") == 2
    assert candidate(s = "ababa") == 4
    assert candidate(s = "abcabcabb") == 4
    assert candidate(s = "aabbccddeeffgg") == 2
    assert candidate(s = "abccba") == 6
    assert candidate(s = "aaaa") == 2
    assert candidate(s = "aabbccddeeff") == 2
    assert candidate(s = "zzazzazz") == 6
    assert candidate(s = "mississippi") == 4
    assert candidate(s = "abbabbaaabbaabbbbabbbbaaaabbbaabbabbabbabbababaabaaaabbbaabbabbabbabbababaabaaaabbbbaabbabbabbabbbbaabbabbabbabbbbaabbabbaaabbaabbbbabbbbaaaabbbaabbabbabbabbababaabaaaabbbaabbabbabbabbababaabaaaabbbbaabbabbabbabbbbaabbabbabbabbababaabaaaabbbaabbabbabbabbababaabaaaa") == 144
    assert candidate(s = "abcdefedcba") == 10
    assert candidate(s = "zzzzzzzz") == 2
    assert candidate(s = "aabbccdd") == 2
    assert candidate(s = "level") == 4
    assert candidate(s = "bbabab") == 4
    assert candidate(s = "zzzxxzzz") == 4
    assert candidate(s = "abcdefg") == 0
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiii") == 2
    assert candidate(s = "aabaaabaa") == 6
    assert candidate(s = "aabbccddeeffaabbccddeeffaabbccddeeff") == 6
    assert candidate(s = "aaaaabaaaabaaaa") == 6
    assert candidate(s = "zzzzzyyyyyxxxxxwwwwwvvvvvuuuuutttttssssssrrrrqqqqpppplllloooonnnnmmmmmllllkkkkjjjjihhhhhgggggfffffeeee") == 4
    assert candidate(s = "abracadabra") == 6
    assert candidate(s = "abacabacabacabacabacabacabacabacabacabacabacabacaba") == 50
    assert candidate(s = "abcdefghijjiabcdefghij") == 6
    assert candidate(s = "aabbccddeeffggffeeddccbaaabbccddeeffgg") == 14
    assert candidate(s = "deifiedcivicdeified") == 18
    assert candidate(s = "noonnoon") == 6
    assert candidate(s = "abcdefghihgfedcbaabcdefghihgfedcba") == 34
    assert candidate(s = "abacabadabacabad") == 14
    assert candidate(s = "abcdcbe") == 4
    assert candidate(s = "abcdabcdeedcbadcb") == 16
    assert candidate(s = "aabbaabbaabbaabb") == 8
    assert candidate(s = "abcddcbaabcddcbaabcddcba") == 20
    assert candidate(s = "abacdedcabacdedcab") == 16
    assert candidate(s = "zxcvbnmlkjihgfedcba") == 2
    assert candidate(s = "abbaabbaabbaabba") == 10
    assert candidate(s = "zzzzyzzzzyzzzzyzzzzyzzzzyzzzz") == 10
    assert candidate(s = "abcdeffdcba") == 10
    assert candidate(s = "ababcbababcba") == 10
    assert candidate(s = "mnonopqponomn") == 10
    assert candidate(s = "aabbccddeeefffgghhiiijjjkkklllmmmnnooppqqrrssttuuvvwwxxyyzz") == 2
    assert candidate(s = "abababababababab") == 14
    assert candidate(s = "abcdeedcba") == 10
    assert candidate(s = "abababababa") == 10
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 52
    assert candidate(s = "abacaxb") == 4
    assert candidate(s = "xyzzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyxzyzyx") == 40
    assert candidate(s = "ababababababababab") == 16
    assert candidate(s = "abcabcabcabcabcabc") == 10
    assert candidate(s = "xzyyzxzyyzxzyyz") == 12
    assert candidate(s = "aabbccddeeffgghhii") == 2
    assert candidate(s = "aaaaabaaaabaaaabaaaa") == 6
    assert candidate(s = "abcdeffedcba") == 12
    assert candidate(s = "abcdabcdabcdabcd") == 6
    assert candidate(s = "mnopqponmlkjihgfedcba") == 8
    assert candidate(s = "racecarlevelracecar") == 18
    assert candidate(s = "aabbbaaabbbaaabbbaaabbb") == 8
    assert candidate(s = "abcdefghijjihgfedcba") == 20
    assert candidate(s = "abcdabcdabcdabcdabcd") == 8
    assert candidate(s = "abacabacabacab") == 12
    assert candidate(s = "aabbccddccbaa") == 8
    assert candidate(s = "abababababababababab") == 18
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 2
    assert candidate(s = "abacabadabacaba") == 14
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 2
    assert candidate(s = "abcdabcdeabcd") == 4
    assert candidate(s = "abcaabcdccba") == 8
    assert candidate(s = "abcdeedcbafgfedcba") == 12
    assert candidate(s = "abcdefgfedcba") == 12
    assert candidate(s = "abcdeedcbabcdeedcb") == 14
    assert candidate(s = "ababccba") == 6
    assert candidate(s = "aaaabbbbccccddddeeeeaabbccddeeff") == 4
    assert candidate(s = "zzyzzyzzyzzyzzyz") == 10
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 2
    assert candidate(s = "abcdedcbafedcba") == 10
    assert candidate(s = "abacbacbacbacbacbacb") == 12
    assert candidate(s = "abcdefgihgfedcbaz") == 14
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 0
    assert candidate(s = "aabbccddeeffaabbccddeeff") == 4
    assert candidate(s = "abacabadabacabadabacabad") == 22
    assert candidate(s = "ababcbabcbabcbab") == 14
    assert candidate(s = "abcaaacba") == 8
    assert candidate(s = "abcbaeabcba") == 10
    assert candidate(s = "aabbaaabbbaaaabbaaabbbaaaabbaa") == 12
    assert candidate(s = "noonhighnoon") == 8
    assert candidate(s = "abcdefghijkllkjihgfedcba") == 24
    assert candidate(s = "zxyzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxz") == 46
    assert candidate(s = "aabbaabbccddeeffaabbccddeeff") == 6
    assert candidate(s = "zzzzyyyyxxxxwwwwvvvuuuutttsssrqqppoonnmmllkkjjiihhggffeeddccbbaa") == 2
    assert candidate(s = "abababababababababababab") == 22
    assert candidate(s = "abcdefghihgfedcbaghfedcba") == 16
    assert candidate(s = "ababababab") == 8
    assert candidate(s = "abcddcba") == 8
    assert candidate(s = "xyzzyxzyxzyxzyxyzzyx") == 14
    assert candidate(s = "xyzzyxzyzyx") == 8
    assert candidate(s = "aabbccddeeaabbccddee") == 4
    assert candidate(s = "abcabcabcabcabc") == 8
    assert candidate(s = "refercivicrefer") == 14
    assert candidate(s = "mnopqrstuvutsrqponmlkjihgfedcbaedcba") == 18


