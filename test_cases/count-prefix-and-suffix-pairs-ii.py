def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'aa', 'a']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'aa', 'a']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'a', 'a', 'a', 'a']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'a', 'a', 'a', 'a']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(words = ['x', 'xx', 'xxx', 'xxxx']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['x', 'xx', 'xxx', 'xxxx']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abab', 'ab']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abab', 'ab']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['x', 'xx', 'xxx', 'xxxx', 'xxxxx']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['x', 'xx', 'xxx', 'xxxx', 'xxxxx']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz']) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz']) == 15: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hellohello', 'hellohellohello', 'he']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hellohello', 'hellohellohello', 'he']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abcabc', 'abcd', 'abcabcabc']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abcabc', 'abcd', 'abcabcabc']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']) == 45: {e}')
    
    total += 1
    try:
        result = candidate(words = ['unique', 'uniqueword', 'uniquewordunique', 'uniq']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['unique', 'uniqueword', 'uniquewordunique', 'uniq']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abcabc', 'abcabcabc']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abcabc', 'abcabcabc']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xyzxyz', 'zyxzyx']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xyzxyz', 'zyxzyx']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcdeabcda', 'ab']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcdeabcda', 'ab']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aba', 'ababa', 'aa']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aba', 'ababa', 'aa']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['pa', 'papa', 'ma', 'mama']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['pa', 'papa', 'ma', 'mama']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'testtest', 'testtesttest', 't']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'testtest', 'testtesttest', 't']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abcabc', 'abcabcabc', 'a']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abcabc', 'abcabcabc', 'a']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['pattern', 'patternpattern', 'patternpatternpattern', 'patternpatternpatternpattern']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['pattern', 'patternpattern', 'patternpatternpattern', 'patternpatternpatternpattern']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same']) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same']) == 45: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mississippi', 'issis', 'sis', 'issippi', 'iss', 'missi', 'ippi', 'pi', 'ssippi', 'mississipi', 'ississippiissippi']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mississippi', 'issis', 'sis', 'issippi', 'iss', 'missi', 'ippi', 'pi', 'ssippi', 'mississipi', 'ississippiissippi']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaabbbb', 'aaaabbbbcccc', 'aaaabbbbccccdddd', 'aaaabbbbccccddddaaaa', 'aa', 'bb', 'cc', 'dd']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaabbbb', 'aaaabbbbcccc', 'aaaabbbbccccdddd', 'aaaabbbbccccddddaaaa', 'aa', 'bb', 'cc', 'dd']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcabcabc', 'abc', 'abcabc', 'ab', 'a', 'abcabcabcabcabc']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcabcabc', 'abc', 'abcabc', 'ab', 'a', 'abcabcabcabcabc']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ababab', 'abab', 'ab', 'a', 'babab', 'bab', 'b']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ababab', 'abab', 'ab', 'a', 'babab', 'bab', 'b']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyzyxyzyx', 'xyzyx', 'zyxzyx', 'xyz', 'zyx', 'yzy', 'zyzy', 'yzyxyzyx', 'yzyxyzyxyzyxyzyx']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyzyxyzyx', 'xyzyx', 'zyxzyx', 'xyz', 'zyx', 'yzy', 'zyzy', 'yzyxyzyx', 'yzyxyzyxyzyxyzyx']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['repeat', 'repeatrepeat', 'repeatrepeatrepeat', 'peat', 'eat', 'at', 't', 'rep', 're', 'r', 'e', 'a', 'p', 'te']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repeat', 'repeatrepeat', 'repeatrepeatrepeat', 'peat', 'eat', 'at', 't', 'rep', 're', 'r', 'e', 'a', 'p', 'te']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'edcba', 'abcdeabcde', 'edcbaedcba', 'abcdeedcbaabcde']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'edcba', 'abcdeabcde', 'edcbaedcba', 'abcdeedcbaabcde']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyxyxy', 'xyxyxyxyxy', 'xyxyxyxyxyxyxy', 'xy', 'yx', 'x', 'y', 'xyxy', 'yxyx', 'xyyx', 'xxyx']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyxyxy', 'xyxyxyxyxy', 'xyxyxyxyxyxyxy', 'xy', 'yx', 'x', 'y', 'xyxy', 'yxyx', 'xyyx', 'xxyx']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefixsuffix', 'prefixsuffixprefixsuffix', 'prefixsuffixprefixsuffixprefixsuffix']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefixsuffix', 'prefixsuffixprefixsuffix', 'prefixsuffixprefixsuffixprefixsuffix']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdeabcde', 'bcdeabcd', 'cdeabcde', 'deabcdec', 'eabcdabc', 'abcde', 'bcde', 'cde', 'de', 'e', 'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdeabcde', 'bcdeabcd', 'cdeabcde', 'deabcdec', 'eabcdabc', 'abcde', 'bcde', 'cde', 'de', 'e', 'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['longwordlongword', 'longwordlongwordlongword', 'longword', 'word', 'long', 'wo', 'rd', 'ngwordlongword', 'wordlongwordlong', 'ngwordlongwordngwordlongword']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['longwordlongword', 'longwordlongwordlongword', 'longword', 'word', 'long', 'wo', 'rd', 'ngwordlongword', 'wordlongwordlong', 'ngwordlongwordngwordlongword']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdabcdabcd', 'abcdabcd', 'abcd', 'abc', 'ab', 'a', 'abcdabcdabcdabcdabcdabcd']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdabcdabcd', 'abcdabcd', 'abcd', 'abc', 'ab', 'a', 'abcdabcdabcdabcdabcdabcd']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['pattern', 'ternpat', 'ternpatpat', 'pat', 'tern', 'patternpat', 'ternpattern', 'patterntern', 'ternpatternpat']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['pattern', 'ternpat', 'ternpatpat', 'pat', 'tern', 'patternpat', 'ternpattern', 'patterntern', 'ternpatternpat']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdabcdabcdabcd', 'abcdabcdabcd', 'abcdabcd', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd', 'abcdabcdabcdabcdabcdabcdabcdabcd', 'abcdabcdabcdabcdabcdabcdabcd', 'abcdabcdabcdabcdabcdabcd', 'abcdabcdabcdabcdabcd', 'abcdabcdabcdabcd', 'abcdabcdabcd', 'abcdabcd', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd']) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdabcdabcdabcd', 'abcdabcdabcd', 'abcdabcd', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd', 'abcdabcdabcdabcdabcdabcdabcdabcd', 'abcdabcdabcdabcdabcdabcdabcd', 'abcdabcdabcdabcdabcdabcd', 'abcdabcdabcdabcdabcd', 'abcdabcdabcdabcd', 'abcdabcdabcd', 'abcdabcd', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd']) == 32: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaaa', 'aaa', 'aaaa', 'aaaaaa', 'aa']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaaa', 'aaa', 'aaaa', 'aaaaaa', 'aa']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefixsuffix', 'prefix', 'suffix', 'prefixprefix', 'suffixsuffix', 'pre', 'suf']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefixsuffix', 'prefix', 'suffix', 'prefixprefix', 'suffixsuffix', 'pre', 'suf']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyxyxyxy', 'xyxy', 'xyxyxy', 'xy', 'x', 'xyxyxyxyxyxy']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyxyxyxy', 'xyxy', 'xyxyxy', 'xy', 'x', 'xyxyxyxyxyxy']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyxyxyxyxy', 'xyxyxyxy', 'xyxyxy', 'xyxy', 'xy', 'x', 'y', 'xyxyxyxyxyxyxyxy', 'xyxyxyxyxyxyxyxyxyxyxy', 'xyxyxyxyxyxyxyxyxyxyxyxyxyxyxy', 'xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy']) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyxyxyxyxy', 'xyxyxyxy', 'xyxyxy', 'xyxy', 'xy', 'x', 'y', 'xyxyxyxyxyxyxyxy', 'xyxyxyxyxyxyxyxyxyxyxy', 'xyxyxyxyxyxyxyxyxyxyxyxyxyxyxy', 'xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy']) == 26: {e}')
    
    total += 1
    try:
        result = candidate(words = ['complexwordcomplexword', 'complexword', 'complex', 'com', 'co', 'complexwordcomplexwordcomplexword']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['complexwordcomplexword', 'complexword', 'complex', 'com', 'co', 'complexwordcomplexwordcomplexword']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'aa', 'a', 'aaaaaaaaaaaa', 'aaaa']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'aa', 'a', 'aaaaaaaaaaaa', 'aaaa']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcabcabc', 'abc', 'abcabc', 'ab', 'a', 'b', 'c']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcabcabc', 'abc', 'abcabc', 'ab', 'a', 'b', 'c']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdabcd', 'abcd', 'cdab', 'dabc', 'bcda', 'cabd', 'bacd', 'abcdabcdabcd', 'abcdabcdabcdabcd', 'abcdabcdabcdabcdabcdabcdabcdabcd']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdabcd', 'abcd', 'cdab', 'dabc', 'bcda', 'cabd', 'bacd', 'abcdabcdabcd', 'abcdabcdabcdabcd', 'abcdabcdabcdabcdabcdabcdabcdabcd']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcabcabc', 'abcabc', 'abc', 'a', 'b', 'c', 'abcabcabcabc']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcabcabc', 'abcabc', 'abc', 'a', 'b', 'c', 'abcabcabcabc']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['longprefix', 'longprefixlongprefix', 'longprefixlongprefixlongprefix']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['longprefix', 'longprefixlongprefix', 'longprefixlongprefixlongprefix']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abcabc', 'abcabcabc', 'abcabcabcabc']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abcabc', 'abcabcabc', 'abcabcabcabc']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcabcabc', 'abcabc', 'abc', 'a', 'b', 'c']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcabcabc', 'abcabc', 'abc', 'a', 'b', 'c']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefixsuffix', 'prefix', 'suffix', 'prefixsuffixprefixsuffix', 'prefixprefix', 'suffixsuffix', 'prefixsuffixprefix', 'suffixprefixsuffix']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefixsuffix', 'prefix', 'suffix', 'prefixsuffixprefixsuffix', 'prefixprefix', 'suffixsuffix', 'prefixsuffixprefix', 'suffixprefixsuffix']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['repeatedrepeated', 'repeated', 'repeatedrepeatedrepeated', 'repeatedrepeatedrepeatedrepeated', 'repeatedrepeatedrepeatedrepeatedrepeated', 'repeatedrepeatedrepeated', 'repeated', 'repeatedrepeatedrepeatedrepeatedrepeated']) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repeatedrepeated', 'repeated', 'repeatedrepeatedrepeated', 'repeatedrepeatedrepeatedrepeated', 'repeatedrepeatedrepeatedrepeatedrepeated', 'repeatedrepeatedrepeated', 'repeated', 'repeatedrepeatedrepeatedrepeatedrepeated']) == 20: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'aaab', 'aabb', 'abbb', 'bbbb', 'baaa', 'baab', 'babb', 'bbba', 'bbbb', 'abab', 'baba', 'abba', 'baab', 'abba', 'baab', 'abba', 'baab']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'aaab', 'aabb', 'abbb', 'bbbb', 'baaa', 'baab', 'babb', 'bbba', 'bbbb', 'abab', 'baba', 'abba', 'baab', 'abba', 'baab', 'abba', 'baab']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcdabcd', 'abcdabcdabcd', 'abcde', 'abcdeabcde']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcdabcd', 'abcdabcdabcd', 'abcde', 'abcdeabcde']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abacaba', 'abac', 'acaba', 'aba', 'ba', 'a', 'abacabaabacaba', 'abacabaabacabaabacaba']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abacaba', 'abac', 'acaba', 'aba', 'ba', 'a', 'abacabaabacaba', 'abacabaabacabaabacaba']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'anan', 'nana', 'anana', 'banana', 'bananaana', 'anana', 'ana', 'nana', 'banana']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'anan', 'nana', 'anana', 'banana', 'bananaana', 'anana', 'ana', 'nana', 'banana']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'bbccdd', 'ccddaa', 'aabb', 'bbaa', 'ccdd', 'aabbccdd', 'ddccbb', 'bbccddaa', 'aabbccbbcc', 'ccddbbcc', 'bbccddcc', 'aabbccddccdd', 'ddccbbccbbcc']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'bbccdd', 'ccddaa', 'aabb', 'bbaa', 'ccdd', 'aabbccdd', 'ddccbb', 'bbccddaa', 'aabbccbbcc', 'ccddbbcc', 'bbccddcc', 'aabbccddccdd', 'ddccbbccbbcc']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdabcdabcd', 'abcd', 'abc', 'ab', 'a', 'abcdabcd']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdabcdabcd', 'abcd', 'abc', 'ab', 'a', 'abcdabcd']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabb', 'aabbaabb', 'aabbaabbaabb', 'aabbaabbaabbaabb', 'aabbaabbaabbaabbaabb', 'aabb', 'aabbaabb', 'aabbaabbaabb', 'aabbaabbaabbaabbaabb']) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabb', 'aabbaabb', 'aabbaabbaabb', 'aabbaabbaabbaabb', 'aabbaabbaabbaabbaabb', 'aabb', 'aabbaabb', 'aabbaabbaabb', 'aabbaabbaabbaabbaabb']) == 27: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcabcabc', 'abcabc', 'abc', 'ab', 'a']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcabcabc', 'abcabc', 'abc', 'ab', 'a']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa']) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa']) == 15: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ababab', 'abab', 'aba', 'ab', 'a', 'abcabcabcabc']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ababab', 'abab', 'aba', 'ab', 'a', 'abcabcabcabc']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['longwordlongword', 'longword', 'word', 'long', 'short', 'longwordlong', 'longwordshort']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['longwordlongword', 'longword', 'word', 'long', 'short', 'longwordlong', 'longwordshort']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['racecar', 'race', 'car', 'racecar', 'racecarcar', 'racecarcarcar']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['racecar', 'race', 'car', 'racecar', 'racecarcar', 'racecarcarcar']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ababababab', 'babababa', 'abab', 'bab', 'ab', 'a', 'abababababababababab', 'abababababababababababababababababab']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ababababab', 'babababa', 'abab', 'bab', 'ab', 'a', 'abababababababababab', 'abababababababababababababababababab']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(words = ['racecar', 'racecarracecar', 'racecarracecarracecar', 'racecarracecarracecarracecar', 'racecarracecarracecarracecarracecar', 'racecarracecarracecarracecarracecarracecar']) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['racecar', 'racecarracecar', 'racecarracecarracecar', 'racecarracecarracecarracecar', 'racecarracecarracecarracecarracecar', 'racecarracecarracecarracecarracecarracecar']) == 15: {e}')
    
    total += 1
    try:
        result = candidate(words = ['repeated', 'repeatedrepeated', 'repeatedrepeatedrepeated']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repeated', 'repeatedrepeated', 'repeatedrepeatedrepeated']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['repeatrepeatrepeat', 'repeat', 'repeatrepeat', 'rep', 're', 'repeatrepeatrepeatrepeat']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repeatrepeatrepeat', 'repeat', 'repeatrepeat', 'rep', 're', 'repeatrepeatrepeatrepeat']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa']) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa']) == 15: {e}')
    
    total += 1
    try:
        result = candidate(words = ['repeatedrepeated', 'repeated', 'rep', 'eated', 'eat', 'eatereat', 'eatrepeat']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repeatedrepeated', 'repeated', 'rep', 'eated', 'eat', 'eatereat', 'eatrepeat']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['palindromemordnilap', 'mordnilap', 'ordnil', 'rnil', 'nil', 'il', 'l', 'o', 'd', 'p', 'emordnilap']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['palindromemordnilap', 'mordnilap', 'ordnil', 'rnil', 'nil', 'il', 'l', 'o', 'd', 'p', 'emordnilap']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mixedcase', 'mixed', 'mix', 'edcase', 'edc', 'ase', 'asem', 'mixedcasemixed', 'mixedcasem', 'mixedcasease']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mixedcase', 'mixed', 'mix', 'edcase', 'edc', 'ase', 'asem', 'mixedcasemixed', 'mixedcasem', 'mixedcasease']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same']) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same']) == 190: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(words = ['aaaa', 'aa', 'a']) == 0
    assert candidate(words = ['a', 'a', 'a', 'a', 'a']) == 10
    assert candidate(words = ['x', 'xx', 'xxx', 'xxxx']) == 6
    assert candidate(words = ['abab', 'ab']) == 0
    assert candidate(words = ['x', 'xx', 'xxx', 'xxxx', 'xxxxx']) == 10
    assert candidate(words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz']) == 15
    assert candidate(words = ['hello', 'hellohello', 'hellohellohello', 'he']) == 3
    assert candidate(words = ['abc', 'abcabc', 'abcd', 'abcabcabc']) == 3
    assert candidate(words = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']) == 45
    assert candidate(words = ['unique', 'uniqueword', 'uniquewordunique', 'uniq']) == 1
    assert candidate(words = ['abc', 'abcabc', 'abcabcabc']) == 3
    assert candidate(words = ['xyz', 'xyzxyz', 'zyxzyx']) == 1
    assert candidate(words = ['abcd', 'abcdeabcda', 'ab']) == 0
    assert candidate(words = ['a', 'aba', 'ababa', 'aa']) == 4
    assert candidate(words = ['pa', 'papa', 'ma', 'mama']) == 2
    assert candidate(words = ['test', 'testtest', 'testtesttest', 't']) == 3
    assert candidate(words = ['abc', 'abcabc', 'abcabcabc', 'a']) == 3
    assert candidate(words = ['pattern', 'patternpattern', 'patternpatternpattern', 'patternpatternpatternpattern']) == 6
    assert candidate(words = ['same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same']) == 45
    assert candidate(words = ['mississippi', 'issis', 'sis', 'issippi', 'iss', 'missi', 'ippi', 'pi', 'ssippi', 'mississipi', 'ississippiissippi']) == 0
    assert candidate(words = ['aaaabbbb', 'aaaabbbbcccc', 'aaaabbbbccccdddd', 'aaaabbbbccccddddaaaa', 'aa', 'bb', 'cc', 'dd']) == 0
    assert candidate(words = ['abcabcabc', 'abc', 'abcabc', 'ab', 'a', 'abcabcabcabcabc']) == 4
    assert candidate(words = ['ababab', 'abab', 'ab', 'a', 'babab', 'bab', 'b']) == 0
    assert candidate(words = ['xyzyxyzyx', 'xyzyx', 'zyxzyx', 'xyz', 'zyx', 'yzy', 'zyzy', 'yzyxyzyx', 'yzyxyzyxyzyxyzyx']) == 1
    assert candidate(words = ['repeat', 'repeatrepeat', 'repeatrepeatrepeat', 'peat', 'eat', 'at', 't', 'rep', 're', 'r', 'e', 'a', 'p', 'te']) == 3
    assert candidate(words = ['abcde', 'edcba', 'abcdeabcde', 'edcbaedcba', 'abcdeedcbaabcde']) == 3
    assert candidate(words = ['xyxyxy', 'xyxyxyxyxy', 'xyxyxyxyxyxyxy', 'xy', 'yx', 'x', 'y', 'xyxy', 'yxyx', 'xyyx', 'xxyx']) == 7
    assert candidate(words = ['prefixsuffix', 'prefixsuffixprefixsuffix', 'prefixsuffixprefixsuffixprefixsuffix']) == 3
    assert candidate(words = ['abcdeabcde', 'bcdeabcd', 'cdeabcde', 'deabcdec', 'eabcdabc', 'abcde', 'bcde', 'cde', 'de', 'e', 'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']) == 1
    assert candidate(words = ['longwordlongword', 'longwordlongwordlongword', 'longword', 'word', 'long', 'wo', 'rd', 'ngwordlongword', 'wordlongwordlong', 'ngwordlongwordngwordlongword']) == 2
    assert candidate(words = ['abcdabcdabcd', 'abcdabcd', 'abcd', 'abc', 'ab', 'a', 'abcdabcdabcdabcdabcdabcd']) == 3
    assert candidate(words = ['pattern', 'ternpat', 'ternpatpat', 'pat', 'tern', 'patternpat', 'ternpattern', 'patterntern', 'ternpatternpat']) == 3
    assert candidate(words = ['abcdabcdabcdabcd', 'abcdabcdabcd', 'abcdabcd', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd', 'abcdabcdabcdabcdabcdabcdabcdabcd', 'abcdabcdabcdabcdabcdabcdabcd', 'abcdabcdabcdabcdabcdabcd', 'abcdabcdabcdabcdabcd', 'abcdabcdabcdabcd', 'abcdabcdabcd', 'abcdabcd', 'abcd', 'abc', 'ab', 'a', 'b', 'c', 'd']) == 32
    assert candidate(words = ['aaaaa', 'aaa', 'aaaa', 'aaaaaa', 'aa']) == 4
    assert candidate(words = ['prefixsuffix', 'prefix', 'suffix', 'prefixprefix', 'suffixsuffix', 'pre', 'suf']) == 2
    assert candidate(words = ['xyxyxyxy', 'xyxy', 'xyxyxy', 'xy', 'x', 'xyxyxyxyxyxy']) == 5
    assert candidate(words = ['xyxyxyxyxy', 'xyxyxyxy', 'xyxyxy', 'xyxy', 'xy', 'x', 'y', 'xyxyxyxyxyxyxyxy', 'xyxyxyxyxyxyxyxyxyxyxy', 'xyxyxyxyxyxyxyxyxyxyxyxyxyxyxy', 'xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy']) == 26
    assert candidate(words = ['complexwordcomplexword', 'complexword', 'complex', 'com', 'co', 'complexwordcomplexwordcomplexword']) == 2
    assert candidate(words = ['aaaa', 'aa', 'a', 'aaaaaaaaaaaa', 'aaaa']) == 6
    assert candidate(words = ['abcabcabc', 'abc', 'abcabc', 'ab', 'a', 'b', 'c']) == 1
    assert candidate(words = ['abcdabcd', 'abcd', 'cdab', 'dabc', 'bcda', 'cabd', 'bacd', 'abcdabcdabcd', 'abcdabcdabcdabcd', 'abcdabcdabcdabcdabcdabcdabcdabcd']) == 9
    assert candidate(words = ['abcabcabc', 'abcabc', 'abc', 'a', 'b', 'c', 'abcabcabcabc']) == 3
    assert candidate(words = ['longprefix', 'longprefixlongprefix', 'longprefixlongprefixlongprefix']) == 3
    assert candidate(words = ['abc', 'abcabc', 'abcabcabc', 'abcabcabcabc']) == 6
    assert candidate(words = ['abcabcabc', 'abcabc', 'abc', 'a', 'b', 'c']) == 0
    assert candidate(words = ['prefixsuffix', 'prefix', 'suffix', 'prefixsuffixprefixsuffix', 'prefixprefix', 'suffixsuffix', 'prefixsuffixprefix', 'suffixprefixsuffix']) == 5
    assert candidate(words = ['repeatedrepeated', 'repeated', 'repeatedrepeatedrepeated', 'repeatedrepeatedrepeatedrepeated', 'repeatedrepeatedrepeatedrepeatedrepeated', 'repeatedrepeatedrepeated', 'repeated', 'repeatedrepeatedrepeatedrepeatedrepeated']) == 20
    assert candidate(words = ['aaaa', 'aaab', 'aabb', 'abbb', 'bbbb', 'baaa', 'baab', 'babb', 'bbba', 'bbbb', 'abab', 'baba', 'abba', 'baab', 'abba', 'baab', 'abba', 'baab']) == 10
    assert candidate(words = ['abcd', 'abcdabcd', 'abcdabcdabcd', 'abcde', 'abcdeabcde']) == 4
    assert candidate(words = ['abacaba', 'abac', 'acaba', 'aba', 'ba', 'a', 'abacabaabacaba', 'abacabaabacabaabacaba']) == 7
    assert candidate(words = ['banana', 'anan', 'nana', 'anana', 'banana', 'bananaana', 'anana', 'ana', 'nana', 'banana']) == 5
    assert candidate(words = ['aabbcc', 'bbccdd', 'ccddaa', 'aabb', 'bbaa', 'ccdd', 'aabbccdd', 'ddccbb', 'bbccddaa', 'aabbccbbcc', 'ccddbbcc', 'bbccddcc', 'aabbccddccdd', 'ddccbbccbbcc']) == 0
    assert candidate(words = ['abcdabcdabcd', 'abcd', 'abc', 'ab', 'a', 'abcdabcd']) == 1
    assert candidate(words = ['aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']) == 10
    assert candidate(words = ['aabb', 'aabbaabb', 'aabbaabbaabb', 'aabbaabbaabbaabb', 'aabbaabbaabbaabbaabb', 'aabb', 'aabbaabb', 'aabbaabbaabb', 'aabbaabbaabbaabbaabb']) == 27
    assert candidate(words = ['abcabcabc', 'abcabc', 'abc', 'ab', 'a']) == 0
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa']) == 15
    assert candidate(words = ['ababab', 'abab', 'aba', 'ab', 'a', 'abcabcabcabc']) == 0
    assert candidate(words = ['longwordlongword', 'longword', 'word', 'long', 'short', 'longwordlong', 'longwordshort']) == 1
    assert candidate(words = ['racecar', 'race', 'car', 'racecar', 'racecarcar', 'racecarcarcar']) == 1
    assert candidate(words = ['ababababab', 'babababa', 'abab', 'bab', 'ab', 'a', 'abababababababababab', 'abababababababababababababababababab']) == 7
    assert candidate(words = ['racecar', 'racecarracecar', 'racecarracecarracecar', 'racecarracecarracecarracecar', 'racecarracecarracecarracecarracecar', 'racecarracecarracecarracecarracecarracecar']) == 15
    assert candidate(words = ['repeated', 'repeatedrepeated', 'repeatedrepeatedrepeated']) == 3
    assert candidate(words = ['repeatrepeatrepeat', 'repeat', 'repeatrepeat', 'rep', 're', 'repeatrepeatrepeatrepeat']) == 4
    assert candidate(words = ['aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa']) == 15
    assert candidate(words = ['repeatedrepeated', 'repeated', 'rep', 'eated', 'eat', 'eatereat', 'eatrepeat']) == 2
    assert candidate(words = ['palindromemordnilap', 'mordnilap', 'ordnil', 'rnil', 'nil', 'il', 'l', 'o', 'd', 'p', 'emordnilap']) == 0
    assert candidate(words = ['mixedcase', 'mixed', 'mix', 'edcase', 'edc', 'ase', 'asem', 'mixedcasemixed', 'mixedcasem', 'mixedcasease']) == 1
    assert candidate(words = ['same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same']) == 190


