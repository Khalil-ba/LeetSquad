def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abcdeabcde") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcde") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzz") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzz") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyx") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyx") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabc") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabc") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abab") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abab") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabc") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabc") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbccc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbccc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabad") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabad") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghij") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghij") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrsmnopqrsmnopqrsmnopqrsmnopqrsmnopqrs") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrsmnopqrsmnopqrsmnopqrsmnopqrsmnopqrs") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgihgfedcba") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgihgfedcba") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcde") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcde") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopmnopmnop") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopmnopmnop") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaabbbaaabbbaaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaabbbaaabbbaaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbbbbccccccccdddddd") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbbbbccccccccdddddd") == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeffedcbaa") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeffedcbaa") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzxyz") == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzxyz") == 53: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzz") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzz") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdeabcdabcdeabcd") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdeabcdabcdeabcd") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdefabcdefabcdef") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdefabcdefabcdef") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrsmnopqrsmnopqrs") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrsmnopqrsmnopqrs") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefg") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefg") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstmnopqrstmnopqrstmnopqrstmnopqrstmnopqrst") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstmnopqrstmnopqrstmnopqrstmnopqrstmnopqrst") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgihgfedcbamnopqrsmnopqrsmnopqrs") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgihgfedcbamnopqrsmnopqrsmnopqrs") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzab") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzab") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefghijklmnopqrstuvwxyz") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefghijklmnopqrstuvwxyz") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabadabacabad") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabadabacabad") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabc") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabc") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababab") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababab") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefg") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefg") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghij") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghij") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdefabcdef") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdefabcdef") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababababababababababababababababababab") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababababababababababababababababababab") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabc") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabc") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababab") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababab") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwzyxwzyxwzyxwzyxwzyxwzyxwzyxwzyxwzyxw") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwzyxwzyxwzyxwzyxwzyxwzyxwzyxwzyxwzyxw") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijkabcdefghijk") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijkabcdefghijk") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababab") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababab") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabac") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabac") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhii") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhii") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvwxyz") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvwxyz") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefgabcdefgh") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefgabcdefgh") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeffedcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeffedcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdeabcdeabcde") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdeabcdeabcde") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddcccbbaaa") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddcccbbaaa") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzxy") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzxy") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyqwertyqwertyqwerty") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyqwertyqwertyqwerty") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyabcdefghijklmnopqrstuvwxy") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyabcdefghijklmnopqrstuvwxy") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcdeabcdeabcdeabcde") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcdeabcdeabcdeabcde") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyz") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyz") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabcxyzabcxyzabcxyzabc") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabcxyzabcxyzabcxyzabc") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstmnopqrstmnopqrstmnopqrst") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstmnopqrstmnopqrstmnopqrst") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcfdefgdefgdefg") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcfdefgdefgdefg") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabb") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabb") == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abcdeabcde") == -1
    assert candidate(s = "abba") == 2
    assert candidate(s = "zzzzzz") == -1
    assert candidate(s = "aabbcc") == 4
    assert candidate(s = "abacabadabacaba") == 1
    assert candidate(s = "abcabcabcabc") == -1
    assert candidate(s = "xyzzyx") == 4
    assert candidate(s = "abacd") == 4
    assert candidate(s = "abcdef") == 5
    assert candidate(s = "aabbccddeeff") == 10
    assert candidate(s = "abcdeabc") == 2
    assert candidate(s = "xyzabc") == 5
    assert candidate(s = "aaaa") == -1
    assert candidate(s = "abab") == -1
    assert candidate(s = "abcabcabcabcabcabcabc") == -1
    assert candidate(s = "aaabbbccc") == 6
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == -1
    assert candidate(s = "abacabadabacabadabacabad") == -1
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 25
    assert candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghij") == -1
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == -1
    assert candidate(s = "mnopqrsmnopqrsmnopqrsmnopqrsmnopqrsmnopqrs") == -1
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 60
    assert candidate(s = "abcdefgihgfedcba") == 14
    assert candidate(s = "abcdabcde") == 8
    assert candidate(s = "mnopmnopmnop") == -1
    assert candidate(s = "aabbaaabbbaaabbbaaa") == -1
    assert candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == -1
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc") == -1
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbbbbccccccccdddddd") == 31
    assert candidate(s = "abcdeffedcbaa") == 10
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzxyz") == 53
    assert candidate(s = "zzzzzzzzzzzzzzz") == -1
    assert candidate(s = "abcdabcdeabcdabcdeabcd") == -1
    assert candidate(s = "abcdefabcdefabcdefabcdefabcdef") == -1
    assert candidate(s = "mnopqrsmnopqrsmnopqrs") == -1
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz") == -1
    assert candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == -1
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd") == -1
    assert candidate(s = "abcdefgabcdefgabcdefg") == -1
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 30
    assert candidate(s = "mnopqrstmnopqrstmnopqrstmnopqrstmnopqrstmnopqrst") == -1
    assert candidate(s = "abcdefgihgfedcbamnopqrsmnopqrsmnopqrs") == 21
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzab") == 48
    assert candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == -1
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz") == 50
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefghijklmnopqrstuvwxyz") == -1
    assert candidate(s = "abacabadabacabadabacabadabacabadabacabad") == -1
    assert candidate(s = "abcabcabcabcabcabcabcabcabc") == -1
    assert candidate(s = "ababababababababababababababab") == -1
    assert candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefg") == -1
    assert candidate(s = "abcdefghijabcdefghij") == -1
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == -1
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 50
    assert candidate(s = "abcdefabcdefabcdefabcdef") == -1
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == -1
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 52
    assert candidate(s = "abcdabcdabcd") == -1
    assert candidate(s = "abababababababababababababababababababababababababababababababab") == -1
    assert candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == -1
    assert candidate(s = "abcabcabcabcabcabcabcabc") == -1
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc") == -1
    assert candidate(s = "abababababab") == -1
    assert candidate(s = "zyxwzyxwzyxwzyxwzyxwzyxwzyxwzyxwzyxwzyxw") == -1
    assert candidate(s = "abcdefgabcdefg") == -1
    assert candidate(s = "abcdefghijkabcdefghijk") == -1
    assert candidate(s = "abababababababababababababababab") == -1
    assert candidate(s = "abacabadabac") == 1
    assert candidate(s = "aabbccddeeffgghhii") == 16
    assert candidate(s = "mnopqrstuvwxyz") == 13
    assert candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 54
    assert candidate(s = "abcdefgabcdefgabcdefgabcdefgh") == 28
    assert candidate(s = "abcdeffedcba") == 10
    assert candidate(s = "abcdabcdeabcdeabcde") == -1
    assert candidate(s = "aaabbbcccdddcccbbaaa") == 14
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzxy") == 51
    assert candidate(s = "qwertyqwertyqwertyqwerty") == -1
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == -1
    assert candidate(s = "abcdefghijklmnopqrstuvwxyabcdefghijklmnopqrstuvwxy") == -1
    assert candidate(s = "abcdeabcdeabcdeabcdeabcdeabcde") == -1
    assert candidate(s = "xyzxyzxyzxyz") == -1
    assert candidate(s = "xyzabcxyzabcxyzabcxyzabc") == -1
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 50
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == -1
    assert candidate(s = "mnopqrstmnopqrstmnopqrstmnopqrst") == -1
    assert candidate(s = "abcabcabcabcfdefgdefgdefg") == 13
    assert candidate(s = "aabbaabbaabbaabb") == -1


