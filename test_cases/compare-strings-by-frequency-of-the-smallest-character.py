def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(queries = ['ccc'],words = ['a', 'bb', 'ccc', 'dddd']) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['ccc'],words = ['a', 'bb', 'ccc', 'dddd']) == [1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['a', 'b', 'c'],words = ['d', 'e', 'f', 'g']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['a', 'b', 'c'],words = ['d', 'e', 'f', 'g']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abc', 'def'],words = ['ghi', 'jkl']) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abc', 'def'],words = ['ghi', 'jkl']) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['zzz'],words = ['aaa', 'bbb', 'ccc']) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['zzz'],words = ['aaa', 'bbb', 'ccc']) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abc', 'bcd'],words = ['def', 'ghi']) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abc', 'bcd'],words = ['def', 'ghi']) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['aaa', 'bbb', 'ccc'],words = ['ddd', 'eee', 'fff']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['aaa', 'bbb', 'ccc'],words = ['ddd', 'eee', 'fff']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['a', 'aa', 'aaa'],words = ['b', 'bb', 'bbb', 'bbbb']) == [3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['a', 'aa', 'aaa'],words = ['b', 'bb', 'bbb', 'bbbb']) == [3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['cbd'],words = ['zaaaz']) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['cbd'],words = ['zaaaz']) == [1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['bbb', 'cc'],words = ['a', 'aa', 'aaa', 'aaaa']) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['bbb', 'cc'],words = ['a', 'aa', 'aaa', 'aaaa']) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['a'],words = ['b', 'c', 'd']) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['a'],words = ['b', 'c', 'd']) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abc', 'bcd'],words = ['cde', 'def', 'efg']) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abc', 'bcd'],words = ['cde', 'def', 'efg']) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['xyz'],words = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['xyz'],words = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['a', 'aa'],words = ['b', 'bb', 'bbb']) == [2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['a', 'aa'],words = ['b', 'bb', 'bbb']) == [2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['xyz'],words = ['abc', 'def', 'ghi']) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['xyz'],words = ['abc', 'def', 'ghi']) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],words = ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],words = ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['zz', 'zaz', 'zzz'],words = ['aaa', 'aa', 'a', 'aaaaa', 'aaaa', 'aaaab']) == [4, 5, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['zz', 'zaz', 'zzz'],words = ['aaa', 'aa', 'a', 'aaaaa', 'aaaa', 'aaaab']) == [4, 5, 3]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['aabbcc', 'ddeeff', 'gghhii'],words = ['jjkkll', 'mmnnoo', 'ppqqrr', 'ssttuu']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['aabbcc', 'ddeeff', 'gghhii'],words = ['jjkkll', 'mmnnoo', 'ppqqrr', 'ssttuu']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['aaa', 'aab', 'aac'],words = ['bbb', 'bbc', 'bba', 'abb', 'aba', 'aab']) == [0, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['aaa', 'aab', 'aac'],words = ['bbb', 'bbc', 'bba', 'abb', 'aba', 'aab']) == [0, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['ab', 'bc', 'cd'],words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['ab', 'bc', 'cd'],words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcd', 'dcba', 'abcd', 'dcba'],words = ['abcd', 'dcba', 'abcd', 'dcba', 'abcd', 'dcba']) == [0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcd', 'dcba', 'abcd', 'dcba'],words = ['abcd', 'dcba', 'abcd', 'dcba', 'abcd', 'dcba']) == [0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcd', 'abdc', 'acdb'],words = ['bcde', 'cdef', 'defg', 'efgh']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcd', 'abdc', 'acdb'],words = ['bcde', 'cdef', 'defg', 'efgh']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['aaaa', 'bbb', 'cc'],words = ['zzzz', 'zzz', 'zz', 'z']) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['aaaa', 'bbb', 'cc'],words = ['zzzz', 'zzz', 'zz', 'z']) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['a', 'b', 'c', 'd', 'e', 'f'],words = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['a', 'b', 'c', 'd', 'e', 'f'],words = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcdabcd', 'bcdbcd', 'cdcdcd'],words = ['ddd', 'dddd', 'ddddd']) == [3, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcdabcd', 'bcdbcd', 'cdcdcd'],words = ['ddd', 'dddd', 'ddddd']) == [3, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['a', 'a', 'a', 'a'],words = ['b', 'b', 'b', 'b']) == [0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['a', 'a', 'a', 'a'],words = ['b', 'b', 'b', 'b']) == [0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcde', 'bcdef', 'cdefg'],words = ['defgh', 'efghi', 'fghij', 'ghijk', 'hijkl', 'ijklm']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcde', 'bcdef', 'cdefg'],words = ['defgh', 'efghi', 'fghij', 'ghijk', 'hijkl', 'ijklm']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz'],words = ['zzzz', 'zzz', 'zz', 'z', 'a']) == [0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz'],words = ['zzzz', 'zzz', 'zz', 'z', 'a']) == [0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['hello', 'world'],words = ['python', 'java', 'csharp', 'ruby', 'swift']) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['hello', 'world'],words = ['python', 'java', 'csharp', 'ruby', 'swift']) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcd', 'ab', 'abc'],words = ['abcd', 'abc', 'ab', 'a']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcd', 'ab', 'abc'],words = ['abcd', 'abc', 'ab', 'a']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['x', 'xx', 'xxx', 'xxxx', 'xxxxx'],words = ['y', 'yy', 'yyy', 'yyyy', 'yyyyy', 'yyyyyy']) == [5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['x', 'xx', 'xxx', 'xxxx', 'xxxxx'],words = ['y', 'yy', 'yyy', 'yyyy', 'yyyyy', 'yyyyyy']) == [5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['xyxzyz', 'yzyzyx', 'zxzyxz'],words = ['zxyzxy', 'xyzxyz', 'yzxyzx', 'zyxzyz']) == [0, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['xyxzyz', 'yzyzyx', 'zxzyxz'],words = ['zxyzxy', 'xyzxyz', 'yzxyzx', 'zyxzyz']) == [0, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcdefghij', 'bcdefghijk', 'cdefghijkl'],words = ['defghijklm', 'efghijklmn', 'fghijklmno', 'ghijklmnop', 'hijklmnopq', 'ijklmnopqr']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcdefghij', 'bcdefghijk', 'cdefghijkl'],words = ['defghijklm', 'efghijklmn', 'fghijklmno', 'ghijklmnop', 'hijklmnopq', 'ijklmnopqr']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['xyz', 'xyzz', 'xyzzz'],words = ['wxyz', 'wwxyz', 'wwwxyz', 'wwwwxyz']) == [3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['xyz', 'xyzz', 'xyzzz'],words = ['wxyz', 'wwxyz', 'wwwxyz', 'wwwwxyz']) == [3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba'],words = ['qwertyuiopasdfghjklzxcvbnm', 'mnbvcxzasdfghjklpoiuytrewq']) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba'],words = ['qwertyuiopasdfghjklzxcvbnm', 'mnbvcxzasdfghjklpoiuytrewq']) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['zzzzzz', 'yyyyyy', 'xxxxxx'],words = ['wwwwww', 'vvvvvv', 'uuuuuu', 'tttttt']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['zzzzzz', 'yyyyyy', 'xxxxxx'],words = ['wwwwww', 'vvvvvv', 'uuuuuu', 'tttttt']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['aabbcc', 'bbccdd', 'ccddee', 'ddeeff', 'eeffgg'],words = ['ffgghh', 'gghhiijj', 'hhiijjkk', 'iijjkkll', 'jjkkllmm']) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['aabbcc', 'bbccdd', 'ccddee', 'ddeeff', 'eeffgg'],words = ['ffgghh', 'gghhiijj', 'hhiijjkk', 'iijjkkll', 'jjkkllmm']) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcdef', 'bcdefg', 'cdefgh'],words = ['defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcdef', 'bcdefg', 'cdefgh'],words = ['defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['zzz', 'zzzz'],words = ['aaaaa', 'aaa', 'aa', 'a']) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['zzz', 'zzzz'],words = ['aaaaa', 'aaa', 'aa', 'a']) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz']) == [5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz']) == [5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['zzzzz', 'zzzz', 'zzz', 'zz', 'z'],words = ['zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z', 'a']) == [1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['zzzzz', 'zzzz', 'zzz', 'zz', 'z'],words = ['zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z', 'a']) == [1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['zzz', 'zz', 'z'],words = ['aaa', 'aa', 'a', 'aaaa']) == [1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['zzz', 'zz', 'z'],words = ['aaa', 'aa', 'a', 'aaaa']) == [1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['aabbcc', 'bbaacc', 'ccaabb'],words = ['aabbb', 'bbccc', 'ccaaa', 'abcabc', 'aabbccaa']) == [2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['aabbcc', 'bbaacc', 'ccaabb'],words = ['aabbb', 'bbccc', 'ccaaa', 'abcabc', 'aabbccaa']) == [2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['aab', 'abb', 'abc'],words = ['aab', 'abb', 'abc', 'acc', 'bac', 'bca', 'cab', 'cba', 'cca']) == [0, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['aab', 'abb', 'abc'],words = ['aab', 'abb', 'abc', 'acc', 'bac', 'bca', 'cab', 'cba', 'cca']) == [0, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['aaaaab', 'aaaabb', 'aaabbb', 'aabbbb', 'abbbbb'],words = ['bbbbb', 'bbbb', 'bbb', 'bb', 'b']) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['aaaaab', 'aaaabb', 'aaabbb', 'aabbbb', 'abbbbb'],words = ['bbbbb', 'bbbb', 'bbb', 'bb', 'b']) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['apple', 'banana', 'cherry'],words = ['date', 'elderberry', 'fig', 'grape', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya']) == [2, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['apple', 'banana', 'cherry'],words = ['date', 'elderberry', 'fig', 'grape', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya']) == [2, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['apple', 'banana', 'cherry'],words = ['date', 'fig', 'grape', 'kiwi']) == [1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['apple', 'banana', 'cherry'],words = ['date', 'fig', 'grape', 'kiwi']) == [1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['aabbcc', 'bbaacc', 'ccaabb'],words = ['aabbc', 'bbccc', 'ccaab', 'aaabb', 'bbcca', 'ccaab']) == [1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['aabbcc', 'bbaacc', 'ccaabb'],words = ['aabbc', 'bbccc', 'ccaab', 'aaabb', 'bbcca', 'ccaab']) == [1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['apple', 'banana', 'cherry'],words = ['date', 'elderberry', 'fig', 'grape']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['apple', 'banana', 'cherry'],words = ['date', 'elderberry', 'fig', 'grape']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['zzzzz', 'zzzz', 'zzz', 'zz', 'z'],words = ['aaaaa', 'aaaa', 'aaa', 'aa', 'a']) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['zzzzz', 'zzzz', 'zzz', 'zz', 'z'],words = ['aaaaa', 'aaaa', 'aaa', 'aa', 'a']) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['mnopqr', 'nopqrs', 'opqrst'],words = ['pqrsqt', 'qrstuv', 'rstuvw', 'stuvwx', 'tuvwxy', 'uvwxyx']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['mnopqr', 'nopqrs', 'opqrst'],words = ['pqrsqt', 'qrstuv', 'rstuvw', 'stuvwx', 'tuvwxy', 'uvwxyx']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['zzz', 'yyy', 'xxx'],words = ['www', 'vvv', 'uuu', 'ttt', 'ss']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['zzz', 'yyy', 'xxx'],words = ['www', 'vvv', 'uuu', 'ttt', 'ss']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['aabbcc', 'bbccdd', 'ccddeeff'],words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['aabbcc', 'bbccdd', 'ccddeeff'],words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcd', 'abc', 'ab'],words = ['zzzz', 'zzz', 'zz', 'z']) == [3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcd', 'abc', 'ab'],words = ['zzzz', 'zzz', 'zz', 'z']) == [3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['aabbcc', 'bbccdd', 'ccddaa'],words = ['ddeeff', 'eeffgg', 'ffgghh']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['aabbcc', 'bbccdd', 'ccddaa'],words = ['ddeeff', 'eeffgg', 'ffgghh']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['aab', 'aabbb', 'aabbbb'],words = ['b', 'bb', 'bbb', 'bbbb', 'bbbbb', 'bbbbbb', 'bbbbbbb']) == [5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['aab', 'aabbb', 'aabbbb'],words = ['b', 'bb', 'bbb', 'bbbb', 'bbbbb', 'bbbbbb', 'bbbbbbb']) == [5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['leetcode', 'challenge', 'python'],words = ['programming', 'interview', 'solution', 'difficulty', 'easy', 'hard', 'medium']) == [1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['leetcode', 'challenge', 'python'],words = ['programming', 'interview', 'solution', 'difficulty', 'easy', 'hard', 'medium']) == [1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcd', 'abcde', 'abcdef'],words = ['bcdefg', 'cdefgh', 'defghi', 'efghij']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcd', 'abcde', 'abcdef'],words = ['bcdefg', 'cdefgh', 'defghi', 'efghij']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcd', 'abdc', 'adcb'],words = ['bcde', 'dcbe', 'debc', 'edcb']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcd', 'abdc', 'adcb'],words = ['bcde', 'dcbe', 'debc', 'edcb']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['mississippi', 'delaware', 'kentucky'],words = ['alabama', 'missouri', 'georgia', 'texas', 'california', 'arizona', 'wyoming']) == [0, 1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['mississippi', 'delaware', 'kentucky'],words = ['alabama', 'missouri', 'georgia', 'texas', 'california', 'arizona', 'wyoming']) == [0, 1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcdefg', 'hijklmn', 'opqrstu', 'vwxyzab'],words = ['cdefghi', 'defghij', 'efghijk', 'fghijkl', 'ghijklm']) == [0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcdefg', 'hijklmn', 'opqrstu', 'vwxyzab'],words = ['cdefghi', 'defghij', 'efghijk', 'fghijkl', 'ghijklm']) == [0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcdef', 'ghijkl', 'mnopqr'],words = ['stuvwx', 'yzabcd', 'efghij', 'klmnop', 'qrstuv']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcdef', 'ghijkl', 'mnopqr'],words = ['stuvwx', 'yzabcd', 'efghij', 'klmnop', 'qrstuv']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['apple', 'banana', 'cherry'],words = ['date', 'fig', 'grape', 'kiwi', 'lemon', 'mango']) == [1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['apple', 'banana', 'cherry'],words = ['date', 'fig', 'grape', 'kiwi', 'lemon', 'mango']) == [1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['hello', 'world'],words = ['python', 'java', 'c++', 'ruby']) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['hello', 'world'],words = ['python', 'java', 'c++', 'ruby']) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcd', 'abdc', 'aabc'],words = ['aaa', 'aaab', 'baaab', 'baaabbb']) == [4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcd', 'abdc', 'aabc'],words = ['aaa', 'aaab', 'baaab', 'baaabbb']) == [4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['a'],words = ['aaaaaaaaaab', 'aaaaaaaaaa', 'aaaaaaaaa', 'aaaaaaaa', 'aaaaaaa', 'aaaaaa', 'aaaaa', 'aaaa', 'aaa', 'aa', 'a']) == [10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['a'],words = ['aaaaaaaaaab', 'aaaaaaaaaa', 'aaaaaaaaa', 'aaaaaaaa', 'aaaaaaa', 'aaaaaa', 'aaaaa', 'aaaa', 'aaa', 'aa', 'a']) == [10]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['a', 'b', 'c', 'd', 'e', 'f'],words = ['g', 'h', 'i', 'j', 'k', 'l', 'm']) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['a', 'b', 'c', 'd', 'e', 'f'],words = ['g', 'h', 'i', 'j', 'k', 'l', 'm']) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['zzz', 'zzzz', 'zzzzz'],words = ['zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz']) == [4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['zzz', 'zzzz', 'zzzzz'],words = ['zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz']) == [4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z'],words = ['aaaaaa', 'aaaaa', 'aaaa', 'aaa', 'aa', 'a']) == [0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z'],words = ['aaaaaa', 'aaaaa', 'aaaa', 'aaa', 'aa', 'a']) == [0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcdef', 'bcdefg', 'cdefgh'],words = ['defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcdef', 'bcdefg', 'cdefgh'],words = ['defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['xylophone', 'guitar', 'piano'],words = ['flute', 'harmonica', 'trumpet', 'violin', 'cello', 'saxophone', 'trombone', 'tuba']) == [2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['xylophone', 'guitar', 'piano'],words = ['flute', 'harmonica', 'trumpet', 'violin', 'cello', 'saxophone', 'trombone', 'tuba']) == [2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['zz', 'yy', 'xx'],words = ['ww', 'vv', 'uu', 'tt', 'ss', 'rr', 'qq', 'pp', 'oo', 'nn']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['zz', 'yy', 'xx'],words = ['ww', 'vv', 'uu', 'tt', 'ss', 'rr', 'qq', 'pp', 'oo', 'nn']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcxyz', 'zzzz', 'uvw'],words = ['mnop', 'qrst', 'xyz', 'aabbcc']) == [1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcxyz', 'zzzz', 'uvw'],words = ['mnop', 'qrst', 'xyz', 'aabbcc']) == [1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['mnop', 'qrst', 'uvwx', 'yzab', 'cdef'],words = ['efgh', 'ghij', 'ijkl', 'klmn', 'lmno']) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['mnop', 'qrst', 'uvwx', 'yzab', 'cdef'],words = ['efgh', 'ghij', 'ijkl', 'klmn', 'lmno']) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['zzz', 'yyy', 'xxx'],words = ['www', 'vvv', 'uuu', 'ttt']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['zzz', 'yyy', 'xxx'],words = ['www', 'vvv', 'uuu', 'ttt']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['xyzz', 'zzyx', 'zzyy'],words = ['zzzz', 'zzyz', 'zyzz', 'zzzy', 'zyyz', 'zyzy', 'zyzz', 'zzzyz']) == [3, 3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['xyzz', 'zzyx', 'zzyy'],words = ['zzzz', 'zzyz', 'zyzz', 'zzzy', 'zyyz', 'zyzy', 'zyzz', 'zzzyz']) == [3, 3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['a', 'b', 'c', 'd', 'e'],words = ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['a', 'b', 'c', 'd', 'e'],words = ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['zzz', 'zzzz', 'zzzzz'],words = ['zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz', 'zzzzzzzzzz']) == [5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['zzz', 'zzzz', 'zzzzz'],words = ['zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz', 'zzzzzzzzzz']) == [5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['aaaaa', 'bbb', 'cccc'],words = ['ddd', 'eee', 'ffff', 'ggggg']) == [0, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['aaaaa', 'bbb', 'cccc'],words = ['ddd', 'eee', 'ffff', 'ggggg']) == [0, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['mnop', 'qrst', 'uvwx', 'yzab'],words = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yzab']) == [0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['mnop', 'qrst', 'uvwx', 'yzab'],words = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yzab']) == [0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcdabcd', 'abcdeabcde', 'abcdefabcdef'],words = ['bcdefgbcdefg', 'cdefghcdefgh', 'defghidefghi']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcdabcd', 'abcdeabcde', 'abcdefabcdef'],words = ['bcdefgbcdefg', 'cdefghcdefgh', 'defghidefghi']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['zzzz', 'yyyy', 'xxxx', 'wwww'],words = ['vvvv', 'uuuu', 'tttt', 'ssss', 'rrrr', 'qqqq', 'pppp', 'oooo', 'nnnn', 'mmmm']) == [0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['zzzz', 'yyyy', 'xxxx', 'wwww'],words = ['vvvv', 'uuuu', 'tttt', 'ssss', 'rrrr', 'qqqq', 'pppp', 'oooo', 'nnnn', 'mmmm']) == [0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['applepie', 'bananabread', 'cherrypie'],words = ['strawberry', 'blueberry', 'raspberry']) == [1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['applepie', 'bananabread', 'cherrypie'],words = ['strawberry', 'blueberry', 'raspberry']) == [1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcd', 'abcde', 'abcdef'],words = ['bcde', 'bcdef', 'bcdefg', 'bcdefgh', 'bcdefghi', 'bcdefghij']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcd', 'abcde', 'abcdef'],words = ['bcde', 'bcdef', 'bcdefg', 'bcdefgh', 'bcdefghi', 'bcdefghij']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['zzz', 'yyy', 'xxx'],words = ['www', 'vvv', 'uuu', 'ttt', 'sss']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['zzz', 'yyy', 'xxx'],words = ['www', 'vvv', 'uuu', 'ttt', 'sss']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abc', 'abcd', 'abcde', 'abcdef'],words = ['bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl']) == [0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abc', 'abcd', 'abcde', 'abcdef'],words = ['bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl']) == [0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['xyz', 'xyzz', 'xyzzz'],words = ['uvw', 'uvwv', 'uvwvv', 'uvwvvv', 'uvwvvvv', 'uvwvvvvv']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['xyz', 'xyzz', 'xyzzz'],words = ['uvw', 'uvwv', 'uvwvv', 'uvwvvv', 'uvwvvvv', 'uvwvvvvv']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['aabbcc', 'bbccdd', 'ccddee'],words = ['ddeeff', 'eeffgg', 'ffgghh', 'gghhii']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['aabbcc', 'bbccdd', 'ccddee'],words = ['ddeeff', 'eeffgg', 'ffgghh', 'gghhii']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['zzzzz', 'yyyyy', 'xxxxx'],words = ['wwwww', 'vvvvv', 'uuuuu', 'ttttt', 'sssss']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['zzzzz', 'yyyyy', 'xxxxx'],words = ['wwwww', 'vvvvv', 'uuuuu', 'ttttt', 'sssss']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcdefgh', 'hgfedcba', 'fedcbahg'],words = ['ghfedcba', 'ahgfedcb', 'bahgfedc', 'cbahgfed', 'dcbahegf', 'efgdcba', 'gfedcba', 'hgfedcb', 'abcdefgh']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcdefgh', 'hgfedcba', 'fedcbahg'],words = ['ghfedcba', 'ahgfedcb', 'bahgfedc', 'cbahgfed', 'dcbahegf', 'efgdcba', 'gfedcba', 'hgfedcb', 'abcdefgh']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcdabcd', 'bcdbcd', 'cdab'],words = ['ababcdabcd', 'bcdbcdabcd', 'cdababcd', 'abcdabcdabcd', 'bcdabcd', 'cdabcd', 'abcd']) == [2, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcdabcd', 'bcdbcd', 'cdab'],words = ['ababcdabcd', 'bcdbcdabcd', 'cdababcd', 'abcdabcdabcd', 'bcdabcd', 'cdabcd', 'abcd']) == [2, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['ab', 'abc', 'abcd'],words = ['bc', 'bcd', 'bcde', 'bcdef', 'bcdefg', 'bcdefgh']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['ab', 'abc', 'abcd'],words = ['bc', 'bcd', 'bcde', 'bcdef', 'bcdefg', 'bcdefgh']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['zzzzzzzzzz', 'zzzzzzzzz', 'zzzzzzzz', 'zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z'],words = ['aaaaaaaaaa', 'aaaaaaaaa', 'aaaaaaaa', 'aaaaaaa', 'aaaaaa', 'aaaaa', 'aaaa', 'aaa', 'aa', 'a']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['zzzzzzzzzz', 'zzzzzzzzz', 'zzzzzzzz', 'zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z'],words = ['aaaaaaaaaa', 'aaaaaaaaa', 'aaaaaaaa', 'aaaaaaa', 'aaaaaa', 'aaaaa', 'aaaa', 'aaa', 'aa', 'a']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['zz', 'yy', 'xx', 'ww', 'vv'],words = ['uu', 'tt', 'ss', 'rr', 'qq', 'pp', 'oo', 'nn', 'mm', 'll']) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['zz', 'yy', 'xx', 'ww', 'vv'],words = ['uu', 'tt', 'ss', 'rr', 'qq', 'pp', 'oo', 'nn', 'mm', 'll']) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['abcdef', 'ghijkl', 'mnopqr'],words = ['stuvwx', 'yzabcd', 'efghij', 'klmnop']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['abcdef', 'ghijkl', 'mnopqr'],words = ['stuvwx', 'yzabcd', 'efghij', 'klmnop']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['mmmmmm', 'nnnnnn', 'oooooo', 'pppppp'],words = ['qqqqqq', 'rrrrrr', 'ssssss', 'tttttt']) == [0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['mmmmmm', 'nnnnnn', 'oooooo', 'pppppp'],words = ['qqqqqq', 'rrrrrr', 'ssssss', 'tttttt']) == [0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['qwerty', 'asdfgh', 'zxcvbn'],words = ['poiuyt', 'lkjhgf', 'mnbvcx', 'tyuiop', 'ghjklcvbnm']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['qwerty', 'asdfgh', 'zxcvbn'],words = ['poiuyt', 'lkjhgf', 'mnbvcx', 'tyuiop', 'ghjklcvbnm']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['xyz', 'zyx', 'yxz'],words = ['qrs', 'rsq', 'srq']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['xyz', 'zyx', 'yxz'],words = ['qrs', 'rsq', 'srq']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['aaaaaaaa', 'bbbbbbbb', 'cccccccc'],words = ['dddddddd', 'eeeeeeee', 'ffffffff', 'gggggggg', 'hhhhhhhh', 'iiiiiiii', 'jjjjjjjj', 'kkkkkkkk', 'llllllll']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['aaaaaaaa', 'bbbbbbbb', 'cccccccc'],words = ['dddddddd', 'eeeeeeee', 'ffffffff', 'gggggggg', 'hhhhhhhh', 'iiiiiiii', 'jjjjjjjj', 'kkkkkkkk', 'llllllll']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['ab', 'bc', 'cd', 'de', 'ef'],words = ['zz', 'zy', 'yx', 'xw', 'vw', 'uv', 'tu', 'ts', 'sr', 'rq', 'qp', 'po', 'on', 'nm', 'ml', 'lk', 'kj', 'ji', 'ih', 'hg', 'gf', 'fe', 'ed', 'dc', 'cb', 'ba']) == [1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['ab', 'bc', 'cd', 'de', 'ef'],words = ['zz', 'zy', 'yx', 'xw', 'vw', 'uv', 'tu', 'ts', 'sr', 'rq', 'qp', 'po', 'on', 'nm', 'ml', 'lk', 'kj', 'ji', 'ih', 'hg', 'gf', 'fe', 'ed', 'dc', 'cb', 'ba']) == [1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(queries = ['apple', 'banana', 'cherry'],words = ['date', 'elderberry', 'fig', 'grape', 'honeydew']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = ['apple', 'banana', 'cherry'],words = ['date', 'elderberry', 'fig', 'grape', 'honeydew']) == [0, 0, 0]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(queries = ['ccc'],words = ['a', 'bb', 'ccc', 'dddd']) == [1]
    assert candidate(queries = ['a', 'b', 'c'],words = ['d', 'e', 'f', 'g']) == [0, 0, 0]
    assert candidate(queries = ['abc', 'def'],words = ['ghi', 'jkl']) == [0, 0]
    assert candidate(queries = ['zzz'],words = ['aaa', 'bbb', 'ccc']) == [0]
    assert candidate(queries = ['abc', 'bcd'],words = ['def', 'ghi']) == [0, 0]
    assert candidate(queries = ['aaa', 'bbb', 'ccc'],words = ['ddd', 'eee', 'fff']) == [0, 0, 0]
    assert candidate(queries = ['a', 'aa', 'aaa'],words = ['b', 'bb', 'bbb', 'bbbb']) == [3, 2, 1]
    assert candidate(queries = ['cbd'],words = ['zaaaz']) == [1]
    assert candidate(queries = ['bbb', 'cc'],words = ['a', 'aa', 'aaa', 'aaaa']) == [1, 2]
    assert candidate(queries = ['a'],words = ['b', 'c', 'd']) == [0]
    assert candidate(queries = ['abc', 'bcd'],words = ['cde', 'def', 'efg']) == [0, 0]
    assert candidate(queries = ['xyz'],words = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']) == [5]
    assert candidate(queries = ['a', 'aa'],words = ['b', 'bb', 'bbb']) == [2, 1]
    assert candidate(queries = ['xyz'],words = ['abc', 'def', 'ghi']) == [0]
    assert candidate(queries = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],words = ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(queries = ['zz', 'zaz', 'zzz'],words = ['aaa', 'aa', 'a', 'aaaaa', 'aaaa', 'aaaab']) == [4, 5, 3]
    assert candidate(queries = ['aabbcc', 'ddeeff', 'gghhii'],words = ['jjkkll', 'mmnnoo', 'ppqqrr', 'ssttuu']) == [0, 0, 0]
    assert candidate(queries = ['aaa', 'aab', 'aac'],words = ['bbb', 'bbc', 'bba', 'abb', 'aba', 'aab']) == [0, 1, 1]
    assert candidate(queries = ['ab', 'bc', 'cd'],words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']) == [0, 0, 0]
    assert candidate(queries = ['abcd', 'dcba', 'abcd', 'dcba'],words = ['abcd', 'dcba', 'abcd', 'dcba', 'abcd', 'dcba']) == [0, 0, 0, 0]
    assert candidate(queries = ['abcd', 'abdc', 'acdb'],words = ['bcde', 'cdef', 'defg', 'efgh']) == [0, 0, 0]
    assert candidate(queries = ['aaaa', 'bbb', 'cc'],words = ['zzzz', 'zzz', 'zz', 'z']) == [0, 1, 2]
    assert candidate(queries = ['a', 'b', 'c', 'd', 'e', 'f'],words = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']) == [0, 0, 0, 0, 0, 0]
    assert candidate(queries = ['abcdabcd', 'bcdbcd', 'cdcdcd'],words = ['ddd', 'dddd', 'ddddd']) == [3, 3, 2]
    assert candidate(queries = ['a', 'a', 'a', 'a'],words = ['b', 'b', 'b', 'b']) == [0, 0, 0, 0]
    assert candidate(queries = ['abcde', 'bcdef', 'cdefg'],words = ['defgh', 'efghi', 'fghij', 'ghijk', 'hijkl', 'ijklm']) == [0, 0, 0]
    assert candidate(queries = ['zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz'],words = ['zzzz', 'zzz', 'zz', 'z', 'a']) == [0, 0, 0, 0, 1]
    assert candidate(queries = ['hello', 'world'],words = ['python', 'java', 'csharp', 'ruby', 'swift']) == [1, 1]
    assert candidate(queries = ['abcd', 'ab', 'abc'],words = ['abcd', 'abc', 'ab', 'a']) == [0, 0, 0]
    assert candidate(queries = ['x', 'xx', 'xxx', 'xxxx', 'xxxxx'],words = ['y', 'yy', 'yyy', 'yyyy', 'yyyyy', 'yyyyyy']) == [5, 4, 3, 2, 1]
    assert candidate(queries = ['xyxzyz', 'yzyzyx', 'zxzyxz'],words = ['zxyzxy', 'xyzxyz', 'yzxyzx', 'zyxzyz']) == [0, 3, 0]
    assert candidate(queries = ['abcdefghij', 'bcdefghijk', 'cdefghijkl'],words = ['defghijklm', 'efghijklmn', 'fghijklmno', 'ghijklmnop', 'hijklmnopq', 'ijklmnopqr']) == [0, 0, 0]
    assert candidate(queries = ['xyz', 'xyzz', 'xyzzz'],words = ['wxyz', 'wwxyz', 'wwwxyz', 'wwwwxyz']) == [3, 3, 3]
    assert candidate(queries = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba'],words = ['qwertyuiopasdfghjklzxcvbnm', 'mnbvcxzasdfghjklpoiuytrewq']) == [0, 0]
    assert candidate(queries = ['zzzzzz', 'yyyyyy', 'xxxxxx'],words = ['wwwwww', 'vvvvvv', 'uuuuuu', 'tttttt']) == [0, 0, 0]
    assert candidate(queries = ['aabbcc', 'bbccdd', 'ccddee', 'ddeeff', 'eeffgg'],words = ['ffgghh', 'gghhiijj', 'hhiijjkk', 'iijjkkll', 'jjkkllmm']) == [0, 0, 0, 0, 0]
    assert candidate(queries = ['abcdef', 'bcdefg', 'cdefgh'],words = ['defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn']) == [0, 0, 0]
    assert candidate(queries = ['zzz', 'zzzz'],words = ['aaaaa', 'aaa', 'aa', 'a']) == [1, 1]
    assert candidate(queries = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz']) == [5, 4, 3, 2, 1]
    assert candidate(queries = ['zzzzz', 'zzzz', 'zzz', 'zz', 'z'],words = ['zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z', 'a']) == [1, 2, 3, 4, 5]
    assert candidate(queries = ['zzz', 'zz', 'z'],words = ['aaa', 'aa', 'a', 'aaaa']) == [1, 2, 3]
    assert candidate(queries = ['aabbcc', 'bbaacc', 'ccaabb'],words = ['aabbb', 'bbccc', 'ccaaa', 'abcabc', 'aabbccaa']) == [2, 2, 2]
    assert candidate(queries = ['aab', 'abb', 'abc'],words = ['aab', 'abb', 'abc', 'acc', 'bac', 'bca', 'cab', 'cba', 'cca']) == [0, 1, 1]
    assert candidate(queries = ['aaaaab', 'aaaabb', 'aaabbb', 'aabbbb', 'abbbbb'],words = ['bbbbb', 'bbbb', 'bbb', 'bb', 'b']) == [0, 1, 2, 3, 4]
    assert candidate(queries = ['apple', 'banana', 'cherry'],words = ['date', 'elderberry', 'fig', 'grape', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya']) == [2, 0, 2]
    assert candidate(queries = ['apple', 'banana', 'cherry'],words = ['date', 'fig', 'grape', 'kiwi']) == [1, 0, 1]
    assert candidate(queries = ['aabbcc', 'bbaacc', 'ccaabb'],words = ['aabbc', 'bbccc', 'ccaab', 'aaabb', 'bbcca', 'ccaab']) == [1, 1, 1]
    assert candidate(queries = ['apple', 'banana', 'cherry'],words = ['date', 'elderberry', 'fig', 'grape']) == [0, 0, 0]
    assert candidate(queries = ['zzzzz', 'zzzz', 'zzz', 'zz', 'z'],words = ['aaaaa', 'aaaa', 'aaa', 'aa', 'a']) == [0, 1, 2, 3, 4]
    assert candidate(queries = ['mnopqr', 'nopqrs', 'opqrst'],words = ['pqrsqt', 'qrstuv', 'rstuvw', 'stuvwx', 'tuvwxy', 'uvwxyx']) == [0, 0, 0]
    assert candidate(queries = ['zzz', 'yyy', 'xxx'],words = ['www', 'vvv', 'uuu', 'ttt', 'ss']) == [0, 0, 0]
    assert candidate(queries = ['aabbcc', 'bbccdd', 'ccddeeff'],words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij']) == [0, 0, 0]
    assert candidate(queries = ['abcd', 'abc', 'ab'],words = ['zzzz', 'zzz', 'zz', 'z']) == [3, 3, 3]
    assert candidate(queries = ['aabbcc', 'bbccdd', 'ccddaa'],words = ['ddeeff', 'eeffgg', 'ffgghh']) == [0, 0, 0]
    assert candidate(queries = ['aab', 'aabbb', 'aabbbb'],words = ['b', 'bb', 'bbb', 'bbbb', 'bbbbb', 'bbbbbb', 'bbbbbbb']) == [5, 5, 5]
    assert candidate(queries = ['leetcode', 'challenge', 'python'],words = ['programming', 'interview', 'solution', 'difficulty', 'easy', 'hard', 'medium']) == [1, 1, 1]
    assert candidate(queries = ['abcd', 'abcde', 'abcdef'],words = ['bcdefg', 'cdefgh', 'defghi', 'efghij']) == [0, 0, 0]
    assert candidate(queries = ['abcd', 'abdc', 'adcb'],words = ['bcde', 'dcbe', 'debc', 'edcb']) == [0, 0, 0]
    assert candidate(queries = ['mississippi', 'delaware', 'kentucky'],words = ['alabama', 'missouri', 'georgia', 'texas', 'california', 'arizona', 'wyoming']) == [0, 1, 4]
    assert candidate(queries = ['abcdefg', 'hijklmn', 'opqrstu', 'vwxyzab'],words = ['cdefghi', 'defghij', 'efghijk', 'fghijkl', 'ghijklm']) == [0, 0, 0, 0]
    assert candidate(queries = ['abcdef', 'ghijkl', 'mnopqr'],words = ['stuvwx', 'yzabcd', 'efghij', 'klmnop', 'qrstuv']) == [0, 0, 0]
    assert candidate(queries = ['apple', 'banana', 'cherry'],words = ['date', 'fig', 'grape', 'kiwi', 'lemon', 'mango']) == [1, 0, 1]
    assert candidate(queries = ['hello', 'world'],words = ['python', 'java', 'c++', 'ruby']) == [1, 1]
    assert candidate(queries = ['abcd', 'abdc', 'aabc'],words = ['aaa', 'aaab', 'baaab', 'baaabbb']) == [4, 4, 4]
    assert candidate(queries = ['a'],words = ['aaaaaaaaaab', 'aaaaaaaaaa', 'aaaaaaaaa', 'aaaaaaaa', 'aaaaaaa', 'aaaaaa', 'aaaaa', 'aaaa', 'aaa', 'aa', 'a']) == [10]
    assert candidate(queries = ['a', 'b', 'c', 'd', 'e', 'f'],words = ['g', 'h', 'i', 'j', 'k', 'l', 'm']) == [0, 0, 0, 0, 0, 0]
    assert candidate(queries = ['zzz', 'zzzz', 'zzzzz'],words = ['zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz']) == [4, 4, 4]
    assert candidate(queries = ['zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z'],words = ['aaaaaa', 'aaaaa', 'aaaa', 'aaa', 'aa', 'a']) == [0, 1, 2, 3, 4, 5]
    assert candidate(queries = ['abcdef', 'bcdefg', 'cdefgh'],words = ['defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm']) == [0, 0, 0]
    assert candidate(queries = ['xylophone', 'guitar', 'piano'],words = ['flute', 'harmonica', 'trumpet', 'violin', 'cello', 'saxophone', 'trombone', 'tuba']) == [2, 2, 2]
    assert candidate(queries = ['zz', 'yy', 'xx'],words = ['ww', 'vv', 'uu', 'tt', 'ss', 'rr', 'qq', 'pp', 'oo', 'nn']) == [0, 0, 0]
    assert candidate(queries = ['abcxyz', 'zzzz', 'uvw'],words = ['mnop', 'qrst', 'xyz', 'aabbcc']) == [1, 0, 1]
    assert candidate(queries = ['mnop', 'qrst', 'uvwx', 'yzab', 'cdef'],words = ['efgh', 'ghij', 'ijkl', 'klmn', 'lmno']) == [0, 0, 0, 0, 0]
    assert candidate(queries = ['zzz', 'yyy', 'xxx'],words = ['www', 'vvv', 'uuu', 'ttt']) == [0, 0, 0]
    assert candidate(queries = ['xyzz', 'zzyx', 'zzyy'],words = ['zzzz', 'zzyz', 'zyzz', 'zzzy', 'zyyz', 'zyzy', 'zyzz', 'zzzyz']) == [3, 3, 1]
    assert candidate(queries = ['a', 'b', 'c', 'd', 'e'],words = ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']) == [0, 0, 0, 0, 0]
    assert candidate(queries = ['zzz', 'zzzz', 'zzzzz'],words = ['zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz', 'zzzzzzzzzz']) == [5, 5, 5]
    assert candidate(queries = ['aaaaa', 'bbb', 'cccc'],words = ['ddd', 'eee', 'ffff', 'ggggg']) == [0, 2, 1]
    assert candidate(queries = ['mnop', 'qrst', 'uvwx', 'yzab'],words = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yzab']) == [0, 0, 0, 0]
    assert candidate(queries = ['abcdabcd', 'abcdeabcde', 'abcdefabcdef'],words = ['bcdefgbcdefg', 'cdefghcdefgh', 'defghidefghi']) == [0, 0, 0]
    assert candidate(queries = ['zzzz', 'yyyy', 'xxxx', 'wwww'],words = ['vvvv', 'uuuu', 'tttt', 'ssss', 'rrrr', 'qqqq', 'pppp', 'oooo', 'nnnn', 'mmmm']) == [0, 0, 0, 0]
    assert candidate(queries = ['applepie', 'bananabread', 'cherrypie'],words = ['strawberry', 'blueberry', 'raspberry']) == [1, 0, 1]
    assert candidate(queries = ['abcd', 'abcde', 'abcdef'],words = ['bcde', 'bcdef', 'bcdefg', 'bcdefgh', 'bcdefghi', 'bcdefghij']) == [0, 0, 0]
    assert candidate(queries = ['zzz', 'yyy', 'xxx'],words = ['www', 'vvv', 'uuu', 'ttt', 'sss']) == [0, 0, 0]
    assert candidate(queries = ['abc', 'abcd', 'abcde', 'abcdef'],words = ['bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl']) == [0, 0, 0, 0]
    assert candidate(queries = ['xyz', 'xyzz', 'xyzzz'],words = ['uvw', 'uvwv', 'uvwvv', 'uvwvvv', 'uvwvvvv', 'uvwvvvvv']) == [0, 0, 0]
    assert candidate(queries = ['aabbcc', 'bbccdd', 'ccddee'],words = ['ddeeff', 'eeffgg', 'ffgghh', 'gghhii']) == [0, 0, 0]
    assert candidate(queries = ['zzzzz', 'yyyyy', 'xxxxx'],words = ['wwwww', 'vvvvv', 'uuuuu', 'ttttt', 'sssss']) == [0, 0, 0]
    assert candidate(queries = ['abcdefgh', 'hgfedcba', 'fedcbahg'],words = ['ghfedcba', 'ahgfedcb', 'bahgfedc', 'cbahgfed', 'dcbahegf', 'efgdcba', 'gfedcba', 'hgfedcb', 'abcdefgh']) == [0, 0, 0]
    assert candidate(queries = ['abcdabcd', 'bcdbcd', 'cdab'],words = ['ababcdabcd', 'bcdbcdabcd', 'cdababcd', 'abcdabcdabcd', 'bcdabcd', 'cdabcd', 'abcd']) == [2, 2, 3]
    assert candidate(queries = ['ab', 'abc', 'abcd'],words = ['bc', 'bcd', 'bcde', 'bcdef', 'bcdefg', 'bcdefgh']) == [0, 0, 0]
    assert candidate(queries = ['zzzzzzzzzz', 'zzzzzzzzz', 'zzzzzzzz', 'zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z'],words = ['aaaaaaaaaa', 'aaaaaaaaa', 'aaaaaaaa', 'aaaaaaa', 'aaaaaa', 'aaaaa', 'aaaa', 'aaa', 'aa', 'a']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(queries = ['zz', 'yy', 'xx', 'ww', 'vv'],words = ['uu', 'tt', 'ss', 'rr', 'qq', 'pp', 'oo', 'nn', 'mm', 'll']) == [0, 0, 0, 0, 0]
    assert candidate(queries = ['abcdef', 'ghijkl', 'mnopqr'],words = ['stuvwx', 'yzabcd', 'efghij', 'klmnop']) == [0, 0, 0]
    assert candidate(queries = ['mmmmmm', 'nnnnnn', 'oooooo', 'pppppp'],words = ['qqqqqq', 'rrrrrr', 'ssssss', 'tttttt']) == [0, 0, 0, 0]
    assert candidate(queries = ['qwerty', 'asdfgh', 'zxcvbn'],words = ['poiuyt', 'lkjhgf', 'mnbvcx', 'tyuiop', 'ghjklcvbnm']) == [0, 0, 0]
    assert candidate(queries = ['xyz', 'zyx', 'yxz'],words = ['qrs', 'rsq', 'srq']) == [0, 0, 0]
    assert candidate(queries = ['aaaaaaaa', 'bbbbbbbb', 'cccccccc'],words = ['dddddddd', 'eeeeeeee', 'ffffffff', 'gggggggg', 'hhhhhhhh', 'iiiiiiii', 'jjjjjjjj', 'kkkkkkkk', 'llllllll']) == [0, 0, 0]
    assert candidate(queries = ['ab', 'bc', 'cd', 'de', 'ef'],words = ['zz', 'zy', 'yx', 'xw', 'vw', 'uv', 'tu', 'ts', 'sr', 'rq', 'qp', 'po', 'on', 'nm', 'ml', 'lk', 'kj', 'ji', 'ih', 'hg', 'gf', 'fe', 'ed', 'dc', 'cb', 'ba']) == [1, 1, 1, 1, 1]
    assert candidate(queries = ['apple', 'banana', 'cherry'],words = ['date', 'elderberry', 'fig', 'grape', 'honeydew']) == [0, 0, 0]


