def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "dsahjpjauf",words = ['ahjpjau', 'ja', 'ahbwzgqnuk', 'tnmlanowax']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "dsahjpjauf",words = ['ahjpjau', 'ja', 'ahbwzgqnuk', 'tnmlanowax']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",words = ['a', 'bb', 'acd', 'ace']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",words = ['a', 'bb', 'acd', 'ace']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",words = ['qz', 'qp', 'qw', 'qr', 'qe', 'qt', 'qu', 'qi', 'qo', 'qp', 'qa', 'qs', 'qd', 'qf', 'qg', 'qh', 'qj', 'qk', 'ql', 'qm', 'zn', 'zm', 'zk', 'zj', 'zh', 'zg', 'zf', 'qe', 'qd', 'qc', 'qb', 'qa', 'zv', 'zu', 'zt', 'zs', 'zr', 'zp', 'zo', 'zn', 'zm', 'zk', 'zj', 'zh', 'zg', 'zf', 'ze', 'zd', 'zc', 'zb', 'za']) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",words = ['qz', 'qp', 'qw', 'qr', 'qe', 'qt', 'qu', 'qi', 'qo', 'qp', 'qa', 'qs', 'qd', 'qf', 'qg', 'qh', 'qj', 'qk', 'ql', 'qm', 'zn', 'zm', 'zk', 'zj', 'zh', 'zg', 'zf', 'qe', 'qd', 'qc', 'qb', 'qa', 'zv', 'zu', 'zt', 'zs', 'zr', 'zp', 'zo', 'zn', 'zm', 'zk', 'zj', 'zh', 'zg', 'zf', 'ze', 'zd', 'zc', 'zb', 'za']) == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",words = ['miss', 'issi', 'ssip', 'ppis', 'isip', 'ippi', 'sipi', 'sspi', 'issp']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",words = ['miss', 'issi', 'ssip', 'ppis', 'isip', 'ippi', 'sipi', 'sspi', 'issp']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "longstringwithvariouscharacters",words = ['long', 'string', 'with', 'various', 'characters', 'longstring', 'withvarious']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longstringwithvariouscharacters",words = ['long', 'string', 'with', 'various', 'characters', 'longstring', 'withvarious']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbcccc",words = ['aaabbb', 'bbcc', 'abac', 'aabb', 'accc', 'bbbc', 'cccc', 'bbbb', 'aabbcc']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbcccc",words = ['aaabbb', 'bbcc', 'abac', 'aabb', 'accc', 'bbbc', 'cccc', 'bbbb', 'aabbcc']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",words = ['aba', 'abc', 'bac', 'bca', 'cab', 'acb', 'a', 'b', 'c', 'd', 'ab', 'ba', 'bc', 'cb', 'ac', 'ca']) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",words = ['aba', 'abc', 'bac', 'bca', 'cab', 'acb', 'a', 'b', 'c', 'd', 'ab', 'ba', 'bc', 'cb', 'ac', 'ca']) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",words = ['is', 'issi', 'miss', 'issip', 'ppi', 'ipi', 'mississippi']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",words = ['is', 'issi', 'miss', 'issip', 'ppi', 'ipi', 'mississippi']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "thefastbrownfoxjumpsoverthelazydog",words = ['the', 'fast', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog', 'thebrownfox', 'jumpsoverthelazy']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thefastbrownfoxjumpsoverthelazydog",words = ['the', 'fast', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog', 'thebrownfox', 'jumpsoverthelazy']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'xyz', 'mnopqr', 'uvw', 'zabcdefghijklmnopqrst']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'xyz', 'mnopqr', 'uvw', 'zabcdefghijklmnopqrst']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",words = ['qwerty', 'asdfgh', 'zxcvbn', 'pol', 'lkjhg', 'mnbvcxz', 'yuiop', 'poiuyt', 'hgfdsa', 'xcvbnm', 'qwertyuiop', 'asdfghjklzxcvbnm']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",words = ['qwerty', 'asdfgh', 'zxcvbn', 'pol', 'lkjhg', 'mnbvcxz', 'yuiop', 'poiuyt', 'hgfdsa', 'xcvbnm', 'qwertyuiop', 'asdfghjklzxcvbnm']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",words = ['miss', 'issi', 'ssip', 'ssissipp', 'is', 'mp', 'ms', 's', 'i', 'p', 'pp', 'ip', 'mississippi', 'mississ', 'issipp']) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",words = ['miss', 'issi', 'ssip', 'ssissipp', 'is', 'mp', 'ms', 's', 'i', 'p', 'pp', 'ip', 'mississippi', 'mississ', 'issipp']) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'aaa', 'bbb', 'ccc']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'aaa', 'bbb', 'ccc']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yzab', 'cdef', 'ghij', 'klmn', 'opqr', 'stuv', 'wxyz']) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yzab', 'cdef', 'ghij', 'klmn', 'opqr', 'stuv', 'wxyz']) == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",words = ['abc', 'abcabc', 'abcabcabc', 'abcabcabcabc', 'ab', 'bc', 'ca', 'a', 'b', 'c']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",words = ['abc', 'abcabc', 'abcabcabc', 'abcabcabcabc', 'ab', 'bc', 'ca', 'a', 'b', 'c']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab",words = ['ab', 'aba', 'aab', 'baba', 'babababababab']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab",words = ['ab', 'aba', 'aab', 'baba', 'babababababab']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",words = ['issi', 'miss', 'mip', 'issip', 'issipp', 'mpis', 'mississippi']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",words = ['issi', 'miss', 'mip', 'issip', 'issipp', 'mpis', 'mississippi']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongandrandomstring",words = ['this', 'is', 'very', 'long', 'and', 'random', 'string', 'av', 'er', 'ry', 'on', 'nd', 'ra', 'nd', 'om', 'mi', 'st', 'in', 'ng']) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongandrandomstring",words = ['this', 'is', 'very', 'long', 'and', 'random', 'string', 'av', 'er', 'ry', 'on', 'nd', 'ra', 'nd', 'om', 'mi', 'st', 'in', 'ng']) == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "repeatedcharacters",words = ['repe', 'peate', 'atedchar', 'char', 'acter', 'ters', 'repeatedcharacters']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeatedcharacters",words = ['repe', 'peate', 'atedchar', 'char', 'acter', 'ters', 'repeatedcharacters']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",words = ['abc', 'cab', 'bac', 'aaa', 'bbb', 'ccc', 'abcabc', 'abcbca', 'bcbcab', 'cabcab', 'abcabcabc', 'bcabcabc', 'cabcabca', 'a', 'b', 'c']) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",words = ['abc', 'cab', 'bac', 'aaa', 'bbb', 'ccc', 'abcabc', 'abcbca', 'bcbcab', 'cabcab', 'abcabcabc', 'bcabcabc', 'cabcabca', 'a', 'b', 'c']) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "babcabcabcabcabc",words = ['ba', 'ca', 'ab', 'bc', 'ac', 'abc', 'bac', 'bca', 'cab', 'cba', 'acb', 'bba', 'aaa', 'ccc']) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babcabcabcabcabc",words = ['ba', 'ca', 'ab', 'bc', 'ac', 'abc', 'bac', 'bca', 'cab', 'cba', 'acb', 'bba', 'aaa', 'ccc']) == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'xyz', 'def', 'uvw', 'mnopqr', 'st', 'ghijkl']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'xyz', 'def', 'uvw', 'mnopqr', 'st', 'ghijkl']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohellohello",words = ['he', 'lo', 'ell', 'hell', 'hello', 'heell', 'hellohe', 'helloell', 'helloello', 'hellohello', 'hellohelloh', 'hellohellohe', 'hellohelloell', 'hellohelloello', 'hellohellohello']) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohellohello",words = ['he', 'lo', 'ell', 'hell', 'hello', 'heell', 'hellohe', 'helloell', 'helloello', 'hellohello', 'hellohelloh', 'hellohellohe', 'hellohelloell', 'hellohelloello', 'hellohellohello']) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra",words = ['abra', 'rac', 'cad', 'bra', 'dabra', 'abra', 'acad', 'bracad', 'bracadabra', 'bracadabr', 'abracadabr', 'bracadabraa', 'bracadabrac']) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra",words = ['abra', 'rac', 'cad', 'bra', 'dabra', 'abra', 'acad', 'bracad', 'bracadabra', 'bracadabr', 'abracadabr', 'bracadabraa', 'bracadabrac']) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",words = ['aba', 'abc', 'bac', 'bca', 'cab', 'cba']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",words = ['aba', 'abc', 'bac', 'bca', 'cab', 'cba']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz', 'zzzzzzzzzz']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz', 'zzzzzzzzzz']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",words = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",words = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']) == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra",words = ['abr', 'rac', 'aca', 'dab', 'bra', 'cad', 'bra', 'abra', 'brac', 'acad', 'radab', 'cabra', 'rabrac', 'acadabra', 'adabra', 'bracadabra', 'acabracadabra']) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra",words = ['abr', 'rac', 'aca', 'dab', 'bra', 'cad', 'bra', 'abra', 'brac', 'acad', 'radab', 'cabra', 'rabrac', 'acadabra', 'adabra', 'bracadabra', 'acabracadabra']) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['a', 'z', 'abc', 'xyz', 'abcdefghijklmnopqrstuvwxyzz']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['a', 'z', 'abc', 'xyz', 'abcdefghijklmnopqrstuvwxyzz']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz', 'zzzzzzzzzz']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz', 'zzzzzzzzzz']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'xyz', 'mnop', 'qrstuv', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'xyz', 'mnop', 'qrstuv', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababab",words = ['aa', 'ab', 'ba', 'bb', 'aab', 'aba', 'abb', 'bba', 'bab', 'bbb', 'aaaa', 'abab', 'baba', 'abba', 'baab', 'abaa', 'bbaa', 'aabb', 'abbb', 'baaa', 'baab', 'baaa', 'bbab', 'bbba', 'bbbb', 'aaaaaaaa', 'abababab', 'babababa', 'ababababa', 'babababab']) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababab",words = ['aa', 'ab', 'ba', 'bb', 'aab', 'aba', 'abb', 'bba', 'bab', 'bbb', 'aaaa', 'abab', 'baba', 'abba', 'baab', 'abaa', 'bbaa', 'aabb', 'abbb', 'baaa', 'baab', 'baaa', 'bbab', 'bbba', 'bbbb', 'aaaaaaaa', 'abababab', 'babababa', 'ababababa', 'babababab']) == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",words = ['miss', 'issi', 'ippi', 'ssss', 'ppii', 'mississi', 'issippi', 'mississippi', 'mpis', 'ppis', 'ipis', 'mipp', 'ssip', 'piss', 'missippi', 'missisipp', 'ississippi', 'ssissippi', 'ippii', 'sippi', 'pissi', 'issis', 'missis', 'ssssip', 'pisssippi', 'issippis', 'pississi', 'sissippii', 'ppisssippi', 'mississippipp', 'ississipp', 'ppississippi', 'sippisippi', 'issississi', 'ppississippi', 'mississippippi', 'issississipp', 'ppissississi', 'sissississippi', 'issississippippi']) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",words = ['miss', 'issi', 'ippi', 'ssss', 'ppii', 'mississi', 'issippi', 'mississippi', 'mpis', 'ppis', 'ipis', 'mipp', 'ssip', 'piss', 'missippi', 'missisipp', 'ississippi', 'ssissippi', 'ippii', 'sippi', 'pissi', 'issis', 'missis', 'ssssip', 'pisssippi', 'issippis', 'pississi', 'sissippii', 'ppisssippi', 'mississippipp', 'ississipp', 'ppississippi', 'sippisippi', 'issississi', 'ppississippi', 'mississippippi', 'issississipp', 'ppissississi', 'sissississippi', 'issississippippi']) == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzz']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzz']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz']) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz']) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcodeisacommunityforcoders",words = ['leetcode', 'is', 'acommunity', 'of', 'coders', 'comm', 's', 't']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcodeisacommunityforcoders",words = ['leetcode', 'is', 'acommunity', 'of', 'coders', 'comm', 's', 't']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababababababababababababab",words = ['aa', 'bb', 'ab', 'ba', 'aab', 'abb', 'bab', 'bba']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababababababababababababab",words = ['aa', 'bb', 'ab', 'ba', 'aab', 'abb', 'bab', 'bba']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaaaaabbbb",words = ['bb', 'aaaa', 'bbb', 'baab', 'abba', 'aaaaa', 'bbbbb', 'bababa', 'bbbbba', 'ababab', 'bbabba']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaaaaabbbb",words = ['bb', 'aaaa', 'bbb', 'baab', 'abba', 'aaaaa', 'bbbbb', 'bababa', 'bbbbba', 'ababab', 'bbabba']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaabbbbbbbbccccccccdddddddd",words = ['aaaa', 'bbbb', 'cccc', 'dddd', 'abdc', 'dcba', 'abcd', 'dcba', 'aabb', 'bbcc', 'ccdd', 'dddd', 'ac', 'bd', 'ca', 'db']) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaabbbbbbbbccccccccdddddddd",words = ['aaaa', 'bbbb', 'cccc', 'dddd', 'abdc', 'dcba', 'abcd', 'dcba', 'aabb', 'bbcc', 'ccdd', 'dddd', 'ac', 'bd', 'ca', 'db']) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",words = ['zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",words = ['zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",words = ['qaz', 'wsx', 'edc', 'rfv', 'tgb', 'yhn', 'ujm', 'ikl', 'opy', 'asdf', 'ghjkl', 'zxcvbnm', 'ertyui', 'poiuyt', 'lkjhgfdsa', 'nmolkjiuhgfedcba']) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",words = ['qaz', 'wsx', 'edc', 'rfv', 'tgb', 'yhn', 'ujm', 'ikl', 'opy', 'asdf', 'ghjkl', 'zxcvbnm', 'ertyui', 'poiuyt', 'lkjhgfdsa', 'nmolkjiuhgfedcba']) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",words = ['xyz', 'xy', 'yz', 'xz', 'xx', 'yy', 'zz', 'xzy', 'yzx', 'zxy', 'xyzxyz', 'xyxyxy', 'yzyzyz', 'xzxzxz', 'xxx', 'yyy', 'zzz', 'xzyxzyxzy', 'yzxyzxyz', 'zxzyzxzyz', 'xyzxyzxyzxyz']) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",words = ['xyz', 'xy', 'yz', 'xz', 'xx', 'yy', 'zz', 'xzy', 'yzx', 'zxy', 'xyzxyz', 'xyxyxy', 'yzyzyz', 'xzxzxz', 'xxx', 'yyy', 'zzz', 'xzyxzyxzy', 'yzxyzxyz', 'zxzyzxzyz', 'xyzxyzxyzxyz']) == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "lkjhgfdsapoiuytrewq",words = ['poi', 'uyt', 'rew', 'qwe', 'lkj', 'hgf', 'dsa', 'lkjh', 'gfds', 'poiu', 'uytr', 'trew', 'qwe', 'lkjhg', 'gfdsa', 'poiu', 'uytrw', 'trewq']) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lkjhgfdsapoiuytrewq",words = ['poi', 'uyt', 'rew', 'qwe', 'lkj', 'hgf', 'dsa', 'lkjh', 'gfds', 'poiu', 'uytr', 'trew', 'qwe', 'lkjhg', 'gfdsa', 'poiu', 'uytrw', 'trewq']) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",words = ['aba', 'abc', 'aca', 'ada', 'baa', 'bac', 'bda', 'cab', 'cad', 'cda', 'daa', 'dac', 'dba']) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",words = ['aba', 'abc', 'aca', 'ada', 'baa', 'bac', 'bda', 'cab', 'cad', 'cda', 'daa', 'dac', 'dba']) == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'mnop', 'xyz', 'qrstuv', 'wxyz', 'defghijkl', 'nopqrstuv']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'mnop', 'xyz', 'qrstuv', 'wxyz', 'defghijkl', 'nopqrstuv']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaa",words = ['aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaa",words = ['aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababab",words = ['aba', 'bab', 'aaa', 'bbb', 'aab', 'aba', 'aabbaa', 'bbbabb', 'ab', 'ba', 'aa', 'bb', 'abab', 'baba', 'ababa', 'babab', 'ababab', 'bababa']) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababab",words = ['aba', 'bab', 'aaa', 'bbb', 'aab', 'aba', 'aabbaa', 'bbbabb', 'ab', 'ba', 'aa', 'bb', 'abab', 'baba', 'ababa', 'babab', 'ababab', 'bababa']) == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbabbbbaabaaabaababbbbbbaaabbbabbababbababba",words = ['bb', 'ba', 'bbba', 'bab', 'bbab', 'aa', 'aaa', 'aaaa', 'aaaaa', 'a', 'b', 'ab', 'ba', 'aba', 'bab', 'bba', 'abb', 'aab', 'bbb', 'bbbba']) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbabbbbaabaaabaababbbbbbaaabbbabbababbababba",words = ['bb', 'ba', 'bbba', 'bab', 'bbab', 'aa', 'aaa', 'aaaa', 'aaaaa', 'a', 'b', 'ab', 'ba', 'aba', 'bab', 'bba', 'abb', 'aab', 'bbb', 'bbbba']) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithseveralrepetitions",words = ['this', 'is', 'a', 'very', 'long', 'string', 'with', 'several', 'repetitions', 'verylong', 'stringwith', 'longstring', 'thisisavery', 'averylongstring', 'thisisaverylongstringwithseveralrepetitions']) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithseveralrepetitions",words = ['this', 'is', 'a', 'very', 'long', 'string', 'with', 'several', 'repetitions', 'verylong', 'stringwith', 'longstring', 'thisisavery', 'averylongstring', 'thisisaverylongstringwithseveralrepetitions']) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'xyz', 'abcd', 'uvw', 'wxyz', 'mnopqr', 'def', 'ghi', 'jkl', 'stu']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'xyz', 'abcd', 'uvw', 'wxyz', 'mnopqr', 'def', 'ghi', 'jkl', 'stu']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",words = ['zyx', 'wvut', 'srqp', 'onml', 'kjih', 'gfed', 'cba', 'abc']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",words = ['zyx', 'wvut', 'srqp', 'onml', 'kjih', 'gfed', 'cba', 'abc']) == 7: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "dsahjpjauf",words = ['ahjpjau', 'ja', 'ahbwzgqnuk', 'tnmlanowax']) == 2
    assert candidate(s = "abcde",words = ['a', 'bb', 'acd', 'ace']) == 3
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",words = ['qz', 'qp', 'qw', 'qr', 'qe', 'qt', 'qu', 'qi', 'qo', 'qp', 'qa', 'qs', 'qd', 'qf', 'qg', 'qh', 'qj', 'qk', 'ql', 'qm', 'zn', 'zm', 'zk', 'zj', 'zh', 'zg', 'zf', 'qe', 'qd', 'qc', 'qb', 'qa', 'zv', 'zu', 'zt', 'zs', 'zr', 'zp', 'zo', 'zn', 'zm', 'zk', 'zj', 'zh', 'zg', 'zf', 'ze', 'zd', 'zc', 'zb', 'za']) == 32
    assert candidate(s = "mississippi",words = ['miss', 'issi', 'ssip', 'ppis', 'isip', 'ippi', 'sipi', 'sspi', 'issp']) == 8
    assert candidate(s = "longstringwithvariouscharacters",words = ['long', 'string', 'with', 'various', 'characters', 'longstring', 'withvarious']) == 7
    assert candidate(s = "aaaaabbbbbcccc",words = ['aaabbb', 'bbcc', 'abac', 'aabb', 'accc', 'bbbc', 'cccc', 'bbbb', 'aabbcc']) == 8
    assert candidate(s = "abacabadabacaba",words = ['aba', 'abc', 'bac', 'bca', 'cab', 'acb', 'a', 'b', 'c', 'd', 'ab', 'ba', 'bc', 'cb', 'ac', 'ca']) == 16
    assert candidate(s = "aaaaaaaaaaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == 10
    assert candidate(s = "mississippi",words = ['is', 'issi', 'miss', 'issip', 'ppi', 'ipi', 'mississippi']) == 7
    assert candidate(s = "thefastbrownfoxjumpsoverthelazydog",words = ['the', 'fast', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog', 'thebrownfox', 'jumpsoverthelazy']) == 10
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'xyz', 'mnopqr', 'uvw', 'zabcdefghijklmnopqrst']) == 4
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",words = ['qwerty', 'asdfgh', 'zxcvbn', 'pol', 'lkjhg', 'mnbvcxz', 'yuiop', 'poiuyt', 'hgfdsa', 'xcvbnm', 'qwertyuiop', 'asdfghjklzxcvbnm']) == 7
    assert candidate(s = "mississippi",words = ['miss', 'issi', 'ssip', 'ssissipp', 'is', 'mp', 'ms', 's', 'i', 'p', 'pp', 'ip', 'mississippi', 'mississ', 'issipp']) == 15
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'aaa', 'bbb', 'ccc']) == 9
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yzab', 'cdef', 'ghij', 'klmn', 'opqr', 'stuv', 'wxyz']) == 21
    assert candidate(s = "abcabcabcabc",words = ['abc', 'abcabc', 'abcabcabc', 'abcabcabcabc', 'ab', 'bc', 'ca', 'a', 'b', 'c']) == 10
    assert candidate(s = "ababababab",words = ['ab', 'aba', 'aab', 'baba', 'babababababab']) == 4
    assert candidate(s = "mississippi",words = ['issi', 'miss', 'mip', 'issip', 'issipp', 'mpis', 'mississippi']) == 6
    assert candidate(s = "thisisaverylongandrandomstring",words = ['this', 'is', 'very', 'long', 'and', 'random', 'string', 'av', 'er', 'ry', 'on', 'nd', 'ra', 'nd', 'om', 'mi', 'st', 'in', 'ng']) == 19
    assert candidate(s = "repeatedcharacters",words = ['repe', 'peate', 'atedchar', 'char', 'acter', 'ters', 'repeatedcharacters']) == 7
    assert candidate(s = "abcabcabcabc",words = ['abc', 'cab', 'bac', 'aaa', 'bbb', 'ccc', 'abcabc', 'abcbca', 'bcbcab', 'cabcab', 'abcabcabc', 'bcabcabc', 'cabcabca', 'a', 'b', 'c']) == 16
    assert candidate(s = "babcabcabcabcabc",words = ['ba', 'ca', 'ab', 'bc', 'ac', 'abc', 'bac', 'bca', 'cab', 'cba', 'acb', 'bba', 'aaa', 'ccc']) == 14
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'xyz', 'def', 'uvw', 'mnopqr', 'st', 'ghijkl']) == 7
    assert candidate(s = "hellohellohellohello",words = ['he', 'lo', 'ell', 'hell', 'hello', 'heell', 'hellohe', 'helloell', 'helloello', 'hellohello', 'hellohelloh', 'hellohellohe', 'hellohelloell', 'hellohelloello', 'hellohellohello']) == 15
    assert candidate(s = "abracadabra",words = ['abra', 'rac', 'cad', 'bra', 'dabra', 'abra', 'acad', 'bracad', 'bracadabra', 'bracadabr', 'abracadabr', 'bracadabraa', 'bracadabrac']) == 11
    assert candidate(s = "aaaaaaaaaaaaaaaaaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == 10
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']) == 9
    assert candidate(s = "abacabadabacaba",words = ['aba', 'abc', 'bac', 'bca', 'cab', 'cba']) == 6
    assert candidate(s = "zzzzzzzzzz",words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz', 'zzzzzzzzzz']) == 10
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",words = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']) == 26
    assert candidate(s = "abracadabra",words = ['abr', 'rac', 'aca', 'dab', 'bra', 'cad', 'bra', 'abra', 'brac', 'acad', 'radab', 'cabra', 'rabrac', 'acadabra', 'adabra', 'bracadabra', 'acabracadabra']) == 15
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['a', 'z', 'abc', 'xyz', 'abcdefghijklmnopqrstuvwxyzz']) == 4
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz', 'zzzzzzzzzz']) == 10
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'xyz', 'mnop', 'qrstuv', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == 31
    assert candidate(s = "ababababababababababababababababababababababab",words = ['aa', 'ab', 'ba', 'bb', 'aab', 'aba', 'abb', 'bba', 'bab', 'bbb', 'aaaa', 'abab', 'baba', 'abba', 'baab', 'abaa', 'bbaa', 'aabb', 'abbb', 'baaa', 'baab', 'baaa', 'bbab', 'bbba', 'bbbb', 'aaaaaaaa', 'abababab', 'babababa', 'ababababa', 'babababab']) == 30
    assert candidate(s = "mississippi",words = ['miss', 'issi', 'ippi', 'ssss', 'ppii', 'mississi', 'issippi', 'mississippi', 'mpis', 'ppis', 'ipis', 'mipp', 'ssip', 'piss', 'missippi', 'missisipp', 'ississippi', 'ssissippi', 'ippii', 'sippi', 'pissi', 'issis', 'missis', 'ssssip', 'pisssippi', 'issippis', 'pississi', 'sissippii', 'ppisssippi', 'mississippipp', 'ississipp', 'ppississippi', 'sippisippi', 'issississi', 'ppississippi', 'mississippippi', 'issississipp', 'ppissississi', 'sissississippi', 'issississippippi']) == 18
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzz']) == 5
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz']) == 12
    assert candidate(s = "leetcodeisacommunityforcoders",words = ['leetcode', 'is', 'acommunity', 'of', 'coders', 'comm', 's', 't']) == 8
    assert candidate(s = "abababababababababababababababababababababababababab",words = ['aa', 'bb', 'ab', 'ba', 'aab', 'abb', 'bab', 'bba']) == 8
    assert candidate(s = "bbaaaaabbbb",words = ['bb', 'aaaa', 'bbb', 'baab', 'abba', 'aaaaa', 'bbbbb', 'bababa', 'bbbbba', 'ababab', 'bbabba']) == 6
    assert candidate(s = "aaaaaaaabbbbbbbbccccccccdddddddd",words = ['aaaa', 'bbbb', 'cccc', 'dddd', 'abdc', 'dcba', 'abcd', 'dcba', 'aabb', 'bbcc', 'ccdd', 'dddd', 'ac', 'bd', 'ca', 'db']) == 11
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",words = ['zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz']) == 5
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",words = ['qaz', 'wsx', 'edc', 'rfv', 'tgb', 'yhn', 'ujm', 'ikl', 'opy', 'asdf', 'ghjkl', 'zxcvbnm', 'ertyui', 'poiuyt', 'lkjhgfdsa', 'nmolkjiuhgfedcba']) == 12
    assert candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",words = ['xyz', 'xy', 'yz', 'xz', 'xx', 'yy', 'zz', 'xzy', 'yzx', 'zxy', 'xyzxyz', 'xyxyxy', 'yzyzyz', 'xzxzxz', 'xxx', 'yyy', 'zzz', 'xzyxzyxzy', 'yzxyzxyz', 'zxzyzxzyz', 'xyzxyzxyzxyz']) == 21
    assert candidate(s = "aaaaaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == 6
    assert candidate(s = "lkjhgfdsapoiuytrewq",words = ['poi', 'uyt', 'rew', 'qwe', 'lkj', 'hgf', 'dsa', 'lkjh', 'gfds', 'poiu', 'uytr', 'trew', 'qwe', 'lkjhg', 'gfdsa', 'poiu', 'uytrw', 'trewq']) == 16
    assert candidate(s = "abacabadabacaba",words = ['aba', 'abc', 'aca', 'ada', 'baa', 'bac', 'bda', 'cab', 'cad', 'cda', 'daa', 'dac', 'dba']) == 13
    assert candidate(s = "aaaaaaaaaaaaaaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == 10
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'mnop', 'xyz', 'qrstuv', 'wxyz', 'defghijkl', 'nopqrstuv']) == 7
    assert candidate(s = "aaaaaaaaaaaaaaa",words = ['aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == 9
    assert candidate(s = "abababababababababababab",words = ['aba', 'bab', 'aaa', 'bbb', 'aab', 'aba', 'aabbaa', 'bbbabb', 'ab', 'ba', 'aa', 'bb', 'abab', 'baba', 'ababa', 'babab', 'ababab', 'bababa']) == 18
    assert candidate(s = "bcbabbbbaabaaabaababbbbbbaaabbbabbababbababba",words = ['bb', 'ba', 'bbba', 'bab', 'bbab', 'aa', 'aaa', 'aaaa', 'aaaaa', 'a', 'b', 'ab', 'ba', 'aba', 'bab', 'bba', 'abb', 'aab', 'bbb', 'bbbba']) == 20
    assert candidate(s = "thisisaverylongstringwithseveralrepetitions",words = ['this', 'is', 'a', 'very', 'long', 'string', 'with', 'several', 'repetitions', 'verylong', 'stringwith', 'longstring', 'thisisavery', 'averylongstring', 'thisisaverylongstringwithseveralrepetitions']) == 15
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'xyz', 'abcd', 'uvw', 'wxyz', 'mnopqr', 'def', 'ghi', 'jkl', 'stu']) == 10
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",words = ['zyx', 'wvut', 'srqp', 'onml', 'kjih', 'gfed', 'cba', 'abc']) == 7


