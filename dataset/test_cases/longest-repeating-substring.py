def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "pypypypypypypypypyp") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pypypypypypypypypyp") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabcaabdaab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcaabdaab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohello") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohello") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyz") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyz") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "pwwkewpwwkewpwwkew") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pwwkewpwwkewpwwkew") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "acacacacacacac") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acacacacacacac") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffaabbccddeeffaabbccddeeff") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffaabbccddeeffaabbccddeeff") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithrepeatingthisisaverylong") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithrepeatingthisisaverylong") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyzxyz") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyzxyz") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaa") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaa") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghij") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghij") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxxyxyxyxyxyxyxyxyxyxxyxyxyxyx") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxxyxyxyxyxyxyxyxyxyxxyxyxyxyx") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabad") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabad") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaananabananabanana") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaananabananabanana") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbacbcba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbacbcba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zabzabzabzabzab") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zabzabzabzabzab") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippimississippi") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippimississippi") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabcdabcabcd") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabcdabcabcd") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaananabanana") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaananabanana") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabc") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabc") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabaaaabaaaabaaaab") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabaaaabaaaabaaaab") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopqwertyuiop") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopqwertyuiop") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaananaban") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaananaban") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcababcababcab") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcababcababcab") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississipississippi") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississipississippi") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabcxyzabcxyz") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabcxyzabcxyz") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabraabracadabraabracadabra") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabraabracadabraabracadabra") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababab") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababab") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "anappleapernapple") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "anappleapernapple") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabcdabcdabc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabcdabcdabc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertqwertyuiopasdfghjklzxcvbnm") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertqwertyuiopasdfghjklzxcvbnm") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxxyxyxyxyx") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxxyxyxyxyx") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbaaaabbbaaa") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbaaaabbbaaa") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbcbcbcbcbcbcb") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbcbcbcbcbcbcb") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghiabcdefghi") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghiabcdefghi") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyz") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyz") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "pqrstpqrstpqrstpqrst") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pqrstpqrstpqrstpqrst") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabcabcd") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabcabcd") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcdeabcde") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcdeabcde") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaananabanananaban") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaananabanananaban") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijkabcdefghij") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijkabcdefghij") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabraabracadabra") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabraabracadabra") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyz") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyz") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxyxyxyxyxyxyxy") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxyxyxyxyxyxyxy") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbccccddddd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbccccddddd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghabcdefghabcdefgh") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghabcdefghabcdefgh") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffaabbccddeeff") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffaabbccddeeff") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabad") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabad") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabcaabdaabaabcaabdaabaabcaabdaab") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcaabdaabaabcaabdaabaabcaabdaab") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaananabananan") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaananabananan") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcde") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcde") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyz") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyz") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "repeatedrepeatedrepeated") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeatedrepeatedrepeated") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefg") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefg") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghij") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghij") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabc") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabc") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "zxyxzyzyzxzyzyzyzxzyzyzyz") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxyxzyzyzxzyzyzyzxzyzyzyz") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghabcdefgh") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghabcdefgh") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "pqpqppqpqppqpqpqpqppqp") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pqpqppqpqppqpqpqpqppqp") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefggfedcbabcdefggfedcb") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefggfedcbabcdefggfedcb") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzxyzzxyzzxyzzxyzzxyzz") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzxyzzxyzzxyzzxyzzxyzz") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaab") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaab") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqmnopqmnopqmnopq") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqmnopqmnopqmnopq") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertqwertqwert") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertqwertqwert") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzyzxyzxyzyz") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzyzxyzxyzyz") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabada") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabada") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "repeatedrepeatedrepeatedrepeatedrepeated") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeatedrepeatedrepeatedrepeatedrepeated") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "pqpqppqpqppqpqp") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pqpqppqpqppqpqp") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "ananananaanana") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ananananaanana") == 7: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "pypypypypypypypypyp") == 17
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 0
    assert candidate(s = "abababab") == 6
    assert candidate(s = "abcabcabc") == 6
    assert candidate(s = "abracadabra") == 4
    assert candidate(s = "abcabcabcabc") == 9
    assert candidate(s = "abcdabcabc") == 3
    assert candidate(s = "abbaba") == 2
    assert candidate(s = "xyzxyzxyz") == 6
    assert candidate(s = "banana") == 3
    assert candidate(s = "aabcaabdaab") == 3
    assert candidate(s = "abcdefgabcdefg") == 7
    assert candidate(s = "abcdefgh") == 0
    assert candidate(s = "abcd") == 0
    assert candidate(s = "hellohello") == 5
    assert candidate(s = "aaaa") == 3
    assert candidate(s = "mississippi") == 4
    assert candidate(s = "xyzxyzxyzxyz") == 9
    assert candidate(s = "abcdefg") == 0
    assert candidate(s = "pwwkewpwwkewpwwkew") == 12
    assert candidate(s = "acacacacacacac") == 12
    assert candidate(s = "aabbccddeeffaabbccddeeffaabbccddeeff") == 24
    assert candidate(s = "thisisaverylongstringwithrepeatingthisisaverylong") == 15
    assert candidate(s = "abcdeabcd") == 4
    assert candidate(s = "xyzxyzxyzxyzxyzxyzxyz") == 18
    assert candidate(s = "aaaaaaaaaa") == 9
    assert candidate(s = "abcdefghijabcdefghijabcdefghij") == 20
    assert candidate(s = "abcdabcdabcd") == 8
    assert candidate(s = "xyxxyxyxyxyxyxyxyxyxyxxyxyxyxyx") == 17
    assert candidate(s = "abacabadabacabad") == 8
    assert candidate(s = "bananaananabananabanana") == 11
    assert candidate(s = "abcbacbcba") == 4
    assert candidate(s = "zabzabzabzabzab") == 12
    assert candidate(s = "mississippimississippi") == 11
    assert candidate(s = "abcdabcabcdabcabcd") == 11
    assert candidate(s = "bananaananabanana") == 6
    assert candidate(s = "abcabcabcabcabcabcabc") == 18
    assert candidate(s = "aaaaabaaaabaaaabaaaab") == 15
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 36
    assert candidate(s = "qwertyuiopqwertyuiop") == 10
    assert candidate(s = "bananaananaban") == 5
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 27
    assert candidate(s = "abcababcababcab") == 10
    assert candidate(s = "mississipississippi") == 8
    assert candidate(s = "xyzabcxyzabcxyz") == 9
    assert candidate(s = "abracadabraabracadabraabracadabra") == 22
    assert candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == 27
    assert candidate(s = "ababababababababab") == 16
    assert candidate(s = "anappleapernapple") == 6
    assert candidate(s = "abcdabcabcdabcdabc") == 7
    assert candidate(s = "abcabcabcabcabcabc") == 15
    assert candidate(s = "qwertqwertyuiopasdfghjklzxcvbnm") == 5
    assert candidate(s = "xyxxyxyxyxyx") == 7
    assert candidate(s = "aaaaabbbaaaabbbaaa") == 10
    assert candidate(s = "aaaaaaa") == 6
    assert candidate(s = "abcbcbcbcbcbcbcb") == 13
    assert candidate(s = "aaaaa") == 4
    assert candidate(s = "abacabadabacaba") == 7
    assert candidate(s = "abcdefghiabcdefghi") == 9
    assert candidate(s = "xyzxyzxyzxyzxyzxyz") == 15
    assert candidate(s = "pqrstpqrstpqrstpqrst") == 15
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 19
    assert candidate(s = "abcdabcabcabcd") == 6
    assert candidate(s = "abcdeabcdeabcdeabcde") == 15
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop") == 10
    assert candidate(s = "bananaananabanananaban") == 8
    assert candidate(s = "abcdefghijkabcdefghij") == 10
    assert candidate(s = "abracadabraabracadabra") == 11
    assert candidate(s = "xyzxyzxyzxyzxyz") == 12
    assert candidate(s = "xyxyxyxyxyxyxyxyxyxyxy") == 20
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1
    assert candidate(s = "aaaaabbbbbccccddddd") == 4
    assert candidate(s = "abcdefghabcdefghabcdefgh") == 16
    assert candidate(s = "aabbccddeeffaabbccddeeff") == 12
    assert candidate(s = "abacabadabacabadabacabad") == 16
    assert candidate(s = "aabcaabdaabaabcaabdaabaabcaabdaab") == 22
    assert candidate(s = "bananaananabananan") == 6
    assert candidate(s = "abcdeabcdeabcde") == 10
    assert candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyz") == 21
    assert candidate(s = "repeatedrepeatedrepeated") == 16
    assert candidate(s = "abcdefgabcdefgabcdefg") == 14
    assert candidate(s = "abcdefghijabcdefghij") == 10
    assert candidate(s = "abcabcabcabcabcabcabcabc") == 21
    assert candidate(s = "zxyxzyzyzxzyzyzyzxzyzyzyz") == 13
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 26
    assert candidate(s = "abcdefghabcdefgh") == 8
    assert candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis") == 2
    assert candidate(s = "pqpqppqpqppqpqpqpqppqp") == 10
    assert candidate(s = "abcdefggfedcbabcdefggfedcb") == 13
    assert candidate(s = "xyzzxyzzxyzzxyzzxyzzxyzz") == 20
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaab") == 21
    assert candidate(s = "mnopqmnopqmnopqmnopq") == 15
    assert candidate(s = "qwertqwertqwert") == 10
    assert candidate(s = "xyzxyzyzxyzxyzyz") == 8
    assert candidate(s = "abacabadabacabadabacabada") == 17
    assert candidate(s = "abcabcabcabcabc") == 12
    assert candidate(s = "repeatedrepeatedrepeatedrepeatedrepeated") == 32
    assert candidate(s = "pqpqppqpqppqpqp") == 10
    assert candidate(s = "ananananaanana") == 7


