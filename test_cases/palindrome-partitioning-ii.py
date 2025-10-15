def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "ab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoon") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoon") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabb") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabb") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbm") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbm") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "leet") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leet") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababcbabcba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababcbabcba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdcbaabcdeedcba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdcbaabcdeedcba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdfgdcabaedcba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcabaedcba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabcbabcbabcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcbabcbabcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abaaabaaabaaab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abaaabaaabaaab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcbaeedcba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcbaeedcba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "acbbccaaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acbbccaaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbb") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbb") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaabaaabaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaabaaabaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdbacabcbaabcbaabcba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdbacabcbaabcbaabcba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbababaabbaabb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbababaabbaabb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdbacabcbaab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdbacabcbaab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabaaaabaaabaaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabaaaabaaabaaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdbacabcbaabcbaabcbaabcbaabcba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdbacabcbaabcbaabcbaabcbaabcba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdcbaabcdeedcbaabcdeedcba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdcbaabcdeedcbaabcdeedcba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabaaaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabaaaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonmoonnoon") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonmoonnoon") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabacaba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabacaba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbb") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbb") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbabbabbbabbabbbabbabbbabbbabbb") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbabbabbbabbabbbabbabbbabbbabbb") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbabbabba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbabbabba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoonnoon") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoonnoon") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcbe") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcbe") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababbbababbbaba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababbbababbbaba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamracecar") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamracecar") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbac") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbac") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcbafedcbabcd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcbafedcbabcd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabb") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabb") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbabbabbbabbabbbabbabbb") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbabbabbbabbabbbabbabbb") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaababcba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaababcba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbabbaabbabba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbabbaabbabba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacaba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacaba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcbaefghfeabcdcba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcbaefghfeabcdcba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarabcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarabcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyxzyxyzyx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyxzyxyzyx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeffffggg") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeffffggg") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelup") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelup") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "noon") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noon") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyzyxzyxzyx") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyzyxzyxzyx") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "deeee") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deeee") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaabcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaabcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyxzyzyxzyx") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyxzyzyxzyx") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcbaabcdeedcbaabcdeedcbaabcdeedcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcbaabcdeedcbaabcdeedcbaabcdeedcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxxyzyxyzyx") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxxyzyxyzyx") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcd") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcd") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "level") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "level") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaabananabana") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaabananabana") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghiijihgfedcba") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghiijihgfedcba") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaabaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaabaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdbacabcbaabcbaabcbaabcbaab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdbacabcbaabcbaabcbaabcbaab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcd") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcd") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "madam") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madam") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababcba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababcba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorcarcarecat") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorcarcarecat") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggg") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggg") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababbabaababbabaababbab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababbabaababbabaababbab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdbacabcbaabcbaabcbaabcba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdbacabcbaabcbaabcbaabcba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbabbabb") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbabbabb") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbabbbbabb") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbabbbbabb") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbabcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbabcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbddcba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbddcba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaeabcdedcba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaeabcdedcba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbabcbabcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbabcbabcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbabbc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbabbc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "anana") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "anana") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aababababababababababababababababababababababababababababababababababababab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aababababababababababababababababababababababababababababababababababababab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbacdcba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbacdcba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abaca") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abaca") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdbacaba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdbacaba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamimadam") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamimadam") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaabcbaabcbaabcbaabcbaabcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaabcbaabcbaabcbaabcbaabcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbabba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbabba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaabananabananaabananabanana") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaabananabananaabananabanana") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffgggbbb") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffgggbbb") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdbacabcbaabcbaab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdbacabcbaabcbaab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarannakayak") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarannakayak") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "amanaplanacanalpanama") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "amanaplanacanalpanama") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonracecar") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonracecar") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoon") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoon") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdbacabcba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdbacabcba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonmoonnoonnoonnoonnoonnoon") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonmoonnoonnoonnoonnoonnoon") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcbabacdcba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcbabacdcba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "mamad") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mamad") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbccccccccc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbccccccccc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgfedcbamnoponmabcdedcba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgfedcbamnoponmabcdedcba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonhighnoon") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonhighnoon") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarlevelmadamracecar") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarlevelmadamracecar") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdfgdcaba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcaba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaabbaabbaabb") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaabbaabbaabb") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabcde") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabcde") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcbaabcdedcbaabcdedcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcbaabcdedcbaabcdedcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdbacabcbaabcba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdbacabcbaabcba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotor") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotor") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcadacbdb") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcadacbdb") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzazxzyx") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzazxzyx") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabc") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabc") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababbbababbbababb") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababbbababbbababb") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefff") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefff") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdbacabcbaabcbaabcbaab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdbacabcbaabcbaabcbaab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcbabcdcbabcdcbabcdcb") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcbabcdcbabcdcbabcdcb") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggghhhhiiiii") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggghhhhiiiii") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdcaba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdcaba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbccccc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbccccc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbababab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbababab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyzyx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyzyx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbab") == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abcba") == 0
    assert candidate(s = "aabbaa") == 0
    assert candidate(s = "abcdcba") == 0
    assert candidate(s = "abababab") == 1
    assert candidate(s = "a") == 0
    assert candidate(s = "ab") == 1
    assert candidate(s = "noonnoon") == 0
    assert candidate(s = "aabaa") == 0
    assert candidate(s = "aabb") == 1
    assert candidate(s = "racecar") == 0
    assert candidate(s = "abba") == 0
    assert candidate(s = "abcdabcdabcd") == 11
    assert candidate(s = "abc") == 2
    assert candidate(s = "abcd") == 3
    assert candidate(s = "abccba") == 0
    assert candidate(s = "aab") == 1
    assert candidate(s = "abcbm") == 2
    assert candidate(s = "aabbcc") == 2
    assert candidate(s = "mississippi") == 3
    assert candidate(s = "leet") == 2
    assert candidate(s = "abcdefg") == 6
    assert candidate(s = "ababcbabcba") == 2
    assert candidate(s = "abacdcbaabcdeedcba") == 4
    assert candidate(s = "abacdfgdcabaedcba") == 12
    assert candidate(s = "aabcbabcbabcba") == 1
    assert candidate(s = "abaaabaaabaaab") == 1
    assert candidate(s = "abcabcabcabc") == 11
    assert candidate(s = "abcdeedcbaeedcba") == 5
    assert candidate(s = "acbbccaaa") == 3
    assert candidate(s = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbb") == 1
    assert candidate(s = "aabaaabaaabaaa") == 1
    assert candidate(s = "abacdbacabcbaabcbaabcba") == 6
    assert candidate(s = "aabbababaabbaabb") == 4
    assert candidate(s = "abacdbacabcbaab") == 5
    assert candidate(s = "abacba") == 3
    assert candidate(s = "aaaaabaaaabaaabaaa") == 2
    assert candidate(s = "abacdbacabcbaabcbaabcbaabcbaabcba") == 6
    assert candidate(s = "abacdcbaabcdeedcbaabcdeedcba") == 4
    assert candidate(s = "aaaabaaaaa") == 1
    assert candidate(s = "noonmoonnoon") == 3
    assert candidate(s = "abccbaabccba") == 0
    assert candidate(s = "abacabacaba") == 0
    assert candidate(s = "aaaaabbbbb") == 1
    assert candidate(s = "abbbabbabbbabbabbbabbabbbabbbabbb") == 1
    assert candidate(s = "abbaabbabbabba") == 1
    assert candidate(s = "noonnoonnoonnoon") == 0
    assert candidate(s = "abcdcbe") == 2
    assert candidate(s = "ababbbababbbaba") == 0
    assert candidate(s = "abacaba") == 0
    assert candidate(s = "madamracecar") == 1
    assert candidate(s = "abcbac") == 1
    assert candidate(s = "abcdedcbafedcbabcd") == 3
    assert candidate(s = "aaaabaaa") == 1
    assert candidate(s = "aabbaabbaabbaabb") == 1
    assert candidate(s = "abbbabbabbbabbabbbabbabbb") == 1
    assert candidate(s = "abcbaababcba") == 3
    assert candidate(s = "abbabbaabbabba") == 0
    assert candidate(s = "abacabadabacabadabacabadabacaba") == 0
    assert candidate(s = "abab") == 1
    assert candidate(s = "abcdcbaefghfeabcdcba") == 7
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
    assert candidate(s = "racecarabcba") == 1
    assert candidate(s = "xyzyxzyxyzyx") == 3
    assert candidate(s = "aabbccddeeeffffggg") == 6
    assert candidate(s = "levelup") == 2
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 0
    assert candidate(s = "abababababababab") == 1
    assert candidate(s = "abcdeedcba") == 0
    assert candidate(s = "ababababababab") == 1
    assert candidate(s = "noon") == 0
    assert candidate(s = "aaaaaa") == 0
    assert candidate(s = "xyxzyzyxzyxzyx") == 9
    assert candidate(s = "abababababab") == 1
    assert candidate(s = "deeee") == 1
    assert candidate(s = "abcbaabcba") == 0
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0
    assert candidate(s = "xyzyxzyzyxzyx") == 6
    assert candidate(s = "abcdeedcbaabcdeedcbaabcdeedcbaabcdeedcba") == 0
    assert candidate(s = "zyxxyzyxyzyx") == 2
    assert candidate(s = "abcdabcdabcdabcd") == 15
    assert candidate(s = "level") == 0
    assert candidate(s = "bananaabananabana") == 4
    assert candidate(s = "abcdefghiijihgfedcba") == 17
    assert candidate(s = "aabaabaaa") == 1
    assert candidate(s = "abacdbacabcbaabcbaabcbaabcbaab") == 5
    assert candidate(s = "abcdabcdabcdabcdabcd") == 19
    assert candidate(s = "madam") == 0
    assert candidate(s = "abbbba") == 0
    assert candidate(s = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaa") == 0
    assert candidate(s = "ababababcba") == 2
    assert candidate(s = "rotorcarcarecat") == 10
    assert candidate(s = "abacabadabacaba") == 0
    assert candidate(s = "abababa") == 0
    assert candidate(s = "aabbccddeeefffggg") == 6
    assert candidate(s = "ababbabaababbabaababbab") == 1
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 0
    assert candidate(s = "abacdbacabcbaabcbaabcbaabcba") == 6
    assert candidate(s = "abbabbabb") == 1
    assert candidate(s = "abbbabbbbabb") == 2
    assert candidate(s = "abcbabcba") == 0
    assert candidate(s = "banana") == 1
    assert candidate(s = "abcbddcba") == 5
    assert candidate(s = "abcbaeabcdedcba") == 2
    assert candidate(s = "abcbabcbabcba") == 0
    assert candidate(s = "bcbabbc") == 3
    assert candidate(s = "ababababababababababababab") == 1
    assert candidate(s = "anana") == 0
    assert candidate(s = "aababababababababababababababababababababababababababababababababababababab") == 1
    assert candidate(s = "aabbccddeeffgg") == 6
    assert candidate(s = "abbacdcba") == 3
    assert candidate(s = "aabbccddeeff") == 5
    assert candidate(s = "abaca") == 2
    assert candidate(s = "abacdbacaba") == 4
    assert candidate(s = "madamimadam") == 0
    assert candidate(s = "abcdefghij") == 9
    assert candidate(s = "abcbaabcbaabcbaabcbaabcbaabcba") == 0
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 25
    assert candidate(s = "aabbabba") == 1
    assert candidate(s = "bananaabananabananaabananabanana") == 6
    assert candidate(s = "aabbccddeeefffgggbbb") == 7
    assert candidate(s = "abacdbacabcbaabcbaab") == 5
    assert candidate(s = "racecarannakayak") == 2
    assert candidate(s = "amanaplanacanalpanama") == 0
    assert candidate(s = "aaaaaaaaaaaaaaaaaab") == 1
    assert candidate(s = "noonracecar") == 1
    assert candidate(s = "noonnoonnoon") == 0
    assert candidate(s = "abacdbacabcba") == 6
    assert candidate(s = "noonmoonnoonnoonnoonnoonnoon") == 3
    assert candidate(s = "abcdedcba") == 0
    assert candidate(s = "abcdeedcbabacdcba") == 5
    assert candidate(s = "mamad") == 2
    assert candidate(s = "aaaaaaaaaabbbbbbbbbccccccccc") == 2
    assert candidate(s = "abcdefgfedcbamnoponmabcdedcba") == 2
    assert candidate(s = "noonhighnoon") == 5
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0
    assert candidate(s = "racecarlevelmadamracecar") == 3
    assert candidate(s = "abacdfgdcaba") == 7
    assert candidate(s = "aabaaabbaabbaabb") == 2
    assert candidate(s = "abcdabcabcde") == 11
    assert candidate(s = "ababababab") == 1
    assert candidate(s = "abcdedcbaabcdedcbaabcdedcba") == 0
    assert candidate(s = "abacdbacabcbaabcba") == 6
    assert candidate(s = "rotor") == 0
    assert candidate(s = "abcadacbdb") == 3
    assert candidate(s = "xyzzazxzyx") == 6
    assert candidate(s = "aabba") == 1
    assert candidate(s = "abcabcabcabcabcabcabcabc") == 23
    assert candidate(s = "ababbbababbbababb") == 1
    assert candidate(s = "aabbccddeeefff") == 5
    assert candidate(s = "abacdbacabcbaabcbaabcbaab") == 5
    assert candidate(s = "abcdcbabcdcbabcdcbabcdcb") == 1
    assert candidate(s = "aabbccddeeefffggghhhhiiiii") == 8
    assert candidate(s = "abcabcabcabcabc") == 14
    assert candidate(s = "abacdcaba") == 0
    assert candidate(s = "aaaaabbbbbccccc") == 2
    assert candidate(s = "aabbababab") == 2
    assert candidate(s = "xyxzyzyx") == 3
    assert candidate(s = "abbab") == 1


