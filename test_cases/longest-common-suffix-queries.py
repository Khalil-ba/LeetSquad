def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(wordsContainer = ['banana', 'mango', 'papaya'],wordsQuery = ['ana', 'ango', 'aya']) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['banana', 'mango', 'papaya'],wordsQuery = ['ana', 'ango', 'aya']) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcde', 'bcde', 'cde', 'de', 'e'],wordsQuery = ['cde', 'de', 'e', 'a', 'b']) == [2, 3, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcde', 'bcde', 'cde', 'de', 'e'],wordsQuery = ['cde', 'de', 'e', 'a', 'b']) == [2, 3, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['xyz', 'zyx', 'zxy'],wordsQuery = ['x', 'y', 'z']) == [1, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['xyz', 'zyx', 'zxy'],wordsQuery = ['x', 'y', 'z']) == [1, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['zzzzz', 'zzzz', 'zzz', 'zz', 'z'],wordsQuery = ['zzzz', 'zzz', 'zz', 'z', 'a']) == [1, 2, 3, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['zzzzz', 'zzzz', 'zzz', 'zz', 'z'],wordsQuery = ['zzzz', 'zzz', 'zz', 'z', 'a']) == [1, 2, 3, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['a', 'ab', 'abc'],wordsQuery = ['a', 'ab', 'abc']) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['a', 'ab', 'abc'],wordsQuery = ['a', 'ab', 'abc']) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['unique', 'suffix', 'words'],wordsQuery = ['fix', 'ffix', 'uffix']) == [1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['unique', 'suffix', 'words'],wordsQuery = ['fix', 'ffix', 'uffix']) == [1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcd', 'bcd', 'xbcd'],wordsQuery = ['cd', 'bcd', 'xyz']) == [1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcd', 'bcd', 'xbcd'],wordsQuery = ['cd', 'bcd', 'xyz']) == [1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['hello', 'world', 'python'],wordsQuery = ['lo', 'rld', 'on']) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['hello', 'world', 'python'],wordsQuery = ['lo', 'rld', 'on']) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['a', 'b', 'c'],wordsQuery = ['d', 'e', 'f']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['a', 'b', 'c'],wordsQuery = ['d', 'e', 'f']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcdefgh', 'poiuygh', 'ghghgh'],wordsQuery = ['gh', 'acbfgh', 'acbfegh']) == [2, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcdefgh', 'poiuygh', 'ghghgh'],wordsQuery = ['gh', 'acbfgh', 'acbfegh']) == [2, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcde', 'bcde', 'cde'],wordsQuery = ['cde', 'de', 'e']) == [2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcde', 'bcde', 'cde'],wordsQuery = ['cde', 'de', 'e']) == [2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['same', 'same', 'same'],wordsQuery = ['same', 'same', 'same']) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['same', 'same', 'same'],wordsQuery = ['same', 'same', 'same']) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['longestword', 'short', 'word'],wordsQuery = ['word', 'short', 'longestword']) == [2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['longestword', 'short', 'word'],wordsQuery = ['word', 'short', 'longestword']) == [2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['apple', 'maple', 'orange'],wordsQuery = ['le', 'ple', 'range']) == [0, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['apple', 'maple', 'orange'],wordsQuery = ['le', 'ple', 'range']) == [0, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['a', 'b', 'c'],wordsQuery = ['a', 'b', 'c']) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['a', 'b', 'c'],wordsQuery = ['a', 'b', 'c']) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abc', 'def', 'ghi'],wordsQuery = ['abc', 'def', 'ghi']) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abc', 'def', 'ghi'],wordsQuery = ['abc', 'def', 'ghi']) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['a', 'b', 'c', 'd'],wordsQuery = ['a', 'b', 'c', 'd']) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['a', 'b', 'c', 'd'],wordsQuery = ['a', 'b', 'c', 'd']) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['aaaaa', 'bbbbb', 'ccccc', 'abcde', 'bcdef', 'cdefg'],wordsQuery = ['abcde', 'bcdef', 'cdefg', 'de', 'ef', 'f']) == [3, 4, 5, 3, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['aaaaa', 'bbbbb', 'ccccc', 'abcde', 'bcdef', 'cdefg'],wordsQuery = ['abcde', 'bcdef', 'cdefg', 'de', 'ef', 'f']) == [3, 4, 5, 3, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcdef', 'defabc', 'abc', 'def', 'efg', 'fg', 'g'],wordsQuery = ['abc', 'def', 'efg', 'fg', 'g', 'a', 'bcd', 'cde']) == [2, 3, 4, 5, 6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcdef', 'defabc', 'abc', 'def', 'efg', 'fg', 'g'],wordsQuery = ['abc', 'def', 'efg', 'fg', 'g', 'a', 'bcd', 'cde']) == [2, 3, 4, 5, 6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcdefghijk', 'ghijklmno', 'ijklmnopq', 'jklmnopqr', 'klmnopqrs', 'lmnopqrst'],wordsQuery = ['ijkl', 'mnop', 'nopq', 'opqr', 'pqrs', 'qrstu', 'rstuv', 'stuvw', 'tuvwx', 'uvwxy', 'vwxyz', 'wxyz', 'xyz', 'yz', 'z']) == [1, 1, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcdefghijk', 'ghijklmno', 'ijklmnopq', 'jklmnopqr', 'klmnopqrs', 'lmnopqrst'],wordsQuery = ['ijkl', 'mnop', 'nopq', 'opqr', 'pqrs', 'qrstu', 'rstuv', 'stuvw', 'tuvwx', 'uvwxy', 'vwxyz', 'wxyz', 'xyz', 'yz', 'z']) == [1, 1, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['aabbcc', 'bbcc', 'bcc', 'cc', 'c', 'aabbccdd', 'bbccdd', 'bccdd', 'ccdd', 'cdd', 'dd', 'd'],wordsQuery = ['cc', 'dd', 'cdd', 'bcc', 'bbcc', 'aabbcc', 'xyz', 'abc', 'd', 'ccdd', 'aabbccdd']) == [3, 10, 9, 2, 1, 0, 4, 4, 11, 8, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['aabbcc', 'bbcc', 'bcc', 'cc', 'c', 'aabbccdd', 'bbccdd', 'bccdd', 'ccdd', 'cdd', 'dd', 'd'],wordsQuery = ['cc', 'dd', 'cdd', 'bcc', 'bbcc', 'aabbcc', 'xyz', 'abc', 'd', 'ccdd', 'aabbccdd']) == [3, 10, 9, 2, 1, 0, 4, 4, 11, 8, 5]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['zzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzz', 'zzzzzzzzzzzzz', 'zzzzzzzzzzzz', 'zzzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzz', 'zzzzzzzz', 'zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z', ''],wordsQuery = ['zzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzz', 'zzzzzzzzzzzzz', 'zzzzzzzzzzzz', 'zzzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzz', 'zzzzzzzz', 'zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['zzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzz', 'zzzzzzzzzzzzz', 'zzzzzzzzzzzz', 'zzzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzz', 'zzzzzzzz', 'zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z', ''],wordsQuery = ['zzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzz', 'zzzzzzzzzzzzz', 'zzzzzzzzzzzz', 'zzzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzz', 'zzzzzzzz', 'zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 15]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['aaaaa', 'aaabaaa', 'aaacaaa', 'aaad', 'aa', 'a', 'aaeaaa'],wordsQuery = ['aa', 'aaa', 'aaaa', 'aaaaa', 'aaab', 'aaac', 'aaad', 'aae']) == [4, 0, 0, 0, 5, 5, 3, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['aaaaa', 'aaabaaa', 'aaacaaa', 'aaad', 'aa', 'a', 'aaeaaa'],wordsQuery = ['aa', 'aaa', 'aaaa', 'aaaaa', 'aaab', 'aaac', 'aaad', 'aae']) == [4, 0, 0, 0, 5, 5, 3, 5]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['apple', 'pple', 'ple', 'le', 'e', 'orange', 'range', 'ange', 'nge', 'ge', 'e'],wordsQuery = ['ple', 'le', 'e', 'apple', 'orange', 'range', 'nge', 'ge']) == [2, 3, 4, 0, 5, 6, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['apple', 'pple', 'ple', 'le', 'e', 'orange', 'range', 'ange', 'nge', 'ge', 'e'],wordsQuery = ['ple', 'le', 'e', 'apple', 'orange', 'range', 'nge', 'ge']) == [2, 3, 4, 0, 5, 6, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcd', 'bcd', 'cd', 'd', ''],wordsQuery = ['abcd', 'bcd', 'cd', 'd', '', 'a', 'b', 'c']) == [0, 1, 2, 3, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcd', 'bcd', 'cd', 'd', ''],wordsQuery = ['abcd', 'bcd', 'cd', 'd', '', 'a', 'b', 'c']) == [0, 1, 2, 3, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['ababab', 'bababa', 'abab', 'bab', 'ab', 'b', 'a'],wordsQuery = ['ab', 'bab', 'abab', 'bababa', 'ababab', 'ba', 'a']) == [4, 3, 2, 1, 0, 1, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['ababab', 'bababa', 'abab', 'bab', 'ab', 'b', 'a'],wordsQuery = ['ab', 'bab', 'abab', 'bababa', 'ababab', 'ba', 'a']) == [4, 3, 2, 1, 0, 1, 6]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['longestword', 'longest', 'long', 'lo', 'l'],wordsQuery = ['word', 'st', 'ng', 'g', 'o', 'wordd', 'ngggg']) == [0, 1, 2, 2, 3, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['longestword', 'longest', 'long', 'lo', 'l'],wordsQuery = ['word', 'st', 'ng', 'g', 'o', 'wordd', 'ngggg']) == [0, 1, 2, 2, 3, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcd', 'bcd', 'bcd', 'cd', 'cd', 'd'],wordsQuery = ['cd', 'bcd', 'd', 'a', 'ab', 'abcd']) == [3, 1, 5, 5, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcd', 'bcd', 'bcd', 'cd', 'cd', 'd'],wordsQuery = ['cd', 'bcd', 'd', 'a', 'ab', 'abcd']) == [3, 1, 5, 5, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],wordsQuery = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa']) == [0, 1, 2, 3, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],wordsQuery = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa']) == [0, 1, 2, 3, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['prefix', 'prefixx', 'prefixxx', 'prefixxxx'],wordsQuery = ['fix', 'xfix', 'xxfix', 'xxxfix', 'xxxxfix', 'prefix']) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['prefix', 'prefixx', 'prefixxx', 'prefixxxx'],wordsQuery = ['fix', 'xfix', 'xxfix', 'xxxfix', 'xxxxfix', 'prefix']) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcd', 'bcd', 'cd', 'd', 'abcdabcd', 'bcdbcd', 'cdcd', 'dd', 'abcdabcde'],wordsQuery = ['abcd', 'bcd', 'cd', 'd', 'abcdabcd', 'bcdbcd', 'cdcd', 'dd', 'e', 'abcdabcde', 'de', 'cde', 'bcde']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcd', 'bcd', 'cd', 'd', 'abcdabcd', 'bcdbcd', 'cdcd', 'dd', 'abcdabcde'],wordsQuery = ['abcd', 'bcd', 'cd', 'd', 'abcdabcd', 'bcdbcd', 'cdcd', 'dd', 'e', 'abcdabcde', 'de', 'cde', 'bcde']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcdexyz', 'bcdexyz', 'cdexyz', 'dexyz', 'exyz', 'xyz'],wordsQuery = ['xyz', 'exyz', 'dexyz', 'cdexyz', 'bcdexyz', 'abcdexyz', 'z']) == [5, 4, 3, 2, 1, 0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcdexyz', 'bcdexyz', 'cdexyz', 'dexyz', 'exyz', 'xyz'],wordsQuery = ['xyz', 'exyz', 'dexyz', 'cdexyz', 'bcdexyz', 'abcdexyz', 'z']) == [5, 4, 3, 2, 1, 0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcdexyz', 'bcdexyz', 'xbcdexyz', 'abcdexyz'],wordsQuery = ['cdexyz', 'bcdexyz', 'xyz', 'abcdexyz']) == [1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcdexyz', 'bcdexyz', 'xbcdexyz', 'abcdexyz'],wordsQuery = ['cdexyz', 'bcdexyz', 'xyz', 'abcdexyz']) == [1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['hello', 'world', 'hello_world', 'world_hello', 'hold', 'old', 'ld', 'd'],wordsQuery = ['hello', 'world', 'hello_world', 'hold', 'old', 'ld', 'd', 'o']) == [0, 1, 2, 4, 5, 6, 7, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['hello', 'world', 'hello_world', 'world_hello', 'hold', 'old', 'ld', 'd'],wordsQuery = ['hello', 'world', 'hello_world', 'hold', 'old', 'ld', 'd', 'o']) == [0, 1, 2, 4, 5, 6, 7, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['apple', 'orange', 'banana', 'grape', 'pineapple'],wordsQuery = ['apple', 'orange', 'banana', 'grape', 'pineapple', 'pe', 'e']) == [0, 1, 2, 3, 4, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['apple', 'orange', 'banana', 'grape', 'pineapple'],wordsQuery = ['apple', 'orange', 'banana', 'grape', 'pineapple', 'pe', 'e']) == [0, 1, 2, 3, 4, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['xyz', 'yz', 'z', 'wxyz', 'vwxyz'],wordsQuery = ['z', 'yz', 'xyz', 'wxyz', 'vwxyz', 'wxyzz']) == [2, 1, 0, 3, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['xyz', 'yz', 'z', 'wxyz', 'vwxyz'],wordsQuery = ['z', 'yz', 'xyz', 'wxyz', 'vwxyz', 'wxyzz']) == [2, 1, 0, 3, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['aaaa', 'aaab', 'aaac', 'aaba', 'aabb', 'aabc', 'aaca', 'aacc', 'abaa', 'abab', 'abac', 'abba', 'abbb', 'abbc', 'abca', 'abcb', 'abcc', 'acaa', 'acab', 'acac', 'acba', 'acbb', 'acbc', 'acca', 'accb', 'accc'],wordsQuery = ['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acc', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc', 'a', 'b', 'c', 'aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6, 15, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['aaaa', 'aaab', 'aaac', 'aaba', 'aabb', 'aabc', 'aaca', 'aacc', 'abaa', 'abab', 'abac', 'abba', 'abbb', 'abbc', 'abca', 'abcb', 'abcc', 'acaa', 'acab', 'acac', 'acba', 'acbb', 'acbc', 'acca', 'accb', 'accc'],wordsQuery = ['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acc', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc', 'a', 'b', 'c', 'aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6, 15, 7]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['example', 'samples', 'examples', 'sampless'],wordsQuery = ['ple', 'les', 'ample', 'sample', 'samples', 'examples', 'sampless']) == [0, 1, 0, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['example', 'samples', 'examples', 'sampless'],wordsQuery = ['ple', 'les', 'ample', 'sample', 'samples', 'examples', 'sampless']) == [0, 1, 0, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcdefghij', 'abcdefghijk', 'abcdefgh', 'abcdefg', 'abcde', 'abcd'],wordsQuery = ['defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl']) == [3, 2, 5, 0, 1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcdefghij', 'abcdefghijk', 'abcdefgh', 'abcdefg', 'abcde', 'abcd'],wordsQuery = ['defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl']) == [3, 2, 5, 0, 1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcdefghij', 'bcdefghij', 'cdefghij', 'defghij', 'efghij', 'fghij', 'ghij', 'hij', 'ij', 'j'],wordsQuery = ['ghij', 'hij', 'ij', 'j', 'k', 'abcdefghij', 'bcdefghij', 'cdefghij', 'defghij']) == [6, 7, 8, 9, 9, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcdefghij', 'bcdefghij', 'cdefghij', 'defghij', 'efghij', 'fghij', 'ghij', 'hij', 'ij', 'j'],wordsQuery = ['ghij', 'hij', 'ij', 'j', 'k', 'abcdefghij', 'bcdefghij', 'cdefghij', 'defghij']) == [6, 7, 8, 9, 9, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['aabbcc', 'bbaacc', 'ccaabb', 'aabb', 'bbaa', 'ccaac', 'aac', 'ac', 'c'],wordsQuery = ['aabbcc', 'bbaacc', 'ccaabb', 'aabb', 'bbaa', 'ccaac', 'aac', 'ac', 'c', 'aa', 'bb', 'cc']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 4, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['aabbcc', 'bbaacc', 'ccaabb', 'aabb', 'bbaa', 'ccaac', 'aac', 'ac', 'c'],wordsQuery = ['aabbcc', 'bbaacc', 'ccaabb', 'aabb', 'bbaa', 'ccaac', 'aac', 'ac', 'c', 'aa', 'bb', 'cc']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 4, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],wordsQuery = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],wordsQuery = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['banana', 'anana', 'nana', 'ana', 'na', 'a'],wordsQuery = ['ana', 'na', 'a', 'anana', 'nana', 'banana', 'bana', 'ananaa']) == [3, 4, 5, 1, 2, 0, 3, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['banana', 'anana', 'nana', 'ana', 'na', 'a'],wordsQuery = ['ana', 'na', 'a', 'anana', 'nana', 'banana', 'bana', 'ananaa']) == [3, 4, 5, 1, 2, 0, 3, 5]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcdefg', 'defg', 'efg', 'fg', 'g'],wordsQuery = ['defg', 'efg', 'fg', 'g', 'abcdefg']) == [1, 2, 3, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcdefg', 'defg', 'efg', 'fg', 'g'],wordsQuery = ['defg', 'efg', 'fg', 'g', 'abcdefg']) == [1, 2, 3, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['repeated', 'repeatedword', 'repeat', 'rep', 're', 'r'],wordsQuery = ['repeated', 'repeatedword', 'repeat', 'rep', 're', 'r', 'ed', 'at', 't', 'e', '']) == [0, 1, 2, 3, 4, 5, 0, 2, 2, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['repeated', 'repeatedword', 'repeat', 'rep', 're', 'r'],wordsQuery = ['repeated', 'repeatedword', 'repeat', 'rep', 're', 'r', 'ed', 'at', 't', 'e', '']) == [0, 1, 2, 3, 4, 5, 0, 2, 2, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['suffix', 'fix', 'suffixfix', 'suffixsuffix', 'ffix', 'fixfix', 'suffixfixfix'],wordsQuery = ['suffix', 'fix', 'suffixfix', 'suffixsuffix', 'ffix', 'fixfix', 'suffixfixfix', 'ff', 'ix', 'x']) == [0, 1, 2, 3, 4, 5, 6, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['suffix', 'fix', 'suffixfix', 'suffixsuffix', 'ffix', 'fixfix', 'suffixfixfix'],wordsQuery = ['suffix', 'fix', 'suffixfix', 'suffixsuffix', 'ffix', 'fixfix', 'suffixfixfix', 'ff', 'ix', 'x']) == [0, 1, 2, 3, 4, 5, 6, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijk', 'lmnopqr', 'stuvwxyz'],wordsQuery = ['mnopqr', 'lmnopqr', 'stuv', 'xyz', 'pqrs']) == [3, 3, 3, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijk', 'lmnopqr', 'stuvwxyz'],wordsQuery = ['mnopqr', 'lmnopqr', 'stuv', 'xyz', 'pqrs']) == [3, 3, 3, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['unique', 'uniq', 'un', 'u'],wordsQuery = ['ue', 'iq', 'n', 'u', 'uniq', 'unique', 'nique']) == [0, 1, 2, 3, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['unique', 'uniq', 'un', 'u'],wordsQuery = ['ue', 'iq', 'n', 'u', 'uniq', 'unique', 'nique']) == [0, 1, 2, 3, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['short', 'shorter', 'shortest', 'shortestest'],wordsQuery = ['est', 'test', 'st', 'rtest', 'shortestestest', 'shorter', 'shortest']) == [2, 2, 2, 2, 3, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['short', 'shorter', 'shortest', 'shortestest'],wordsQuery = ['est', 'test', 'st', 'rtest', 'shortestestest', 'shorter', 'shortest']) == [2, 2, 2, 2, 3, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['hello', 'world', 'programming', 'worldwide', 'program'],wordsQuery = ['gram', 'ing', 'world', 'hello', 'pro', 'gramming']) == [4, 2, 1, 0, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['hello', 'world', 'programming', 'worldwide', 'program'],wordsQuery = ['gram', 'ing', 'world', 'hello', 'pro', 'gramming']) == [4, 2, 1, 0, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['suffix', 'prefix', 'suffixprefix', 'prefixsuffix'],wordsQuery = ['fix', 'fixx', 'suffix', 'prefix', 'uffix', 'frefix', 'sufix']) == [0, 0, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['suffix', 'prefix', 'suffixprefix', 'prefixsuffix'],wordsQuery = ['fix', 'fixx', 'suffix', 'prefix', 'uffix', 'frefix', 'sufix']) == [0, 0, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['xyz', 'zyx', 'yxz', 'zxz', 'xzy', 'zyy'],wordsQuery = ['xyz', 'zyx', 'yz', 'zx', 'xz', 'yy']) == [0, 1, 0, 1, 2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['xyz', 'zyx', 'yxz', 'zxz', 'xzy', 'zyy'],wordsQuery = ['xyz', 'zyx', 'yz', 'zx', 'xz', 'yy']) == [0, 1, 0, 1, 2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['aaaa', 'aaa', 'aa', 'a', ''],wordsQuery = ['aaaa', 'aaa', 'aa', 'a', '', 'b']) == [0, 1, 2, 3, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['aaaa', 'aaa', 'aa', 'a', ''],wordsQuery = ['aaaa', 'aaa', 'aa', 'a', '', 'b']) == [0, 1, 2, 3, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],wordsQuery = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa']) == [0, 1, 2, 3, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],wordsQuery = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa']) == [0, 1, 2, 3, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcdefg', 'defghij', 'efghijk', 'fghijkl', 'ghijklm'],wordsQuery = ['fgh', 'ghijk', 'ijkl', 'jklm', 'mnop']) == [0, 2, 3, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcdefg', 'defghij', 'efghijk', 'fghijkl', 'ghijklm'],wordsQuery = ['fgh', 'ghijk', 'ijkl', 'jklm', 'mnop']) == [0, 2, 3, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['suffix', 'suffixx', 'suffixxx', 'suffixxxx'],wordsQuery = ['ffix', 'xffix', 'xxffix', 'xxxffix', 'xxxxffix', 'suffix']) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['suffix', 'suffixx', 'suffixxx', 'suffixxxx'],wordsQuery = ['ffix', 'xffix', 'xxffix', 'xxxffix', 'xxxxffix', 'suffix']) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcdefghij', 'bcdefghij', 'cdefghij', 'defghij', 'efghij', 'fghij', 'ghij', 'hij', 'ij', 'j'],wordsQuery = (['abcdefghij', 'efghij', 'fghij', 'ghij', 'hij', 'ij', 'j', 'abcdefghijk', 'defghijk', 'fghijk', 'ghijk', 'hijk', 'ijk', 'jk', 'k'],)) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcdefghij', 'bcdefghij', 'cdefghij', 'defghij', 'efghij', 'fghij', 'ghij', 'hij', 'ij', 'j'],wordsQuery = (['abcdefghij', 'efghij', 'fghij', 'ghij', 'hij', 'ij', 'j', 'abcdefghijk', 'defghijk', 'fghijk', 'ghijk', 'hijk', 'ijk', 'jk', 'k'],)) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['sameprefixsame', 'sameprefix', 'same', 'different'],wordsQuery = ['sameprefixsame', 'sameprefix', 'same', 'different', 'sameprefixsame', 'sameprefix', 'same', 'different']) == [0, 1, 2, 3, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['sameprefixsame', 'sameprefix', 'same', 'different'],wordsQuery = ['sameprefixsame', 'sameprefix', 'same', 'different', 'sameprefixsame', 'sameprefix', 'same', 'different']) == [0, 1, 2, 3, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['suffix', 'suffixes', 'suffices', 'suffixing', 'suffixied'],wordsQuery = ['fix', 'fixes', 'fices', 'fixing', 'fixied', 'suffix', 'suffixes']) == [0, 1, 2, 3, 4, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['suffix', 'suffixes', 'suffices', 'suffixing', 'suffixied'],wordsQuery = ['fix', 'fixes', 'fices', 'fixing', 'fixied', 'suffix', 'suffixes']) == [0, 1, 2, 3, 4, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['longestword', 'longword', 'long', 'lon', 'lo', 'l'],wordsQuery = ['ongestword', 'ongword', 'ong', 'on', 'o', 'l', 'x']) == [0, 1, 2, 3, 4, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['longestword', 'longword', 'long', 'lon', 'lo', 'l'],wordsQuery = ['ongestword', 'ongword', 'ong', 'on', 'o', 'l', 'x']) == [0, 1, 2, 3, 4, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['one', 'two', 'three', 'four', 'five'],wordsQuery = ['ne', 'wo', 'ree', 'our', 'ive', 'ven', 'on']) == [0, 1, 2, 3, 4, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['one', 'two', 'three', 'four', 'five'],wordsQuery = ['ne', 'wo', 'ree', 'our', 'ive', 'ven', 'on']) == [0, 1, 2, 3, 4, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcabcabc', 'bcabcabc', 'cabcabc', 'abcabc', 'bcabc', 'cabc', 'abc', 'bc', 'c', 'a', 'b', 'c'],wordsQuery = ['abc', 'bc', 'c', 'a', 'b', 'c', 'abcabc', 'bcabc', 'cabc', 'abcabcabc', 'xyz', 'zzz', 'aaaaa', 'bbbbb', 'ccccc', 'dddd', 'eeeee', 'ffffff', 'gggg', 'hhhhh', 'iiiii', 'jjjjj', 'kkkkk', 'lllll', 'mmmmm', 'nnnnn', 'ooooo', 'ppppp', 'qqqqq', 'rrrrr', 'sssss', 'ttttt', 'uuuuu', 'vvvvv', 'wwwww', 'xxxxx', 'yyyyy', 'zzzzz']) == [6, 7, 8, 9, 10, 8, 3, 4, 5, 0, 8, 8, 9, 10, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcabcabc', 'bcabcabc', 'cabcabc', 'abcabc', 'bcabc', 'cabc', 'abc', 'bc', 'c', 'a', 'b', 'c'],wordsQuery = ['abc', 'bc', 'c', 'a', 'b', 'c', 'abcabc', 'bcabc', 'cabc', 'abcabcabc', 'xyz', 'zzz', 'aaaaa', 'bbbbb', 'ccccc', 'dddd', 'eeeee', 'ffffff', 'gggg', 'hhhhh', 'iiiii', 'jjjjj', 'kkkkk', 'lllll', 'mmmmm', 'nnnnn', 'ooooo', 'ppppp', 'qqqqq', 'rrrrr', 'sssss', 'ttttt', 'uuuuu', 'vvvvv', 'wwwww', 'xxxxx', 'yyyyy', 'zzzzz']) == [6, 7, 8, 9, 10, 8, 3, 4, 5, 0, 8, 8, 9, 10, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['aabbcc', 'bbcc', 'bcc', 'cc', 'c'],wordsQuery = ['aabbcc', 'bbcc', 'bcc', 'cc', 'c', 'd', 'e', 'f']) == [0, 1, 2, 3, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['aabbcc', 'bbcc', 'bcc', 'cc', 'c'],wordsQuery = ['aabbcc', 'bbcc', 'bcc', 'cc', 'c', 'd', 'e', 'f']) == [0, 1, 2, 3, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['apple', 'banana', 'grape', 'pineapple', 'orange'],wordsQuery = ['apple', 'banana', 'grape', 'pineapple', 'orange', 'le', 'ane', 'e']) == [0, 1, 2, 3, 4, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['apple', 'banana', 'grape', 'pineapple', 'orange'],wordsQuery = ['apple', 'banana', 'grape', 'pineapple', 'orange', 'le', 'ane', 'e']) == [0, 1, 2, 3, 4, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['longstring', 'longstr', 'longs', 'long', 'lo', 'l'],wordsQuery = ['longstr', 'longs', 'long', 'lo', 'l', 'o', 'ongstr', 'ngstr', 'gstr', 'str']) == [1, 2, 3, 4, 5, 4, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['longstring', 'longstr', 'longs', 'long', 'lo', 'l'],wordsQuery = ['longstr', 'longs', 'long', 'lo', 'l', 'o', 'ongstr', 'ngstr', 'gstr', 'str']) == [1, 2, 3, 4, 5, 4, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['xyzabc', 'yabc', 'xabc', 'abc', 'bc', 'c'],wordsQuery = ['abc', 'c', 'bc', 'xyzabc', 'yabc', 'xabc']) == [3, 5, 4, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['xyzabc', 'yabc', 'xabc', 'abc', 'bc', 'c'],wordsQuery = ['abc', 'c', 'bc', 'xyzabc', 'yabc', 'xabc']) == [3, 5, 4, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['aabbcc', 'bbaa', 'ccaa', 'aab', 'bb', 'cc'],wordsQuery = ['aabbcc', 'bbaa', 'ccaa', 'aab', 'bb', 'cc', 'aabb', 'bbcc', 'aa', 'b', 'c']) == [0, 1, 2, 3, 4, 5, 4, 0, 1, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['aabbcc', 'bbaa', 'ccaa', 'aab', 'bb', 'cc'],wordsQuery = ['aabbcc', 'bbaa', 'ccaa', 'aab', 'bb', 'cc', 'aabb', 'bbcc', 'aa', 'b', 'c']) == [0, 1, 2, 3, 4, 5, 4, 0, 1, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcdefghij', 'bcdefghij', 'cdefghij', 'defghij', 'efghij', 'fghij', 'ghij', 'hij', 'ij', 'j'],wordsQuery = ['ij', 'fghij', 'ghij', 'hij', 'ij', 'j', 'abcdef', 'xyz', 'zzz', 'abcdefghij']) == [8, 5, 6, 7, 8, 9, 9, 9, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcdefghij', 'bcdefghij', 'cdefghij', 'defghij', 'efghij', 'fghij', 'ghij', 'hij', 'ij', 'j'],wordsQuery = ['ij', 'fghij', 'ghij', 'hij', 'ij', 'j', 'abcdef', 'xyz', 'zzz', 'abcdefghij']) == [8, 5, 6, 7, 8, 9, 9, 9, 9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcabcabcabc', 'bcabcabcabc', 'cabcabcabc', 'abcabcabc', 'bcabcabc', 'cabcabc', 'abcabc', 'bcabc', 'cabc', 'abc', 'bc', 'c'],wordsQuery = ['abcabcabcabc', 'bcabcabcabc', 'cabcabcabc', 'abcabcabc', 'bcabcabc', 'cabcabc', 'abcabc', 'bcabc', 'cabc', 'abc', 'bc', 'c', 'd', 'e', 'f']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcabcabcabc', 'bcabcabcabc', 'cabcabcabc', 'abcabcabc', 'bcabcabc', 'cabcabc', 'abcabc', 'bcabc', 'cabc', 'abc', 'bc', 'c'],wordsQuery = ['abcabcabcabc', 'bcabcabcabc', 'cabcabcabc', 'abcabcabc', 'bcabcabc', 'cabcabc', 'abcabc', 'bcabc', 'cabc', 'abc', 'bc', 'c', 'd', 'e', 'f']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11, 11]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['suffix', 'suffixmatch', 'suffixmatchlong', 'suffixmatchlongest'],wordsQuery = ['suffix', 'match', 'long', 'longest', 'suffixmatch', 'suffixmatchlong', 'suffixmatchlongest']) == [0, 1, 2, 3, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['suffix', 'suffixmatch', 'suffixmatchlong', 'suffixmatchlongest'],wordsQuery = ['suffix', 'match', 'long', 'longest', 'suffixmatch', 'suffixmatchlong', 'suffixmatchlongest']) == [0, 1, 2, 3, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['racecar', 'civic', 'level', 'rotor', 'deified'],wordsQuery = ['car', 'civic', 'vel', 'rotor', 'deified', 'cara', 'ivic']) == [0, 1, 2, 3, 4, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['racecar', 'civic', 'level', 'rotor', 'deified'],wordsQuery = ['car', 'civic', 'vel', 'rotor', 'deified', 'cara', 'ivic']) == [0, 1, 2, 3, 4, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcdefgh', 'abcdefg', 'abcde', 'abcd', 'abc', 'ab', 'a'],wordsQuery = ['abcd', 'abc', 'ab', 'a', 'z', 'bcd', 'cde']) == [3, 4, 5, 6, 6, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcdefgh', 'abcdefg', 'abcde', 'abcd', 'abc', 'ab', 'a'],wordsQuery = ['abcd', 'abc', 'ab', 'a', 'z', 'bcd', 'cde']) == [3, 4, 5, 6, 6, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['xyzabc', 'yzabc', 'zabc', 'abc', 'c'],wordsQuery = ['zabc', 'abc', 'c', 'xyzabc', 'y']) == [2, 3, 4, 0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['xyzabc', 'yzabc', 'zabc', 'abc', 'c'],wordsQuery = ['zabc', 'abc', 'c', 'xyzabc', 'y']) == [2, 3, 4, 0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcdexyz', 'bcdexyz', 'cdexyz', 'dexyz', 'exyz', 'xyz', 'yz', 'z'],wordsQuery = ['abcdexyz', 'bcdexyz', 'cdexyz', 'dexyz', 'exyz', 'xyz', 'yz', 'z', 'xyz', 'exyz', 'dexyz', 'cdexyz', 'bcdexyz', 'abcdexyz']) == [0, 1, 2, 3, 4, 5, 6, 7, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcdexyz', 'bcdexyz', 'cdexyz', 'dexyz', 'exyz', 'xyz', 'yz', 'z'],wordsQuery = ['abcdexyz', 'bcdexyz', 'cdexyz', 'dexyz', 'exyz', 'xyz', 'yz', 'z', 'xyz', 'exyz', 'dexyz', 'cdexyz', 'bcdexyz', 'abcdexyz']) == [0, 1, 2, 3, 4, 5, 6, 7, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['apple', 'bpple', 'cppla', 'dppla', 'epple'],wordsQuery = ['pple', 'apple', 'bpple', 'cppla', 'dppla', 'epple']) == [0, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['apple', 'bpple', 'cppla', 'dppla', 'epple'],wordsQuery = ['pple', 'apple', 'bpple', 'cppla', 'dppla', 'epple']) == [0, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee'],wordsQuery = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'aaa', 'bbb', 'ccc', 'ddd', 'eee', 'aa', 'bb', 'cc', 'dd', 'ee', 'a', 'b', 'c', 'd', 'e']) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee'],wordsQuery = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'aaa', 'bbb', 'ccc', 'ddd', 'eee', 'aa', 'bb', 'cc', 'dd', 'ee', 'a', 'b', 'c', 'd', 'e']) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['abcd', 'bcd', 'cd', 'd'],wordsQuery = ['abcd', 'bcd', 'cd', 'd', 'abcd', 'bcd', 'cd', 'd']) == [0, 1, 2, 3, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['abcd', 'bcd', 'cd', 'd'],wordsQuery = ['abcd', 'bcd', 'cd', 'd', 'abcd', 'bcd', 'cd', 'd']) == [0, 1, 2, 3, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['zzzzz', 'zzzz', 'zzz', 'zz', 'z'],wordsQuery = ['zzzzz', 'zzzz', 'zzz', 'zz', 'z', 'a', 'b', 'c']) == [0, 1, 2, 3, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['zzzzz', 'zzzz', 'zzz', 'zz', 'z'],wordsQuery = ['zzzzz', 'zzzz', 'zzz', 'zz', 'z', 'a', 'b', 'c']) == [0, 1, 2, 3, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['thisisatest', 'isisatest', 'sisatest', 'isatest', 'satest', 'atest', 'test', 'est', 'st', 't'],wordsQuery = ['test', 'est', 'st', 't', 'a', 'b', 'c', 'd', 'e', 'f']) == [6, 7, 8, 9, 9, 9, 9, 9, 9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['thisisatest', 'isisatest', 'sisatest', 'isatest', 'satest', 'atest', 'test', 'est', 'st', 't'],wordsQuery = ['test', 'est', 'st', 't', 'a', 'b', 'c', 'd', 'e', 'f']) == [6, 7, 8, 9, 9, 9, 9, 9, 9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['longword', 'longerword', 'longestword', 'shortword', 'tinyword'],wordsQuery = ['word', 'longword', 'longerword', 'longestword', 'shortword', 'tinyword', 'long', 'longer', 'longest', 'short', 'tiny', 'o', 'r', 't', 'w', 'd']) == [0, 0, 1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['longword', 'longerword', 'longestword', 'shortword', 'tinyword'],wordsQuery = ['word', 'longword', 'longerword', 'longestword', 'shortword', 'tinyword', 'long', 'longer', 'longest', 'short', 'tiny', 'o', 'r', 't', 'w', 'd']) == [0, 0, 1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['unique', 'distinct', 'separate', 'different', 'uniquely'],wordsQuery = ['unique', 'distinct', 'separate', 'different', 'uniquely', 'un']) == [0, 1, 2, 3, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['unique', 'distinct', 'separate', 'different', 'uniquely'],wordsQuery = ['unique', 'distinct', 'separate', 'different', 'uniquely', 'un']) == [0, 1, 2, 3, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['longwordwithsuffix', 'wordwithsuffix', 'withsuffix', 'suffix', 'fix', 'ix', 'x'],wordsQuery = ['suffix', 'fix', 'ix', 'x', 'y', 'z', 'wordwithsuffix', 'longwordwithsuffix']) == [3, 4, 5, 6, 6, 6, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['longwordwithsuffix', 'wordwithsuffix', 'withsuffix', 'suffix', 'fix', 'ix', 'x'],wordsQuery = ['suffix', 'fix', 'ix', 'x', 'y', 'z', 'wordwithsuffix', 'longwordwithsuffix']) == [3, 4, 5, 6, 6, 6, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['longestword', 'longest', 'long', 'lon', 'lo', 'l'],wordsQuery = ['longestword', 'longest', 'longestword', 'lon', 'lo', 'xyz']) == [0, 1, 0, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['longestword', 'longest', 'long', 'lon', 'lo', 'l'],wordsQuery = ['longestword', 'longest', 'longestword', 'lon', 'lo', 'xyz']) == [0, 1, 0, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(wordsContainer = ['uniqueword', 'anotherword', 'commonword', 'similarword', 'dissimilarword'],wordsQuery = ['word', 'similar', 'dissimilar', 'unique', 'another', 'common']) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordsContainer = ['uniqueword', 'anotherword', 'commonword', 'similarword', 'dissimilarword'],wordsQuery = ['word', 'similar', 'dissimilar', 'unique', 'another', 'common']) == [0, 0, 0, 0, 0, 0]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(wordsContainer = ['banana', 'mango', 'papaya'],wordsQuery = ['ana', 'ango', 'aya']) == [0, 1, 2]
    assert candidate(wordsContainer = ['abcde', 'bcde', 'cde', 'de', 'e'],wordsQuery = ['cde', 'de', 'e', 'a', 'b']) == [2, 3, 4, 4, 4]
    assert candidate(wordsContainer = ['xyz', 'zyx', 'zxy'],wordsQuery = ['x', 'y', 'z']) == [1, 2, 0]
    assert candidate(wordsContainer = ['zzzzz', 'zzzz', 'zzz', 'zz', 'z'],wordsQuery = ['zzzz', 'zzz', 'zz', 'z', 'a']) == [1, 2, 3, 4, 4]
    assert candidate(wordsContainer = ['a', 'ab', 'abc'],wordsQuery = ['a', 'ab', 'abc']) == [0, 1, 2]
    assert candidate(wordsContainer = ['unique', 'suffix', 'words'],wordsQuery = ['fix', 'ffix', 'uffix']) == [1, 1, 1]
    assert candidate(wordsContainer = ['abcd', 'bcd', 'xbcd'],wordsQuery = ['cd', 'bcd', 'xyz']) == [1, 1, 1]
    assert candidate(wordsContainer = ['hello', 'world', 'python'],wordsQuery = ['lo', 'rld', 'on']) == [0, 1, 2]
    assert candidate(wordsContainer = ['a', 'b', 'c'],wordsQuery = ['d', 'e', 'f']) == [0, 0, 0]
    assert candidate(wordsContainer = ['abcdefgh', 'poiuygh', 'ghghgh'],wordsQuery = ['gh', 'acbfgh', 'acbfegh']) == [2, 0, 2]
    assert candidate(wordsContainer = ['abcde', 'bcde', 'cde'],wordsQuery = ['cde', 'de', 'e']) == [2, 2, 2]
    assert candidate(wordsContainer = ['same', 'same', 'same'],wordsQuery = ['same', 'same', 'same']) == [0, 0, 0]
    assert candidate(wordsContainer = ['longestword', 'short', 'word'],wordsQuery = ['word', 'short', 'longestword']) == [2, 1, 0]
    assert candidate(wordsContainer = ['apple', 'maple', 'orange'],wordsQuery = ['le', 'ple', 'range']) == [0, 0, 2]
    assert candidate(wordsContainer = ['a', 'b', 'c'],wordsQuery = ['a', 'b', 'c']) == [0, 1, 2]
    assert candidate(wordsContainer = ['abc', 'def', 'ghi'],wordsQuery = ['abc', 'def', 'ghi']) == [0, 1, 2]
    assert candidate(wordsContainer = ['a', 'b', 'c', 'd'],wordsQuery = ['a', 'b', 'c', 'd']) == [0, 1, 2, 3]
    assert candidate(wordsContainer = ['aaaaa', 'bbbbb', 'ccccc', 'abcde', 'bcdef', 'cdefg'],wordsQuery = ['abcde', 'bcdef', 'cdefg', 'de', 'ef', 'f']) == [3, 4, 5, 3, 4, 4]
    assert candidate(wordsContainer = ['abcdef', 'defabc', 'abc', 'def', 'efg', 'fg', 'g'],wordsQuery = ['abc', 'def', 'efg', 'fg', 'g', 'a', 'bcd', 'cde']) == [2, 3, 4, 5, 6, 6, 6, 6]
    assert candidate(wordsContainer = ['abcdefghijk', 'ghijklmno', 'ijklmnopq', 'jklmnopqr', 'klmnopqrs', 'lmnopqrst'],wordsQuery = ['ijkl', 'mnop', 'nopq', 'opqr', 'pqrs', 'qrstu', 'rstuv', 'stuvw', 'tuvwx', 'uvwxy', 'vwxyz', 'wxyz', 'xyz', 'yz', 'z']) == [1, 1, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(wordsContainer = ['aabbcc', 'bbcc', 'bcc', 'cc', 'c', 'aabbccdd', 'bbccdd', 'bccdd', 'ccdd', 'cdd', 'dd', 'd'],wordsQuery = ['cc', 'dd', 'cdd', 'bcc', 'bbcc', 'aabbcc', 'xyz', 'abc', 'd', 'ccdd', 'aabbccdd']) == [3, 10, 9, 2, 1, 0, 4, 4, 11, 8, 5]
    assert candidate(wordsContainer = ['zzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzz', 'zzzzzzzzzzzzz', 'zzzzzzzzzzzz', 'zzzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzz', 'zzzzzzzz', 'zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z', ''],wordsQuery = ['zzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzz', 'zzzzzzzzzzzzz', 'zzzzzzzzzzzz', 'zzzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzz', 'zzzzzzzz', 'zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 15]
    assert candidate(wordsContainer = ['aaaaa', 'aaabaaa', 'aaacaaa', 'aaad', 'aa', 'a', 'aaeaaa'],wordsQuery = ['aa', 'aaa', 'aaaa', 'aaaaa', 'aaab', 'aaac', 'aaad', 'aae']) == [4, 0, 0, 0, 5, 5, 3, 5]
    assert candidate(wordsContainer = ['apple', 'pple', 'ple', 'le', 'e', 'orange', 'range', 'ange', 'nge', 'ge', 'e'],wordsQuery = ['ple', 'le', 'e', 'apple', 'orange', 'range', 'nge', 'ge']) == [2, 3, 4, 0, 5, 6, 8, 9]
    assert candidate(wordsContainer = ['abcd', 'bcd', 'cd', 'd', ''],wordsQuery = ['abcd', 'bcd', 'cd', 'd', '', 'a', 'b', 'c']) == [0, 1, 2, 3, 4, 4, 4, 4]
    assert candidate(wordsContainer = ['ababab', 'bababa', 'abab', 'bab', 'ab', 'b', 'a'],wordsQuery = ['ab', 'bab', 'abab', 'bababa', 'ababab', 'ba', 'a']) == [4, 3, 2, 1, 0, 1, 6]
    assert candidate(wordsContainer = ['longestword', 'longest', 'long', 'lo', 'l'],wordsQuery = ['word', 'st', 'ng', 'g', 'o', 'wordd', 'ngggg']) == [0, 1, 2, 2, 3, 0, 2]
    assert candidate(wordsContainer = ['abcd', 'bcd', 'bcd', 'cd', 'cd', 'd'],wordsQuery = ['cd', 'bcd', 'd', 'a', 'ab', 'abcd']) == [3, 1, 5, 5, 5, 0]
    assert candidate(wordsContainer = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],wordsQuery = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa']) == [0, 1, 2, 3, 4, 4, 4]
    assert candidate(wordsContainer = ['prefix', 'prefixx', 'prefixxx', 'prefixxxx'],wordsQuery = ['fix', 'xfix', 'xxfix', 'xxxfix', 'xxxxfix', 'prefix']) == [0, 0, 0, 0, 0, 0]
    assert candidate(wordsContainer = ['abcd', 'bcd', 'cd', 'd', 'abcdabcd', 'bcdbcd', 'cdcd', 'dd', 'abcdabcde'],wordsQuery = ['abcd', 'bcd', 'cd', 'd', 'abcdabcd', 'bcdbcd', 'cdcd', 'dd', 'e', 'abcdabcde', 'de', 'cde', 'bcde']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8]
    assert candidate(wordsContainer = ['abcdexyz', 'bcdexyz', 'cdexyz', 'dexyz', 'exyz', 'xyz'],wordsQuery = ['xyz', 'exyz', 'dexyz', 'cdexyz', 'bcdexyz', 'abcdexyz', 'z']) == [5, 4, 3, 2, 1, 0, 5]
    assert candidate(wordsContainer = ['abcdexyz', 'bcdexyz', 'xbcdexyz', 'abcdexyz'],wordsQuery = ['cdexyz', 'bcdexyz', 'xyz', 'abcdexyz']) == [1, 1, 1, 0]
    assert candidate(wordsContainer = ['hello', 'world', 'hello_world', 'world_hello', 'hold', 'old', 'ld', 'd'],wordsQuery = ['hello', 'world', 'hello_world', 'hold', 'old', 'ld', 'd', 'o']) == [0, 1, 2, 4, 5, 6, 7, 0]
    assert candidate(wordsContainer = ['apple', 'orange', 'banana', 'grape', 'pineapple'],wordsQuery = ['apple', 'orange', 'banana', 'grape', 'pineapple', 'pe', 'e']) == [0, 1, 2, 3, 4, 3, 0]
    assert candidate(wordsContainer = ['xyz', 'yz', 'z', 'wxyz', 'vwxyz'],wordsQuery = ['z', 'yz', 'xyz', 'wxyz', 'vwxyz', 'wxyzz']) == [2, 1, 0, 3, 4, 2]
    assert candidate(wordsContainer = ['aaaa', 'aaab', 'aaac', 'aaba', 'aabb', 'aabc', 'aaca', 'aacc', 'abaa', 'abab', 'abac', 'abba', 'abbb', 'abbc', 'abca', 'abcb', 'abcc', 'acaa', 'acab', 'acac', 'acba', 'acbb', 'acbc', 'acca', 'accb', 'accc'],wordsQuery = ['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acc', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc', 'a', 'b', 'c', 'aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6, 15, 7]
    assert candidate(wordsContainer = ['example', 'samples', 'examples', 'sampless'],wordsQuery = ['ple', 'les', 'ample', 'sample', 'samples', 'examples', 'sampless']) == [0, 1, 0, 0, 1, 2, 3]
    assert candidate(wordsContainer = ['abcdefghij', 'abcdefghijk', 'abcdefgh', 'abcdefg', 'abcde', 'abcd'],wordsQuery = ['defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl']) == [3, 2, 5, 0, 1, 5]
    assert candidate(wordsContainer = ['abcdefghij', 'bcdefghij', 'cdefghij', 'defghij', 'efghij', 'fghij', 'ghij', 'hij', 'ij', 'j'],wordsQuery = ['ghij', 'hij', 'ij', 'j', 'k', 'abcdefghij', 'bcdefghij', 'cdefghij', 'defghij']) == [6, 7, 8, 9, 9, 0, 1, 2, 3]
    assert candidate(wordsContainer = ['aabbcc', 'bbaacc', 'ccaabb', 'aabb', 'bbaa', 'ccaac', 'aac', 'ac', 'c'],wordsQuery = ['aabbcc', 'bbaacc', 'ccaabb', 'aabb', 'bbaa', 'ccaac', 'aac', 'ac', 'c', 'aa', 'bb', 'cc']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 4, 3, 0]
    assert candidate(wordsContainer = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],wordsQuery = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(wordsContainer = ['banana', 'anana', 'nana', 'ana', 'na', 'a'],wordsQuery = ['ana', 'na', 'a', 'anana', 'nana', 'banana', 'bana', 'ananaa']) == [3, 4, 5, 1, 2, 0, 3, 5]
    assert candidate(wordsContainer = ['abcdefg', 'defg', 'efg', 'fg', 'g'],wordsQuery = ['defg', 'efg', 'fg', 'g', 'abcdefg']) == [1, 2, 3, 4, 0]
    assert candidate(wordsContainer = ['repeated', 'repeatedword', 'repeat', 'rep', 're', 'r'],wordsQuery = ['repeated', 'repeatedword', 'repeat', 'rep', 're', 'r', 'ed', 'at', 't', 'e', '']) == [0, 1, 2, 3, 4, 5, 0, 2, 2, 4, 5]
    assert candidate(wordsContainer = ['suffix', 'fix', 'suffixfix', 'suffixsuffix', 'ffix', 'fixfix', 'suffixfixfix'],wordsQuery = ['suffix', 'fix', 'suffixfix', 'suffixsuffix', 'ffix', 'fixfix', 'suffixfixfix', 'ff', 'ix', 'x']) == [0, 1, 2, 3, 4, 5, 6, 1, 1, 1]
    assert candidate(wordsContainer = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijk', 'lmnopqr', 'stuvwxyz'],wordsQuery = ['mnopqr', 'lmnopqr', 'stuv', 'xyz', 'pqrs']) == [3, 3, 3, 4, 3]
    assert candidate(wordsContainer = ['unique', 'uniq', 'un', 'u'],wordsQuery = ['ue', 'iq', 'n', 'u', 'uniq', 'unique', 'nique']) == [0, 1, 2, 3, 1, 0, 0]
    assert candidate(wordsContainer = ['short', 'shorter', 'shortest', 'shortestest'],wordsQuery = ['est', 'test', 'st', 'rtest', 'shortestestest', 'shorter', 'shortest']) == [2, 2, 2, 2, 3, 1, 2]
    assert candidate(wordsContainer = ['hello', 'world', 'programming', 'worldwide', 'program'],wordsQuery = ['gram', 'ing', 'world', 'hello', 'pro', 'gramming']) == [4, 2, 1, 0, 0, 2]
    assert candidate(wordsContainer = ['suffix', 'prefix', 'suffixprefix', 'prefixsuffix'],wordsQuery = ['fix', 'fixx', 'suffix', 'prefix', 'uffix', 'frefix', 'sufix']) == [0, 0, 0, 1, 0, 1, 0]
    assert candidate(wordsContainer = ['xyz', 'zyx', 'yxz', 'zxz', 'xzy', 'zyy'],wordsQuery = ['xyz', 'zyx', 'yz', 'zx', 'xz', 'yy']) == [0, 1, 0, 1, 2, 5]
    assert candidate(wordsContainer = ['aaaa', 'aaa', 'aa', 'a', ''],wordsQuery = ['aaaa', 'aaa', 'aa', 'a', '', 'b']) == [0, 1, 2, 3, 4, 4]
    assert candidate(wordsContainer = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],wordsQuery = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa']) == [0, 1, 2, 3, 4, 4]
    assert candidate(wordsContainer = ['abcdefg', 'defghij', 'efghijk', 'fghijkl', 'ghijklm'],wordsQuery = ['fgh', 'ghijk', 'ijkl', 'jklm', 'mnop']) == [0, 2, 3, 4, 0]
    assert candidate(wordsContainer = ['suffix', 'suffixx', 'suffixxx', 'suffixxxx'],wordsQuery = ['ffix', 'xffix', 'xxffix', 'xxxffix', 'xxxxffix', 'suffix']) == [0, 0, 0, 0, 0, 0]
    assert candidate(wordsContainer = ['abcdefghij', 'bcdefghij', 'cdefghij', 'defghij', 'efghij', 'fghij', 'ghij', 'hij', 'ij', 'j'],wordsQuery = (['abcdefghij', 'efghij', 'fghij', 'ghij', 'hij', 'ij', 'j', 'abcdefghijk', 'defghijk', 'fghijk', 'ghijk', 'hijk', 'ijk', 'jk', 'k'],)) == [9]
    assert candidate(wordsContainer = ['sameprefixsame', 'sameprefix', 'same', 'different'],wordsQuery = ['sameprefixsame', 'sameprefix', 'same', 'different', 'sameprefixsame', 'sameprefix', 'same', 'different']) == [0, 1, 2, 3, 0, 1, 2, 3]
    assert candidate(wordsContainer = ['suffix', 'suffixes', 'suffices', 'suffixing', 'suffixied'],wordsQuery = ['fix', 'fixes', 'fices', 'fixing', 'fixied', 'suffix', 'suffixes']) == [0, 1, 2, 3, 4, 0, 1]
    assert candidate(wordsContainer = ['longestword', 'longword', 'long', 'lon', 'lo', 'l'],wordsQuery = ['ongestword', 'ongword', 'ong', 'on', 'o', 'l', 'x']) == [0, 1, 2, 3, 4, 5, 5]
    assert candidate(wordsContainer = ['one', 'two', 'three', 'four', 'five'],wordsQuery = ['ne', 'wo', 'ree', 'our', 'ive', 'ven', 'on']) == [0, 1, 2, 3, 4, 0, 0]
    assert candidate(wordsContainer = ['abcabcabc', 'bcabcabc', 'cabcabc', 'abcabc', 'bcabc', 'cabc', 'abc', 'bc', 'c', 'a', 'b', 'c'],wordsQuery = ['abc', 'bc', 'c', 'a', 'b', 'c', 'abcabc', 'bcabc', 'cabc', 'abcabcabc', 'xyz', 'zzz', 'aaaaa', 'bbbbb', 'ccccc', 'dddd', 'eeeee', 'ffffff', 'gggg', 'hhhhh', 'iiiii', 'jjjjj', 'kkkkk', 'lllll', 'mmmmm', 'nnnnn', 'ooooo', 'ppppp', 'qqqqq', 'rrrrr', 'sssss', 'ttttt', 'uuuuu', 'vvvvv', 'wwwww', 'xxxxx', 'yyyyy', 'zzzzz']) == [6, 7, 8, 9, 10, 8, 3, 4, 5, 0, 8, 8, 9, 10, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
    assert candidate(wordsContainer = ['aabbcc', 'bbcc', 'bcc', 'cc', 'c'],wordsQuery = ['aabbcc', 'bbcc', 'bcc', 'cc', 'c', 'd', 'e', 'f']) == [0, 1, 2, 3, 4, 4, 4, 4]
    assert candidate(wordsContainer = ['apple', 'banana', 'grape', 'pineapple', 'orange'],wordsQuery = ['apple', 'banana', 'grape', 'pineapple', 'orange', 'le', 'ane', 'e']) == [0, 1, 2, 3, 4, 0, 0, 0]
    assert candidate(wordsContainer = ['longstring', 'longstr', 'longs', 'long', 'lo', 'l'],wordsQuery = ['longstr', 'longs', 'long', 'lo', 'l', 'o', 'ongstr', 'ngstr', 'gstr', 'str']) == [1, 2, 3, 4, 5, 4, 1, 1, 1, 1]
    assert candidate(wordsContainer = ['xyzabc', 'yabc', 'xabc', 'abc', 'bc', 'c'],wordsQuery = ['abc', 'c', 'bc', 'xyzabc', 'yabc', 'xabc']) == [3, 5, 4, 0, 1, 2]
    assert candidate(wordsContainer = ['aabbcc', 'bbaa', 'ccaa', 'aab', 'bb', 'cc'],wordsQuery = ['aabbcc', 'bbaa', 'ccaa', 'aab', 'bb', 'cc', 'aabb', 'bbcc', 'aa', 'b', 'c']) == [0, 1, 2, 3, 4, 5, 4, 0, 1, 4, 5]
    assert candidate(wordsContainer = ['abcdefghij', 'bcdefghij', 'cdefghij', 'defghij', 'efghij', 'fghij', 'ghij', 'hij', 'ij', 'j'],wordsQuery = ['ij', 'fghij', 'ghij', 'hij', 'ij', 'j', 'abcdef', 'xyz', 'zzz', 'abcdefghij']) == [8, 5, 6, 7, 8, 9, 9, 9, 9, 0]
    assert candidate(wordsContainer = ['abcabcabcabc', 'bcabcabcabc', 'cabcabcabc', 'abcabcabc', 'bcabcabc', 'cabcabc', 'abcabc', 'bcabc', 'cabc', 'abc', 'bc', 'c'],wordsQuery = ['abcabcabcabc', 'bcabcabcabc', 'cabcabcabc', 'abcabcabc', 'bcabcabc', 'cabcabc', 'abcabc', 'bcabc', 'cabc', 'abc', 'bc', 'c', 'd', 'e', 'f']) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11, 11]
    assert candidate(wordsContainer = ['suffix', 'suffixmatch', 'suffixmatchlong', 'suffixmatchlongest'],wordsQuery = ['suffix', 'match', 'long', 'longest', 'suffixmatch', 'suffixmatchlong', 'suffixmatchlongest']) == [0, 1, 2, 3, 1, 2, 3]
    assert candidate(wordsContainer = ['racecar', 'civic', 'level', 'rotor', 'deified'],wordsQuery = ['car', 'civic', 'vel', 'rotor', 'deified', 'cara', 'ivic']) == [0, 1, 2, 3, 4, 1, 1]
    assert candidate(wordsContainer = ['abcdefgh', 'abcdefg', 'abcde', 'abcd', 'abc', 'ab', 'a'],wordsQuery = ['abcd', 'abc', 'ab', 'a', 'z', 'bcd', 'cde']) == [3, 4, 5, 6, 6, 3, 2]
    assert candidate(wordsContainer = ['xyzabc', 'yzabc', 'zabc', 'abc', 'c'],wordsQuery = ['zabc', 'abc', 'c', 'xyzabc', 'y']) == [2, 3, 4, 0, 4]
    assert candidate(wordsContainer = ['abcdexyz', 'bcdexyz', 'cdexyz', 'dexyz', 'exyz', 'xyz', 'yz', 'z'],wordsQuery = ['abcdexyz', 'bcdexyz', 'cdexyz', 'dexyz', 'exyz', 'xyz', 'yz', 'z', 'xyz', 'exyz', 'dexyz', 'cdexyz', 'bcdexyz', 'abcdexyz']) == [0, 1, 2, 3, 4, 5, 6, 7, 5, 4, 3, 2, 1, 0]
    assert candidate(wordsContainer = ['apple', 'bpple', 'cppla', 'dppla', 'epple'],wordsQuery = ['pple', 'apple', 'bpple', 'cppla', 'dppla', 'epple']) == [0, 0, 1, 2, 3, 4]
    assert candidate(wordsContainer = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee'],wordsQuery = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'aaa', 'bbb', 'ccc', 'ddd', 'eee', 'aa', 'bb', 'cc', 'dd', 'ee', 'a', 'b', 'c', 'd', 'e']) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
    assert candidate(wordsContainer = ['abcd', 'bcd', 'cd', 'd'],wordsQuery = ['abcd', 'bcd', 'cd', 'd', 'abcd', 'bcd', 'cd', 'd']) == [0, 1, 2, 3, 0, 1, 2, 3]
    assert candidate(wordsContainer = ['zzzzz', 'zzzz', 'zzz', 'zz', 'z'],wordsQuery = ['zzzzz', 'zzzz', 'zzz', 'zz', 'z', 'a', 'b', 'c']) == [0, 1, 2, 3, 4, 4, 4, 4]
    assert candidate(wordsContainer = ['thisisatest', 'isisatest', 'sisatest', 'isatest', 'satest', 'atest', 'test', 'est', 'st', 't'],wordsQuery = ['test', 'est', 'st', 't', 'a', 'b', 'c', 'd', 'e', 'f']) == [6, 7, 8, 9, 9, 9, 9, 9, 9, 9]
    assert candidate(wordsContainer = ['longword', 'longerword', 'longestword', 'shortword', 'tinyword'],wordsQuery = ['word', 'longword', 'longerword', 'longestword', 'shortword', 'tinyword', 'long', 'longer', 'longest', 'short', 'tiny', 'o', 'r', 't', 'w', 'd']) == [0, 0, 1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(wordsContainer = ['unique', 'distinct', 'separate', 'different', 'uniquely'],wordsQuery = ['unique', 'distinct', 'separate', 'different', 'uniquely', 'un']) == [0, 1, 2, 3, 4, 0]
    assert candidate(wordsContainer = ['longwordwithsuffix', 'wordwithsuffix', 'withsuffix', 'suffix', 'fix', 'ix', 'x'],wordsQuery = ['suffix', 'fix', 'ix', 'x', 'y', 'z', 'wordwithsuffix', 'longwordwithsuffix']) == [3, 4, 5, 6, 6, 6, 1, 0]
    assert candidate(wordsContainer = ['longestword', 'longest', 'long', 'lon', 'lo', 'l'],wordsQuery = ['longestword', 'longest', 'longestword', 'lon', 'lo', 'xyz']) == [0, 1, 0, 3, 4, 5]
    assert candidate(wordsContainer = ['uniqueword', 'anotherword', 'commonword', 'similarword', 'dissimilarword'],wordsQuery = ['word', 'similar', 'dissimilar', 'unique', 'another', 'common']) == [0, 0, 0, 0, 0, 0]


