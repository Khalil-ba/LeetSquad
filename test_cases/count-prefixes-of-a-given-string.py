def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hell', 'he', 'h'],s = "hello") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hell', 'he', 'h'],s = "hello") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['short'],s = "shorter") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['short'],s = "shorter") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'same'],s = "same") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'same'],s = "same") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello'],s = "h") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello'],s = "h") == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello'],s = "hello") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello'],s = "hello") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['d', 'do', 'dog', 'doge'],s = "doge") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['d', 'do', 'dog', 'doge'],s = "doge") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix'],s = "prefix") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix'],s = "prefix") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'same', 'same'],s = "same") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'same', 'same'],s = "same") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['world'],s = "world") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['world'],s = "world") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c'],s = "abcde") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c'],s = "abcde") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a'],s = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a'],s = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['not', 'a', 'prefix'],s = "example") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['not', 'a', 'prefix'],s = "example") == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'testing', 't'],s = "testing") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'testing', 't'],s = "testing") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xy', 'x'],s = "xyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xy', 'x'],s = "xyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd'],s = "abc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd'],s = "abc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c'],s = "d") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c'],s = "d") == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'testing', 'tested'],s = "testing") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'testing', 'tested'],s = "testing") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'a'],s = "aa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'a'],s = "aa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc'],s = "abc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc'],s = "abc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abcd', 'abcde'],s = "abcdef") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abcd', 'abcde'],s = "abcdef") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['z', 'zz', 'zzz'],s = "zzzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['z', 'zz', 'zzz'],s = "zzzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'bat', 'rat'],s = "car") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'bat', 'rat'],s = "car") == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'ab', 'bc', 'abc'],s = "abc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'ab', 'bc', 'abc'],s = "abc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['h'],s = "hello") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['h'],s = "hello") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a'],s = "b") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a'],s = "b") == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['yes', 'no'],s = "yesman") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['yes', 'no'],s = "yesman") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix'],s = "prefixing") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix'],s = "prefixing") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'he', 'h'],s = "hello") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'he', 'h'],s = "hello") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test'],s = "testing") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test'],s = "testing") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'ab', 'abc', 'abcd'],s = "abcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'ab', 'abc', 'abcd'],s = "abcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['subsequence', 'subsequen', 'subsequen', 'subsequ', 'subsequ', 'subseq'],s = "subsequence") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['subsequence', 'subsequen', 'subsequen', 'subsequ', 'subsequ', 'subseq'],s = "subsequence") == 6: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'abc', 'abcd'],s = "abcd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'abc', 'abcd'],s = "abcd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'testing', 'tested', 'te'],s = "testing") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'testing', 'tested', 'te'],s = "testing") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['unique', 'uniq', 'un'],s = "unique") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['unique', 'uniq', 'un'],s = "unique") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['different', 'dif', 'diff', 'differ'],s = "different") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['different', 'dif', 'diff', 'differ'],s = "different") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['partial', 'parti', 'part', 'par'],s = "partialmatch") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['partial', 'parti', 'part', 'par'],s = "partialmatch") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'pre', 'pred'],s = "predicate") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'pre', 'pred'],s = "predicate") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['example', 'examp', 'exam', 'exa', 'ex', 'e'],s = "example") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['example', 'examp', 'exam', 'exa', 'ex', 'e'],s = "example") == 6: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'prefi', 'pref', 'pre'],s = "prefix") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'prefi', 'pref', 'pre'],s = "prefix") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abcd', 'ab', 'a'],s = "abcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abcd', 'ab', 'a'],s = "abcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['complex', 'com', 'comp', 'comple', 'complexe'],s = "complex") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['complex', 'com', 'comp', 'comple', 'complexe'],s = "complex") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'prefi', 'prefixe', 'prefixex'],s = "prefixextension") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'prefi', 'prefixe', 'prefixex'],s = "prefixextension") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa', 'aaaa'],s = "aaaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa', 'aaaa'],s = "aaaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['example', 'ex', 'exa', 'exam', 'examp', 'examp'],s = "example") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['example', 'ex', 'exa', 'exam', 'examp', 'examp'],s = "example") == 6: {e}')
    
    total += 1
    try:
        result = candidate(words = ['complex', 'comple', 'compl', 'comp'],s = "complexity") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['complex', 'comple', 'compl', 'comp'],s = "complexity") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hell', 'he'],s = "hello") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hell', 'he'],s = "hello") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'bcde', 'cde', 'de', 'e'],s = "abcde") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'bcde', 'cde', 'de', 'e'],s = "abcde") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'def', 'ghi'],s = "abcdefghi") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'def', 'ghi'],s = "abcdefghi") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['not', 'no', 'n'],s = "note") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['not', 'no', 'n'],s = "note") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['multiple', 'multip', 'multi', 'mult', 'mult'],s = "multiple") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['multiple', 'multip', 'multi', 'mult', 'mult'],s = "multiple") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'words', 'wording'],s = "word") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'words', 'wording'],s = "word") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'pre', 'p'],s = "prefix") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'pre', 'p'],s = "prefix") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['overlap', 'over', 'ov', 'o'],s = "overlap") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['overlap', 'over', 'ov', 'o'],s = "overlap") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],s = "aaaaaaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],s = "aaaaaaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],s = "aaaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],s = "aaaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['short', 'shorter', 'shortest'],s = "short") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['short', 'shorter', 'shortest'],s = "short") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg'],s = "abcdefgh") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg'],s = "abcdefgh") == 7: {e}')
    
    total += 1
    try:
        result = candidate(words = ['short', 'shot', 'sh', 's'],s = "shortstory") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['short', 'shot', 'sh', 's'],s = "shortstory") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abc', 'ab', 'a'],s = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abc', 'ab', 'a'],s = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['longword', 'long', 'lo', 'l', 'lon', 'longw'],s = "longword") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['longword', 'long', 'lo', 'l', 'lon', 'longw'],s = "longword") == 6: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e'],s = "abcde") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e'],s = "abcde") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'pre', 'p'],s = "prefix") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'pre', 'p'],s = "prefix") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'pre', 'pref', 'prefi', 'prefixe'],s = "prefix") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'pre', 'pref', 'prefi', 'prefixe'],s = "prefix") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aa', 'a'],s = "aaaaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aa', 'a'],s = "aaaaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'wording', 'worded', 'wordingword'],s = "wordingword") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'wording', 'worded', 'wordingword'],s = "wordingword") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'testing', 'testi', 'testin'],s = "testingstring") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'testing', 'testi', 'testin'],s = "testingstring") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'three', 'four'],s = "one") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'three', 'four'],s = "one") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['different', 'diff', 'diffe', 'differen', 'differen'],s = "different") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['different', 'diff', 'diffe', 'differen', 'differen'],s = "different") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['unique', 'uniq', 'un', 'u'],s = "unique") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['unique', 'uniq', 'un', 'u'],s = "unique") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aa', 'a', 'aaaa'],s = "aaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aa', 'a', 'aaaa'],s = "aaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'bcde', 'cdef', 'defg'],s = "abcd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'bcde', 'cdef', 'defg'],s = "abcd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['not', 'no', 'n'],s = "note") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['not', 'no', 'n'],s = "note") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'same', 'same', 'same'],s = "same") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'same', 'same', 'same'],s = "same") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'testing', 'tea', 'te'],s = "testing") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'testing', 'tea', 'te'],s = "testing") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['longword', 'long', 'lo', 'l'],s = "longwordexample") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['longword', 'long', 'lo', 'l'],s = "longwordexample") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['begin', 'beg', 'be', 'b'],s = "beginning") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['begin', 'beg', 'be', 'b'],s = "beginning") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['overlap', 'over', 'o'],s = "overlap") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['overlap', 'over', 'o'],s = "overlap") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'testing', 'tes', 't'],s = "testing") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'testing', 'tes', 't'],s = "testing") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xy', 'xyz', 'xyzz'],s = "xy") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xy', 'xyz', 'xyzz'],s = "xy") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'three', 'four', 'five'],s = "fives") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'three', 'four', 'five'],s = "fives") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['longword', 'long', 'lo', 'l'],s = "longword") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['longword', 'long', 'lo', 'l'],s = "longword") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['example', 'ex', 'exa', 'exam', 'examp'],s = "example") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['example', 'ex', 'exa', 'exam', 'examp'],s = "example") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'three'],s = "onetwothree") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'three'],s = "onetwothree") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abcd', 'abcde'],s = "abcdef") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abcd', 'abcde'],s = "abcdef") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['multiple', 'multi', 'mul', 'mu'],s = "multiples") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['multiple', 'multi', 'mul', 'mu'],s = "multiples") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'wor', 'wo', 'w'],s = "word") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'wor', 'wo', 'w'],s = "word") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'ban', 'ba', 'b'],s = "bananarama") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'ban', 'ba', 'b'],s = "bananarama") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abc', 'ab', 'a'],s = "abcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abc', 'ab', 'a'],s = "abcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa', 'aaaa'],s = "aaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa', 'aaaa'],s = "aaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'pre', 'prefixx', 'prefixxx', 'prefixxxx'],s = "prefixx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'pre', 'prefixx', 'prefixxx', 'prefixxxx'],s = "prefixx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['quick', 'qui', 'quic', 'quicks', 'quickb'],s = "quickbrownfox") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['quick', 'qui', 'quic', 'quicks', 'quickb'],s = "quickbrownfox") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'testing', 'tested'],s = "testing") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'testing', 'tested'],s = "testing") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'onetwo', 'onetwothree'],s = "onetwothree") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'onetwo', 'onetwothree'],s = "onetwothree") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'prog', 'pro'],s = "programming") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'prog', 'pro'],s = "programming") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['part', 'partial', 'partially'],s = "partially") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['part', 'partial', 'partially'],s = "partially") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aa', 'a', 'aaaa'],s = "aaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aa', 'a', 'aaaa'],s = "aaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'three', 'four'],s = "one") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'three', 'four'],s = "one") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'pre', 'prex', 'abc'],s = "prefix") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'pre', 'prex', 'abc'],s = "prefix") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abcd', 'abcde'],s = "abcdefg") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abcd', 'abcde'],s = "abcdefg") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['repeat', 'repe', 'rep', 're', 'r'],s = "repeat") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repeat', 'repe', 'rep', 're', 'r'],s = "repeat") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde'],s = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde'],s = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],s = "aaaaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],s = "aaaaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['complex', 'comp', 'com', 'co', 'c'],s = "complexity") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['complex', 'comp', 'com', 'co', 'c'],s = "complexity") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['python', 'pyth', 'py'],s = "python") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['python', 'pyth', 'py'],s = "python") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xy', 'x'],s = "xy") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xy', 'x'],s = "xy") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xy', 'x', ''],s = "xyz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xy', 'x', ''],s = "xyz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['complex', 'com', 'co', 'c'],s = "complex") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['complex', 'com', 'co', 'c'],s = "complex") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'prefixx', 'prefixxx', 'prefixxxx'],s = "prefix") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'prefixx', 'prefixxx', 'prefixxxx'],s = "prefix") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abcd', 'abcde'],s = "abcdefg") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abcd', 'abcde'],s = "abcdefg") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'def', 'ghi', 'abc'],s = "abcdefghi") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'def', 'ghi', 'abc'],s = "abcdefghi") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'cattle', 'cattleman'],s = "cattleman") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'cattle', 'cattleman'],s = "cattleman") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'xy', 'x'],s = "xyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'xy', 'x'],s = "xyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'same', 'same'],s = "same") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'same', 'same'],s = "same") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'pre', 'pref'],s = "prefix") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'pre', 'pref'],s = "prefix") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef'],s = "fghijkl") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef'],s = "fghijkl") == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['small', 'smaller', 'smallest', 'smallerest'],s = "smallerest") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['small', 'smaller', 'smallest', 'smallerest'],s = "smallerest") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['substring', 'subs', 'sub', 'su'],s = "substringexample") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['substring', 'subs', 'sub', 'su'],s = "substringexample") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abcd', 'abcde', 'abcdef'],s = "abcdefg") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abcd', 'abcde', 'abcdef'],s = "abcdefg") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'testing', 'testi'],s = "test") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'testing', 'testi'],s = "test") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zz', 'zzz', 'zzzz'],s = "zzzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zz', 'zzz', 'zzzz'],s = "zzzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'he', 'hell'],s = "hello") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'he', 'hell'],s = "hello") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'pre', 'pref', 'prex'],s = "prefix") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'pre', 'pref', 'prex'],s = "prefix") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['z', 'zz', 'zzz', 'zzzz'],s = "zzzzzz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['z', 'zz', 'zzz', 'zzzz'],s = "zzzzzz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['unique', 'uniq', 'uni', 'un', 'u'],s = "unique") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['unique', 'uniq', 'uni', 'un', 'u'],s = "unique") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'dog', 'car', 'catch', 'cart'],s = "catch") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'dog', 'car', 'catch', 'cart'],s = "catch") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['consistent', 'consist', 'consi', 'cons'],s = "consistency") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['consistent', 'consist', 'consi', 'cons'],s = "consistency") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],s = "abcdefghij") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],s = "abcdefghij") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['unique', 'uniq', 'uni', 'un'],s = "uniques") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['unique', 'uniq', 'uni', 'un'],s = "uniques") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world', 'hel', 'wo', 'wor'],s = "helloworld") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world', 'hel', 'wo', 'wor'],s = "helloworld") == 2: {e}')
    
    total += 1
    try:
        result = candidate(words = ['overlap', 'over', 'ov', 'overlaplap'],s = "overlap") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['overlap', 'over', 'ov', 'overlaplap'],s = "overlap") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['matching', 'match', 'mat', 'ma', 'm'],s = "matching") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['matching', 'match', 'mat', 'ma', 'm'],s = "matching") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hell', 'he', 'h', 'hellohello'],s = "hellohello") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hell', 'he', 'h', 'hellohello'],s = "hellohello") == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa', 'aaaa'],s = "aaaaaaaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa', 'aaaa'],s = "aaaaaaaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'testing', 'testing123'],s = "test") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'testing', 'testing123'],s = "test") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['match', 'mat', 'ma', 'm'],s = "match") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['match', 'mat', 'ma', 'm'],s = "match") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['example', 'exa', 'ex', 'e'],s = "example") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['example', 'exa', 'ex', 'e'],s = "example") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hell', 'he', 'h'],s = "hello") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hell', 'he', 'h'],s = "hello") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'wording', 'wordings'],s = "word") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'wording', 'wordings'],s = "word") == 1: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'pre', 'p', 'programming'],s = "prefix") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'pre', 'p', 'programming'],s = "prefix") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'ab', 'abc', 'abcd'],s = "abcde") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'ab', 'abc', 'abcd'],s = "abcde") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['unique', 'uniqueness', 'uni', 'un'],s = "uniqueness") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['unique', 'uniqueness', 'uni', 'un'],s = "uniqueness") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'on', 'o', 'ones'],s = "one") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'on', 'o', 'ones'],s = "one") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'wo', 'w'],s = "word") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'wo', 'w'],s = "word") == 3: {e}')
    
    total += 1
    try:
        result = candidate(words = ['prefix', 'pre', 'pr', 'p'],s = "prefix") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['prefix', 'pre', 'pr', 'p'],s = "prefix") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['example', 'exam', 'ex', 'e'],s = "examples") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['example', 'exam', 'ex', 'e'],s = "examples") == 4: {e}')
    
    total += 1
    try:
        result = candidate(words = ['common', 'commo', 'comm', 'com', 'co', 'c'],s = "common") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['common', 'commo', 'comm', 'com', 'co', 'c'],s = "common") == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(words = ['hello', 'hell', 'he', 'h'],s = "hello") == 4
    assert candidate(words = ['short'],s = "shorter") == 1
    assert candidate(words = ['same', 'same'],s = "same") == 2
    assert candidate(words = ['hello'],s = "h") == 0
    assert candidate(words = ['hello'],s = "hello") == 1
    assert candidate(words = ['d', 'do', 'dog', 'doge'],s = "doge") == 4
    assert candidate(words = ['prefix'],s = "prefix") == 1
    assert candidate(words = ['same', 'same', 'same'],s = "same") == 3
    assert candidate(words = ['world'],s = "world") == 1
    assert candidate(words = ['a', 'b', 'c'],s = "abcde") == 1
    assert candidate(words = ['a'],s = "a") == 1
    assert candidate(words = ['not', 'a', 'prefix'],s = "example") == 0
    assert candidate(words = ['test', 'testing', 't'],s = "testing") == 3
    assert candidate(words = ['xyz', 'xy', 'x'],s = "xyz") == 3
    assert candidate(words = ['abcd'],s = "abc") == 0
    assert candidate(words = ['a', 'b', 'c'],s = "d") == 0
    assert candidate(words = ['test', 'testing', 'tested'],s = "testing") == 2
    assert candidate(words = ['a', 'a'],s = "aa") == 2
    assert candidate(words = ['abc'],s = "abc") == 1
    assert candidate(words = ['abc', 'abcd', 'abcde'],s = "abcdef") == 3
    assert candidate(words = ['z', 'zz', 'zzz'],s = "zzzz") == 3
    assert candidate(words = ['cat', 'bat', 'rat'],s = "car") == 0
    assert candidate(words = ['a', 'b', 'c', 'ab', 'bc', 'abc'],s = "abc") == 3
    assert candidate(words = ['h'],s = "hello") == 1
    assert candidate(words = ['a'],s = "b") == 0
    assert candidate(words = ['yes', 'no'],s = "yesman") == 1
    assert candidate(words = ['prefix'],s = "prefixing") == 1
    assert candidate(words = ['hello', 'he', 'h'],s = "hello") == 3
    assert candidate(words = ['test'],s = "testing") == 1
    assert candidate(words = ['a', 'ab', 'abc', 'abcd'],s = "abcd") == 4
    assert candidate(words = ['subsequence', 'subsequen', 'subsequen', 'subsequ', 'subsequ', 'subseq'],s = "subsequence") == 6
    assert candidate(words = ['ab', 'abc', 'abcd'],s = "abcd") == 3
    assert candidate(words = ['test', 'testing', 'tested', 'te'],s = "testing") == 3
    assert candidate(words = ['unique', 'uniq', 'un'],s = "unique") == 3
    assert candidate(words = ['different', 'dif', 'diff', 'differ'],s = "different") == 4
    assert candidate(words = ['partial', 'parti', 'part', 'par'],s = "partialmatch") == 4
    assert candidate(words = ['prefix', 'pre', 'pred'],s = "predicate") == 2
    assert candidate(words = ['example', 'examp', 'exam', 'exa', 'ex', 'e'],s = "example") == 6
    assert candidate(words = ['prefix', 'prefi', 'pref', 'pre'],s = "prefix") == 4
    assert candidate(words = ['abc', 'abcd', 'ab', 'a'],s = "abcd") == 4
    assert candidate(words = ['complex', 'com', 'comp', 'comple', 'complexe'],s = "complex") == 4
    assert candidate(words = ['prefix', 'prefi', 'prefixe', 'prefixex'],s = "prefixextension") == 4
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa'],s = "aaaaa") == 4
    assert candidate(words = ['example', 'ex', 'exa', 'exam', 'examp', 'examp'],s = "example") == 6
    assert candidate(words = ['complex', 'comple', 'compl', 'comp'],s = "complexity") == 4
    assert candidate(words = ['hello', 'hell', 'he'],s = "hello") == 3
    assert candidate(words = ['abcde', 'bcde', 'cde', 'de', 'e'],s = "abcde") == 1
    assert candidate(words = ['abc', 'def', 'ghi'],s = "abcdefghi") == 1
    assert candidate(words = ['not', 'no', 'n'],s = "note") == 3
    assert candidate(words = ['multiple', 'multip', 'multi', 'mult', 'mult'],s = "multiple") == 5
    assert candidate(words = ['word', 'words', 'wording'],s = "word") == 1
    assert candidate(words = ['prefix', 'pre', 'p'],s = "prefix") == 3
    assert candidate(words = ['overlap', 'over', 'ov', 'o'],s = "overlap") == 4
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],s = "aaaaaaaa") == 5
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],s = "aaaaa") == 5
    assert candidate(words = ['short', 'shorter', 'shortest'],s = "short") == 1
    assert candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg'],s = "abcdefgh") == 7
    assert candidate(words = ['short', 'shot', 'sh', 's'],s = "shortstory") == 3
    assert candidate(words = ['abcd', 'abc', 'ab', 'a'],s = "a") == 1
    assert candidate(words = ['longword', 'long', 'lo', 'l', 'lon', 'longw'],s = "longword") == 6
    assert candidate(words = ['a', 'b', 'c', 'd', 'e'],s = "abcde") == 1
    assert candidate(words = ['prefix', 'pre', 'p'],s = "prefix") == 3
    assert candidate(words = ['prefix', 'pre', 'pref', 'prefi', 'prefixe'],s = "prefix") == 4
    assert candidate(words = ['aaa', 'aa', 'a'],s = "aaaaa") == 3
    assert candidate(words = ['word', 'wording', 'worded', 'wordingword'],s = "wordingword") == 3
    assert candidate(words = ['test', 'testing', 'testi', 'testin'],s = "testingstring") == 4
    assert candidate(words = ['one', 'two', 'three', 'four'],s = "one") == 1
    assert candidate(words = ['different', 'diff', 'diffe', 'differen', 'differen'],s = "different") == 5
    assert candidate(words = ['unique', 'uniq', 'un', 'u'],s = "unique") == 4
    assert candidate(words = ['aaa', 'aa', 'a', 'aaaa'],s = "aaa") == 3
    assert candidate(words = ['abcd', 'bcde', 'cdef', 'defg'],s = "abcd") == 1
    assert candidate(words = ['not', 'no', 'n'],s = "note") == 3
    assert candidate(words = ['same', 'same', 'same', 'same'],s = "same") == 4
    assert candidate(words = ['test', 'testing', 'tea', 'te'],s = "testing") == 3
    assert candidate(words = ['longword', 'long', 'lo', 'l'],s = "longwordexample") == 4
    assert candidate(words = ['begin', 'beg', 'be', 'b'],s = "beginning") == 4
    assert candidate(words = ['overlap', 'over', 'o'],s = "overlap") == 3
    assert candidate(words = ['test', 'testing', 'tes', 't'],s = "testing") == 4
    assert candidate(words = ['xy', 'xyz', 'xyzz'],s = "xy") == 1
    assert candidate(words = ['one', 'two', 'three', 'four', 'five'],s = "fives") == 1
    assert candidate(words = ['longword', 'long', 'lo', 'l'],s = "longword") == 4
    assert candidate(words = ['example', 'ex', 'exa', 'exam', 'examp'],s = "example") == 5
    assert candidate(words = ['one', 'two', 'three'],s = "onetwothree") == 1
    assert candidate(words = ['abc', 'abcd', 'abcde'],s = "abcdef") == 3
    assert candidate(words = ['multiple', 'multi', 'mul', 'mu'],s = "multiples") == 4
    assert candidate(words = ['word', 'wor', 'wo', 'w'],s = "word") == 4
    assert candidate(words = ['banana', 'ban', 'ba', 'b'],s = "bananarama") == 4
    assert candidate(words = ['abcd', 'abc', 'ab', 'a'],s = "abcd") == 4
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa'],s = "aaaa") == 4
    assert candidate(words = ['prefix', 'pre', 'prefixx', 'prefixxx', 'prefixxxx'],s = "prefixx") == 3
    assert candidate(words = ['quick', 'qui', 'quic', 'quicks', 'quickb'],s = "quickbrownfox") == 4
    assert candidate(words = ['test', 'testing', 'tested'],s = "testing") == 2
    assert candidate(words = ['one', 'onetwo', 'onetwothree'],s = "onetwothree") == 3
    assert candidate(words = ['programming', 'prog', 'pro'],s = "programming") == 3
    assert candidate(words = ['part', 'partial', 'partially'],s = "partially") == 3
    assert candidate(words = ['aaa', 'aa', 'a', 'aaaa'],s = "aaaa") == 4
    assert candidate(words = ['one', 'two', 'three', 'four'],s = "one") == 1
    assert candidate(words = ['prefix', 'pre', 'prex', 'abc'],s = "prefix") == 2
    assert candidate(words = ['abc', 'abcd', 'abcde'],s = "abcdefg") == 3
    assert candidate(words = ['repeat', 'repe', 'rep', 're', 'r'],s = "repeat") == 5
    assert candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde'],s = "a") == 1
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],s = "aaaaaa") == 5
    assert candidate(words = ['complex', 'comp', 'com', 'co', 'c'],s = "complexity") == 5
    assert candidate(words = ['python', 'pyth', 'py'],s = "python") == 3
    assert candidate(words = ['xyz', 'xy', 'x'],s = "xy") == 2
    assert candidate(words = ['xyz', 'xy', 'x', ''],s = "xyz") == 4
    assert candidate(words = ['complex', 'com', 'co', 'c'],s = "complex") == 4
    assert candidate(words = ['prefix', 'prefixx', 'prefixxx', 'prefixxxx'],s = "prefix") == 1
    assert candidate(words = ['abc', 'abcd', 'abcde'],s = "abcdefg") == 3
    assert candidate(words = ['abc', 'def', 'ghi', 'abc'],s = "abcdefghi") == 2
    assert candidate(words = ['cat', 'cattle', 'cattleman'],s = "cattleman") == 3
    assert candidate(words = ['xyz', 'xy', 'x'],s = "xyz") == 3
    assert candidate(words = ['same', 'same', 'same'],s = "same") == 3
    assert candidate(words = ['prefix', 'pre', 'pref'],s = "prefix") == 3
    assert candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef'],s = "fghijkl") == 0
    assert candidate(words = ['small', 'smaller', 'smallest', 'smallerest'],s = "smallerest") == 3
    assert candidate(words = ['substring', 'subs', 'sub', 'su'],s = "substringexample") == 4
    assert candidate(words = ['abc', 'abcd', 'abcde', 'abcdef'],s = "abcdefg") == 4
    assert candidate(words = ['test', 'testing', 'testi'],s = "test") == 1
    assert candidate(words = ['zz', 'zzz', 'zzzz'],s = "zzzz") == 3
    assert candidate(words = ['hello', 'he', 'hell'],s = "hello") == 3
    assert candidate(words = ['prefix', 'pre', 'pref', 'prex'],s = "prefix") == 3
    assert candidate(words = ['z', 'zz', 'zzz', 'zzzz'],s = "zzzzzz") == 4
    assert candidate(words = ['unique', 'uniq', 'uni', 'un', 'u'],s = "unique") == 5
    assert candidate(words = ['cat', 'dog', 'car', 'catch', 'cart'],s = "catch") == 2
    assert candidate(words = ['consistent', 'consist', 'consi', 'cons'],s = "consistency") == 3
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],s = "abcdefghij") == 1
    assert candidate(words = ['unique', 'uniq', 'uni', 'un'],s = "uniques") == 4
    assert candidate(words = ['hello', 'world', 'hel', 'wo', 'wor'],s = "helloworld") == 2
    assert candidate(words = ['overlap', 'over', 'ov', 'overlaplap'],s = "overlap") == 3
    assert candidate(words = ['matching', 'match', 'mat', 'ma', 'm'],s = "matching") == 5
    assert candidate(words = ['hello', 'hell', 'he', 'h', 'hellohello'],s = "hellohello") == 5
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa'],s = "aaaaaaaaa") == 4
    assert candidate(words = ['test', 'testing', 'testing123'],s = "test") == 1
    assert candidate(words = ['match', 'mat', 'ma', 'm'],s = "match") == 4
    assert candidate(words = ['example', 'exa', 'ex', 'e'],s = "example") == 4
    assert candidate(words = ['hello', 'hell', 'he', 'h'],s = "hello") == 4
    assert candidate(words = ['word', 'wording', 'wordings'],s = "word") == 1
    assert candidate(words = ['prefix', 'pre', 'p', 'programming'],s = "prefix") == 3
    assert candidate(words = ['a', 'ab', 'abc', 'abcd'],s = "abcde") == 4
    assert candidate(words = ['unique', 'uniqueness', 'uni', 'un'],s = "uniqueness") == 4
    assert candidate(words = ['one', 'on', 'o', 'ones'],s = "one") == 3
    assert candidate(words = ['word', 'wo', 'w'],s = "word") == 3
    assert candidate(words = ['prefix', 'pre', 'pr', 'p'],s = "prefix") == 4
    assert candidate(words = ['example', 'exam', 'ex', 'e'],s = "examples") == 4
    assert candidate(words = ['common', 'commo', 'comm', 'com', 'co', 'c'],s = "common") == 6


