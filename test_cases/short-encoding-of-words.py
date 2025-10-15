def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno']) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno']) == 20: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'testing', 'tested', 'testable']) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'testing', 'tested', 'testable']) == 29: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hell', 'he', 'h']) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hell', 'he', 'h']) == 16: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aa', 'a']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aa', 'a']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'three', 'four', 'five']) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'three', 'four', 'five']) == 24: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'bcde', 'cdef', 'defg']) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'bcde', 'cdef', 'defg']) == 20: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'ple', 'le', 'e']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'ple', 'le', 'e']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'testcase', 'cases', 'ase', 'se', 'e']) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'testcase', 'cases', 'ase', 'se', 'e']) == 20: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world', 'python', 'programming']) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world', 'python', 'programming']) == 31: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'pple', 'ple', 'le', 'e']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'pple', 'ple', 'le', 'e']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'bc', 'cd', 'da']) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'bc', 'cd', 'da']) == 12: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'aaa', 'aaaa', 'aaaaa']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'aaa', 'aaaa', 'aaaaa']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'aaa', 'aaaa']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'aaa', 'aaaa']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == 52: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xy', 'y', 'z']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xy', 'y', 'z']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g']) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g']) == 14: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'dog', 'rat', 'car']) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'dog', 'rat', 'car']) == 16: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world', 'hold']) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world', 'hold']) == 17: {e}')
    
    total += 1
    try:
        result = candidate(words = ['time', 'me', 'bell']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['time', 'me', 'bell']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(words = ['at', 'ac', 'bc', 'abc']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['at', 'ac', 'bc', 'abc']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world', 'code', 'word']) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world', 'code', 'word']) == 22: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde']) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde']) == 12: {e}')
    
    total += 1
    try:
        result = candidate(words = ['t']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['t']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world', 'word', 'hello']) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world', 'word', 'hello']) == 17: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde']) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde']) == 20: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh']) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh']) == 24: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'nana', 'ana', 'na', 'a', 'nan', 'nanan']) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'nana', 'ana', 'na', 'a', 'nan', 'nanan']) == 13: {e}')
    
    total += 1
    try:
        result = candidate(words = ['sequence', 'equence', 'quence', 'uence', 'ence', 'nce', 'ce', 'e', 'sq', 'qu', 'uen', 'en']) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['sequence', 'equence', 'quence', 'uence', 'ence', 'nce', 'ce', 'e', 'sq', 'qu', 'uen', 'en']) == 19: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xy', 'xz', 'yz', 'x', 'y', 'z']) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xy', 'xz', 'yz', 'x', 'y', 'z']) == 12: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'zyx', 'yzx', 'yxz', 'zxy', 'xzy', 'zy', 'yx', 'xz', 'zx', 'xy']) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'zyx', 'yzx', 'yxz', 'zxy', 'xzy', 'zy', 'yx', 'xz', 'zx', 'xy']) == 24: {e}')
    
    total += 1
    try:
        result = candidate(words = ['random', 'andom', 'dom', 'om', 'm', 'rando', 'and', 'nd', 'd', 'rand', 'ran', 'ra', 'ndom']) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['random', 'andom', 'dom', 'om', 'm', 'rando', 'and', 'nd', 'd', 'rand', 'ran', 'ra', 'ndom']) == 25: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'bcde', 'cdef', 'defg', 'efgh']) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'bcde', 'cdef', 'defg', 'efgh']) == 25: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bc', 'c', 'abcd', 'bcd']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bc', 'c', 'abcd', 'bcd']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'ple', 'leetcode', 'code', 'ode', 'de']) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'ple', 'leetcode', 'code', 'ode', 'de']) == 15: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaaa', 'aaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaa']) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaaa', 'aaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaa']) == 16: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'aaa', 'aaaa', 'aab', 'aabaa', 'aabaaa', 'aabaaaa']) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'aaa', 'aaaa', 'aab', 'aabaa', 'aabaaa', 'aabaaaa']) == 25: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefgh', 'efgh', 'fgh', 'gh', 'h', 'abcdefghijk', 'ghijk', 'hijk', 'ijk', 'jk', 'k']) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefgh', 'efgh', 'fgh', 'gh', 'h', 'abcdefghijk', 'ghijk', 'hijk', 'ijk', 'jk', 'k']) == 21: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xylophone', 'ylophone', 'lophone', 'ophone', 'phone', 'hone', 'one', 'ne', 'e']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xylophone', 'ylophone', 'lophone', 'ophone', 'phone', 'hone', 'one', 'ne', 'e']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']) == 35: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twentyone', 'twentytwo', 'twentythree', 'twentyfour', 'twentyfive']) == 162
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twentyone', 'twentytwo', 'twentythree', 'twentyfour', 'twentyfive']) == 162: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'bcd', 'cd', 'd', 'abcde', 'bcde', 'cde', 'de', 'e']) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'bcd', 'cd', 'd', 'abcde', 'bcde', 'cde', 'de', 'e']) == 11: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hell', 'hel', 'he', 'h', 'world', 'worl', 'wor', 'wo', 'w']) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hell', 'hel', 'he', 'h', 'world', 'worl', 'wor', 'wo', 'w']) == 40: {e}')
    
    total += 1
    try:
        result = candidate(words = ['supercalifragilisticexpialidocious', 'supercalifragilisticexpialidocio', 'supercalifragilisticexpialido', 'supercalifragilisticexpalia', 'supercalifragilisticexpali', 'supercalifragilisticexpal', 'supercalifragilisticexpa', 'supercalifragilisticex', 'supercalifragilistice', 'supercalifragilistic', 'supercalifragilisti', 'supercalifragilist', 'supercalifragilis', 'supercalifragili', 'supercalifragil', 'supercalifragi', 'supercalifrag', 'supercalifra', 'supercalifr', 'supercalif', 'supercali', 'supercal', 'superc', 'super', 'supe', 'sup', 'su', 's']) == 469
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['supercalifragilisticexpialidocious', 'supercalifragilisticexpialidocio', 'supercalifragilisticexpialido', 'supercalifragilisticexpalia', 'supercalifragilisticexpali', 'supercalifragilisticexpal', 'supercalifragilisticexpa', 'supercalifragilisticex', 'supercalifragilistice', 'supercalifragilistic', 'supercalifragilisti', 'supercalifragilist', 'supercalifragilis', 'supercalifragili', 'supercalifragil', 'supercalifragi', 'supercalifrag', 'supercalifra', 'supercalifr', 'supercalif', 'supercali', 'supercal', 'superc', 'super', 'supe', 'sup', 'su', 's']) == 469: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'bcd', 'cd', 'd', 'a', 'ab', 'abc', 'bc', 'c']) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'bcd', 'cd', 'd', 'a', 'ab', 'abc', 'bc', 'c']) == 14: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abracadabra', 'bracadabr', 'racadabr', 'acadabr', 'cadabr', 'adabr', 'dabr', 'abr', 'br', 'r']) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abracadabra', 'bracadabr', 'racadabr', 'acadabr', 'cadabr', 'adabr', 'dabr', 'abr', 'br', 'r']) == 22: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xylophone', 'ylophone', 'lophone', 'ophone', 'phone', 'hone', 'one', 'ne', 'e', 'x']) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xylophone', 'ylophone', 'lophone', 'ophone', 'phone', 'hone', 'one', 'ne', 'e', 'x']) == 12: {e}')
    
    total += 1
    try:
        result = candidate(words = ['qwerty', 'werty', 'erty', 'rty', 'ty', 'y', 'qwertyuiop', 'ertyuiop', 'rtyuiop', 'tyuiop', 'yuiop', 'uiop', 'iop', 'op', 'p']) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['qwerty', 'werty', 'erty', 'rty', 'ty', 'y', 'qwertyuiop', 'ertyuiop', 'rtyuiop', 'tyuiop', 'yuiop', 'uiop', 'iop', 'op', 'p']) == 18: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaaaa', 'aaaaa', 'aaaa', 'aaa', 'aa', 'a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaaaa', 'aaaaa', 'aaaa', 'aaa', 'aa', 'a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zebra', 'bra', 'ra', 'a', 'abacaxi', 'bacaxi', 'acaxi', 'caxi', 'axi', 'xi', 'i']) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zebra', 'bra', 'ra', 'a', 'abacaxi', 'bacaxi', 'acaxi', 'caxi', 'axi', 'xi', 'i']) == 14: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z', 'zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z', 'zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'abc', 'abcd', 'abcde', 'abcdef']) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'abc', 'abcd', 'abcde', 'abcdef']) == 25: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'bcd', 'cd', 'd', 'efgh', 'fgh', 'gh', 'h', 'ijkl', 'jkl', 'kl', 'l']) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'bcd', 'cd', 'd', 'efgh', 'fgh', 'gh', 'h', 'ijkl', 'jkl', 'kl', 'l']) == 15: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'testing', 'tests', 'tes', 'te', 't', 'testcase', 'cases', 'ase', 'se', 'e']) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'testing', 'tests', 'tes', 'te', 't', 'testcase', 'cases', 'ase', 'se', 'e']) == 41: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'anana', 'nana', 'ana', 'na', 'a', 'ban']) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'anana', 'nana', 'ana', 'na', 'a', 'ban']) == 11: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'bcd', 'cd', 'd', 'def', 'ef', 'f', 'fgh', 'gh', 'h']) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'bcd', 'cd', 'd', 'def', 'ef', 'f', 'fgh', 'gh', 'h']) == 13: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'anana', 'nana', 'ana', 'na', 'a', 'nabana', 'bananab']) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'anana', 'nana', 'ana', 'na', 'a', 'nabana', 'bananab']) == 22: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']) == 42: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'logarithm', 'rhythm', 'syzygy', 'zymurgy', 'zymurgy', 'zymurgy', 'zymurgy', 'zymurgy']) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'logarithm', 'rhythm', 'syzygy', 'zymurgy', 'zymurgy', 'zymurgy', 'zymurgy', 'zymurgy']) == 42: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jkl', 'kl', 'l']) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jkl', 'kl', 'l']) == 45: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 78: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hell', 'helo', 'he', 'h', 'e']) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hell', 'helo', 'he', 'h', 'e']) == 21: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abacaxi', 'bacaxi', 'caxi', 'axi', 'xi', 'i']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abacaxi', 'bacaxi', 'caxi', 'axi', 'xi', 'i']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'zyx', 'yzx', 'yxz', 'xzy', 'zxy']) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'zyx', 'yzx', 'yxz', 'xzy', 'zxy']) == 24: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'rhythm', 'rhythmically', 'thym', 'hym', 'ym', 'm']) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'rhythm', 'rhythmically', 'thym', 'hym', 'ym', 'm']) == 35: {e}')
    
    total += 1
    try:
        result = candidate(words = ['flower', 'flow', 'flight', 'flighting', 'flour']) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['flower', 'flow', 'flight', 'flighting', 'flour']) == 35: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'ord', 'rd', 'd', 'word', 'ord', 'rd', 'd', 'word', 'ord', 'rd', 'd', 'word', 'ord', 'rd', 'd', 'word', 'ord', 'rd', 'd']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'ord', 'rd', 'd', 'word', 'ord', 'rd', 'd', 'word', 'ord', 'rd', 'd', 'word', 'ord', 'rd', 'd', 'word', 'ord', 'rd', 'd']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'peel', 'pale', 'ale', 'le']) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'peel', 'pale', 'ale', 'le']) == 16: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'ple', 'le', 'e', 'app', 'ppl']) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'ple', 'le', 'e', 'app', 'ppl']) == 14: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefgh', 'bcdefghi', 'cdefghij', 'defghijk', 'efghijkl', 'fghijklm', 'ghijklmn', 'hijklmno', 'ijklmnop', 'jklmnopq']) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefgh', 'bcdefghi', 'cdefghij', 'defghijk', 'efghijkl', 'fghijklm', 'ghijklmn', 'hijklmno', 'ijklmnop', 'jklmnopq']) == 90: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'bc', 'abc', 'abcd', 'abcde']) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'bc', 'abc', 'abcd', 'abcde']) == 18: {e}')
    
    total += 1
    try:
        result = candidate(words = ['overlap', 'lap', 'ap', 'p', 'nolap', 'olap', 'lapo', 'lapor', 'laporator', 'laporatory']) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['overlap', 'lap', 'ap', 'p', 'nolap', 'olap', 'lapo', 'lapor', 'laporator', 'laporatory']) == 46: {e}')
    
    total += 1
    try:
        result = candidate(words = ['panorama', 'anorama', 'norama', 'orama', 'rama', 'ama', 'ma', 'a', 'planet', 'lanet', 'anet', 'net', 'et', 't']) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['panorama', 'anorama', 'norama', 'orama', 'rama', 'ama', 'ma', 'a', 'planet', 'lanet', 'anet', 'net', 'et', 't']) == 16: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'ple', 'le', 'e', 'app', 'pple', 'plea']) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'ple', 'le', 'e', 'app', 'pple', 'plea']) == 15: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zebra', 'ebra', 'bra', 'ra', 'a', 'z']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zebra', 'ebra', 'bra', 'ra', 'a', 'z']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'dog', 'god', 'tac', 'act', 'gat']) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'dog', 'god', 'tac', 'act', 'gat']) == 24: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg']) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg']) == 20: {e}')
    
    total += 1
    try:
        result = candidate(words = ['coding', 'ing', 'ode', 'de', 'e']) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['coding', 'ing', 'ode', 'de', 'e']) == 11: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb', 'bbb', 'bbb']) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb', 'bbb', 'bbb']) == 32: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'bcd', 'cd', 'd', 'abcds', 'bcde', 'cde', 'de', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'bcd', 'cd', 'd', 'abcds', 'bcde', 'cde', 'de', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']) == 96: {e}')
    
    total += 1
    try:
        result = candidate(words = ['unique', 'un', 'iq', 'que', 'eue', 'eu', 'ue', 'eq', 'qu', 'uq']) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['unique', 'un', 'iq', 'que', 'eue', 'eu', 'ue', 'eq', 'qu', 'uq']) == 29: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'ana', 'nana', 'anaconda', 'conda']) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'ana', 'nana', 'anaconda', 'conda']) == 16: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zebra', 'ebra', 'bra', 'ra', 'a', 'cab', 'ab', 'b']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zebra', 'ebra', 'bra', 'ra', 'a', 'cab', 'ab', 'b']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'ming', 'gram', 'ing', 'am', 'm']) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'ming', 'gram', 'ing', 'am', 'm']) == 17: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']) == 65: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'lgorithm', 'gorithm', 'orithm', 'rithm', 'ithm', 'thm', 'hm', 'm']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'lgorithm', 'gorithm', 'orithm', 'rithm', 'ithm', 'thm', 'hm', 'm']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'lgorithm', 'gorithm', 'rhythm', 'hythm', 'hythm', 'thm', 'hm', 'm', 'a']) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'lgorithm', 'gorithm', 'rhythm', 'hythm', 'hythm', 'thm', 'hm', 'm', 'a']) == 19: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefgh', 'bcdefgh', 'cdefgh', 'defgh', 'efgh', 'fgh', 'gh', 'h']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefgh', 'bcdefgh', 'cdefgh', 'defgh', 'efgh', 'fgh', 'gh', 'h']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(words = ['sun', 'un', 'n', 'moon', 'oon', 'on', 'noon', 'oon', 'on', 'n']) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['sun', 'un', 'n', 'moon', 'oon', 'on', 'noon', 'oon', 'on', 'n']) == 14: {e}')
    
    total += 1
    try:
        result = candidate(words = ['longest', 'longer', 'long', 'lo', 'l', 'longestword', 'word', 'ord', 'rd', 'd']) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['longest', 'longer', 'long', 'lo', 'l', 'longestword', 'word', 'ord', 'rd', 'd']) == 37: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'peach', 'pear', 'leap', 'lead', 'meat', 'heat', 'seat']) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'peach', 'pear', 'leap', 'lead', 'meat', 'heat', 'seat']) == 42: {e}')
    
    total += 1
    try:
        result = candidate(words = ['watermelon', 'atermelon', 'termelon', 'ermelon', 'rmelon', 'melon', 'elon', 'lon', 'on', 'n', 'w']) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['watermelon', 'atermelon', 'termelon', 'ermelon', 'rmelon', 'melon', 'elon', 'lon', 'on', 'n', 'w']) == 13: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'aaab', 'aabb', 'abbb', 'bbbb']) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'aaab', 'aabb', 'abbb', 'bbbb']) == 25: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'ananas', 'nana', 'ana', 'na', 'a', 'banana', 'ananas', 'nana', 'ana', 'na', 'a']) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'ananas', 'nana', 'ana', 'na', 'a', 'banana', 'ananas', 'nana', 'ana', 'na', 'a']) == 14: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'ffff', 'gggg', 'hhhh', 'iiii', 'jjjj', 'kkkk', 'llll', 'mmmm', 'nnnn', 'oooo', 'pppp', 'qqqq', 'rrrr', 'ssss', 'tttt']) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'ffff', 'gggg', 'hhhh', 'iiii', 'jjjj', 'kkkk', 'llll', 'mmmm', 'nnnn', 'oooo', 'pppp', 'qqqq', 'rrrr', 'ssss', 'tttt']) == 100: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aab', 'aac', 'aba', 'abc', 'aca', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc']) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aab', 'aac', 'aba', 'abc', 'aca', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc']) == 96: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaaa', 'aaa', 'aa', 'a', 'aaaaa']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaaa', 'aaa', 'aa', 'a', 'aaaaa']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'nana', 'ana', 'na', 'a', 'anana', 'ananana', 'anananana', 'ananananana']) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'nana', 'ana', 'na', 'a', 'anana', 'ananana', 'anananana', 'ananananana']) == 19: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdexyz', 'bcdexyz', 'cdexyz', 'dexyz', 'exyz', 'xyz', 'yz', 'z']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdexyz', 'bcdexyz', 'cdexyz', 'dexyz', 'exyz', 'xyz', 'yz', 'z']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'anana', 'nana', 'ana', 'na', 'a', 'cat', 'at', 't']) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'anana', 'nana', 'ana', 'na', 'a', 'cat', 'at', 't']) == 11: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'yz', 'z', 'xy', 'x', 'yx', 'zxy', 'zyx', 'yxz', 'zyxz', 'xyzz', 'zyzzz', 'zyzyz']) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'yz', 'z', 'xy', 'x', 'yx', 'zxy', 'zyx', 'yxz', 'zyxz', 'xyzz', 'zyzzz', 'zyzyz']) == 34: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefgh', 'bcdefghi', 'cdefghij', 'defghijk', 'efghijkl', 'fghijklm', 'ghijklmn', 'hijklmno', 'ijklmnop', 'jklmnopq', 'klmnopqr', 'lmnopqrs', 'mnopqrst', 'nopqrstu', 'opqrstuv', 'pqrstuvw', 'qrstuvwx', 'rstuvwxy', 'stuvwxyz']) == 171
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefgh', 'bcdefghi', 'cdefghij', 'defghijk', 'efghijkl', 'fghijklm', 'ghijklmn', 'hijklmno', 'ijklmnop', 'jklmnopq', 'klmnopqr', 'lmnopqrs', 'mnopqrst', 'nopqrstu', 'opqrstuv', 'pqrstuvw', 'qrstuvwx', 'rstuvwxy', 'stuvwxyz']) == 171: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'gramming', 'mming', 'ming', 'ing', 'ng', 'g']) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'gramming', 'mming', 'ming', 'ing', 'ng', 'g']) == 12: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'bcdef', 'cdefg', 'defgh', 'efghi', 'fghij', 'ghijk', 'hijkl', 'ijklm', 'jklmn', 'klmno', 'lmnop', 'mnopq', 'nopqr', 'opqrs', 'pqrst', 'qrstu', 'rstuv', 'stuvw', 'tuvwx', 'uvwxy', 'vwxyz', 'wxyz', 'xyz', 'yz', 'z']) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'bcdef', 'cdefg', 'defgh', 'efghi', 'fghij', 'ghijk', 'hijkl', 'ijklm', 'jklmn', 'klmno', 'lmnop', 'mnopq', 'nopqr', 'opqrs', 'pqrst', 'qrstu', 'rstuv', 'stuvw', 'tuvwx', 'uvwxy', 'vwxyz', 'wxyz', 'xyz', 'yz', 'z']) == 132: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'app', 'ple', 'le', 'e']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'app', 'ple', 'le', 'e']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(words = ['pqr', 'pqs', 'prq', 'prs', 'psq', 'psr', 'rpq', 'rps', 'rsp', 'rsq', 'spq', 'spr']) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['pqr', 'pqs', 'prq', 'prs', 'psq', 'psr', 'rpq', 'rps', 'rsp', 'rsq', 'spq', 'spr']) == 48: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij', 'jk', 'kl', 'lm', 'mn', 'no', 'op', 'pq', 'qr', 'rs', 'st', 'tu', 'uv', 'vw', 'wx', 'xy', 'yz']) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij', 'jk', 'kl', 'lm', 'mn', 'no', 'op', 'pq', 'qr', 'rs', 'st', 'tu', 'uv', 'vw', 'wx', 'xy', 'yz']) == 75: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'ple', 'le', 'e', 'orange', 'range', 'age', 'ge']) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'ple', 'le', 'e', 'orange', 'range', 'age', 'ge']) == 17: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'bcd', 'cd', 'd', 'abcd', 'bcd', 'cd', 'd']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'bcd', 'cd', 'd', 'abcd', 'bcd', 'cd', 'd']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'ple', 'app', 'le', 'p', 'l', 'e', 'a']) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'ple', 'app', 'le', 'p', 'l', 'e', 'a']) == 14: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']) == 96: {e}')
    
    total += 1
    try:
        result = candidate(words = ['optimization', 'ptimization', 'timization', 'imization', 'mization', 'ization', 'zation', 'ation', 'tion', 'ion', 'on', 'n']) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['optimization', 'ptimization', 'timization', 'imization', 'mization', 'ization', 'zation', 'ation', 'tion', 'ion', 'on', 'n']) == 13: {e}')
    
    total += 1
    try:
        result = candidate(words = ['sequence', 'equence', 'quence', 'uence', 'ence', 'nce', 'ce', 'e', 's', 'sequ', 'seq']) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['sequence', 'equence', 'quence', 'uence', 'ence', 'nce', 'ce', 'e', 's', 'sequ', 'seq']) == 20: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefg', 'cdefg', 'defg', 'efg', 'fg', 'g']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefg', 'cdefg', 'defg', 'efg', 'fg', 'g']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abracadabra', 'racadabra', 'cadabra', 'adabra', 'dabra', 'abra', 'bra', 'ra', 'a']) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abracadabra', 'racadabra', 'cadabra', 'adabra', 'dabra', 'abra', 'bra', 'ra', 'a']) == 12: {e}')
    
    total += 1
    try:
        result = candidate(words = ['kitten', 'ten', 'en', 'n', 'sitting', 'ting', 'ing', 'ng', 'g']) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['kitten', 'ten', 'en', 'n', 'sitting', 'ting', 'ing', 'ng', 'g']) == 15: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno']) == 20
    assert candidate(words = ['test', 'testing', 'tested', 'testable']) == 29
    assert candidate(words = ['hello', 'hell', 'he', 'h']) == 16
    assert candidate(words = ['aaa', 'aa', 'a']) == 4
    assert candidate(words = ['one', 'two', 'three', 'four', 'five']) == 24
    assert candidate(words = ['abcd', 'bcde', 'cdef', 'defg']) == 20
    assert candidate(words = ['apple', 'ple', 'le', 'e']) == 6
    assert candidate(words = ['test', 'testcase', 'cases', 'ase', 'se', 'e']) == 20
    assert candidate(words = ['hello', 'world', 'python', 'programming']) == 31
    assert candidate(words = ['apple', 'pple', 'ple', 'le', 'e']) == 6
    assert candidate(words = ['ab', 'bc', 'cd', 'da']) == 12
    assert candidate(words = ['aa', 'aaa', 'aaaa', 'aaaaa']) == 6
    assert candidate(words = ['aa', 'aaa', 'aaaa']) == 5
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == 52
    assert candidate(words = ['xyz', 'xy', 'y', 'z']) == 7
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g']) == 14
    assert candidate(words = ['cat', 'dog', 'rat', 'car']) == 16
    assert candidate(words = ['hello', 'world', 'hold']) == 17
    assert candidate(words = ['time', 'me', 'bell']) == 10
    assert candidate(words = ['at', 'ac', 'bc', 'abc']) == 10
    assert candidate(words = ['hello', 'world', 'code', 'word']) == 22
    assert candidate(words = ['abc', 'bcd', 'cde']) == 12
    assert candidate(words = ['t']) == 2
    assert candidate(words = ['hello', 'world', 'word', 'hello']) == 17
    assert candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde']) == 20
    assert candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh']) == 24
    assert candidate(words = ['banana', 'nana', 'ana', 'na', 'a', 'nan', 'nanan']) == 13
    assert candidate(words = ['sequence', 'equence', 'quence', 'uence', 'ence', 'nce', 'ce', 'e', 'sq', 'qu', 'uen', 'en']) == 19
    assert candidate(words = ['xyz', 'xy', 'xz', 'yz', 'x', 'y', 'z']) == 12
    assert candidate(words = ['xyz', 'zyx', 'yzx', 'yxz', 'zxy', 'xzy', 'zy', 'yx', 'xz', 'zx', 'xy']) == 24
    assert candidate(words = ['random', 'andom', 'dom', 'om', 'm', 'rando', 'and', 'nd', 'd', 'rand', 'ran', 'ra', 'ndom']) == 25
    assert candidate(words = ['abcd', 'bcde', 'cdef', 'defg', 'efgh']) == 25
    assert candidate(words = ['abc', 'bc', 'c', 'abcd', 'bcd']) == 9
    assert candidate(words = ['apple', 'ple', 'leetcode', 'code', 'ode', 'de']) == 15
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaaa', 'aaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaa']) == 16
    assert candidate(words = ['aa', 'aaa', 'aaaa', 'aab', 'aabaa', 'aabaaa', 'aabaaaa']) == 25
    assert candidate(words = ['abcdefgh', 'efgh', 'fgh', 'gh', 'h', 'abcdefghijk', 'ghijk', 'hijk', 'ijk', 'jk', 'k']) == 21
    assert candidate(words = ['xylophone', 'ylophone', 'lophone', 'ophone', 'phone', 'hone', 'one', 'ne', 'e']) == 10
    assert candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']) == 35
    assert candidate(words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twentyone', 'twentytwo', 'twentythree', 'twentyfour', 'twentyfive']) == 162
    assert candidate(words = ['abcd', 'bcd', 'cd', 'd', 'abcde', 'bcde', 'cde', 'de', 'e']) == 11
    assert candidate(words = ['hello', 'hell', 'hel', 'he', 'h', 'world', 'worl', 'wor', 'wo', 'w']) == 40
    assert candidate(words = ['supercalifragilisticexpialidocious', 'supercalifragilisticexpialidocio', 'supercalifragilisticexpialido', 'supercalifragilisticexpalia', 'supercalifragilisticexpali', 'supercalifragilisticexpal', 'supercalifragilisticexpa', 'supercalifragilisticex', 'supercalifragilistice', 'supercalifragilistic', 'supercalifragilisti', 'supercalifragilist', 'supercalifragilis', 'supercalifragili', 'supercalifragil', 'supercalifragi', 'supercalifrag', 'supercalifra', 'supercalifr', 'supercalif', 'supercali', 'supercal', 'superc', 'super', 'supe', 'sup', 'su', 's']) == 469
    assert candidate(words = ['abcd', 'bcd', 'cd', 'd', 'a', 'ab', 'abc', 'bc', 'c']) == 14
    assert candidate(words = ['abracadabra', 'bracadabr', 'racadabr', 'acadabr', 'cadabr', 'adabr', 'dabr', 'abr', 'br', 'r']) == 22
    assert candidate(words = ['xylophone', 'ylophone', 'lophone', 'ophone', 'phone', 'hone', 'one', 'ne', 'e', 'x']) == 12
    assert candidate(words = ['qwerty', 'werty', 'erty', 'rty', 'ty', 'y', 'qwertyuiop', 'ertyuiop', 'rtyuiop', 'tyuiop', 'yuiop', 'uiop', 'iop', 'op', 'p']) == 18
    assert candidate(words = ['aaaaaa', 'aaaaa', 'aaaa', 'aaa', 'aa', 'a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa']) == 7
    assert candidate(words = ['zebra', 'bra', 'ra', 'a', 'abacaxi', 'bacaxi', 'acaxi', 'caxi', 'axi', 'xi', 'i']) == 14
    assert candidate(words = ['zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z', 'zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z']) == 8
    assert candidate(words = ['ab', 'abc', 'abcd', 'abcde', 'abcdef']) == 25
    assert candidate(words = ['abcd', 'bcd', 'cd', 'd', 'efgh', 'fgh', 'gh', 'h', 'ijkl', 'jkl', 'kl', 'l']) == 15
    assert candidate(words = ['test', 'testing', 'tests', 'tes', 'te', 't', 'testcase', 'cases', 'ase', 'se', 'e']) == 41
    assert candidate(words = ['banana', 'anana', 'nana', 'ana', 'na', 'a', 'ban']) == 11
    assert candidate(words = ['abcd', 'bcd', 'cd', 'd', 'def', 'ef', 'f', 'fgh', 'gh', 'h']) == 13
    assert candidate(words = ['banana', 'anana', 'nana', 'ana', 'na', 'a', 'nabana', 'bananab']) == 22
    assert candidate(words = ['ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']) == 42
    assert candidate(words = ['algorithm', 'logarithm', 'rhythm', 'syzygy', 'zymurgy', 'zymurgy', 'zymurgy', 'zymurgy', 'zymurgy']) == 42
    assert candidate(words = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jkl', 'kl', 'l']) == 45
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 78
    assert candidate(words = ['hello', 'hell', 'helo', 'he', 'h', 'e']) == 21
    assert candidate(words = ['abacaxi', 'bacaxi', 'caxi', 'axi', 'xi', 'i']) == 8
    assert candidate(words = ['xyz', 'zyx', 'yzx', 'yxz', 'xzy', 'zxy']) == 24
    assert candidate(words = ['algorithm', 'rhythm', 'rhythmically', 'thym', 'hym', 'ym', 'm']) == 35
    assert candidate(words = ['flower', 'flow', 'flight', 'flighting', 'flour']) == 35
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa']) == 8
    assert candidate(words = ['word', 'ord', 'rd', 'd', 'word', 'ord', 'rd', 'd', 'word', 'ord', 'rd', 'd', 'word', 'ord', 'rd', 'd', 'word', 'ord', 'rd', 'd']) == 5
    assert candidate(words = ['apple', 'peel', 'pale', 'ale', 'le']) == 16
    assert candidate(words = ['apple', 'ple', 'le', 'e', 'app', 'ppl']) == 14
    assert candidate(words = ['abcdefgh', 'bcdefghi', 'cdefghij', 'defghijk', 'efghijkl', 'fghijklm', 'ghijklmn', 'hijklmno', 'ijklmnop', 'jklmnopq']) == 90
    assert candidate(words = ['ab', 'bc', 'abc', 'abcd', 'abcde']) == 18
    assert candidate(words = ['overlap', 'lap', 'ap', 'p', 'nolap', 'olap', 'lapo', 'lapor', 'laporator', 'laporatory']) == 46
    assert candidate(words = ['panorama', 'anorama', 'norama', 'orama', 'rama', 'ama', 'ma', 'a', 'planet', 'lanet', 'anet', 'net', 'et', 't']) == 16
    assert candidate(words = ['apple', 'ple', 'le', 'e', 'app', 'pple', 'plea']) == 15
    assert candidate(words = ['zebra', 'ebra', 'bra', 'ra', 'a', 'z']) == 8
    assert candidate(words = ['cat', 'dog', 'god', 'tac', 'act', 'gat']) == 24
    assert candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg']) == 20
    assert candidate(words = ['coding', 'ing', 'ode', 'de', 'e']) == 11
    assert candidate(words = ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb', 'bbb', 'bbb']) == 32
    assert candidate(words = ['abcd', 'bcd', 'cd', 'd', 'abcds', 'bcde', 'cde', 'de', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']) == 96
    assert candidate(words = ['unique', 'un', 'iq', 'que', 'eue', 'eu', 'ue', 'eq', 'qu', 'uq']) == 29
    assert candidate(words = ['banana', 'ana', 'nana', 'anaconda', 'conda']) == 16
    assert candidate(words = ['zebra', 'ebra', 'bra', 'ra', 'a', 'cab', 'ab', 'b']) == 10
    assert candidate(words = ['programming', 'ming', 'gram', 'ing', 'am', 'm']) == 17
    assert candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']) == 65
    assert candidate(words = ['algorithm', 'lgorithm', 'gorithm', 'orithm', 'rithm', 'ithm', 'thm', 'hm', 'm']) == 10
    assert candidate(words = ['algorithm', 'lgorithm', 'gorithm', 'rhythm', 'hythm', 'hythm', 'thm', 'hm', 'm', 'a']) == 19
    assert candidate(words = ['abcdefgh', 'bcdefgh', 'cdefgh', 'defgh', 'efgh', 'fgh', 'gh', 'h']) == 9
    assert candidate(words = ['sun', 'un', 'n', 'moon', 'oon', 'on', 'noon', 'oon', 'on', 'n']) == 14
    assert candidate(words = ['longest', 'longer', 'long', 'lo', 'l', 'longestword', 'word', 'ord', 'rd', 'd']) == 37
    assert candidate(words = ['apple', 'peach', 'pear', 'leap', 'lead', 'meat', 'heat', 'seat']) == 42
    assert candidate(words = ['watermelon', 'atermelon', 'termelon', 'ermelon', 'rmelon', 'melon', 'elon', 'lon', 'on', 'n', 'w']) == 13
    assert candidate(words = ['aaaa', 'aaab', 'aabb', 'abbb', 'bbbb']) == 25
    assert candidate(words = ['banana', 'ananas', 'nana', 'ana', 'na', 'a', 'banana', 'ananas', 'nana', 'ana', 'na', 'a']) == 14
    assert candidate(words = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'ffff', 'gggg', 'hhhh', 'iiii', 'jjjj', 'kkkk', 'llll', 'mmmm', 'nnnn', 'oooo', 'pppp', 'qqqq', 'rrrr', 'ssss', 'tttt']) == 100
    assert candidate(words = ['aaa', 'aab', 'aac', 'aba', 'abc', 'aca', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc']) == 96
    assert candidate(words = ['aaaa', 'aaa', 'aa', 'a', 'aaaaa']) == 6
    assert candidate(words = ['banana', 'nana', 'ana', 'na', 'a', 'anana', 'ananana', 'anananana', 'ananananana']) == 19
    assert candidate(words = ['abcdexyz', 'bcdexyz', 'cdexyz', 'dexyz', 'exyz', 'xyz', 'yz', 'z']) == 9
    assert candidate(words = ['banana', 'anana', 'nana', 'ana', 'na', 'a', 'cat', 'at', 't']) == 11
    assert candidate(words = ['xyz', 'yz', 'z', 'xy', 'x', 'yx', 'zxy', 'zyx', 'yxz', 'zyxz', 'xyzz', 'zyzzz', 'zyzyz']) == 34
    assert candidate(words = ['abcdefgh', 'bcdefghi', 'cdefghij', 'defghijk', 'efghijkl', 'fghijklm', 'ghijklmn', 'hijklmno', 'ijklmnop', 'jklmnopq', 'klmnopqr', 'lmnopqrs', 'mnopqrst', 'nopqrstu', 'opqrstuv', 'pqrstuvw', 'qrstuvwx', 'rstuvwxy', 'stuvwxyz']) == 171
    assert candidate(words = ['programming', 'gramming', 'mming', 'ming', 'ing', 'ng', 'g']) == 12
    assert candidate(words = ['abcde', 'bcdef', 'cdefg', 'defgh', 'efghi', 'fghij', 'ghijk', 'hijkl', 'ijklm', 'jklmn', 'klmno', 'lmnop', 'mnopq', 'nopqr', 'opqrs', 'pqrst', 'qrstu', 'rstuv', 'stuvw', 'tuvwx', 'uvwxy', 'vwxyz', 'wxyz', 'xyz', 'yz', 'z']) == 132
    assert candidate(words = ['apple', 'app', 'ple', 'le', 'e']) == 10
    assert candidate(words = ['pqr', 'pqs', 'prq', 'prs', 'psq', 'psr', 'rpq', 'rps', 'rsp', 'rsq', 'spq', 'spr']) == 48
    assert candidate(words = ['ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij', 'jk', 'kl', 'lm', 'mn', 'no', 'op', 'pq', 'qr', 'rs', 'st', 'tu', 'uv', 'vw', 'wx', 'xy', 'yz']) == 75
    assert candidate(words = ['apple', 'ple', 'le', 'e', 'orange', 'range', 'age', 'ge']) == 17
    assert candidate(words = ['abcd', 'bcd', 'cd', 'd', 'abcd', 'bcd', 'cd', 'd']) == 5
    assert candidate(words = ['apple', 'ple', 'app', 'le', 'p', 'l', 'e', 'a']) == 14
    assert candidate(words = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']) == 96
    assert candidate(words = ['optimization', 'ptimization', 'timization', 'imization', 'mization', 'ization', 'zation', 'ation', 'tion', 'ion', 'on', 'n']) == 13
    assert candidate(words = ['sequence', 'equence', 'quence', 'uence', 'ence', 'nce', 'ce', 'e', 's', 'sequ', 'seq']) == 20
    assert candidate(words = ['abcdefg', 'cdefg', 'defg', 'efg', 'fg', 'g']) == 8
    assert candidate(words = ['abracadabra', 'racadabra', 'cadabra', 'adabra', 'dabra', 'abra', 'bra', 'ra', 'a']) == 12
    assert candidate(words = ['kitten', 'ten', 'en', 'n', 'sitting', 'ting', 'ing', 'ng', 'g']) == 15


