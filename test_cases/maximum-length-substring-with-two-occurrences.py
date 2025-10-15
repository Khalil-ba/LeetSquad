def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbccc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbccc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabacbebebe") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabacbebebe") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbc") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbc") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabacbacbac") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabacbacbac") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzyyxx") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzyyxx") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbbbcba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbbbcba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabad") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabad") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghh") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghh") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcde") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcde") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijj") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijj") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaabbbaaaabbbaaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaabbbaaaabbbaaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacaba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacaba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghij") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghij") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccaaaabbbbccccaaaabbbbccccaaaabbbbccccaaaabbbbcccc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccaaaabbbbccccaaaabbbbccccaaaabbbbccccaaaabbbbcccc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrsmnopqrsmnopqrsmnopqrsmnopqrsmnopqrsmnopqrsmnopqrsmnopqrs") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrsmnopqrsmnopqrsmnopqrsmnopqrsmnopqrsmnopqrsmnopqrsmnopqrs") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdeabcdabcdeabcdabcdeabcdabcdeabcdabcdeabcdabcdeabcdabcdeabcdabcdabcdabcd") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdeabcdabcdeabcdabcdeabcdabcdeabcdabcdeabcdabcdeabcdabcdeabcdabcdabcdabcd") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddeeefffggghhhiiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddeeefffggghhhiiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyxwvutsrqponmlkjihgfedcba") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyxwvutsrqponmlkjihgfedcba") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzz") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzz") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabadabacabad") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabadabacabad") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddeeefffggghhhiiijjjkkklllmmmnnnoooppqqrrrsssttuuvvwwxxyyzz") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddeeefffggghhhiiijjjkkklllmmmnnnoooppqqrrrsssttuuvvwwxxyyzz") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzz") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzz") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzyzyzyzyzyzyzy") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzyzyzyzyzyzyzy") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcbacbacbabcabcabcabcabcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcbacbacbabcabcabcabcabcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdef") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdef") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabccddeeffaabbccddeeffaabbccddeeff") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabccddeeffaabbccddeeffaabbccddeeff") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyyxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyyxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvabcdefghijklmnopqrstuv") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvabcdefghijklmnopqrstuv") == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 20: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "zzzzzzzzz") == 2
    assert candidate(s = "aaabbbccc") == 4
    assert candidate(s = "aabbaa") == 4
    assert candidate(s = "abababab") == 4
    assert candidate(s = "aabacbebebe") == 6
    assert candidate(s = "abacabadabacaba") == 5
    assert candidate(s = "abab") == 4
    assert candidate(s = "abcabcabc") == 6
    assert candidate(s = "aabbc") == 5
    assert candidate(s = "aabacbacbac") == 6
    assert candidate(s = "ababababab") == 4
    assert candidate(s = "abcabc") == 6
    assert candidate(s = "aabb") == 4
    assert candidate(s = "zzzzyyxx") == 6
    assert candidate(s = "xyzxyzxyz") == 6
    assert candidate(s = "bcbbbcba") == 4
    assert candidate(s = "zzzzzzzzzz") == 2
    assert candidate(s = "zzzzzzzzzzzz") == 2
    assert candidate(s = "abacabad") == 5
    assert candidate(s = "abababababab") == 4
    assert candidate(s = "aabbccddeeffgg") == 14
    assert candidate(s = "aaabbb") == 4
    assert candidate(s = "aaaa") == 2
    assert candidate(s = "aabbccddeeffgghh") == 16
    assert candidate(s = "aabbccddeeff") == 12
    assert candidate(s = "abcdeabcde") == 10
    assert candidate(s = "aabbcc") == 6
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 52
    assert candidate(s = "aabbccddeeffgghhiijj") == 20
    assert candidate(s = "abacaba") == 5
    assert candidate(s = "abcdefg") == 7
    assert candidate(s = "aaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbbaaabbb") == 4
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzz") == 52
    assert candidate(s = "aabbaaabbbaaaabbbaaaa") == 4
    assert candidate(s = "abacabadabacabadabacaba") == 5
    assert candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghij") == 20
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 6
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 6
    assert candidate(s = "aaaabbbbccccaaaabbbbccccaaaabbbbccccaaaabbbbccccaaaabbbbcccc") == 4
    assert candidate(s = "mnopqrsmnopqrsmnopqrsmnopqrsmnopqrsmnopqrsmnopqrsmnopqrsmnopqrs") == 14
    assert candidate(s = "abcdabcdeabcdabcdeabcdabcdeabcdabcdeabcdabcdeabcdabcdeabcdabcdeabcdabcdabcdabcd") == 10
    assert candidate(s = "aaabbbcccdddeeefffggghhhiiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz") == 4
    assert candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabb") == 4
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 6
    assert candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabb") == 4
    assert candidate(s = "abcdefghijklaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 52
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 52
    assert candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 20
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyxwvutsrqponmlkjihgfedcba") == 52
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 6
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 2
    assert candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabb") == 4
    assert candidate(s = "xyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzzyxyzzz") == 5
    assert candidate(s = "abacabadabacabadabacabadabacabadabacabad") == 5
    assert candidate(s = "aaabbbcccdddeeefffggghhhiiijjjkkklllmmmnnnoooppqqrrrsssttuuvvwwxxyyzz") == 16
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzz") == 27
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 52
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 52
    assert candidate(s = "zzzzzyzyzyzyzyzyzy") == 4
    assert candidate(s = "abcabcbacbacbabcabcabcabcabcabcabc") == 6
    assert candidate(s = "abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdef") == 12
    assert candidate(s = "abcabcabcabcabcabc") == 6
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 2
    assert candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 52
    assert candidate(s = "aabccddeeffaabbccddeeffaabbccddeeff") == 12
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyyxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == 52
    assert candidate(s = "abcdefghijklmnopqrstuvabcdefghijklmnopqrstuv") == 44
    assert candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba") == 4
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzz") == 52
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzz") == 52
    assert candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabb") == 4
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 8
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 6
    assert candidate(s = "abcabcabcabcabc") == 6
    assert candidate(s = "abcdaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 52
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 8
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 6
    assert candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 20


