def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(strs = ['zyx', 'zyx', 'zyx']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zyx', 'zyx', 'zyx']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['rrjk', 'furt', 'guzm']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['rrjk', 'furt', 'guzm']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['axx', 'ggs', 'zzz']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['axx', 'ggs', 'zzz']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['ghi', 'def', 'abc']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['ghi', 'def', 'abc']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['aaa', 'bbb', 'ccc']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['aaa', 'bbb', 'ccc']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abc', 'bcd', 'cde']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abc', 'bcd', 'cde']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abc', 'abc', 'abc']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abc', 'abc', 'abc']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['a', 'b', 'c', 'd']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['a', 'b', 'c', 'd']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdef', 'uvwxyz']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdef', 'uvwxyz']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zzz', 'aaa', 'zzz']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zzz', 'aaa', 'zzz']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zyx', 'wvu', 'tsr']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zyx', 'wvu', 'tsr']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['edcba']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['edcba']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'abdc', 'acdb']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'abdc', 'acdb']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'dbca', 'adcb', 'cbad']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'dbca', 'adcb', 'cbad']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['babca', 'bbazb']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['babca', 'bbazb']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['a', 'b', 'c']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['a', 'b', 'c']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzabcd']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzabcd']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['fedcb', 'edcba', 'dcbae', 'cbade', 'baced', 'acbed']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['fedcb', 'edcba', 'dcbae', 'cbade', 'baced', 'acbed']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba']) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba']) == 25: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'adbc', 'bacd', 'bdac']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'adbc', 'bacd', 'bdac']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abacabad', 'babacaba', 'cacabada', 'dacabada']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abacabad', 'babacaba', 'cacabada', 'dacabada']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdabcd', 'dcbaabcd', 'abcdabdc', 'abdcabcd', 'abcdcdab', 'cdabcdab', 'abcdabcd', 'cdababcd', 'abcdcdab', 'dcabcdab']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdabcd', 'dcbaabcd', 'abcdabdc', 'abdcabcd', 'abcdcdab', 'cdabcdab', 'abcdabcd', 'cdababcd', 'abcdcdab', 'dcabcdab']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdefgh', 'hgfedcba', 'abcdefgh', 'hgfedcba', 'abcdefgh']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdefgh', 'hgfedcba', 'abcdefgh', 'hgfedcba', 'abcdefgh']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['leetcode', 'leetcoed', 'leetcdeo', 'leetcodeo', 'leetcodeo', 'leetcodeo']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['leetcode', 'leetcoed', 'leetcdeo', 'leetcodeo', 'leetcodeo', 'leetcodeo']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zyx', 'yxz', 'xyz']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zyx', 'yxz', 'xyz']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['aabbaa', 'abcabc', 'acbacb', 'bacbac', 'bbacab']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['aabbaa', 'abcabc', 'acbacb', 'bacbac', 'bbacab']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zzz', 'yyy', 'xxx', 'www', 'vvv', 'uuu']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zzz', 'yyy', 'xxx', 'www', 'vvv', 'uuu']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdefgh', 'bcadegfh', 'cgdbefha', 'dgfbceha', 'egfdcbha', 'fgecadhb']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdefgh', 'bcadegfh', 'cgdbefha', 'dgfbceha', 'egfdcbha', 'fgecadhb']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklnmopqrstuvwxyz']) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklnmopqrstuvwxyz']) == 25: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zabc', 'zcad', 'zdba', 'zeac', 'zfcd', 'zgda', 'zhec', 'zida', 'zjea', 'zkcf']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zabc', 'zcad', 'zdba', 'zeac', 'zfcd', 'zgda', 'zhec', 'zida', 'zjea', 'zkcf']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['azazaz', 'bababa', 'cacaca', 'dadada', 'eaeaea']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['azazaz', 'bababa', 'cacaca', 'dadada', 'eaeaea']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdefg', 'bcefgij', 'acdfhij']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdefg', 'bcefgij', 'acdfhij']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'abdc', 'acdb', 'cadb', 'dabc']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'abdc', 'acdb', 'cadb', 'dabc']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['xyz', 'zyx', 'wvu', 'tsr', 'qpo', 'nml', 'kji', 'hgf', 'edc', 'baa']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['xyz', 'zyx', 'wvu', 'tsr', 'qpo', 'nml', 'kji', 'hgf', 'edc', 'baa']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['aeg', 'bdh', 'cfi', 'egj', 'fhk', 'gjl']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['aeg', 'bdh', 'cfi', 'egj', 'fhk', 'gjl']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['qrst', 'mnop', 'ijkl', 'efgh', 'abcd', 'mnop', 'qrst', 'efgh', 'ijkl', 'abcd', 'mnop', 'qrst', 'efgh', 'ijkl', 'abcd', 'mnop', 'qrst', 'efgh', 'ijkl', 'abcd']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['qrst', 'mnop', 'ijkl', 'efgh', 'abcd', 'mnop', 'qrst', 'efgh', 'ijkl', 'abcd', 'mnop', 'qrst', 'efgh', 'ijkl', 'abcd', 'mnop', 'qrst', 'efgh', 'ijkl', 'abcd']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zzzzzzzz', 'zzzzzzzy', 'zzzzzzzx', 'zzzzzzyx', 'zzzzzyxy', 'zzzzyxxy', 'zzzyxxyx', 'zzyxxyxy']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zzzzzzzz', 'zzzzzzzy', 'zzzzzzzx', 'zzzzzzyx', 'zzzzzyxy', 'zzzzyxxy', 'zzzyxxyx', 'zzyxxyxy']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdefghij', 'abcdefghik', 'abcdefghij', 'abcdefghim', 'abcdefghin']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdefghij', 'abcdefghik', 'abcdefghij', 'abcdefghim', 'abcdefghin']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['aabbcc', 'bbccaa', 'ccaabb', 'aabbbc']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['aabbcc', 'bbccaa', 'ccaabb', 'aabbbc']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdefg', 'bceghik', 'acegikm', 'adegimn']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdefg', 'bceghik', 'acegikm', 'adegimn']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['qwertyuiop', 'asdfghjklz', 'zxcvbnmqwe', 'qwertyuiop', 'asdfghjklz']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['qwertyuiop', 'asdfghjklz', 'zxcvbnmqwe', 'qwertyuiop', 'asdfghjklz']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['qrst', 'rstu', 'stuv', 'tuvw', 'uvwx']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['qrst', 'rstu', 'stuv', 'tuvw', 'uvwx']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['aabbccdd', 'bbaaccee', 'ccaabbee', 'ddeebbaa', 'eeccbbdd']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['aabbccdd', 'bbaaccee', 'ccaabbee', 'ddeebbaa', 'eeccbbdd']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba']) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba']) == 25: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['qwerty', 'wertyq', 'ertyqw', 'rtyqwe', 'tyqwer', 'yqwret']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['qwerty', 'wertyq', 'ertyqw', 'rtyqwe', 'tyqwer', 'yqwret']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['cba', 'bca', 'bac', 'acb']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['cba', 'bca', 'bac', 'acb']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['aebf', 'accf', 'bdgf', 'cddg', 'defh', 'edgh', 'feih', 'gjih', 'hkji']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['aebf', 'accf', 'bdgf', 'cddg', 'defh', 'edgh', 'feih', 'gjih', 'hkji']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['aabbcc', 'bbaacc', 'ccabba', 'aababc', 'bbacab', 'abcabc', 'cbaabc', 'abacba', 'bacabc', 'cababc']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['aabbcc', 'bbaacc', 'ccabba', 'aababc', 'bbacab', 'abcabc', 'cbaabc', 'abacba', 'bacabc', 'cababc']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zyxwvu', 'utsrqpon', 'mlkjihgf', 'edcba']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zyxwvu', 'utsrqpon', 'mlkjihgf', 'edcba']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['cba', 'daf', 'gee']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['cba', 'daf', 'gee']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abc', 'bac', 'cab', 'bca', 'cab', 'cba']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abc', 'bac', 'cab', 'bca', 'cab', 'cba']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['leetcode', 'leetcede', 'leotcede']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['leetcode', 'leetcede', 'leotcede']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba']) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba']) == 25: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'adcb', 'bacd', 'bdac', 'cabd', 'cdab', 'dcba', 'dcab', 'dabc', 'dacb']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'adcb', 'bacd', 'bdac', 'cabd', 'cdab', 'dcba', 'dcab', 'dabc', 'dacb']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zzzz', 'zzyz', 'zyyz', 'yzzz', 'yzyz', 'yyyz', 'yyyx', 'yyxx', 'yxxx', 'xxxx']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zzzz', 'zzyz', 'zyyz', 'yzzz', 'yzyz', 'yyyz', 'yyyx', 'yyxx', 'yxxx', 'xxxx']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yzab']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yzab']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['aabbcc', 'bbaacc', 'bbacac', 'aabcbc', 'cababc', 'bcbacc']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['aabbcc', 'bbaacc', 'bbacac', 'aabcbc', 'cababc', 'bcbacc']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['xyz', 'zyx', 'yxz', 'xzy', 'yzx', 'zxy']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['xyz', 'zyx', 'yxz', 'xzy', 'yzx', 'zxy']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'mnopqrstuvwxyzabcdefghijkl', 'fedcbazyxwvutsrqponmlkjihg']) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'mnopqrstuvwxyzabcdefghijkl', 'fedcbazyxwvutsrqponmlkjihg']) == 25: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['mnopqr', 'opqrst', 'pqrstu', 'qrstuv']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['mnopqr', 'opqrst', 'pqrstu', 'qrstuv']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'dcba', 'abcd', 'dcba']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'dcba', 'abcd', 'dcba']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['aabbcc', 'bbccaa', 'ccaabb', 'aabbbc', 'bbccaa', 'ccaabb', 'aabbbc']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['aabbcc', 'bbccaa', 'ccaabb', 'aabbbc', 'bbccaa', 'ccaabb', 'aabbbc']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdefg', 'gfedcba', 'bacdefg', 'ihgfedc', 'jklmnop']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdefg', 'gfedcba', 'bacdefg', 'ihgfedc', 'jklmnop']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['qpwoeiruty', 'qpwoeiruty', 'qpwoeiruty']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['qpwoeiruty', 'qpwoeiruty', 'qpwoeiruty']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['mnop', 'qrst', 'uvwx', 'yzab', 'cdef', 'ghij', 'klmn', 'opqr', 'stuv', 'wxyz']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['mnop', 'qrst', 'uvwx', 'yzab', 'cdef', 'ghij', 'klmn', 'opqr', 'stuv', 'wxyz']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'bcde', 'cdef', 'defg']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'bcde', 'cdef', 'defg']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['aabbcc', 'abbccc', 'abcccc', 'bcccdd', 'cccddd', 'ccdddd', 'cddddd', 'dddddd']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['aabbcc', 'abbccc', 'abcccc', 'bcccdd', 'cccddd', 'ccdddd', 'cddddd', 'dddddd']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['aabbccddeeff', 'abcdefabcdef', 'fedcbafedcba', 'abcdefabcdef', 'aabbccddeeff']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['aabbccddeeff', 'abcdefabcdef', 'fedcbafedcba', 'abcdefabcdef', 'aabbccddeeff']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdefghij', 'jihgfedcba', 'abcdefghij', 'jihgfedcba', 'abcdefghij', 'jihgfedcba']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdefghij', 'jihgfedcba', 'abcdefghij', 'jihgfedcba', 'abcdefghij', 'jihgfedcba']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba']) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba']) == 25: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwx', 'vwxy', 'wxyz']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwx', 'vwxy', 'wxyz']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['aabbcc', 'bbccdd', 'ccddeeff', 'ddeeffgg']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['aabbcc', 'bbccdd', 'ccddeeff', 'ddeeffgg']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdabcd', 'bcdbcdcd', 'cdcdcdcd', 'dcdcdcdc', 'efefefef', 'fefefefe', 'gfefefef', 'hfhfhfhf', 'ihihihih']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdabcd', 'bcdbcdcd', 'cdcdcdcd', 'dcdcdcdc', 'efefefef', 'fefefefe', 'gfefefef', 'hfhfhfhf', 'ihihihih']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['xyzuvw', 'wvuxyz', 'uvwxyx', 'vxyzwu', 'uzwvxy', 'zwxyuv', 'yxwvuz', 'zyxuvw', 'wvuzxy', 'uvwxyx', 'vxyzwu', 'uzwvxy', 'zwxyuv', 'yxwvuz', 'zyxuvw', 'wvuzxy', 'uvwxyx', 'vxyzwu', 'uzwvxy', 'zwxyuv', 'yxwvuz', 'zyxuvw']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['xyzuvw', 'wvuxyz', 'uvwxyx', 'vxyzwu', 'uzwvxy', 'zwxyuv', 'yxwvuz', 'zyxuvw', 'wvuzxy', 'uvwxyx', 'vxyzwu', 'uzwvxy', 'zwxyuv', 'yxwvuz', 'zyxuvw', 'wvuzxy', 'uvwxyx', 'vxyzwu', 'uzwvxy', 'zwxyuv', 'yxwvuz', 'zyxuvw']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcde', 'bcdef', 'cdefg', 'defgh', 'efghi', 'fghij', 'ghijk', 'hijkl', 'ijklm', 'jklmn']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcde', 'bcdef', 'cdefg', 'defgh', 'efghi', 'fghij', 'ghijk', 'hijkl', 'ijklm', 'jklmn']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['ba', 'ab', 'ba', 'ab', 'ba', 'ab']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['ba', 'ab', 'ba', 'ab', 'ba', 'ab']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['zab', 'bac', 'cab', 'dcb']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['zab', 'bac', 'cab', 'dcb']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdef', 'fedcba', 'dcbaef', 'bacfed', 'efabcd', 'fedcba']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdef', 'fedcba', 'dcbaef', 'bacfed', 'efabcd', 'fedcba']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['aaaaaaaaaa', 'aabbaabbcc', 'aabbaabbcc', 'aabbaabbcc', 'aabbaabbcc', 'aabbaabbcc']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['aaaaaaaaaa', 'aabbaabbcc', 'aabbaabbcc', 'aabbaabbcc', 'aabbaabbcc', 'aabbaabbcc']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'dcba', 'abcd', 'dcba', 'abcd']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'dcba', 'abcd', 'dcba', 'abcd']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee', 'fffff', 'ggggg', 'hhhhh', 'iiiii', 'jjjjj']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee', 'fffff', 'ggggg', 'hhhhh', 'iiiii', 'jjjjj']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['aabb', 'bbaa', 'abab', 'baba', 'abba', 'baab']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['aabb', 'bbaa', 'abab', 'baba', 'abba', 'baab']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'abdc', 'acbd', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'abdc', 'acbd', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk', 'pqrst', 'tsrqp', 'uvwxy', 'yxwvu', 'z', 'z', 'z', 'z', 'z']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk', 'pqrst', 'tsrqp', 'uvwxy', 'yxwvu', 'z', 'z', 'z', 'z', 'z']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcd', 'efgh', 'ijkl', 'mnop']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcd', 'efgh', 'ijkl', 'mnop']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['abcdefg', 'gfedcba', 'hijklmn', 'nmolkji', 'opqrstu', 'utsrqpo']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['abcdefg', 'gfedcba', 'hijklmn', 'nmolkji', 'opqrstu', 'utsrqpo']) == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(strs = ['zyx', 'zyx', 'zyx']) == 2
    assert candidate(strs = ['rrjk', 'furt', 'guzm']) == 2
    assert candidate(strs = ['axx', 'ggs', 'zzz']) == 0
    assert candidate(strs = ['ghi', 'def', 'abc']) == 0
    assert candidate(strs = ['aaa', 'bbb', 'ccc']) == 0
    assert candidate(strs = ['abc', 'bcd', 'cde']) == 0
    assert candidate(strs = ['abc', 'abc', 'abc']) == 0
    assert candidate(strs = ['a', 'b', 'c', 'd']) == 0
    assert candidate(strs = ['abcdef', 'uvwxyz']) == 0
    assert candidate(strs = ['zzz', 'aaa', 'zzz']) == 0
    assert candidate(strs = ['zyx', 'wvu', 'tsr']) == 2
    assert candidate(strs = ['edcba']) == 4
    assert candidate(strs = ['abcd', 'abdc', 'acdb']) == 1
    assert candidate(strs = ['abcd', 'dbca', 'adcb', 'cbad']) == 3
    assert candidate(strs = ['babca', 'bbazb']) == 3
    assert candidate(strs = ['a', 'b', 'c']) == 0
    assert candidate(strs = ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzabcd']) == 2
    assert candidate(strs = ['abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij']) == 0
    assert candidate(strs = ['fedcb', 'edcba', 'dcbae', 'cbade', 'baced', 'acbed']) == 4
    assert candidate(strs = ['zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba']) == 25
    assert candidate(strs = ['abcd', 'adbc', 'bacd', 'bdac']) == 2
    assert candidate(strs = ['abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij']) == 0
    assert candidate(strs = ['abacabad', 'babacaba', 'cacabada', 'dacabada']) == 5
    assert candidate(strs = ['abcdabcd', 'dcbaabcd', 'abcdabdc', 'abdcabcd', 'abcdcdab', 'cdabcdab', 'abcdabcd', 'cdababcd', 'abcdcdab', 'dcabcdab']) == 6
    assert candidate(strs = ['abcdefgh', 'hgfedcba', 'abcdefgh', 'hgfedcba', 'abcdefgh']) == 7
    assert candidate(strs = ['leetcode', 'leetcoed', 'leetcdeo', 'leetcodeo', 'leetcodeo', 'leetcodeo']) == 5
    assert candidate(strs = ['zyx', 'yxz', 'xyz']) == 2
    assert candidate(strs = ['aabbaa', 'abcabc', 'acbacb', 'bacbac', 'bbacab']) == 4
    assert candidate(strs = ['zzz', 'yyy', 'xxx', 'www', 'vvv', 'uuu']) == 0
    assert candidate(strs = ['abcdefgh', 'bcadegfh', 'cgdbefha', 'dgfbceha', 'egfdcbha', 'fgecadhb']) == 5
    assert candidate(strs = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklnmopqrstuvwxyz']) == 25
    assert candidate(strs = ['abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh']) == 0
    assert candidate(strs = ['zabc', 'zcad', 'zdba', 'zeac', 'zfcd', 'zgda', 'zhec', 'zida', 'zjea', 'zkcf']) == 3
    assert candidate(strs = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm']) == 0
    assert candidate(strs = ['azazaz', 'bababa', 'cacaca', 'dadada', 'eaeaea']) == 3
    assert candidate(strs = ['abcdefg', 'bcefgij', 'acdfhij']) == 0
    assert candidate(strs = ['abcd', 'abdc', 'acdb', 'cadb', 'dabc']) == 2
    assert candidate(strs = ['xyz', 'zyx', 'wvu', 'tsr', 'qpo', 'nml', 'kji', 'hgf', 'edc', 'baa']) == 2
    assert candidate(strs = ['aeg', 'bdh', 'cfi', 'egj', 'fhk', 'gjl']) == 0
    assert candidate(strs = ['qrst', 'mnop', 'ijkl', 'efgh', 'abcd', 'mnop', 'qrst', 'efgh', 'ijkl', 'abcd', 'mnop', 'qrst', 'efgh', 'ijkl', 'abcd', 'mnop', 'qrst', 'efgh', 'ijkl', 'abcd']) == 0
    assert candidate(strs = ['zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz']) == 0
    assert candidate(strs = ['zzzzzzzz', 'zzzzzzzy', 'zzzzzzzx', 'zzzzzzyx', 'zzzzzyxy', 'zzzzyxxy', 'zzzyxxyx', 'zzyxxyxy']) == 6
    assert candidate(strs = ['abcdefghij', 'abcdefghik', 'abcdefghij', 'abcdefghim', 'abcdefghin']) == 0
    assert candidate(strs = ['aabbcc', 'bbccaa', 'ccaabb', 'aabbbc']) == 4
    assert candidate(strs = ['abcdefg', 'bceghik', 'acegikm', 'adegimn']) == 0
    assert candidate(strs = ['qwertyuiop', 'asdfghjklz', 'zxcvbnmqwe', 'qwertyuiop', 'asdfghjklz']) == 7
    assert candidate(strs = ['qrst', 'rstu', 'stuv', 'tuvw', 'uvwx']) == 0
    assert candidate(strs = ['aabbccdd', 'bbaaccee', 'ccaabbee', 'ddeebbaa', 'eeccbbdd']) == 6
    assert candidate(strs = ['zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba']) == 25
    assert candidate(strs = ['zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz']) == 0
    assert candidate(strs = ['qwerty', 'wertyq', 'ertyqw', 'rtyqwe', 'tyqwer', 'yqwret']) == 5
    assert candidate(strs = ['cba', 'bca', 'bac', 'acb']) == 2
    assert candidate(strs = ['aebf', 'accf', 'bdgf', 'cddg', 'defh', 'edgh', 'feih', 'gjih', 'hkji']) == 2
    assert candidate(strs = ['aabbcc', 'bbaacc', 'ccabba', 'aababc', 'bbacab', 'abcabc', 'cbaabc', 'abacba', 'bacabc', 'cababc']) == 4
    assert candidate(strs = ['zyxwvu', 'utsrqpon', 'mlkjihgf', 'edcba']) == 5
    assert candidate(strs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == 0
    assert candidate(strs = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy']) == 0
    assert candidate(strs = ['cba', 'daf', 'gee']) == 2
    assert candidate(strs = ['abc', 'bac', 'cab', 'bca', 'cab', 'cba']) == 2
    assert candidate(strs = ['leetcode', 'leetcede', 'leotcede']) == 5
    assert candidate(strs = ['zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba']) == 25
    assert candidate(strs = ['zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz']) == 0
    assert candidate(strs = ['abcd', 'adcb', 'bacd', 'bdac', 'cabd', 'cdab', 'dcba', 'dcab', 'dabc', 'dacb']) == 3
    assert candidate(strs = ['zzzz', 'zzyz', 'zyyz', 'yzzz', 'yzyz', 'yyyz', 'yyyx', 'yyxx', 'yxxx', 'xxxx']) == 3
    assert candidate(strs = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yzab']) == 2
    assert candidate(strs = ['aabbcc', 'bbaacc', 'bbacac', 'aabcbc', 'cababc', 'bcbacc']) == 3
    assert candidate(strs = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']) == 0
    assert candidate(strs = ['xyz', 'zyx', 'yxz', 'xzy', 'yzx', 'zxy']) == 2
    assert candidate(strs = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'mnopqrstuvwxyzabcdefghijkl', 'fedcbazyxwvutsrqponmlkjihg']) == 25
    assert candidate(strs = ['mnopqr', 'opqrst', 'pqrstu', 'qrstuv']) == 0
    assert candidate(strs = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn']) == 0
    assert candidate(strs = ['abcd', 'dcba', 'abcd', 'dcba']) == 3
    assert candidate(strs = ['aabbcc', 'bbccaa', 'ccaabb', 'aabbbc', 'bbccaa', 'ccaabb', 'aabbbc']) == 4
    assert candidate(strs = ['abcdefg', 'gfedcba', 'bacdefg', 'ihgfedc', 'jklmnop']) == 6
    assert candidate(strs = ['pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']) == 0
    assert candidate(strs = ['qpwoeiruty', 'qpwoeiruty', 'qpwoeiruty']) == 5
    assert candidate(strs = ['mnop', 'qrst', 'uvwx', 'yzab', 'cdef', 'ghij', 'klmn', 'opqr', 'stuv', 'wxyz']) == 2
    assert candidate(strs = ['abcd', 'bcde', 'cdef', 'defg']) == 0
    assert candidate(strs = ['aabbcc', 'abbccc', 'abcccc', 'bcccdd', 'cccddd', 'ccdddd', 'cddddd', 'dddddd']) == 0
    assert candidate(strs = ['aabbccddeeff', 'abcdefabcdef', 'fedcbafedcba', 'abcdefabcdef', 'aabbccddeeff']) == 10
    assert candidate(strs = ['abcdefghij', 'jihgfedcba', 'abcdefghij', 'jihgfedcba', 'abcdefghij', 'jihgfedcba']) == 9
    assert candidate(strs = ['zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba']) == 25
    assert candidate(strs = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwx', 'vwxy', 'wxyz']) == 0
    assert candidate(strs = ['aabbcc', 'bbccdd', 'ccddeeff', 'ddeeffgg']) == 0
    assert candidate(strs = ['abcdabcd', 'bcdbcdcd', 'cdcdcdcd', 'dcdcdcdc', 'efefefef', 'fefefefe', 'gfefefef', 'hfhfhfhf', 'ihihihih']) == 5
    assert candidate(strs = ['xyzuvw', 'wvuxyz', 'uvwxyx', 'vxyzwu', 'uzwvxy', 'zwxyuv', 'yxwvuz', 'zyxuvw', 'wvuzxy', 'uvwxyx', 'vxyzwu', 'uzwvxy', 'zwxyuv', 'yxwvuz', 'zyxuvw', 'wvuzxy', 'uvwxyx', 'vxyzwu', 'uzwvxy', 'zwxyuv', 'yxwvuz', 'zyxuvw']) == 5
    assert candidate(strs = ['abcde', 'bcdef', 'cdefg', 'defgh', 'efghi', 'fghij', 'ghijk', 'hijkl', 'ijklm', 'jklmn']) == 0
    assert candidate(strs = ['zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz']) == 0
    assert candidate(strs = ['ba', 'ab', 'ba', 'ab', 'ba', 'ab']) == 1
    assert candidate(strs = ['zab', 'bac', 'cab', 'dcb']) == 2
    assert candidate(strs = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk']) == 4
    assert candidate(strs = ['abcdef', 'fedcba', 'dcbaef', 'bacfed', 'efabcd', 'fedcba']) == 5
    assert candidate(strs = ['aaaaaaaaaa', 'aabbaabbcc', 'aabbaabbcc', 'aabbaabbcc', 'aabbaabbcc', 'aabbaabbcc']) == 2
    assert candidate(strs = ['abcd', 'dcba', 'abcd', 'dcba', 'abcd']) == 3
    assert candidate(strs = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee', 'fffff', 'ggggg', 'hhhhh', 'iiiii', 'jjjjj']) == 0
    assert candidate(strs = ['aabb', 'bbaa', 'abab', 'baba', 'abba', 'baab']) == 3
    assert candidate(strs = ['abcd', 'abdc', 'acbd', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']) == 3
    assert candidate(strs = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk', 'pqrst', 'tsrqp', 'uvwxy', 'yxwvu', 'z', 'z', 'z', 'z', 'z']) == 4
    assert candidate(strs = ['abcd', 'efgh', 'ijkl', 'mnop']) == 0
    assert candidate(strs = ['abcdefg', 'gfedcba', 'hijklmn', 'nmolkji', 'opqrstu', 'utsrqpo']) == 6


