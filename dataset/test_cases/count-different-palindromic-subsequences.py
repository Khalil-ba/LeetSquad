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
        result = candidate(s = "abccba") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccba") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abac") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abac") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba") == 104860361
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba") == 104860361: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaa") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaa") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd") == 29348
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd") == 29348: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcddcba") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcddcba") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "bccb") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bccb") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacaba") == 2571
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacaba") == 2571: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababbabaabbababbab") == 212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababbabaabbababbab") == 212: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabb") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabb") == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccaaaabbbbccccaaaabbbbcccc") == 996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccaaaabbbbccccaaaabbbbcccc") == 996: {e}')
    
    total += 1
    try:
        result = candidate(s = "ddccbbbaaacccbdd") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ddccbbbaaacccbdd") == 94: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == 84: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbccccddddaaaaabbbbbccccddddaaaaabbbbbccccddddaaaaabbbbbccccddddaaaaabbbbbccccddddaaaaabbbbbccccddddaaaaabbbbbccccdddd") == 127372410
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbccccddddaaaaabbbbbccccddddaaaaabbbbbccccddddaaaaabbbbbccccddddaaaaabbbbbccccddddaaaaabbbbbccccddddaaaaabbbbbccccdddd") == 127372410: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcddcbaabcddcba") == 340
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcddcbaabcddcba") == 340: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd") == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd") == 72: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababab") == 8358
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababab") == 8358: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddaaaabbbbccccdddd") == 224
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddaaaabbbbccccdddd") == 224: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 450061485
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 450061485: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbaaaaabbbbaaaaabbbbaaaaabbbbaaaaabbbbaaaaabbbbaaaa") == 61293
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbaaaaabbbbaaaaabbbbaaaaabbbbaaaaabbbbaaaaabbbbaaaa") == 61293: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcba") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcba") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "acbdca") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acbdca") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 320164
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 320164: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababababababababababababababababababababab") == 672623781
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababababababababababababababababababababab") == 672623781: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdbca") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdbca") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccbaabccba") == 446
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccbaabccba") == 446: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdaabbccbddc") == 184
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdaabbccbddc") == 184: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababab") == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababab") == 106: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababab") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababab") == 64: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcababcababcababcababcababcababcababcab") == 237716
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcababcababcababcababcababcababcababcab") == 237716: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdaabbccbddcddcbaabccbddcddcba") == 17166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdaabbccbddcddcbaabccbddcddcba") == 17166: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc") == 504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc") == 504: {e}')
    
    total += 1
    try:
        result = candidate(s = "aababaababaababaababaababaababaababaababaababaababa") == 442187
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aababaababaababaababaababaababaababaababaababaababa") == 442187: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbccaddccbbbaabbbccaddccbbba") == 4260
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbccaddccbbbaabbbccaddccbbba") == 4260: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcd") == 244
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcd") == 244: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcd") == 812
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcd") == 812: {e}')
    
    total += 1
    try:
        result = candidate(s = "ddccbbbaaacccbbbaaacccbdd") == 607
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ddccbbbaaacccbbbaaacccbdd") == 607: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 38097140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 38097140: {e}')
    
    total += 1
    try:
        result = candidate(s = "dddddddddddddddddddddddd") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "dddddddddddddddddddddddd") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab") == 462
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab") == 462: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 232
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 232: {e}')
    
    total += 1
    try:
        result = candidate(s = "dcbadcbadcbadcbadcbadcb") == 2219
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "dcbadcbadcbadcbadcbadcb") == 2219: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabababababababa") == 161
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabababababababa") == 161: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcd") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcd") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbcccc") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbcccc") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccccddddddbbbaaaadddbbbbccccaaaabbbccbbccbbccbbccbbccbbccbbbbaaaaddbbbbccccaaaaadddbbbbccccaaaabbbccbbccbbccbbccbbccbbccbbbbaaaadd") == 584072730
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccccddddddbbbaaaadddbbbbccccaaaabbbccbbccbbccbbccbbccbbccbbbbaaaaddbbbbccccaaaaadddbbbbccccaaaabbbccbbccbbccbbccbbccbbccbbbbaaaadd") == 584072730: {e}')
    
    total += 1
    try:
        result = candidate(s = "dcbaabcd") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "dcbaabcd") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcd") == 852725823
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcd") == 852725823: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdbabcdbabcdb") == 607
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdbabcdbabcdb") == 607: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccdddd") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccdddd") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabad") == 2784
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabad") == 2784: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaabba") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaabba") == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcd") == 96936
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcd") == 96936: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddccbbaa") == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddccbbaa") == 106: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabcba") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabcba") == 56: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababab") == 1216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababab") == 1216: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda") == 198263755
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda") == 198263755: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabc") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabc") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 125826312
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 125826312: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcbadcbadcbabcd") == 432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcbadcbadcbabcd") == 432: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabc") == 2952
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabc") == 2952: {e}')
    
    total += 1
    try:
        result = candidate(s = "dcbbabdccacbaaadbcbbabcbbb") == 934
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "dcbbabdccacbaaadbcbbabcbbb") == 934: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababa") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababa") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 320443980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 320443980: {e}')
    
    total += 1
    try:
        result = candidate(s = "ddddcbbaabcdccbdddbddbcccbdbabdbbaccabdbdddcbbaabaddabbdcbbaabcddbacccbadcbbaabcdccbdddbddbcccbdbabdbbaccabdbddd") == 923039370
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ddddcbbaabcdccbdddbddbcccbdbabdbbaccabdbdddcbbaabaddabbdcbbaabcddbacccbadcbbaabcdccbdddbddbcccbdbabdbbaccabdbddd") == 923039370: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcadcbadcbadcb") == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcadcbadcbadcb") == 210: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcbaabcd") == 649659461
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcbaabcd") == 649659461: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcbaabcdcbaabcdcba") == 1694
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcbaabcdcbaabcdcba") == 1694: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abba") == 6
    assert candidate(s = "abccba") == 14
    assert candidate(s = "abcba") == 10
    assert candidate(s = "abac") == 5
    assert candidate(s = "a") == 1
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba") == 104860361
    assert candidate(s = "aabbaa") == 10
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd") == 29348
    assert candidate(s = "abcddcba") == 30
    assert candidate(s = "bccb") == 6
    assert candidate(s = "aaa") == 3
    assert candidate(s = "abcd") == 4
    assert candidate(s = "aabb") == 4
    assert candidate(s = "aaaa") == 4
    assert candidate(s = "abab") == 6
    assert candidate(s = "abacabadabacabadabacaba") == 2571
    assert candidate(s = "ababbabaabbababbab") == 212
    assert candidate(s = "aabbaabbaabb") == 44
    assert candidate(s = "aaaabbbbccccaaaabbbbccccaaaabbbbcccc") == 996
    assert candidate(s = "ddccbbbaaacccbdd") == 94
    assert candidate(s = "abcabcabcabc") == 84
    assert candidate(s = "aaaaabbbbbccccddddaaaaabbbbbccccddddaaaaabbbbbccccddddaaaaabbbbbccccddddaaaaabbbbbccccddddaaaaabbbbbccccddddaaaaabbbbbccccdddd") == 127372410
    assert candidate(s = "abcddcbaabcddcba") == 340
    assert candidate(s = "abcdabcdabcd") == 72
    assert candidate(s = "abababababababababababababababab") == 8358
    assert candidate(s = "aaaabbbbccccddddaaaabbbbccccdddd") == 224
    assert candidate(s = "abacaba") == 19
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 450061485
    assert candidate(s = "aaaabbbaaaaabbbbaaaaabbbbaaaaabbbbaaaaabbbbaaaaabbbbaaaa") == 61293
    assert candidate(s = "abcdcba") == 22
    assert candidate(s = "acbdca") == 14
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 320164
    assert candidate(s = "ababababababababababababababababababababababababababababababababababababababababababab") == 672623781
    assert candidate(s = "abcdbca") == 20
    assert candidate(s = "abccbaabccbaabccba") == 446
    assert candidate(s = "abcdabcdaabbccbddc") == 184
    assert candidate(s = "ababababababab") == 106
    assert candidate(s = "abababababab") == 64
    assert candidate(s = "abcababcababcababcababcababcababcababcab") == 237716
    assert candidate(s = "abcdabcdaabbccbddcddcbaabccbddcddcba") == 17166
    assert candidate(s = "abcabcabcabcabcabc") == 504
    assert candidate(s = "aababaababaababaababaababaababaababaababaababaababa") == 442187
    assert candidate(s = "abbbccaddccbbbaabbbccaddccbbba") == 4260
    assert candidate(s = "abcdabcdabcdabcd") == 244
    assert candidate(s = "abcdabcdabcdabcdabcd") == 812
    assert candidate(s = "ddccbbbaaacccbbbaaacccbdd") == 607
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 38097140
    assert candidate(s = "dddddddddddddddddddddddd") == 24
    assert candidate(s = "abababababababababab") == 462
    assert candidate(s = "aaaaa") == 5
    assert candidate(s = "abacabadabacaba") == 232
    assert candidate(s = "dcbadcbadcbadcbadcbadcb") == 2219
    assert candidate(s = "aabababababababa") == 161
    assert candidate(s = "abcdabcd") == 20
    assert candidate(s = "aaaaabbbbbcccc") == 14
    assert candidate(s = "abccccddddddbbbaaaadddbbbbccccaaaabbbccbbccbbccbbccbbccbbccbbbbaaaaddbbbbccccaaaaadddbbbbccccaaaabbbccbbccbbccbbccbbccbbccbbbbaaaadd") == 584072730
    assert candidate(s = "dcbaabcd") == 30
    assert candidate(s = "abcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcdabcabcd") == 852725823
    assert candidate(s = "abcdabcdbabcdbabcdb") == 607
    assert candidate(s = "aaaabbbbccccdddd") == 16
    assert candidate(s = "abacabadabacabadabacabad") == 2784
    assert candidate(s = "abbaabbaabba") == 54
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcd") == 96936
    assert candidate(s = "aabbccddccbbaa") == 106
    assert candidate(s = "abccbaabcba") == 56
    assert candidate(s = "abababababababababababab") == 1216
    assert candidate(s = "ababababab") == 38
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda") == 198263755
    assert candidate(s = "abcabc") == 12
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 125826312
    assert candidate(s = "abcdcbadcbadcbabcd") == 432
    assert candidate(s = "abcabcabcabcabcabcabcabc") == 2952
    assert candidate(s = "dcbbabdccacbaaadbcbbabcbbb") == 934
    assert candidate(s = "ababa") == 9
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 320443980
    assert candidate(s = "ddddcbbaabcdccbdddbddbcccbdbabdbbaccabdbdddcbbaabaddabbdcbbaabcddbacccbadcbbaabcdccbdddbddbcccbdbabdbbaccabdbddd") == 923039370
    assert candidate(s = "abcadcbadcbadcb") == 210
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcbaabcd") == 649659461
    assert candidate(s = "abcdcbaabcdcbaabcdcba") == 1694


