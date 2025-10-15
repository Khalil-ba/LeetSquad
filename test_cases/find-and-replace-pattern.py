def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world', 'leetcode'],pattern = "aaaaa") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world', 'leetcode'],pattern = "aaaaa") == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'deq', 'mee', 'aqq', 'dkd', 'ccc'],pattern = "abb") == ['mee', 'aqq']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'deq', 'mee', 'aqq', 'dkd', 'ccc'],pattern = "abb") == ['mee', 'aqq']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abb', 'abb', 'abb'],pattern = "abc") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abb', 'abb', 'abb'],pattern = "abc") == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abb', 'abc', 'abz', 'xyz', 'xyy'],pattern = "abb") == ['abb', 'xyy']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abb', 'abc', 'abz', 'xyz', 'xyy'],pattern = "abb") == ['abb', 'xyy']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'bbb', 'ccc'],pattern = "aaa") == ['aaa', 'bbb', 'ccc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'bbb', 'ccc'],pattern = "aaa") == ['aaa', 'bbb', 'ccc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c'],pattern = "a") == ['a', 'b', 'c']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c'],pattern = "a") == ['a', 'b', 'c']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world', 'abcde', 'uvwxy'],pattern = "abcde") == ['world', 'abcde', 'uvwxy']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world', 'abcde', 'uvwxy'],pattern = "abcde") == ['world', 'abcde', 'uvwxy']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abb', 'abb', 'abb', 'abb'],pattern = "abc") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abb', 'abb', 'abb', 'abb'],pattern = "abc") == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abb', 'abc', 'aab'],pattern = "abb") == ['abb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abb', 'abc', 'aab'],pattern = "abb") == ['abb']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aba', 'bcb', 'bab'],pattern = "aba") == ['aba', 'bcb', 'bab']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aba', 'bcb', 'bab'],pattern = "aba") == ['aba', 'bcb', 'bab']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abb', 'abc', 'aab', 'aba'],pattern = "abb") == ['abb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abb', 'abc', 'aab', 'aba'],pattern = "abb") == ['abb']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abb', 'abc', 'xyz', 'xyy'],pattern = "abb") == ['abb', 'xyy']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abb', 'abc', 'xyz', 'xyy'],pattern = "abb") == ['abb', 'xyy']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abb', 'aaa', 'aab'],pattern = "abb") == ['abb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abb', 'aaa', 'aab'],pattern = "abb") == ['abb']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abba', 'abab', 'baab', 'baba', 'aaaa'],pattern = "aabb") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abba', 'abab', 'baab', 'baba', 'aaaa'],pattern = "aabb") == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abac', 'bcad', 'aacc', 'bbdd', 'aabb'],pattern = "abab") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abac', 'bcad', 'aacc', 'bbdd', 'aabb'],pattern = "abab") == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefg', 'hijklmn', 'opqrstu', 'vwxyzab', 'cdefghi'],pattern = "abcdefg") == ['abcdefg', 'hijklmn', 'opqrstu', 'vwxyzab', 'cdefghi']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefg', 'hijklmn', 'opqrstu', 'vwxyzab', 'cdefghi'],pattern = "abcdefg") == ['abcdefg', 'hijklmn', 'opqrstu', 'vwxyzab', 'cdefghi']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcabc', 'bcbcbc', 'dedede', 'aiaiai', 'jkjkjk'],pattern = "abcabc") == ['abcabc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcabc', 'bcbcbc', 'dedede', 'aiaiai', 'jkjkjk'],pattern = "abcabc") == ['abcabc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'bcdef', 'cdefg', 'defgh', 'efghi'],pattern = "abcde") == ['abcde', 'bcdef', 'cdefg', 'defgh', 'efghi']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'bcdef', 'cdefg', 'defgh', 'efghi'],pattern = "abcde") == ['abcde', 'bcdef', 'cdefg', 'defgh', 'efghi']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zyx', 'yxz', 'xyz', 'zyz', 'yzy', 'zzy', 'zzz', 'zzz'],pattern = "zyx") == ['zyx', 'yxz', 'xyz']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zyx', 'yxz', 'xyz', 'zyz', 'yzy', 'zzy', 'zzz', 'zzz'],pattern = "zyx") == ['zyx', 'yxz', 'xyz']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyx', 'yxy', 'xyz', 'zyz'],pattern = "aba") == ['xyx', 'yxy', 'zyz']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyx', 'yxy', 'xyz', 'zyz'],pattern = "aba") == ['xyx', 'yxy', 'zyz']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'bcdea', 'cdeab', 'deabc', 'eabcd'],pattern = "abcde") == ['abcde', 'bcdea', 'cdeab', 'deabc', 'eabcd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'bcdea', 'cdeab', 'deabc', 'eabcd'],pattern = "abcde") == ['abcde', 'bcdea', 'cdeab', 'deabc', 'eabcd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'efgh', 'ijkl'],pattern = "abcd") == ['abcd', 'efgh', 'ijkl']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'efgh', 'ijkl'],pattern = "abcd") == ['abcd', 'efgh', 'ijkl']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaaabbbbbcccccdddddeeeeeffffffggggghhhhhhiiiiijjjjjkkkkklllllmmmmmnnnnnooooo', 'zzzzzyyyyyxxxxxwwwwwvvvvvtttttsssssrrrrrqqqqqppppoonnnnnmmmmmlllllkkkkkjjjjjiiiii', 'tttttsssssrrrrrqqqqqppppponnnnnmmmmmlllllkkkkkjjjjjiiiiihhhhhhgggggffffffeeeeedddddeeecccbbbaaaaa'],pattern = "tttttsssssrrrrrqqqqqppppponnnnnmmmmmlllllkkkkkjjjjjiiiiihhhhhhgggggffffffeeeeedddddeeecccbbbaaaaa") == ['tttttsssssrrrrrqqqqqppppponnnnnmmmmmlllllkkkkkjjjjjiiiiihhhhhhgggggffffffeeeeedddddeeecccbbbaaaaa']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaaabbbbbcccccdddddeeeeeffffffggggghhhhhhiiiiijjjjjkkkkklllllmmmmmnnnnnooooo', 'zzzzzyyyyyxxxxxwwwwwvvvvvtttttsssssrrrrrqqqqqppppoonnnnnmmmmmlllllkkkkkjjjjjiiiii', 'tttttsssssrrrrrqqqqqppppponnnnnmmmmmlllllkkkkkjjjjjiiiiihhhhhhgggggffffffeeeeedddddeeecccbbbaaaaa'],pattern = "tttttsssssrrrrrqqqqqppppponnnnnmmmmmlllllkkkkkjjjjjiiiiihhhhhhgggggffffffeeeeedddddeeecccbbbaaaaa") == ['tttttsssssrrrrrqqqqqppppponnnnnmmmmmlllllkkkkkjjjjjiiiiihhhhhhgggggffffffeeeeedddddeeecccbbbaaaaa']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcc', 'abbc', 'abcb', 'acbb', 'adbb'],pattern = "abbc") == ['abbc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcc', 'abbc', 'abcb', 'acbb', 'adbb'],pattern = "abbc") == ['abbc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyx', 'yxy', 'xyy', 'yyy', 'xyxy'],pattern = "xxyx") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyx', 'yxy', 'xyy', 'yyy', 'xyxy'],pattern = "xxyx") == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'dcba', 'abab', 'dcdc', 'aabb'],pattern = "abcd") == ['abcd', 'dcba']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'dcba', 'abab', 'dcdc', 'aabb'],pattern = "abcd") == ['abcd', 'dcba']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'ddeeff', 'gghhii', 'jjkkll', 'mmnnoo'],pattern = "aabbcc") == ['aabbcc', 'ddeeff', 'gghhii', 'jjkkll', 'mmnnoo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'ddeeff', 'gghhii', 'jjkkll', 'mmnnoo'],pattern = "aabbcc") == ['aabbcc', 'ddeeff', 'gghhii', 'jjkkll', 'mmnnoo']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzzz', 'zzzz', 'zzzz', 'zzzz'],pattern = "aaaa") == ['zzzz', 'zzzz', 'zzzz', 'zzzz']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzzz', 'zzzz', 'zzzz', 'zzzz'],pattern = "aaaa") == ['zzzz', 'zzzz', 'zzzz', 'zzzz']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abbc', 'deee', 'zzzz'],pattern = "aabb") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abbc', 'deee', 'zzzz'],pattern = "aabb") == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'bcdea', 'cdeab', 'deabc', 'eabcd', 'fghij'],pattern = "abcde") == ['abcde', 'bcdea', 'cdeab', 'deabc', 'eabcd', 'fghij']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'bcdea', 'cdeab', 'deabc', 'eabcd', 'fghij'],pattern = "abcde") == ['abcde', 'bcdea', 'cdeab', 'deabc', 'eabcd', 'fghij']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdef', 'fedcba', 'ghijkl', 'lkjihg', 'mnopqr', 'rqponm'],pattern = "abcdef") == ['abcdef', 'fedcba', 'ghijkl', 'lkjihg', 'mnopqr', 'rqponm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdef', 'fedcba', 'ghijkl', 'lkjihg', 'mnopqr', 'rqponm'],pattern = "abcdef") == ['abcdef', 'fedcba', 'ghijkl', 'lkjihg', 'mnopqr', 'rqponm']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ijkl', 'ikjl', 'ijlk', 'ijlk', 'ikjl'],pattern = "ijkl") == ['ijkl', 'ikjl', 'ijlk', 'ijlk', 'ikjl']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ijkl', 'ikjl', 'ijlk', 'ijlk', 'ikjl'],pattern = "ijkl") == ['ijkl', 'ikjl', 'ijlk', 'ijlk', 'ikjl']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mnop', 'qrst', 'uvwx'],pattern = "mnop") == ['mnop', 'qrst', 'uvwx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mnop', 'qrst', 'uvwx'],pattern = "mnop") == ['mnop', 'qrst', 'uvwx']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyzx', 'yzxy', 'zxyx', 'yxzy', 'xzyz', 'zyzx', 'yzyz', 'zyzy'],pattern = "abcb") == ['zxyx', 'xzyz']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyzx', 'yzxy', 'zxyx', 'yxzy', 'xzyz', 'zyzx', 'yzyz', 'zyzy'],pattern = "abcb") == ['zxyx', 'xzyz']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mnop', 'mnop', 'mnop', 'mnop', 'mnop', 'mnop', 'mnop', 'mnop'],pattern = "mnop") == ['mnop', 'mnop', 'mnop', 'mnop', 'mnop', 'mnop', 'mnop', 'mnop']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mnop', 'mnop', 'mnop', 'mnop', 'mnop', 'mnop', 'mnop', 'mnop'],pattern = "mnop") == ['mnop', 'mnop', 'mnop', 'mnop', 'mnop', 'mnop', 'mnop', 'mnop']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['tttt', 'tqtq', 'ttqt', 'qtqt', 'qtqq'],pattern = "aaaa") == ['tttt']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['tttt', 'tqtq', 'ttqt', 'qtqt', 'qtqq'],pattern = "aaaa") == ['tttt']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyy', 'yxx', 'xyz', 'xyx', 'xxy'],pattern = "aba") == ['xyx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyy', 'yxx', 'xyz', 'xyx', 'xxy'],pattern = "aba") == ['xyx']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['qrst', 'qstr', 'qrts', 'qtsr', 'qtpr', 'qrsp'],pattern = "qrst") == ['qrst', 'qstr', 'qrts', 'qtsr', 'qtpr', 'qrsp']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['qrst', 'qstr', 'qrts', 'qtsr', 'qtpr', 'qrsp'],pattern = "qrst") == ['qrst', 'qstr', 'qrts', 'qtsr', 'qtpr', 'qrsp']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyzy', 'zyxy', 'yzyx', 'zyxz'],pattern = "xyzy") == ['xyzy', 'zyxy']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyzy', 'zyxy', 'yzyx', 'zyxz'],pattern = "xyzy") == ['xyzy', 'zyxy']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mnop', 'qrst', 'uvwx', 'yzxy', 'qrst'],pattern = "abcd") == ['mnop', 'qrst', 'uvwx', 'qrst']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mnop', 'qrst', 'uvwx', 'yzxy', 'qrst'],pattern = "abcd") == ['mnop', 'qrst', 'uvwx', 'qrst']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['qrst', 'rstq', 'stqr', 'tqrs', 'qrst', 'rstq', 'stqr', 'tqrs'],pattern = "abcd") == ['qrst', 'rstq', 'stqr', 'tqrs', 'qrst', 'rstq', 'stqr', 'tqrs']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['qrst', 'rstq', 'stqr', 'tqrs', 'qrst', 'rstq', 'stqr', 'tqrs'],pattern = "abcd") == ['qrst', 'rstq', 'stqr', 'tqrs', 'qrst', 'rstq', 'stqr', 'tqrs']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mnop', 'nopm', 'opmn', 'pqrs', 'qrst', 'stuv', 'tuvw', 'uvwx'],pattern = "mnop") == ['mnop', 'nopm', 'opmn', 'pqrs', 'qrst', 'stuv', 'tuvw', 'uvwx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mnop', 'nopm', 'opmn', 'pqrs', 'qrst', 'stuv', 'tuvw', 'uvwx'],pattern = "mnop") == ['mnop', 'nopm', 'opmn', 'pqrs', 'qrst', 'stuv', 'tuvw', 'uvwx']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xxy', 'xyy', 'yxx', 'yyx', 'xyx', 'yxy'],pattern = "xyy") == ['xyy', 'yxx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xxy', 'xyy', 'yxx', 'yyx', 'xyx', 'yxy'],pattern = "xyy") == ['xyy', 'yxx']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk'],pattern = "abc") == ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk'],pattern = "abc") == ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abacabadabacaba', 'babcbabcbbabcbb', 'abacabadabcadaa'],pattern = "abacabadabacaba") == ['abacabadabacaba']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abacabadabacaba', 'babcbabcbbabcbb', 'abacabadabcadaa'],pattern = "abacabadabacaba") == ['abacabadabacaba']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abbcc', 'aabbb', 'aabbcc', 'abbbaa', 'abacba', 'abcabc'],pattern = "abbcc") == ['abbcc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abbcc', 'aabbb', 'aabbcc', 'abbbaa', 'abacba', 'abcabc'],pattern = "abbcc") == ['abbcc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyyx', 'mnop', 'qrst'],pattern = "mnop") == ['mnop', 'qrst']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyyx', 'mnop', 'qrst'],pattern = "mnop") == ['mnop', 'qrst']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijkabcdefghijk'],pattern = "abcdefghijklmnopqrstuvwxyz") == ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijkabcdefghijk'],pattern = "abcdefghijklmnopqrstuvwxyz") == ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['deq', 'mee', 'aqq', 'dkd', 'ccc', 'eii', 'fff', 'ggh'],pattern = "abb") == ['mee', 'aqq', 'eii']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['deq', 'mee', 'aqq', 'dkd', 'ccc', 'eii', 'fff', 'ggh'],pattern = "abb") == ['mee', 'aqq', 'eii']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'vwxyz', 'pqrst'],pattern = "uvwxy") == ['abcde', 'vwxyz', 'pqrst']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'vwxyz', 'pqrst'],pattern = "uvwxy") == ['abcde', 'vwxyz', 'pqrst']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['qrst', 'uvwx', 'yzab'],pattern = "abcd") == ['qrst', 'uvwx', 'yzab']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['qrst', 'uvwx', 'yzab'],pattern = "abcd") == ['qrst', 'uvwx', 'yzab']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyx', 'yxy', 'zaz', 'azz', 'bzb', 'abb'],pattern = "aba") == ['xyx', 'yxy', 'zaz', 'bzb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyx', 'yxy', 'zaz', 'azz', 'bzb', 'abb'],pattern = "aba") == ['xyx', 'yxy', 'zaz', 'bzb']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xyy', 'xzy', 'yxy', 'yzy', 'zyx'],pattern = "xyz") == ['xyz', 'xzy', 'zyx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xyy', 'xzy', 'yxy', 'yzy', 'zyx'],pattern = "xyz") == ['xyz', 'xzy', 'zyx']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mnop', 'nmop', 'mnop', 'npom', 'mnop'],pattern = "abcd") == ['mnop', 'nmop', 'mnop', 'npom', 'mnop']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mnop', 'nmop', 'mnop', 'npom', 'mnop'],pattern = "abcd") == ['mnop', 'nmop', 'mnop', 'npom', 'mnop']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzabcf'],pattern = "abcdef") == ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzabcf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzabcf'],pattern = "abcdef") == ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzabcf']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mnop', 'nomp', 'mpon', 'mnop', 'mnoo', 'mmno'],pattern = "mnop") == ['mnop', 'nomp', 'mpon', 'mnop']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mnop', 'nomp', 'mpon', 'mnop', 'mnoo', 'mmno'],pattern = "mnop") == ['mnop', 'nomp', 'mpon', 'mnop']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abca', 'decd', 'mefm', 'aqqz', 'dkdf', 'ccca'],pattern = "abba") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abca', 'decd', 'mefm', 'aqqz', 'dkdf', 'ccca'],pattern = "abba") == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'bbccdd', 'ccddaa', 'ddeeff', 'eefggh'],pattern = "aabbcc") == ['aabbcc', 'bbccdd', 'ccddaa', 'ddeeff']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'bbccdd', 'ccddaa', 'ddeeff', 'eefggh'],pattern = "aabbcc") == ['aabbcc', 'bbccdd', 'ccddaa', 'ddeeff']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk'],pattern = "abcd") == ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk'],pattern = "abcd") == ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abba', 'abab', 'aabb', 'baba', 'baab', 'bbaa'],pattern = "abba") == ['abba', 'baab']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abba', 'abab', 'aabb', 'baba', 'baab', 'bbaa'],pattern = "abba") == ['abba', 'baab']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abacaba', 'cabadab', 'bacabac', 'adabaad', 'abaabab'],pattern = "abacaba") == ['abacaba']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abacaba', 'cabadab', 'bacabac', 'adabaad', 'abaabab'],pattern = "abacaba") == ['abacaba']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs'],pattern = "mnop") == ['ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs'],pattern = "mnop") == ['ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzzzz', 'yyyyy', 'xxxxx', 'wwwww', 'vvvvv'],pattern = "aaaaa") == ['zzzzz', 'yyyyy', 'xxxxx', 'wwwww', 'vvvvv']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzzzz', 'yyyyy', 'xxxxx', 'wwwww', 'vvvvv'],pattern = "aaaaa") == ['zzzzz', 'yyyyy', 'xxxxx', 'wwwww', 'vvvvv']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mnoonm', 'mnoono', 'mmnnoo', 'noonmm'],pattern = "mnoonm") == ['mnoonm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mnoonm', 'mnoono', 'mmnnoo', 'noonmm'],pattern = "mnoonm") == ['mnoonm']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyyx', 'mnop', 'qrst'],pattern = "abba") == ['xyyx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyyx', 'mnop', 'qrst'],pattern = "abba") == ['xyyx']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzz', 'aaa', 'zzz', 'aaa'],pattern = "abc") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzz', 'aaa', 'zzz', 'aaa'],pattern = "abc") == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'edcba', 'abcde', 'edcba'],pattern = "abcde") == ['abcde', 'edcba', 'abcde', 'edcba']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'edcba', 'abcde', 'edcba'],pattern = "abcde") == ['abcde', 'edcba', 'abcde', 'edcba']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abca', 'abcb', 'abcc', 'abdd'],pattern = "abba") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abca', 'abcb', 'abcc', 'abdd'],pattern = "abba") == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['baba', 'abab', 'aaaa', 'bbbb', 'abcd'],pattern = "abba") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['baba', 'abab', 'aaaa', 'bbbb', 'abcd'],pattern = "abba") == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abab', 'abac', 'aabb', 'abba', 'aaaa', 'bbbb', 'abac'],pattern = "abcd") == ['abcd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abab', 'abac', 'aabb', 'abba', 'aaaa', 'bbbb', 'abac'],pattern = "abcd") == ['abcd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcabcabcabcabcabcabcabc', 'bcbcbcbcbcbcbcbcbcbcbcbcbcbcb', 'cbbccbbccbbccbbccbbccbbccbbcc', 'abcbbccbbccbbccbbccbbccbbccbb'],pattern = "abcabcabcabcabcabcabcabc") == ['abcabcabcabcabcabcabcabc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcabcabcabcabcabcabcabc', 'bcbcbcbcbcbcbcbcbcbcbcbcbcbcb', 'cbbccbbccbbccbbccbbccbbccbbcc', 'abcbbccbbccbbccbbccbbccbbccbb'],pattern = "abcabcabcabcabcabcabcabc") == ['abcabcabcabcabcabcabcabc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abac', 'deed', 'zaff'],pattern = "deed") == ['deed']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abac', 'deed', 'zaff'],pattern = "deed") == ['deed']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefgh', 'hgfedcba', 'ijklmnop', 'ponmlkji', 'qrstuvwx', 'xwvutsrq'],pattern = "abcdefgh") == ['abcdefgh', 'hgfedcba', 'ijklmnop', 'ponmlkji', 'qrstuvwx', 'xwvutsrq']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefgh', 'hgfedcba', 'ijklmnop', 'ponmlkji', 'qrstuvwx', 'xwvutsrq'],pattern = "abcdefgh") == ['abcdefgh', 'hgfedcba', 'ijklmnop', 'ponmlkji', 'qrstuvwx', 'xwvutsrq']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'vwxyz', 'pqrst'],pattern = "vwxyz") == ['abcde', 'vwxyz', 'pqrst']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'vwxyz', 'pqrst'],pattern = "vwxyz") == ['abcde', 'vwxyz', 'pqrst']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abac', 'baba', 'abca', 'baac', 'caba', 'dada'],pattern = "abac") == ['abac']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abac', 'baba', 'abca', 'baac', 'caba', 'dada'],pattern = "abac") == ['abac']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['efgh', 'efgi', 'efgh', 'efgi', 'efgh'],pattern = "abcd") == ['efgh', 'efgi', 'efgh', 'efgi', 'efgh']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['efgh', 'efgi', 'efgh', 'efgi', 'efgh'],pattern = "abcd") == ['efgh', 'efgi', 'efgh', 'efgi', 'efgh']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ababab', 'bababa', 'cdcdcd', 'dcdcdc', 'efefef', 'fefefe'],pattern = "ababab") == ['ababab', 'bababa', 'cdcdcd', 'dcdcdc', 'efefef', 'fefefe']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ababab', 'bababa', 'cdcdcd', 'dcdcdc', 'efefef', 'fefefe'],pattern = "ababab") == ['ababab', 'bababa', 'cdcdcd', 'dcdcdc', 'efefef', 'fefefe']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abab', 'baba', 'abba', 'aaaa', 'bbbb', 'cccc', 'aabb', 'abab'],pattern = "abab") == ['abab', 'baba', 'abab']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abab', 'baba', 'abba', 'aaaa', 'bbbb', 'cccc', 'aabb', 'abab'],pattern = "abab") == ['abab', 'baba', 'abab']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abab', 'baba', 'abba', 'baab', 'aaaa', 'bbbb'],pattern = "abab") == ['abab', 'baba']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abab', 'baba', 'abba', 'baab', 'aaaa', 'bbbb'],pattern = "abab") == ['abab', 'baba']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'bbccdd', 'ccddaa', 'ddeeff', 'eeffgg', 'ffggee'],pattern = "abcdef") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'bbccdd', 'ccddaa', 'ddeeff', 'eeffgg', 'ffggee'],pattern = "abcdef") == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzzz', 'zzyz', 'zyzy', 'zyyz'],pattern = "aaaa") == ['zzzz']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzzz', 'zzyz', 'zyzy', 'zyyz'],pattern = "aaaa") == ['zzzz']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaaaa', 'bbbbbb', 'cccccc', 'dddddd', 'eeeeee', 'ffffff'],pattern = "aaaaaa") == ['aaaaaa', 'bbbbbb', 'cccccc', 'dddddd', 'eeeeee', 'ffffff']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaaaa', 'bbbbbb', 'cccccc', 'dddddd', 'eeeeee', 'ffffff'],pattern = "aaaaaa") == ['aaaaaa', 'bbbbbb', 'cccccc', 'dddddd', 'eeeeee', 'ffffff']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aab', 'aba', 'aab', 'aba', 'aab'],pattern = "aba") == ['aba', 'aba']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aab', 'aba', 'aab', 'aba', 'aab'],pattern = "aba") == ['aba', 'aba']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaaa', 'bbbbb', 'ccccc'],pattern = "abcde") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaaa', 'bbbbb', 'ccccc'],pattern = "abcde") == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'vwxyz', 'mnopq', 'rstuv', 'fghij'],pattern = "abcde") == ['abcde', 'vwxyz', 'mnopq', 'rstuv', 'fghij']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'vwxyz', 'mnopq', 'rstuv', 'fghij'],pattern = "abcde") == ['abcde', 'vwxyz', 'mnopq', 'rstuv', 'fghij']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aab', 'aba', 'baa', 'aaa'],pattern = "aab") == ['aab']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aab', 'aba', 'baa', 'aaa'],pattern = "aab") == ['aab']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abac', 'debd', 'mee', 'aqq', 'dkd', 'ccc'],pattern = "abac") == ['abac', 'dkd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abac', 'debd', 'mee', 'aqq', 'dkd', 'ccc'],pattern = "abac") == ['abac', 'dkd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabb', 'bbcc', 'ccdd'],pattern = "aabb") == ['aabb', 'bbcc', 'ccdd']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabb', 'bbcc', 'ccdd'],pattern = "aabb") == ['aabb', 'bbcc', 'ccdd']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbccdd', 'bbaaddcc', 'ccddaabb', 'ddccaabb'],pattern = "aabbccdd") == ['aabbccdd', 'bbaaddcc', 'ccddaabb', 'ddccaabb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbccdd', 'bbaaddcc', 'ccddaabb', 'ddccaabb'],pattern = "aabbccdd") == ['aabbccdd', 'bbaaddcc', 'ccddaabb', 'ddccaabb']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefgh', 'hgfedcba', 'abcdefgh', 'hgfedcba'],pattern = "abcdefgh") == ['abcdefgh', 'hgfedcba', 'abcdefgh', 'hgfedcba']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefgh', 'hgfedcba', 'abcdefgh', 'hgfedcba'],pattern = "abcdefgh") == ['abcdefgh', 'hgfedcba', 'abcdefgh', 'hgfedcba']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['wxyz', 'wyxz', 'wyzx', 'wxzy', 'wxyz'],pattern = "wxyz") == ['wxyz', 'wyxz', 'wyzx', 'wxzy', 'wxyz']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['wxyz', 'wyxz', 'wyzx', 'wxzy', 'wxyz'],pattern = "wxyz") == ['wxyz', 'wyxz', 'wyzx', 'wxzy', 'wxyz']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'zzzzyyyyxxxxwwwwvvvvuuuuttssrrqqppoonnmmllkkjjiihhggee', 'mnopmnopmnopmnopmnopmnopmnopmnopmnopmnopmnop'],pattern = "abcdefghijklmnopqrstuvwxyzzz") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'zzzzyyyyxxxxwwwwvvvvuuuuttssrrqqppoonnmmllkkjjiihhggee', 'mnopmnopmnopmnopmnopmnopmnopmnopmnopmnopmnop'],pattern = "abcdefghijklmnopqrstuvwxyzzz") == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzzz', 'yyyy', 'xxxx', 'wwww', 'vvvv', 'uuuu'],pattern = "aaaa") == ['zzzz', 'yyyy', 'xxxx', 'wwww', 'vvvv', 'uuuu']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzzz', 'yyyy', 'xxxx', 'wwww', 'vvvv', 'uuuu'],pattern = "aaaa") == ['zzzz', 'yyyy', 'xxxx', 'wwww', 'vvvv', 'uuuu']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'ba', 'aa', 'bb', 'cc', 'dd'],pattern = "ab") == ['ab', 'ba']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'ba', 'aa', 'bb', 'cc', 'dd'],pattern = "ab") == ['ab', 'ba']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xxyy', 'xyyx', 'xxyx', 'yxyx'],pattern = "abab") == ['yxyx']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xxyy', 'xyyx', 'xxyx', 'yxyx'],pattern = "abab") == ['yxyx']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abac', 'abcd', 'abca', 'abac'],pattern = "abac") == ['abac', 'abac']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abac', 'abcd', 'abca', 'abac'],pattern = "abac") == ['abac', 'abac']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['uvw', 'uvw', 'uvw', 'uvw', 'uvw', 'uvw'],pattern = "uvw") == ['uvw', 'uvw', 'uvw', 'uvw', 'uvw', 'uvw']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['uvw', 'uvw', 'uvw', 'uvw', 'uvw', 'uvw'],pattern = "uvw") == ['uvw', 'uvw', 'uvw', 'uvw', 'uvw', 'uvw']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcbacbacbacbacbac', 'bcabcabcabcabcabc', 'cbacbacbacbacbacba', 'bacbacbacbacbacbac'],pattern = "abcbacbacbacbacbac") == ['abcbacbacbacbacbac']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcbacbacbacbacbac', 'bcabcabcabcabcabc', 'cbacbacbacbacbacba', 'bacbacbacbacbacbac'],pattern = "abcbacbacbacbacbac") == ['abcbacbacbacbacbac']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['pqrs', 'prqs', 'psqr', 'psrq', 'pqsr'],pattern = "qrst") == ['pqrs', 'prqs', 'psqr', 'psrq', 'pqsr']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['pqrs', 'prqs', 'psqr', 'psrq', 'pqsr'],pattern = "qrst") == ['pqrs', 'prqs', 'psqr', 'psrq', 'pqsr']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh'],pattern = "abc") == ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh'],pattern = "abc") == ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabcb', 'bbaab', 'cbbaa', 'ababa'],pattern = "aabcb") == ['aabcb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabcb', 'bbaab', 'cbbaa', 'ababa'],pattern = "aabcb") == ['aabcb']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abababababababababab', 'bababababababababa', 'aabbaabbaabbaabb', 'bbabbaabbaabbabb'],pattern = "abababababababababab") == ['abababababababababab', 'bababababababababa']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abababababababababab', 'bababababababababa', 'aabbaabbaabbaabb', 'bbabbaabbaabbabb'],pattern = "abababababababababab") == ['abababababababababab', 'bababababababababa']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'zyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx', 'mnopmnopmnopmnopmnopmnopmnopmnopmnopmnopmnop'],pattern = "abcdefghijklmnopqrstuvwxyzz") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'zyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx', 'mnopmnopmnopmnopmnopmnopmnopmnopmnopmnopmnop'],pattern = "abcdefghijklmnopqrstuvwxyzz") == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaabbbb', 'ccccdddd', 'eeeeffff', 'ggggaaaa', 'bbbbcccc'],pattern = "aabbccdd") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaabbbb', 'ccccdddd', 'eeeeffff', 'ggggaaaa', 'bbbbcccc'],pattern = "aabbccdd") == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaaa', 'bbbbb', 'ccccc'],pattern = "zzzzz") == ['aaaaa', 'bbbbb', 'ccccc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaaa', 'bbbbb', 'ccccc'],pattern = "zzzzz") == ['aaaaa', 'bbbbb', 'ccccc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mxyz', 'yzxy', 'zxyz', 'yzzx', 'zzzz'],pattern = "wxyz") == ['mxyz']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mxyz', 'yzxy', 'zxyz', 'yzzx', 'zzzz'],pattern = "wxyz") == ['mxyz']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabb', 'bbcc', 'ccdd', 'aacc', 'abab'],pattern = "aabb") == ['aabb', 'bbcc', 'ccdd', 'aacc']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabb', 'bbcc', 'ccdd', 'aacc', 'abab'],pattern = "aabb") == ['aabb', 'bbcc', 'ccdd', 'aacc']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcabc', 'defdef', 'ghighi', 'jkljkl', 'mnopmn', 'opqropqr'],pattern = "abcabc") == ['abcabc', 'defdef', 'ghighi', 'jkljkl']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcabc', 'defdef', 'ghighi', 'jkljkl', 'mnopmn', 'opqropqr'],pattern = "abcabc") == ['abcabc', 'defdef', 'ghighi', 'jkljkl']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'],pattern = "abc") == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'],pattern = "abc") == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abdc', 'acbd', 'acdb'],pattern = "acdb") == ['abcd', 'abdc', 'acbd', 'acdb']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abdc', 'acbd', 'acdb'],pattern = "acdb") == ['abcd', 'abdc', 'acbd', 'acdb']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'bbccdd', 'ccddeeff', 'ddeeffgg', 'eeffgghh'],pattern = "aabbc") == ['aabbcc', 'bbccdd', 'ccddeeff', 'ddeeffgg', 'eeffgghh']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'bbccdd', 'ccddeeff', 'ddeeffgg', 'eeffgghh'],pattern = "aabbc") == ['aabbcc', 'bbccdd', 'ccddeeff', 'ddeeffgg', 'eeffgghh']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['stuv', 'stvu', 'tuvv', 'stvv', 'stvu'],pattern = "stvu") == ['stuv', 'stvu', 'stvu']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['stuv', 'stvu', 'tuvv', 'stvv', 'stvu'],pattern = "stvu") == ['stuv', 'stvu', 'stvu']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abac', 'deed', 'zaff'],pattern = "abab") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abac', 'deed', 'zaff'],pattern = "abab") == []: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ababab', 'bababa', 'ababba', 'bababb', 'aabbab', 'bbaaab', 'abbaab', 'babaab'],pattern = "ababab") == ['ababab', 'bababa']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ababab', 'bababa', 'ababba', 'bababb', 'aabbab', 'bbaaab', 'abbaab', 'babaab'],pattern = "ababab") == ['ababab', 'bababa']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mnop', 'ponm', 'mpon', 'mnop', 'nmop'],pattern = "mnop") == ['mnop', 'ponm', 'mpon', 'mnop', 'nmop']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mnop', 'ponm', 'mpon', 'mnop', 'nmop'],pattern = "mnop") == ['mnop', 'ponm', 'mpon', 'mnop', 'nmop']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abac', 'baca', 'caab', 'acab', 'caba'],pattern = "abac") == ['abac', 'acab']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abac', 'baca', 'caab', 'acab', 'caba'],pattern = "abac") == ['abac', 'acab']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabb', 'bbaa', 'abab', 'baab', 'aaaa', 'bbbb', 'abba', 'baba'],pattern = "aabb") == ['aabb', 'bbaa']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabb', 'bbaa', 'abab', 'baab', 'aaaa', 'bbbb', 'abba', 'baba'],pattern = "aabb") == ['aabb', 'bbaa']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcabc', 'defdef', 'ghighi', 'jkljkl', 'mnopqr'],pattern = "abcabc") == ['abcabc', 'defdef', 'ghighi', 'jkljkl']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcabc', 'defdef', 'ghighi', 'jkljkl', 'mnopqr'],pattern = "abcabc") == ['abcabc', 'defdef', 'ghighi', 'jkljkl']: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(words = ['hello', 'world', 'leetcode'],pattern = "aaaaa") == []
    assert candidate(words = ['abc', 'deq', 'mee', 'aqq', 'dkd', 'ccc'],pattern = "abb") == ['mee', 'aqq']
    assert candidate(words = ['abb', 'abb', 'abb'],pattern = "abc") == []
    assert candidate(words = ['abb', 'abc', 'abz', 'xyz', 'xyy'],pattern = "abb") == ['abb', 'xyy']
    assert candidate(words = ['aaa', 'bbb', 'ccc'],pattern = "aaa") == ['aaa', 'bbb', 'ccc']
    assert candidate(words = ['a', 'b', 'c'],pattern = "a") == ['a', 'b', 'c']
    assert candidate(words = ['hello', 'world', 'abcde', 'uvwxy'],pattern = "abcde") == ['world', 'abcde', 'uvwxy']
    assert candidate(words = ['abb', 'abb', 'abb', 'abb'],pattern = "abc") == []
    assert candidate(words = ['abb', 'abc', 'aab'],pattern = "abb") == ['abb']
    assert candidate(words = ['aba', 'bcb', 'bab'],pattern = "aba") == ['aba', 'bcb', 'bab']
    assert candidate(words = ['abb', 'abc', 'aab', 'aba'],pattern = "abb") == ['abb']
    assert candidate(words = ['abb', 'abc', 'xyz', 'xyy'],pattern = "abb") == ['abb', 'xyy']
    assert candidate(words = ['abb', 'aaa', 'aab'],pattern = "abb") == ['abb']
    assert candidate(words = ['abba', 'abab', 'baab', 'baba', 'aaaa'],pattern = "aabb") == []
    assert candidate(words = ['abac', 'bcad', 'aacc', 'bbdd', 'aabb'],pattern = "abab") == []
    assert candidate(words = ['abcdefg', 'hijklmn', 'opqrstu', 'vwxyzab', 'cdefghi'],pattern = "abcdefg") == ['abcdefg', 'hijklmn', 'opqrstu', 'vwxyzab', 'cdefghi']
    assert candidate(words = ['abcabc', 'bcbcbc', 'dedede', 'aiaiai', 'jkjkjk'],pattern = "abcabc") == ['abcabc']
    assert candidate(words = ['abcde', 'bcdef', 'cdefg', 'defgh', 'efghi'],pattern = "abcde") == ['abcde', 'bcdef', 'cdefg', 'defgh', 'efghi']
    assert candidate(words = ['zyx', 'yxz', 'xyz', 'zyz', 'yzy', 'zzy', 'zzz', 'zzz'],pattern = "zyx") == ['zyx', 'yxz', 'xyz']
    assert candidate(words = ['xyx', 'yxy', 'xyz', 'zyz'],pattern = "aba") == ['xyx', 'yxy', 'zyz']
    assert candidate(words = ['abcde', 'bcdea', 'cdeab', 'deabc', 'eabcd'],pattern = "abcde") == ['abcde', 'bcdea', 'cdeab', 'deabc', 'eabcd']
    assert candidate(words = ['abcd', 'efgh', 'ijkl'],pattern = "abcd") == ['abcd', 'efgh', 'ijkl']
    assert candidate(words = ['aaaaabbbbbcccccdddddeeeeeffffffggggghhhhhhiiiiijjjjjkkkkklllllmmmmmnnnnnooooo', 'zzzzzyyyyyxxxxxwwwwwvvvvvtttttsssssrrrrrqqqqqppppoonnnnnmmmmmlllllkkkkkjjjjjiiiii', 'tttttsssssrrrrrqqqqqppppponnnnnmmmmmlllllkkkkkjjjjjiiiiihhhhhhgggggffffffeeeeedddddeeecccbbbaaaaa'],pattern = "tttttsssssrrrrrqqqqqppppponnnnnmmmmmlllllkkkkkjjjjjiiiiihhhhhhgggggffffffeeeeedddddeeecccbbbaaaaa") == ['tttttsssssrrrrrqqqqqppppponnnnnmmmmmlllllkkkkkjjjjjiiiiihhhhhhgggggffffffeeeeedddddeeecccbbbaaaaa']
    assert candidate(words = ['abcd', 'abcc', 'abbc', 'abcb', 'acbb', 'adbb'],pattern = "abbc") == ['abbc']
    assert candidate(words = ['xyx', 'yxy', 'xyy', 'yyy', 'xyxy'],pattern = "xxyx") == []
    assert candidate(words = ['abcd', 'dcba', 'abab', 'dcdc', 'aabb'],pattern = "abcd") == ['abcd', 'dcba']
    assert candidate(words = ['aabbcc', 'ddeeff', 'gghhii', 'jjkkll', 'mmnnoo'],pattern = "aabbcc") == ['aabbcc', 'ddeeff', 'gghhii', 'jjkkll', 'mmnnoo']
    assert candidate(words = ['zzzz', 'zzzz', 'zzzz', 'zzzz'],pattern = "aaaa") == ['zzzz', 'zzzz', 'zzzz', 'zzzz']
    assert candidate(words = ['abbc', 'deee', 'zzzz'],pattern = "aabb") == []
    assert candidate(words = ['abcde', 'bcdea', 'cdeab', 'deabc', 'eabcd', 'fghij'],pattern = "abcde") == ['abcde', 'bcdea', 'cdeab', 'deabc', 'eabcd', 'fghij']
    assert candidate(words = ['abcdef', 'fedcba', 'ghijkl', 'lkjihg', 'mnopqr', 'rqponm'],pattern = "abcdef") == ['abcdef', 'fedcba', 'ghijkl', 'lkjihg', 'mnopqr', 'rqponm']
    assert candidate(words = ['ijkl', 'ikjl', 'ijlk', 'ijlk', 'ikjl'],pattern = "ijkl") == ['ijkl', 'ikjl', 'ijlk', 'ijlk', 'ikjl']
    assert candidate(words = ['mnop', 'qrst', 'uvwx'],pattern = "mnop") == ['mnop', 'qrst', 'uvwx']
    assert candidate(words = ['xyzx', 'yzxy', 'zxyx', 'yxzy', 'xzyz', 'zyzx', 'yzyz', 'zyzy'],pattern = "abcb") == ['zxyx', 'xzyz']
    assert candidate(words = ['mnop', 'mnop', 'mnop', 'mnop', 'mnop', 'mnop', 'mnop', 'mnop'],pattern = "mnop") == ['mnop', 'mnop', 'mnop', 'mnop', 'mnop', 'mnop', 'mnop', 'mnop']
    assert candidate(words = ['tttt', 'tqtq', 'ttqt', 'qtqt', 'qtqq'],pattern = "aaaa") == ['tttt']
    assert candidate(words = ['xyy', 'yxx', 'xyz', 'xyx', 'xxy'],pattern = "aba") == ['xyx']
    assert candidate(words = ['qrst', 'qstr', 'qrts', 'qtsr', 'qtpr', 'qrsp'],pattern = "qrst") == ['qrst', 'qstr', 'qrts', 'qtsr', 'qtpr', 'qrsp']
    assert candidate(words = ['xyzy', 'zyxy', 'yzyx', 'zyxz'],pattern = "xyzy") == ['xyzy', 'zyxy']
    assert candidate(words = ['mnop', 'qrst', 'uvwx', 'yzxy', 'qrst'],pattern = "abcd") == ['mnop', 'qrst', 'uvwx', 'qrst']
    assert candidate(words = ['qrst', 'rstq', 'stqr', 'tqrs', 'qrst', 'rstq', 'stqr', 'tqrs'],pattern = "abcd") == ['qrst', 'rstq', 'stqr', 'tqrs', 'qrst', 'rstq', 'stqr', 'tqrs']
    assert candidate(words = ['mnop', 'nopm', 'opmn', 'pqrs', 'qrst', 'stuv', 'tuvw', 'uvwx'],pattern = "mnop") == ['mnop', 'nopm', 'opmn', 'pqrs', 'qrst', 'stuv', 'tuvw', 'uvwx']
    assert candidate(words = ['xxy', 'xyy', 'yxx', 'yyx', 'xyx', 'yxy'],pattern = "xyy") == ['xyy', 'yxx']
    assert candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk'],pattern = "abc") == ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk']
    assert candidate(words = ['abacabadabacaba', 'babcbabcbbabcbb', 'abacabadabcadaa'],pattern = "abacabadabacaba") == ['abacabadabacaba']
    assert candidate(words = ['abbcc', 'aabbb', 'aabbcc', 'abbbaa', 'abacba', 'abcabc'],pattern = "abbcc") == ['abbcc']
    assert candidate(words = ['xyyx', 'mnop', 'qrst'],pattern = "mnop") == ['mnop', 'qrst']
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijkabcdefghijk'],pattern = "abcdefghijklmnopqrstuvwxyz") == ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba']
    assert candidate(words = ['deq', 'mee', 'aqq', 'dkd', 'ccc', 'eii', 'fff', 'ggh'],pattern = "abb") == ['mee', 'aqq', 'eii']
    assert candidate(words = ['abcde', 'vwxyz', 'pqrst'],pattern = "uvwxy") == ['abcde', 'vwxyz', 'pqrst']
    assert candidate(words = ['qrst', 'uvwx', 'yzab'],pattern = "abcd") == ['qrst', 'uvwx', 'yzab']
    assert candidate(words = ['xyx', 'yxy', 'zaz', 'azz', 'bzb', 'abb'],pattern = "aba") == ['xyx', 'yxy', 'zaz', 'bzb']
    assert candidate(words = ['xyz', 'xyy', 'xzy', 'yxy', 'yzy', 'zyx'],pattern = "xyz") == ['xyz', 'xzy', 'zyx']
    assert candidate(words = ['mnop', 'nmop', 'mnop', 'npom', 'mnop'],pattern = "abcd") == ['mnop', 'nmop', 'mnop', 'npom', 'mnop']
    assert candidate(words = ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzabcf'],pattern = "abcdef") == ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzabcf']
    assert candidate(words = ['mnop', 'nomp', 'mpon', 'mnop', 'mnoo', 'mmno'],pattern = "mnop") == ['mnop', 'nomp', 'mpon', 'mnop']
    assert candidate(words = ['abca', 'decd', 'mefm', 'aqqz', 'dkdf', 'ccca'],pattern = "abba") == []
    assert candidate(words = ['aabbcc', 'bbccdd', 'ccddaa', 'ddeeff', 'eefggh'],pattern = "aabbcc") == ['aabbcc', 'bbccdd', 'ccddaa', 'ddeeff']
    assert candidate(words = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk'],pattern = "abcd") == ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk']
    assert candidate(words = ['abba', 'abab', 'aabb', 'baba', 'baab', 'bbaa'],pattern = "abba") == ['abba', 'baab']
    assert candidate(words = ['abacaba', 'cabadab', 'bacabac', 'adabaad', 'abaabab'],pattern = "abacaba") == ['abacaba']
    assert candidate(words = ['ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs'],pattern = "mnop") == ['ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs']
    assert candidate(words = ['zzzzz', 'yyyyy', 'xxxxx', 'wwwww', 'vvvvv'],pattern = "aaaaa") == ['zzzzz', 'yyyyy', 'xxxxx', 'wwwww', 'vvvvv']
    assert candidate(words = ['mnoonm', 'mnoono', 'mmnnoo', 'noonmm'],pattern = "mnoonm") == ['mnoonm']
    assert candidate(words = ['xyyx', 'mnop', 'qrst'],pattern = "abba") == ['xyyx']
    assert candidate(words = ['zzz', 'aaa', 'zzz', 'aaa'],pattern = "abc") == []
    assert candidate(words = ['abcde', 'edcba', 'abcde', 'edcba'],pattern = "abcde") == ['abcde', 'edcba', 'abcde', 'edcba']
    assert candidate(words = ['abcd', 'abca', 'abcb', 'abcc', 'abdd'],pattern = "abba") == []
    assert candidate(words = ['baba', 'abab', 'aaaa', 'bbbb', 'abcd'],pattern = "abba") == []
    assert candidate(words = ['abcd', 'abab', 'abac', 'aabb', 'abba', 'aaaa', 'bbbb', 'abac'],pattern = "abcd") == ['abcd']
    assert candidate(words = ['abcabcabcabcabcabcabcabc', 'bcbcbcbcbcbcbcbcbcbcbcbcbcbcb', 'cbbccbbccbbccbbccbbccbbccbbcc', 'abcbbccbbccbbccbbccbbccbbccbb'],pattern = "abcabcabcabcabcabcabcabc") == ['abcabcabcabcabcabcabcabc']
    assert candidate(words = ['abac', 'deed', 'zaff'],pattern = "deed") == ['deed']
    assert candidate(words = ['abcdefgh', 'hgfedcba', 'ijklmnop', 'ponmlkji', 'qrstuvwx', 'xwvutsrq'],pattern = "abcdefgh") == ['abcdefgh', 'hgfedcba', 'ijklmnop', 'ponmlkji', 'qrstuvwx', 'xwvutsrq']
    assert candidate(words = ['abcde', 'vwxyz', 'pqrst'],pattern = "vwxyz") == ['abcde', 'vwxyz', 'pqrst']
    assert candidate(words = ['abac', 'baba', 'abca', 'baac', 'caba', 'dada'],pattern = "abac") == ['abac']
    assert candidate(words = ['efgh', 'efgi', 'efgh', 'efgi', 'efgh'],pattern = "abcd") == ['efgh', 'efgi', 'efgh', 'efgi', 'efgh']
    assert candidate(words = ['ababab', 'bababa', 'cdcdcd', 'dcdcdc', 'efefef', 'fefefe'],pattern = "ababab") == ['ababab', 'bababa', 'cdcdcd', 'dcdcdc', 'efefef', 'fefefe']
    assert candidate(words = ['abab', 'baba', 'abba', 'aaaa', 'bbbb', 'cccc', 'aabb', 'abab'],pattern = "abab") == ['abab', 'baba', 'abab']
    assert candidate(words = ['abab', 'baba', 'abba', 'baab', 'aaaa', 'bbbb'],pattern = "abab") == ['abab', 'baba']
    assert candidate(words = ['aabbcc', 'bbccdd', 'ccddaa', 'ddeeff', 'eeffgg', 'ffggee'],pattern = "abcdef") == []
    assert candidate(words = ['zzzz', 'zzyz', 'zyzy', 'zyyz'],pattern = "aaaa") == ['zzzz']
    assert candidate(words = ['aaaaaa', 'bbbbbb', 'cccccc', 'dddddd', 'eeeeee', 'ffffff'],pattern = "aaaaaa") == ['aaaaaa', 'bbbbbb', 'cccccc', 'dddddd', 'eeeeee', 'ffffff']
    assert candidate(words = ['aab', 'aba', 'aab', 'aba', 'aab'],pattern = "aba") == ['aba', 'aba']
    assert candidate(words = ['aaaaa', 'bbbbb', 'ccccc'],pattern = "abcde") == []
    assert candidate(words = ['abcde', 'vwxyz', 'mnopq', 'rstuv', 'fghij'],pattern = "abcde") == ['abcde', 'vwxyz', 'mnopq', 'rstuv', 'fghij']
    assert candidate(words = ['aab', 'aba', 'baa', 'aaa'],pattern = "aab") == ['aab']
    assert candidate(words = ['abac', 'debd', 'mee', 'aqq', 'dkd', 'ccc'],pattern = "abac") == ['abac', 'dkd']
    assert candidate(words = ['aabb', 'bbcc', 'ccdd'],pattern = "aabb") == ['aabb', 'bbcc', 'ccdd']
    assert candidate(words = ['aabbccdd', 'bbaaddcc', 'ccddaabb', 'ddccaabb'],pattern = "aabbccdd") == ['aabbccdd', 'bbaaddcc', 'ccddaabb', 'ddccaabb']
    assert candidate(words = ['abcdefgh', 'hgfedcba', 'abcdefgh', 'hgfedcba'],pattern = "abcdefgh") == ['abcdefgh', 'hgfedcba', 'abcdefgh', 'hgfedcba']
    assert candidate(words = ['wxyz', 'wyxz', 'wyzx', 'wxzy', 'wxyz'],pattern = "wxyz") == ['wxyz', 'wyxz', 'wyzx', 'wxzy', 'wxyz']
    assert candidate(words = ['aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'zzzzyyyyxxxxwwwwvvvvuuuuttssrrqqppoonnmmllkkjjiihhggee', 'mnopmnopmnopmnopmnopmnopmnopmnopmnopmnopmnop'],pattern = "abcdefghijklmnopqrstuvwxyzzz") == []
    assert candidate(words = ['zzzz', 'yyyy', 'xxxx', 'wwww', 'vvvv', 'uuuu'],pattern = "aaaa") == ['zzzz', 'yyyy', 'xxxx', 'wwww', 'vvvv', 'uuuu']
    assert candidate(words = ['ab', 'ba', 'aa', 'bb', 'cc', 'dd'],pattern = "ab") == ['ab', 'ba']
    assert candidate(words = ['xxyy', 'xyyx', 'xxyx', 'yxyx'],pattern = "abab") == ['yxyx']
    assert candidate(words = ['abac', 'abcd', 'abca', 'abac'],pattern = "abac") == ['abac', 'abac']
    assert candidate(words = ['uvw', 'uvw', 'uvw', 'uvw', 'uvw', 'uvw'],pattern = "uvw") == ['uvw', 'uvw', 'uvw', 'uvw', 'uvw', 'uvw']
    assert candidate(words = ['abcbacbacbacbacbac', 'bcabcabcabcabcabc', 'cbacbacbacbacbacba', 'bacbacbacbacbacbac'],pattern = "abcbacbacbacbacbac") == ['abcbacbacbacbacbac']
    assert candidate(words = ['pqrs', 'prqs', 'psqr', 'psrq', 'pqsr'],pattern = "qrst") == ['pqrs', 'prqs', 'psqr', 'psrq', 'pqsr']
    assert candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh'],pattern = "abc") == ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh']
    assert candidate(words = ['aabcb', 'bbaab', 'cbbaa', 'ababa'],pattern = "aabcb") == ['aabcb']
    assert candidate(words = ['abababababababababab', 'bababababababababa', 'aabbaabbaabbaabb', 'bbabbaabbaabbabb'],pattern = "abababababababababab") == ['abababababababababab', 'bababababababababa']
    assert candidate(words = ['abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'zyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyx', 'mnopmnopmnopmnopmnopmnopmnopmnopmnopmnopmnop'],pattern = "abcdefghijklmnopqrstuvwxyzz") == []
    assert candidate(words = ['aaaabbbb', 'ccccdddd', 'eeeeffff', 'ggggaaaa', 'bbbbcccc'],pattern = "aabbccdd") == []
    assert candidate(words = ['aaaaa', 'bbbbb', 'ccccc'],pattern = "zzzzz") == ['aaaaa', 'bbbbb', 'ccccc']
    assert candidate(words = ['mxyz', 'yzxy', 'zxyz', 'yzzx', 'zzzz'],pattern = "wxyz") == ['mxyz']
    assert candidate(words = ['aabb', 'bbcc', 'ccdd', 'aacc', 'abab'],pattern = "aabb") == ['aabb', 'bbcc', 'ccdd', 'aacc']
    assert candidate(words = ['abcabc', 'defdef', 'ghighi', 'jkljkl', 'mnopmn', 'opqropqr'],pattern = "abcabc") == ['abcabc', 'defdef', 'ghighi', 'jkljkl']
    assert candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'],pattern = "abc") == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert candidate(words = ['abcd', 'abdc', 'acbd', 'acdb'],pattern = "acdb") == ['abcd', 'abdc', 'acbd', 'acdb']
    assert candidate(words = ['aabbcc', 'bbccdd', 'ccddeeff', 'ddeeffgg', 'eeffgghh'],pattern = "aabbc") == ['aabbcc', 'bbccdd', 'ccddeeff', 'ddeeffgg', 'eeffgghh']
    assert candidate(words = ['stuv', 'stvu', 'tuvv', 'stvv', 'stvu'],pattern = "stvu") == ['stuv', 'stvu', 'stvu']
    assert candidate(words = ['abac', 'deed', 'zaff'],pattern = "abab") == []
    assert candidate(words = ['ababab', 'bababa', 'ababba', 'bababb', 'aabbab', 'bbaaab', 'abbaab', 'babaab'],pattern = "ababab") == ['ababab', 'bababa']
    assert candidate(words = ['mnop', 'ponm', 'mpon', 'mnop', 'nmop'],pattern = "mnop") == ['mnop', 'ponm', 'mpon', 'mnop', 'nmop']
    assert candidate(words = ['abac', 'baca', 'caab', 'acab', 'caba'],pattern = "abac") == ['abac', 'acab']
    assert candidate(words = ['aabb', 'bbaa', 'abab', 'baab', 'aaaa', 'bbbb', 'abba', 'baba'],pattern = "aabb") == ['aabb', 'bbaa']
    assert candidate(words = ['abcabc', 'defdef', 'ghighi', 'jkljkl', 'mnopqr'],pattern = "abcabc") == ['abcabc', 'defdef', 'ghighi', 'jkljkl']


