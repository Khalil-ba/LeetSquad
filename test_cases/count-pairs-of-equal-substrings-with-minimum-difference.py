def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(firstString = "abcdefghijklmnopqrstuvwxyz",secondString = "zyxwvutsrqponmlkjihgfedcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abcdefghijklmnopqrstuvwxyz",secondString = "zyxwvutsrqponmlkjihgfedcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abcabcabc",secondString = "cbacbacba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abcabcabc",secondString = "cbacbacba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abc",secondString = "cab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abc",secondString = "cab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "xyz",secondString = "zyxzyxzyx") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "xyz",secondString = "zyxzyxzyx") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "aaaabbbb",secondString = "bbbbaaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "aaaabbbb",secondString = "bbbbaaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "aaaaaa",secondString = "bbbbb") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "aaaaaa",secondString = "bbbbb") == 0: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "hello",secondString = "world") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "hello",secondString = "world") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "unique",secondString = "uniquestrings") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "unique",secondString = "uniquestrings") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "ababababab",secondString = "bababababa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "ababababab",secondString = "bababababa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "python",secondString = "nohtypython") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "python",secondString = "nohtypython") == 6: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abcde",secondString = "fghij") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abcde",secondString = "fghij") == 0: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "hello",secondString = "olleh") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "hello",secondString = "olleh") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "mississippi",secondString = "ppississimm") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "mississippi",secondString = "ppississimm") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abcdabcd",secondString = "dcbaabcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abcdabcd",secondString = "dcbaabcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "z",secondString = "z") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "z",secondString = "z") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abacabadabacaba",secondString = "abcabcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abacabadabacaba",secondString = "abcabcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "aabbcc",secondString = "abcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "aabbcc",secondString = "abcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abc",secondString = "abc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abc",secondString = "abc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "zzzz",secondString = "zzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "zzzz",secondString = "zzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "aaaaa",secondString = "bbbbb") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "aaaaa",secondString = "bbbbb") == 0: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abc",secondString = "abcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abc",secondString = "abcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "banana",secondString = "nabana") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "banana",secondString = "nabana") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "aaaaa",secondString = "aaaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "aaaaa",secondString = "aaaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "hello",secondString = "hello") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "hello",secondString = "hello") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abcdefg",secondString = "ghfedcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abcdefg",secondString = "ghfedcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "xyz",secondString = "zyxzyx") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "xyz",secondString = "zyxzyx") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "aaa",secondString = "aaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "aaa",secondString = "aaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abcabc",secondString = "cbacba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abcabc",secondString = "cbacba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "hello",secondString = "ollhe") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "hello",secondString = "ollhe") == 2: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "leetcode",secondString = "leetcode") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "leetcode",secondString = "leetcode") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "hello",secondString = "ohell") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "hello",secondString = "ohell") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abababab",secondString = "babababa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abababab",secondString = "babababa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "mississippi",secondString = "ississippi") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "mississippi",secondString = "ississippi") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "zzzz",secondString = "zzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "zzzz",secondString = "zzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "aaaa",secondString = "bbbb") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "aaaa",secondString = "bbbb") == 0: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "zzzz",secondString = "zzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "zzzz",secondString = "zzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "banana",secondString = "nanaba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "banana",secondString = "nanaba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abcdxyz",secondString = "xyzabcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abcdxyz",secondString = "xyzabcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "mississippi",secondString = "issipi") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "mississippi",secondString = "issipi") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abcde",secondString = "edcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abcde",secondString = "edcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "a",secondString = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "a",secondString = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abcdefg",secondString = "gfedcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abcdefg",secondString = "gfedcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "xyz",secondString = "zyx") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "xyz",secondString = "zyx") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "a",secondString = "aaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "a",secondString = "aaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "xyz",secondString = "zyxwvut") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "xyz",secondString = "zyxwvut") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "aaaaaab",secondString = "bbbaaaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "aaaaaab",secondString = "bbbaaaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "xyz",secondString = "zyxzyxzyxzyx") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "xyz",secondString = "zyxzyxzyxzyx") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abcdef",secondString = "ghijkl") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abcdef",secondString = "ghijkl") == 0: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abcd",secondString = "bccda") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abcd",secondString = "bccda") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "software",secondString = "ware") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "software",secondString = "ware") == 4: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abcabc",secondString = "bcbcbcb") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abcabc",secondString = "bcbcbcb") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abc",secondString = "def") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abc",secondString = "def") == 0: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "mississippi",secondString = "pississippi") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "mississippi",secondString = "pississippi") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "aabbcc",secondString = "ccbbaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "aabbcc",secondString = "ccbbaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "aabbccdd",secondString = "ddbbaacc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "aabbccdd",secondString = "ddbbaacc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "aaaaaa",secondString = "bbbbbb") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "aaaaaa",secondString = "bbbbbb") == 0: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "ab",secondString = "cd") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "ab",secondString = "cd") == 0: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "leetcode",secondString = "etco") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "leetcode",secondString = "etco") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "programming",secondString = "gnimmargorp") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "programming",secondString = "gnimmargorp") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abcabcabc",secondString = "abc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abcabcabc",secondString = "abc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "hello",secondString = "yellow") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "hello",secondString = "yellow") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "aaaaabbbbb",secondString = "bbbbbbaaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "aaaaabbbbb",secondString = "bbbbbbaaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "aaaabbbbcccc",secondString = "bbbbaaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "aaaabbbbcccc",secondString = "bbbbaaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abcdef",secondString = "fedcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abcdef",secondString = "fedcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "engineer",secondString = "engine") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "engineer",secondString = "engine") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abc",secondString = "defg") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abc",secondString = "defg") == 0: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abcabcabcabc",secondString = "abcabcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abcabcabcabc",secondString = "abcabcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abababab",secondString = "bababa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abababab",secondString = "bababa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abcabcabcabc",secondString = "abcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abcabcabcabc",secondString = "abcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "zzzzz",secondString = "zzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "zzzzz",secondString = "zzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abcabcabcabc",secondString = "cbacbacbacba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abcabcabcabc",secondString = "cbacbacbacba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "aaaaaaa",secondString = "bbbbbbb") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "aaaaaaa",secondString = "bbbbbbb") == 0: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "xyza",secondString = "ayzx") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "xyza",secondString = "ayzx") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "zzzzzz",secondString = "zzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "zzzzzz",secondString = "zzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abab",secondString = "baba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abab",secondString = "baba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "abcabcabc",secondString = "abcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "abcabcabc",secondString = "abcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "testcase",secondString = "casesensitive") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "testcase",secondString = "casesensitive") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "test",secondString = "sett") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "test",secondString = "sett") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "aaa",secondString = "aaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "aaa",secondString = "aaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "aaaa",secondString = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "aaaa",secondString = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "hello",secondString = "llhe") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "hello",secondString = "llhe") == 2: {e}')
    
    total += 1
    try:
        result = candidate(firstString = "aaaa",secondString = "aaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(firstString = "aaaa",secondString = "aaaa") == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(firstString = "abcdefghijklmnopqrstuvwxyz",secondString = "zyxwvutsrqponmlkjihgfedcba") == 1
    assert candidate(firstString = "abcabcabc",secondString = "cbacbacba") == 1
    assert candidate(firstString = "abc",secondString = "cab") == 2
    assert candidate(firstString = "xyz",secondString = "zyxzyxzyx") == 1
    assert candidate(firstString = "aaaabbbb",secondString = "bbbbaaaa") == 1
    assert candidate(firstString = "aaaaaa",secondString = "bbbbb") == 0
    assert candidate(firstString = "hello",secondString = "world") == 1
    assert candidate(firstString = "unique",secondString = "uniquestrings") == 1
    assert candidate(firstString = "ababababab",secondString = "bababababa") == 1
    assert candidate(firstString = "python",secondString = "nohtypython") == 6
    assert candidate(firstString = "abcde",secondString = "fghij") == 0
    assert candidate(firstString = "hello",secondString = "olleh") == 1
    assert candidate(firstString = "mississippi",secondString = "ppississimm") == 1
    assert candidate(firstString = "abcdabcd",secondString = "dcbaabcd") == 4
    assert candidate(firstString = "z",secondString = "z") == 1
    assert candidate(firstString = "abacabadabacaba",secondString = "abcabcabc") == 2
    assert candidate(firstString = "aabbcc",secondString = "abcabc") == 1
    assert candidate(firstString = "abc",secondString = "abc") == 3
    assert candidate(firstString = "zzzz",secondString = "zzzzzzzz") == 1
    assert candidate(firstString = "aaaaa",secondString = "bbbbb") == 0
    assert candidate(firstString = "abc",secondString = "abcabcabc") == 3
    assert candidate(firstString = "banana",secondString = "nabana") == 1
    assert candidate(firstString = "aaaaa",secondString = "aaaaa") == 1
    assert candidate(firstString = "hello",secondString = "hello") == 1
    assert candidate(firstString = "abcdefg",secondString = "ghfedcba") == 1
    assert candidate(firstString = "xyz",secondString = "zyxzyx") == 1
    assert candidate(firstString = "aaa",secondString = "aaa") == 1
    assert candidate(firstString = "abcabc",secondString = "cbacba") == 1
    assert candidate(firstString = "hello",secondString = "ollhe") == 2
    assert candidate(firstString = "leetcode",secondString = "leetcode") == 1
    assert candidate(firstString = "hello",secondString = "ohell") == 1
    assert candidate(firstString = "abababab",secondString = "babababa") == 1
    assert candidate(firstString = "mississippi",secondString = "ississippi") == 1
    assert candidate(firstString = "zzzz",secondString = "zzzz") == 1
    assert candidate(firstString = "aaaa",secondString = "bbbb") == 0
    assert candidate(firstString = "zzzz",secondString = "zzzzzzzzz") == 1
    assert candidate(firstString = "banana",secondString = "nanaba") == 2
    assert candidate(firstString = "abcdxyz",secondString = "xyzabcd") == 4
    assert candidate(firstString = "mississippi",secondString = "issipi") == 1
    assert candidate(firstString = "abcde",secondString = "edcba") == 1
    assert candidate(firstString = "a",secondString = "a") == 1
    assert candidate(firstString = "abcdefg",secondString = "gfedcba") == 1
    assert candidate(firstString = "xyz",secondString = "zyx") == 1
    assert candidate(firstString = "a",secondString = "aaaa") == 1
    assert candidate(firstString = "xyz",secondString = "zyxwvut") == 1
    assert candidate(firstString = "aaaaaab",secondString = "bbbaaaaa") == 1
    assert candidate(firstString = "xyz",secondString = "zyxzyxzyxzyx") == 1
    assert candidate(firstString = "abcdef",secondString = "ghijkl") == 0
    assert candidate(firstString = "abcd",secondString = "bccda") == 1
    assert candidate(firstString = "software",secondString = "ware") == 4
    assert candidate(firstString = "abcabc",secondString = "bcbcbcb") == 1
    assert candidate(firstString = "abc",secondString = "def") == 0
    assert candidate(firstString = "mississippi",secondString = "pississippi") == 1
    assert candidate(firstString = "aabbcc",secondString = "ccbbaa") == 1
    assert candidate(firstString = "aabbccdd",secondString = "ddbbaacc") == 1
    assert candidate(firstString = "aaaaaa",secondString = "bbbbbb") == 0
    assert candidate(firstString = "ab",secondString = "cd") == 0
    assert candidate(firstString = "leetcode",secondString = "etco") == 1
    assert candidate(firstString = "programming",secondString = "gnimmargorp") == 1
    assert candidate(firstString = "abcabcabc",secondString = "abc") == 3
    assert candidate(firstString = "hello",secondString = "yellow") == 1
    assert candidate(firstString = "aaaaabbbbb",secondString = "bbbbbbaaaa") == 1
    assert candidate(firstString = "aaaabbbbcccc",secondString = "bbbbaaaa") == 1
    assert candidate(firstString = "abcdef",secondString = "fedcba") == 1
    assert candidate(firstString = "engineer",secondString = "engine") == 1
    assert candidate(firstString = "abc",secondString = "defg") == 0
    assert candidate(firstString = "abcabcabcabc",secondString = "abcabcabcabc") == 3
    assert candidate(firstString = "abababab",secondString = "bababa") == 1
    assert candidate(firstString = "abcabcabcabc",secondString = "abcabc") == 3
    assert candidate(firstString = "zzzzz",secondString = "zzzzz") == 1
    assert candidate(firstString = "abcabcabcabc",secondString = "cbacbacbacba") == 1
    assert candidate(firstString = "aaaaaaa",secondString = "bbbbbbb") == 0
    assert candidate(firstString = "xyza",secondString = "ayzx") == 1
    assert candidate(firstString = "zzzzzz",secondString = "zzzzzz") == 1
    assert candidate(firstString = "abab",secondString = "baba") == 1
    assert candidate(firstString = "abcabcabc",secondString = "abcabcabc") == 3
    assert candidate(firstString = "testcase",secondString = "casesensitive") == 1
    assert candidate(firstString = "test",secondString = "sett") == 1
    assert candidate(firstString = "aaa",secondString = "aaaa") == 1
    assert candidate(firstString = "aaaa",secondString = "a") == 1
    assert candidate(firstString = "hello",secondString = "llhe") == 2
    assert candidate(firstString = "aaaa",secondString = "aaaa") == 1


