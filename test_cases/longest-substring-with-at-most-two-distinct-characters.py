def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababccababcc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababccababcc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabacbebebe") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabacbebebe") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abaccc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abaccc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabcxyzabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabcxyzabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccaabbb") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccaabbb") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaabbbaaa") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaabbbaaa") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzz") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzz") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "mmazzzzzzz") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mmazzzzzzz") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbbcccc") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbbcccc") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "eceba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eceba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabac") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabac") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaa") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaa") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbcccccccccccccccccccccc") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbcccccccccccccccccccccc") == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabbaabb") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabbaabb") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababab") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababab") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacababaacbbccba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacababaacbbccba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababababababababababababab") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababababababababababababab") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababab") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababab") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccaaaabbbbcccc") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccaaaabbbbcccc") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccccbbbbaaaaccccbbaaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccccbbbbaaaaccccbbaaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggg") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggg") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdeabcdefg") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdeabcdefg") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbbbbaaaaabbbaaabbbaabbbaaa") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbbbbaaaaabbbaaabbbaabbbaaa") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxy") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxy") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabccccaaaabbbbccccaaaabbbbcccc") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabccccaaaabbbbccccaaaabbbbcccc") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbaaabbbaaabbbaaa") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbaaabbbaaabbbaaa") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabababababcabcabc") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabababababcabcabc") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaaabbbbaaabbb") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaaabbbbaaabbb") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabraabracadabraabracadabraabracadabraabracadabra") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabraabracadabraabracadabraabracadabraabracadabra") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaabbbbbbbbaaaaabbbbbbbbcccccccccccaaaabbbbcccc") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaabbbbbbbbaaaaabbbbbbbbcccccccccccaaaabbbbcccc") == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababbabcbababc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababbabcbababc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccbaabccbaabccbaabccbaabccba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccbaabccbaabccbaabccbaabccba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggghhh") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggghhh") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccccddeee") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccccddeee") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaabbbaaaabbbaaabbbaabbbaaaabbbaaabbbaabbbaaaaabbbaaaaabbbaaaa") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaabbbaaaabbbaaabbbaabbbaaaabbbaaabbbaabbbaaaaabbbaaaaabbbaaaa") == 66: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbbbbcccccc") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbbbbcccccc") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababab") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababab") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabcccccaaa") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcccccaaa") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcdeabcde") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcdeabcde") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababab") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababab") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvwxyzmnopqrstuvwxyzmnopqrstuvwxyzmnopqrstuvwxyz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvwxyzmnopqrstuvwxyzmnopqrstuvwxyzmnopqrstuvwxyz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefggfedcba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefggfedcba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdeff") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdeff") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzyyyyyy") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzyyyyyy") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbccccdddd") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbccccdddd") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababababab") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababababab") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbbccccddeeeeffff") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbbccccddeeeeffff") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabccbbbaaaacccbbb") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabccbbbaaaacccbbb") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zxyzzxyzzxyzzxyzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxyzzxyzzxyzzxyzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzz") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzz") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaccddccbaaabb") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaccddccbaaabb") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabb") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabb") == 16: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 2
    assert candidate(s = "ababccababcc") == 4
    assert candidate(s = "aabacbebebe") == 6
    assert candidate(s = "a") == 1
    assert candidate(s = "abcabcabc") == 2
    assert candidate(s = "abcabcabcabc") == 2
    assert candidate(s = "ababababab") == 10
    assert candidate(s = "abaccc") == 4
    assert candidate(s = "aa") == 2
    assert candidate(s = "") == 0
    assert candidate(s = "abcabc") == 2
    assert candidate(s = "xyzabcxyzabc") == 2
    assert candidate(s = "xyzxyzxyz") == 2
    assert candidate(s = "abacab") == 3
    assert candidate(s = "ccaabbb") == 5
    assert candidate(s = "aabbaaabbbaaa") == 13
    assert candidate(s = "zzzzzzzzzzzzz") == 13
    assert candidate(s = "abcd") == 2
    assert candidate(s = "aabbccddeeff") == 4
    assert candidate(s = "aab") == 3
    assert candidate(s = "aabbcc") == 4
    assert candidate(s = "mmazzzzzzz") == 8
    assert candidate(s = "aabbbbcccc") == 8
    assert candidate(s = "eceba") == 3
    assert candidate(s = "abacaba") == 3
    assert candidate(s = "abacabac") == 3
    assert candidate(s = "aaaaaaa") == 7
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 2
    assert candidate(s = "abcdefg") == 2
    assert candidate(s = "aaaaaaaaaabbbbbbbbbcccccccccccccccccccccc") == 31
    assert candidate(s = "aabbaabbaabbaabbaabbaabb") == 24
    assert candidate(s = "ababababababababababababababababababababababababab") == 50
    assert candidate(s = "abacababaacbbccba") == 6
    assert candidate(s = "abababababababababababababababababababababababababab") == 52
    assert candidate(s = "ababababababababababab") == 22
    assert candidate(s = "aabbccaaaabbbbcccc") == 8
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 2
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 42
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 54
    assert candidate(s = "aabbbcccccbbbbaaaaccccbbaaa") == 12
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggg") == 8
    assert candidate(s = "abcdabcdeabcdefg") == 2
    assert candidate(s = "abacabadabacaba") == 3
    assert candidate(s = "aabbbbbbaaaaabbbaaabbbaabbbaaa") == 30
    assert candidate(s = "abracadabra") == 3
    assert candidate(s = "xyxyxyxyxyxyxyxyxyxyxyxyxy") == 26
    assert candidate(s = "aabccccaaaabbbbccccaaaabbbbcccc") == 8
    assert candidate(s = "aaabbbaaabbbaaabbbaaa") == 21
    assert candidate(s = "aabababababcabcabc") == 11
    assert candidate(s = "aaabaaaabbbbaaabbb") == 18
    assert candidate(s = "abracadabraabracadabraabracadabraabracadabraabracadabra") == 3
    assert candidate(s = "aaaaaaaabbbbbbbbaaaaabbbbbbbbcccccccccccaaaabbbbcccc") == 29
    assert candidate(s = "ababbabcbababc") == 7
    assert candidate(s = "abccbaabccbaabccbaabccbaabccbaabccba") == 4
    assert candidate(s = "aabbccddeeefffggghhh") == 6
    assert candidate(s = "aabbccccddeee") == 6
    assert candidate(s = "abcabcabcabcabcabcabcabc") == 2
    assert candidate(s = "aabbaaabbbaaaabbbaaabbbaabbbaaaabbbaaabbbaabbbaaaaabbbaaaaabbbaaaa") == 66
    assert candidate(s = "aaaaaabbbbbcccccc") == 11
    assert candidate(s = "abababababab") == 12
    assert candidate(s = "aabcccccaaa") == 8
    assert candidate(s = "abcdeabcdeabcdeabcde") == 2
    assert candidate(s = "ababababababababababababab") == 26
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52
    assert candidate(s = "mnopqrstuvwxyzmnopqrstuvwxyzmnopqrstuvwxyzmnopqrstuvwxyz") == 2
    assert candidate(s = "abcdefggfedcba") == 4
    assert candidate(s = "abcdefabcdeff") == 3
    assert candidate(s = "abcdabcdabcdabcdabcdabcd") == 2
    assert candidate(s = "zzzzzzyyyyyy") == 12
    assert candidate(s = "aaaaabbbbccccdddd") == 9
    assert candidate(s = "abababababababababababababababababab") == 36
    assert candidate(s = "aabbaabbbccccddeeeeffff") == 9
    assert candidate(s = "mississippi") == 7
    assert candidate(s = "aabccbbbaaaacccbbb") == 7
    assert candidate(s = "abcabcabcabcabc") == 2
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 4
    assert candidate(s = "zxyzzxyzzxyzzxyzz") == 3
    assert candidate(s = "zzzzzzzzzzzzzzzzzz") == 18
    assert candidate(s = "aabbaaccddccbaaabb") == 6
    assert candidate(s = "aabbaabbaabbaabb") == 16


