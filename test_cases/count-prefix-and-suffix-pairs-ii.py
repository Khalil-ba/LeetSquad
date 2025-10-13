# Import the utils module for prompts
from utils import *

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
