def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "aaaa",words = ['aa', 'aa']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa",words = ['aa', 'aa']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",words = ['he', 'll', 'o']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",words = ['he', 'll', 'o']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",words = ['a']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",words = ['a']) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",words = ['a', 'bc']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",words = ['a', 'bc']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",words = ['a', 'b', 'c']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",words = ['a', 'b', 'c']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",words = ['a', 'bcd']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",words = ['a', 'bcd']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "cat",words = ['ca', 't']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cat",words = ['ca', 't']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",words = ['abc', 'd']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",words = ['abc', 'd']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",words = ['he', 'l', 'lo']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",words = ['he', 'l', 'lo']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",words = ['ab', 'c']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",words = ['ab', 'c']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "",words = ['a', 'b', 'c']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",words = ['a', 'b', 'c']) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "iloveleetcode",words = ['apples', 'i', 'love', 'leetcode']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "iloveleetcode",words = ['apples', 'i', 'love', 'leetcode']) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",words = ['he', 'llo']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",words = ['he', 'llo']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",words = ['a', 'b', 'c', 'd']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",words = ['a', 'b', 'c', 'd']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",words = ['ab', 'cd']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",words = ['ab', 'cd']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",words = ['abcd']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",words = ['abcd']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "iloveleetcode",words = ['i', 'love', 'leetcode', 'apples']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "iloveleetcode",words = ['i', 'love', 'leetcode', 'apples']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",words = ['x', 'y', 'z']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",words = ['x', 'y', 'z']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",words = ['a', 'b', 'c']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",words = ['a', 'b', 'c']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",words = ['abc']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",words = ['abc']) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "complexprefixstring",words = ['complex', 'prefix', 'string', 'extra']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "complexprefixstring",words = ['complex', 'prefix', 'string', 'extra']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aquickbrownfox",words = ['a', 'quick', 'brown', 'fox', 'jumps']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aquickbrownfox",words = ['a', 'quick', 'brown', 'fox', 'jumps']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "onetwothree",words = ['one', 'two', 'three', 'four', 'five']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "onetwothree",words = ['one', 'two', 'three', 'four', 'five']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "algorithm",words = ['algo', 'r', 'ith', 'm']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "algorithm",words = ['algo', 'r', 'ith', 'm']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "python",words = ['py', 'th', 'on', 'n']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "python",words = ['py', 'th', 'on', 'n']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "complexprefix",words = ['com', 'ple', 'xpre', 'fix']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "complexprefix",words = ['com', 'ple', 'xpre', 'fix']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "concatenate",words = ['con', 'cat', 'en', 'ate']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "concatenate",words = ['con', 'cat', 'en', 'ate']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "algorithms",words = ['algo', 'rithm', 's', 'data']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "algorithms",words = ['algo', 'rithm', 's', 'data']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra",words = ['abra', 'ca', 'da', 'bra', 'bra']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra",words = ['abra', 'ca', 'da', 'bra', 'bra']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "substring",words = ['sub', 'str', 'ing', 'example']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "substring",words = ['sub', 'str', 'ing', 'example']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "onetwothreefour",words = ['one', 'two', 'three', 'four', 'five']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "onetwothreefour",words = ['one', 'two', 'three', 'four', 'five']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",words = ['x', 'y', 'z', 'w']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",words = ['x', 'y', 'z', 'w']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "prefixstring",words = ['pre', 'fix', 'string']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "prefixstring",words = ['pre', 'fix', 'string']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",words = ['pro', 'gram', 'ming']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",words = ['pro', 'gram', 'ming']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "concatenate",words = ['con', 'cat', 'e', 'nate']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "concatenate",words = ['con', 'cat', 'e', 'nate']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisatest",words = ['this', 'is', 'a', 'test', 'case']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisatest",words = ['this', 'is', 'a', 'test', 'case']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "substring",words = ['sub', 'string', 'abc']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "substring",words = ['sub', 'string', 'abc']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",words = ['mis', 'si', 'ssippi', 'p']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",words = ['mis', 'si', 'ssippi', 'p']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "prefixprefix",words = ['pre', 'fix', 'pre', 'fix', 'pre', 'fix']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "prefixprefix",words = ['pre', 'fix', 'pre', 'fix', 'pre', 'fix']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",words = ['a', 'b', 'c', 'def', 'ghi']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",words = ['a', 'b', 'c', 'def', 'ghi']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisatest",words = ['this', 'is', 'a', 'test', 'case']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisatest",words = ['this', 'is', 'a', 'test', 'case']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",words = ['a', 'b', 'c', 'd', 'e', 'f', 'g']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",words = ['a', 'b', 'c', 'd', 'e', 'f', 'g']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbccc",words = ['aaa', 'bbb', 'ccc', 'ddd']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbccc",words = ['aaa', 'bbb', 'ccc', 'ddd']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",words = ['h', 'he', 'hel', 'hell', 'hello']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",words = ['h', 'he', 'hel', 'hell', 'hello']) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabc",words = ['ab', 'c', 'd', 'abc', 'def']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabc",words = ['ab', 'c', 'd', 'abc', 'def']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "complexstring",words = ['com', 'plex', 'string', 'other']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "complexstring",words = ['com', 'plex', 'string', 'other']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",words = ['abcd', 'ef', 'gh', 'ijk']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",words = ['abcd', 'ef', 'gh', 'ijk']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "uniqueprefix",words = ['unique', 'prefix', 'not']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uniqueprefix",words = ['unique', 'prefix', 'not']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "prefix",words = ['pre', 'fix', 'e', 'f', 'g']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "prefix",words = ['pre', 'fix', 'e', 'f', 'g']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "oneonetwo",words = ['one', 'one', 'two', 'three']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "oneonetwo",words = ['one', 'one', 'two', 'three']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzy",words = ['xy', 'zz', 'y', 'z']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzy",words = ['xy', 'zz', 'y', 'z']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "partialmatch",words = ['partial', 'non', 'matching', 'words']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "partialmatch",words = ['partial', 'non', 'matching', 'words']) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "prefixmatching",words = ['pre', 'fix', 'mat', 'ching']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "prefixmatching",words = ['pre', 'fix', 'mat', 'ching']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "overlapexample",words = ['over', 'lap', 'ex', 'ample']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "overlapexample",words = ['over', 'lap', 'ex', 'ample']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "boundary",words = ['bound', 'ary', 'extra']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "boundary",words = ['bound', 'ary', 'extra']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "partialmatch",words = ['par', 'tial', 'match', 'nomatch']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "partialmatch",words = ['par', 'tial', 'match', 'nomatch']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcd",words = ['abcd', 'abcd', 'abcd']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcd",words = ['abcd', 'abcd', 'abcd']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "oneonetwo",words = ['one', 'one', 'two', 'three']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "oneonetwo",words = ['one', 'one', 'two', 'three']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",words = ['abc', 'def', 'ghi', 'j']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",words = ['abc', 'def', 'ghi', 'j']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",words = ['mis', 'si', 'ss', 'ippi']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",words = ['mis', 'si', 'ss', 'ippi']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "matchmaking",words = ['mat', 'ch', 'mak', 'ing']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "matchmaking",words = ['mat', 'ch', 'mak', 'ing']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",words = ['a', 'bc', 'de', 'fg', 'xyz']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",words = ['a', 'bc', 'de', 'fg', 'xyz']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "prefix",words = ['pre', 'fix', 'ed', 'abc']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "prefix",words = ['pre', 'fix', 'ed', 'abc']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "prefix",words = ['pre', 'fix', 'post']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "prefix",words = ['pre', 'fix', 'post']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr",words = ['mn', 'op', 'qr', 'st']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr",words = ['mn', 'op', 'qr', 'st']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "programminglanguage",words = ['pro', 'gram', 'ming', 'lan', 'guage']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programminglanguage",words = ['pro', 'gram', 'ming', 'lan', 'guage']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohello",words = ['hello', 'hello', 'world']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohello",words = ['hello', 'hello', 'world']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "prefixstring",words = ['pre', 'fix', 'str', 'ing']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "prefixstring",words = ['pre', 'fix', 'str', 'ing']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellothere",words = ['he', 'll', 'o', 'there']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellothere",words = ['he', 'll', 'o', 'there']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "concatenation",words = ['con', 'cat', 'en', 'ation']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "concatenation",words = ['con', 'cat', 'en', 'ation']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohello",words = ['hello', 'hello', 'hello']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohello",words = ['hello', 'hello', 'hello']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",words = ['h', 'e', 'l', 'l', 'o', 'world']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",words = ['h', 'e', 'l', 'l', 'o', 'world']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "quickbrownfox",words = ['quick', 'brown', 'fox', 'jump']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "quickbrownfox",words = ['quick', 'brown', 'fox', 'jump']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghi",words = ['abc', 'def', 'ghi', 'jkl']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghi",words = ['abc', 'def', 'ghi', 'jkl']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "one",words = ['on', 'e', 'extra']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "one",words = ['on', 'e', 'extra']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "notprefix",words = ['prefix', 'not']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "notprefix",words = ['prefix', 'not']) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",words = ['a', 'bc', 'def', 'gh']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",words = ['a', 'bc', 'def', 'gh']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "prefixstring",words = ['prefix', 'string', 'extra']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "prefixstring",words = ['prefix', 'string', 'extra']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "prefix",words = ['pre', 'fi', 'x']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "prefix",words = ['pre', 'fi', 'x']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "longword",words = ['lo', 'ng', 'wor', 'd']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longword",words = ['lo', 'ng', 'wor', 'd']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "xxyyyzzz",words = ['xx', 'yyy', 'zzz', 'a']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xxyyyzzz",words = ['xx', 'yyy', 'zzz', 'a']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "concatenation",words = ['con', 'cat', 'en', 'ation']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "concatenation",words = ['con', 'cat', 'en', 'ation']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "unique",words = ['un', 'iq', 'ue']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "unique",words = ['un', 'iq', 'ue']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "algorithm",words = ['algo', 'r', 'ith', 'm']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "algorithm",words = ['algo', 'r', 'ith', 'm']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "variouslengths",words = ['vari', 'ous', 'length', 's']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "variouslengths",words = ['vari', 'ous', 'length', 's']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "two",words = ['tw', 'o', 'tw', 'o']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "two",words = ['tw', 'o', 'tw', 'o']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcd",words = ['abc', 'd', 'abcd']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcd",words = ['abc', 'd', 'abcd']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "wordplay",words = ['word', 'play', 'game', 'time']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "wordplay",words = ['word', 'play', 'game', 'time']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",words = ['pro', 'gram', 'ming', 'lang']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",words = ['pro', 'gram', 'ming', 'lang']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "concatenation",words = ['con', 'cat', 'enation', 'ation']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "concatenation",words = ['con', 'cat', 'enation', 'ation']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "supercalifragilisticexpialidocious",words = ['super', 'cali', 'fragilistic', 'expiali', 'docious']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "supercalifragilisticexpialidocious",words = ['super', 'cali', 'fragilistic', 'expiali', 'docious']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",words = ['a', 'bc', 'de', 'fghi', 'j']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",words = ['a', 'bc', 'de', 'fghi', 'j']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "algorithm",words = ['algo', 'rith', 'm']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "algorithm",words = ['algo', 'rith', 'm']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "testcase",words = ['tes', 't', 'ca', 'se']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "testcase",words = ['tes', 't', 'ca', 'se']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "concatenation",words = ['con', 'cat', 'e', 'na', 'tion']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "concatenation",words = ['con', 'cat', 'e', 'na', 'tion']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",words = ['abc', 'def', 'ghi', 'j']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",words = ['abc', 'def', 'ghi', 'j']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",words = ['x', 'y', 'z', 'a', 'b', 'c']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",words = ['x', 'y', 'z', 'a', 'b', 'c']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "prefixtest",words = ['pre', 'fix', 'test', 'suffix']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "prefixtest",words = ['pre', 'fix', 'test', 'suffix']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "repeated",words = ['rep', 'e', 'ated']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeated",words = ['rep', 'e', 'ated']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "matchingprefix",words = ['matching', 'prefix', 'matching', 'prefix']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "matchingprefix",words = ['matching', 'prefix', 'matching', 'prefix']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdexyz",words = ['abc', 'de', 'xyz', 'mnop']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdexyz",words = ['abc', 'de', 'xyz', 'mnop']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccdd",words = ['aa', 'bb', 'cc', 'd', 'd']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccdd",words = ['aa', 'bb', 'cc', 'd', 'd']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",words = ['a', 'b', 'c', 'def']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",words = ['a', 'b', 'c', 'def']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "programmingisfun",words = ['pro', 'gram', 'ming', 'is', 'fun']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programmingisfun",words = ['pro', 'gram', 'ming', 'is', 'fun']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "short",words = ['shor', 't']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "short",words = ['shor', 't']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",words = ['mis', 'si', 's', 'ip', 'pi']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",words = ['mis', 'si', 's', 'ip', 'pi']) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "repeatedword",words = ['repeated', 'word', 'repeated']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeatedword",words = ['repeated', 'word', 'repeated']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "rapiddevelopment",words = ['rap', 'id', 'devel', 'op', 'ment']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rapiddevelopment",words = ['rap', 'id', 'devel', 'op', 'ment']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "onetwothree",words = ['one', 'two', 'three', 'four']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "onetwothree",words = ['one', 'two', 'three', 'four']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "interviewquestion",words = ['inter', 'view', 'quest', 'ion']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "interviewquestion",words = ['inter', 'view', 'quest', 'ion']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcd",words = ['abcd', 'abcd']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcd",words = ['abcd', 'abcd']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "longstring",words = ['long', 'string', 'extrastuff']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longstring",words = ['long', 'string', 'extrastuff']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",words = ['xy', 'z', 'a', 'b']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",words = ['xy', 'z', 'a', 'b']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisatest",words = ['this', 'is', 'a', 'test']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisatest",words = ['this', 'is', 'a', 'test']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",words = ['abc', 'def', 'g', 'h']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",words = ['abc', 'def', 'g', 'h']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellothere",words = ['he', 'll', 'ot', 'her', 'e']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellothere",words = ['he', 'll', 'ot', 'her', 'e']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "buildingblocks",words = ['building', 'block', 's']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "buildingblocks",words = ['building', 'block', 's']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",words = ['abc', 'de', 'f', 'gh', 'ij']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",words = ['abc', 'de', 'f', 'gh', 'ij']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "prefixmatch",words = ['prefix', 'ma', 'tch']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "prefixmatch",words = ['prefix', 'ma', 'tch']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "python",words = ['py', 'th', 'on', 'o']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "python",words = ['py', 'th', 'on', 'o']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "python",words = ['py', 't', 'h', 'o', 'n', 'extra']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "python",words = ['py', 't', 'h', 'o', 'n', 'extra']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",words = ['aa', 'bb', 'cc', 'dd']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",words = ['aa', 'bb', 'cc', 'dd']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacax",words = ['aba', 'c', 'ax', 'a']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacax",words = ['aba', 'c', 'ax', 'a']) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",words = ['aa', 'bb', 'cc', 'dd']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",words = ['aa', 'bb', 'cc', 'dd']) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "aaaa",words = ['aa', 'aa']) == True
    assert candidate(s = "hello",words = ['he', 'll', 'o']) == True
    assert candidate(s = "abc",words = ['a']) == False
    assert candidate(s = "abc",words = ['a', 'bc']) == True
    assert candidate(s = "a",words = ['a', 'b', 'c']) == True
    assert candidate(s = "abcd",words = ['a', 'bcd']) == True
    assert candidate(s = "cat",words = ['ca', 't']) == True
    assert candidate(s = "abcd",words = ['abc', 'd']) == True
    assert candidate(s = "hello",words = ['he', 'l', 'lo']) == True
    assert candidate(s = "abc",words = ['ab', 'c']) == True
    assert candidate(s = "",words = ['a', 'b', 'c']) == False
    assert candidate(s = "iloveleetcode",words = ['apples', 'i', 'love', 'leetcode']) == False
    assert candidate(s = "hello",words = ['he', 'llo']) == True
    assert candidate(s = "abcd",words = ['a', 'b', 'c', 'd']) == True
    assert candidate(s = "abcd",words = ['ab', 'cd']) == True
    assert candidate(s = "abcd",words = ['abcd']) == True
    assert candidate(s = "iloveleetcode",words = ['i', 'love', 'leetcode', 'apples']) == True
    assert candidate(s = "xyz",words = ['x', 'y', 'z']) == True
    assert candidate(s = "abc",words = ['a', 'b', 'c']) == True
    assert candidate(s = "abcd",words = ['abc']) == False
    assert candidate(s = "complexprefixstring",words = ['complex', 'prefix', 'string', 'extra']) == True
    assert candidate(s = "aquickbrownfox",words = ['a', 'quick', 'brown', 'fox', 'jumps']) == True
    assert candidate(s = "onetwothree",words = ['one', 'two', 'three', 'four', 'five']) == True
    assert candidate(s = "algorithm",words = ['algo', 'r', 'ith', 'm']) == True
    assert candidate(s = "python",words = ['py', 'th', 'on', 'n']) == True
    assert candidate(s = "complexprefix",words = ['com', 'ple', 'xpre', 'fix']) == True
    assert candidate(s = "concatenate",words = ['con', 'cat', 'en', 'ate']) == True
    assert candidate(s = "algorithms",words = ['algo', 'rithm', 's', 'data']) == True
    assert candidate(s = "abracadabra",words = ['abra', 'ca', 'da', 'bra', 'bra']) == True
    assert candidate(s = "substring",words = ['sub', 'str', 'ing', 'example']) == True
    assert candidate(s = "onetwothreefour",words = ['one', 'two', 'three', 'four', 'five']) == True
    assert candidate(s = "xyz",words = ['x', 'y', 'z', 'w']) == True
    assert candidate(s = "prefixstring",words = ['pre', 'fix', 'string']) == True
    assert candidate(s = "programming",words = ['pro', 'gram', 'ming']) == True
    assert candidate(s = "concatenate",words = ['con', 'cat', 'e', 'nate']) == True
    assert candidate(s = "thisisatest",words = ['this', 'is', 'a', 'test', 'case']) == True
    assert candidate(s = "substring",words = ['sub', 'string', 'abc']) == True
    assert candidate(s = "mississippi",words = ['mis', 'si', 'ssippi', 'p']) == True
    assert candidate(s = "prefixprefix",words = ['pre', 'fix', 'pre', 'fix', 'pre', 'fix']) == True
    assert candidate(s = "abcdef",words = ['a', 'b', 'c', 'def', 'ghi']) == True
    assert candidate(s = "thisisatest",words = ['this', 'is', 'a', 'test', 'case']) == True
    assert candidate(s = "abcdefg",words = ['a', 'b', 'c', 'd', 'e', 'f', 'g']) == True
    assert candidate(s = "aaabbbccc",words = ['aaa', 'bbb', 'ccc', 'ddd']) == True
    assert candidate(s = "hello",words = ['h', 'he', 'hel', 'hell', 'hello']) == False
    assert candidate(s = "abcdabc",words = ['ab', 'c', 'd', 'abc', 'def']) == True
    assert candidate(s = "complexstring",words = ['com', 'plex', 'string', 'other']) == True
    assert candidate(s = "abcdefghijk",words = ['abcd', 'ef', 'gh', 'ijk']) == True
    assert candidate(s = "uniqueprefix",words = ['unique', 'prefix', 'not']) == True
    assert candidate(s = "prefix",words = ['pre', 'fix', 'e', 'f', 'g']) == True
    assert candidate(s = "oneonetwo",words = ['one', 'one', 'two', 'three']) == True
    assert candidate(s = "xyzzy",words = ['xy', 'zz', 'y', 'z']) == True
    assert candidate(s = "partialmatch",words = ['partial', 'non', 'matching', 'words']) == False
    assert candidate(s = "prefixmatching",words = ['pre', 'fix', 'mat', 'ching']) == True
    assert candidate(s = "overlapexample",words = ['over', 'lap', 'ex', 'ample']) == True
    assert candidate(s = "boundary",words = ['bound', 'ary', 'extra']) == True
    assert candidate(s = "partialmatch",words = ['par', 'tial', 'match', 'nomatch']) == True
    assert candidate(s = "abcdabcd",words = ['abcd', 'abcd', 'abcd']) == True
    assert candidate(s = "oneonetwo",words = ['one', 'one', 'two', 'three']) == True
    assert candidate(s = "abcdefghij",words = ['abc', 'def', 'ghi', 'j']) == True
    assert candidate(s = "mississippi",words = ['mis', 'si', 'ss', 'ippi']) == True
    assert candidate(s = "matchmaking",words = ['mat', 'ch', 'mak', 'ing']) == True
    assert candidate(s = "abcdefg",words = ['a', 'bc', 'de', 'fg', 'xyz']) == True
    assert candidate(s = "prefix",words = ['pre', 'fix', 'ed', 'abc']) == True
    assert candidate(s = "prefix",words = ['pre', 'fix', 'post']) == True
    assert candidate(s = "mnopqr",words = ['mn', 'op', 'qr', 'st']) == True
    assert candidate(s = "programminglanguage",words = ['pro', 'gram', 'ming', 'lan', 'guage']) == True
    assert candidate(s = "hellohello",words = ['hello', 'hello', 'world']) == True
    assert candidate(s = "prefixstring",words = ['pre', 'fix', 'str', 'ing']) == True
    assert candidate(s = "hellothere",words = ['he', 'll', 'o', 'there']) == True
    assert candidate(s = "concatenation",words = ['con', 'cat', 'en', 'ation']) == True
    assert candidate(s = "hellohello",words = ['hello', 'hello', 'hello']) == True
    assert candidate(s = "hello",words = ['h', 'e', 'l', 'l', 'o', 'world']) == True
    assert candidate(s = "quickbrownfox",words = ['quick', 'brown', 'fox', 'jump']) == True
    assert candidate(s = "abcdefghi",words = ['abc', 'def', 'ghi', 'jkl']) == True
    assert candidate(s = "one",words = ['on', 'e', 'extra']) == True
    assert candidate(s = "notprefix",words = ['prefix', 'not']) == False
    assert candidate(s = "abcdefgh",words = ['a', 'bc', 'def', 'gh']) == True
    assert candidate(s = "prefixstring",words = ['prefix', 'string', 'extra']) == True
    assert candidate(s = "prefix",words = ['pre', 'fi', 'x']) == True
    assert candidate(s = "longword",words = ['lo', 'ng', 'wor', 'd']) == True
    assert candidate(s = "xxyyyzzz",words = ['xx', 'yyy', 'zzz', 'a']) == True
    assert candidate(s = "concatenation",words = ['con', 'cat', 'en', 'ation']) == True
    assert candidate(s = "unique",words = ['un', 'iq', 'ue']) == True
    assert candidate(s = "abcdefghij",words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == True
    assert candidate(s = "algorithm",words = ['algo', 'r', 'ith', 'm']) == True
    assert candidate(s = "variouslengths",words = ['vari', 'ous', 'length', 's']) == True
    assert candidate(s = "two",words = ['tw', 'o', 'tw', 'o']) == True
    assert candidate(s = "abcdabcd",words = ['abc', 'd', 'abcd']) == True
    assert candidate(s = "wordplay",words = ['word', 'play', 'game', 'time']) == True
    assert candidate(s = "programming",words = ['pro', 'gram', 'ming', 'lang']) == True
    assert candidate(s = "concatenation",words = ['con', 'cat', 'enation', 'ation']) == True
    assert candidate(s = "supercalifragilisticexpialidocious",words = ['super', 'cali', 'fragilistic', 'expiali', 'docious']) == True
    assert candidate(s = "abcdefghij",words = ['a', 'bc', 'de', 'fghi', 'j']) == True
    assert candidate(s = "algorithm",words = ['algo', 'rith', 'm']) == True
    assert candidate(s = "testcase",words = ['tes', 't', 'ca', 'se']) == True
    assert candidate(s = "concatenation",words = ['con', 'cat', 'e', 'na', 'tion']) == True
    assert candidate(s = "abcdefghij",words = ['abc', 'def', 'ghi', 'j']) == True
    assert candidate(s = "xyz",words = ['x', 'y', 'z', 'a', 'b', 'c']) == True
    assert candidate(s = "prefixtest",words = ['pre', 'fix', 'test', 'suffix']) == True
    assert candidate(s = "repeated",words = ['rep', 'e', 'ated']) == True
    assert candidate(s = "matchingprefix",words = ['matching', 'prefix', 'matching', 'prefix']) == True
    assert candidate(s = "abcdexyz",words = ['abc', 'de', 'xyz', 'mnop']) == True
    assert candidate(s = "aabbccdd",words = ['aa', 'bb', 'cc', 'd', 'd']) == True
    assert candidate(s = "abcdef",words = ['a', 'b', 'c', 'def']) == True
    assert candidate(s = "programmingisfun",words = ['pro', 'gram', 'ming', 'is', 'fun']) == True
    assert candidate(s = "short",words = ['shor', 't']) == True
    assert candidate(s = "mississippi",words = ['mis', 'si', 's', 'ip', 'pi']) == False
    assert candidate(s = "repeatedword",words = ['repeated', 'word', 'repeated']) == True
    assert candidate(s = "rapiddevelopment",words = ['rap', 'id', 'devel', 'op', 'ment']) == True
    assert candidate(s = "onetwothree",words = ['one', 'two', 'three', 'four']) == True
    assert candidate(s = "interviewquestion",words = ['inter', 'view', 'quest', 'ion']) == True
    assert candidate(s = "abcdabcd",words = ['abcd', 'abcd']) == True
    assert candidate(s = "longstring",words = ['long', 'string', 'extrastuff']) == True
    assert candidate(s = "xyz",words = ['xy', 'z', 'a', 'b']) == True
    assert candidate(s = "thisisatest",words = ['this', 'is', 'a', 'test']) == True
    assert candidate(s = "abcdefg",words = ['abc', 'def', 'g', 'h']) == True
    assert candidate(s = "hellothere",words = ['he', 'll', 'ot', 'her', 'e']) == True
    assert candidate(s = "buildingblocks",words = ['building', 'block', 's']) == True
    assert candidate(s = "abcdefghij",words = ['abc', 'de', 'f', 'gh', 'ij']) == True
    assert candidate(s = "prefixmatch",words = ['prefix', 'ma', 'tch']) == True
    assert candidate(s = "python",words = ['py', 'th', 'on', 'o']) == True
    assert candidate(s = "python",words = ['py', 't', 'h', 'o', 'n', 'extra']) == True
    assert candidate(s = "aabbcc",words = ['aa', 'bb', 'cc', 'dd']) == True
    assert candidate(s = "abacax",words = ['aba', 'c', 'ax', 'a']) == True
    assert candidate(s = "aabbcc",words = ['aa', 'bb', 'cc', 'dd']) == True


