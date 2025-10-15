def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == "aabbcc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == "aabbcc": {e}')
    
    total += 1
    try:
        result = candidate(s = "bdda") == "addb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bdda") == "addb": {e}')
    
    total += 1
    try:
        result = candidate(s = "cba") == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cba") == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "bac") == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bac") == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaa") == "aaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa") == "aaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde") == "abcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde") == "abcde": {e}')
    
    total += 1
    try:
        result = candidate(s = "zza") == "azz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zza") == "azz": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == "abcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == "abcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "edcba") == "abcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "edcba") == "abcde": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == "aaaaaaaabcbdbcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == "aaaaaaaabcbdbcb": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccdddd") == "aaaabbbbccccdddd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccdddd") == "aaaabbbbccccdddd": {e}')
    
    total += 1
    try:
        result = candidate(s = "fedcb") == "bcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "fedcb") == "bcdef": {e}')
    
    total += 1
    try:
        result = candidate(s = "ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp") == "ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp") == "ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbccc") == "aaabbbccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbccc") == "aaabbbccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "fedcbafedcbafedcba") == "aaabcdefbcdefbcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "fedcbafedcbafedcba") == "aaabcdefbcdefbcdef": {e}')
    
    total += 1
    try:
        result = candidate(s = "fedcbaghijk") == "abcdefghijk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "fedcbaghijk") == "abcdefghijk": {e}')
    
    total += 1
    try:
        result = candidate(s = "mjwqeqpdpdwdwwvwqwdqeqpqwwqwwqwwpqwwqwpqwwqppwpqpqppwpqpqpqpqpqpqpqpqpqpqpqpqpqpqppwqqqqqqqppqqqpqpwq") == "ddddepppppppppppppppppppppppppppppqqqqqqqqqqqqwwqqqqqqqqqqqqqqwqqwqwwqwqwwqwwqwwqwwqqqwqwvwwwppqeqwjm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mjwqeqpdpdwdwwvwqwdqeqpqwwqwwqwwpqwwqwpqwwqppwpqpqppwpqpqpqpqpqpqpqpqpqpqpqpqpqpqppwqqqqqqqppqqqpqpwq") == "ddddepppppppppppppppppppppppppppppqqqqqqqqqqqqwwqqqqqqqqqqqqqqwqqwqwwqwqwwqwwqwwqwwqqqwqwvwwwppqeqwjm": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnooopppqqqrrrssstttuuuuvvvwwwxxxyyyzzz") == "aaabbbcccdddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnooopppqqqrrrssstttuuuuvvvwwwxxxyyyzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnooopppqqqrrrssstttuuuuvvvwwwxxxyyyzzz") == "aaabbbcccdddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnooopppqqqrrrssstttuuuuvvvwwwxxxyyyzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "acbcbabcbabcba") == "aaaabcbbcbbcbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acbcbabcbabcba") == "aaaabcbbcbbcbc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "aaaaaaaaaaaaaaaaaaabcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "aaaaaaaaaaaaaaaaaaabcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc": {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbaaa") == "aaabbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbaaa") == "aaabbb": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcba") == "aabcdcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcba") == "aabcdcb": {e}')
    
    total += 1
    try:
        result = candidate(s = "zazbzczdz") == "abcdzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zazbzczdz") == "abcdzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzaaa") == "aaazzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzaaa") == "aaazzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "amazingleetcodeproblem") == "aabelmorpedocteelgnizm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "amazingleetcodeproblem") == "aabelmorpedocteelgnizm": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgzyxwvutsrqponmlkjihgfedcba") == "aabcdefghijklmnopqrstuvwxyzgfedcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgzyxwvutsrqponmlkjihgfedcba") == "aabcdefghijklmnopqrstuvwxyzgfedcb": {e}')
    
    total += 1
    try:
        result = candidate(s = "fedcbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbac") == "aaaaaaaaaaaaaaaaabcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbccdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "fedcbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbac") == "aaaaaaaaaaaaaaaaabcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbccdef": {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra") == "aaaaarbdcrb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra") == "aaaaarbdcrb": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabccccaaa") == "aaaaaccccb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabccccaaa") == "aaaaaccccb": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcda") == "aaadcbdcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcda") == "aaadcbdcb": {e}')
    
    total += 1
    try:
        result = candidate(s = "bacbacbacb") == "aaabbccbcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bacbacbacb") == "aaabbccbcb": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde") == "aaaaaaaaaabcdedcbedcbedcbedcbedcbedcbedcbedcbedcbe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde") == "aaaaaaaaaabcdedcbedcbedcbedcbedcbedcbedcbedcbedcbe": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaa") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaa") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzz") == "abcdefghijklmnopqrstuvwxyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzz") == "abcdefghijklmnopqrstuvwxyzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzyyyxxxwwwwvvvuuutttsssrqqqpppoonnmmlkkjjiihhggffeedcba") == "abcdeeffgghhiijjkklmmnnoopppqqqrssstttuuuvvvwwwwxxxyyyzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzyyyxxxwwwwvvvuuutttsssrqqqpppoonnmmlkkjjiihhggffeedcba") == "abcdeeffgghhiijjkklmmnnoopppqqqrssstttuuuvvvwwwwxxxyyyzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "caabdbac") == "aaabcdbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "caabdbac") == "aaabcdbc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffff") == "aaaabbbbccccddddeeeeffff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffff") == "aaaabbbbccccddddeeeeffff": {e}')
    
    total += 1
    try:
        result = candidate(s = "fedcba") == "abcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "fedcba") == "abcdef": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabc") == "aaabcbcdcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabc") == "aaabcbcdcb": {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcode") == "cdeoteel"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcode") == "cdeoteel": {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar") == "aacecrr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar") == "aacecrr": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzyyxxwvwuvuttrssrqqponnmlkkjjiihhhggffeeddcbbbaaa") == "aaabbbcddeeffgghhhiijjkklmnnopqqrssrttuvuwvwxxyyzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzyyxxwvwuvuttrssrqqponnmlkkjjiihhhggffeeddcbbbaaa") == "aaabbbcddeeffgghhhiijjkklmnnopqqrssrttuvuwvwxxyyzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == "aabcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == "aabcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcb": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == "aaaabcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcbzyxwvutsrqponmlkjihgfedcbzyxwvutsrqponmlkjihgfedcbz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == "aaaabcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcbzyxwvutsrqponmlkjihgfedcbzyxwvutsrqponmlkjihgfedcbz": {e}')
    
    total += 1
    try:
        result = candidate(s = "banana") == "aaannb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana") == "aaannb": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcde") == "aabcdedcbe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcde") == "aabcdedcbe": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == "iiiippssssm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == "iiiippssssm": {e}')
    
    total += 1
    try:
        result = candidate(s = "acacacacac") == "aaaaaccccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acacacacac") == "aaaaaccccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdbacd") == "aaabcdcbdcbd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdbacd") == "aaabcdcbdcbd": {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaaccdd") == "aabbccdd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaaccdd") == "aabbccdd": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcd") == "aaaabcdcbdcbdcbd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcd") == "aaaabcdcbdcbdcbd": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccddd") == "aaabbbcccddd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccddd") == "aaabbbcccddd": {e}')
    
    total += 1
    try:
        result = candidate(s = "qrsnspndpsnpppdnspndpdpsnsnspdpspndpdpsnpsdpsnpspdpsndpdpsnpdpsnpsdpsnpd") == "ddddddddddddddpnspspnsppnsppnsppspnspspnsppnpsppsnsnsppnpsnpppnspnpsnsrq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qrsnspndpsnpppdnspndpdpsnsnspdpspndpdpsnpsdpsnpspdpsndpdpsnpdpsnpsdpsnpd") == "ddddddddddddddpnspspnsppnsppnsppspnspspnsppnpsppsnsnsppnpsnpppnspnpsnsrq": {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababab") == "aaaaaaaaaaaaaabbbbbbbbbbbbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababab") == "aaaaaaaaaaaaaabbbbbbbbbbbbbb": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyxzyx") == "xxxyzyzzy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxzyx") == "xxxyzyzzy": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "aabbcc") == "aabbcc"
    assert candidate(s = "bdda") == "addb"
    assert candidate(s = "cba") == "abc"
    assert candidate(s = "bac") == "abc"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz"
    assert candidate(s = "aaa") == "aaa"
    assert candidate(s = "abcde") == "abcde"
    assert candidate(s = "zza") == "azz"
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == "abcdefghijklmnopqrstuvwxyz"
    assert candidate(s = "a") == "a"
    assert candidate(s = "edcba") == "abcde"
    assert candidate(s = "abacabadabacaba") == "aaaaaaaabcbdbcb"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(s = "aaaabbbbccccdddd") == "aaaabbbbccccdddd"
    assert candidate(s = "fedcb") == "bcdef"
    assert candidate(s = "ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp") == "ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp"
    assert candidate(s = "aaabbbccc") == "aaabbbccc"
    assert candidate(s = "fedcbafedcbafedcba") == "aaabcdefbcdefbcdef"
    assert candidate(s = "fedcbaghijk") == "abcdefghijk"
    assert candidate(s = "mjwqeqpdpdwdwwvwqwdqeqpqwwqwwqwwpqwwqwpqwwqppwpqpqppwpqpqpqpqpqpqpqpqpqpqpqpqpqpqppwqqqqqqqppqqqpqpwq") == "ddddepppppppppppppppppppppppppppppqqqqqqqqqqqqwwqqqqqqqqqqqqqqwqqwqwwqwqwwqwwqwwqwwqqqwqwvwwwppqeqwjm"
    assert candidate(s = "aaabbbcccdddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnooopppqqqrrrssstttuuuuvvvwwwxxxyyyzzz") == "aaabbbcccdddeeefffggghhhiiiijjjjkkkkllllmmmmnnnnooopppqqqrrrssstttuuuuvvvwwwxxxyyyzzz"
    assert candidate(s = "acbcbabcbabcba") == "aaaabcbbcbbcbc"
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "aaaaaaaaaaaaaaaaaaabcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc"
    assert candidate(s = "bbbaaa") == "aaabbb"
    assert candidate(s = "abcdcba") == "aabcdcb"
    assert candidate(s = "zazbzczdz") == "abcdzzzzz"
    assert candidate(s = "zzzaaa") == "aaazzz"
    assert candidate(s = "amazingleetcodeproblem") == "aabelmorpedocteelgnizm"
    assert candidate(s = "abcdefgzyxwvutsrqponmlkjihgfedcba") == "aabcdefghijklmnopqrstuvwxyzgfedcb"
    assert candidate(s = "fedcbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbac") == "aaaaaaaaaaaaaaaaabcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbccdef"
    assert candidate(s = "abracadabra") == "aaaaarbdcrb"
    assert candidate(s = "aabccccaaa") == "aaaaaccccb"
    assert candidate(s = "abcdabcda") == "aaadcbdcb"
    assert candidate(s = "bacbacbacb") == "aaabbccbcb"
    assert candidate(s = "abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde") == "aaaaaaaaaabcdedcbedcbedcbedcbedcbedcbedcbedcbedcbe"
    assert candidate(s = "zzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaazzzaaaa") == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzz") == "abcdefghijklmnopqrstuvwxyzz"
    assert candidate(s = "zzzyyyxxxwwwwvvvuuutttsssrqqqpppoonnmmlkkjjiihhggffeedcba") == "abcdeeffgghhiijjkklmmnnoopppqqqrssstttuuuvvvwwwwxxxyyyzzz"
    assert candidate(s = "caabdbac") == "aaabcdbc"
    assert candidate(s = "aaaabbbbccccddddeeeeffff") == "aaaabbbbccccddddeeeeffff"
    assert candidate(s = "fedcba") == "abcdef"
    assert candidate(s = "abcdabcabc") == "aaabcbcdcb"
    assert candidate(s = "leetcode") == "cdeoteel"
    assert candidate(s = "racecar") == "aacecrr"
    assert candidate(s = "zzzyyxxwvwuvuttrssrqqponnmlkkjjiihhhggffeeddcbbbaaa") == "aaabbbcddeeffgghhhiijjkklmnnopqqrssrttuvuwvwxxyyzzz"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == "aabcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcb"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == "aaaabcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcbzyxwvutsrqponmlkjihgfedcbzyxwvutsrqponmlkjihgfedcbz"
    assert candidate(s = "banana") == "aaannb"
    assert candidate(s = "abcdeabcde") == "aabcdedcbe"
    assert candidate(s = "mississippi") == "iiiippssssm"
    assert candidate(s = "acacacacac") == "aaaaaccccc"
    assert candidate(s = "abcdabcdbacd") == "aaabcdcbdcbd"
    assert candidate(s = "bbaaccdd") == "aabbccdd"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(s = "abcdabcdabcdabcd") == "aaaabcdcbdcbdcbd"
    assert candidate(s = "aaabbbcccddd") == "aaabbbcccddd"
    assert candidate(s = "qrsnspndpsnpppdnspndpdpsnsnspdpspndpdpsnpsdpsnpspdpsndpdpsnpdpsnpsdpsnpd") == "ddddddddddddddpnspspnsppnsppnsppspnspspnsppnpsppsnsnsppnpsnpppnspnpsnsrq"
    assert candidate(s = "abababababababababababababab") == "aaaaaaaaaaaaaabbbbbbbbbbbbbb"
    assert candidate(s = "xyzzyxzyx") == "xxxyzyzzy"


