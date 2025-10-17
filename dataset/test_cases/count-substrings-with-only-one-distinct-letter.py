def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbccdd") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbccdd") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzz") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzz") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbb") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbb") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "aa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzy") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzy") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcd") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcd") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaa") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaa") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzxyzzy") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzxyzzy") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaaaabbb") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaaaabbb") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijjihgfedcba") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijjihgfedcba") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbccc") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbccc") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiii") == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiii") == 90: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggghhhhiiiijjjjkkkkllllmmmmnnnnoooo") == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggghhhhiiiijjjjkkkkllllmmmmnnnnoooo") == 110: {e}')
    
    total += 1
    try:
        result = candidate(s = "qqqqqqqqqqppppppppooonnnnmmmmlllkkkjjjiii") == 141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qqqqqqqqqqppppppppooonnnnmmmmlllkkkjjjiii") == 141: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 5673
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 5673: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaaabaaaabaaaab") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaaabaaaabaaaab") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 990: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggg") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggg") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzz") == 141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzz") == 141: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbbbccccddddeeeeefffffgggggg") == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbbbccccddddeeeeefffffgggggg") == 87: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 220: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggghhhiii") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggghhhiii") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnoooppnnooo") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnoooppnnooo") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccccccba") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccccccba") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 5778
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 5778: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrssrqpomnopqrssrqpomn") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrssrqpomnopqrssrqpomn") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbbcccccccdddddddddeeeeeeeeeeffffffffffggggggggggg") == 262
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbbcccccccdddddddddeeeeeeeeeeffffffffffggggggggggg") == 262: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 53: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbccccccccccccc") == 613
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbccccccccccccc") == 613: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb") == 1959
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb") == 1959: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababababababab") == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababababababab") == 58: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabccddeeeaaa") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabccddeeeaaa") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbbbbcccccccc") == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbbbbcccccccc") == 72: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbccddddeeefff") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbccddddeeefff") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 84: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 8853
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 8853: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaabbbaaaabbbbbaaaa") == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaabbbaaaabbbbbaaaa") == 53: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccccdddddddeeeeeeeeefffffffffgggggggggggggggg") == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccccdddddddeeeeeeeeefffffffffgggggggggggggggg") == 270: {e}')
    
    total += 1
    try:
        result = candidate(s = "lllllllllllllll") == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lllllllllllllll") == 120: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxyxyxyxyxyxyxy") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxyxyxyxyxyxyxy") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 78: {e}')
    
    total += 1
    try:
        result = candidate(s = "ppppqqqqrrrsssss") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ppppqqqqrrrsssss") == 41: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcccddd") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcccddd") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1275: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzyyxxy") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzyyxxy") == 15: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "aabbcc") == 9
    assert candidate(s = "bbccdd") == 9
    assert candidate(s = "zzzzz") == 15
    assert candidate(s = "aaaba") == 8
    assert candidate(s = "abcdabcdabcd") == 12
    assert candidate(s = "ababab") == 6
    assert candidate(s = "zzz") == 6
    assert candidate(s = "ababababab") == 10
    assert candidate(s = "abc") == 3
    assert candidate(s = "aaaaabbbb") == 25
    assert candidate(s = "aa") == 3
    assert candidate(s = "zzzzy") == 11
    assert candidate(s = "abcdabcd") == 8
    assert candidate(s = "aaaaaaaaaa") == 55
    assert candidate(s = "zzzzzxyzzy") == 21
    assert candidate(s = "bbaaaabbb") == 19
    assert candidate(s = "a") == 1
    assert candidate(s = "abcdefghijjihgfedcba") == 21
    assert candidate(s = "aaabbbccc") == 18
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiii") == 90
    assert candidate(s = "aabbccddeeefffggghhhhiiiijjjjkkkkllllmmmmnnnnoooo") == 110
    assert candidate(s = "qqqqqqqqqqppppppppooonnnnmmmmlllkkkjjjiii") == 141
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 26
    assert candidate(s = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 5673
    assert candidate(s = "aaabaaaabaaaabaaaab") == 40
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 990
    assert candidate(s = "abacabadabacaba") == 15
    assert candidate(s = "abcabcabc") == 9
    assert candidate(s = "aabbccddeeefffggg") == 30
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzz") == 141
    assert candidate(s = "abbbbbccccddddeeeeefffffgggggg") == 87
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 220
    assert candidate(s = "abcde") == 5
    assert candidate(s = "aabbccddeeefffggghhhiii") == 42
    assert candidate(s = "mnoooppnnooo") == 20
    assert candidate(s = "abccccccba") == 25
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 5778
    assert candidate(s = "mnopqrssrqpomnopqrssrqpomn") == 28
    assert candidate(s = "aabbbbcccccccdddddddddeeeeeeeeeeffffffffffggggggggggg") == 262
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 53
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbccccccccccccc") == 613
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb") == 1959
    assert candidate(s = "ababababababababababababababababababababababababababababab") == 58
    assert candidate(s = "aabccddeeeaaa") == 22
    assert candidate(s = "aaaaaabbbbbcccccccc") == 72
    assert candidate(s = "aabbbccddddeeefff") == 34
    assert candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 84
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 8853
    assert candidate(s = "aabbaaabbbaaaabbbbbaaaa") == 53
    assert candidate(s = "aabbccccdddddddeeeeeeeeefffffffffgggggggggggggggg") == 270
    assert candidate(s = "lllllllllllllll") == 120
    assert candidate(s = "xyxyxyxyxyxyxyxyxyxyxy") == 22
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 78
    assert candidate(s = "ppppqqqqrrrsssss") == 41
    assert candidate(s = "aabbcccddd") == 18
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1275
    assert candidate(s = "xyzzzyyxxy") == 15


