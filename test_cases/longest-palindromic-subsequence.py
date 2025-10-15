def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abcba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcba") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcba") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonhighnoon") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonhighnoon") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "cbbd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cbbd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "ab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcb") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcb") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "noon") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noon") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "deeee") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deeee") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "agbdba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "agbdba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "character") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "character") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "level") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "level") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabcdefggfedcbagfedcba") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcdefggfedcbagfedcba") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonappa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonappa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aacaagttaccagtcacaagttaacaagttaccagtcacaagttaac") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aacaagttaccagtcacaagttaacaagttaccagtcacaagttaac") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbdbba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbdbba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelmadam") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelmadam") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaababa") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaababa") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdaedcba") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdaedcba") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "babbbabbbbabbb") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babbbabbbbabbb") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "tattarrattat") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "tattarrattat") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabaaaa") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabaaaa") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoon") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoon") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = ('elrmenmet',)) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = ('elrmenmet',)) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeaabbccddeeff") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeaabbccddeeff") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamracecar") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamracecar") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "nogood") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nogood") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcbazxyzyxcba") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcbazxyzyxcba") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "epelppel") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "epelppel") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaabbabaaabbbaabaa") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaabbabaaabbbaabaa") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdaabcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdaabcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zazalxlkjlkjlkjljlkjljlkjlkjljlkjljlkjljlkjljlkjljlkjljlkjljlkjlkjljlkjljlkjljlkjljlkjljlkjlkjljlkjljlkjljlkjl") == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zazalxlkjlkjlkjljlkjljlkjlkjljlkjljlkjljlkjljlkjljlkjljlkjljlkjlkjljlkjljlkjljlkjljlkjljlkjlkjljlkjljlkjljlkjl") == 81: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabcba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabcba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabacbebebe") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabacbebebe") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "kayak") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "kayak") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorotor") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorotor") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxzyxzyxzyxzyx") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxzyxzyxzyxzyx") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "elkfaodfnofowefwaefewfafwefawfawfawfawfawfawfawfawfawfawfaw") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "elkfaodfnofowefwaefewfafwefawfawfawfawfawfawfawfawfawfawfaw") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefggfedcba") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefggfedcba") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "attacking") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "attacking") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "nursesrun") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nursesrun") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccdd") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccdd") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "aibohphobia") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aibohphobia") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcaebcabcbcabcbc") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcaebcabcbcabcbc") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "deeeeved") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deeeeved") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "madam") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madam") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababa") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababa") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "radar") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "radar") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "pwwkew") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pwwkew") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeffggghhhhiiii") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeffggghhhhiiii") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc") == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc") == 109: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghikjlmnopqrstuvwxyz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghikjlmnopqrstuvwxyz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabcdedcbazyx") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabcdedcbazyx") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabcbab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcbab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcadacaabc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcadacaabc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "anana") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "anana") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbabbaaabbabbaaabbabbaaabbabba") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbabbaaabbabbaaabbabbaaabbabba") == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyxzyxzyxzyxzyx") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyxzyxzyxzyxzyx") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaaabaaabaaaba") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaaabaaabaaaba") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "longestpalindromicsubsequence") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longestpalindromicsubsequence") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "zxcvbnnbvxcz") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxcvbnnbvxcz") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarannakayak") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarannakayak") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghgfedcba") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghgfedcba") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghiijkmlkjihgfedcba") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghiijkmlkjihgfedcba") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "mimimum") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mimimum") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aannnaaaa") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aannnaaaa") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "repaper") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repaper") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "mamadmim") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mamadmim") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "mamad") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mamad") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdfgdcaba") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcaba") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcddcba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcddcba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "civic") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "civic") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotor") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotor") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghihgfedcba") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghihgfedcba") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "intersubjective") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "intersubjective") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "lrfipxxl") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lrfipxxl") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "madaminnadamsandnoon") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madaminnadamsandnoon") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "forgeeksskeegfor") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "forgeeksskeegfor") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbccccc") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbccccc") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "refer") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "refer") == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abcba") == 5
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 1
    assert candidate(s = "abcdcba") == 7
    assert candidate(s = "abcdedcba") == 9
    assert candidate(s = "noonhighnoon") == 11
    assert candidate(s = "a") == 1
    assert candidate(s = "cbbd") == 2
    assert candidate(s = "ab") == 1
    assert candidate(s = "aabaa") == 5
    assert candidate(s = "abcde") == 1
    assert candidate(s = "racecar") == 7
    assert candidate(s = "abcb") == 3
    assert candidate(s = "bcbab") == 3
    assert candidate(s = "noon") == 4
    assert candidate(s = "banana") == 5
    assert candidate(s = "deeee") == 4
    assert candidate(s = "agbdba") == 5
    assert candidate(s = "abccba") == 6
    assert candidate(s = "aaaa") == 4
    assert candidate(s = "character") == 5
    assert candidate(s = "level") == 5
    assert candidate(s = "bbbab") == 4
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 1
    assert candidate(s = "abcdefg") == 1
    assert candidate(s = "aabcdefggfedcbagfedcba") == 16
    assert candidate(s = "noonappa") == 4
    assert candidate(s = "aacaagttaccagtcacaagttaacaagttaccagtcacaagttaac") == 33
    assert candidate(s = "abbdbba") == 7
    assert candidate(s = "abracadabra") == 7
    assert candidate(s = "abcabcabcabc") == 7
    assert candidate(s = "levelmadam") == 5
    assert candidate(s = "abbaababa") == 8
    assert candidate(s = "abcdaedcba") == 9
    assert candidate(s = "babbbabbbbabbb") == 12
    assert candidate(s = "tattarrattat") == 12
    assert candidate(s = "aaaabaaaa") == 9
    assert candidate(s = "noonnoon") == 8
    assert candidate(s = "abccbaabccba") == 12
    assert candidate(s = ('elrmenmet',)) == 1
    assert candidate(s = "aabbccddeeaabbccddeeff") == 6
    assert candidate(s = "madamracecar") == 7
    assert candidate(s = "nogood") == 3
    assert candidate(s = "abcdcbazxyzyxcba") == 11
    assert candidate(s = "epelppel") == 5
    assert candidate(s = "aabaaabbabaaabbbaabaa") == 19
    assert candidate(s = "abcdaabcd") == 4
    assert candidate(s = "zazalxlkjlkjlkjljlkjljlkjlkjljlkjljlkjljlkjljlkjljlkjljlkjljlkjlkjljlkjljlkjljlkjljlkjljlkjlkjljlkjljlkjljlkjl") == 81
    assert candidate(s = "xyzabcba") == 5
    assert candidate(s = "aabacbebebe") == 5
    assert candidate(s = "kayak") == 5
    assert candidate(s = "rotorotor") == 9
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 52
    assert candidate(s = "zyxzyxzyxzyxzyx") == 9
    assert candidate(s = "elkfaodfnofowefwaefewfafwefawfawfawfawfawfawfawfawfawfawfaw") == 35
    assert candidate(s = "abcdefggfedcba") == 14
    assert candidate(s = "attacking") == 4
    assert candidate(s = "nursesrun") == 9
    assert candidate(s = "aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccdd") == 26
    assert candidate(s = "aibohphobia") == 11
    assert candidate(s = "abcaebcabcbcabcbc") == 11
    assert candidate(s = "deeeeved") == 7
    assert candidate(s = "madam") == 5
    assert candidate(s = "ababababababa") == 13
    assert candidate(s = "radar") == 5
    assert candidate(s = "pwwkew") == 3
    assert candidate(s = "aabbccddeeeffggghhhhiiii") == 4
    assert candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc") == 109
    assert candidate(s = "abcdefghikjlmnopqrstuvwxyz") == 1
    assert candidate(s = "xyzabcdedcbazyx") == 15
    assert candidate(s = "aabcbab") == 5
    assert candidate(s = "abcadacaabc") == 7
    assert candidate(s = "aabaaa") == 5
    assert candidate(s = "anana") == 5
    assert candidate(s = "aabbabbaaabbabbaaabbabbaaabbabba") == 31
    assert candidate(s = "aabbccddeeffgg") == 2
    assert candidate(s = "xyzyxzyxzyxzyxzyx") == 13
    assert candidate(s = "aabaaaabaaabaaaba") == 15
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 2
    assert candidate(s = "longestpalindromicsubsequence") == 9
    assert candidate(s = "zxcvbnnbvxcz") == 10
    assert candidate(s = "racecarannakayak") == 8
    assert candidate(s = "abcdefghgfedcba") == 15
    assert candidate(s = "abcdefghiijkmlkjihgfedcba") == 23
    assert candidate(s = "mimimum") == 5
    assert candidate(s = "aannnaaaa") == 7
    assert candidate(s = "repaper") == 7
    assert candidate(s = "mamadmim") == 5
    assert candidate(s = "mamad") == 3
    assert candidate(s = "abacdfgdcaba") == 11
    assert candidate(s = "abcddcba") == 8
    assert candidate(s = "civic") == 5
    assert candidate(s = "rotor") == 5
    assert candidate(s = "abcdefghihgfedcba") == 17
    assert candidate(s = "intersubjective") == 7
    assert candidate(s = "lrfipxxl") == 4
    assert candidate(s = "mississippi") == 7
    assert candidate(s = "madaminnadamsandnoon") == 10
    assert candidate(s = "forgeeksskeegfor") == 12
    assert candidate(s = "aaaaabbbbbccccc") == 5
    assert candidate(s = "refer") == 5


