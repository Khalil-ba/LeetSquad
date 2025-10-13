# Import the utils module for prompts
from utils import *

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
