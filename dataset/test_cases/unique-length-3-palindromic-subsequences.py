def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abcba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "madam") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madam") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "adc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "adc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "noon") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noon") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabca") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabca") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbcbaba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbcbaba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "level") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "level") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabacbaabacba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabacbaabacba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonmoonnoonmoonnoonmoonnoonmoonnoonmoonnoonmoonnoon") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonmoonnoonmoonnoonmoonnoonmoonnoonmoonnoonmoonnoon") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyyxwwvvuuttssrrqqppoonnmmllkkjjiihhggeeffddccbbaa") == 352
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyyxwwvvuuttssrrqqppoonnmmllkkjjiihhggeeffddccbbaa") == 352: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzyyyyxxxwwvvuttsrrqqppoonnmmllkkjjiihhggffeeddccba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzyyyyxxxwwvvuttsrrqqppoonnmmllkkjjiihhggffeeddccba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzazzaaz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzazzaaz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababcab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababcab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabad") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabad") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarcarcarecarracecarcarcarecarracecarcarcarecarracecar") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarcarcarecarracecarcarcarecarracecarcarcarecarracecar") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdfgdcaba") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcaba") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbaaabbbaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbaaabbbaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaaabaaaaabaaaabaaaaaabaaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaaabaaaaabaaaabaaaaaabaaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabaaaabaaaab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabaaaabaaaab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbabcbabcbabcbabcbabcbabcba") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbabcbabcbabcbabcbabcbabcba") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "bababababababababababababababababababababa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bababababababababababababababababababababa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbac") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbac") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 325: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyxyzyxyzyx") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyxyzyxyzyx") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 650: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcbaedcba") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcbaedcba") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbbaabbaabbbaabbaabbbaabbaabbbaabbaabbba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbbaabbaabbbaabbaabbbaabbaabbbaabbaabbba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghihgfedcbaabcdefghihgfedcba") == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghihgfedcbaabcdefghihgfedcba") == 80: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaaabaaaabaaaabaaaabaaaabaaaabaaaabaaaab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaaabaaaabaaaabaaaabaaaabaaaabaaaabaaaab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbacbacbacbacbacbacbacbacbacbacbacbacb") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbacbacbacbacbacbacbacbacbacbacbacbacb") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababababababababababababababababababababababababababababa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababababababababababababababababababababababababababababa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzzzz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzzzz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "mamamadadadmmadammaddada") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mamamadadadmmadammaddada") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababababab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababababab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaabbbbbbbbbbbbccccccccccdddddddddd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaabbbbbbbbbbbbccccccccccdddddddddd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarcarcarecarracecarcarcarecarracecar") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarcarcarecarracecarcarcarecarracecar") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbacbacbacba") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbacbacbacba") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababababababababab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababababababababab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippississippiississippiississippiississippiississippi") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippississippiississippiississippiississippiississippi") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonmoonnoonmoon") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonmoonnoonmoon") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonmoonnoonmoonnoonmoonnoonmoonnoonmoonnoonmoonnoonnoonmoon") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonmoonnoonmoonnoonmoonnoonmoonnoonmoonnoonmoonnoonnoonmoon") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbccccc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbccccc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippississippiississippiississippiississippi") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippississippiississippiississippiississippi") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabad") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabad") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzyyyxxwwvvuttsrrqqppoonnmmllkkjjiihhggffeeddccba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzyyyxxwwvvuttsrrqqppoonnmmllkkjjiihhggffeeddccba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba") == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abcba") == 3
    assert candidate(s = "madam") == 3
    assert candidate(s = "abcdedcba") == 10
    assert candidate(s = "aaaaa") == 1
    assert candidate(s = "adc") == 0
    assert candidate(s = "abcabcabc") == 9
    assert candidate(s = "abracadabra") == 13
    assert candidate(s = "aaa") == 1
    assert candidate(s = "racecar") == 6
    assert candidate(s = "abba") == 1
    assert candidate(s = "noon") == 1
    assert candidate(s = "abccba") == 3
    assert candidate(s = "aaaa") == 1
    assert candidate(s = "aabbcc") == 0
    assert candidate(s = "mississippi") == 5
    assert candidate(s = "aabca") == 3
    assert candidate(s = "bbcbaba") == 4
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 0
    assert candidate(s = "xyzzyx") == 3
    assert candidate(s = "level") == 3
    assert candidate(s = "abcdefg") == 0
    assert candidate(s = "aabacbaabacba") == 8
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 0
    assert candidate(s = "noonmoonnoonmoonnoonmoonnoonmoonnoonmoonnoonmoonnoon") == 9
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyyxwwvvuuttssrrqqppoonnmmllkkjjiihhggeeffddccbbaa") == 352
    assert candidate(s = "zzzzzzzyyyyxxxwwvvuttsrrqqppoonnmmllkkjjiihhggffeeddccba") == 3
    assert candidate(s = "zzzazzaaz") == 4
    assert candidate(s = "abacabadabacaba") == 11
    assert candidate(s = "ababababababababababababababababababababab") == 4
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 9
    assert candidate(s = "ababcab") == 6
    assert candidate(s = "abacabadabacabadabacabadabacabad") == 16
    assert candidate(s = "racecarcarcarecarracecarcarcarecarracecarcarcarecarracecar") == 16
    assert candidate(s = "abacdfgdcaba") == 16
    assert candidate(s = "aabbbaaabbbaaa") == 4
    assert candidate(s = "aaabaaaabaaaaabaaaabaaaaaabaaaa") == 4
    assert candidate(s = "aaaabaaaabaaaab") == 4
    assert candidate(s = "abcbabcbabcbabcbabcbabcbabcba") == 9
    assert candidate(s = "bababababababababababababababababababababa") == 4
    assert candidate(s = "abcbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbac") == 9
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 4
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 325
    assert candidate(s = "xyzyxyzyxyzyx") == 9
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 650
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcbaedcba") == 20
    assert candidate(s = "abbaabbbaabbaabbbaabbaabbbaabbaabbbaabbaabbba") == 4
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 9
    assert candidate(s = "abcdefghihgfedcbaabcdefghihgfedcba") == 80
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 26
    assert candidate(s = "aaabaaaabaaaabaaaabaaaabaaaabaaaabaaaabaaaab") == 4
    assert candidate(s = "abcbacbacbacbacbacbacbacbacbacbacbacbacb") == 9
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
    assert candidate(s = "babababababababababababababababababababababababababababababa") == 4
    assert candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba") == 4
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzzzz") == 26
    assert candidate(s = "mamamadadadmmadammaddada") == 9
    assert candidate(s = "aabbccddeeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1
    assert candidate(s = "ababababababababababababababababababababababababababab") == 4
    assert candidate(s = "aaaaaaaaaaaabbbbbbbbbbbbccccccccccdddddddddd") == 4
    assert candidate(s = "racecarcarcarecarracecarcarcarecarracecar") == 16
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 9
    assert candidate(s = "abacbacbacbacba") == 9
    assert candidate(s = "ababababababababababababababababababababababababababababababab") == 4
    assert candidate(s = "mississippississippiississippiississippiississippiississippi") == 9
    assert candidate(s = "abcabcabcabcabc") == 9
    assert candidate(s = "noonmoonnoonmoon") == 8
    assert candidate(s = "noonmoonnoonmoonnoonmoonnoonmoonnoonmoonnoonmoonnoonnoonmoon") == 9
    assert candidate(s = "aaaaabbbbbccccc") == 3
    assert candidate(s = "mississippississippiississippiississippiississippi") == 9
    assert candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabad") == 16
    assert candidate(s = "zzzzzyyyxxwwvvuttsrrqqppoonnmmllkkjjiihhggffeeddccba") == 2
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 0
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 9
    assert candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba") == 4


