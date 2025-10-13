# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(strs = ['zaz', 'zbz', 'zcz']) == 0
    assert candidate(strs = ['a', 'b']) == 0
    assert candidate(strs = ['zzz', 'zzz', 'zzz']) == 0
    assert candidate(strs = ['xyz', 'yza', 'zab']) == 2
    assert candidate(strs = ['abc', 'bcd', 'cde']) == 0
    assert candidate(strs = ['abc', 'abc', 'abc']) == 0
    assert candidate(strs = ['abcd', 'efgh', 'ijkl']) == 0
    assert candidate(strs = ['cba', 'daf', 'ghi']) == 1
    assert candidate(strs = ['abc', 'bce', 'cae']) == 1
    assert candidate(strs = ['zyx', 'wvu', 'tsr']) == 3
    assert candidate(strs = ['abcd', 'abce', 'abcf', 'abcg', 'abch', 'abci', 'abcj', 'abck', 'abcl', 'abcm', 'abcn', 'abco', 'abcp', 'abcq', 'abcr', 'abcs', 'abct', 'abcd', 'abce', 'abcf', 'abcg', 'abch', 'abci', 'abcj', 'abck', 'abcl', 'abcm', 'abcn', 'abco', 'abcp', 'abcq', 'abcr', 'abcs', 'abct']) == 1
    assert candidate(strs = ['xyz', 'yza', 'zab', 'abc', 'bcd', 'cde']) == 3
    assert candidate(strs = ['xyz', 'uvw', 'rst', 'qpo', 'nml', 'klm', 'jih', 'fed', 'cba']) == 3
    assert candidate(strs = ['qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop', 'opq', 'pqa', 'qaz', 'wsx', 'edc', 'rfv', 'tgb', 'yhn', 'ujm', 'ikl', 'olk', 'pvc', 'bnm']) == 3
    assert candidate(strs = ['xyz', 'xyx', 'xzy']) == 1
    assert candidate(strs = ['zyx', 'yxw', 'xwv', 'uvw']) == 3
    assert candidate(strs = ['abcd', 'dbca', 'efgh', 'hgfj']) == 2
    assert candidate(strs = ['abcd', 'abce', 'abcf', 'abcg', 'abch']) == 0
    assert candidate(strs = ['zz', 'zy', 'yx', 'xz', 'yz', 'zx']) == 2
    assert candidate(strs = ['abcd', 'dcba', 'abcd', 'dcba', 'abcd', 'dcba']) == 4
    assert candidate(strs = ['aabbcc', 'bbccdd', 'ccddee', 'ddeeff']) == 0
    assert candidate(strs = ['zzzz', 'zzzy', 'zzzx', 'zzxw']) == 2
    assert candidate(strs = ['mnop', 'mnoq', 'mnop']) == 1
    assert candidate(strs = ['aabbcc', 'abacbc', 'abcabc', 'acbacb', 'accbab', 'babcac', 'bbacab', 'bbcaab', 'bcabca', 'bcacab', 'bcbaca', 'bcbcaa', 'cacaba', 'cacbaa', 'caacab', 'caacba', 'cababc', 'cabacb', 'cabbac', 'cabcab', 'cabcba', 'cacabc', 'cacbba', 'cbabac', 'cbabca', 'cbacab', 'cbacba', 'cbbaca', 'cbbcaa', 'ccabab', 'ccabac', 'ccabba', 'ccbaab', 'ccbaca', 'ccbacb']) == 5
    assert candidate(strs = ['abcd', 'abdc', 'acdb']) == 1
    assert candidate(strs = ['aaaa', 'aaab', 'aabb', 'abbb']) == 0
    assert candidate(strs = ['abc', 'bac', 'bca', 'cab', 'cba', 'acb']) == 3
    assert candidate(strs = ['same', 'sake', 'sage', 'sage', 'sane', 'sane', 'sane']) == 1
    assert candidate(strs = ['abcdef', 'bcdefg', 'cdefgh', 'defghi']) == 0
    assert candidate(strs = ['abc', 'bac', 'cab', 'cba', 'bca', 'acb']) == 3
    assert candidate(strs = ['cat', 'dog', 'bat', 'rat', 'hat', 'mat', 'eat', 'tat', 'sat', 'pat']) == 3
    assert candidate(strs = ['abcd', 'dcba', 'abcd', 'dcba']) == 4
    assert candidate(strs = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'ffff']) == 0
    assert candidate(strs = ['apple', 'apply', 'appla']) == 1
    assert candidate(strs = ['zzzz', 'zzyx', 'zzyv', 'zzyu', 'zzyt', 'zzyr', 'zzys', 'zzyr', 'zzyp', 'zzyq', 'zzxo', 'zzxn', 'zzxm', 'zzxl', 'zzxk', 'zzxj', 'zzxi', 'zzxh', 'zzxg', 'zzxf', 'zzxe', 'zzxd', 'zzxc', 'zzwb', 'zzwa', 'zzza']) == 2
    assert candidate(strs = ['leetcode', 'loveleetcode', 'leetcodeer', 'leetcodexx']) == 7
    assert candidate(strs = ['abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij']) == 0
    assert candidate(strs = ['ab', 'ba', 'ab', 'ba', 'ab']) == 2
    assert candidate(strs = ['hello', 'helpp', 'hells']) == 1
    assert candidate(strs = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij', 'fghijk']) == 0
    assert candidate(strs = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yzc']) == 1
    assert candidate(strs = ['mnop', 'qrst', 'uvwx', 'yzab']) == 2
    assert candidate(strs = ['abcd', 'abdc', 'acbd', 'adbc']) == 2
    assert candidate(strs = ['xyzz', 'wvut', 'qrst', 'ponm', 'lkji', 'hgfed', 'cbazyx', 'abcdefgh']) == 4
    assert candidate(strs = ['qrst', 'qrsu', 'qrsu']) == 0
    assert candidate(strs = ['abcd', 'abcf', 'abce', 'abcd', 'abcf', 'abcd']) == 1
    assert candidate(strs = ['qrst', 'abcd', 'mnop', 'efgh']) == 4
    assert candidate(strs = ['abcd', 'dddd', 'abcd', 'dddd']) == 3
    assert candidate(strs = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']) == 1
    assert candidate(strs = ['hello', 'hallo', 'hullo', 'hella']) == 2
    assert candidate(strs = ['aabbccdd', 'bbaaccee', 'ccddeeff', 'ddeeffgg']) == 2
    assert candidate(strs = ['zyxwvu', 'utsrqo', 'ponmlk', 'jihgfed', 'cba']) == 6
    assert candidate(strs = ['abc', 'bca', 'cab', 'acb']) == 3
    assert candidate(strs = ['pqr', 'stu', 'vwx', 'yzp']) == 1
    assert candidate(strs = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy']) == 0
    assert candidate(strs = ['mnop', 'mlkj', 'ihgf', 'edcb']) == 4
    assert candidate(strs = ['xyz', 'zyx', 'yzz', 'xzz']) == 2
    assert candidate(strs = ['zzzz', 'yyyy', 'xxxx', 'wwww']) == 4
    assert candidate(strs = ['abcdefg', 'bcdefgh', 'cdefghi', 'defghij', 'efghijk', 'fghijkl', 'ghijklm']) == 0
    assert candidate(strs = ['xyz', 'wxy', 'uvw', 'stu']) == 3
    assert candidate(strs = ['mnop', 'mnop', 'mnop', 'mnop']) == 0
    assert candidate(strs = ['a', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']) == 1
    assert candidate(strs = ['abcd', 'acbd', 'adbc', 'dabc', 'dbac', 'dcab', 'dcba']) == 3
    assert candidate(strs = ['abcd', 'acfg', 'aegi', 'afih']) == 1
    assert candidate(strs = ['aabbcc', 'bbccdd', 'ccddeeff', 'ddeeffgg', 'eeffgghh', 'ffgghhii']) == 0
    assert candidate(strs = ['xyz', 'uvw', 'rst', 'qpo']) == 3
    assert candidate(strs = ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']) == 3
    assert candidate(strs = ['abcdefgh', 'hgfedcba', 'abcdefgh', 'hgfedcba', 'abcdefgh', 'hgfedcba']) == 8
    assert candidate(strs = ['mnop', 'mnoq', 'mnop', 'mnop']) == 1
    assert candidate(strs = ['abcd', 'abcf', 'abce', 'abch', 'abcd', 'abci', 'abcd', 'abck']) == 1
    assert candidate(strs = ['aeg', 'bdf', 'cce']) == 2
    assert candidate(strs = ['mnop', 'qrst', 'uvwx', 'yzab', 'cdef', 'ghij', 'klmn', 'opqr', 'stuv', 'wxyz']) == 4
    assert candidate(strs = ['abcd', 'bcde', 'cdef', 'defg']) == 0
    assert candidate(strs = ['abcdef', 'acdefg', 'aeghij']) == 0
    assert candidate(strs = ['abcd', 'bfgh', 'cgij', 'dhjk']) == 0
    assert candidate(strs = ['banana', 'bandana', 'bananna']) == 2
    assert candidate(strs = ['abcd', 'abdc', 'abcc']) == 2
    assert candidate(strs = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwx', 'vwxy', 'wxyz']) == 0
    assert candidate(strs = ['aabbcc', 'bbccdd', 'ccddeeff', 'ddeeffgg']) == 0
    assert candidate(strs = ['pqr', 'pqs', 'pqt', 'pqu', 'pqv', 'pqw', 'pqx', 'pqy', 'pqz']) == 0
    assert candidate(strs = ['abcdef', 'fghijk', 'lmnopq', 'rstuvw', 'xyzuvw', 'vwxyzw', 'utrewq', 'ponmlk', 'jihgfedcba']) == 6
    assert candidate(strs = ['zyxwv', 'utsrq', 'ponml', 'kjihg', 'fedcba']) == 5
    assert candidate(strs = ['zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz']) == 0
    assert candidate(strs = ['abcdefg', 'bcdefgh', 'cdefghi', 'defghij', 'efghijk']) == 0
    assert candidate(strs = ['water', 'waste', 'wider']) == 3
    assert candidate(strs = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj', 'kkk']) == 0
    assert candidate(strs = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj', 'kkk', 'lll', 'mmm', 'nnn', 'ooo', 'ppp', 'qqq', 'rrr', 'sss', 'ttt', 'uuu', 'vvv', 'www', 'xxx', 'yyy', 'zzz']) == 0
    assert candidate(strs = ['abcd', 'acfg', 'aegh']) == 0
    assert candidate(strs = ['zzzzzzzz', 'zzyyyyxx', 'zyxwvutu', 'zyxwvuts']) == 7
    assert candidate(strs = ['xzy', 'uvw', 'rst', 'qpo', 'nml', 'klm', 'jih', 'fed', 'cba', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yzx']) == 3
    assert candidate(strs = ['abcdefghijklmnopqrstuvwxyz', 'bcdefghijklmnopqrstuvwxyza', 'cdefghijklmnopqrstuvwxyzab', 'defghijklmnopqrstuvwxyzabcde', 'efghijklmnopqrstuvwxyzabcdefg', 'fghijklmnopqrstuvwxyzabcdefg hijklmnopqrstuvwxyzabcdefg hijklmnopqrstuvwxyzabcdefg hijklmnopqrstuvwxyzabcdefg hijklmnopqrstuvwxyzabcdefg hijklmnopqrstuvwxyzabcdefg hijklmnopqrstuvwxyzabcdefg']) == 5
    assert candidate(strs = ['abc', 'bca', 'cab', 'bac']) == 3
    assert candidate(strs = ['aab', 'aac', 'aab', 'aac']) == 1
    assert candidate(strs = ['abcd', 'bfgh', 'cgij', 'dhkj']) == 0
    assert candidate(strs = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee', 'fffff', 'ggggg', 'hhhhh', 'iiiii', 'jjjjj']) == 0
    assert candidate(strs = ['abcd', 'efgh', 'ijkl', 'mnop']) == 0
    assert candidate(strs = ['abcd', 'bfgh', 'cijj', 'dklm']) == 0
    assert candidate(strs = ['abcdefg', 'bcdefga', 'cdefgab', 'defgabc']) == 3
    assert candidate(strs = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee']) == 0
