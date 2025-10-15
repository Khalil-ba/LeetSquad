def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaa") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaa") == 55: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijj") == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijj") == 165: {e}')
    
    total += 1
    try:
        result = candidate(word = "aba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaabbbbcccc") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaabbbbcccc") == 66: {e}')
    
    total += 1
    try:
        result = candidate(word = "babcbabcbab") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "babcbabcbab") == 32: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghija") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghija") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabb") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabb") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgg") == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgg") == 84: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghij") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghij") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "jihgfedcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jihgfedcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeff") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeff") == 63: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacaba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacaba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "jij") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jij") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijabcdefghij") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijabcdefghij") == 23: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcde") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcde") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "ijji") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ijji") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "jjjjj") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jjjjj") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "jijijijiji") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jijijijiji") == 40: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbaa") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbaa") == 19: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabc") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabc") == 21: {e}')
    
    total += 1
    try:
        result = candidate(word = "he") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "he") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijabcdefghijabcdefghij") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijabcdefghijabcdefghij") == 63: {e}')
    
    total += 1
    try:
        result = candidate(word = "jijjjijijj") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jijjjijijj") == 41: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaa") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaa") == 28: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaa") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaa") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacabadabacaba") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabadabacaba") == 32: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaabbbbbbbbaaaaaaaabbbbbbbb") == 464
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaabbbbbbbbaaaaaaaabbbbbbbb") == 464: {e}')
    
    total += 1
    try:
        result = candidate(word = "jihgfedcbajihgfedcbajihgfedcbajihgfedcbajihgfedcba") == 176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jihgfedcbajihgfedcbajihgfedcbajihgfedcbajihgfedcba") == 176: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 1038
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 1038: {e}')
    
    total += 1
    try:
        result = candidate(word = "jijijiijijijiijijijiijijijiijijijiijijijiijijiij") == 879
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jijijiijijijiijijijiijijijiijijijiijijijiijijiij") == 879: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijabcde") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijabcde") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj") == 903
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj") == 903: {e}')
    
    total += 1
    try:
        result = candidate(word = "acacacacacacacacacac") == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "acacacacacacacacacac") == 155: {e}')
    
    total += 1
    try:
        result = candidate(word = "jijijiijjjjijiijijijiijjjjijiijijijiijjjjijiijijijiijjjjijiijijijiijjjjijiijijijiijjjjijiijijijiijjjjijiijijijiijjjjj") == 5171
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jijijiijjjjijiijijijiijjjjijiijijijiijjjjijiijijijiijjjjijiijijijiijjjjijiijijijiijjjjijiijijijiijjjjijiijijijiijjjjj") == 5171: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghij") == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghij") == 106: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccdd") == 4720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccdd") == 4720: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbaaabbbaaabbaaa") == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbaaabbbaaabbaaa") == 126: {e}')
    
    total += 1
    try:
        result = candidate(word = "jjiijjiijjjiiijjiiijjjijjjiiijjiiijjjijjjjj") == 721
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jjiijjiijjjiiijjiiijjjijjjiiijjiiijjjijjjjj") == 721: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbaabbaabbaabb") == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbaabbaabbaabb") == 120: {e}')
    
    total += 1
    try:
        result = candidate(word = "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj") == 990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj") == 990: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbaabbaabbaabbccddeeffgghhiijj") == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbaabbaabbaabbccddeeffgghhiijj") == 420: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabcabcabcabcabcabcabc") == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabcabcabcabcabcabcabc") == 225: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdeedcba") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdeedcba") == 23: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjj") == 640
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjj") == 640: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdabcdaabbccddeeffgghhiijj") == 222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdabcdaabbccddeeffgghhiijj") == 222: {e}')
    
    total += 1
    try:
        result = candidate(word = "ababababababababababababababababababababab") == 672
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ababababababababababababababababababababab") == 672: {e}')
    
    total += 1
    try:
        result = candidate(word = "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj") == 2485
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj") == 2485: {e}')
    
    total += 1
    try:
        result = candidate(word = "jijijiijjjijiiiiij") == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jijijiijjjijiiiiij") == 132: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 176: {e}')
    
    total += 1
    try:
        result = candidate(word = "ababababababababababababab") == 260
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ababababababababababababab") == 260: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbaaabbbaaabbaaabbba") == 187
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbaaabbbaaabbaaabbba") == 187: {e}')
    
    total += 1
    try:
        result = candidate(word = "acccabbbdcbaaaccbbaaccbbcdac") == 161
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "acccabbbdcbaaaccbbaaccbbcdac") == 161: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbaaabbbaaaabbbaaa") == 159
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbaaabbbaaaabbbaaa") == 159: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabcabc") == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabcabc") == 57: {e}')
    
    total += 1
    try:
        result = candidate(word = "jjjjjjjjjj") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jjjjjjjjjj") == 55: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 670
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 670: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijkabcdefghijkabcdefghijk") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijkabcdefghijkabcdefghijk") == 63: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 452
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 452: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeee") == 1025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeee") == 1025: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijabcdeijfgh") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijabcdeijfgh") == 23: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 820
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 820: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaabbbbbbbbbbbbccccccccccdddddddddd") == 738
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaabbbbbbbbbbbbccccccccccdddddddddd") == 738: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeaabbccddeeaabbccddeedcba") == 403
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeaabbccddeeaabbccddeedcba") == 403: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 715
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 715: {e}')
    
    total += 1
    try:
        result = candidate(word = "babababababababababa") == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "babababababababababa") == 155: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjijjiihhggeeffddccbbaa") == 501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjijjiihhggeeffddccbbaa") == 501: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjabcdefghijabcdefghijabcdefghijabcdefghij") == 363
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjabcdefghijabcdefghijabcdefghijabcdefghij") == 363: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabccbaabccbaabcabccbaabccba") == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabccbaabccbaabcabccbaabccba") == 225: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijjihgfedcba") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijjihgfedcba") == 48: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacabadabacabadabacabad") == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabadabacabadabacabad") == 90: {e}')
    
    total += 1
    try:
        result = candidate(word = "abababababababababababababababab") == 392
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abababababababababababababababab") == 392: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacabadabacabadabacabadabacabad") == 154
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacabadabacabadabacabadabacabad") == 154: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "aaaaaaaaaa") == 55
    assert candidate(word = "aabbccddeeffgghhiijj") == 165
    assert candidate(word = "aba") == 4
    assert candidate(word = "aaaabbbbcccc") == 66
    assert candidate(word = "babcbabcbab") == 32
    assert candidate(word = "abcdefghija") == 11
    assert candidate(word = "abcdcba") == 10
    assert candidate(word = "aaa") == 6
    assert candidate(word = "aabb") == 9
    assert candidate(word = "aabbccddeeffgg") == 84
    assert candidate(word = "abcdefghij") == 10
    assert candidate(word = "jihgfedcba") == 10
    assert candidate(word = "aabbccddeeff") == 63
    assert candidate(word = "abcabc") == 9
    assert candidate(word = "abacaba") == 12
    assert candidate(word = "jij") == 4
    assert candidate(word = "xyz") == 0
    assert candidate(word = "abcdefghijabcdefghij") == 23
    assert candidate(word = "abcde") == 5
    assert candidate(word = "ijji") == 8
    assert candidate(word = "jjjjj") == 15
    assert candidate(word = "jijijijiji") == 40
    assert candidate(word = "aabbaa") == 19
    assert candidate(word = "abcabcabc") == 21
    assert candidate(word = "he") == 2
    assert candidate(word = "a") == 1
    assert candidate(word = "abcdefghijabcdefghijabcdefghij") == 63
    assert candidate(word = "jijjjijijj") == 41
    assert candidate(word = "aaaaaaa") == 28
    assert candidate(word = "aaaaa") == 15
    assert candidate(word = "abacabadabacaba") == 32
    assert candidate(word = "aaaaaaaabbbbbbbbaaaaaaaabbbbbbbb") == 464
    assert candidate(word = "jihgfedcbajihgfedcbajihgfedcbajihgfedcbajihgfedcba") == 176
    assert candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 1038
    assert candidate(word = "jijijiijijijiijijijiijijijiijijijiijijijiijijiij") == 879
    assert candidate(word = "abcdefghijabcde") == 15
    assert candidate(word = "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj") == 903
    assert candidate(word = "acacacacacacacacacac") == 155
    assert candidate(word = "jijijiijjjjijiijijijiijjjjijiijijijiijjjjijiijijijiijjjjijiijijijiijjjjijiijijijiijjjjijiijijijiijjjjijiijijijiijjjjj") == 5171
    assert candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghij") == 106
    assert candidate(word = "aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccdd") == 4720
    assert candidate(word = "aabbaaabbbaaabbaaa") == 126
    assert candidate(word = "jjiijjiijjjiiijjiiijjjijjjiiijjiiijjjijjjjj") == 721
    assert candidate(word = "aabbaabbaabbaabb") == 120
    assert candidate(word = "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj") == 990
    assert candidate(word = "aabbaabbaabbaabbccddeeffgghhiijj") == 420
    assert candidate(word = "abcabcabcabcabcabcabcabcabcabc") == 225
    assert candidate(word = "abcdeedcba") == 23
    assert candidate(word = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjj") == 640
    assert candidate(word = "abcdabcdaabbccddeeffgghhiijj") == 222
    assert candidate(word = "ababababababababababababababababababababab") == 672
    assert candidate(word = "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj") == 2485
    assert candidate(word = "jijijiijjjijiiiiij") == 132
    assert candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 176
    assert candidate(word = "ababababababababababababab") == 260
    assert candidate(word = "aabbaaabbbaaabbaaabbba") == 187
    assert candidate(word = "acccabbbdcbaaaccbbaaccbbcdac") == 161
    assert candidate(word = "aabbaaabbbaaaabbbaaa") == 159
    assert candidate(word = "abcabcabcabcabc") == 57
    assert candidate(word = "jjjjjjjjjj") == 55
    assert candidate(word = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 670
    assert candidate(word = "abcdefghijkabcdefghijkabcdefghijk") == 63
    assert candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 452
    assert candidate(word = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeee") == 1025
    assert candidate(word = "abcdefghijabcdeijfgh") == 23
    assert candidate(word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 820
    assert candidate(word = "aaaaaaaaaabbbbbbbbbbbbccccccccccdddddddddd") == 738
    assert candidate(word = "aabbccddeeaabbccddeeaabbccddeedcba") == 403
    assert candidate(word = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 715
    assert candidate(word = "babababababababababa") == 155
    assert candidate(word = "aabbccddeeffgghhiijjijjiihhggeeffddccbbaa") == 501
    assert candidate(word = "aabbccddeeffgghhiijjabcdefghijabcdefghijabcdefghijabcdefghij") == 363
    assert candidate(word = "abcabccbaabccbaabcabccbaabccba") == 225
    assert candidate(word = "abcdefghijjihgfedcba") == 48
    assert candidate(word = "abacabadabacabadabacabad") == 90
    assert candidate(word = "abababababababababababababababab") == 392
    assert candidate(word = "abacabadabacabadabacabadabacabad") == 154


