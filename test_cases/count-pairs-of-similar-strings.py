# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(words = ['aabbcc', 'abc', 'ab', 'a', 'b', 'c']) == 1
    assert candidate(words = ['aaa', 'bbb', 'ccc', 'aab', 'aba', 'baa']) == 3
    assert candidate(words = ['aabbcc', 'abc', 'aabb', 'aaabbbcc', 'abcabc']) == 6
    assert candidate(words = ['a', 'b', 'c', 'd', 'e']) == 0
    assert candidate(words = ['aaa', 'bbb', 'ccc', 'abc', 'abc']) == 1
    assert candidate(words = ['abcd', 'bcad', 'cabd', 'dabc']) == 6
    assert candidate(words = ['nba', 'cba', 'dba']) == 0
    assert candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']) == 15
    assert candidate(words = ['abcd', 'dcba', 'abdc', 'badc']) == 6
    assert candidate(words = ['aabb', 'ab', 'ba']) == 3
    assert candidate(words = ['abc', 'def', 'ghi', 'jkl']) == 0
    assert candidate(words = ['aa', 'bb', 'cc', 'abc', 'cba', 'bca']) == 3
    assert candidate(words = ['a', 'b', 'c', 'd']) == 0
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == 0
    assert candidate(words = ['abc', 'abc', 'abc', 'abc']) == 6
    assert candidate(words = ['abcd', 'dcba', 'abcd', 'dcba', 'abcd']) == 10
    assert candidate(words = ['aaa', 'bbb', 'ccc', 'aaa']) == 1
    assert candidate(words = ['abc', 'def', 'ghi']) == 0
    assert candidate(words = ['aba', 'aabb', 'abcd', 'bac', 'aabc']) == 2
    assert candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno']) == 0
    assert candidate(words = ['ab', 'ba', 'ab', 'ba', 'ab', 'ba']) == 15
    assert candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'aabbcc', 'bbaacc', 'ccbaab', 'aabbbc']) == 45
    assert candidate(words = ['abcde', 'edcba', 'abc', 'bca', 'cab', 'deabc']) == 6
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba']) == 6
    assert candidate(words = ['aabbcc', 'abcabc', 'bcaabc', 'cababc', 'bcabac']) == 10
    assert candidate(words = ['aabbccddeeff', 'ffeeddccbbaa', 'abcdef', 'fedcba', 'efabcd', 'fedcba', 'abcdefg', 'gfedcba', 'hijklm', 'mlkjih']) == 17
    assert candidate(words = ['aabbcc', 'bbaacc', 'ccaabb', 'aabbc', 'bbaac', 'ccaab', 'aaabb', 'aabbb', 'abbbb', 'bbbbb']) == 18
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == 0
    assert candidate(words = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'ffff', 'gggg', 'hhhh', 'iiii', 'jjjj']) == 0
    assert candidate(words = ['abcdefg', 'gfedcba', 'ghijklm', 'mlkjihg', 'nopqrst', 'tsrqpon', 'vwxyz', 'zyxwv', 'abcdabcd', 'efghijkl', 'mnopqrstuvw', 'xyzzyxwv', 'utsrqponmlkjihgfedcba']) == 6
    assert candidate(words = ['hello', 'olleh', 'world', 'dlrow', 'python', 'nohtyp', 'java', 'avaj', 'algorithm', 'mhtirogla', 'data', 'tatad', 'structure', 'erutcurts', 'example', 'elpmaxe', 'test', 'tset', 'code', 'edoc', 'challenge', 'egnellahc', 'interview', 'weivretni']) == 12
    assert candidate(words = ['xyzxyzxyz', 'zyxzyxzyx', 'yzxyzxyz', 'zyxyzxyz', 'xzyzxzyx', 'xyzzyxzyx', 'zyxzyxzyx', 'xyzzyxzyx', 'xzyzxzyx', 'xyzxyzxyz']) == 45
    assert candidate(words = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee', 'aaaaa', 'bbbbb']) == 2
    assert candidate(words = ['abcd', 'abce', 'abcf', 'abdg', 'abdh', 'abei', 'abdj', 'abcd', 'abcd']) == 3
    assert candidate(words = ['aabbcc', 'abc', 'ab', 'a', 'b', 'c', 'abcde', 'edcba', 'fghij', 'jihgf', 'mnopq', 'qpomn']) == 4
    assert candidate(words = ['abcd', 'dcba', 'cdab', 'bacd', 'cabd', 'abcd', 'acdb', 'bdac', 'bcda', 'dabc', 'adcb', 'cdba', 'bacd', 'abcd', 'bcad']) == 105
    assert candidate(words = ['abcd', 'dcba', 'abcd', 'dcba', 'abcd', 'abcd', 'abcd', 'dcba', 'dcba', 'abcd']) == 45
    assert candidate(words = ['xyz', 'zyx', 'abc', 'cab', 'bac', 'xyz', 'zyx']) == 9
    assert candidate(words = ['aaaa', 'aabb', 'abab', 'abba', 'baba', 'bbaa', 'baab', 'abab', 'aabb', 'abba']) == 36
    assert candidate(words = ['abc', 'bca', 'cab', 'xyz', 'zyx', 'yzx']) == 6
    assert candidate(words = ['ab', 'ba', 'ac', 'ca', 'ad', 'da', 'bc', 'cb', 'bd', 'db', 'cd', 'dc']) == 6
    assert candidate(words = ['abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']) == 0
    assert candidate(words = ['xyz', 'zyx', 'yzx', 'xzy', 'yxz', 'zxy', 'xyzz', 'yzzx', 'zzxy', 'zzzx', 'zxzy', 'xzyz']) == 55
    assert candidate(words = ['unique', 'ueinque', 'qneuie', 'neiqueu', 'ienquue', 'enuiqueu', 'qieuenu', 'euniqeu', 'ueinqeu', 'neuiqeu', 'uieqneu', 'niuqueeu', 'eiunqueu', 'iuqeenu', 'qieuenu', 'euniqeu', 'ueinqeu', 'neuiqeu', 'uieqneu', 'niuqueeu', 'eiunqueu', 'iuqeenu', 'qieuenu', 'euniqeu', 'ueinqeu', 'neuiqeu', 'uieqneu', 'niuqueeu', 'eiunqueu', 'iuqeenu', 'qieuenu', 'euniqeu', 'ueinqeu', 'neuiqeu', 'uieqneu', 'niuqueeu', 'eiunqueu', 'iuqeenu', 'qieuenu', 'euniqeu', 'ueinqeu', 'neuiqeu', 'uieqneu', 'niuqueeu', 'eiunqueu', 'iuqeenu', 'qieuenu', 'euniqeu', 'ueinqeu', 'neuiqeu', 'uieqneu', 'niuqueeu', 'eiunqueu', 'iuqeenu']) == 1431
    assert candidate(words = ['aaa', 'aa', 'a', 'b', 'bb', 'bbb', 'bbbb', 'bbbbb']) == 13
    assert candidate(words = ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']) == 276
    assert candidate(words = ['pqrst', 'rstqp', 'qrstp', 'srtpq', 'tsrqp', 'tspqr', 'pqrst', 'rstqp', 'qrstp', 'srtpq', 'tsrqp', 'tspqr']) == 66
    assert candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'abc', 'acb', 'bac', 'bca']) == 45
    assert candidate(words = ['abc', 'abd', 'abe', 'abf', 'abg', 'abh', 'abi', 'abj', 'abk', 'abl', 'abm', 'abn', 'abo', 'abp', 'abq', 'abr', 'abs', 'abt', 'abu', 'abv', 'abw', 'abx', 'aby', 'abz']) == 0
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba']) == 15
    assert candidate(words = ['xyz', 'zyx', 'zyx', 'xyz', 'yxxz', 'zyxz', 'xzyz', 'yxzz', 'zxzy', 'zyzz', 'zzzy', 'zyyz', 'zyzx', 'xzyz', 'zzyx', 'zyxz', 'zyzx', 'zyxz', 'zyzx', 'zyxz', 'zyzx', 'zyzx', 'zyzx', 'zyzx', 'zyzx', 'zyzx', 'zyzx', 'zyzx', 'zyzx', 'zyzx', 'zyzx', 'zyzx', 'zyzx', 'zyzx', 'zyzx', 'zyzx', 'zyzx', 'zyzx', 'zyzx', 'zyzx', 'zyzx', 'zyzx']) == 744
    assert candidate(words = ['abcdefg', 'gfedcba', 'hijklmn', 'nmkljih', 'opqrstu', 'utsrqpo', 'vwxyz', 'zyxwv', 'abcdefg', 'gfedcba', 'hijklmn', 'nmkljih', 'opqrstu', 'utsrqpo', 'vwxyz', 'zyxwv']) == 24
    assert candidate(words = ['abc', 'bca', 'cab', 'xyz', 'zyx', 'yxz']) == 6
    assert candidate(words = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'ffff', 'gggg', 'hhhh', 'iiii', 'jjjj', 'kkkk', 'llll', 'mmmm', 'nnnn', 'oooo', 'pppp', 'qqqq', 'rrrr', 'ssss', 'tttt', 'uuuu', 'vvvv', 'wwww', 'xxxx', 'yyyy', 'zzzz', 'aaab', 'bbba', 'ccca', 'ddda', 'eeea', 'fffa', 'ggga', 'hhha', 'iiia', 'jjja', 'kkka', 'llla', 'mmma', 'nnna', 'oooo', 'pppa', 'qqqa', 'rrra', 'sssa', 'ttta', 'uuua', 'vvva', 'wwwa', 'xxxa', 'yyya', 'zzza', 'aab', 'bba', 'cca', 'dda', 'eea', 'ffa', 'gga', 'hha', 'iaa', 'jaa', 'kaa', 'laa', 'maa', 'naa', 'oaa', 'paa', 'qaa', 'raa', 'saa', 'taa', 'uaa', 'vaa', 'waa', 'xaa', 'yaa', 'zaa', 'aabbb', 'bbbaa', 'cccaa', 'dddaa', 'eeeea', 'ffffa', 'gggga', 'hhhaa', 'iiiia', 'jjjaa', 'kkkaa', 'lllaa', 'mmmia', 'nnnaa', 'ooooo', 'pppaa', 'qqqaa', 'rrraa', 'ssaaa', 'tttaa', 'uuuaa', 'vvvaa', 'wwwaa', 'xxxaa', 'yyaaa', 'zzzaa']) == 85
    assert candidate(words = ['abacabadabacaba', 'bacbacbacbacbac', 'cabacabacabacab', 'abcabcabcabcabc', 'bcbcbcbcbcbcb', 'cbcbcbcbcbcbc']) == 4
    assert candidate(words = ['aaa', 'bbb', 'ccc', 'abc', 'bca', 'cab', 'abc', 'bca', 'cab']) == 15
    assert candidate(words = ['aaaa', 'aaab', 'aaba', 'abaa', 'baaa', 'bbaa', 'bbba', 'bbbb']) == 15
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'mnopqrstuvwxyzabcdefghijkl']) == 3
    assert candidate(words = ['abcd', 'abce', 'abcf', 'abdg', 'abdh', 'abdi', 'abdj', 'abcd']) == 1
    assert candidate(words = ['aabbcc', 'abcabc', 'bcaabc', 'cababc', 'aabbcc', 'bbaacc', 'ccbaab']) == 21
    assert candidate(words = ['xyz', 'zyx', 'yxz', 'zxy', 'xzy', 'yzx']) == 15
    assert candidate(words = ['xyz', 'zyx', 'yxz', 'xzy', 'yzx', 'zxy', 'abc', 'bca', 'cab', 'aaa', 'bbb', 'ccc', 'aba', 'bab', 'aab', 'abb', 'baa', 'bba', 'abb', 'aab', 'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']) == 55
    assert candidate(words = ['xyz', 'zyx', 'yzx', 'xzy', 'yxz', 'zxy', 'zyxw', 'wxyz']) == 16
    assert candidate(words = ['mnop', 'mnopqr', 'mnopqrs', 'mnopqrst', 'mnopqrstuv', 'mnopqrstuvw', 'mnopqrstuvwx', 'mnopqrstuvwxy', 'mnopqrstuvwxyz']) == 0
    assert candidate(words = ['abcabc', 'bcabc', 'cabc', 'abc', 'bca', 'cab', 'aabbcc', 'bbccaa', 'ccaabb']) == 36
    assert candidate(words = ['abcde', 'edcba', 'bcdea', 'deabc', 'cdeab']) == 10
    assert candidate(words = ['abcdef', 'fedcba', 'ghijkl', 'lkjhgf', 'mnopqr', 'rqponm', 'stuvwx', 'xwvuts', 'yz', 'zy']) == 4
    assert candidate(words = ['pqr', 'qrp', 'prq', 'rpq', 'rqp', 'pqr', 'abc', 'cab', 'bac', 'abcde', 'edcba', 'fghij', 'jihgf', 'mnopq', 'qpomn']) == 21
    assert candidate(words = ['abc', 'abcd', 'abce', 'abcf', 'abcg', 'abch', 'abci', 'abcj', 'abck', 'abcl', 'abcm', 'abcn', 'abco', 'abcp', 'abcq', 'abcr', 'abcs', 'abct', 'abcu', 'abcv', 'abcw', 'abcx', 'abcy', 'abcz']) == 0
    assert candidate(words = ['ab', 'ba', 'ac', 'ca', 'ad', 'da', 'bc', 'cb', 'bd', 'db', 'cd', 'dc', 'abcd', 'dcba', 'cdab', 'bacd', 'cabd', 'acbd', 'cadb', 'abcd', 'dcba', 'cdab', 'bacd', 'cabd', 'acbd', 'cadb']) == 97
    assert candidate(words = ['abcabcabc', 'bcbcbcbc', 'cacacac', 'abababab', 'babababa', 'acacacac', 'abcabcabc', 'bcbcbcbc', 'cacacac', 'abababab']) == 8
    assert candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'zyx']) == 0
    assert candidate(words = ['abcdabcdabcdabcdabcdabcdabcdabcd', 'bcadbcadbcadbcadbcadbcadbcadbcad', 'cdabcdabcdabcdabcdabcdabcdabcdabc', 'dcbadcbadcbadcbadcbadcbadcbadcba', 'abcdabcdabcdabcdabcdabcdabcdabcde']) == 6
    assert candidate(words = ['apple', 'pale', 'pplea', 'elppa', 'ppale', 'pleap']) == 15
    assert candidate(words = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'ffff', 'gggg', 'hhhh', 'iiii', 'jjjj']) == 0
    assert candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'abc', 'acb', 'bac', 'bca', 'cab', 'cba']) == 276
    assert candidate(words = ['mnopqr', 'nopqrm', 'opqrmn', 'pqrmno', 'qrmnop', 'rmnopq', 'mnopqr', 'nopqrm', 'opqrmn', 'pqrmno', 'qrmnop', 'rmnopq', 'mnopqr', 'nopqrm', 'opqrmn', 'pqrmno', 'qrmnop', 'rmnopq']) == 153
    assert candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']) == 0
    assert candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'uvw', 'rst', 'qpo', 'nml', 'kji', 'fed', 'cba', 'zyx', 'wvu', 'tsr', 'pon', 'mlk', 'jih', 'gf', 'de', 'abc']) == 6
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == 0
    assert candidate(words = ['aaa', 'bbb', 'ccc', 'abc', 'bca', 'cab', 'aab', 'aba', 'baa', 'bbc', 'bcb', 'cbb', 'acc', 'cac', 'cca']) == 12
    assert candidate(words = ['abcdef', 'fedcba', 'bcdefa', 'defabc', 'efabcd', 'fabcde', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'uvw', 'rst', 'qpo', 'nml', 'kji', 'fed', 'cba', 'zyx', 'wvu', 'tsr', 'pon', 'mlk', 'jih', 'gf', 'de', 'abc']) == 21
    assert candidate(words = ['abcde', 'edcba', 'fghij', 'jihgf', 'abcde', 'edcba']) == 7
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz']) == 45
    assert candidate(words = ['aabbcc', 'abcabc', 'ababab', 'acacac', 'bcbcbc', 'bacbac', 'cabcab', 'abcabcabc', 'xyzxyzxyz', 'zyxzyxzyx']) == 11
    assert candidate(words = ['abcdefg', 'gfedcba', 'fedcbag', 'bagfedc', 'abcdefg', 'gfedcba', 'fedcbag', 'bagfedc', 'abcdefg', 'gfedcba']) == 45
    assert candidate(words = ['abcdefghij', 'jihgfedcba', 'abcdefghij', 'jihgfedcba', 'abcdefghij', 'jihgfedcba']) == 15
    assert candidate(words = ['abcdef', 'fedcba', 'defabc', 'cabfed', 'bcadef', 'fedcba', 'abcdef', 'abcdef']) == 28
    assert candidate(words = ['abcde', 'edcba', 'cdeab', 'decba', 'bacde', 'ecbad', 'abcd', 'dcba', 'abc', 'bca', 'cab', 'acb', 'bac', 'cba', 'a', 'b', 'c', 'd', 'e']) == 31
    assert candidate(words = ['aabbcc', 'aabbc', 'aabc', 'abc', 'ab', 'a', 'b', 'bb', 'bbb', 'bbbb', 'bbbbb', 'bbbbb', 'bbbb', 'bbb', 'bb', 'b']) == 51
    assert candidate(words = ['same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same']) == 3403
    assert candidate(words = ['ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al', 'am', 'an', 'ao', 'ap', 'aq', 'ar', 'as', 'at', 'au', 'av', 'aw', 'ax', 'ay', 'az']) == 0
    assert candidate(words = ['xyz', 'yzx', 'zxy', 'zyx', 'yxz', 'xzy', 'abc', 'cab', 'bca']) == 18
    assert candidate(words = ['abc', 'abcabc', 'abcabcabc', 'abcabcabcabc', 'abcabcabcabcabc', 'abcabcabcabcabcabc', 'abcabcabcabcabcabcabc', 'abcabcabcabcabcabcabcabc']) == 28
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == 26
    assert candidate(words = ['test', 'sett', 'stet', 'tset', 'ttes', 'etts', 'etst', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste', 'stte', 'ttse', 'tste']) == 3828
    assert candidate(words = ['ab', 'ba', 'ac', 'ca', 'ad', 'da', 'bc', 'cb', 'bd', 'db', 'cd', 'dc', 'abcd', 'dcba', 'cdab', 'bacd', 'cabd', 'abcd', 'abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'ab', 'ba', 'ac', 'ca', 'ad', 'da', 'bc', 'cb', 'bd', 'db', 'cd', 'dc', 'abcd', 'dcba', 'cdab', 'bacd', 'cabd', 'abcd']) == 117
    assert candidate(words = ['aaaa', 'aaab', 'aaba', 'aabb', 'abaa', 'abab', 'abba', 'abbb', 'baaa', 'baab', 'baba', 'babb', 'bbaa', 'bbab', 'bbba', 'bbbb']) == 91
    assert candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'aabbcc', 'ddeeff', 'gghhiijj', 'kkllmm', 'nnoopp', 'qqrrss', 'ttuuvv', 'wwxxyy', 'zz', 'aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj', 'kkk', 'lll', 'mmm', 'nnn', 'ooo', 'ppp', 'qqq', 'rrr', 'sss', 'ttt', 'uuu', 'vvv', 'www', 'xxx', 'yyy', 'zzz']) == 3
    assert candidate(words = ['aabbcc', 'bbaacc', 'ccbbaa', 'aabbcc', 'bbaacc', 'ccbbaa', 'aabbbc', 'bbaacc', 'ccbbaa', 'aabbbc', 'bbaacc', 'ccbbaa']) == 66
    assert candidate(words = ['hello', 'olleh', 'ohell', 'loleh', 'ehlol', 'llohe', 'world', 'dlrow', 'owrld', 'rldwo', 'ldwor', 'dworld', 'wolrd', 'orldw', 'lrwod', 'rwdol', 'dlorw', 'lorwd', 'rowdl', 'owrld', 'dlrow', 'world', 'dlrow', 'owrld', 'rldwo', 'ldwor', 'dworld', 'wolrd', 'orldw', 'lrwod', 'rwdol', 'dlorw', 'lorwd', 'rowdl', 'owrld', 'dlrow', 'world', 'dlrow', 'owrld', 'rldwo', 'ldwor', 'dworld', 'wolrd', 'orldw', 'lrwod', 'rwdol', 'dlorw', 'lorwd', 'rowdl', 'owrld']) == 961
