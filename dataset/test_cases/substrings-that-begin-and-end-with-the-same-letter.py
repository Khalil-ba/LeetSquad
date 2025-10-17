def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "zxyxzyxzyxz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxyxzyxzyxz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abaacababa") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abaacababa") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabcaabxcaabcxaabcaabc") == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcaabxcaabcxaabcaabc") == 88: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacad") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacad") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaa") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaa") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 78: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyx") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyx") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "rhythms") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rhythms") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzyxwwxyzzzxxzzzywxyz") == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzyxwwxyzzzxxzzzywxyz") == 76: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcd") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcd") == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "madam") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madam") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaxbacab") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaxbacab") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "deified") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deified") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabad") == 111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabad") == 111: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabb") == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabb") == 110: {e}')
    
    total += 1
    try:
        result = candidate(s = "repaper") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repaper") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzz") == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzz") == 125: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaa") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaa") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 820
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 820: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbaabbbaabbbaabbb") == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbaabbbaabbbaabbb") == 114: {e}')
    
    total += 1
    try:
        result = candidate(s = "kayak") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "kayak") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "nootnootnootnootnootnoot") == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nootnootnootnootnootnoot") == 120: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaabbaabba") == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaabbaabba") == 72: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 165: {e}')
    
    total += 1
    try:
        result = candidate(s = "thefactisthatthefactisthat") == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thefactisthatthefactisthat") == 71: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm") == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm") == 78: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzz") == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzz") == 104: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 210: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 220: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabc") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabc") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaa") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaa") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotor") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotor") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaabbaabbaabba") == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaabbaabbaabba") == 110: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzz") == 117
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzz") == 117: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcbaabcdeedcba") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcbaabcdeedcba") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzz") == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzz") == 110: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmnbvcxzlkjhgfdsapoiuytrewq") == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmnbvcxzlkjhgfdsapoiuytrewq") == 76: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 78: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghij") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghij") == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "noon") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noon") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 85: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 165: {e}')
    
    total += 1
    try:
        result = candidate(s = "reviled") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "reviled") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyxzyxzyxzyxzyxzyx") == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxzyxzyxzyxzyxzyx") == 84: {e}')
    
    total += 1
    try:
        result = candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis") == 131
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis") == 131: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 92: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeffedcba") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeffedcba") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "redder") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "redder") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "reviver") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "reviver") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyz") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyz") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "nflibpnflibpnflibp") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nflibpnflibpnflibp") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbccccdddddeeeee") == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbccccdddddeeeee") == 70: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 2346
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 2346: {e}')
    
    total += 1
    try:
        result = candidate(s = "level") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "level") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccbaabccbaabccbaabccba") == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccbaabccbaabccbaabccba") == 165: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarcarcar") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarcarcar") == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "refer") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "refer") == 7: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "zxyxzyxzyxz") == 26
    assert candidate(s = "abcba") == 7
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 26
    assert candidate(s = "abaacababa") == 28
    assert candidate(s = "abababab") == 20
    assert candidate(s = "aaaaa") == 15
    assert candidate(s = "a") == 1
    assert candidate(s = "aabcaabxcaabcxaabcaabc") == 88
    assert candidate(s = "abcabcabc") == 18
    assert candidate(s = "ababababab") == 30
    assert candidate(s = "aaa") == 6
    assert candidate(s = "zzz") == 6
    assert candidate(s = "abba") == 6
    assert candidate(s = "aaaabbbbcccc") == 30
    assert candidate(s = "zzzzzzzzzz") == 55
    assert candidate(s = "banana") == 10
    assert candidate(s = "abacad") == 9
    assert candidate(s = "aaabaaa") == 22
    assert candidate(s = "mississippi") == 24
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 78
    assert candidate(s = "xyzzyx") == 9
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 26
    assert candidate(s = "abcdefg") == 7
    assert candidate(s = "rhythms") == 8
    assert candidate(s = "zzyxwwxyzzzxxzzzywxyz") == 76
    assert candidate(s = "abcdabcdabcdabcdabcd") == 60
    assert candidate(s = "madam") == 7
    assert candidate(s = "abacaxbacab") == 25
    assert candidate(s = "deified") == 10
    assert candidate(s = "abacabadabacabadabacabad") == 111
    assert candidate(s = "aabbaabbaabbaabbaabb") == 110
    assert candidate(s = "repaper") == 10
    assert candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzz") == 125
    assert candidate(s = "aabbaa") == 13
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 820
    assert candidate(s = "aabbbaabbbaabbbaabbb") == 114
    assert candidate(s = "kayak") == 7
    assert candidate(s = "nootnootnootnootnootnoot") == 120
    assert candidate(s = "abacabadabacaba") == 50
    assert candidate(s = "abbaabbaabbaabba") == 72
    assert candidate(s = "abracadabra") == 23
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 165
    assert candidate(s = "thefactisthatthefactisthat") == 71
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm") == 78
    assert candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzz") == 104
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 210
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 220
    assert candidate(s = "abcdabcabc") == 19
    assert candidate(s = "aaaaaaaaaa") == 55
    assert candidate(s = "rotor") == 7
    assert candidate(s = "abbaabbaabbaabbaabba") == 110
    assert candidate(s = "racecar") == 10
    assert candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzz") == 117
    assert candidate(s = "abcdeedcbaabcdeedcba") == 50
    assert candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzz") == 110
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmnbvcxzlkjhgfdsapoiuytrewq") == 76
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 78
    assert candidate(s = "abcdefghijabcdefghijabcdefghij") == 60
    assert candidate(s = "noon") == 6
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 85
    assert candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 165
    assert candidate(s = "reviled") == 8
    assert candidate(s = "xyzzyxzyxzyxzyxzyxzyx") == 84
    assert candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis") == 131
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop") == 46
    assert candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 92
    assert candidate(s = "abcdeffedcba") == 18
    assert candidate(s = "redder") == 9
    assert candidate(s = "reviver") == 10
    assert candidate(s = "xyzxyzxyzxyzxyz") == 45
    assert candidate(s = "nflibpnflibpnflibp") == 36
    assert candidate(s = "abcabcabcabcabc") == 45
    assert candidate(s = "aaaaabbbbbccccdddddeeeee") == 70
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 2346
    assert candidate(s = "level") == 7
    assert candidate(s = "abccbaabccbaabccbaabccbaabccba") == 165
    assert candidate(s = "racecarcarcar") == 31
    assert candidate(s = "refer") == 7


