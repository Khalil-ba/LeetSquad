def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "2[ab3[cd]]") == "abcdcdcdabcdcdcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[ab3[cd]]") == "abcdcdcdabcdcdcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[ab3[c]]") == "abcccabccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[ab3[c]]") == "abcccabccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "1[a1[b1[c]]]") == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1[a1[b1[c]]]") == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[3[a]]") == "aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[3[a]]") == "aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "a1[b]") == "ab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a1[b]") == "ab": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[a3[b]1[c]]") == "abbbcabbbcabbbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[a3[b]1[c]]") == "abbbcabbbcabbbc": {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "10[abc]") == "abcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10[abc]") == "abcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "1[2[3[4[a]]]]") == "aaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1[2[3[4[a]]]]") == "aaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[3[a]b]") == "aaabaaab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[3[a]b]") == "aaabaaab": {e}')
    
    total += 1
    try:
        result = candidate(s = "4[ab]") == "abababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "4[ab]") == "abababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "1[a2[b3[c]]]") == "abcccbccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1[a2[b3[c]]]") == "abcccbccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "10[a]") == "aaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10[a]") == "aaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2[b]c") == "abbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2[b]c") == "abbc": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[abc]3[cd]ef") == "abcabccdcdcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[abc]3[cd]ef") == "abcabccdcdcdef": {e}')
    
    total += 1
    try:
        result = candidate(s = "1[a]") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1[a]") == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[a2[c]]") == "accaccacc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[a2[c]]") == "accaccacc": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[a]2[bc]") == "aaabcbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[a]2[bc]") == "aaabcbc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc") == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc") == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[a3[b2[c]]]") == "abccbccbccabccbccbccabccbccbcc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[a3[b2[c]]]") == "abccbccbccabccbccbccabccbccbcc": {e}')
    
    total += 1
    try:
        result = candidate(s = "100[ab]") == "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100[ab]") == "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "a[b]") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a[b]") == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[b3[c]]") == "bcccbccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[b3[c]]") == "bcccbccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "1[xyz]2[uvw]") == "xyzuvwuvw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1[xyz]2[uvw]") == "xyzuvwuvw": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2[b3[c]]") == "abcccbccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2[b3[c]]") == "abcccbccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "1[a1[b]]") == "ab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1[a1[b]]") == "ab": {e}')
    
    total += 1
    try:
        result = candidate(s = "4[3[z]2[y]]") == "zzzyyzzzyyzzzyyzzzyy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "4[3[z]2[y]]") == "zzzyyzzzyyzzzyyzzzyy": {e}')
    
    total += 1
    try:
        result = candidate(s = "5[ab3[c2[d]]]") == "abcddcddcddabcddcddcddabcddcddcddabcddcddcddabcddcddcdd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5[ab3[c2[d]]]") == "abcddcddcddabcddcddcddabcddcddcddabcddcddcddabcddcddcdd": {e}')
    
    total += 1
    try:
        result = candidate(s = "5[a1[b2[c3[d4[e]]]]]") == "abcdeeeedeeeedeeeecdeeeedeeeedeeeeabcdeeeedeeeedeeeecdeeeedeeeedeeeeabcdeeeedeeeedeeeecdeeeedeeeedeeeeabcdeeeedeeeedeeeecdeeeedeeeedeeeeabcdeeeedeeeedeeeecdeeeedeeeedeeee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5[a1[b2[c3[d4[e]]]]]") == "abcdeeeedeeeedeeeecdeeeedeeeedeeeeabcdeeeedeeeedeeeecdeeeedeeeedeeeeabcdeeeedeeeedeeeecdeeeedeeeedeeeeabcdeeeedeeeedeeeecdeeeedeeeedeeeeabcdeeeedeeeedeeeecdeeeedeeeedeeee": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2[b3[c4[d5[e6[f7[g]]]]]]") == "abcdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggcdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggcdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggbcdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggcdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggcdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfggggggg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2[b3[c4[d5[e6[f7[g]]]]]]") == "abcdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggcdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggcdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggbcdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggcdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggcdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfggggggg": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc3[d2[e1[f]]]") == "abcdefefdefefdefef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc3[d2[e1[f]]]") == "abcdefefdefefdefef": {e}')
    
    total += 1
    try:
        result = candidate(s = "5[a2[b3[c4[d]]]]") == "abcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcdddd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5[a2[b3[c4[d]]]]") == "abcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcdddd": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[2[mn]1[op]2[qr]]") == "mnmnopqrqrmnmnopqrqrmnmnopqrqr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[2[mn]1[op]2[qr]]") == "mnmnopqrqrmnmnopqrqrmnmnopqrqr": {e}')
    
    total += 1
    try:
        result = candidate(s = "5[c2[d]]") == "cddcddcddcddcdd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5[c2[d]]") == "cddcddcddcddcdd": {e}')
    
    total += 1
    try:
        result = candidate(s = "a1[b2[c3[d]]]") == "abcdddcddd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a1[b2[c3[d]]]") == "abcdddcddd": {e}')
    
    total += 1
    try:
        result = candidate(s = "7[2[x]3[y]]") == "xxyyyxxyyyxxyyyxxyyyxxyyyxxyyyxxyyy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "7[2[x]3[y]]") == "xxyyyxxyyyxxyyyxxyyyxxyyyxxyyyxxyyy": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[ab3[cd]]4[ef5[gh]]") == "abcdcdcdabcdcdcdefghghghghghefghghghghghefghghghghghefghghghghgh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[ab3[cd]]4[ef5[gh]]") == "abcdcdcdabcdcdcdefghghghghghefghghghghghefghghghghghefghghghghgh": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[ab2[c]]4[de]") == "abccabccabccdededede"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[ab2[c]]4[de]") == "abccabccabccdededede": {e}')
    
    total += 1
    try:
        result = candidate(s = "4[ab3[c2[d]]]") == "abcddcddcddabcddcddcddabcddcddcddabcddcddcdd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "4[ab3[c2[d]]]") == "abcddcddcddabcddcddcddabcddcddcddabcddcddcdd": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[a2[b1[c0[d]]]]") == "abcbcabcbcabcbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[a2[b1[c0[d]]]]") == "abcbcabcbcabcbc": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[a4[b5[c6[d7[e8[f]]]]]]") == "abcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffabcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffabcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[a4[b5[c6[d7[e8[f]]]]]]") == "abcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffabcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffabcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffff": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[2[a]1[b]]2[3[c]4[d]]") == "aabaabaabcccddddcccdddd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[2[a]1[b]]2[3[c]4[d]]") == "aabaabaabcccddddcccdddd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc2[def3[ghi]]jkl4[mno5[pqr]]stu") == "abcdefghighighidefghighighijklmnopqrpqrpqrpqrpqrmnopqrpqrpqrpqrpqrmnopqrpqrpqrpqrpqrmnopqrpqrpqrpqrpqrstu"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc2[def3[ghi]]jkl4[mno5[pqr]]stu") == "abcdefghighighidefghighighijklmnopqrpqrpqrpqrpqrmnopqrpqrpqrpqrpqrmnopqrpqrpqrpqrpqrmnopqrpqrpqrpqrpqrstu": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[3[a]2[b3[c]2[d]]]") == "aaabcccddbcccddaaabcccddbcccdd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[3[a]2[b3[c]2[d]]]") == "aaabcccddbcccddaaabcccddbcccdd": {e}')
    
    total += 1
    try:
        result = candidate(s = "6[ab2[cd3[ef]]]") == "abcdefefefcdefefefabcdefefefcdefefefabcdefefefcdefefefabcdefefefcdefefefabcdefefefcdefefefabcdefefefcdefefef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "6[ab2[cd3[ef]]]") == "abcdefefefcdefefefabcdefefefcdefefefabcdefefefcdefefefabcdefefefcdefefefabcdefefefcdefefefabcdefefefcdefefef": {e}')
    
    total += 1
    try:
        result = candidate(s = "7[fg]2[h3[i]]") == "fgfgfgfgfgfgfghiiihiii"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "7[fg]2[h3[i]]") == "fgfgfgfgfgfgfghiiihiii": {e}')
    
    total += 1
    try:
        result = candidate(s = "7[x2[y3[z4[w]]]]") == "xyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwwwxyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwwwxyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwwwxyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwwwxyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwwwxyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwwwxyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwww"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "7[x2[y3[z4[w]]]]") == "xyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwwwxyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwwwxyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwwwxyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwwwxyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwwwxyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwwwxyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwww": {e}')
    
    total += 1
    try:
        result = candidate(s = "5[2[x3[y]]4[z]]") == "xyyyxyyyzzzzxyyyxyyyzzzzxyyyxyyyzzzzxyyyxyyyzzzzxyyyxyyyzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5[2[x3[y]]4[z]]") == "xyyyxyyyzzzzxyyyxyyyzzzzxyyyxyyyzzzzxyyyxyyyzzzzxyyyxyyyzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "6[ab2[cd3[ef4[gh]]]]") == "abcdefghghghghefghghghghefghghghghcdefghghghghefghghghghefghghghghabcdefghghghghefghghghghefghghghghcdefghghghghefghghghghefghghghghabcdefghghghghefghghghghefghghghghcdefghghghghefghghghghefghghghghabcdefghghghghefghghghghefghghghghcdefghghghghefghghghghefghghghghabcdefghghghghefghghghghefghghghghcdefghghghghefghghghghefghghghghabcdefghghghghefghghghghefghghghghcdefghghghghefghghghghefghghghgh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "6[ab2[cd3[ef4[gh]]]]") == "abcdefghghghghefghghghghefghghghghcdefghghghghefghghghghefghghghghabcdefghghghghefghghghghefghghghghcdefghghghghefghghghghefghghghghabcdefghghghghefghghghghefghghghghcdefghghghghefghghghghefghghghghabcdefghghghghefghghghghefghghghghcdefghghghghefghghghghefghghghghabcdefghghghghefghghghghefghghghghcdefghghghghefghghghghefghghghghabcdefghghghghefghghghghefghghghghcdefghghghghefghghghghefghghghgh": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[x2[y3[z]]]1[a]") == "xyzzzyzzzxyzzzyzzza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[x2[y3[z]]]1[a]") == "xyzzzyzzzxyzzzyzzza": {e}')
    
    total += 1
    try:
        result = candidate(s = "7[z]6[y5[x4[w3[v2[u1[t]]]]]]") == "zzzzzzzyxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututyxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututyxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututyxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututyxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututyxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvutut"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "7[z]6[y5[x4[w3[v2[u1[t]]]]]]") == "zzzzzzzyxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututyxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututyxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututyxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututyxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututyxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvutut": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[a3[b4[c]]]") == "abccccbccccbccccabccccbccccbcccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[a3[b4[c]]]") == "abccccbccccbccccabccccbccccbcccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "10[a9[bc3[de]]]") == "abcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdedede"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10[a9[bc3[de]]]") == "abcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdedede": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[ab]4[cd]5[ef]") == "abababcdcdcdcdefefefefef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[ab]4[cd]5[ef]") == "abababcdcdcdcdefefefefef": {e}')
    
    total += 1
    try:
        result = candidate(s = "10[ab]") == "abababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10[ab]") == "abababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "5[4[3[2[1[x]]]]]") == "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5[4[3[2[1[x]]]]]") == "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[ab3[cd4[ef]]]") == "abcdefefefefcdefefefefcdefefefefabcdefefefefcdefefefefcdefefefef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[ab3[cd4[ef]]]") == "abcdefefefefcdefefefefcdefefefefabcdefefefefcdefefefefcdefefefef": {e}')
    
    total += 1
    try:
        result = candidate(s = "5[ab]3[cd]2[ef1[gh]]") == "abababababcdcdcdefghefgh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5[ab]3[cd]2[ef1[gh]]") == "abababababcdcdcdefghefgh": {e}')
    
    total += 1
    try:
        result = candidate(s = "7[2[pq]3[rs]]") == "pqpqrsrsrspqpqrsrsrspqpqrsrsrspqpqrsrsrspqpqrsrsrspqpqrsrsrspqpqrsrsrs"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "7[2[pq]3[rs]]") == "pqpqrsrsrspqpqrsrsrspqpqrsrsrspqpqrsrsrspqpqrsrsrspqpqrsrsrspqpqrsrsrs": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[3[a]b]4[c5[d]]") == "aaabaaabcdddddcdddddcdddddcddddd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[3[a]b]4[c5[d]]") == "aaabaaabcdddddcdddddcdddddcddddd": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[2[3[4[a]]]]") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[2[3[4[a]]]]") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "6[2[a]3[b]]") == "aabbbaabbbaabbbaabbbaabbbaabbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "6[2[a]3[b]]") == "aabbbaabbbaabbbaabbbaabbbaabbb": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[abc3[def4[ghi5[jkl]]]]") == "abcdefghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljkldefghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljkldefghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklabcdefghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljkldefghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljkldefghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljkl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[abc3[def4[ghi5[jkl]]]]") == "abcdefghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljkldefghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljkldefghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklabcdefghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljkldefghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljkldefghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljkl": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[a3[b4[c5[d6[e]]]]]") == "abcdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeebcdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeebcdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeeabcdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeebcdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeebcdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[a3[b4[c5[d6[e]]]]]") == "abcdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeebcdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeebcdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeeabcdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeebcdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeebcdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeee": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[2[1[0[]]]]") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[2[1[0[]]]]") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "10[f9[g]]") == "fgggggggggfgggggggggfgggggggggfgggggggggfgggggggggfgggggggggfgggggggggfgggggggggfgggggggggfggggggggg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10[f9[g]]") == "fgggggggggfgggggggggfgggggggggfgggggggggfgggggggggfgggggggggfgggggggggfgggggggggfgggggggggfggggggggg": {e}')
    
    total += 1
    try:
        result = candidate(s = "15[abc10[de]]") == "abcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdededededededededede"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "15[abc10[de]]") == "abcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdededededededededede": {e}')
    
    total += 1
    try:
        result = candidate(s = "5[k9[l10[m]]]") == "klmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmklmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmklmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmklmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmklmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5[k9[l10[m]]]") == "klmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmklmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmklmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmklmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmklmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmm": {e}')
    
    total += 1
    try:
        result = candidate(s = "5[xy2[z3[w4[v]]]]") == "xyzwvvvvwvvvvwvvvvzwvvvvwvvvvwvvvvxyzwvvvvwvvvvwvvvvzwvvvvwvvvvwvvvvxyzwvvvvwvvvvwvvvvzwvvvvwvvvvwvvvvxyzwvvvvwvvvvwvvvvzwvvvvwvvvvwvvvvxyzwvvvvwvvvvwvvvvzwvvvvwvvvvwvvvv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5[xy2[z3[w4[v]]]]") == "xyzwvvvvwvvvvwvvvvzwvvvvwvvvvwvvvvxyzwvvvvwvvvvwvvvvzwvvvvwvvvvwvvvvxyzwvvvvwvvvvwvvvvzwvvvvwvvvvwvvvvxyzwvvvvwvvvvwvvvvzwvvvvwvvvvwvvvvxyzwvvvvwvvvvwvvvvzwvvvvwvvvvwvvvv": {e}')
    
    total += 1
    try:
        result = candidate(s = "1[1[1[1[ab]]]]") == "ab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1[1[1[1[ab]]]]") == "ab": {e}')
    
    total += 1
    try:
        result = candidate(s = "5[1[2[3[4[5[a]]]]]]") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5[1[2[3[4[5[a]]]]]]") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "4[ab2[c]]") == "abccabccabccabcc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "4[ab2[c]]") == "abccabccabccabcc": {e}')
    
    total += 1
    try:
        result = candidate(s = "4[a2[b3[c]]]") == "abcccbcccabcccbcccabcccbcccabcccbccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "4[a2[b3[c]]]") == "abcccbcccabcccbcccabcccbcccabcccbccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[x3[y4[z]]]") == "xyzzzzyzzzzyzzzzxyzzzzyzzzzyzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[x3[y4[z]]]") == "xyzzzzyzzzzyzzzzxyzzzzyzzzzyzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[2[3[4[a]]]5[b]]") == "aaaaaaaaaaaaaaaaaaaaaaaabbbbbaaaaaaaaaaaaaaaaaaaaaaaabbbbbaaaaaaaaaaaaaaaaaaaaaaaabbbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[2[3[4[a]]]5[b]]") == "aaaaaaaaaaaaaaaaaaaaaaaabbbbbaaaaaaaaaaaaaaaaaaaaaaaabbbbbaaaaaaaaaaaaaaaaaaaaaaaabbbbb": {e}')
    
    total += 1
    try:
        result = candidate(s = "10[ab2[cd]ef3[gh]]") == "abcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghgh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10[ab2[cd]ef3[gh]]") == "abcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghgh": {e}')
    
    total += 1
    try:
        result = candidate(s = "5[abc2[def]]") == "abcdefdefabcdefdefabcdefdefabcdefdefabcdefdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5[abc2[def]]") == "abcdefdefabcdefdefabcdefdefabcdefdefabcdefdef": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[2[3[a2[b]]]]") == "abbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[2[3[a2[b]]]]") == "abbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabb": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[3[ab]]") == "abababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[3[ab]]") == "abababababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[xy2[z]]2[ab]") == "xyzzxyzzxyzzabab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[xy2[z]]2[ab]") == "xyzzxyzzxyzzabab": {e}')
    
    total += 1
    try:
        result = candidate(s = "10[1[a]2[b]3[c]4[d]5[e]]") == "abbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10[1[a]2[b]3[c]4[d]5[e]]") == "abbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeee": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[2[3[4[x]]]]") == "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[2[3[4[x]]]]") == "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[3[a]b4[c]]") == "aaabccccaaabcccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[3[a]b4[c]]") == "aaabccccaaabcccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "10[x]") == "xxxxxxxxxx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10[x]") == "xxxxxxxxxx": {e}')
    
    total += 1
    try:
        result = candidate(s = "4[2[xy]z]") == "xyxyzxyxyzxyxyzxyxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "4[2[xy]z]") == "xyxyzxyxyzxyxyzxyxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "6[a5[b4[c3[d2[e1[f]]]]]]") == "abcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefabcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefabcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefabcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefabcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefabcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "6[a5[b4[c3[d2[e1[f]]]]]]") == "abcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefabcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefabcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefabcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefabcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefabcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefef": {e}')
    
    total += 1
    try:
        result = candidate(s = "4[x5[yz]w]") == "xyzyzyzyzyzwxyzyzyzyzyzwxyzyzyzyzyzwxyzyzyzyzyzw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "4[x5[yz]w]") == "xyzyzyzyzyzwxyzyzyzyzyzwxyzyzyzyzyzwxyzyzyzyzyzw": {e}')
    
    total += 1
    try:
        result = candidate(s = "4[3[2[b1[c]]]]") == "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "4[3[2[b1[c]]]]") == "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[x3[xy4[z]]]") == "xxyzzzzxyzzzzxyzzzzxxyzzzzxyzzzzxyzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[x3[xy4[z]]]") == "xxyzzzzxyzzzzxyzzzzxxyzzzzxyzzzzxyzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[3[a2[b]]c]") == "abbabbabbcabbabbabbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[3[a2[b]]c]") == "abbabbabbcabbabbabbc": {e}')
    
    total += 1
    try:
        result = candidate(s = "9[abc]8[def]7[ghi]") == "abcabcabcabcabcabcabcabcabcdefdefdefdefdefdefdefdefghighighighighighighi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "9[abc]8[def]7[ghi]") == "abcabcabcabcabcabcabcabcabcdefdefdefdefdefdefdefdefghighighighighighighi": {e}')
    
    total += 1
    try:
        result = candidate(s = "4[ab]5[cd]") == "ababababcdcdcdcdcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "4[ab]5[cd]") == "ababababcdcdcdcdcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[3[xy]z]") == "xyxyxyzxyxyxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[3[xy]z]") == "xyxyxyzxyxyxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "4[x3[y2[z]]]") == "xyzzyzzyzzxyzzyzzyzzxyzzyzzyzzxyzzyzzyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "4[x3[y2[z]]]") == "xyzzyzzyzzxyzzyzzyzzxyzzyzzyzzxyzzyzzyzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[2[a]b]") == "aabaabaab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[2[a]b]") == "aabaabaab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc2[3[de]fg]") == "abcdededefgdededefg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc2[3[de]fg]") == "abcdededefgdededefg": {e}')
    
    total += 1
    try:
        result = candidate(s = "1[abc2[def3[ghi]]]") == "abcdefghighighidefghighighi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1[abc2[def3[ghi]]]") == "abcdefghighighidefghighighi": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[abc2[def3[ghi]]]") == "abcdefghighighidefghighighiabcdefghighighidefghighighi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[abc2[def3[ghi]]]") == "abcdefghighighidefghighighiabcdefghighighidefghighighi": {e}')
    
    total += 1
    try:
        result = candidate(s = "1[2[3[4[5[a]]]]]") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1[2[3[4[5[a]]]]]") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "5[ab3[cd]]") == "abcdcdcdabcdcdcdabcdcdcdabcdcdcdabcdcdcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5[ab3[cd]]") == "abcdcdcdabcdcdcdabcdcdcdabcdcdcdabcdcdcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[x3[y4[z]]]1[w]") == "xyzzzzyzzzzyzzzzxyzzzzyzzzzyzzzzw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[x3[y4[z]]]1[w]") == "xyzzzzyzzzzyzzzzxyzzzzyzzzzyzzzzw": {e}')
    
    total += 1
    try:
        result = candidate(s = "7[2[a]3[b]]") == "aabbbaabbbaabbbaabbbaabbbaabbbaabbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "7[2[a]3[b]]") == "aabbbaabbbaabbbaabbbaabbbaabbbaabbb": {e}')
    
    total += 1
    try:
        result = candidate(s = "9[8[7[6[5[4[3[2[1[0[a]]]]]]]]]]") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "9[8[7[6[5[4[3[2[1[0[a]]]]]]]]]]") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "4[x5[y]]") == "xyyyyyxyyyyyxyyyyyxyyyyy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "4[x5[y]]") == "xyyyyyxyyyyyxyyyyyxyyyyy": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[abc3[def4[ghi]]]") == "abcdefghighighighidefghighighighidefghighighighiabcdefghighighighidefghighighighidefghighighighi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[abc3[def4[ghi]]]") == "abcdefghighighighidefghighighighidefghighighighiabcdefghighighighidefghighighighidefghighighighi": {e}')
    
    total += 1
    try:
        result = candidate(s = "5[ab2[c]]3[xy]2[de]") == "abccabccabccabccabccxyxyxydede"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5[ab2[c]]3[xy]2[de]") == "abccabccabccabccabccxyxyxydede": {e}')
    
    total += 1
    try:
        result = candidate(s = "5[abc2[de]]") == "abcdedeabcdedeabcdedeabcdedeabcdede"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5[abc2[de]]") == "abcdedeabcdedeabcdedeabcdedeabcdede": {e}')
    
    total += 1
    try:
        result = candidate(s = "7[k2[3[xyz]]]") == "kxyzxyzxyzxyzxyzxyzkxyzxyzxyzxyzxyzxyzkxyzxyzxyzxyzxyzxyzkxyzxyzxyzxyzxyzxyzkxyzxyzxyzxyzxyzxyzkxyzxyzxyzxyzxyzxyzkxyzxyzxyzxyzxyzxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "7[k2[3[xyz]]]") == "kxyzxyzxyzxyzxyzxyzkxyzxyzxyzxyzxyzxyzkxyzxyzxyzxyzxyzxyzkxyzxyzxyzxyzxyzxyzkxyzxyzxyzxyzxyzxyzkxyzxyzxyzxyzxyzxyzkxyzxyzxyzxyzxyzxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "1[abc2[def]]") == "abcdefdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1[abc2[def]]") == "abcdefdef": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[3[4[5[6[7[8[9[0[1[a]]]]]]]]]]") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[3[4[5[6[7[8[9[0[1[a]]]]]]]]]]") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[2[1[x]]]") == "xxxxxx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[2[1[x]]]") == "xxxxxx": {e}')
    
    total += 1
    try:
        result = candidate(s = "5[ab2[cd]]") == "abcdcdabcdcdabcdcdabcdcdabcdcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5[ab2[cd]]") == "abcdcdabcdcdabcdcdabcdcdabcdcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "6[5[4[3[2[1[a]]]]]]") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "6[5[4[3[2[1[a]]]]]]") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "7[xyz]3[abc2[def1[ghi]]]") == "xyzxyzxyzxyzxyzxyzxyzabcdefghidefghiabcdefghidefghiabcdefghidefghi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "7[xyz]3[abc2[def1[ghi]]]") == "xyzxyzxyzxyzxyzxyzxyzabcdefghidefghiabcdefghidefghiabcdefghidefghi": {e}')
    
    total += 1
    try:
        result = candidate(s = "x1[y2[z3[a4[b5[c]]]]]") == "xyzabcccccbcccccbcccccbcccccabcccccbcccccbcccccbcccccabcccccbcccccbcccccbccccczabcccccbcccccbcccccbcccccabcccccbcccccbcccccbcccccabcccccbcccccbcccccbccccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "x1[y2[z3[a4[b5[c]]]]]") == "xyzabcccccbcccccbcccccbcccccabcccccbcccccbcccccbcccccabcccccbcccccbcccccbccccczabcccccbcccccbcccccbcccccabcccccbcccccbcccccbcccccabcccccbcccccbcccccbccccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[ab2[c3[d]]]") == "abcdddcdddabcdddcdddabcdddcddd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[ab2[c3[d]]]") == "abcdddcdddabcdddcdddabcdddcddd": {e}')
    
    total += 1
    try:
        result = candidate(s = "6[a2[b3[c4[d]]]]") == "abcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcdddd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "6[a2[b3[c4[d]]]]") == "abcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcdddd": {e}')
    
    total += 1
    try:
        result = candidate(s = "15[a]") == "aaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "15[a]") == "aaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "5[2[3[a]]]") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5[2[3[a]]]") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[xy3[z]]4[ab]") == "xyzzzxyzzzabababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[xy3[z]]4[ab]") == "xyzzzxyzzzabababab": {e}')
    
    total += 1
    try:
        result = candidate(s = "1[a2[b3[c4[d5[e]]]]]") == "abcdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeeebcdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1[a2[b3[c4[d5[e]]]]]") == "abcdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeeebcdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeee": {e}')
    
    total += 1
    try:
        result = candidate(s = "4[a3[b]]") == "abbbabbbabbbabbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "4[a3[b]]") == "abbbabbbabbbabbb": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[ab]3[cd]4[ef]") == "ababcdcdcdefefefef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[ab]3[cd]4[ef]") == "ababcdcdcdefefefef": {e}')
    
    total += 1
    try:
        result = candidate(s = "1[2[3[4[5[6[7[8[9[0[x]]]]]]]]]]") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1[2[3[4[5[6[7[8[9[0[x]]]]]]]]]]") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "1[2[3[4[5[6[x]]]]]]") == "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1[2[3[4[5[6[x]]]]]]") == "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[a3[b4[c5[d6[e7[f]]]]]]") == "abcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffbcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffbcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffabcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffbcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffbcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[a3[b4[c5[d6[e7[f]]]]]]") == "abcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffbcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffbcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffabcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffbcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffbcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffff": {e}')
    
    total += 1
    try:
        result = candidate(s = "4[a3[b2[c1[d]]]]") == "abcdcdbcdcdbcdcdabcdcdbcdcdbcdcdabcdcdbcdcdbcdcdabcdcdbcdcdbcdcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "4[a3[b2[c1[d]]]]") == "abcdcdbcdcdbcdcdabcdcdbcdcdbcdcdabcdcdbcdcdbcdcdabcdcdbcdcdbcdcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[2[3[4[5[a]]]]]") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[2[3[4[5[a]]]]]") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "1[xyz]2[uvw]3[2[abc]3[def]]4[ghi]") == "xyzuvwuvwabcabcdefdefdefabcabcdefdefdefabcabcdefdefdefghighighighi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1[xyz]2[uvw]3[2[abc]3[def]]4[ghi]") == "xyzuvwuvwabcabcdefdefdefabcabcdefdefdefabcabcdefdefdefghighighighi": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[xyz2[abc]4[def]]5[ghi]") == "xyzabcabcdefdefdefdefxyzabcabcdefdefdefdefxyzabcabcdefdefdefdefghighighighighi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[xyz2[abc]4[def]]5[ghi]") == "xyzabcabcdefdefdefdefxyzabcabcdefdefdefdefxyzabcabcdefdefdefdefghighighighighi": {e}')
    
    total += 1
    try:
        result = candidate(s = "2[2[2[2[2[abc]]]]]") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2[2[2[2[2[abc]]]]]") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "3[b2[c]1[d]]4[e]") == "bccdbccdbccdeeee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3[b2[c]1[d]]4[e]") == "bccdbccdbccdeeee": {e}')
    
    total += 1
    try:
        result = candidate(s = "a2[b3[c4[d5[e]]]]") == "abcdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeeebcdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a2[b3[c4[d5[e]]]]") == "abcdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeeebcdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeee": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "2[ab3[cd]]") == "abcdcdcdabcdcdcd"
    assert candidate(s = "2[ab3[c]]") == "abcccabccc"
    assert candidate(s = "1[a1[b1[c]]]") == "abc"
    assert candidate(s = "2[3[a]]") == "aaaaaa"
    assert candidate(s = "a1[b]") == "ab"
    assert candidate(s = "3[a3[b]1[c]]") == "abbbcabbbcabbbc"
    assert candidate(s = "a") == "a"
    assert candidate(s = "10[abc]") == "abcabcabcabcabcabcabcabcabcabc"
    assert candidate(s = "1[2[3[4[a]]]]") == "aaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "2[3[a]b]") == "aaabaaab"
    assert candidate(s = "4[ab]") == "abababab"
    assert candidate(s = "1[a2[b3[c]]]") == "abcccbccc"
    assert candidate(s = "10[a]") == "aaaaaaaaaa"
    assert candidate(s = "a2[b]c") == "abbc"
    assert candidate(s = "2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert candidate(s = "1[a]") == "a"
    assert candidate(s = "3[a2[c]]") == "accaccacc"
    assert candidate(s = "3[a]2[bc]") == "aaabcbc"
    assert candidate(s = "abc") == "abc"
    assert candidate(s = "3[a3[b2[c]]]") == "abccbccbccabccbccbccabccbccbcc"
    assert candidate(s = "100[ab]") == "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab"
    assert candidate(s = "a[b]") == "a"
    assert candidate(s = "2[b3[c]]") == "bcccbccc"
    assert candidate(s = "1[xyz]2[uvw]") == "xyzuvwuvw"
    assert candidate(s = "a2[b3[c]]") == "abcccbccc"
    assert candidate(s = "1[a1[b]]") == "ab"
    assert candidate(s = "4[3[z]2[y]]") == "zzzyyzzzyyzzzyyzzzyy"
    assert candidate(s = "5[ab3[c2[d]]]") == "abcddcddcddabcddcddcddabcddcddcddabcddcddcddabcddcddcdd"
    assert candidate(s = "5[a1[b2[c3[d4[e]]]]]") == "abcdeeeedeeeedeeeecdeeeedeeeedeeeeabcdeeeedeeeedeeeecdeeeedeeeedeeeeabcdeeeedeeeedeeeecdeeeedeeeedeeeeabcdeeeedeeeedeeeecdeeeedeeeedeeeeabcdeeeedeeeedeeeecdeeeedeeeedeeee"
    assert candidate(s = "a2[b3[c4[d5[e6[f7[g]]]]]]") == "abcdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggcdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggcdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggbcdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggcdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggcdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggdefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfgggggggefgggggggfgggggggfgggggggfgggggggfgggggggfggggggg"
    assert candidate(s = "abc3[d2[e1[f]]]") == "abcdefefdefefdefef"
    assert candidate(s = "5[a2[b3[c4[d]]]]") == "abcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcdddd"
    assert candidate(s = "3[2[mn]1[op]2[qr]]") == "mnmnopqrqrmnmnopqrqrmnmnopqrqr"
    assert candidate(s = "5[c2[d]]") == "cddcddcddcddcdd"
    assert candidate(s = "a1[b2[c3[d]]]") == "abcdddcddd"
    assert candidate(s = "7[2[x]3[y]]") == "xxyyyxxyyyxxyyyxxyyyxxyyyxxyyyxxyyy"
    assert candidate(s = "2[ab3[cd]]4[ef5[gh]]") == "abcdcdcdabcdcdcdefghghghghghefghghghghghefghghghghghefghghghghgh"
    assert candidate(s = "3[ab2[c]]4[de]") == "abccabccabccdededede"
    assert candidate(s = "4[ab3[c2[d]]]") == "abcddcddcddabcddcddcddabcddcddcddabcddcddcdd"
    assert candidate(s = "3[a2[b1[c0[d]]]]") == "abcbcabcbcabcbc"
    assert candidate(s = "3[a4[b5[c6[d7[e8[f]]]]]]") == "abcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffabcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffabcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffbcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffcdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffdeffffffffeffffffffeffffffffeffffffffeffffffffeffffffffeffffffff"
    assert candidate(s = "3[2[a]1[b]]2[3[c]4[d]]") == "aabaabaabcccddddcccdddd"
    assert candidate(s = "abc2[def3[ghi]]jkl4[mno5[pqr]]stu") == "abcdefghighighidefghighighijklmnopqrpqrpqrpqrpqrmnopqrpqrpqrpqrpqrmnopqrpqrpqrpqrpqrmnopqrpqrpqrpqrpqrstu"
    assert candidate(s = "2[3[a]2[b3[c]2[d]]]") == "aaabcccddbcccddaaabcccddbcccdd"
    assert candidate(s = "6[ab2[cd3[ef]]]") == "abcdefefefcdefefefabcdefefefcdefefefabcdefefefcdefefefabcdefefefcdefefefabcdefefefcdefefefabcdefefefcdefefef"
    assert candidate(s = "7[fg]2[h3[i]]") == "fgfgfgfgfgfgfghiiihiii"
    assert candidate(s = "7[x2[y3[z4[w]]]]") == "xyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwwwxyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwwwxyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwwwxyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwwwxyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwwwxyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwwwxyzwwwwzwwwwzwwwwyzwwwwzwwwwzwwww"
    assert candidate(s = "5[2[x3[y]]4[z]]") == "xyyyxyyyzzzzxyyyxyyyzzzzxyyyxyyyzzzzxyyyxyyyzzzzxyyyxyyyzzzz"
    assert candidate(s = "6[ab2[cd3[ef4[gh]]]]") == "abcdefghghghghefghghghghefghghghghcdefghghghghefghghghghefghghghghabcdefghghghghefghghghghefghghghghcdefghghghghefghghghghefghghghghabcdefghghghghefghghghghefghghghghcdefghghghghefghghghghefghghghghabcdefghghghghefghghghghefghghghghcdefghghghghefghghghghefghghghghabcdefghghghghefghghghghefghghghghcdefghghghghefghghghghefghghghghabcdefghghghghefghghghghefghghghghcdefghghghghefghghghghefghghghgh"
    assert candidate(s = "2[x2[y3[z]]]1[a]") == "xyzzzyzzzxyzzzyzzza"
    assert candidate(s = "7[z]6[y5[x4[w3[v2[u1[t]]]]]]") == "zzzzzzzyxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututyxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututyxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututyxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututyxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututyxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvututxwvututvututvututwvututvututvututwvututvututvututwvututvututvutut"
    assert candidate(s = "2[a3[b4[c]]]") == "abccccbccccbccccabccccbccccbcccc"
    assert candidate(s = "10[a9[bc3[de]]]") == "abcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededeabcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdededebcdedede"
    assert candidate(s = "3[ab]4[cd]5[ef]") == "abababcdcdcdcdefefefefef"
    assert candidate(s = "10[ab]") == "abababababababababab"
    assert candidate(s = "5[4[3[2[1[x]]]]]") == "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    assert candidate(s = "2[ab3[cd4[ef]]]") == "abcdefefefefcdefefefefcdefefefefabcdefefefefcdefefefefcdefefefef"
    assert candidate(s = "5[ab]3[cd]2[ef1[gh]]") == "abababababcdcdcdefghefgh"
    assert candidate(s = "7[2[pq]3[rs]]") == "pqpqrsrsrspqpqrsrsrspqpqrsrsrspqpqrsrsrspqpqrsrsrspqpqrsrsrspqpqrsrsrs"
    assert candidate(s = "2[3[a]b]4[c5[d]]") == "aaabaaabcdddddcdddddcdddddcddddd"
    assert candidate(s = "3[2[3[4[a]]]]") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "6[2[a]3[b]]") == "aabbbaabbbaabbbaabbbaabbbaabbb"
    assert candidate(s = "2[abc3[def4[ghi5[jkl]]]]") == "abcdefghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljkldefghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljkldefghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklabcdefghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljkldefghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljkldefghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljklghijkljkljkljkljkl"
    assert candidate(s = "2[a3[b4[c5[d6[e]]]]]") == "abcdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeebcdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeebcdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeeabcdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeebcdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeebcdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeeecdeeeeeedeeeeeedeeeeeedeeeeeedeeeeee"
    assert candidate(s = "3[2[1[0[]]]]") == ""
    assert candidate(s = "10[f9[g]]") == "fgggggggggfgggggggggfgggggggggfgggggggggfgggggggggfgggggggggfgggggggggfgggggggggfgggggggggfggggggggg"
    assert candidate(s = "15[abc10[de]]") == "abcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdedededededededededeabcdededededededededede"
    assert candidate(s = "5[k9[l10[m]]]") == "klmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmklmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmklmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmklmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmklmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmmlmmmmmmmmmm"
    assert candidate(s = "5[xy2[z3[w4[v]]]]") == "xyzwvvvvwvvvvwvvvvzwvvvvwvvvvwvvvvxyzwvvvvwvvvvwvvvvzwvvvvwvvvvwvvvvxyzwvvvvwvvvvwvvvvzwvvvvwvvvvwvvvvxyzwvvvvwvvvvwvvvvzwvvvvwvvvvwvvvvxyzwvvvvwvvvvwvvvvzwvvvvwvvvvwvvvv"
    assert candidate(s = "1[1[1[1[ab]]]]") == "ab"
    assert candidate(s = "5[1[2[3[4[5[a]]]]]]") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "4[ab2[c]]") == "abccabccabccabcc"
    assert candidate(s = "4[a2[b3[c]]]") == "abcccbcccabcccbcccabcccbcccabcccbccc"
    assert candidate(s = "2[x3[y4[z]]]") == "xyzzzzyzzzzyzzzzxyzzzzyzzzzyzzzz"
    assert candidate(s = "3[2[3[4[a]]]5[b]]") == "aaaaaaaaaaaaaaaaaaaaaaaabbbbbaaaaaaaaaaaaaaaaaaaaaaaabbbbbaaaaaaaaaaaaaaaaaaaaaaaabbbbb"
    assert candidate(s = "10[ab2[cd]ef3[gh]]") == "abcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghghabcdcdefghghgh"
    assert candidate(s = "5[abc2[def]]") == "abcdefdefabcdefdefabcdefdefabcdefdefabcdefdef"
    assert candidate(s = "3[2[3[a2[b]]]]") == "abbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabb"
    assert candidate(s = "2[3[ab]]") == "abababababab"
    assert candidate(s = "3[xy2[z]]2[ab]") == "xyzzxyzzxyzzabab"
    assert candidate(s = "10[1[a]2[b]3[c]4[d]5[e]]") == "abbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeeeabbcccddddeeeee"
    assert candidate(s = "3[2[3[4[x]]]]") == "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    assert candidate(s = "2[3[a]b4[c]]") == "aaabccccaaabcccc"
    assert candidate(s = "10[x]") == "xxxxxxxxxx"
    assert candidate(s = "4[2[xy]z]") == "xyxyzxyxyzxyxyzxyxyz"
    assert candidate(s = "6[a5[b4[c3[d2[e1[f]]]]]]") == "abcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefabcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefabcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefabcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefabcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefabcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefbcdefefdefefdefefcdefefdefefdefefcdefefdefefdefefcdefefdefefdefef"
    assert candidate(s = "4[x5[yz]w]") == "xyzyzyzyzyzwxyzyzyzyzyzwxyzyzyzyzyzwxyzyzyzyzyzw"
    assert candidate(s = "4[3[2[b1[c]]]]") == "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc"
    assert candidate(s = "2[x3[xy4[z]]]") == "xxyzzzzxyzzzzxyzzzzxxyzzzzxyzzzzxyzzzz"
    assert candidate(s = "2[3[a2[b]]c]") == "abbabbabbcabbabbabbc"
    assert candidate(s = "9[abc]8[def]7[ghi]") == "abcabcabcabcabcabcabcabcabcdefdefdefdefdefdefdefdefghighighighighighighi"
    assert candidate(s = "4[ab]5[cd]") == "ababababcdcdcdcdcd"
    assert candidate(s = "2[3[xy]z]") == "xyxyxyzxyxyxyz"
    assert candidate(s = "4[x3[y2[z]]]") == "xyzzyzzyzzxyzzyzzyzzxyzzyzzyzzxyzzyzzyzz"
    assert candidate(s = "3[2[a]b]") == "aabaabaab"
    assert candidate(s = "abc2[3[de]fg]") == "abcdededefgdededefg"
    assert candidate(s = "1[abc2[def3[ghi]]]") == "abcdefghighighidefghighighi"
    assert candidate(s = "2[abc2[def3[ghi]]]") == "abcdefghighighidefghighighiabcdefghighighidefghighighi"
    assert candidate(s = "1[2[3[4[5[a]]]]]") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "5[ab3[cd]]") == "abcdcdcdabcdcdcdabcdcdcdabcdcdcdabcdcdcd"
    assert candidate(s = "2[x3[y4[z]]]1[w]") == "xyzzzzyzzzzyzzzzxyzzzzyzzzzyzzzzw"
    assert candidate(s = "7[2[a]3[b]]") == "aabbbaabbbaabbbaabbbaabbbaabbbaabbb"
    assert candidate(s = "9[8[7[6[5[4[3[2[1[0[a]]]]]]]]]]") == ""
    assert candidate(s = "4[x5[y]]") == "xyyyyyxyyyyyxyyyyyxyyyyy"
    assert candidate(s = "2[abc3[def4[ghi]]]") == "abcdefghighighighidefghighighighidefghighighighiabcdefghighighighidefghighighighidefghighighighi"
    assert candidate(s = "5[ab2[c]]3[xy]2[de]") == "abccabccabccabccabccxyxyxydede"
    assert candidate(s = "5[abc2[de]]") == "abcdedeabcdedeabcdedeabcdedeabcdede"
    assert candidate(s = "7[k2[3[xyz]]]") == "kxyzxyzxyzxyzxyzxyzkxyzxyzxyzxyzxyzxyzkxyzxyzxyzxyzxyzxyzkxyzxyzxyzxyzxyzxyzkxyzxyzxyzxyzxyzxyzkxyzxyzxyzxyzxyzxyzkxyzxyzxyzxyzxyzxyz"
    assert candidate(s = "1[abc2[def]]") == "abcdefdef"
    assert candidate(s = "2[3[4[5[6[7[8[9[0[1[a]]]]]]]]]]") == ""
    assert candidate(s = "3[2[1[x]]]") == "xxxxxx"
    assert candidate(s = "5[ab2[cd]]") == "abcdcdabcdcdabcdcdabcdcdabcdcd"
    assert candidate(s = "6[5[4[3[2[1[a]]]]]]") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "7[xyz]3[abc2[def1[ghi]]]") == "xyzxyzxyzxyzxyzxyzxyzabcdefghidefghiabcdefghidefghiabcdefghidefghi"
    assert candidate(s = "x1[y2[z3[a4[b5[c]]]]]") == "xyzabcccccbcccccbcccccbcccccabcccccbcccccbcccccbcccccabcccccbcccccbcccccbccccczabcccccbcccccbcccccbcccccabcccccbcccccbcccccbcccccabcccccbcccccbcccccbccccc"
    assert candidate(s = "3[ab2[c3[d]]]") == "abcdddcdddabcdddcdddabcdddcddd"
    assert candidate(s = "6[a2[b3[c4[d]]]]") == "abcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcddddabcddddcddddcddddbcddddcddddcdddd"
    assert candidate(s = "15[a]") == "aaaaaaaaaaaaaaa"
    assert candidate(s = "5[2[3[a]]]") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "2[xy3[z]]4[ab]") == "xyzzzxyzzzabababab"
    assert candidate(s = "1[a2[b3[c4[d5[e]]]]]") == "abcdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeeebcdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeee"
    assert candidate(s = "4[a3[b]]") == "abbbabbbabbbabbb"
    assert candidate(s = "2[ab]3[cd]4[ef]") == "ababcdcdcdefefefef"
    assert candidate(s = "1[2[3[4[5[6[7[8[9[0[x]]]]]]]]]]") == ""
    assert candidate(s = "1[2[3[4[5[6[x]]]]]]") == "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    assert candidate(s = "2[a3[b4[c5[d6[e7[f]]]]]]") == "abcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffbcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffbcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffabcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffbcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffbcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffcdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffffdefffffffefffffffefffffffefffffffefffffffefffffff"
    assert candidate(s = "4[a3[b2[c1[d]]]]") == "abcdcdbcdcdbcdcdabcdcdbcdcdbcdcdabcdcdbcdcdbcdcdabcdcdbcdcdbcdcd"
    assert candidate(s = "3[2[3[4[5[a]]]]]") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(s = "1[xyz]2[uvw]3[2[abc]3[def]]4[ghi]") == "xyzuvwuvwabcabcdefdefdefabcabcdefdefdefabcabcdefdefdefghighighighi"
    assert candidate(s = "3[xyz2[abc]4[def]]5[ghi]") == "xyzabcabcdefdefdefdefxyzabcabcdefdefdefdefxyzabcabcdefdefdefdefghighighighighi"
    assert candidate(s = "2[2[2[2[2[abc]]]]]") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(s = "3[b2[c]1[d]]4[e]") == "bccdbccdbccdeeee"
    assert candidate(s = "a2[b3[c4[d5[e]]]]") == "abcdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeeebcdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeeecdeeeeedeeeeedeeeeedeeeee"


