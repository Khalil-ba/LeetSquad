# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(strs = ['zyx', 'zyx', 'zyx']) == 2
    assert candidate(strs = ['rrjk', 'furt', 'guzm']) == 2
    assert candidate(strs = ['axx', 'ggs', 'zzz']) == 0
    assert candidate(strs = ['ghi', 'def', 'abc']) == 0
    assert candidate(strs = ['aaa', 'bbb', 'ccc']) == 0
    assert candidate(strs = ['abc', 'bcd', 'cde']) == 0
    assert candidate(strs = ['abc', 'abc', 'abc']) == 0
    assert candidate(strs = ['a', 'b', 'c', 'd']) == 0
    assert candidate(strs = ['abcdef', 'uvwxyz']) == 0
    assert candidate(strs = ['zzz', 'aaa', 'zzz']) == 0
    assert candidate(strs = ['zyx', 'wvu', 'tsr']) == 2
    assert candidate(strs = ['edcba']) == 4
    assert candidate(strs = ['abcd', 'abdc', 'acdb']) == 1
    assert candidate(strs = ['abcd', 'dbca', 'adcb', 'cbad']) == 3
    assert candidate(strs = ['babca', 'bbazb']) == 3
    assert candidate(strs = ['a', 'b', 'c']) == 0
    assert candidate(strs = ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzabcd']) == 2
    assert candidate(strs = ['abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij']) == 0
    assert candidate(strs = ['fedcb', 'edcba', 'dcbae', 'cbade', 'baced', 'acbed']) == 4
    assert candidate(strs = ['zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba']) == 25
    assert candidate(strs = ['abcd', 'adbc', 'bacd', 'bdac']) == 2
    assert candidate(strs = ['abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij']) == 0
    assert candidate(strs = ['abacabad', 'babacaba', 'cacabada', 'dacabada']) == 5
    assert candidate(strs = ['abcdabcd', 'dcbaabcd', 'abcdabdc', 'abdcabcd', 'abcdcdab', 'cdabcdab', 'abcdabcd', 'cdababcd', 'abcdcdab', 'dcabcdab']) == 6
    assert candidate(strs = ['abcdefgh', 'hgfedcba', 'abcdefgh', 'hgfedcba', 'abcdefgh']) == 7
    assert candidate(strs = ['leetcode', 'leetcoed', 'leetcdeo', 'leetcodeo', 'leetcodeo', 'leetcodeo']) == 5
    assert candidate(strs = ['zyx', 'yxz', 'xyz']) == 2
    assert candidate(strs = ['aabbaa', 'abcabc', 'acbacb', 'bacbac', 'bbacab']) == 4
    assert candidate(strs = ['zzz', 'yyy', 'xxx', 'www', 'vvv', 'uuu']) == 0
    assert candidate(strs = ['abcdefgh', 'bcadegfh', 'cgdbefha', 'dgfbceha', 'egfdcbha', 'fgecadhb']) == 5
    assert candidate(strs = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklnmopqrstuvwxyz']) == 25
    assert candidate(strs = ['abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh']) == 0
    assert candidate(strs = ['zabc', 'zcad', 'zdba', 'zeac', 'zfcd', 'zgda', 'zhec', 'zida', 'zjea', 'zkcf']) == 3
    assert candidate(strs = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm']) == 0
    assert candidate(strs = ['azazaz', 'bababa', 'cacaca', 'dadada', 'eaeaea']) == 3
    assert candidate(strs = ['abcdefg', 'bcefgij', 'acdfhij']) == 0
    assert candidate(strs = ['abcd', 'abdc', 'acdb', 'cadb', 'dabc']) == 2
    assert candidate(strs = ['xyz', 'zyx', 'wvu', 'tsr', 'qpo', 'nml', 'kji', 'hgf', 'edc', 'baa']) == 2
    assert candidate(strs = ['aeg', 'bdh', 'cfi', 'egj', 'fhk', 'gjl']) == 0
    assert candidate(strs = ['qrst', 'mnop', 'ijkl', 'efgh', 'abcd', 'mnop', 'qrst', 'efgh', 'ijkl', 'abcd', 'mnop', 'qrst', 'efgh', 'ijkl', 'abcd', 'mnop', 'qrst', 'efgh', 'ijkl', 'abcd']) == 0
    assert candidate(strs = ['zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz']) == 0
    assert candidate(strs = ['zzzzzzzz', 'zzzzzzzy', 'zzzzzzzx', 'zzzzzzyx', 'zzzzzyxy', 'zzzzyxxy', 'zzzyxxyx', 'zzyxxyxy']) == 6
    assert candidate(strs = ['abcdefghij', 'abcdefghik', 'abcdefghij', 'abcdefghim', 'abcdefghin']) == 0
    assert candidate(strs = ['aabbcc', 'bbccaa', 'ccaabb', 'aabbbc']) == 4
    assert candidate(strs = ['abcdefg', 'bceghik', 'acegikm', 'adegimn']) == 0
    assert candidate(strs = ['qwertyuiop', 'asdfghjklz', 'zxcvbnmqwe', 'qwertyuiop', 'asdfghjklz']) == 7
    assert candidate(strs = ['qrst', 'rstu', 'stuv', 'tuvw', 'uvwx']) == 0
    assert candidate(strs = ['aabbccdd', 'bbaaccee', 'ccaabbee', 'ddeebbaa', 'eeccbbdd']) == 6
    assert candidate(strs = ['zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba']) == 25
    assert candidate(strs = ['zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz']) == 0
    assert candidate(strs = ['qwerty', 'wertyq', 'ertyqw', 'rtyqwe', 'tyqwer', 'yqwret']) == 5
    assert candidate(strs = ['cba', 'bca', 'bac', 'acb']) == 2
    assert candidate(strs = ['aebf', 'accf', 'bdgf', 'cddg', 'defh', 'edgh', 'feih', 'gjih', 'hkji']) == 2
    assert candidate(strs = ['aabbcc', 'bbaacc', 'ccabba', 'aababc', 'bbacab', 'abcabc', 'cbaabc', 'abacba', 'bacabc', 'cababc']) == 4
    assert candidate(strs = ['zyxwvu', 'utsrqpon', 'mlkjihgf', 'edcba']) == 5
    assert candidate(strs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == 0
    assert candidate(strs = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy']) == 0
    assert candidate(strs = ['cba', 'daf', 'gee']) == 2
    assert candidate(strs = ['abc', 'bac', 'cab', 'bca', 'cab', 'cba']) == 2
    assert candidate(strs = ['leetcode', 'leetcede', 'leotcede']) == 5
    assert candidate(strs = ['zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba']) == 25
    assert candidate(strs = ['zzzz', 'zzzz', 'zzzz', 'zzzz', 'zzzz']) == 0
    assert candidate(strs = ['abcd', 'adcb', 'bacd', 'bdac', 'cabd', 'cdab', 'dcba', 'dcab', 'dabc', 'dacb']) == 3
    assert candidate(strs = ['zzzz', 'zzyz', 'zyyz', 'yzzz', 'yzyz', 'yyyz', 'yyyx', 'yyxx', 'yxxx', 'xxxx']) == 3
    assert candidate(strs = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yzab']) == 2
    assert candidate(strs = ['aabbcc', 'bbaacc', 'bbacac', 'aabcbc', 'cababc', 'bcbacc']) == 3
    assert candidate(strs = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']) == 0
    assert candidate(strs = ['xyz', 'zyx', 'yxz', 'xzy', 'yzx', 'zxy']) == 2
    assert candidate(strs = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'mnopqrstuvwxyzabcdefghijkl', 'fedcbazyxwvutsrqponmlkjihg']) == 25
    assert candidate(strs = ['mnopqr', 'opqrst', 'pqrstu', 'qrstuv']) == 0
    assert candidate(strs = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn']) == 0
    assert candidate(strs = ['abcd', 'dcba', 'abcd', 'dcba']) == 3
    assert candidate(strs = ['aabbcc', 'bbccaa', 'ccaabb', 'aabbbc', 'bbccaa', 'ccaabb', 'aabbbc']) == 4
    assert candidate(strs = ['abcdefg', 'gfedcba', 'bacdefg', 'ihgfedc', 'jklmnop']) == 6
    assert candidate(strs = ['pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']) == 0
    assert candidate(strs = ['qpwoeiruty', 'qpwoeiruty', 'qpwoeiruty']) == 5
    assert candidate(strs = ['mnop', 'qrst', 'uvwx', 'yzab', 'cdef', 'ghij', 'klmn', 'opqr', 'stuv', 'wxyz']) == 2
    assert candidate(strs = ['abcd', 'bcde', 'cdef', 'defg']) == 0
    assert candidate(strs = ['aabbcc', 'abbccc', 'abcccc', 'bcccdd', 'cccddd', 'ccdddd', 'cddddd', 'dddddd']) == 0
    assert candidate(strs = ['aabbccddeeff', 'abcdefabcdef', 'fedcbafedcba', 'abcdefabcdef', 'aabbccddeeff']) == 10
    assert candidate(strs = ['abcdefghij', 'jihgfedcba', 'abcdefghij', 'jihgfedcba', 'abcdefghij', 'jihgfedcba']) == 9
    assert candidate(strs = ['zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba', 'zyxwvutsrqponmlkjihgfedcba']) == 25
    assert candidate(strs = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwx', 'vwxy', 'wxyz']) == 0
    assert candidate(strs = ['aabbcc', 'bbccdd', 'ccddeeff', 'ddeeffgg']) == 0
    assert candidate(strs = ['abcdabcd', 'bcdbcdcd', 'cdcdcdcd', 'dcdcdcdc', 'efefefef', 'fefefefe', 'gfefefef', 'hfhfhfhf', 'ihihihih']) == 5
    assert candidate(strs = ['xyzuvw', 'wvuxyz', 'uvwxyx', 'vxyzwu', 'uzwvxy', 'zwxyuv', 'yxwvuz', 'zyxuvw', 'wvuzxy', 'uvwxyx', 'vxyzwu', 'uzwvxy', 'zwxyuv', 'yxwvuz', 'zyxuvw', 'wvuzxy', 'uvwxyx', 'vxyzwu', 'uzwvxy', 'zwxyuv', 'yxwvuz', 'zyxuvw']) == 5
    assert candidate(strs = ['abcde', 'bcdef', 'cdefg', 'defgh', 'efghi', 'fghij', 'ghijk', 'hijkl', 'ijklm', 'jklmn']) == 0
    assert candidate(strs = ['zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz']) == 0
    assert candidate(strs = ['ba', 'ab', 'ba', 'ab', 'ba', 'ab']) == 1
    assert candidate(strs = ['zab', 'bac', 'cab', 'dcb']) == 2
    assert candidate(strs = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk']) == 4
    assert candidate(strs = ['abcdef', 'fedcba', 'dcbaef', 'bacfed', 'efabcd', 'fedcba']) == 5
    assert candidate(strs = ['aaaaaaaaaa', 'aabbaabbcc', 'aabbaabbcc', 'aabbaabbcc', 'aabbaabbcc', 'aabbaabbcc']) == 2
    assert candidate(strs = ['abcd', 'dcba', 'abcd', 'dcba', 'abcd']) == 3
    assert candidate(strs = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee', 'fffff', 'ggggg', 'hhhhh', 'iiiii', 'jjjjj']) == 0
    assert candidate(strs = ['aabb', 'bbaa', 'abab', 'baba', 'abba', 'baab']) == 3
    assert candidate(strs = ['abcd', 'abdc', 'acbd', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']) == 3
    assert candidate(strs = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk', 'pqrst', 'tsrqp', 'uvwxy', 'yxwvu', 'z', 'z', 'z', 'z', 'z']) == 4
    assert candidate(strs = ['abcd', 'efgh', 'ijkl', 'mnop']) == 0
    assert candidate(strs = ['abcdefg', 'gfedcba', 'hijklmn', 'nmolkji', 'opqrstu', 'utsrqpo']) == 6
