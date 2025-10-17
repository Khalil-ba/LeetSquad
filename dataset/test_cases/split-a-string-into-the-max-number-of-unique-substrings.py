def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "aaaabbbb") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbb") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abac") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abac") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababccc") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababccc") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzz") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzz") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcd") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcd") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "noon") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noon") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabad") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabad") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zabac") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zabac") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcd") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcd") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccdd") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccdd") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxyxyxyxy") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxyxyxyxy") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababcabcabc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababcabcabc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabacabacabac") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabacabacabac") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabad") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabad") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyxzyxzy") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxzyxzy") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababab") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababab") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghij") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghij") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohello") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohello") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabad") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabad") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "repaid") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repaid") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbccccdddd") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbccccdddd") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "redder") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "redder") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaaabbaabaaab") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaaabbaabaaab") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaxabacaxabacax") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaxabacaxabacax") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "optimization") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "optimization") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyxzyxzyzyxzyz") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxzyxzyzyxzyz") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "kayak") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "kayak") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcde") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcde") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababab") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababab") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzyzxzyzzzzzzzzzz") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzyzxzyzzzzzzzzzz") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijkabcdefghijk") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijkabcdefghijk") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnop") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnop") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "level") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "level") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababa") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababa") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcdabcdeabcde") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcdabcdeabcde") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijjihgfedcba") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijjihgfedcba") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbbbbbaaaaabbbbbbbaaaa") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbbbbbaaaaabbbbbbbaaaa") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeff") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeff") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyz") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyz") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdeabcdeabcd") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdeabcdeabcd") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdaabbcc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdaabbcc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcdeabcde") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcdeabcde") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccdd") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccdd") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "detartrated") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "detartrated") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccdddd") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccdddd") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabacabadaba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabacabadaba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabad") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabad") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "deified") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deified") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoon") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoon") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "repaper") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repaper") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaabba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaabba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbcbcbcbcbc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbcbcbcbcbc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdfgdcaba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcaba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcde") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcde") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabcda") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabcda") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefg") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefg") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotor") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotor") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghihgfedcba") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghihgfedcba") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghij") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghij") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabc") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabc") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffggzzzz") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffggzzzz") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdefabcdef") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdefabcdef") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbccccddddeeeefffggg") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbccccddddeeeefffggg") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "reviled") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "reviled") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghabcdefgh") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghabcdefgh") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghh") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghh") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzyyyxxxwwwvvvuuu") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzyyyxxxwwwvvvuuu") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcdeabc") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcdeabc") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcaabbcc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcaabbcc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzyxyzzzyxyzzzyxyzzzy") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzyxyzzzyxyzzzyxyzzzy") == 11: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "aaaabbbb") == 5
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 26
    assert candidate(s = "abac") == 3
    assert candidate(s = "abcdef") == 6
    assert candidate(s = "aaaaaaaab") == 4
    assert candidate(s = "a") == 1
    assert candidate(s = "zzzzzzz") == 3
    assert candidate(s = "abcabcabc") == 6
    assert candidate(s = "abcabcabcabc") == 7
    assert candidate(s = "ababccc") == 5
    assert candidate(s = "zzzzzzzzzzzzzzzz") == 5
    assert candidate(s = "aa") == 1
    assert candidate(s = "abcabc") == 4
    assert candidate(s = "abcdabcd") == 6
    assert candidate(s = "xyzxyzxyz") == 6
    assert candidate(s = "noon") == 3
    assert candidate(s = "abacabad") == 5
    assert candidate(s = "banana") == 4
    assert candidate(s = "aba") == 2
    assert candidate(s = "zzzzzz") == 3
    assert candidate(s = "aabbcc") == 4
    assert candidate(s = "zabac") == 4
    assert candidate(s = "abcdabcdabcdabcd") == 9
    assert candidate(s = "abacaba") == 4
    assert candidate(s = "aabbccdd") == 6
    assert candidate(s = "abcdefg") == 7
    assert candidate(s = "xyxyxyxyxyxyxyxy") == 7
    assert candidate(s = "ababcabcabc") == 7
    assert candidate(s = "abacabacabacabac") == 8
    assert candidate(s = "abacabadabacabadabacabadabacabad") == 13
    assert candidate(s = "xyzzyxzyxzy") == 7
    assert candidate(s = "ababababababababababababababababab") == 10
    assert candidate(s = "abcdefghijabcdefghijabcdefghij") == 20
    assert candidate(s = "hellohellohello") == 9
    assert candidate(s = "abacabadabacabad") == 9
    assert candidate(s = "repaid") == 6
    assert candidate(s = "aaaaabbbbccccdddd") == 10
    assert candidate(s = "abccbaabccba") == 7
    assert candidate(s = "redder") == 4
    assert candidate(s = "aabaaaabbaabaaab") == 7
    assert candidate(s = "abacaxabacaxabacax") == 10
    assert candidate(s = "optimization") == 10
    assert candidate(s = "aaaaaaaaaaaaaaa") == 5
    assert candidate(s = "xyzzyxzyxzyzyxzyz") == 9
    assert candidate(s = "kayak") == 4
    assert candidate(s = "abcdabcde") == 7
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 26
    assert candidate(s = "abababababababab") == 7
    assert candidate(s = "ababababababab") == 6
    assert candidate(s = "abababababab") == 6
    assert candidate(s = "zzzyzxzyzzzzzzzzzz") == 7
    assert candidate(s = "abcdefghijkabcdefghijk") == 16
    assert candidate(s = "abcabcabcabcabcabc") == 9
    assert candidate(s = "abcdefghijklmnop") == 16
    assert candidate(s = "level") == 4
    assert candidate(s = "ababababababababababababababababa") == 10
    assert candidate(s = "abcabcdabcdeabcde") == 10
    assert candidate(s = "abcdefghijjihgfedcba") == 15
    assert candidate(s = "aaaaaabbbbbbaaaaabbbbbbbaaaa") == 11
    assert candidate(s = "aabbaabbccddeeff") == 11
    assert candidate(s = "abacabadabacaba") == 8
    assert candidate(s = "xyzxyzxyzxyzxyzxyz") == 9
    assert candidate(s = "abcdabcdeabcdeabcd") == 11
    assert candidate(s = "abcdabcdaabbcc") == 9
    assert candidate(s = "abcdefgabcdefg") == 10
    assert candidate(s = "abcdeabcdeabcdeabcde") == 11
    assert candidate(s = "aabbaabbccdd") == 8
    assert candidate(s = "aabbccddeeffgg") == 10
    assert candidate(s = "detartrated") == 8
    assert candidate(s = "abcdefghij") == 10
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 26
    assert candidate(s = "aaaabbbbccccdddd") == 10
    assert candidate(s = "aabacabadaba") == 7
    assert candidate(s = "abacabadabacabadabacabad") == 11
    assert candidate(s = "deified") == 5
    assert candidate(s = "noonnoonnoon") == 6
    assert candidate(s = "repaper") == 5
    assert candidate(s = "abbaabbaabba") == 6
    assert candidate(s = "bcbcbcbcbcbcbcbc") == 7
    assert candidate(s = "aaaaaaaaaaaaaaaa") == 5
    assert candidate(s = "abacdfgdcaba") == 8
    assert candidate(s = "abcdeabcdeabcde") == 10
    assert candidate(s = "abcdabcabcda") == 8
    assert candidate(s = "ababababab") == 5
    assert candidate(s = "abcdefgabcdefgabcdefg") == 14
    assert candidate(s = "rotor") == 4
    assert candidate(s = "abcdefghihgfedcba") == 13
    assert candidate(s = "racecar") == 5
    assert candidate(s = "abcdefghijabcdefghij") == 15
    assert candidate(s = "abcabcabcabcabcabcabcabc") == 10
    assert candidate(s = "aabbccddeeffggzzzz") == 13
    assert candidate(s = "abcdefabcdefabcdefabcdef") == 14
    assert candidate(s = "aaaaabbbbccccddddeeeefffggg") == 16
    assert candidate(s = "reviled") == 6
    assert candidate(s = "abcdefghabcdefgh") == 12
    assert candidate(s = "aabbccddeeffgghh") == 12
    assert candidate(s = "zzzzyyyxxxwwwvvvuuu") == 12
    assert candidate(s = "mississippi") == 7
    assert candidate(s = "abcdeabcdeabcdeabc") == 11
    assert candidate(s = "abcabcabcaabbcc") == 9
    assert candidate(s = "abcabcabcabcabc") == 8
    assert candidate(s = "xyzzzyxyzzzyxyzzzyxyzzzy") == 11


