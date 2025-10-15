def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "aab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "bacbac") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bacbac") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbcc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbcc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "acbac") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "acbac") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "aababacaba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aababacaba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "bbcc") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bbcc") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "cccc") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cccc") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaa") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaa") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "cab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "bb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "b") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "b") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "ac") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ac") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaabbbccc") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaabbbccc") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "abac") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abac") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "bbbbbbb") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bbbbbbb") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabccba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabccba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "bbccaa") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bbccaa") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "cba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "ccbaab") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ccbaab") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "ccc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ccc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "ccccab") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ccccab") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "aababab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aababab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaabbbbbc") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaabbbbbc") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word = "cccbbaaa") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cccbbaaa") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "cbac") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cbac") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "ba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "cccccccc") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cccccccc") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "abbbccca") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abbbccca") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcbac") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcbac") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "bbbb") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bbbb") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "caabbac") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "caabbac") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "babbabcabcbacbacbacb") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "babbabcabcbacbacbacb") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaab") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaab") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcaabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcaabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "bbbbbb") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bbbbbb") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "cabababc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cabababc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "bacbacbac") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bacbacbac") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcaacb") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcaacb") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcababc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcababc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacbacbac") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacbacbac") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcbcbc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcbcbc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaa") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaa") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "bbbaccc") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bbbaccc") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word = "babcbcbcabc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "babcbcbcabc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcbcb") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcbcb") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "aacaabbc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aacaabbc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacbac") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacbac") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "acb") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "acb") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "ababab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ababab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "cabcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cabcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "abab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "accba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "accba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabacbac") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabacbac") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "bababab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bababab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "bbbbbbbb") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bbbbbbbb") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "acbabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "acbabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabcbc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabcbc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcaabcbacbacb") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcaabcbacbacb") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabcbabccba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabcbabccba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "abccccba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abccccba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "baabbcc") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "baabbcc") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "cabcab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cabcab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "cbacba") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cbacba") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "bac") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bac") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaa") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaa") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcbbca") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcbbca") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "bca") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bca") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "ababac") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ababac") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "cbacbacb") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cbacbacb") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "abccba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abccba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "cabcabcab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cabcabcab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabcabc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabcabc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "bbbacabc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bbbacabc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "acbacbac") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "acbacbac") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaac") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaac") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "bbaaac") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bbaaac") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcacbac") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcacbac") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "abacbc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacbc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "ccca") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ccca") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "cccccc") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cccccc") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbaacc") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbaacc") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "acbacbacbac") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "acbacbacbac") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "acbacbacb") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "acbacbacb") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "ccccbbbaaa") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ccccbbbaaa") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "acabca") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "acabca") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "abbbcccaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abbbcccaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbbccc") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbbccc") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcbac") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcbac") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabca") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabca") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "ccababca") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ccababca") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "bababacbcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bababacbcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "accab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "accab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "abbbac") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abbbac") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "acbbca") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "acbbca") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcabca") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcabca") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcbcbcbc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcbcbcbc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabcbcbc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabcbcbc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcabcabcabc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcabcabcabc") == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "aab") == 3
    assert candidate(word = "abc") == 0
    assert candidate(word = "bacbac") == 6
    assert candidate(word = "aabbcc") == 6
    assert candidate(word = "acbac") == 4
    assert candidate(word = "aababacaba") == 8
    assert candidate(word = "abcabc") == 0
    assert candidate(word = "bbcc") == 5
    assert candidate(word = "cccc") == 8
    assert candidate(word = "aaaaa") == 10
    assert candidate(word = "cab") == 3
    assert candidate(word = "bb") == 4
    assert candidate(word = "aaa") == 6
    assert candidate(word = "b") == 2
    assert candidate(word = "ac") == 1
    assert candidate(word = "aaabbbccc") == 12
    assert candidate(word = "abac") == 2
    assert candidate(word = "bbbbbbb") == 14
    assert candidate(word = "aabccba") == 8
    assert candidate(word = "bbccaa") == 9
    assert candidate(word = "cba") == 6
    assert candidate(word = "ccbaab") == 9
    assert candidate(word = "ccc") == 6
    assert candidate(word = "bcab") == 2
    assert candidate(word = "ccccab") == 9
    assert candidate(word = "aababab") == 5
    assert candidate(word = "aaaaaabbbbbc") == 18
    assert candidate(word = "cccbbaaa") == 16
    assert candidate(word = "cbac") == 5
    assert candidate(word = "abcabcabc") == 0
    assert candidate(word = "ba") == 4
    assert candidate(word = "cccccccc") == 16
    assert candidate(word = "abbbccca") == 10
    assert candidate(word = "abcbac") == 3
    assert candidate(word = "bbbb") == 8
    assert candidate(word = "caabbac") == 8
    assert candidate(word = "babbabcabcbacbacbacb") == 16
    assert candidate(word = "aaaab") == 7
    assert candidate(word = "bcaabc") == 3
    assert candidate(word = "bbbbbb") == 12
    assert candidate(word = "cabababc") == 4
    assert candidate(word = "bacbacbac") == 9
    assert candidate(word = "bcaacb") == 6
    assert candidate(word = "abcababc") == 1
    assert candidate(word = "abacbacbac") == 8
    assert candidate(word = "bcbcbc") == 3
    assert candidate(word = "aaaaaaaa") == 16
    assert candidate(word = "bbbaccc") == 11
    assert candidate(word = "babcbcbcabc") == 4
    assert candidate(word = "bcbcb") == 4
    assert candidate(word = "aacaabbc") == 7
    assert candidate(word = "abacbac") == 5
    assert candidate(word = "aaaaaa") == 12
    assert candidate(word = "acb") == 3
    assert candidate(word = "ababab") == 3
    assert candidate(word = "cabcabc") == 2
    assert candidate(word = "aabbccabc") == 6
    assert candidate(word = "abab") == 2
    assert candidate(word = "abacab") == 3
    assert candidate(word = "bcabc") == 1
    assert candidate(word = "accba") == 7
    assert candidate(word = "aabacbac") == 7
    assert candidate(word = "bababab") == 5
    assert candidate(word = "bbbbbbbb") == 16
    assert candidate(word = "acbabc") == 3
    assert candidate(word = "aabcbc") == 3
    assert candidate(word = "abcaabcbacbacb") == 10
    assert candidate(word = "aabcbabccba") == 10
    assert candidate(word = "abccccba") == 10
    assert candidate(word = "baabbcc") == 8
    assert candidate(word = "cabcab") == 3
    assert candidate(word = "cbacba") == 9
    assert candidate(word = "bac") == 3
    assert candidate(word = "aaaa") == 8
    assert candidate(word = "abcbbca") == 5
    assert candidate(word = "bca") == 3
    assert candidate(word = "ababac") == 3
    assert candidate(word = "cbacbacb") == 10
    assert candidate(word = "abccba") == 6
    assert candidate(word = "cabcabcab") == 3
    assert candidate(word = "abcabcabcabcabc") == 0
    assert candidate(word = "bbbacabc") == 7
    assert candidate(word = "acbacbac") == 7
    assert candidate(word = "aaac") == 5
    assert candidate(word = "bbaaac") == 9
    assert candidate(word = "abcacbac") == 4
    assert candidate(word = "abacbc") == 3
    assert candidate(word = "ccca") == 8
    assert candidate(word = "cccccc") == 12
    assert candidate(word = "aabbaacc") == 10
    assert candidate(word = "acbacbacbac") == 10
    assert candidate(word = "abcba") == 4
    assert candidate(word = "acbacbacb") == 9
    assert candidate(word = "ccccbbbaaa") == 20
    assert candidate(word = "acabca") == 3
    assert candidate(word = "abbbcccaa") == 12
    assert candidate(word = "aabbbccc") == 10
    assert candidate(word = "abcabcbac") == 3
    assert candidate(word = "abcabca") == 2
    assert candidate(word = "ccababca") == 7
    assert candidate(word = "bababacbcabc") == 6
    assert candidate(word = "accab") == 4
    assert candidate(word = "abbbac") == 6
    assert candidate(word = "acbbca") == 6
    assert candidate(word = "bcabca") == 3
    assert candidate(word = "bcbcbcbc") == 4
    assert candidate(word = "aabcbcbc") == 4
    assert candidate(word = "abcabcabcabc") == 0


