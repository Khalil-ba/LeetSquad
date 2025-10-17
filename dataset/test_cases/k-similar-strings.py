def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "ccbbaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "ccbbaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abac",s2 = "baca") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abac",s2 = "baca") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "dcba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "dcba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abc",s2 = "bca") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc",s2 = "bca") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "fedcba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "fedcba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabc",s2 = "abac") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabc",s2 = "abac") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcde",s2 = "edcba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcde",s2 = "edcba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ab",s2 = "ba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ab",s2 = "ba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "abcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "abcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbaabbcc",s2 = "ccbbaabbaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbaabbcc",s2 = "ccbbaabbaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeff",s2 = "ffeeddccbbaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeff",s2 = "ffeeddccbbaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabc",s2 = "cbacbacba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabc",s2 = "cbacbacba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdeabcde",s2 = "edcbaedcba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdeabcde",s2 = "edcbaedcba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeff",s2 = "fedcbafedcba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeff",s2 = "fedcbafedcba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "bbaacc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "bbaacc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccdd",s2 = "ddccbaab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccdd",s2 = "ddccbaab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "hgfedcba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "hgfedcba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "ccbaab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "ccbaab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefabc",s2 = "cbadefabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefabc",s2 = "cbadefabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabc",s2 = "bcbacabac") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabc",s2 = "bcbacabac") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabc",s2 = "cbaabcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabc",s2 = "cbaabcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcd",s2 = "dcbaabcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcd",s2 = "dcbaabcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefabc",s2 = "fdecbaabc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefabc",s2 = "fdecbaabc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "jihgfedcba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "jihgfedcba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcd",s2 = "dcbadcba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcd",s2 = "dcbadcba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "fabcde") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "fabcde") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbc",s2 = "bbaca") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbc",s2 = "bbaca") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "gfedcba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "gfedcba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbbccc",s2 = "cccbbbaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbbccc",s2 = "cccbbbaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "cbacba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "cbacba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abababab",s2 = "babababa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abababab",s2 = "babababa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabcabc",s2 = "cbacbacbacba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabcabc",s2 = "cbacbacbacba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeff",s2 = "abcdefabcdef") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeff",s2 = "abcdefabcdef") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcdabcd",s2 = "dcbaabcdabcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcdabcd",s2 = "dcbaabcdabcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeff",s2 = "ffeeddccbaab") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeff",s2 = "ffeeddccbaab") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabdc",s2 = "dcbaacb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabdc",s2 = "dcbaacb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabc",s2 = "cbacba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabc",s2 = "cbacba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabc",s2 = "bcbaca") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabc",s2 = "bcbaca") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefabcdef",s2 = "defabcfedcba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefabcdef",s2 = "defabcfedcba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabc",s2 = "cbabac") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabc",s2 = "cbabac") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabc",s2 = "cccbaabba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabc",s2 = "cccbaabba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcdef",s2 = "defbbaac") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcdef",s2 = "defbbaac") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefabcdef",s2 = "fedcbafedcba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefabcdef",s2 = "fedcbafedcba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaabbbb",s2 = "bbbbaaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaabbbb",s2 = "bbbbaaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abac",s2 = "caba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abac",s2 = "caba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgabcdefg",s2 = "gfedcbagfedcba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgabcdefg",s2 = "gfedcbagfedcba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcbca",s2 = "bcbaca") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcbca",s2 = "bcbaca") == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s1 = "aabbcc",s2 = "ccbbaa") == 2
    assert candidate(s1 = "abac",s2 = "baca") == 2
    assert candidate(s1 = "abcd",s2 = "dcba") == 2
    assert candidate(s1 = "abc",s2 = "bca") == 2
    assert candidate(s1 = "abcdef",s2 = "fedcba") == 3
    assert candidate(s1 = "aabc",s2 = "abac") == 1
    assert candidate(s1 = "abcde",s2 = "edcba") == 2
    assert candidate(s1 = "ab",s2 = "ba") == 1
    assert candidate(s1 = "aabbcc",s2 = "abcabc") == 2
    assert candidate(s1 = "aabbaabbcc",s2 = "ccbbaabbaa") == 2
    assert candidate(s1 = "aabbccddeeff",s2 = "ffeeddccbbaa") == 6
    assert candidate(s1 = "abcabcabc",s2 = "cbacbacba") == 3
    assert candidate(s1 = "abcdeabcde",s2 = "edcbaedcba") == 4
    assert candidate(s1 = "aabbccddeeff",s2 = "fedcbafedcba") == 7
    assert candidate(s1 = "aabbcc",s2 = "bbaacc") == 2
    assert candidate(s1 = "aabbccdd",s2 = "ddccbaab") == 5
    assert candidate(s1 = "abcdefgh",s2 = "hgfedcba") == 4
    assert candidate(s1 = "aabbcc",s2 = "ccbaab") == 3
    assert candidate(s1 = "abcdefabc",s2 = "cbadefabc") == 1
    assert candidate(s1 = "abcabcabc",s2 = "bcbacabac") == 4
    assert candidate(s1 = "abcabcabc",s2 = "cbaabcabc") == 1
    assert candidate(s1 = "abcdabcd",s2 = "dcbaabcd") == 2
    assert candidate(s1 = "abcdefabc",s2 = "fdecbaabc") == 4
    assert candidate(s1 = "abcdefghij",s2 = "jihgfedcba") == 5
    assert candidate(s1 = "abcdabcd",s2 = "dcbadcba") == 4
    assert candidate(s1 = "abcdef",s2 = "fabcde") == 5
    assert candidate(s1 = "aabbc",s2 = "bbaca") == 3
    assert candidate(s1 = "abcdefg",s2 = "gfedcba") == 3
    assert candidate(s1 = "aabbbccc",s2 = "cccbbbaa") == 3
    assert candidate(s1 = "aabbcc",s2 = "cbacba") == 3
    assert candidate(s1 = "abababab",s2 = "babababa") == 4
    assert candidate(s1 = "abcabcabcabc",s2 = "cbacbacbacba") == 4
    assert candidate(s1 = "aabbccddeeff",s2 = "abcdefabcdef") == 7
    assert candidate(s1 = "abcdabcdabcd",s2 = "dcbaabcdabcd") == 2
    assert candidate(s1 = "aabbccddeeff",s2 = "ffeeddccbaab") == 7
    assert candidate(s1 = "abcabdc",s2 = "dcbaacb") == 4
    assert candidate(s1 = "abcabc",s2 = "cbacba") == 2
    assert candidate(s1 = "abcabc",s2 = "bcbaca") == 3
    assert candidate(s1 = "abcdefabcdef",s2 = "defabcfedcba") == 6
    assert candidate(s1 = "abcabc",s2 = "cbabac") == 2
    assert candidate(s1 = "abcabcabc",s2 = "cccbaabba") == 4
    assert candidate(s1 = "aabbcdef",s2 = "defbbaac") == 4
    assert candidate(s1 = "abcdefabcdef",s2 = "fedcbafedcba") == 6
    assert candidate(s1 = "aaaabbbb",s2 = "bbbbaaaa") == 4
    assert candidate(s1 = "abac",s2 = "caba") == 2
    assert candidate(s1 = "abcdefgabcdefg",s2 = "gfedcbagfedcba") == 6
    assert candidate(s1 = "abcbca",s2 = "bcbaca") == 2


