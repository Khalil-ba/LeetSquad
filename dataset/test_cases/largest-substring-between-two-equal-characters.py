def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "aabbaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzx") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzx") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcda") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcda") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcbb") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcbb") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcode") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcode") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvmnop") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvmnop") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "zabz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zabz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "cbzxy") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cbzxy") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcde") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcde") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zabacdz") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zabacdz") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrlomn") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrlomn") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abca") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abca") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihggffeeddccbbaa") == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihggffeeddccbbaa") == 102: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccdddd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccdddd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabc") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabc") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababcabcab") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababcabcab") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzxywvutsrqponmlkjihgfedcba") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzxywvutsrqponmlkjihgfedcba") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdexyzabcdexyzabcdexyz") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdexyzabcdexyzabcdexyz") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzza") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzza") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzz") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzz") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "deified") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deified") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "pqrstuvwxyzabcdefghijklmno") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pqrstuvwxyzabcdefghijklmno") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgahijklmnopqrstuvwxyz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgahijklmnopqrstuvwxyz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorrotorrotor") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorrotorrotor") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbccccccccddddddddeeeeeeeeeffffffffggggggggghhhhhhhhiiiiiiiiiijjjjjjjjjjjjjjjjjkkkkkkkkkkkllllllllllllllllllmmmmmmmmmmmmmmmmmmmnnnnnnnnnnnnnnnnnnnooooooooooooooooppppppppppppppppppppqqqqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrrrrsssssssssssssssssssssttttttttttttttttttttuuuuuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwwwwwxxxyyyyyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzzzzzz") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbccccccccddddddddeeeeeeeeeffffffffggggggggghhhhhhhhiiiiiiiiiijjjjjjjjjjjjjjjjjkkkkkkkkkkkllllllllllllllllllmmmmmmmmmmmmmmmmmmmnnnnnnnnnnnnnnnnnnnooooooooooooooooppppppppppppppppppppqqqqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrrrrsssssssssssssssssssssttttttttttttttttttttuuuuuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwwwwwxxxyyyyyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzzzzzz") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbcccccdddddeeeee") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbcccccdddddeeeee") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "kayak") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "kayak") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeaabbccddeeffgghheeffgghhii") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeaabbccddeeffgghheeffgghhii") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdaebcdfeghifijkiljklmnopqrstuvswxyzxyzz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdaebcdfeghifijkiljklmnopqrstuvswxyzxyzz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyxzyzyxzyzyxzyzyx") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyxzyzyxzyzyxzyzyx") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "ab") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabcdefghijklmnopqrstuvwxyzabcde") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcdefghijklmnopqrstuvwxyzabcde") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzxyzzxyzzxyzzxyzz") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzxyzzxyzzxyzzxyzz") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcb") == 113
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcb") == 113: {e}')
    
    total += 1
    try:
        result = candidate(s = "acbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcba") == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcba") == 110: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotor") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotor") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaa") == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaa") == 105: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghij") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghij") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghij") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghij") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "noon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaaacaaaaadaaaaaeaaaaa") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaaacaaaaadaaaaaeaaaaa") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis") == 37: {e}')
    
    total += 1
    try:
        result = candidate(s = "lkjlkjlkjlkjlkjlkj") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lkjlkjlkjlkjlkjlkj") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeafghijaklmnopqrastuvwxyz") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeafghijaklmnopqrastuvwxyz") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaabbbaaa") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaabbbaaa") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdaebcdfeghifijkiljklmnopqrstuvswxyzxyzzzyxwvutsrqponmlkjilfedcbazyxwvutsrqponmlkjihgfedcba") == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdaebcdfeghifijkiljklmnopqrstuvswxyzxyzzzyxwvutsrqponmlkjilfedcbazyxwvutsrqponmlkjihgfedcba") == 91: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijjihegfedcba") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijjihegfedcba") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaxab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaxab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxz") == 124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxz") == 124: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "level") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "level") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijzyxwvutsrqponmlkjihgfedcba") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijzyxwvutsrqponmlkjihgfedcba") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgxyzgfedcba") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgxyzgfedcba") == 15: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "aabbaa") == 4
    assert candidate(s = "xyzx") == 2
    assert candidate(s = "a") == -1
    assert candidate(s = "aa") == 0
    assert candidate(s = "abcda") == 3
    assert candidate(s = "abcabc") == 2
    assert candidate(s = "abcdabcd") == 3
    assert candidate(s = "xyz") == -1
    assert candidate(s = "abcabcbb") == 5
    assert candidate(s = "leetcode") == 5
    assert candidate(s = "mnopqrstuvmnop") == 9
    assert candidate(s = "zzzzzzzzzz") == 8
    assert candidate(s = "zabz") == 2
    assert candidate(s = "cbzxy") == -1
    assert candidate(s = "abcdeabcde") == 4
    assert candidate(s = "aabbcc") == 0
    assert candidate(s = "zabacdz") == 5
    assert candidate(s = "mnopqrlomn") == 7
    assert candidate(s = "abacaba") == 5
    assert candidate(s = "abca") == 2
    assert candidate(s = "abcdefg") == -1
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihggffeeddccbbaa") == 102
    assert candidate(s = "aaaabbbbccccdddd") == 2
    assert candidate(s = "abcabcabcabcabcabcabc") == 17
    assert candidate(s = "ababcabcab") == 7
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzxywvutsrqponmlkjihgfedcba") == 50
    assert candidate(s = "abcdexyzabcdexyzabcdexyz") == 15
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzza") == 51
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzz") == 8
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 49
    assert candidate(s = "deified") == 5
    assert candidate(s = "pqrstuvwxyzabcdefghijklmno") == -1
    assert candidate(s = "abcdefgahijklmnopqrstuvwxyz") == 6
    assert candidate(s = "rotorrotorrotor") == 13
    assert candidate(s = "aaaaaaaaaabbbbbbbbbccccccccddddddddeeeeeeeeeffffffffggggggggghhhhhhhhiiiiiiiiiijjjjjjjjjjjjjjjjjkkkkkkkkkkkllllllllllllllllllmmmmmmmmmmmmmmmmmmmnnnnnnnnnnnnnnnnnnnooooooooooooooooppppppppppppppppppppqqqqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrrrrsssssssssssssssssssssttttttttttttttttttttuuuuuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwwwwwxxxyyyyyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzzzzzz") == 19
    assert candidate(s = "aaaaabbbbbcccccdddddeeeee") == 3
    assert candidate(s = "kayak") == 3
    assert candidate(s = "abacabadabacaba") == 13
    assert candidate(s = "aabbccddeeaabbccddeeffgghheeffgghhii") == 18
    assert candidate(s = "abracadabra") == 9
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 54
    assert candidate(s = "abcabcabcabc") == 8
    assert candidate(s = "abcdaebcdfeghifijkiljklmnopqrstuvswxyzxyzz") == 4
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 51
    assert candidate(s = "xyzyxzyzyxzyzyxzyzyx") == 18
    assert candidate(s = "ab") == -1
    assert candidate(s = "xyzwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == 48
    assert candidate(s = "aabcdefghijklmnopqrstuvwxyzabcde") == 26
    assert candidate(s = "xyzzxyzzxyzzxyzzxyzz") == 16
    assert candidate(s = "abcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcb") == 113
    assert candidate(s = "acbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcbabcba") == 110
    assert candidate(s = "rotor") == 3
    assert candidate(s = "racecar") == 5
    assert candidate(s = "aaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaaabbbaaa") == 105
    assert candidate(s = "abcdefghijabcdefghij") == 9
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 50
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 25
    assert candidate(s = "abcdefghijabcdefghijabcdefghij") == 19
    assert candidate(s = "noon") == 2
    assert candidate(s = "aaabaaaacaaaaadaaaaaeaaaaa") == 24
    assert candidate(s = "abcdefgabcdefg") == 6
    assert candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis") == 37
    assert candidate(s = "lkjlkjlkjlkjlkjlkj") == 14
    assert candidate(s = "abcdeafghijaklmnopqrastuvwxyz") == 19
    assert candidate(s = "aabbaaabbbaaa") == 11
    assert candidate(s = "abcdaebcdfeghifijkiljklmnopqrstuvswxyzxyzzzyxwvutsrqponmlkjilfedcbazyxwvutsrqponmlkjihgfedcba") == 91
    assert candidate(s = "abcdefghijjihegfedcba") == 19
    assert candidate(s = "abacaxab") == 5
    assert candidate(s = "mississippi") == 8
    assert candidate(s = "xyzzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxz") == 124
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 0
    assert candidate(s = "level") == 3
    assert candidate(s = "abcdefghijzyxwvutsrqponmlkjihgfedcba") == 34
    assert candidate(s = "abcdefgxyzgfedcba") == 15


