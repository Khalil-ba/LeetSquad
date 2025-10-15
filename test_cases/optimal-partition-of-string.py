def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abcdefg") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abac") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abac") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdeabcdefabcdefg") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdeabcdefabcdefg") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "optimal") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "optimal") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "ssssss") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ssssss") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "ab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "partition") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "partition") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcadef") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcadef") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "pqrspqrspqrs") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pqrspqrspqrs") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcde") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcde") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "unique") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "unique") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "characters") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "characters") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaa") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaa") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abca") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abca") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zxyxzyxz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxyxzyxz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzxy") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzxy") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcdeabcdeabcde") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcdeabcdeabcde") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxxyxyxyxxyxyxyxyxyx") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxxyxyxyxxyxyxyxyxyx") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "repeatrepeatrepeatrepeatrepeat") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeatrepeatrepeatrepeatrepeat") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "uniquecharacterswithoutrepeating") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uniquecharacterswithoutrepeating") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabaeabacabafabacabadabacabaeabacabaf") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabaeabacabafabacabadabacabaeabacabaf") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabaf") == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabaf") == 72: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabad") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabad") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbccccdddd") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbccccdddd") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdeabcdabcdef") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdeabcdabcdef") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiijjjjjjkkkkkkklllllllmmmmmmmnnnnnnnooooooooppppppppqqqqqqqqrrrrrrrrssssssssttttttttuuuuuuuuvvvvvvvvwwwwwwwwxxxxxxxxxyyyyyyyyzzzzzzzz") == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiijjjjjjkkkkkkklllllllmmmmmmmnnnnnnnooooooooppppppppqqqqqqqqrrrrrrrrssssssssttttttttuuuuuuuuvvvvvvvvwwwwwwwwxxxxxxxxxyyyyyyyyzzzzzzzz") == 145: {e}')
    
    total += 1
    try:
        result = candidate(s = "longerstringwithoutrepeats") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longerstringwithoutrepeats") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippimississippimississippi") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippimississippimississippi") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbcccccdddddeeeeeeaaaaabbbbbcccccdddddeeeeeeaaaaabbbbbcccccdddddeeeeeeaaaaabbbbbcccccdddddeeeeee") == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbcccccdddddeeeeeeaaaaabbbbbcccccdddddeeeeeeaaaaabbbbbcccccdddddeeeeeeaaaaabbbbbcccccdddddeeeeee") == 85: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbcccccdddddeeeee") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbcccccdddddeeeee") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabraabracadabraabracadabra") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabraabracadabraabracadabra") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeeffffffffgggggggghhhhhhhh") == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeeffffffffgggggggghhhhhhhh") == 59: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "noon") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noon") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringthatwilltestthealgorithm") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringthatwilltestthealgorithm") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohellohellohellohello") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohellohellohellohello") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzz") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzz") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcbaabcdedcbaabcdedcbaabcdedcbaabcdedcbaabcdedcbaabcdedcbaabcdedcbaabcdedcbaabcdedcba") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcbaabcdedcbaabcdedcbaabcdedcbaabcdedcbaabcdedcbaabcdedcbaabcdedcbaabcdedcbaabcdedcba") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaxbabax") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaxbabax") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaabbbbbbbbccccccccddddddddeeeeeeee") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaabbbbbbbbccccccccddddddddeeeeeeee") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "thecuriouscaseofjeffersonraisethetrapdoor") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thecuriouscaseofjeffersonraisethetrapdoor") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefghijklmnopqrstuvwxyz") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefghijklmnopqrstuvwxyz") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 70: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbccccddddeeeeffffgggg") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbccccddddeeeeffffgggg") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzysabcabcabcabcabcabcabcabc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzysabcabcabcabcabcabcabcabc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklaaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklaaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabraabracadabra") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabraabracadabra") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababcbabcab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababcbabcab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabad") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabad") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 61: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabaf") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabaf") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffaabbccddeeff") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffaabbccddeeff") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcd") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcd") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisanexamplestringthatneedstobepartitionedproperly") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisanexamplestringthatneedstobepartitionedproperly") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabaeabacabaf") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabaeabacabaf") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabaf") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabaf") == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabcbcbcbaabcabcbcbcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcbcbcbaabcabcbcbcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrsmnopqrsmnopqrsmnopqrs") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrsmnopqrsmnopqrsmnopqrs") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbcccddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnoooo") == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbcccddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnoooo") == 43: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabc") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabc") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabaf") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabaf") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "ppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxxyyyyzzzz") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxxyyyyzzzz") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzxyzzxyzzxyzzxyzzxyzz") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzxyzzxyzzxyzzxyzzxyzz") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzz") == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzz") == 43: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbbbaaaabbbbbbbaaaabbbbbbbaaaabbbbb") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbbbaaaabbbbbbbaaaabbbbbbbaaaabbbbb") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 50: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abcdefg") == 1
    assert candidate(s = "abac") == 2
    assert candidate(s = "abcdabcdeabcdefabcdefg") == 4
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 44
    assert candidate(s = "abababab") == 4
    assert candidate(s = "aaaaa") == 5
    assert candidate(s = "a") == 1
    assert candidate(s = "optimal") == 1
    assert candidate(s = "abcabcabc") == 3
    assert candidate(s = "ssssss") == 6
    assert candidate(s = "abcabcabcabc") == 4
    assert candidate(s = "ab") == 1
    assert candidate(s = "partition") == 2
    assert candidate(s = "racecar") == 2
    assert candidate(s = "xyzxyzxyz") == 3
    assert candidate(s = "abcadef") == 2
    assert candidate(s = "banana") == 3
    assert candidate(s = "abc") == 1
    assert candidate(s = "pqrspqrspqrs") == 3
    assert candidate(s = "aabbccddeeff") == 7
    assert candidate(s = "abcdeabcde") == 2
    assert candidate(s = "aabbcc") == 4
    assert candidate(s = "unique") == 2
    assert candidate(s = "characters") == 2
    assert candidate(s = "aaaaaaaaa") == 9
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 27
    assert candidate(s = "abacaba") == 4
    assert candidate(s = "abca") == 2
    assert candidate(s = "zxyxzyxz") == 3
    assert candidate(s = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzxy") == 40
    assert candidate(s = "abcdeabcdeabcdeabcdeabcde") == 5
    assert candidate(s = "xyxxyxyxyxxyxyxyxyxyx") == 12
    assert candidate(s = "repeatrepeatrepeatrepeatrepeat") == 10
    assert candidate(s = "uniquecharacterswithoutrepeating") == 6
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 23
    assert candidate(s = "abacabadabacabaeabacabafabacabadabacabaeabacabaf") == 24
    assert candidate(s = "abacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabaf") == 72
    assert candidate(s = "abacabadabacabad") == 8
    assert candidate(s = "aaaaabbbbbccccdddd") == 15
    assert candidate(s = "abcdabcdeabcdabcdef") == 4
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiijjjjjjkkkkkkklllllllmmmmmmmnnnnnnnooooooooppppppppqqqqqqqqrrrrrrrrssssssssttttttttuuuuuuuuvvvvvvvvwwwwwwwwxxxxxxxxxyyyyyyyyzzzzzzzz") == 145
    assert candidate(s = "longerstringwithoutrepeats") == 5
    assert candidate(s = "abcba") == 2
    assert candidate(s = "mississippimississippimississippi") == 15
    assert candidate(s = "aaaaabbbbbcccccdddddeeeeeeaaaaabbbbbcccccdddddeeeeeeaaaaabbbbbcccccdddddeeeeeeaaaaabbbbbcccccdddddeeeeee") == 85
    assert candidate(s = "aaaaabbbbbcccccdddddeeeee") == 21
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 30
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 16
    assert candidate(s = "abracadabraabracadabraabracadabra") == 15
    assert candidate(s = "aaaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeeffffffffgggggggghhhhhhhh") == 59
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 29
    assert candidate(s = "noon") == 2
    assert candidate(s = "abcabcabcabcabcabc") == 6
    assert candidate(s = "thisisaverylongstringthatwilltestthealgorithm") == 9
    assert candidate(s = "hellohellohellohellohellohello") == 12
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzz") == 24
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm") == 4
    assert candidate(s = "abcdedcbaabcdedcbaabcdedcbaabcdedcbaabcdedcbaabcdedcbaabcdedcbaabcdedcbaabcdedcbaabcdedcba") == 20
    assert candidate(s = "abacdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 3
    assert candidate(s = "abacaxbabax") == 5
    assert candidate(s = "aaaaaaaabbbbbbbbccccccccddddddddeeeeeeee") == 36
    assert candidate(s = "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn") == 40
    assert candidate(s = "abababababababababab") == 10
    assert candidate(s = "abacabadabacaba") == 8
    assert candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad") == 36
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 3
    assert candidate(s = "thecuriouscaseofjeffersonraisethetrapdoor") == 8
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefghijklmnopqrstuvwxyz") == 28
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 70
    assert candidate(s = "aaaaabbbbbccccddddeeeeffffgggg") == 24
    assert candidate(s = "xyzzysabcabcabcabcabcabcabcabc") == 9
    assert candidate(s = "abcdefghijklaaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 38
    assert candidate(s = "abracadabraabracadabra") == 10
    assert candidate(s = "ababcbabcab") == 5
    assert candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabad") == 28
    assert candidate(s = "mnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 61
    assert candidate(s = "abacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabaf") == 36
    assert candidate(s = "aabbccddeeffaabbccddeeff") == 13
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 1
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 40
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 1
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcd") == 9
    assert candidate(s = "thisisanexamplestringthatneedstobepartitionedproperly") == 9
    assert candidate(s = "abacabadabacabaeabacabaf") == 12
    assert candidate(s = "abacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabaf") == 60
    assert candidate(s = "aabcbcbcbaabcabcbcbcba") == 10
    assert candidate(s = "mnopqrsmnopqrsmnopqrsmnopqrs") == 4
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm") == 2
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd") == 8
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 5
    assert candidate(s = "aaaaaabbcccddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnoooo") == 43
    assert candidate(s = "abcabcabcabcabcabcabcabc") == 8
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 2
    assert candidate(s = "abcdabcdaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 29
    assert candidate(s = "abacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabafabacabadabacabaeabacabaf") == 48
    assert candidate(s = "ppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxxyyyyzzzz") == 35
    assert candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 29
    assert candidate(s = "xyzzxyzzxyzzxyzzxyzzxyzz") == 12
    assert candidate(s = "mississippi") == 5
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzz") == 43
    assert candidate(s = "abcabcabcabcabc") == 5
    assert candidate(s = "aaaaabbbbbbbaaaabbbbbbbaaaabbbbbbbaaaabbbbb") == 36
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 50


