def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "zzzzyzyzyyzzyzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzyzyzyyzzyzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abaacbcbb") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abaacbcbb") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeedddccbaa") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeedddccbaa") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcddcba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcddcba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzzzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzzzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeedddccba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeedddccba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgfedcba") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgfedcba") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzyzzyyzzyyzzzzzyyzyzyzyz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzyzzyyzzyyzzzzzyyzyzyzyz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabad") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabad") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaabbbaaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaabbbaaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 7: {e}')
    
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
        result = candidate(s = "aabbccddeeaabbccddeeff") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeaabbccddeeff") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccdd") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccdd") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmnbvcxzlkjhgfdsapoiuytrewqqwertyuiopasdfghjklzxcvbnm") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmnbvcxzlkjhgfdsapoiuytrewqqwertyuiopasdfghjklzxcvbnm") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzxyz") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzxyz") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyxwvutsrqponmlkjihgfedcba") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyxwvutsrqponmlkjihgfedcba") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababababababababababababababababababababababababababab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababababababababababababababababababababababababababab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyxzyzxzyzyzyzyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxzyzxzyzyzyzyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbbccccddddeeeeefffffggggghhhhhiiiiijjjjjkkkkklllllmmmmmnnnnnooooo") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbbccccddddeeeeefffffggggghhhhhiiiiijjjjjkkkkklllllmmmmmnnnnnooooo") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "zzzzyzyzyyzzyzz") == 3
    assert candidate(s = "abcba") == 5
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 26
    assert candidate(s = "abaacbcbb") == 5
    assert candidate(s = "aabbaa") == 4
    assert candidate(s = "aabbccddeeeedddccbaa") == 8
    assert candidate(s = "abababab") == 4
    assert candidate(s = "a") == 1
    assert candidate(s = "abacabadabacaba") == 7
    assert candidate(s = "abcabcabc") == 3
    assert candidate(s = "abcabcabcabc") == 6
    assert candidate(s = "aa") == 2
    assert candidate(s = "abcddcba") == 8
    assert candidate(s = "zzzzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzzzz") == 3
    assert candidate(s = "abcde") == 5
    assert candidate(s = "aabb") == 4
    assert candidate(s = "aabbccddeeeedddccba") == 7
    assert candidate(s = "abcdeedcba") == 10
    assert candidate(s = "zzzzzzzzzz") == 2
    assert candidate(s = "abcdefgfedcba") == 13
    assert candidate(s = "abcdabcdabcd") == 4
    assert candidate(s = "zzzyzzyyzzyyzzzzzyyzyzyzyz") == 4
    assert candidate(s = "abacabad") == 6
    assert candidate(s = "aabbaaabbbaaa") == 3
    assert candidate(s = "abcd") == 4
    assert candidate(s = "aabbccddeeff") == 12
    assert candidate(s = "aabbcc") == 6
    assert candidate(s = "mississippi") == 7
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 52
    assert candidate(s = "aabbccddeeffgghhiijj") == 20
    assert candidate(s = "aabbccddeeaabbccddeeff") == 12
    assert candidate(s = "aabbccdd") == 8
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 2
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmnbvcxzlkjhgfdsapoiuytrewqqwertyuiopasdfghjklzxcvbnm") == 27
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzxyz") == 49
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 26
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyxwvutsrqponmlkjihgfedcba") == 26
    assert candidate(s = "abababababababababababababababababababababababababababababababababababababababab") == 4
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 1
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == 51
    assert candidate(s = "xyzzyxzyzxzyzyzyzyz") == 3
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 4
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 26
    assert candidate(s = "aaabbbbccccddddeeeeefffffggggghhhhhiiiiijjjjjkkkkklllllmmmmmnnnnnooooo") == 18
    assert candidate(s = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaab") == 3
    assert candidate(s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52


