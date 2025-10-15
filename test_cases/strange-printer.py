def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "pppppppp") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pppppppp") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzy") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzy") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "ppqpqr") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ppqpqr") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabc") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabc") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcd") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcd") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbb") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbb") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzyyyxx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzyyyxx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abca") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abca") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacaba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacaba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababaabababa") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababaabababa") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabad") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabad") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == 43: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzyzxzyzxzyzxzyzxzyzxzyzxzyz") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzyzxzyzxzyzxzyzxzyzxzyzxzyz") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeaabbccddeeaabbcc") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeaabbccddeeaabbcc") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaabbbaaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaabbbaaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghabcdeghijklmno") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghabcdeghijklmno") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbcccccccccccccccccc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbcccccccccccccccccc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeaabbccddeeaabbccddeeaabbcc") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeaabbccddeeaabbccddeeaabbcc") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzyyyzzzzyyy") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzyyyzzzzyyy") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababababababababababababababababababababababa") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababababababababababababababababababababababa") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabad") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabad") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeaabbcc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeaabbcc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzy") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzy") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhii") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhii") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzy") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzy") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeffedcba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeffedcba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeefffffffff") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeefffffffff") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefedcba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefedcba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabb") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabb") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababab") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababab") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcbaedcbaedcba") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcbaedcbaedcba") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababababababababababab") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababababababababababab") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbcccccccccc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbcccccccccc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddfffgggaaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddfffgggaaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbccccccccccccccccccccdddddddddddddddddd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbccccccccccccccccccccdddddddddddddddddd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccba") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccba") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffaabbccddeeffaabbccddeeffaabbccddeeff") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffaabbccddeeffaabbccddeeffaabbccddeeff") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijihgfedcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijihgfedcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeaabbccddeeaabbccddeeee") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeaabbccddeeaabbccddeeee") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabadabacabad") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabadabacabad") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbccccccccccccccccccccddddddddddddddddddaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbcccccccccccccccccc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbccccccccccccccccccccddddddddddddddddddaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbcccccccccccccccccc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzyyxxwvvuuttrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzyyxxwvvuuttrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababab") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababab") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabad") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabad") == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijj") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijj") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabad") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabad") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcaabbcc") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcaabbcc") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabad") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabad") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaab") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaab") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaabcbaabcba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaabcbaabcba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccdddaaabbccccddeee") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccdddaaabbccccddeee") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllll") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllll") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcddcba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcddcba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeffaabb") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeffaabb") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghihgfedcba") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghihgfedcba") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabc") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabc") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabc") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabc") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdbaba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdbaba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyxzyzyxzyzyxzyz") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyxzyzyxzyzyxzyz") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijhgfedcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijhgfedcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababababa") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababababa") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 37: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeaabbcc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeaabbcc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "pppppppp") == 1
    assert candidate(s = "abcba") == 3
    assert candidate(s = "aabbaa") == 2
    assert candidate(s = "zzzzy") == 2
    assert candidate(s = "abababab") == 5
    assert candidate(s = "ppqpqr") == 4
    assert candidate(s = "a") == 1
    assert candidate(s = "abcabcabc") == 7
    assert candidate(s = "aabbc") == 3
    assert candidate(s = "aabaa") == 2
    assert candidate(s = "abcabc") == 5
    assert candidate(s = "abcdabcd") == 7
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 26
    assert candidate(s = "abcdabcdabcd") == 10
    assert candidate(s = "abc") == 3
    assert candidate(s = "abcd") == 4
    assert candidate(s = "aaabbb") == 2
    assert candidate(s = "zzzzyyyxx") == 3
    assert candidate(s = "aabbccddeeff") == 6
    assert candidate(s = "aba") == 2
    assert candidate(s = "aabbcc") == 3
    assert candidate(s = "abacaba") == 4
    assert candidate(s = "abca") == 3
    assert candidate(s = "abacabadabacabadabacaba") == 12
    assert candidate(s = "aabbaabbaabb") == 4
    assert candidate(s = "abababababaabababa") == 9
    assert candidate(s = "abcabcabcabc") == 9
    assert candidate(s = "abacabadabacabadabacabadabacabad") == 17
    assert candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == 43
    assert candidate(s = "zzyzxzyzxzyzxzyzxzyzxzyzxzyz") == 14
    assert candidate(s = "aabbccddeeaabbccddeeaabbcc") == 11
    assert candidate(s = "aabbaaabbbaaa") == 3
    assert candidate(s = "abcdefghabcdeghijklmno") == 21
    assert candidate(s = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbcccccccccccccccccc") == 3
    assert candidate(s = "aabbccddeeaabbccddeeaabbccddeeaabbcc") == 15
    assert candidate(s = "zzzzzyyyzzzzyyy") == 3
    assert candidate(s = "ababababababababababababababababababababababababababababababababababababababababababababa") == 45
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 21
    assert candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 46
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 33
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 26
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 26
    assert candidate(s = "abacabad") == 5
    assert candidate(s = "aaaabbbbccccddddeeeeaabbcc") == 7
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
    assert candidate(s = "abcabcabcabcabcabc") == 13
    assert candidate(s = "zzzzzzzzzzzzzzy") == 2
    assert candidate(s = "aabbccddeeffgghhii") == 9
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzy") == 2
    assert candidate(s = "abcdeffedcba") == 6
    assert candidate(s = "aaaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeefffffffff") == 6
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 1
    assert candidate(s = "abcdefedcba") == 6
    assert candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabb") == 13
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 1
    assert candidate(s = "abababababababababababababab") == 15
    assert candidate(s = "abcdeedcbaedcbaedcba") == 13
    assert candidate(s = "abacabadabacaba") == 8
    assert candidate(s = "abababababababababababababababababababababababab") == 25
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbcccccccccc") == 3
    assert candidate(s = "aaabbbcccdddfffgggaaa") == 6
    assert candidate(s = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbccccccccccccccccccccdddddddddddddddddd") == 4
    assert candidate(s = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccba") == 26
    assert candidate(s = "aabbccddeeffaabbccddeeffaabbccddeeffaabbccddeeff") == 21
    assert candidate(s = "abcdefghijihgfedcba") == 10
    assert candidate(s = "aabbccddeeaabbccddeeaabbccddeeee") == 13
    assert candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 33
    assert candidate(s = "abacabadabacabadabacabadabacabadabacabad") == 21
    assert candidate(s = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbccccccccccccccccccccddddddddddddddddddaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbcccccccccccccccccc") == 6
    assert candidate(s = "zzzyyxxwvvuuttrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == 25
    assert candidate(s = "ababababababababababababab") == 14
    assert candidate(s = "aabbccddeeffgg") == 7
    assert candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabad") == 29
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 26
    assert candidate(s = "aabbccddeeffgghhiijj") == 10
    assert candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabad") == 25
    assert candidate(s = "abcdefg") == 7
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 26
    assert candidate(s = "abcabcabcabcabcabcabcabcaabbcc") == 19
    assert candidate(s = "abacabadabacabadabacabad") == 13
    assert candidate(s = "aaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaab") == 13
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 26
    assert candidate(s = "abcbaabcbaabcba") == 7
    assert candidate(s = "aabbbcccdddaaabbccccddeee") == 8
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllll") == 12
    assert candidate(s = "ababababab") == 6
    assert candidate(s = "abcddcba") == 4
    assert candidate(s = "aabbaabbccddeeffaabb") == 8
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd") == 25
    assert candidate(s = "abcdefghihgfedcba") == 9
    assert candidate(s = "abcabcabcabcabcabcabcabcabc") == 19
    assert candidate(s = "abcabcabcabcabcabcabcabc") == 17
    assert candidate(s = "abcdabcdbaba") == 8
    assert candidate(s = "xyzyxzyzyxzyzyxzyz") == 11
    assert candidate(s = "abcdefghijhgfedcba") == 10
    assert candidate(s = "mississippi") == 5
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
    assert candidate(s = "ababababababababababababababababababababababababababa") == 27
    assert candidate(s = "abcabcabcabcabc") == 11
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 37
    assert candidate(s = "aabbccddeeaabbcc") == 7
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1


