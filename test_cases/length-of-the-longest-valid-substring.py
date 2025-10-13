# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(word = "zzzzzzzzzz",forbidden = ['zz']) == 1
    assert candidate(word = "abacab",forbidden = ['ba', 'ca']) == 2
    assert candidate(word = "leetcode",forbidden = ['de', 'le', 'e']) == 4
    assert candidate(word = "abcde",forbidden = ['fgh']) == 5
    assert candidate(word = "aaaaaaa",forbidden = ['aa']) == 1
    assert candidate(word = "aaaabaaa",forbidden = ['aa']) == 3
    assert candidate(word = "abcde",forbidden = ['fgh', 'ijk']) == 5
    assert candidate(word = "xyz",forbidden = ['xy', 'yz']) == 1
    assert candidate(word = "cbaaaabc",forbidden = ['aaa', 'cb']) == 4
    assert candidate(word = "abcdefghijklmnopqrstuvwxyz",forbidden = ['abc', 'xyz']) == 24
    assert candidate(word = "abcd",forbidden = ['a', 'b', 'c', 'd']) == 0
    assert candidate(word = "abacaba",forbidden = ['ba', 'ca']) == 2
    assert candidate(word = "abcde",forbidden = ['ab', 'bc', 'cd', 'de']) == 1
    assert candidate(word = "aaabbbcccddd",forbidden = ['aaa', 'bbb', 'ccc', 'ddd', 'abc']) == 4
    assert candidate(word = "abcdefghijklmnopqrstuvwxyz",forbidden = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']) == 4
    assert candidate(word = "pppppppppppppppppppppppppppppppppp",forbidden = ['pp', 'p']) == 0
    assert candidate(word = "abcdefghijabcdefghij",forbidden = ['abc', 'def', 'ghi', 'jij', 'fed', 'cba']) == 5
    assert candidate(word = "abcdefghijabcdefghij",forbidden = ['abcdefghij', 'abc', 'def', 'ghi', 'jih', 'ihg', 'fed', 'cba']) == 5
    assert candidate(word = "xyxzyzyxzyzyzxzyzx",forbidden = ['xyz', 'zyx', 'xzy']) == 7
    assert candidate(word = "hellothere",forbidden = ['he', 'lo', 'th', 'er', 'ere']) == 3
    assert candidate(word = "xyzxyzxyzxyz",forbidden = ['xy', 'yz', 'zx', 'xyz']) == 1
    assert candidate(word = "abcdefghij",forbidden = ['abc', 'def', 'ghi', 'j']) == 4
    assert candidate(word = "abcdeabcdeabcde",forbidden = ['abc', 'cde', 'dea', 'bcd']) == 3
    assert candidate(word = "abcdefghijklmnopqrstuvwxyz",forbidden = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']) == 2
    assert candidate(word = "pneumonoultramicroscopicsilicovolcanoconiosis",forbidden = ['pneumo', 'ultra', 'micro', 'scopic', 'silico', 'volcano', 'conio', 'osis', 'pneumonoultramicro', 'microscopic', 'scopicsilico', 'silicovolcano', 'volcanoconi', 'conoosis']) == 11
    assert candidate(word = "qwertyuiopasdfghjklzxcvbnm",forbidden = ['qwe', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop', 'asd', 'sdf', 'dfg', 'fgh', 'ghj', 'hjk', 'jkl', 'klz', 'lzx', 'zxc', 'xcv', 'cvb', 'vbn', 'bnm']) == 4
    assert candidate(word = "mississippi",forbidden = ['iss', 'sip', 'issi', 'ippi']) == 4
    assert candidate(word = "abcabcabcabc",forbidden = ['abcabc', 'bcab', 'cababc']) == 5
    assert candidate(word = "aaaaaaaaaabbbbbbbbbb",forbidden = ['aaa', 'bbb', 'ab', 'ba', 'aab', 'bba']) == 2
    assert candidate(word = "banana",forbidden = ['na', 'an', 'ba', 'baa', 'nan', 'ban', 'anan']) == 1
    assert candidate(word = "abcdefghijklmnopqrstuvwxyz",forbidden = ['xyz', 'uvw', 'rst', 'qpo', 'lmn', 'fed', 'cba']) == 13
    assert candidate(word = "banana",forbidden = ['ana', 'nan', 'ba', 'na', 'an']) == 1
    assert candidate(word = "qwertyuiopasdfghjklzxcvbnm",forbidden = ['qwe', 'rty', 'uiop', 'asdf', 'ghjk', 'lzx', 'cvb', 'nm']) == 6
    assert candidate(word = "xyzxyzxyzxyz",forbidden = ['xy', 'yz', 'zx']) == 1
    assert candidate(word = "aaaaabbbbbcccccc",forbidden = ['aaaa', 'bbbb', 'cccc', 'ab', 'bc', 'ca']) == 3
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",forbidden = ['aabb', 'bbcc', 'ccdd', 'ddee', 'eefg', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'zyz']) == 45
    assert candidate(word = "abcabcabcabc",forbidden = ['abc', 'cab', 'bca']) == 2
    assert candidate(word = "abcdefghijklmnopqrstuvwxyz",forbidden = ['abc', 'xyz', 'mnop', 'qrst']) == 14
    assert candidate(word = "ababababab",forbidden = ['aba', 'bab', 'aaa']) == 2
    assert candidate(word = "mississippi",forbidden = ['issi', 'iss', 'ss', 'ssip', 'ippi']) == 4
    assert candidate(word = "xyzxyzxyz",forbidden = ['xyz', 'xy', 'yz']) == 2
    assert candidate(word = "abcabcabcabcabc",forbidden = ['abc', 'bca', 'cab']) == 2
    assert candidate(word = "abababababababab",forbidden = ['aba', 'bab', 'abb']) == 2
    assert candidate(word = "hellohellohellohello",forbidden = ['he', 'el', 'll', 'lo', 'oh']) == 1
    assert candidate(word = "xyxyxyxyxyxyxyxy",forbidden = ['xyx', 'yxy', 'xyxy']) == 2
    assert candidate(word = "abacabadabacaba",forbidden = ['aba', 'abc', 'bac']) == 5
    assert candidate(word = "mississippi",forbidden = ['issi', 'iss', 'is', 'mp', 'ss', 'pp']) == 3
    assert candidate(word = "abcdefghij",forbidden = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl']) == 2
    assert candidate(word = "mississippi",forbidden = ['iss', 'issi', 'ippi', 'issipp', 'missi', 'sissi', 'ssippi']) == 5
    assert candidate(word = "nolongerforbidden",forbidden = ['for', 'bidden', 'no', 'longer']) == 7
    assert candidate(word = "qwertypoiuytrewq",forbidden = ['qw', 'we', 'er', 'rt', 'ty', 'yu', 'ui', 'io', 'op']) == 11
    assert candidate(word = "banana",forbidden = ['na', 'ba', 'an']) == 1
    assert candidate(word = "thisthisthisthisthis",forbidden = ['thi', 'hist', 'isth', 'histh', 'thist']) == 3
    assert candidate(word = "mississippi",forbidden = ['iss', 'issi', 'ippi']) == 5
    assert candidate(word = "abababababababab",forbidden = ['aba', 'bab', 'aab', 'bba']) == 2
    assert candidate(word = "qwertyuiopasdfghjklzxcvbnm",forbidden = ['qw', 'er', 'ty', 'ui', 'op', 'as', 'df', 'gh', 'jk', 'kl', 'zx', 'cv', 'vb', 'bn', 'nm']) == 2
    assert candidate(word = "abcdabcdabcdabcdabcdabcd",forbidden = ['abcd', 'bcda', 'cdab', 'dabc']) == 3
    assert candidate(word = "abacaxabcd",forbidden = ['ab', 'ca', 'bc', 'd']) == 3
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",forbidden = ['aa', 'bb', 'cc', 'zz', 'yy']) == 44
    assert candidate(word = "banana",forbidden = ['ana', 'nan', 'ban', 'ana', 'naa']) == 2
    assert candidate(word = "mississippi",forbidden = ['issi', 'iss', 'is', 'i', 's', 'p', 'mp']) == 1
    assert candidate(word = "abracadabra",forbidden = ['abr', 'rac', 'ada', 'bra', 'cab', 'cad']) == 3
    assert candidate(word = "abcdefghij",forbidden = ['abcdefghij', 'abcdefghi', 'bcdefgh', 'cdefgh', 'defgh', 'efgh', 'fgh', 'gh', 'h', 'ij']) == 7
    assert candidate(word = "abacabadabacaba",forbidden = ['aba', 'bad', 'cab', 'abc']) == 4
    assert candidate(word = "aaaaaaaaaa",forbidden = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']) == 0
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",forbidden = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 2
    assert candidate(word = "mnopqrstuvwxyzabcdefghijkl",forbidden = ['mnop', 'qrst', 'uvwx', 'yzab', 'cdef', 'ghij', 'klmn', 'opqr', 'stuv', 'wxyz']) == 6
    assert candidate(word = "aabbccddeeff",forbidden = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff']) == 2
    assert candidate(word = "abcabcabcabcabcabcabc",forbidden = ['abcabc', 'bcabc', 'cabc', 'abca', 'bca', 'cab', 'abc']) == 2
    assert candidate(word = "abacabadabacaba",forbidden = ['aba', 'aca', 'bad']) == 4
    assert candidate(word = "thisisaverylongwordthatneedstobecut",forbidden = ['this', 'is', 'very', 'long', 'word', 'that', 'needs', 'to', 'be', 'cut']) == 7
    assert candidate(word = "abacabacabacaba",forbidden = ['aba', 'aca', 'bab']) == 3
    assert candidate(word = "abacabadabacaba",forbidden = ['aba', 'abc', 'bac']) == 5
    assert candidate(word = "thisisateststring",forbidden = ['test', 'string', 'is', 'a', 'this']) == 8
    assert candidate(word = "mississippi",forbidden = ['issi', 'sip', 'iss', 'ippi', 'ppi']) == 4
    assert candidate(word = "abcdefghijklmnopqrstuvwxyz",forbidden = ['abc', 'xyz', 'mnop']) == 14
