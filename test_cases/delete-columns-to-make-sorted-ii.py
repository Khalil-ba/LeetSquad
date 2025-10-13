# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(strs = ['ppp', 'qqq', 'rrr']) == 0
    assert candidate(strs = ['az', 'za']) == 0
    assert candidate(strs = ['xc', 'yb', 'za']) == 0
    assert candidate(strs = ['dog', 'cat', 'bat']) == 2
    assert candidate(strs = ['abcdef', 'uvwxyz']) == 0
    assert candidate(strs = ['abcd', 'abce', 'abcf']) == 0
    assert candidate(strs = ['aaa', 'aaa', 'aaa']) == 0
    assert candidate(strs = ['abc', 'bcd', 'cde']) == 0
    assert candidate(strs = ['zzz', 'aaa', 'zzz']) == 3
    assert candidate(strs = ['abc', 'acd', 'acc']) == 1
    assert candidate(strs = ['zyx', 'wvu', 'tsr']) == 3
    assert candidate(strs = ['axz', 'byz', 'cxz']) == 0
    assert candidate(strs = ['abc', 'acd', 'ace']) == 0
    assert candidate(strs = ['a', 'b', 'c']) == 0
    assert candidate(strs = ['abc', 'bca', 'cab']) == 0
    assert candidate(strs = ['zzz', 'zzz', 'zzz', 'zzz']) == 0
    assert candidate(strs = ['dddd', 'ddda', 'dddd', 'dddd']) == 1
    assert candidate(strs = ['aab', 'abc', 'aaa']) == 2
    assert candidate(strs = ['ca', 'bb', 'ac']) == 1
    assert candidate(strs = ['abcd', 'efgh', 'ijkl']) == 0
    assert candidate(strs = ['az', 'by', 'cx']) == 0
    assert candidate(strs = ['cba', 'daf', 'ghi']) == 0
    assert candidate(strs = ['aab', 'aac', 'aba']) == 0
    assert candidate(strs = ['ghi', 'daf', 'cba']) == 3
    assert candidate(strs = ['abcd', 'efgh', 'ijkl', 'mnop']) == 0
    assert candidate(strs = ['aaa', 'bbb', 'ccc']) == 0
    assert candidate(strs = ['a', 'b', 'c', 'd']) == 0
    assert candidate(strs = ['cba', 'bca', 'cab']) == 2
    assert candidate(strs = ['pqrs', 'qrsn', 'rsnp', 'snpq']) == 0
    assert candidate(strs = ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzabcd']) == 0
    assert candidate(strs = ['aax', 'aba', 'aca', 'ada']) == 0
    assert candidate(strs = ['aab', 'bac', 'aaa']) == 2
    assert candidate(strs = ['xyz', 'yza', 'zab', 'abc', 'bcd']) == 3
    assert candidate(strs = ['xyzz', 'yxzz', 'zxyy', 'zyyx']) == 0
    assert candidate(strs = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']) == 0
    assert candidate(strs = ['abc', 'cab', 'bca', 'bac', 'acb', 'cba']) == 3
    assert candidate(strs = ['fgh', 'ghi', 'hij', 'ijk', 'jkl']) == 0
    assert candidate(strs = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij']) == 0
    assert candidate(strs = ['aaaaa', 'aaabb', 'aabaa', 'aabbb', 'abaaa', 'ababb', 'abaab', 'ababa', 'abbaa', 'abbab', 'abbba', 'abbbb', 'baaaa', 'baaab', 'baaba', 'baabb', 'bbaaa', 'bbaab', 'bbaba', 'bbbaa', 'bbbb', 'caaaa', 'caaab', 'caaba', 'caabb', 'cbaaa', 'cbaab', 'cbaba', 'cbbaa', 'cbbbb', 'daaaa', 'daaab', 'daaba', 'daabb', 'dbaaa', 'dbaab', 'dbaba', 'dbbaa', 'dbbbb', 'eaaaa', 'eaab', 'eaaba', 'eaabb', 'ebaaa', 'ebaab', 'ebaba', 'ebbaa', 'ebbbb', 'faaaa', 'faaab', 'faaba', 'faabb', 'fbaaa', 'fbaab', 'fbaba', 'fbbaa', 'fbbbb']) == 2
    assert candidate(strs = ['zzzzz', 'zzzzx', 'zzzzy', 'zzzzz', 'zzzzz']) == 1
    assert candidate(strs = ['abcde', 'bcdef', 'cdefg', 'defgh', 'efghi']) == 0
    assert candidate(strs = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij']) == 0
    assert candidate(strs = ['abc', 'bac', 'bca', 'cab', 'cba', 'acb']) == 3
    assert candidate(strs = ['banana', 'bandana', 'bandanna']) == 0
    assert candidate(strs = ['zzzzz', 'zzzzz', 'zzzzz', 'zzzzz', 'zzzzz', 'zzzzz', 'zzzzz', 'zzzzz', 'zzzzz']) == 0
    assert candidate(strs = ['qrst', 'prst', 'qrst', 'qrst', 'qrst']) == 1
    assert candidate(strs = ['ghijkl', 'hijklm', 'ijklmn', 'jklmno', 'klmnop']) == 0
    assert candidate(strs = ['random', 'ranbom', 'randam', 'randbm', 'randmm']) == 2
    assert candidate(strs = ['lmno', 'mnop', 'opqr', 'pqrs', 'qrst']) == 0
    assert candidate(strs = ['xyz', 'zyx', 'wxy', 'uvw']) == 3
    assert candidate(strs = ['xyzz', 'yxzz', 'zxyz', 'zzxy', 'zzzx']) == 0
    assert candidate(strs = ['abcd', 'abdc', 'acdb', 'adbc']) == 0
    assert candidate(strs = ['banana', 'banaba', 'banaaa', 'banbaa']) == 1
    assert candidate(strs = ['zzzz', 'zzzy', 'zzzx', 'zzxw', 'zzvw', 'zxvw', 'xvwu']) == 4
    assert candidate(strs = ['pqrst', 'qrstu', 'rstuv', 'stuvw', 'tuvwx', 'uvwxy', 'vwxyz']) == 0
    assert candidate(strs = ['abcd', 'dcba', 'abcd', 'dcba']) == 4
    assert candidate(strs = ['mnopqr', 'zyxwvu', 'tsrqup', 'lkjihg', 'fedcba']) == 6
    assert candidate(strs = ['abcde', 'bcdea', 'cdeab', 'deabc', 'eabcd']) == 0
    assert candidate(strs = ['apple', 'apply', 'appla']) == 1
    assert candidate(strs = ['zzzz', 'zzzy', 'zzzx', 'zzxw', 'zzvw', 'zzuv', 'zztu']) == 2
    assert candidate(strs = ['abcd', 'acbd', 'adbc', 'dabc', 'bdac']) == 4
    assert candidate(strs = ['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx']) == 0
    assert candidate(strs = ['apple', 'apply', 'appla', 'apple', 'applq']) == 1
    assert candidate(strs = ['nmop', 'mnop', 'mnop', 'mnop']) == 1
    assert candidate(strs = ['xyz', 'xyw', 'xyv', 'xyu', 'xyt', 'xys', 'xyr', 'xyp', 'xyo', 'xyn', 'xym', 'xyl', 'xyk', 'xyj', 'xyi', 'xyh', 'xyg', 'xyf', 'xye', 'xyd', 'xyc', 'xyb', 'xya']) == 1
    assert candidate(strs = ['abcde', 'abcdf', 'abcef', 'abceg', 'abcde']) == 2
    assert candidate(strs = ['zzzz', 'zzzy', 'zzyy', 'zyyy', 'yyyy', 'yyyz']) == 4
    assert candidate(strs = ['random', 'randome', 'randomly', 'randomly', 'randomly']) == 0
    assert candidate(strs = ['mnop', 'lmno', 'opqr', 'pqrs', 'qrst']) == 4
    assert candidate(strs = ['aab', 'abc', 'abc']) == 0
    assert candidate(strs = ['qwerty', 'asdfgh', 'zxcvbn']) == 6
    assert candidate(strs = ['x', 'y', 'z', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']) == 1
    assert candidate(strs = ['aabbcc', 'aabbbc', 'aabccc', 'aabccc', 'aabccc']) == 1
    assert candidate(strs = ['abc', 'bce', 'cae']) == 0
    assert candidate(strs = ['zebra', 'zaxar', 'zecos', 'zabba']) == 4
    assert candidate(strs = ['abcdef', 'bcdegh', 'cdefgh', 'defghi', 'efghij', 'fghijk']) == 0
    assert candidate(strs = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'ffff', 'gggg', 'hhhh']) == 0
    assert candidate(strs = ['apple', 'apply', 'appla', 'apppa']) == 1
    assert candidate(strs = ['abac', 'acba', 'baca', 'bcaa', 'cab', 'cba']) == 0
    assert candidate(strs = ['abcd', 'bcad', 'acbd']) == 1
    assert candidate(strs = ['abcd', 'adcb', 'bacd']) == 0
    assert candidate(strs = ['abcdabcd', 'bcdbcdbd', 'cdcddcdc', 'dedededc', 'eeedeeec']) == 0
    assert candidate(strs = ['aaaa', 'aaab', 'aaba', 'aabb', 'abaa', 'abab', 'abba', 'abbb', 'baaa', 'baab', 'baba', 'babb', 'bbaa', 'bbab', 'bbba', 'bbbb']) == 0
    assert candidate(strs = ['abcd', 'abdc', 'acdb', 'acbd']) == 2
    assert candidate(strs = ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']) == 0
    assert candidate(strs = ['aaaabbbb', 'bbbbaaaa', 'aabbaabb', 'abababab', 'bbaabbaa']) == 8
    assert candidate(strs = ['acbac', 'bcbac', 'cbbac', 'dcbac', 'ecbac', 'fcbac']) == 0
    assert candidate(strs = ['moon', 'moan', 'moon', 'mane']) == 3
    assert candidate(strs = ['aabbcc', 'ababcc', 'aaccbb']) == 2
    assert candidate(strs = ['aabbcc', 'abacbc', 'abcabc', 'aabcbc', 'aacbbc']) == 4
    assert candidate(strs = ['aaa', 'aba', 'aaa', 'aca', 'aaa']) == 1
    assert candidate(strs = ['aa', 'bb', 'aa', 'bb', 'aa', 'bb', 'aa', 'bb', 'aa', 'bb']) == 2
    assert candidate(strs = ['aaaaa', 'aaabb', 'aabaa', 'aabab', 'aaced', 'aacef', 'aaceg', 'aaceh', 'aacei', 'aacej', 'aacek', 'aacei', 'aacej', 'aacek', 'aacei', 'aacej', 'aacek', 'aacei', 'aacej', 'aacek']) == 1
    assert candidate(strs = ['aaa', 'aab', 'aac', 'aad', 'aae', 'aaf', 'aag', 'aah', 'aai', 'aaj', 'aak', 'aal', 'aam', 'aan', 'aao', 'aap', 'aaq', 'aar', 'aas', 'aat', 'aau', 'aav', 'aaw', 'aax', 'aay', 'aaz']) == 0
    assert candidate(strs = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yzab']) == 0
    assert candidate(strs = ['abcdef', 'bcdefa', 'cdefab', 'defabc', 'efabcd', 'fabcde']) == 0
    assert candidate(strs = ['abcdef', 'uvwxyz', 'ghijkl']) == 6
    assert candidate(strs = ['aaaa', 'aaab', 'aaac', 'aaba', 'aabb', 'aabc', 'aaca', 'aacb', 'aacc', 'abaa', 'abab', 'abac', 'abba', 'abbb', 'abbc', 'abca', 'abcb', 'abcc', 'acaa', 'acab', 'acac', 'acba', 'acbb', 'acbc', 'acca', 'accb', 'accc', 'baaa', 'baab', 'baac', 'baba', 'babb', 'babc', 'baca', 'bacb', 'bacc', 'bbaa', 'bbab', 'bbac', 'bbba', 'bbbb', 'bbbc', 'bbca', 'bbcb', 'bbcc', 'bcaa', 'bcab', 'bcac', 'bcba', 'bcbb', 'bcbc', 'bccb', 'bccc', 'caaa', 'caab', 'caac', 'caba', 'cabb', 'cabc', 'caca', 'cacb', 'cacc', 'cbaa', 'cbab', 'cbac', 'cbba', 'cbbb', 'cbbc', 'cbca', 'cbcb', 'cbcc', 'ccaa', 'ccab', 'ccac', 'ccba', 'ccbb', 'ccbc', 'ccca', 'cccb', 'cccc']) == 0
    assert candidate(strs = ['mnop', 'mnop', 'mnop', 'mnop', 'mnop']) == 0
    assert candidate(strs = ['pqrs', 'psrq', 'qrst', 'rpsq', 'srqp', 'tqrs']) == 0
    assert candidate(strs = ['aabc', 'abac', 'abca', 'acba', 'acab', 'baca', 'bacb', 'baac', 'bcaa', 'cab', 'cbab', 'caba', 'cbba', 'cbaa']) == 3
    assert candidate(strs = ['lkjihg', 'kjihgf', 'jihgfe', 'ihgfed', 'hgfedc']) == 6
    assert candidate(strs = ['abcdef', 'bcdefa', 'cdefab']) == 0
    assert candidate(strs = ['qwe', 'qaz', 'qwr']) == 2
    assert candidate(strs = ['aaa', 'aab', 'aac', 'aad', 'baa', 'aba', 'aca', 'ada', 'baa', 'aba', 'aca', 'ada', 'baa', 'aba', 'aca', 'ada']) == 3
    assert candidate(strs = ['banana', 'bandana', 'bandanna', 'bandanna']) == 0
    assert candidate(strs = ['zzzz', 'zzyz', 'zzyy', 'zzyx', 'zzyw']) == 2
    assert candidate(strs = ['qwer', 'qweq', 'qwew', 'qwea', 'qwqa', 'qwaq', 'qwaq', 'qwaa', 'qaaa', 'qqaa', 'qqqa', 'qqqw', 'qqqq', 'qwqw', 'qwwq', 'qwqw', 'qqqw']) == 3
    assert candidate(strs = ['abcdefgh', 'hgfedcba', 'abcdefgh', 'hgfedcba']) == 8
    assert candidate(strs = ['aabcc', 'abcab', 'acaba', 'cacab', 'ccaba']) == 0
    assert candidate(strs = ['baab', 'baab', 'baab', 'baab', 'baab', 'baab', 'baab', 'baab', 'baab', 'baab', 'baab', 'baab', 'baab', 'baab', 'baab', 'baab', 'baab', 'baab', 'baab', 'baab']) == 0
    assert candidate(strs = ['abcd', 'abdc', 'acdb', 'adbc', 'aebc', 'afdc', 'agdb', 'ahbc']) == 0
    assert candidate(strs = ['abcdef', 'bcdegh', 'cdefij']) == 0
    assert candidate(strs = ['abcd', 'abce', 'abcf', 'abcd']) == 1
    assert candidate(strs = ['abcdefg', 'bcdefga', 'cdefgab']) == 0
    assert candidate(strs = ['abcd', 'abce', 'abcf', 'abcg']) == 0
    assert candidate(strs = ['xyz', 'xyw', 'xyv', 'xyu', 'xyt', 'xys', 'xyr', 'xqq', 'xpp', 'xoo', 'xnn', 'xmm', 'xll', 'xkk', 'xjj', 'xii', 'xhh', 'xgg', 'xff', 'xee', 'xed', 'xec', 'xeb', 'xea']) == 2
    assert candidate(strs = ['abcd', 'azxy', 'abcy']) == 2
    assert candidate(strs = ['abcd', 'bcde', 'cdef', 'defg', 'efgh']) == 0
    assert candidate(strs = ['hello', 'hellp', 'helpp', 'helpq']) == 0
    assert candidate(strs = ['qpwoeiruty', 'asdfghjklz', 'xcvbnm']) == 4
    assert candidate(strs = ['aabbcc', 'bbccdd', 'ccddeeff', 'ddeeffgg', 'eeffgghh', 'ffgghhii', 'gghhiijj', 'hhiijjkk', 'iijjkkll', 'jjkkllmm', 'kkllmmnn', 'llmmnnoo', 'mmnnoopq', 'nnoopqrs', 'oopqrstu', 'pqrstuvw', 'qrstuvwx', 'rstuvwxy', 'stuvwxyz']) == 0
    assert candidate(strs = ['aaaa', 'aaba', 'aabb', 'abaa', 'abab', 'abbb', 'baaa', 'baab', 'baba', 'babb', 'bbaa', 'bbab', 'bbbb']) == 0
    assert candidate(strs = ['abc', 'bca', 'cab', 'bac', 'acb', 'cba']) == 3
    assert candidate(strs = ['dog', 'cat', 'bat']) == 2
    assert candidate(strs = ['aaaa', 'abaa', 'acaa', 'aada', 'abca', 'abda', 'acba', 'acda', 'aaca', 'aada', 'aaca', 'aaba', 'abba', 'abca', 'acca', 'adca', 'aada', 'aaca', 'aaca', 'aaba']) == 2
    assert candidate(strs = ['zebra', 'zorro', 'zebra']) == 3
    assert candidate(strs = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee']) == 0
    assert candidate(strs = ['pqrs', 'qrst', 'rstu', 'stuv']) == 0
    assert candidate(strs = ['ghi', 'ghi', 'ghi']) == 0
    assert candidate(strs = ['leetcode', 'lintcode', 'testcode']) == 0
    assert candidate(strs = ['abcd', 'abdc', 'acbd']) == 0
    assert candidate(strs = ['abcd', 'bcad', 'cdab']) == 0
    assert candidate(strs = ['abcd', 'abdc', 'abcf']) == 2
    assert candidate(strs = ['hello', 'helps', 'helpp']) == 1
    assert candidate(strs = ['xga', 'xfb', 'yfa']) == 1
    assert candidate(strs = ['aab', 'aac', 'aba', 'aca', 'baa', 'bac', 'bba', 'bbc']) == 0
    assert candidate(strs = ['fed', 'efd', 'eef']) == 2
    assert candidate(strs = ['cba', 'bca', 'abc']) == 2
    assert candidate(strs = ['abc', 'def', 'ghi']) == 0
    assert candidate(strs = ['xyz', 'xyw', 'xyv']) == 1
    assert candidate(strs = ['cba', 'bac', 'bca']) == 3
    assert candidate(strs = ['hello', 'helps', 'heroes']) == 0
    assert candidate(strs = ['zzz', 'aaa', 'zzz']) == 3
    assert candidate(strs = ['zyx', 'wvu', 'tsr']) == 3
    assert candidate(strs = ['zzz', 'zyz', 'zxz']) == 1
    assert candidate(strs = ['aab', 'aac', 'abc']) == 0
    assert candidate(strs = ['abcd', 'dcba', 'abdc']) == 4
    assert candidate(strs = ['zzz', 'zyx', 'zyy']) == 2
    assert candidate(strs = ['zzzz', 'zzyy', 'zyzy', 'zyyz']) == 3
    assert candidate(strs = ['aab', 'aac', 'aba', 'aca']) == 0
    assert candidate(strs = ['dog', 'cat', 'bat']) == 2
    assert candidate(strs = ['abcd', 'abdc', 'acdb']) == 0
    assert candidate(strs = ['zyxw', 'zyxv', 'zyxu']) == 1
    assert candidate(strs = ['fed', 'efd', 'gfd']) == 1
    assert candidate(strs = ['a', 'a', 'a', 'a']) == 0
    assert candidate(strs = ['ghi', 'jkl', 'mno']) == 0
    assert candidate(strs = ['zzz', 'zyx', 'zyw']) == 2
    assert candidate(strs = ['abc', 'acd', 'aab']) == 2
    assert candidate(strs = ['zzzz', 'zzzz', 'zzzz']) == 0
    assert candidate(strs = ['zzzz', 'zzyz', 'zzyy', 'zzyx']) == 2
    assert candidate(strs = ['aaa', 'bbb', 'aaa']) == 3
    assert candidate(strs = ['c', 'b', 'a']) == 1
    assert candidate(strs = ['abcd', 'dcba', 'abcd']) == 4
    assert candidate(strs = ['e', 'd', 'c', 'b', 'a']) == 1
    assert candidate(strs = ['abcd', 'abcf', 'abcg']) == 0
    assert candidate(strs = ['zzz', 'zyz', 'zyx']) == 2
    assert candidate(strs = ['apple', 'apricot', 'banana']) == 0
    assert candidate(strs = ['aabbbabbb', 'bbbaabaab', 'aabbbbaab', 'abbbababa', 'bbaaabbbb', 'bbabaabab', 'abababbaa']) == 9
    assert candidate(strs = ['abcd', 'dcba', 'mnop']) == 0
    assert candidate(strs = ['fed', 'cab', 'dba']) == 3
    assert candidate(strs = ['abcd', 'abcf', 'abce']) == 1
    assert candidate(strs = ['cba', 'fed', 'ihg']) == 0
    assert candidate(strs = ['abcd', 'abdc', 'acbd', 'dacb']) == 0
    assert candidate(strs = ['zzz', 'zyz', 'yzz']) == 2
    assert candidate(strs = ['hello', 'helps', 'heaps']) == 1
    assert candidate(strs = ['zzz', 'zzz', 'zzz']) == 0
    assert candidate(strs = ['same', 'same', 'same']) == 0
    assert candidate(strs = ['abc', 'abc', 'abc']) == 0
    assert candidate(strs = ['xyp', 'ypp', 'xyp']) == 2
    assert candidate(strs = ['aab', 'aac', 'aab']) == 1
    assert candidate(strs = ['zz', 'zy', 'zx']) == 1
    assert candidate(strs = ['az', 'za', 'zz', 'aa']) == 2
    assert candidate(strs = ['abcd', 'acbd', 'dabc', 'dbca']) == 0
    assert candidate(strs = ['aaa', 'aab', 'aac']) == 0
    assert candidate(strs = ['cba', 'cab', 'bac']) == 2
    assert candidate(strs = ['hello', 'hilll', 'hillo']) == 0
    assert candidate(strs = ['rrjk', 'furt', 'guzm']) == 1
    assert candidate(strs = ['fed', 'dbc', 'cba']) == 3
    assert candidate(strs = ['a', 'b', 'c', 'd', 'e']) == 0
    assert candidate(strs = ['hello', 'helps', 'hero']) == 0
    assert candidate(strs = ['abc', 'acd', 'aec']) == 0
    assert candidate(strs = ['ghi', 'def', 'abc']) == 3
    assert candidate(strs = ['fedcba', 'fedcba', 'fedcba']) == 0
    assert candidate(strs = ['azx', 'byy', 'czz']) == 0
    assert candidate(strs = ['xc', 'yb', 'za']) == 0
    assert candidate(strs = ['abcd', 'abcc', 'abcb', 'abca']) == 1
    assert candidate(strs = ['xzxbxyzz', 'xzyxzzzx', 'xzyxzzyz', 'zyzzzxzx']) == 1
    assert candidate(strs = ['ca', 'bb', 'ac']) == 1
    assert candidate(strs = ['fed', 'efd', 'efd']) == 1
    assert candidate(strs = ['axb', 'ayb', 'azb']) == 0
    assert candidate(strs = ['pqrs', 'qrst', 'rstu']) == 0
    assert candidate(strs = ['hello', 'helli', 'hellp']) == 1
    assert candidate(strs = ['abc', 'acd', 'aab']) == 2
    assert candidate(strs = ['a', 'b', 'c']) == 0
