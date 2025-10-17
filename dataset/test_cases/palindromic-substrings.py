def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "babad") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babad") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "noon") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noon") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbaa") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbaa") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "level") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "level") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "civic") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "civic") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotor") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotor") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "zxcvbnmmlkjhgfdsapoiuytrewq") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxcvbnmmlkjhgfdsapoiuytrewq") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaabccbaabcba") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaabccbaabcba") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "amoreinimorac") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "amoreinimorac") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "atoyota") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "atoyota") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcccbbbaa") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcccbbbaa") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabcbaabc") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabcbaabc") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorrotor") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorrotor") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelmadam") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelmadam") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "ab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "steponnopets") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "steponnopets") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoon") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoon") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbb") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbb") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaa") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaa") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcddcbaabcddcba") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcddcbaabcddcba") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarracecarracecarracecar") == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarracecarracecarracecar") == 82: {e}')
    
    total += 1
    try:
        result = candidate(s = "madaminnadammadam") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madaminnadammadam") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyzyzyxzyzyxzyzyxzyx") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyzyzyxzyzyxzyzyxzyx") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonabnoon") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonabnoon") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaabbccddeebbaabbccddee") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaabbccddeebbaabbccddee") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopoiuytrewq") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopoiuytrewq") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccba") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccba") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "aba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyzyzyzyzyzyzy") == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyzyzyzyzyzyzy") == 65: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbacbacbacba") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbacbacbacba") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoonnoon") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoonnoon") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeee") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeee") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamracecar") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamracecar") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorcarrot") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorcarrot") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abca") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abca") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcccbbbbaaa") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcccbbbbaaa") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeeeddccbbaa") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeeeddccbbaa") == 47: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbbb") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbbb") == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbabaabbaa") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbabaabbaa") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyxzyxzyzyxzyz") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxzyxzyzyxzyz") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "madaminnakayak") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madaminnakayak") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccbaabccba") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccbaabccba") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccccbbaa") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccccbbaa") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorcentralrotor") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorcentralrotor") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarracecarracecar") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarracecarracecar") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbaaabbbaaa") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbaaabbbaaa") == 37: {e}')
    
    total += 1
    try:
        result = candidate(s = "xxyyyxyxx") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xxyyyxyxx") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggghhhh") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggghhhh") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdfgdcabaabacdfgdcaba") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcabaabacdfgdcaba") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarbanana") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarbanana") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelup") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelup") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcba") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcba") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "deeee") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deeee") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abaaabaaab") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abaaabaaab") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaba") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaba") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaabcbaabcbaabcba") == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaabcbaabcbaabcba") == 58: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbcbcbcbc") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbcbcbcbc") == 56: {e}')
    
    total += 1
    try:
        result = candidate(s = "abaaabbaaabaaa") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abaaabbaaabaaa") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcababcababc") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcababcababc") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "levellevel") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levellevel") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefedcba") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefedcba") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgfedcbafedcbagfedcbafedcbagfedcba") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgfedcbafedcbagfedcbafedcbagfedcba") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "acdcacdcacdc") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acdcacdcacdc") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "zxcvbnmmnbvcxz") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxcvbnmmnbvcxz") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisnotapalindrome") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisnotapalindrome") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaeae") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaeae") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaa") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaa") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "levellevellevel") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levellevellevel") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcbaabcdcba") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcbaabcdcba") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabc") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabc") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyzyxzyzyzyx") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyzyxzyzyzyx") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdfgdcabaabacdfgdcabaabacdfgdcaba") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcabaabacdfgdcabaabacdfgdcaba") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "leveloneeleven") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leveloneeleven") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "babcbabcba") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babcbabcba") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyzzyzzyzyzy") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyzzyzzyzyzy") == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababa") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababa") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyxyzyx") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyxyzyx") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "civicciviccivicciviccivic") == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "civicciviccivicciviccivic") == 85: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 210: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaba") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaba") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbabcba") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbabcba") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "deifiedrotor") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deifiedrotor") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonracecarrace") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonracecarrace") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "civiccivic") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "civiccivic") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccba") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccba") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamimadam") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamimadam") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 78: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarannakayak") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarannakayak") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "amanaplanacanalpanama") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "amanaplanacanalpanama") == 37: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbabababa") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbabababa") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgfeijklmmlkjihgf") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgfeijklmmlkjihgf") == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarracecar") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarracecar") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoon") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoon") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "deified") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deified") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbcb") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbcb") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorrotorrotor") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorrotorrotor") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcba") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcba") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonhighnoon") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonhighnoon") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaabcbaabcba") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaabcbaabcba") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorrotorrotorrotor") == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorrotorrotorrotor") == 58: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdfgdcaba") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcaba") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabba") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabba") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzz") == 141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzz") == 141: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcddcba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcddcba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabaaa") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabaaa") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghihgfedcba") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghihgfedcba") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyxzyzyx") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyxzyzyx") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxxyxyxxyxyxyx") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxxyxyxxyxyxyx") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzyzx") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzyzx") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgfedcbafedcbagfedcba") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgfedcbafedcbagfedcba") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeaabbccddee") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeaabbccddee") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdfgdcababa") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcababa") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "civicciviccivic") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "civicciviccivic") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyxyzyx") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyxyzyx") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbababaabbaba") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbababaabbaba") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyzyxzyzyzyxzyxzyzyzyxzyzyzyzyx") == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyzyxzyzyzyxzyxzyzyzyxzyzyzyzyx") == 61: {e}')
    
    total += 1
    try:
        result = candidate(s = "forgeeksskeegfor") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "forgeeksskeegfor") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaabababa") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaabababa") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzz") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzz") == 66: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abba") == 6
    assert candidate(s = "aaaaa") == 15
    assert candidate(s = "babad") == 7
    assert candidate(s = "noon") == 6
    assert candidate(s = "banana") == 10
    assert candidate(s = "aabbbaa") == 14
    assert candidate(s = "abc") == 3
    assert candidate(s = "level") == 7
    assert candidate(s = "") == 0
    assert candidate(s = "aaa") == 6
    assert candidate(s = "civic") == 7
    assert candidate(s = "rotor") == 7
    assert candidate(s = "racecar") == 10
    assert candidate(s = "a") == 1
    assert candidate(s = "abcdefg") == 7
    assert candidate(s = "zxcvbnmmlkjhgfdsapoiuytrewq") == 28
    assert candidate(s = "abcbaabccbaabcba") == 34
    assert candidate(s = "amoreinimorac") == 14
    assert candidate(s = "atoyota") == 10
    assert candidate(s = "aabbcccbbbaa") == 23
    assert candidate(s = "abccbaabcbaabc") == 28
    assert candidate(s = "rotorrotor") == 19
    assert candidate(s = "abracadabra") == 13
    assert candidate(s = "levelmadam") == 14
    assert candidate(s = "ab") == 2
    assert candidate(s = "steponnopets") == 18
    assert candidate(s = "noonnoon") == 16
    assert candidate(s = "aaaaabbbb") == 25
    assert candidate(s = "aaaaaaaaaa") == 55
    assert candidate(s = "abcddcbaabcddcba") == 32
    assert candidate(s = "racecarracecarracecarracecar") == 82
    assert candidate(s = "madaminnadammadam") == 27
    assert candidate(s = "xyxzyzyzyxzyzyxzyzyxzyx") == 34
    assert candidate(s = "noonabnoon") == 14
    assert candidate(s = "bbaabbccddeebbaabbccddee") == 40
    assert candidate(s = "qwertyuiopoiuytrewq") == 28
    assert candidate(s = "abccbaabccba") == 24
    assert candidate(s = "aba") == 4
    assert candidate(s = "xyzyzyzyzyzyzyzy") == 65
    assert candidate(s = "abacbacbacbacba") == 16
    assert candidate(s = "noonnoonnoonnoon") == 48
    assert candidate(s = "aabbccddeee") == 18
    assert candidate(s = "abacaba") == 12
    assert candidate(s = "madamracecar") == 17
    assert candidate(s = "rotorcarrot") == 14
    assert candidate(s = "abca") == 4
    assert candidate(s = "aabbcccbbbbaaa") == 30
    assert candidate(s = "aabbccddeeeeeddccbbaa") == 47
    assert candidate(s = "aaaaaabbbb") == 31
    assert candidate(s = "aabbabaabbaa") == 23
    assert candidate(s = "abcba") == 7
    assert candidate(s = "abcdcba") == 10
    assert candidate(s = "xyzzyxzyxzyzyxzyz") == 23
    assert candidate(s = "madaminnakayak") == 20
    assert candidate(s = "abccbaabccbaabccba") == 45
    assert candidate(s = "aabbccccbbaa") == 26
    assert candidate(s = "rotorcentralrotor") == 21
    assert candidate(s = "racecarracecarracecar") == 51
    assert candidate(s = "aabbbaaabbbaaa") == 37
    assert candidate(s = "xxyyyxyxx") == 17
    assert candidate(s = "aabbccddeeefffggghhhh") == 40
    assert candidate(s = "abacdfgdcabaabacdfgdcaba") == 33
    assert candidate(s = "racecarbanana") == 20
    assert candidate(s = "levelup") == 9
    assert candidate(s = "abcdeedcba") == 15
    assert candidate(s = "deeee") == 11
    assert candidate(s = "abaaabaaab") == 24
    assert candidate(s = "abbaabbaba") == 20
    assert candidate(s = "abcbaabcbaabcbaabcba") == 58
    assert candidate(s = "bcbcbcbcbcbcbc") == 56
    assert candidate(s = "abaaabbaaabaaa") == 35
    assert candidate(s = "abcababcababc") == 17
    assert candidate(s = "levellevel") == 19
    assert candidate(s = "abcdefedcba") == 16
    assert candidate(s = "abcdefgfedcbafedcbagfedcbafedcbagfedcba") == 45
    assert candidate(s = "acdcacdcacdc") == 27
    assert candidate(s = "zxcvbnmmnbvcxz") == 21
    assert candidate(s = "thisisnotapalindrome") == 23
    assert candidate(s = "abbaeae") == 11
    assert candidate(s = "aaaaaaa") == 28
    assert candidate(s = "levellevellevel") == 36
    assert candidate(s = "abcdcbaabcdcba") == 27
    assert candidate(s = "abccbaabc") == 15
    assert candidate(s = "xyzyzyxzyzyzyx") == 25
    assert candidate(s = "abacdfgdcabaabacdfgdcabaabacdfgdcaba") == 52
    assert candidate(s = "leveloneeleven") == 19
    assert candidate(s = "babcbabcba") == 20
    assert candidate(s = "zyzzyzzyzyzy") == 29
    assert candidate(s = "abababa") == 16
    assert candidate(s = "xyxzyxyzyx") == 15
    assert candidate(s = "abacabadabacaba") == 32
    assert candidate(s = "civicciviccivicciviccivic") == 85
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 210
    assert candidate(s = "abcbaba") == 11
    assert candidate(s = "abcbabcba") == 17
    assert candidate(s = "deifiedrotor") == 17
    assert candidate(s = "noonracecarrace") == 24
    assert candidate(s = "civiccivic") == 19
    assert candidate(s = "aabbccddeeffgg") == 21
    assert candidate(s = "abccba") == 9
    assert candidate(s = "aabbccddeeff") == 18
    assert candidate(s = "madamimadam") == 20
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 78
    assert candidate(s = "racecarannakayak") == 25
    assert candidate(s = "amanaplanacanalpanama") == 37
    assert candidate(s = "abbabababa") == 24
    assert candidate(s = "abcdefgfeijklmmlkjihgf") == 29
    assert candidate(s = "racecarracecar") == 27
    assert candidate(s = "noonnoonnoon") == 30
    assert candidate(s = "deified") == 10
    assert candidate(s = "bcbcbcbcb") == 25
    assert candidate(s = "abcdef") == 6
    assert candidate(s = "rotorrotorrotor") == 36
    assert candidate(s = "abcdedcba") == 13
    assert candidate(s = "noonhighnoon") == 16
    assert candidate(s = "abcbaabcbaabcba") == 36
    assert candidate(s = "rotorrotorrotorrotor") == 58
    assert candidate(s = "abacdfgdcaba") == 14
    assert candidate(s = "abbaabba") == 16
    assert candidate(s = "ababababab") == 30
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzz") == 141
    assert candidate(s = "abcddcba") == 12
    assert candidate(s = "aaaaabaaa") == 25
    assert candidate(s = "abcdefghihgfedcba") == 25
    assert candidate(s = "xyzyxzyzyx") == 14
    assert candidate(s = "xyxxyxyxxyxyxyx") == 40
    assert candidate(s = "xyzzzyzx") == 13
    assert candidate(s = "abcdefgfedcbafedcbagfedcba") == 32
    assert candidate(s = "aabbccddeeaabbccddee") == 30
    assert candidate(s = "abacdfgdcababa") == 19
    assert candidate(s = "civicciviccivic") == 36
    assert candidate(s = "aabbcc") == 9
    assert candidate(s = "mississippi") == 20
    assert candidate(s = "xyzyxyzyx") == 17
    assert candidate(s = "abbababaabbaba") == 28
    assert candidate(s = "xyxzyzyxzyzyzyxzyxzyzyzyxzyzyzyzyx") == 61
    assert candidate(s = "forgeeksskeegfor") == 23
    assert candidate(s = "bananaabababa") == 27
    assert candidate(s = "abcbba") == 8
    assert candidate(s = "zzzzzzzzzzz") == 66


