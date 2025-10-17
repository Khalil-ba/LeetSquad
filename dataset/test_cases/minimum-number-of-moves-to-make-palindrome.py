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
        result = candidate(s = "letelt") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "letelt") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "mamad") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mamad") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabb") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabb") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgfedcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgfedcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "noon") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noon") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "deeee") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deeee") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "nnnnn") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nnnnn") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "elvtoelvtoe") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "elvtoelvtoe") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "asflkj") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "asflkj") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abca") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abca") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghgfedcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghgfedcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzyzzyzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzyzzyzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonappa") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonappa") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcbad") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcbad") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaabbaaaaaabbbbaa") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaabbaaaaaabbbbaa") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabb") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabb") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "jlvaj") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "jlvaj") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyzyzyzyx") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyzyzyzyx") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "qpwoeirutoip") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qpwoeirutoip") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbacaba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbacaba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoon") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoon") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbb") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbb") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqponmlkjihgfedcbaaaabbbccc") == 161
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqponmlkjihgfedcbaaaabbbccc") == 161: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffgggggffffeeeeddccbaaabb") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffgggggffffeeeeddccbaaabb") == 37: {e}')
    
    total += 1
    try:
        result = candidate(s = "lplllp") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lplllp") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbbaaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbbaaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddcccbbaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddcccbbaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "mmnmm") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mmnmm") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnvovnm") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnvovnm") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeee") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeee") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyx") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyx") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmmlkjhgfdsapoiuytrewq") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmmlkjhgfdsapoiuytrewq") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabb") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabb") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdddcb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdddcb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdxyzzyxcba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdxyzzyxcba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeeddcbaabbaa") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeeddcbaabbaa") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffgggghhhggggfffeeeedddccbbaa") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffgggghhhggggfffeeeedddccbbaa") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffggggggg") == 204
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffggggggg") == 204: {e}')
    
    total += 1
    try:
        result = candidate(s = "ppqqrrssrqqpp") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ppqqrrssrqqpp") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbb") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbb") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcbaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcbaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffeecdccbbaa") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffeecdccbbaa") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggggffffeeeeddccbaaabb") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggggffffeeeeddccbaaabb") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabad") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabad") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyxzyxzyxzyx") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyxzyxzyxzyx") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbabaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbabaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaabcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaabcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zazbzazbzaz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zazbzazbzaz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeffedcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeffedcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbca") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbca") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefedcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefedcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccdd") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccdd") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "level") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "level") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbb") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbb") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "madam") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madam") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabababaab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabababaab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabccbaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabccbaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeffffgggghhhiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwxxyyzz") == 1192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeffffgggghhhiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwxxyyzz") == 1192: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertewq") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertewq") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertytrewq") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertytrewq") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbad") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbad") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaaccdaabb") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaaccdaabb") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aababbaaabbbbbaaaaa") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aababbaaabbbbbaaaaa") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaaabbaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaaabbaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyzyx") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyzyx") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zxcvbnmlkjhgfdasqwertyuiopoiuytrewqasdfghjklmnbvcxz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxcvbnmlkjhgfdasqwertyuiopoiuytrewqasdfghjklmnbvcxz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbbaaaaaaaaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbbaaaaaaaaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeeddcbbbaa") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeeddcbbbaa") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 650: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbabba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbabba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "mmnnllkkjjiihhggffeeddccbbaa") == 182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mmnnllkkjjiihhggffeeddccbbaa") == 182: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbaaaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbaaaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "nnnmmmnnn") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nnnmmmnnn") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "repaper") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repaper") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdfgdcaba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcaba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffgggfhheeeddccbaa") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffgggfhheeeddccbaa") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxzyzyx") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxzyzyx") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcddcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcddcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotor") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotor") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghihgfedcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghihgfedcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeffggffeeddccbbaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeffggffeeddccbbaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcbaedcba") == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcbaedcba") == 115: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeffffgggghhhiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz") == 1311
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeffffgggghhhiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz") == 1311: {e}')
    
    total += 1
    try:
        result = candidate(s = "levellol") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levellol") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeffgfedcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeffgfedcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeedcbaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeedcbaa") == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abcba") == 0
    assert candidate(s = "letelt") == 2
    assert candidate(s = "abcdcba") == 0
    assert candidate(s = "aabbaa") == 0
    assert candidate(s = "abcdedcba") == 0
    assert candidate(s = "mamad") == 3
    assert candidate(s = "aabbc") == 4
    assert candidate(s = "aabb") == 2
    assert candidate(s = "racecar") == 0
    assert candidate(s = "abcdefgfedcba") == 0
    assert candidate(s = "noon") == 0
    assert candidate(s = "deeee") == 2
    assert candidate(s = "nnnnn") == 0
    assert candidate(s = "aabbcc") == 6
    assert candidate(s = "elvtoelvtoe") == 6
    assert candidate(s = "aabbab") == 3
    assert candidate(s = "asflkj") == 5
    assert candidate(s = "abca") == 1
    assert candidate(s = "abcdefghgfedcba") == 0
    assert candidate(s = "zzzyzzyzz") == 1
    assert candidate(s = "noonappa") == 8
    assert candidate(s = "abcdcbad") == 3
    assert candidate(s = "aabaaabbaaaaaabbbbaa") == 11
    assert candidate(s = "aabbaabbaabb") == 6
    assert candidate(s = "jlvaj") == 1
    assert candidate(s = "xyzyzyzyzyx") == 0
    assert candidate(s = "qpwoeirutoip") == 12
    assert candidate(s = "abbbacaba") == 3
    assert candidate(s = "abcabcabcabc") == 6
    assert candidate(s = "noonnoon") == 0
    assert candidate(s = "aaaaabbbb") == 10
    assert candidate(s = "mnopqponmlkjihgfedcbaaaabbbccc") == 161
    assert candidate(s = "aabbccddeeefffgggggffffeeeeddccbaaabb") == 37
    assert candidate(s = "lplllp") == 1
    assert candidate(s = "aabbbbaaa") == 2
    assert candidate(s = "aaabbbcccdddcccbbaaa") == 5
    assert candidate(s = "mmnmm") == 0
    assert candidate(s = "mnvovnm") == 0
    assert candidate(s = "aabbccddeee") == 24
    assert candidate(s = "xyzzyx") == 0
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmmlkjhgfdsapoiuytrewq") == 9
    assert candidate(s = "aabbaabbaabbaabb") == 8
    assert candidate(s = "abcdddcb") == 4
    assert candidate(s = "abcdxyzzyxcba") == 3
    assert candidate(s = "aabbccddeeeeddcbaabbaa") == 22
    assert candidate(s = "aabbccddeeefffgggghhhggggfffeeeedddccbbaa") == 20
    assert candidate(s = "aaaabbbbccccddddeeeeffffggggggg") == 204
    assert candidate(s = "ppqqrrssrqqpp") == 1
    assert candidate(s = "aaabbbb") == 6
    assert candidate(s = "abcdedcbaa") == 4
    assert candidate(s = "aabbccddeeffeecdccbbaa") == 7
    assert candidate(s = "aabbccddeeefffggggffffeeeeddccbaaabb") == 38
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 0
    assert candidate(s = "abcdeedcba") == 0
    assert candidate(s = "abacabad") == 4
    assert candidate(s = "xyzyxzyxzyxzyx") == 2
    assert candidate(s = "aaabbbaaa") == 0
    assert candidate(s = "aabbabaa") == 1
    assert candidate(s = "abcbaabcba") == 0
    assert candidate(s = "zazbzazbzaz") == 0
    assert candidate(s = "abcdeffedcba") == 0
    assert candidate(s = "abcbca") == 1
    assert candidate(s = "abcdefedcba") == 0
    assert candidate(s = "aabbccdd") == 12
    assert candidate(s = "level") == 0
    assert candidate(s = "abcabcba") == 1
    assert candidate(s = "aaaabbbb") == 8
    assert candidate(s = "madam") == 0
    assert candidate(s = "aabababaab") == 3
    assert candidate(s = "aabccbaa") == 0
    assert candidate(s = "abacabadabacaba") == 0
    assert candidate(s = "aabbccddeeeffffgggghhhiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwxxyyzz") == 1192
    assert candidate(s = "qwertewq") == 1
    assert candidate(s = "qwertytrewq") == 0
    assert candidate(s = "abcbad") == 3
    assert candidate(s = "abbaaccdaabb") == 5
    assert candidate(s = "aababbaaabbbbbaaaaa") == 8
    assert candidate(s = "aabaaa") == 1
    assert candidate(s = "aaabaaaabbaa") == 4
    assert candidate(s = "xyzyzyx") == 0
    assert candidate(s = "abccba") == 0
    assert candidate(s = "zxcvbnmlkjhgfdasqwertyuiopoiuytrewqasdfghjklmnbvcxz") == 1
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbbaaaaaaaaa") == 6
    assert candidate(s = "aabbccddeeeeddcbbbaa") == 10
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 650
    assert candidate(s = "aabbabba") == 2
    assert candidate(s = "mmnnllkkjjiihhggffeeddccbbaa") == 182
    assert candidate(s = "aaaaabbbaaaa") == 2
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 25
    assert candidate(s = "nnnmmmnnn") == 0
    assert candidate(s = "repaper") == 0
    assert candidate(s = "abacdfgdcaba") == 1
    assert candidate(s = "aabbccddeeefffgggfhheeeddccbaa") == 22
    assert candidate(s = "abbaabba") == 0
    assert candidate(s = "zyxzyzyx") == 4
    assert candidate(s = "abcddcba") == 0
    assert candidate(s = "rotor") == 0
    assert candidate(s = "abcdefghihgfedcba") == 0
    assert candidate(s = "aabbccddeeeffggffeeddccbbaa") == 3
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcbaedcba") == 115
    assert candidate(s = "aabbccddeeeffffgggghhhiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz") == 1311
    assert candidate(s = "levellol") == 6
    assert candidate(s = "mississippi") == 13
    assert candidate(s = "abcdeffgfedcba") == 1
    assert candidate(s = "aabbccddeedcbaa") == 6


