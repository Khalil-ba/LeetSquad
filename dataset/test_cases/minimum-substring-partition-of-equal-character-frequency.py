def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbccc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbccc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddccdd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddccdd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghi") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghi") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "ab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdef") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdef") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababaccddb") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababaccddb") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "fabccddg") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "fabccddg") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijj") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijj") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabad") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabad") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabb") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabb") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefggfedcbafedcbafedcba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefggfedcbafedcbafedcba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcdeefgghhijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcdeefgghhijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeffgg") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeffgg") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzyyyyxxxxwwwwvvvuuutttsssrqqppoonnmmllkkjjiihhhgggfffeeedddcccbbaa") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzyyyyxxxxwwwwvvvuuutttsssrqqppoonnmmllkkjjiihhhgggfffeeedddcccbbaa") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddcccbbbbaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddcccbbbbaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzyyyyxxxxwwwwvvvuuutttsssrqqppoonnmmllkkjjiihhhgggfffeeedddcccbbaa") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzyyyyxxxxwwwwvvvuuutttsssrqqppoonnmmllkkjjiihhhgggfffeeedddcccbbaa") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdefabcdefabcdef") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdefabcdefabcdef") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghabcdefghabcdefghabcdefgh") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghabcdefghabcdefghabcdefgh") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefghijklmnopqrstuvwxyz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefghijklmnopqrstuvwxyz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaabbbaaaabbbcccdddeeefffggg") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaabbbaaaabbbcccdddeeefffggg") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefgabcdefg") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefgabcdefg") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbccccddddeeeeeffffffgggggghhhhhiiiiijjjjjkkkkklllllmmmmmnnnnnooooo") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbccccddddeeeeeffffffgggggghhhhhiiiiijjjjjkkkkklllllmmmmmnnnnnooooo") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaabb") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaabb") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdefabcdef") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdefabcdef") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "qqwweerrttyyuuuuummmiiiinnnngggg") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qqwweerrttyyuuuuummmiiiinnnngggg") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefg") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefg") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzyyyyxxxxwwwwvvvuuutttsssrqqppoonnmmllkkjjiihhhgggfffeeedddcccbbaa") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzyyyyxxxxwwwwvvvuuutttsssrqqppoonnmmllkkjjiihhhgggfffeeedddcccbbaa") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyxwvutsrqponmlkjihgfedcba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyxwvutsrqponmlkjihgfedcba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzyxzzzyxzzzyxzzzyxzzz") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzyxzzzyxzzzyxzzzyxzzz") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccddd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccddd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcababcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcababcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaabbbbbbbbbc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaabbbbbbbbbc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdef") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdef") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffaabbccddeeff") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffaabbccddeeff") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcdabcabcdeabcdefabcdefg") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcdabcabcdeabcdefabcdefg") == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "zzzzzzzzz") == 1
    assert candidate(s = "aaabbbccc") == 1
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 1
    assert candidate(s = "aabbaabbccddccdd") == 1
    assert candidate(s = "abcdef") == 1
    assert candidate(s = "abababab") == 1
    assert candidate(s = "a") == 1
    assert candidate(s = "abcdefghi") == 1
    assert candidate(s = "abacabadabacaba") == 8
    assert candidate(s = "abab") == 1
    assert candidate(s = "abcabcabc") == 1
    assert candidate(s = "ab") == 1
    assert candidate(s = "aa") == 1
    assert candidate(s = "abcdefabcdef") == 1
    assert candidate(s = "abcde") == 1
    assert candidate(s = "abcabc") == 1
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 1
    assert candidate(s = "abababaccddb") == 2
    assert candidate(s = "zzzzzzzzzz") == 1
    assert candidate(s = "abcdabcdabcd") == 1
    assert candidate(s = "fabccddg") == 3
    assert candidate(s = "aabbcc") == 1
    assert candidate(s = "abcdefghij") == 1
    assert candidate(s = "aabbccddeeffgghhiijj") == 1
    assert candidate(s = "abcdabcdabcdabcd") == 1
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 1
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
    assert candidate(s = "abacabadabacabadabacabad") == 12
    assert candidate(s = "aabbaabbaabbaabbaabb") == 1
    assert candidate(s = "abcdefggfedcbafedcbafedcba") == 2
    assert candidate(s = "aabbcdeefgghhijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 6
    assert candidate(s = "aabbaabbccddeeffgg") == 2
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaaa") == 2
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1
    assert candidate(s = "abcdefghijklaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzyyyyxxxxwwwwvvvuuutttsssrqqppoonnmmllkkjjiihhhgggfffeeedddcccbbaa") == 9
    assert candidate(s = "aaabbbcccdddcccbbbbaaa") == 4
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 1
    assert candidate(s = "zzzzzyyyyxxxxwwwwvvvuuutttsssrqqppoonnmmllkkjjiihhhgggfffeeedddcccbbaa") == 7
    assert candidate(s = "abcdefabcdefabcdefabcdefabcdef") == 1
    assert candidate(s = "abcdefghabcdefghabcdefghabcdefgh") == 1
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz") == 1
    assert candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyz") == 1
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd") == 1
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefghijklmnopqrstuvwxyz") == 1
    assert candidate(s = "aabbaaabbbaaaabbbcccdddeeefffggg") == 3
    assert candidate(s = "ababababababababababababababababab") == 1
    assert candidate(s = "abcdefgabcdefgabcdefgabcdefg") == 1
    assert candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 1
    assert candidate(s = "aabbbccccddddeeeeeffffffgggggghhhhhiiiiijjjjjkkkkklllllmmmmmnnnnnooooo") == 6
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaabb") == 2
    assert candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 2
    assert candidate(s = "abcdefabcdefabcdefabcdef") == 1
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 1
    assert candidate(s = "qqwweerrttyyuuuuummmiiiinnnngggg") == 3
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 1
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 1
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 1
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzabcdefg") == 2
    assert candidate(s = "abcabcabcabcabcabc") == 1
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzyyyyxxxxwwwwvvvuuutttsssrqqppoonnmmllkkjjiihhhgggfffeeedddcccbbaa") == 8
    assert candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 3
    assert candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyxwvutsrqponmlkjihgfedcba") == 2
    assert candidate(s = "xyzzzyxzzzyxzzzyxzzzyxzzz") == 10
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1
    assert candidate(s = "aaabbbcccddd") == 1
    assert candidate(s = "abcabcababcabc") == 2
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabc") == 1
    assert candidate(s = "aaaaaaaaaaabbbbbbbbbc") == 3
    assert candidate(s = "abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdef") == 1
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == 3
    assert candidate(s = "aabbccddeeffaabbccddeeff") == 1
    assert candidate(s = "abcabcdabcabcdeabcdefabcdefg") == 5


