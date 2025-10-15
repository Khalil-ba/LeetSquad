def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(text = "ababababab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ababababab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "abababababababab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abababababababab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "ababa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ababa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzzzzzzzz") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzzzzzzzz") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeffgg") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeffgg") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccdd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccdd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacabadabacaba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacabadabacaba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "abbcccddddeeefffggghhh") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abbcccddddeeefffggghhh") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzxxzzz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzxxzzz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "ababababababababababababababababababababababababababababababababababababababababababababababababababab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ababababababababababababababababababababababababababababababababababababababababababababababababababab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefgabcdefgabcdefg") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefgabcdefgabcdefg") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 106: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdabcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdabcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "abbcccddddeee") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abbcccddddeee") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzzzzzzzzzzzzzzzzzz") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzzzzzzzzzzzzzzzzzz") == 20: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccdd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccdd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "ababcababcab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ababcababcab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeffgghhii") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeffgghhii") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaabaaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaabaaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabacaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabacaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefgabcdefg") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefgabcdefg") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcde") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcde") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccdd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccdd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnoooo") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnoooo") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "abababababababababababababab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abababababababababababababab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadaba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadaba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccccaaaabbccccaaaabbccccaaaabbccccaaaabbccccaaaabbccccaaaabbccccaaaabbccccaaaabbccccaaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccccaaaabbccccaaaabbccccaaaabbccccaaaabbccccaaaabbccccaaaabbccccaaaabbccccaaaabbccccaaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacabadabacab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacabadabacab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccccddddddaaaabbbcccc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccccddddddaaaabbbcccc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "abracadabraabracadabraabracadabra") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abracadabraabracadabraabracadabra") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddaaaaaaaaaabbbbbbbbbbccccccccccddddddddddaaaaaaaaaabbbbbbbbbb") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddaaaaaaaaaabbbbbbbbbbccccccccccddddddddddaaaaaaaaaabbbbbbbbbb") == 11: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyxwvuutsrqponmlkjihgfedcba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyxwvuutsrqponmlkjihgfedcba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "abababababababababababababababababababababababababababababababababababababababababababababab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abababababababababababababababababababababababababababababababababababababababababababababab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzyxyzyxyzyzyzyzyzyzyzyzyzyzyzyzyzyzyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzyxyzyxyzyzyzyzyzyzyzyzyzyzyzyzyzyzyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaabbbbbbccccccdddddeeeeeffffffffgggggghhhhhhiiiiiiijjjjjjkkkkkkklllllllmmmmmmmnnnnnnnooooooo") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaabbbbbbccccccdddddeeeeeffffffffgggggghhhhhhiiiiiiijjjjjjkkkkkkklllllllmmmmmmmnnnnnnnooooooo") == 8: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbaabbaaabbbaabbaabbaabb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbaabbaaabbbaabbaabbaabb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "qqqqwweerrttyyuiioopplkkjjhhggffddssaazzzxxxxccvvbbnmm") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "qqqqwweerrttyyuiioopplkkjjhhggffddssaazzzxxxxccvvbbnmm") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccdd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccdd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "ppppooooiiiiuuuueeeeooooooooaaaaaaaaaaaaaaaaaabbbbbbbbbbbb") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ppppooooiiiiuuuueeeeooooooooaaaaaaaaaaaaaaaaaabbbbbbbbbbbb") == 18: {e}')
    
    total += 1
    try:
        result = candidate(text = "abccbaabccbaabccbaabccba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abccbaabccbaabccbaabccba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabcabcabcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabcabcabcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdabcabcdabcabcdabcabcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdabcabcdabcabcdabcabcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbaaabbbaaabbaabbbaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbaaabbbaaabbaabbbaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbbccddddeeefffggg") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbbccddddeeefffggg") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbaaabbbaaaabbbbaaabbbbaaaabbbbaaabbbbaaaabbbbaaabbbbaaaabbbbaaabbbbaaaabbbbaaabbbbaaaabb") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbaaabbbaaaabbbbaaabbbbaaaabbbbaaabbbbaaaabbbbaaabbbbaaaabbbbaaabbbbaaaabbbbaaabbbbaaaabb") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzzzzzzzzzzzzzyxzzzzzzzzzzzzzyx") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzzzzzzzzzzzzzyxzzzzzzzzzzzzzyx") == 14: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdeedcbaedcbaedcba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdeedcbaedcbaedcba") == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(text = "ababababab") == 3
    assert candidate(text = "abababababababab") == 3
    assert candidate(text = "ababa") == 3
    assert candidate(text = "aaaaa") == 5
    assert candidate(text = "zzzzzzzzzz") == 10
    assert candidate(text = "aabbccddeeffgg") == 2
    assert candidate(text = "aabbccdd") == 2
    assert candidate(text = "abacabadabacaba") == 3
    assert candidate(text = "abbcccddddeeefffggghhh") == 4
    assert candidate(text = "zzzxxzzz") == 4
    assert candidate(text = "aabbaa") == 3
    assert candidate(text = "ababababababababababababababababababababababababababababababababababababababababababababababababababab") == 3
    assert candidate(text = "abcdefgabcdefgabcdefg") == 2
    assert candidate(text = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 106
    assert candidate(text = "abcdabcabc") == 2
    assert candidate(text = "abbcccddddeee") == 4
    assert candidate(text = "zzzzzzzzzzzzzzzzzzzz") == 20
    assert candidate(text = "aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccdd") == 3
    assert candidate(text = "ababcababcab") == 3
    assert candidate(text = "aabbccddeeffgghhii") == 2
    assert candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 2
    assert candidate(text = "aaabaaa") == 6
    assert candidate(text = "aabacaaa") == 5
    assert candidate(text = "abcdefgabcdefg") == 2
    assert candidate(text = "abcde") == 1
    assert candidate(text = "aaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaabbaaab") == 4
    assert candidate(text = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 2
    assert candidate(text = "aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccdd") == 3
    assert candidate(text = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnoooo") == 4
    assert candidate(text = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd") == 2
    assert candidate(text = "abababababababababababababab") == 3
    assert candidate(text = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadaba") == 3
    assert candidate(text = "aabbccccaaaabbccccaaaabbccccaaaabbccccaaaabbccccaaaabbccccaaaabbccccaaaabbccccaaaabbccccaaaa") == 5
    assert candidate(text = "abacabadabacab") == 3
    assert candidate(text = "aabbccccddddddaaaabbbcccc") == 6
    assert candidate(text = "abracadabraabracadabraabracadabra") == 3
    assert candidate(text = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 2
    assert candidate(text = "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddaaaaaaaaaabbbbbbbbbbccccccccccddddddddddaaaaaaaaaabbbbbbbbbb") == 11
    assert candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzyxwvuutsrqponmlkjihgfedcba") == 3
    assert candidate(text = "abababababababababababababababababababababababababababababababababababababababababababababab") == 3
    assert candidate(text = "xyzyxyzyxyzyzyzyzyzyzyzyzyzyzyzyzyzyzyz") == 3
    assert candidate(text = "aaaaabbbbbbccccccdddddeeeeeffffffffgggggghhhhhhiiiiiiijjjjjjkkkkkkklllllllmmmmmmmnnnnnnnooooooo") == 8
    assert candidate(text = "aabccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccbaabbccba") == 3
    assert candidate(text = "aabbaabbaaabbbaabbaabbaabb") == 4
    assert candidate(text = "qqqqwweerrttyyuiioopplkkjjhhggffddssaazzzxxxxccvvbbnmm") == 4
    assert candidate(text = "aabbaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccdd") == 3
    assert candidate(text = "ppppooooiiiiuuuueeeeooooooooaaaaaaaaaaaaaaaaaabbbbbbbbbbbb") == 18
    assert candidate(text = "abccbaabccbaabccbaabccba") == 3
    assert candidate(text = "abcabcabcabcabcabc") == 2
    assert candidate(text = "abcdabcabcdabcabcdabcabcd") == 2
    assert candidate(text = "aabbaaabbbaaabbaabbbaa") == 4
    assert candidate(text = "aabbbccddddeeefffggg") == 4
    assert candidate(text = "aabbaaabbbaaaabbbbaaabbbbaaaabbbbaaabbbbaaaabbbbaaabbbbaaaabbbbaaabbbbaaaabbbbaaabbbbaaaabb") == 5
    assert candidate(text = "xyzzzzzzzzzzzzzyxzzzzzzzzzzzzzyx") == 14
    assert candidate(text = "abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde") == 2
    assert candidate(text = "abcdeedcbaedcbaedcba") == 3


