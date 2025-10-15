def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abcdabcde") == [8, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcde") == [8, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbbbbccccc") == [6, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbbbbccccc") == [6, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz") == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz") == [9]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbbccccc") == [4, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbbccccc") == [4, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdeabcdabcde") == [18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdeabcdabcde") == [18]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zab") == [1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zab") == [1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == [1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zabbcdefghijklmnopqrstuvwxyz") == [28]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zabbcdefghijklmnopqrstuvwxyz") == [28]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeee") == [2, 2, 2, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeee") == [2, 2, 2, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcba") == [7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcba") == [7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab") == [10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab") == [10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zabzabc") == [6, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zabzabc") == [6, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab") == [8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab") == [8]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde") == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde") == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababcbacadefegdehijhklij") == [9, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababcbacadefegdehijhklij") == [9, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(s = "eccbbbbdec") == [10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eccbbbbdec") == [10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcdabcdeabcdefabcdefg") == [24, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcdabcdeabcdefabcdefg") == [24, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == [66]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == [66]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeefffffffffghhhhhhhhiiiiiiiijjjjjjjjkkkkkkkkllllllllmmmmmmmmnnnnnnnnooooooooppppppppqqqqqqqqrrrrrrrrssssssssttttttttuuuuuuuuvvvvvvvvwwwwwwwwxxxxxxxxxyyyyyyyyzzzzzzzz") == [10, 8, 8, 8, 8, 9, 1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 8, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeefffffffffghhhhhhhhiiiiiiiijjjjjjjjkkkkkkkkllllllllmmmmmmmmnnnnnnnnooooooooppppppppqqqqqqqqrrrrrrrrssssssssttttttttuuuuuuuuvvvvvvvvwwwwwwwwxxxxxxxxxyyyyyyyyzzzzzzzz") == [10, 8, 8, 8, 8, 9, 1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 8, 8]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdeabcde") == [14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdeabcde") == [14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggg") == [4, 4, 4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggg") == [4, 4, 4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcadefeghijklmnopqrstuvwxyzzxywvutsrqponmlkjihgfedcba") == [54]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcadefeghijklmnopqrstuvwxyzzxywvutsrqponmlkjihgfedcba") == [54]: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyxzyxzzyxzyxzyxzzyxzyxzyxzzyxzyxzzyxzyxzyxzzyxzyxzyxzzyxzyxzyxzyxzzyxzyxzyxzyx") == [82]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxzyxzzyxzyxzyxzzyxzyxzyxzzyxzyxzzyxzyxzyxzzyxzyxzyxzzyxzyxzyxzyxzzyxzyxzyxzyx") == [82]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzyzxzyzxzyz") == [12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzyzxzyzxzyz") == [12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc") == [30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc") == [30]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabad") == [32]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabad") == [32]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdexyzabcdexyzabcdexyzabcdexyz") == [32]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdexyzabcdexyzabcdexyzabcdexyz") == [32]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghfedcba") == [14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghfedcba") == [14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghihgfedcbaijklmnopqrstuvutsrqponmlkjihgfedcba") == [52]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghihgfedcbaijklmnopqrstuvutsrqponmlkjihgfedcba") == [52]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == [80]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == [80]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyxwvutsrqponmlkjihgfedcba") == [78]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyxwvutsrqponmlkjihgfedcba") == [78]: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == [66]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == [66]: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababcbacadeafgafghijghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == [66]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababcbacadeafgafghijghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == [66]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbaaazzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbaaazzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbaaazzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbaaa") == [212]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbaaazzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbaaazzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbaaazzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbaaa") == [212]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefg") == [21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefg") == [21]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == [70]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == [70]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == [62]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == [62]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghihgfedcba") == [17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghihgfedcba") == [17]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == [63]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == [63]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == [66]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == [66]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 36]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 36]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == [52]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == [52]: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == [30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == [30]: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrsmnopqrstuvwpqrstuv") == [25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrsmnopqrstuvwpqrstuv") == [25]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc") == [18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc") == [18]: {e}')
    
    total += 1
    try:
        result = candidate(s = "lkjihgfedcbaedcba") == [1, 1, 1, 1, 1, 1, 1, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lkjihgfedcbaedcba") == [1, 1, 1, 1, 1, 1, 1, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijkabcdefghijk") == [22]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijkabcdefghijk") == [22]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == [52]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == [52]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefedcbafedcba") == [17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefedcbafedcba") == [17]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbccccdddddeeeeefffffggggghhhhiiiiijjjjkkkkllllmmmmnnnnoooo") == [5, 4, 4, 5, 5, 5, 5, 4, 5, 4, 4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbccccdddddeeeeefffffggggghhhhiiiiijjjjkkkkllllmmmmnnnnoooo") == [5, 4, 4, 5, 5, 5, 5, 4, 5, 4, 4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == [28, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == [28, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == [78]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == [78]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zabacabadefegdehijhklijkmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == [63]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zabacabadefegdehijhklijkmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == [63]: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuabcrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == [47]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuabcrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == [47]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzz") == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzz") == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 18]: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyz") == [12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyz") == [12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == [51]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == [51]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbac") == [64]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbac") == [64]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabababababcabcabcabcdabcdabcdabcdeabcdeabcdefabcdef") == [52]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabababababcabcabcabcdabcdabcdabcdeabcdeabcdefabcdef") == [52]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zababzabz") == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zababzabz") == [9]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffaabbccddeeff") == [24]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffaabbccddeeff") == [24]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhh") == [4, 4, 4, 4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhh") == [4, 4, 4, 4, 4, 4, 4, 4]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abcdabcde") == [8, 1]
    assert candidate(s = "aaaaaabbbbbccccc") == [6, 5, 5]
    assert candidate(s = "xyzxyzxyz") == [9]
    assert candidate(s = "aaaabbbbbccccc") == [4, 5, 5]
    assert candidate(s = "abcdabcdeabcdabcde") == [18]
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    assert candidate(s = "zab") == [1, 1, 1]
    assert candidate(s = "a") == [1]
    assert candidate(s = "zabbcdefghijklmnopqrstuvwxyz") == [28]
    assert candidate(s = "aabbccddeee") == [2, 2, 2, 2, 3]
    assert candidate(s = "abcdcba") == [7]
    assert candidate(s = "ababababab") == [10]
    assert candidate(s = "zabzabc") == [6, 1]
    assert candidate(s = "abababab") == [8]
    assert candidate(s = "abcde") == [1, 1, 1, 1, 1]
    assert candidate(s = "ababcbacadefegdehijhklij") == [9, 7, 8]
    assert candidate(s = "eccbbbbdec") == [10]
    assert candidate(s = "abcabcdabcdeabcdefabcdefg") == [24, 1]
    assert candidate(s = "xyzzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx") == [66]
    assert candidate(s = "aaaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeefffffffffghhhhhhhhiiiiiiiijjjjjjjjkkkkkkkkllllllllmmmmmmmmnnnnnnnnooooooooppppppppqqqqqqqqrrrrrrrrssssssssttttttttuuuuuuuuvvvvvvvvwwwwwwwwxxxxxxxxxyyyyyyyyzzzzzzzz") == [10, 8, 8, 8, 8, 9, 1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 8, 8]
    assert candidate(s = "abcdabcdeabcde") == [14]
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggg") == [4, 4, 4, 4, 4, 4, 4]
    assert candidate(s = "abcadefeghijklmnopqrstuvwxyzzxywvutsrqponmlkjihgfedcba") == [54]
    assert candidate(s = "xyzzyxzyxzzyxzyxzyxzzyxzyxzyxzzyxzyxzzyxzyxzyxzzyxzyxzyxzzyxzyxzyxzyxzzyxzyxzyxzyx") == [82]
    assert candidate(s = "zzyzxzyzxzyz") == [12]
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc") == [30]
    assert candidate(s = "abacabadabacabadabacabadabacabad") == [32]
    assert candidate(s = "abcdexyzabcdexyzabcdexyzabcdexyz") == [32]
    assert candidate(s = "abcdefghfedcba") == [14]
    assert candidate(s = "abcdefghihgfedcbaijklmnopqrstuvutsrqponmlkjihgfedcba") == [52]
    assert candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == [80]
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyxwvutsrqponmlkjihgfedcba") == [78]
    assert candidate(s = "mnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == [66]
    assert candidate(s = "ababcbacadeafgafghijghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == [66]
    assert candidate(s = "zzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbaaazzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbaaazzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbaaazzzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbaaa") == [212]
    assert candidate(s = "abcdefgabcdefgabcdefg") == [21]
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == [70]
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == [62]
    assert candidate(s = "abcdefghihgfedcba") == [17]
    assert candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == [63]
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == [66]
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 36]
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == [52]
    assert candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == [30]
    assert candidate(s = "mnopqrsmnopqrstuvwpqrstuv") == [25]
    assert candidate(s = "abcabcabcabcabcabc") == [18]
    assert candidate(s = "lkjihgfedcbaedcba") == [1, 1, 1, 1, 1, 1, 1, 10]
    assert candidate(s = "abcdefghijkabcdefghijk") == [22]
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == [52]
    assert candidate(s = "abcdefedcbafedcba") == [17]
    assert candidate(s = "aaaaabbbbccccdddddeeeeefffffggggghhhhiiiiijjjjkkkkllllmmmmnnnnoooo") == [5, 4, 4, 5, 5, 5, 5, 4, 5, 4, 4, 4, 4, 4, 4]
    assert candidate(s = "mnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == [28, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == [78]
    assert candidate(s = "zabacabadefegdehijhklijkmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == [63]
    assert candidate(s = "mnopqrstuabcrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == [47]
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzz") == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 18]
    assert candidate(s = "xyzxyzxyzxyz") == [12]
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == [51]
    assert candidate(s = "abacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbac") == [64]
    assert candidate(s = "aabababababcabcabcabcdabcdabcdabcdeabcdeabcdefabcdef") == [52]
    assert candidate(s = "zababzabz") == [9]
    assert candidate(s = "aabbccddeeffaabbccddeeff") == [24]
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhh") == [4, 4, 4, 4, 4, 4, 4, 4]


