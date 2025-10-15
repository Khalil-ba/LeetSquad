def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(patterns = ['a', 'b', 'c'],word = "aaaaabbbbb") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['a', 'b', 'c'],word = "aaaaabbbbb") == 2: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['aa', 'bb', 'cc'],word = "abcabc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['aa', 'bb', 'cc'],word = "abcabc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['a', 'abc', 'bc', 'd'],word = "abc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['a', 'abc', 'bc', 'd'],word = "abc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['aaa'],word = "aaaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['aaa'],word = "aaaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abc'],word = "abc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abc'],word = "abc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['xyz', 'xy', 'yz'],word = "xyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['xyz', 'xy', 'yz'],word = "xyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['hello', 'world'],word = "helloworld") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['hello', 'world'],word = "helloworld") == 2: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['a', 'a', 'a'],word = "ab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['a', 'a', 'a'],word = "ab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['z'],word = "abcz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['z'],word = "abcz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['a', 'b', 'c', 'd', 'e'],word = "edcba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['a', 'b', 'c', 'd', 'e'],word = "edcba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['hello', 'world', 'foo', 'bar'],word = "helloworldfoo") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['hello', 'world', 'foo', 'bar'],word = "helloworldfoo") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['repeated', 'repeat', 'eat'],word = "repeatedrepeat") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['repeated', 'repeat', 'eat'],word = "repeatedrepeat") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['this', 'is', 'a', 'test'],word = "thisisatest") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['this', 'is', 'a', 'test'],word = "thisisatest") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abc', 'cab', 'bac'],word = "abacabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abc', 'cab', 'bac'],word = "abacabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['aabb', 'bbcc', 'ccdd', 'ddaa'],word = "aabbccdd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['aabb', 'bbcc', 'ccdd', 'ddaa'],word = "aabbccdd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['a', 'ab', 'abc', 'abcd'],word = "abcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['a', 'ab', 'abc', 'abcd'],word = "abcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['a', 'aa', 'aaa', 'aaaa'],word = "aaaaaaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['a', 'aa', 'aaa', 'aaaa'],word = "aaaaaaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['overlapping', 'lapping', 'lappingo', 'verlapping'],word = "overlappinglappingoverlappingoverlapping") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['overlapping', 'lapping', 'lappingo', 'verlapping'],word = "overlappinglappingoverlappingoverlapping") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['hello', 'world', 'python', 'programming'],word = "helloworldpythonprogramming") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['hello', 'world', 'python', 'programming'],word = "helloworldpythonprogramming") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['xyz', 'zyx', 'zxy'],word = "xyzzyxzyxzxyzyx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['xyz', 'zyx', 'zxy'],word = "xyzzyxzyxzxyzyx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['xy', 'yx', 'xyz', 'zyx'],word = "xyzzyx") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['xy', 'yx', 'xyz', 'zyx'],word = "xyzzyx") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['lorem', 'ipsum', 'dolor', 'sit', 'amet'],word = "loremipsumdolorsitamet") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['lorem', 'ipsum', 'dolor', 'sit', 'amet'],word = "loremipsumdolorsitamet") == 5: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwx', 'vwxy', 'wxyz'],word = "abcdefghijklmnopqrstuvwxyz") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwx', 'vwxy', 'wxyz'],word = "abcdefghijklmnopqrstuvwxyz") == 23: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['mnop', 'nopq', 'opqr', 'pqrs', 'qrst'],word = "mnopqrstu") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['mnop', 'nopq', 'opqr', 'pqrs', 'qrst'],word = "mnopqrstu") == 5: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['quick', 'brown', 'fox'],word = "thequickbrownfox") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['quick', 'brown', 'fox'],word = "thequickbrownfox") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abcd', 'abcde', 'abcdef'],word = "abcdefgabcdefg") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abcd', 'abcde', 'abcdef'],word = "abcdefgabcdefg") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['xyz', 'zyx', 'yxz', 'xzy', 'zyx'],word = "zyxzyxzyxzyx") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['xyz', 'zyx', 'yxz', 'xzy', 'zyx'],word = "zyxzyxzyxzyx") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['ab', 'ba', 'aba', 'bab'],word = "abababab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['ab', 'ba', 'aba', 'bab'],word = "abababab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['aaaa', 'bbbb', 'cccc'],word = "aaaabbbbccccaaaabbbbcccc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['aaaa', 'bbbb', 'cccc'],word = "aaaabbbbccccaaaabbbbcccc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['aba', 'bba', 'aaa', 'bbb'],word = "abababababa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['aba', 'bba', 'aaa', 'bbb'],word = "abababababa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['repeated', 'pattern', 'substring', 'string'],word = "repeatedpatternsubstringstring") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['repeated', 'pattern', 'substring', 'string'],word = "repeatedpatternsubstringstring") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['ab', 'bc', 'cd', 'de', 'ef', 'fg'],word = "abcdefg") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['ab', 'bc', 'cd', 'de', 'ef', 'fg'],word = "abcdefg") == 6: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['repeated', 'substring', 'example'],word = "repeatedsubstringexample") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['repeated', 'substring', 'example'],word = "repeatedsubstringexample") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['overlap', 'lap', 'ap', 'p'],word = "overlaplapap") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['overlap', 'lap', 'ap', 'p'],word = "overlaplapap") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['hello', 'world', 'python', 'programming'],word = "programmingworldpython") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['hello', 'world', 'python', 'programming'],word = "programmingworldpython") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['longer', 'substrings', 'to', 'check'],word = "thisisalongersubstringtocheck") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['longer', 'substrings', 'to', 'check'],word = "thisisalongersubstringtocheck") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['unique', 'un', 'iq'],word = "uniqueiq") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['unique', 'un', 'iq'],word = "uniqueiq") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['substring', 'string', 'sub'],word = "thisisjustasubstringexample") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['substring', 'string', 'sub'],word = "thisisjustasubstringexample") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['hello', 'world', 'hello', 'world'],word = "helloworldhello") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['hello', 'world', 'hello', 'world'],word = "helloworldhello") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['aaa', 'aa', 'a'],word = "aaaaaaaaaaaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['aaa', 'aa', 'a'],word = "aaaaaaaaaaaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['z', 'zz', 'zzz'],word = "zzzzzzzzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['z', 'zz', 'zzz'],word = "zzzzzzzzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['ab', 'bc', 'cd', 'de', 'ef'],word = "abcdef") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['ab', 'bc', 'cd', 'de', 'ef'],word = "abcdef") == 5: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['123', '234', '345'],word = "1234567890") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['123', '234', '345'],word = "1234567890") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],word = "abcdefghij") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],word = "abcdefghij") == 10: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['a', 'b', 'c', 'd', 'e', 'f'],word = "abcdef") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['a', 'b', 'c', 'd', 'e', 'f'],word = "abcdef") == 6: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['a', 'ab', 'abc', 'abcd', 'abcde'],word = "abcde") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['a', 'ab', 'abc', 'abcd', 'abcde'],word = "abcde") == 5: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['one', 'two', 'three'],word = "onetwothreeonetwothree") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['one', 'two', 'three'],word = "onetwothreeonetwothree") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['aaa', 'aab', 'aba', 'baa', 'aabaa', 'aaaba', 'aaba', 'baaa'],word = "aaaabaaaa") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['aaa', 'aab', 'aba', 'baa', 'aabaa', 'aaaba', 'aaba', 'baaa'],word = "aaaabaaaa") == 8: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['hello', 'world', 'helloworld'],word = "helloworld") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['hello', 'world', 'helloworld'],word = "helloworld") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['quick', 'brown', 'fox'],word = "thequickbrownfoxjumps") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['quick', 'brown', 'fox'],word = "thequickbrownfoxjumps") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['xyz', 'zyx', 'yzz', 'zzz'],word = "xyzzyzyzzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['xyz', 'zyx', 'yzz', 'zzz'],word = "xyzzyzyzzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['aaa', 'bbb', 'ccc', 'abc', 'bca', 'cab'],word = "abcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['aaa', 'bbb', 'ccc', 'abc', 'bca', 'cab'],word = "abcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abcd', 'dcba', 'abcdabcd'],word = "abcdabcdabcdabcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abcd', 'dcba', 'abcdabcd'],word = "abcdabcdabcdabcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['a', 'ab', 'abc', 'abcd', 'abcde'],word = "abcdefghijklmnopqrstuvwxyz") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['a', 'ab', 'abc', 'abcd', 'abcde'],word = "abcdefghijklmnopqrstuvwxyz") == 5: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abc', 'def', 'ghi', 'jkl'],word = "abcdefghijkl") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abc', 'def', 'ghi', 'jkl'],word = "abcdefghijkl") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd'],word = "abcdeabcdeabcdeabcde") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd'],word = "abcdeabcdeabcdeabcde") == 0: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['ab', 'bc', 'cd', 'de'],word = "abcdefg") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['ab', 'bc', 'cd', 'de'],word = "abcdefg") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['pattern', 'matching', 'substrings'],word = "matchingpatternsubstring") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['pattern', 'matching', 'substrings'],word = "matchingpatternsubstring") == 2: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['ab', 'ba', 'abab', 'baba'],word = "abababababababab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['ab', 'ba', 'abab', 'baba'],word = "abababababababab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['same', 'sub', 'string', 'test', 'case'],word = "substringtestcase") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['same', 'sub', 'string', 'test', 'case'],word = "substringtestcase") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['aaaa', 'bbbb', 'cccc', 'ddd'],word = "aaaabbbbccccddd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['aaaa', 'bbbb', 'cccc', 'ddd'],word = "aaaabbbbccccddd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['apple', 'banana', 'cherry'],word = "cherrybananaapple") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['apple', 'banana', 'cherry'],word = "cherrybananaapple") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['cat', 'dog', 'bird', 'fish'],word = "fishdogcatbird") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['cat', 'dog', 'bird', 'fish'],word = "fishdogcatbird") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['python', 'java', 'cpp'],word = "pythonjavacpp") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['python', 'java', 'cpp'],word = "pythonjavacpp") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['aaa', 'bbb', 'ccc', 'ddd'],word = "aaabbbcccddd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['aaa', 'bbb', 'ccc', 'ddd'],word = "aaabbbcccddd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['test', 'sett', 'best'],word = "bestsett") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['test', 'sett', 'best'],word = "bestsett") == 2: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abc', 'bca', 'cab', 'abcabc'],word = "abcabcabcabc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abc', 'bca', 'cab', 'abcabc'],word = "abcabcabcabc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['aaa', 'aa', 'a'],word = "aaaaaaaaaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['aaa', 'aa', 'a'],word = "aaaaaaaaaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['quick', 'brown', 'fox', 'jump', 'over', 'lazy', 'dog'],word = "thequickbrownfoxjumpsoverthelazydog") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['quick', 'brown', 'fox', 'jump', 'over', 'lazy', 'dog'],word = "thequickbrownfoxjumpsoverthelazydog") == 7: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abc', 'cab', 'bca'],word = "abcabcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abc', 'cab', 'bca'],word = "abcabcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['xyz', 'zyx', 'xy', 'yx', 'xzy', 'yzx'],word = "zyxwvutsrqponmlkjihgfedcba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['xyz', 'zyx', 'xy', 'yx', 'xzy', 'yzx'],word = "zyxwvutsrqponmlkjihgfedcba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff'],word = "abcdefabcdefabcdef") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff'],word = "abcdefabcdefabcdef") == 0: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abc', 'def', 'ghi'],word = "defabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abc', 'def', 'ghi'],word = "defabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['quick', 'brown', 'fox'],word = "thequickbrownfoxjumpsoverthelazydog") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['quick', 'brown', 'fox'],word = "thequickbrownfoxjumpsoverthelazydog") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],word = "abcdef ghijklmnopqrstuvwxyz") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],word = "abcdef ghijklmnopqrstuvwxyz") == 9: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['aaa', 'aa', 'a'],word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['aaa', 'aa', 'a'],word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],word = "abcdefghijabcdefghij") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],word = "abcdefghijabcdefghij") == 10: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['test', 'string', 'finding', 'substring'],word = "teststringfindingsubstring") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['test', 'string', 'finding', 'substring'],word = "teststringfindingsubstring") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['aa', 'aaa', 'aaaa'],word = "aaaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['aa', 'aaa', 'aaaa'],word = "aaaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['short', 'shot', 'dot'],word = "shortshot") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['short', 'shot', 'dot'],word = "shortshot") == 2: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['foo', 'bar', 'foobar', 'barfoo'],word = "foobarbarfoobarfoo") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['foo', 'bar', 'foobar', 'barfoo'],word = "foobarbarfoobarfoo") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['aba', 'bab', 'aba'],word = "ababababa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['aba', 'bab', 'aba'],word = "ababababa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['hello', 'world', 'python'],word = "pythonworldhello") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['hello', 'world', 'python'],word = "pythonworldhello") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'],word = "abcacbcbacbacbcbac") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'],word = "abcacbcbacbacbcbac") == 5: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['banana', 'ana', 'nan', 'ban'],word = "banananana") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['banana', 'ana', 'nan', 'ban'],word = "banananana") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abc', 'abcd', 'abcde'],word = "abcdefgh") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abc', 'abcd', 'abcde'],word = "abcdefgh") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abcd', 'dcba', 'abcd'],word = "abcdcbaabcd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abcd', 'dcba', 'abcd'],word = "abcdcbaabcd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['aaaa', 'bbbb', 'cccc', 'dddd'],word = "abcdeabcdeabcde") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['aaaa', 'bbbb', 'cccc', 'dddd'],word = "abcdeabcdeabcde") == 0: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['longpattern', 'long', 'pattern'],word = "longpatternlongpattern") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['longpattern', 'long', 'pattern'],word = "longpatternlongpattern") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij'],word = "abcdefghij") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij'],word = "abcdefghij") == 9: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz'],word = "abcdefghijklmnopqrstuvwxyz") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz'],word = "abcdefghijklmnopqrstuvwxyz") == 24: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['zzz', 'zzzz', 'zzzzz'],word = "zzzzzzzzzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['zzz', 'zzzz', 'zzzzz'],word = "zzzzzzzzzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['ab', 'bc', 'cd', 'de'],word = "abcde") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['ab', 'bc', 'cd', 'de'],word = "abcde") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abc', 'bcd', 'cde', 'def'],word = "abcdefg") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abc', 'bcd', 'cde', 'def'],word = "abcdefg") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abc', 'abcd', 'abcde', 'abcdef'],word = "abcdefg") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abc', 'abcd', 'abcde', 'abcdef'],word = "abcdefg") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['test', 'tset', 'sett', 'settset'],word = "testsettsettset") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['test', 'tset', 'sett', 'settset'],word = "testsettsettset") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['small', 'medium', 'large', 'extra', 'huge'],word = "smallmediumlargeextrahuge") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['small', 'medium', 'large', 'extra', 'huge'],word = "smallmediumlargeextrahuge") == 5: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['pattern', 'tern', 'ternary', 'ternarysearch'],word = "binarysearchternarysearch") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['pattern', 'tern', 'ternary', 'ternarysearch'],word = "binarysearchternarysearch") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['xyz', 'zyx', 'yzx'],word = "xyzzyxzyxzyx") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['xyz', 'zyx', 'yzx'],word = "xyzzyxzyxzyx") == 2: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abcd', 'efgh', 'ijkl'],word = "efghijklabcd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abcd', 'efgh', 'ijkl'],word = "efghijklabcd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abc', 'cab', 'bac', 'bca', 'acb', 'cba'],word = "abcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abc', 'cab', 'bac', 'bca', 'acb', 'cba'],word = "abcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abc', 'abcabc', 'abcabcabc'],word = "abcabcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abc', 'abcabc', 'abcabcabc'],word = "abcabcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['aaa', 'bbb', 'ccc'],word = "abacabadabc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['aaa', 'bbb', 'ccc'],word = "abacabadabc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['one', 'two', 'three', 'onetwothree'],word = "onetwothreeonetwothree") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['one', 'two', 'three', 'onetwothree'],word = "onetwothreeonetwothree") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['search', 'sear', 'arch'],word = "searchingthesearchinthesearch") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['search', 'sear', 'arch'],word = "searchingthesearchinthesearch") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['overlap', 'lap', 'lapping'],word = "lapping") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['overlap', 'lap', 'lapping'],word = "lapping") == 2: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abc', 'def', 'ghi', 'jkl'],word = "abcdefghijklmnopqrstuvwxyz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abc', 'def', 'ghi', 'jkl'],word = "abcdefghijklmnopqrstuvwxyz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abc', 'def', 'ghi', 'jkl'],word = "abcdefghijk") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abc', 'def', 'ghi', 'jkl'],word = "abcdefghijk") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['xyz', 'zyx', 'wxy', 'uvw'],word = "xyzzyxwxyuvw") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['xyz', 'zyx', 'wxy', 'uvw'],word = "xyzzyxwxyuvw") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abc', 'def', 'ghi', 'jkl'],word = "abcdefghij") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abc', 'def', 'ghi', 'jkl'],word = "abcdefghij") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yz'],word = "abcdefghijklmnopqrstuvwxyz") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yz'],word = "abcdefghijklmnopqrstuvwxyz") == 7: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],word = "abcdefghijklmnopqrstuvwxyz") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],word = "abcdefghijklmnopqrstuvwxyz") == 9: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['zz', 'zzz', 'zzzz'],word = "zzzzzzzzzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['zz', 'zzz', 'zzzz'],word = "zzzzzzzzzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],word = "zyxwvutsrqponmlkjihgfedcba") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],word = "zyxwvutsrqponmlkjihgfedcba") == 26: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['example', 'ample', 'mple', 'ple', 'le', 'e'],word = "exampleexampleexample") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['example', 'ample', 'mple', 'ple', 'le', 'e'],word = "exampleexampleexample") == 6: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['ab', 'ba', 'ac', 'ca', 'bc', 'cb'],word = "abcbaacbba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['ab', 'ba', 'ac', 'ca', 'bc', 'cb'],word = "abcbaacbba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['abc', 'def', 'ghi'],word = "abcdefghi") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['abc', 'def', 'ghi'],word = "abcdefghi") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['xyz', 'zyx', 'yzx'],word = "xyzzyxzyx") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['xyz', 'zyx', 'yzx'],word = "xyzzyxzyx") == 2: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['zzz', 'zz', 'z'],word = "zzzzzzzzzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['zzz', 'zz', 'z'],word = "zzzzzzzzzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['pattern', 'tern', 'ternary', 'ary'],word = "patternarypatternary") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['pattern', 'tern', 'ternary', 'ary'],word = "patternarypatternary") == 4: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['xyz', 'abc', 'def', 'ghi', 'jkl'],word = "zyxwvutsrqponmlkjihgfedcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['xyz', 'abc', 'def', 'ghi', 'jkl'],word = "zyxwvutsrqponmlkjihgfedcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(patterns = ['a', 'ab', 'abc', 'abcd'],word = "abcdabcdabcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(patterns = ['a', 'ab', 'abc', 'abcd'],word = "abcdabcdabcd") == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(patterns = ['a', 'b', 'c'],word = "aaaaabbbbb") == 2
    assert candidate(patterns = ['aa', 'bb', 'cc'],word = "abcabc") == 0
    assert candidate(patterns = ['a', 'abc', 'bc', 'd'],word = "abc") == 3
    assert candidate(patterns = ['aaa'],word = "aaaaa") == 1
    assert candidate(patterns = ['abc'],word = "abc") == 1
    assert candidate(patterns = ['xyz', 'xy', 'yz'],word = "xyz") == 3
    assert candidate(patterns = ['hello', 'world'],word = "helloworld") == 2
    assert candidate(patterns = ['a', 'a', 'a'],word = "ab") == 3
    assert candidate(patterns = ['z'],word = "abcz") == 1
    assert candidate(patterns = ['a', 'b', 'c', 'd', 'e'],word = "edcba") == 5
    assert candidate(patterns = ['hello', 'world', 'foo', 'bar'],word = "helloworldfoo") == 3
    assert candidate(patterns = ['repeated', 'repeat', 'eat'],word = "repeatedrepeat") == 3
    assert candidate(patterns = ['this', 'is', 'a', 'test'],word = "thisisatest") == 4
    assert candidate(patterns = ['abc', 'cab', 'bac'],word = "abacabcabc") == 3
    assert candidate(patterns = ['aabb', 'bbcc', 'ccdd', 'ddaa'],word = "aabbccdd") == 3
    assert candidate(patterns = ['a', 'ab', 'abc', 'abcd'],word = "abcd") == 4
    assert candidate(patterns = ['a', 'aa', 'aaa', 'aaaa'],word = "aaaaaaaa") == 4
    assert candidate(patterns = ['overlapping', 'lapping', 'lappingo', 'verlapping'],word = "overlappinglappingoverlappingoverlapping") == 4
    assert candidate(patterns = ['hello', 'world', 'python', 'programming'],word = "helloworldpythonprogramming") == 4
    assert candidate(patterns = ['xyz', 'zyx', 'zxy'],word = "xyzzyxzyxzxyzyx") == 3
    assert candidate(patterns = ['xy', 'yx', 'xyz', 'zyx'],word = "xyzzyx") == 4
    assert candidate(patterns = ['lorem', 'ipsum', 'dolor', 'sit', 'amet'],word = "loremipsumdolorsitamet") == 5
    assert candidate(patterns = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwx', 'vwxy', 'wxyz'],word = "abcdefghijklmnopqrstuvwxyz") == 23
    assert candidate(patterns = ['mnop', 'nopq', 'opqr', 'pqrs', 'qrst'],word = "mnopqrstu") == 5
    assert candidate(patterns = ['quick', 'brown', 'fox'],word = "thequickbrownfox") == 3
    assert candidate(patterns = ['abcd', 'abcde', 'abcdef'],word = "abcdefgabcdefg") == 3
    assert candidate(patterns = ['xyz', 'zyx', 'yxz', 'xzy', 'zyx'],word = "zyxzyxzyxzyx") == 4
    assert candidate(patterns = ['ab', 'ba', 'aba', 'bab'],word = "abababab") == 4
    assert candidate(patterns = ['aaaa', 'bbbb', 'cccc'],word = "aaaabbbbccccaaaabbbbcccc") == 3
    assert candidate(patterns = ['aba', 'bba', 'aaa', 'bbb'],word = "abababababa") == 1
    assert candidate(patterns = ['repeated', 'pattern', 'substring', 'string'],word = "repeatedpatternsubstringstring") == 4
    assert candidate(patterns = ['ab', 'bc', 'cd', 'de', 'ef', 'fg'],word = "abcdefg") == 6
    assert candidate(patterns = ['repeated', 'substring', 'example'],word = "repeatedsubstringexample") == 3
    assert candidate(patterns = ['overlap', 'lap', 'ap', 'p'],word = "overlaplapap") == 4
    assert candidate(patterns = ['hello', 'world', 'python', 'programming'],word = "programmingworldpython") == 3
    assert candidate(patterns = ['longer', 'substrings', 'to', 'check'],word = "thisisalongersubstringtocheck") == 3
    assert candidate(patterns = ['unique', 'un', 'iq'],word = "uniqueiq") == 3
    assert candidate(patterns = ['substring', 'string', 'sub'],word = "thisisjustasubstringexample") == 3
    assert candidate(patterns = ['hello', 'world', 'hello', 'world'],word = "helloworldhello") == 4
    assert candidate(patterns = ['aaa', 'aa', 'a'],word = "aaaaaaaaaaaa") == 3
    assert candidate(patterns = ['z', 'zz', 'zzz'],word = "zzzzzzzzz") == 3
    assert candidate(patterns = ['ab', 'bc', 'cd', 'de', 'ef'],word = "abcdef") == 5
    assert candidate(patterns = ['123', '234', '345'],word = "1234567890") == 3
    assert candidate(patterns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],word = "abcdefghij") == 10
    assert candidate(patterns = ['a', 'b', 'c', 'd', 'e', 'f'],word = "abcdef") == 6
    assert candidate(patterns = ['a', 'ab', 'abc', 'abcd', 'abcde'],word = "abcde") == 5
    assert candidate(patterns = ['one', 'two', 'three'],word = "onetwothreeonetwothree") == 3
    assert candidate(patterns = ['aaa', 'aab', 'aba', 'baa', 'aabaa', 'aaaba', 'aaba', 'baaa'],word = "aaaabaaaa") == 8
    assert candidate(patterns = ['hello', 'world', 'helloworld'],word = "helloworld") == 3
    assert candidate(patterns = ['quick', 'brown', 'fox'],word = "thequickbrownfoxjumps") == 3
    assert candidate(patterns = ['xyz', 'zyx', 'yzz', 'zzz'],word = "xyzzyzyzzz") == 3
    assert candidate(patterns = ['aaa', 'bbb', 'ccc', 'abc', 'bca', 'cab'],word = "abcabcabc") == 3
    assert candidate(patterns = ['abcd', 'dcba', 'abcdabcd'],word = "abcdabcdabcdabcd") == 2
    assert candidate(patterns = ['a', 'ab', 'abc', 'abcd', 'abcde'],word = "abcdefghijklmnopqrstuvwxyz") == 5
    assert candidate(patterns = ['abc', 'def', 'ghi', 'jkl'],word = "abcdefghijkl") == 4
    assert candidate(patterns = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd'],word = "abcdeabcdeabcdeabcde") == 0
    assert candidate(patterns = ['ab', 'bc', 'cd', 'de'],word = "abcdefg") == 4
    assert candidate(patterns = ['pattern', 'matching', 'substrings'],word = "matchingpatternsubstring") == 2
    assert candidate(patterns = ['ab', 'ba', 'abab', 'baba'],word = "abababababababab") == 4
    assert candidate(patterns = ['same', 'sub', 'string', 'test', 'case'],word = "substringtestcase") == 4
    assert candidate(patterns = ['aaaa', 'bbbb', 'cccc', 'ddd'],word = "aaaabbbbccccddd") == 4
    assert candidate(patterns = ['apple', 'banana', 'cherry'],word = "cherrybananaapple") == 3
    assert candidate(patterns = ['cat', 'dog', 'bird', 'fish'],word = "fishdogcatbird") == 4
    assert candidate(patterns = ['python', 'java', 'cpp'],word = "pythonjavacpp") == 3
    assert candidate(patterns = ['aaa', 'bbb', 'ccc', 'ddd'],word = "aaabbbcccddd") == 4
    assert candidate(patterns = ['test', 'sett', 'best'],word = "bestsett") == 2
    assert candidate(patterns = ['abc', 'bca', 'cab', 'abcabc'],word = "abcabcabcabc") == 4
    assert candidate(patterns = ['aaa', 'aa', 'a'],word = "aaaaaaaaaa") == 3
    assert candidate(patterns = ['quick', 'brown', 'fox', 'jump', 'over', 'lazy', 'dog'],word = "thequickbrownfoxjumpsoverthelazydog") == 7
    assert candidate(patterns = ['abc', 'cab', 'bca'],word = "abcabcabcabc") == 3
    assert candidate(patterns = ['xyz', 'zyx', 'xy', 'yx', 'xzy', 'yzx'],word = "zyxwvutsrqponmlkjihgfedcba") == 2
    assert candidate(patterns = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff'],word = "abcdefabcdefabcdef") == 0
    assert candidate(patterns = ['abc', 'def', 'ghi'],word = "defabc") == 2
    assert candidate(patterns = ['quick', 'brown', 'fox'],word = "thequickbrownfoxjumpsoverthelazydog") == 3
    assert candidate(patterns = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],word = "abcdef ghijklmnopqrstuvwxyz") == 9
    assert candidate(patterns = ['aaa', 'aa', 'a'],word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 3
    assert candidate(patterns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],word = "abcdefghijabcdefghij") == 10
    assert candidate(patterns = ['test', 'string', 'finding', 'substring'],word = "teststringfindingsubstring") == 4
    assert candidate(patterns = ['aa', 'aaa', 'aaaa'],word = "aaaa") == 3
    assert candidate(patterns = ['short', 'shot', 'dot'],word = "shortshot") == 2
    assert candidate(patterns = ['foo', 'bar', 'foobar', 'barfoo'],word = "foobarbarfoobarfoo") == 4
    assert candidate(patterns = ['aba', 'bab', 'aba'],word = "ababababa") == 3
    assert candidate(patterns = ['hello', 'world', 'python'],word = "pythonworldhello") == 3
    assert candidate(patterns = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'],word = "abcacbcbacbacbcbac") == 5
    assert candidate(patterns = ['banana', 'ana', 'nan', 'ban'],word = "banananana") == 4
    assert candidate(patterns = ['abc', 'abcd', 'abcde'],word = "abcdefgh") == 3
    assert candidate(patterns = ['abcd', 'dcba', 'abcd'],word = "abcdcbaabcd") == 3
    assert candidate(patterns = ['aaaa', 'bbbb', 'cccc', 'dddd'],word = "abcdeabcdeabcde") == 0
    assert candidate(patterns = ['longpattern', 'long', 'pattern'],word = "longpatternlongpattern") == 3
    assert candidate(patterns = ['ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij'],word = "abcdefghij") == 9
    assert candidate(patterns = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz'],word = "abcdefghijklmnopqrstuvwxyz") == 24
    assert candidate(patterns = ['zzz', 'zzzz', 'zzzzz'],word = "zzzzzzzzzz") == 3
    assert candidate(patterns = ['ab', 'bc', 'cd', 'de'],word = "abcde") == 4
    assert candidate(patterns = ['abc', 'bcd', 'cde', 'def'],word = "abcdefg") == 4
    assert candidate(patterns = ['abc', 'abcd', 'abcde', 'abcdef'],word = "abcdefg") == 4
    assert candidate(patterns = ['test', 'tset', 'sett', 'settset'],word = "testsettsettset") == 4
    assert candidate(patterns = ['small', 'medium', 'large', 'extra', 'huge'],word = "smallmediumlargeextrahuge") == 5
    assert candidate(patterns = ['pattern', 'tern', 'ternary', 'ternarysearch'],word = "binarysearchternarysearch") == 3
    assert candidate(patterns = ['xyz', 'zyx', 'yzx'],word = "xyzzyxzyxzyx") == 2
    assert candidate(patterns = ['abcd', 'efgh', 'ijkl'],word = "efghijklabcd") == 3
    assert candidate(patterns = ['abc', 'cab', 'bac', 'bca', 'acb', 'cba'],word = "abcabcabc") == 3
    assert candidate(patterns = ['abc', 'abcabc', 'abcabcabc'],word = "abcabcabcabc") == 3
    assert candidate(patterns = ['aaa', 'bbb', 'ccc'],word = "abacabadabc") == 0
    assert candidate(patterns = ['one', 'two', 'three', 'onetwothree'],word = "onetwothreeonetwothree") == 4
    assert candidate(patterns = ['search', 'sear', 'arch'],word = "searchingthesearchinthesearch") == 3
    assert candidate(patterns = ['overlap', 'lap', 'lapping'],word = "lapping") == 2
    assert candidate(patterns = ['abc', 'def', 'ghi', 'jkl'],word = "abcdefghijklmnopqrstuvwxyz") == 4
    assert candidate(patterns = ['abc', 'def', 'ghi', 'jkl'],word = "abcdefghijk") == 3
    assert candidate(patterns = ['xyz', 'zyx', 'wxy', 'uvw'],word = "xyzzyxwxyuvw") == 4
    assert candidate(patterns = ['abc', 'def', 'ghi', 'jkl'],word = "abcdefghij") == 3
    assert candidate(patterns = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yz'],word = "abcdefghijklmnopqrstuvwxyz") == 7
    assert candidate(patterns = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],word = "abcdefghijklmnopqrstuvwxyz") == 9
    assert candidate(patterns = ['zz', 'zzz', 'zzzz'],word = "zzzzzzzzzz") == 3
    assert candidate(patterns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],word = "zyxwvutsrqponmlkjihgfedcba") == 26
    assert candidate(patterns = ['example', 'ample', 'mple', 'ple', 'le', 'e'],word = "exampleexampleexample") == 6
    assert candidate(patterns = ['ab', 'ba', 'ac', 'ca', 'bc', 'cb'],word = "abcbaacbba") == 5
    assert candidate(patterns = ['abc', 'def', 'ghi'],word = "abcdefghi") == 3
    assert candidate(patterns = ['xyz', 'zyx', 'yzx'],word = "xyzzyxzyx") == 2
    assert candidate(patterns = ['zzz', 'zz', 'z'],word = "zzzzzzzzzz") == 3
    assert candidate(patterns = ['pattern', 'tern', 'ternary', 'ary'],word = "patternarypatternary") == 4
    assert candidate(patterns = ['xyz', 'abc', 'def', 'ghi', 'jkl'],word = "zyxwvutsrqponmlkjihgfedcba") == 0
    assert candidate(patterns = ['a', 'ab', 'abc', 'abcd'],word = "abcdabcdabcd") == 4


