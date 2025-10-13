# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(words = ['abac', 'deed', 'civic', 'rotor']) == 3
    assert candidate(words = ['aabbcc', 'ddeeff', 'gghhiijj', 'kklmmoopp']) == 4
    assert candidate(words = ['aa', 'bb', 'cc', 'dd', 'ee']) == 5
    assert candidate(words = ['noon', 'level', 'deified', 'civic', 'rotor']) == 5
    assert candidate(words = ['aaaa', 'bbbb', 'cccc']) == 3
    assert candidate(words = ['abac', 'decd', 'efef', 'ghgh']) == 3
    assert candidate(words = ['abcde', 'fghij', 'klmno']) == 0
    assert candidate(words = ['a', 'b', 'c', 'd', 'e']) == 5
    assert candidate(words = ['abbb', 'ba', 'aa']) == 3
    assert candidate(words = ['race', 'car', 'level']) == 3
    assert candidate(words = ['race', 'car', 'level', 'deified']) == 4
    assert candidate(words = ['abc', 'ab']) == 2
    assert candidate(words = ['aaa', 'bbb', 'ccc', 'ddd']) == 4
    assert candidate(words = ['hello', 'world', 'python', 'programming', 'code']) == 4
    assert candidate(words = ['abac', 'deed', 'racecar', 'refer', 'madam']) == 4
    assert candidate(words = ['abcde', 'fghij', 'klmno', 'pqrst']) == 0
    assert candidate(words = ['noon', 'civic', 'rotor', 'stats']) == 4
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == 10
    assert candidate(words = ['deified', 'civic', 'rotor', 'redder']) == 4
    assert candidate(words = ['hello', 'world', 'python', 'programming']) == 3
    assert candidate(words = ['noon', 'civic', 'rotor', 'refer']) == 4
    assert candidate(words = ['aabbcc', 'bbaacc', 'ccabba', 'aabbbc', 'bbcaac']) == 4
    assert candidate(words = ['xyz', 'zyx', 'abc', 'cba', 'aaa', 'bbb']) == 6
    assert candidate(words = ['abcd', 'dcba', 'efgh', 'hgf', 'i', 'jklm', 'mlkj']) == 7
    assert candidate(words = ['ab', 'cd', 'ef', 'gh', 'ij']) == 0
    assert candidate(words = ['cd', 'ef', 'a']) == 1
    assert candidate(words = ['xxyyzz', 'yzyzyz', 'xzyzxz', 'zyzxzy', 'zzzyyy', 'yyzzzy', 'zzzzyy', 'xxxyyy', 'yyxxzz', 'zzxyyx']) == 9
    assert candidate(words = ['aabbccddeeff', 'abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yz', 'abcdefgh', 'ijklmnop', 'qrstuv', 'wxyz']) == 10
    assert candidate(words = ['xyz', 'zyx', 'yzx', 'zxy', 'yxz', 'xzy', 'abc', 'cba', 'bac', 'bca', 'cab', 'acb']) == 12
    assert candidate(words = ['abcdefghijk', 'zyxwvutsrqp', 'mnopqrstuvw', 'abcdefghij', 'zyxwvutsr', 'mnopqrstu', 'abcdefgh', 'zyxwvuts', 'mnopqrs', 'abcdefg', 'zyxwvut', 'mnopqr', 'abcdef', 'zyxwvu', 'mnopq', 'abcde', 'zyxwv', 'mnop', 'abcd', 'zyxw', 'mno', 'abc', 'zyx', 'mn', 'ab', 'zy', 'm', 'a', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b']) == 52
    assert candidate(words = ['racecar', 'madam', 'refer', 'level', 'deified', 'rotor', 'reviled', 'deed', 'civic', 'rotor', 'redder', 'repaper', 'rotor', 'deed', 'civic', 'level']) == 16
    assert candidate(words = ['noon', 'civic', 'rotor', 'stats', 'level', 'deified', 'reviled', 'refer', 'abcba', 'babcb', 'ababa', 'abacaba']) == 12
    assert candidate(words = ['aabbaa', 'bbaabb', 'ababab', 'bababa', 'aabbba', 'bbaabb', 'ababab', 'bababa', 'aabbaa', 'bbaabb']) == 9
    assert candidate(words = ['abcdefghij', 'jihgfedcba', 'abcdefgh', 'hgfedcba', 'abcdef', 'fedcba', 'abc', 'cba', 'ab', 'ba', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == 20
    assert candidate(words = ['aabbcc', 'ddeeff', 'gghhii', 'jklmno', 'pqrsut', 'vwxyzv']) == 3
    assert candidate(words = ['abacaxa', 'banana', 'civic', 'rotor', 'stats', 'level']) == 6
    assert candidate(words = ['abcdefgh', 'hgfedcba', 'abcdefg', 'gfedcba', 'abcde', 'edcba', 'abcd', 'dcba', 'abc', 'cba', 'ab', 'ba', 'a', 'b']) == 14
    assert candidate(words = ['aaabbbccc', 'dddeeefff', 'ggghhhiii', 'jjjkkklll', 'mmmnnnooo', 'pppqqqrrr', 'ssstttuuu', 'vvvwwwxxx', 'yyyzzzwww', 'xxxyyyzzz']) == 8
    assert candidate(words = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj', 'kkk', 'lll', 'mmm', 'nnn', 'ooo', 'ppp', 'qqq', 'rrr', 'sss', 'ttt', 'uuu', 'vvv', 'www', 'xxx', 'yyy', 'zzz']) == 26
    assert candidate(words = ['aabbcc', 'bbaacc', 'cabbac', 'abcabc', 'acbacb', 'bababc']) == 5
    assert candidate(words = ['abcdefg', 'hijklmn', 'opqrstu', 'vwxyz', 'abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'mnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'mnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba']) == 11
    assert candidate(words = ['abcabcabc', 'bcabcabc', 'cabcabcab', 'abcabcbca', 'bcabcabcb', 'cabcabcbc', 'abcabcabc', 'bcabcabc', 'cabcabcab', 'abcabcbca', 'bcabcabcb', 'cabcabcbc', 'abcabcabc', 'bcabcabc', 'cabcabcab', 'abcabcbca', 'bcabcabcb', 'cabcabcbc']) == 18
    assert candidate(words = ['aabbcc', 'abcabc', 'defdef', 'xyzxyz', 'mnopqr', 'qrstuv']) == 4
    assert candidate(words = ['abcdabcd', 'efefef', 'ghighi', 'jkjkjk', 'lmnmln', 'opopop', 'qrstqr', 'stuvst', 'wxyxw', 'zyzzyz']) == 8
    assert candidate(words = ['racecar', 'madam', 'level', 'refer', 'deed']) == 5
    assert candidate(words = ['racecar', 'madam', 'refer', 'deed', 'level', 'noon', 'civic', 'rotor', 'stats', 'reviled', 'repaid', 'drawer', 'civic', 'rotor', 'redder', 'deed', 'peep', 'noon', 'kayak', 'reviled', 'repaid', 'civic', 'rotor', 'redder', 'deed', 'peep', 'noon', 'kayak', 'madam', 'refer', 'deed', 'level', 'noon', 'civic', 'rotor', 'stats']) == 36
    assert candidate(words = ['aabbcc', 'abcabc', 'bbaacc', 'ccbb', 'aabb', 'abc', 'aab', 'aaa', 'bbb', 'ccc']) == 10
    assert candidate(words = ['abcd', 'dcba', 'efgh', 'hgfe', 'ijkl', 'lkji', 'mnop', 'ponm']) == 8
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'mnopqrstuvwxyzabcdefghijkl', 'abcdefghijlmnopqrstuvwxyz', 'qrstuvwxyzabcdefghij', 'klmnopqrstuvwxyzabcdefghi', 'jklmnopqrstuvwxyzabcdefgh', 'ijklmnopqrstuvwxyzabcdefg', 'hijklmnopqrstuvwxyzabcdef', 'ghijklmnopqrstuvwxyzabcde', 'fghijklmnopqrstuvwxyzabcd', 'efghijklmnopqrstuvwxyzabc', 'defghijklmnopqrstuvwxyzab', 'cdefghijklmnopqrstuvwxyza', 'bcdefghijklmnopqrstuvwxyzab', 'abcdefghijklmnopqrstuvwxyz']) == 15
    assert candidate(words = ['aabb', 'bbaa', 'ccdd', 'ddcc', 'eeff', 'ffee', 'gghh', 'higg', 'iijj', 'jjii', 'kkll', 'llkk', 'mmnn', 'nnaa', 'aabb', 'bbcc', 'ccdd', 'ddeeff', 'ffgghh', 'hhiijj', 'kkeeff', 'gghh', 'iijj', 'aabb', 'bbcc', 'ccdd', 'ddeeff', 'ffgghh', 'hhiijj', 'kkeeff', 'gghh', 'iijj', 'aabb', 'bbcc', 'ccdd', 'ddeeff', 'ffgghh', 'hhiijj', 'kkeeff', 'gghh', 'iijj', 'aabb', 'bbcc', 'ccdd', 'ddeeff', 'ffgghh', 'hhiijj', 'kkeeff', 'gghh', 'iijj', 'aabb', 'bbcc', 'ccdd', 'ddeeff', 'ffgghh', 'hhiijj', 'kkeeff']) == 56
    assert candidate(words = ['aabbaa', 'bbccbb', 'cccddd', 'ddeecc', 'effe', 'ggh', 'hi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'z']) == 19
    assert candidate(words = ['aaaaaaaaab', 'bbbbbbbbbb', 'cccccccccc', 'dddddddddd', 'eeeeeeeee', 'fffffffff', 'gggggggg', 'hhhhhhh', 'iiiiii', 'jjjjj', 'kkkk', 'lll', 'mm', 'n', 'o']) == 14
    assert candidate(words = ['aaabbbccc', 'bbbaaaccc', 'cccbbbaaa', 'aabbcc', 'bbaacc', 'ccaabb', 'aabbbc', 'bbcaac', 'ccaabb', 'abcabc', 'ababab', 'bababa', 'aaaaaa', 'bbbbbb', 'cccccc', 'dddddd']) == 16
    assert candidate(words = ['aaaaaa', 'bbbbbb', 'cccccc', 'dddddd', 'eeeeee', 'ffffff', 'gggggg', 'hhhhhh', 'iiiiii', 'jjjjjj', 'kkkkkk', 'llllll', 'mmmmmm', 'nnnnnn', 'oooooo', 'pppppp', 'qqqqqq', 'rrrrrr', 'ssssss', 'tttttt', 'uuuuuu', 'vvvvvv', 'wwwwww', 'xxxxxx', 'yyyyyy', 'zzzzzz']) == 26
    assert candidate(words = ['aabbaa', 'bbaaab', 'ababab', 'bababa', 'aabbba', 'baaabb', 'aababb', 'abbaab', 'ababba', 'babaab', 'abbaba', 'babbaa', 'baabba', 'aababb', 'abbaab']) == 15
    assert candidate(words = ['racecar', 'level', 'deified', 'civic', 'rotor', 'stats', 'refer', 'rotor', 'reviled', 'deed', 'peep', 'noon', 'racecar', 'refer', 'civic', 'level']) == 16
    assert candidate(words = ['abcba', 'babcb', 'ababa', 'abacaba', 'racecar', 'madam']) == 6
    assert candidate(words = ['aaaaaaaaaa', 'bbbbbbbbbb', 'cccccccccc', 'dddddddddd', 'eeeeeeeeee', 'ffffffffff', 'gggggggggg', 'hhhhhhhhhh', 'iiiiiiiiii', 'jjjjjjjjjj']) == 10
    assert candidate(words = ['aab', 'aac', 'abb', 'abc', 'aba', 'aca', 'aaa', 'bbb', 'aab', 'aac', 'aba', 'aca', 'aaa', 'bbb']) == 14
    assert candidate(words = ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzabcd', 'efghij', 'klmnop', 'qrstuv', 'wxyzab', 'cdefgh']) == 8
    assert candidate(words = ['zzzz', 'yyyy', 'xxxx', 'wwww', 'vvvv', 'uuuu', 'tttt', 'ssss', 'rrrr', 'qqqq', 'pppp', 'oooo', 'nnnn', 'mmmm', 'llll', 'kkkk', 'jjjj', 'iiii', 'hhhh', 'gggg', 'ffffff']) == 21
    assert candidate(words = ['abcde', 'edcba', 'fedcb', 'bcdef', 'cdefg', 'bcdea', 'gfedc', 'abcdf', 'bcadf', 'bcade', 'bcdefg', 'bcdefgh', 'bcdefghi', 'bcdefghij', 'bcdefghijk']) == 15
    assert candidate(words = ['abcd', 'dcba', 'efgh', 'hgf', 'ijkl', 'lkj', 'mnop', 'ponm', 'qrst', 'tsrq', 'uvw', 'wvu', 'xyz', 'zyx', 'abcd', 'dcba', 'efgh', 'hgf', 'ijkl', 'lkj', 'mnop', 'ponm', 'qrst', 'tsrq', 'uvw', 'wvu', 'xyz', 'zyx']) == 28
    assert candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'abcdefgh', 'hgfedcba', 'ijklmnop', 'ponmlkji', 'qrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba']) == 31
    assert candidate(words = ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzabcd', 'efghij', 'klmnop', 'qrstuv', 'wxyzab']) == 8
    assert candidate(words = ['abacax', 'bxdxcy', 'cydxdz', 'zxdxzy', 'yxzxyw', 'wxwxyv', 'vwxyvu', 'uvwxut', 'tuvwus', 'suvwtv', 'rvtwus', 'qtwvur', 'ptwvus', 'otwvur', 'ntwvus', 'mtwvur', 'ltwvus', 'kwtvur', 'jwtvus', 'itwvur', 'htwvur', 'gtwvur', 'ftwvur', 'etwvur', 'dtwvur', 'ctwvur', 'btwvur', 'atwvur']) == 24
    assert candidate(words = ['racecar', 'level', 'deified', 'rotor', 'redder', 'repaper', 'reviled', 'kayak']) == 7
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == 52
    assert candidate(words = ['abcdefg', 'ghijklm', 'nopqrstu', 'vwxyzabc', 'defghijk', 'lmnopqrs', 'tuvwxyz', 'abcdefghi', 'jklmnopqr', 'stuvwxyzabc']) == 8
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 52
    assert candidate(words = ['abacax', 'banana', 'anana', 'civic', 'racecar', 'madam', 'level', 'deified']) == 8
    assert candidate(words = ['abababab', 'babababa', 'acacacac', 'bacbacba', 'cdcddcdc', 'dddddddd', 'eeeeeeee', 'ffffffff', 'gggggggg', 'hhhhhhhh']) == 9
    assert candidate(words = ['racecar', 'madam', 'level', 'rotor', 'deified']) == 5
    assert candidate(words = ['ab', 'ba', 'ac', 'ca', 'ad', 'da', 'ae', 'ea', 'af', 'fa', 'ag', 'ga', 'ah', 'ha', 'ai', 'ia', 'aj', 'ja', 'ak', 'ka', 'al', 'la', 'am', 'ma', 'an', 'na', 'ao', 'oa', 'ap', 'pa', 'aq', 'qa', 'ar', 'ra', 'as', 'sa', 'at', 'ta', 'au', 'ua', 'av', 'va', 'aw', 'wa', 'ax', 'xa', 'ay', 'ya', 'az', 'za']) == 50
    assert candidate(words = ['abacaba', 'bcbcbcb', 'bababab', 'cacacac', 'dcdcdcd', 'efefefe', 'gigigig', 'huhuhuh', 'ijijiij', 'kjkjkjk', 'lmnlmnl', 'ponponp', 'qrqrqrq', 'stststs', 'xvxvxvx', 'wywywyw', 'uzuzuzu', 'vavavav', 'bbabbab', 'abbabba']) == 20
    assert candidate(words = ['aabbccddeeff', 'bbccddeeffgg', 'ccddeeffgghh', 'ddeeffgghhiijj', 'eeffgghhiijjkkll', 'ffgghhiijjkkllmmnn', 'gghhiijjkkllmmnnoopp', 'hhiijjkkllmmnnooppqqrr', 'iijjkkllmmnnooppqqrrssttuuvv', 'jjkkllmmnnooppqqrrssttuuvvwxyz']) == 9
    assert candidate(words = ['aabb', 'bbaa', 'abab', 'baba', 'aaaa', 'bbbb', 'abcd', 'dcba', 'efgh', 'ghfe', 'ijkl', 'lkji', 'mnop', 'ponm', 'qrst', 'tsrq', 'uvwx', 'xwvu', 'yzxy', 'yxzy', 'abcdef', 'fedcba', 'ghijkl', 'lkjihg', 'mnopqr', 'rqponm', 'stuvwx', 'xwvuts', 'yzabcd', 'dcba']) == 29
    assert candidate(words = ['racecar', 'madam', 'refer', 'deified', 'rotor', 'kayak', 'reviled', 'repaper', 'redder', 'deed', 'peep', 'noon', 'civic', 'rotor', 'stats', 'level']) == 16
    assert candidate(words = ['abcdabcd', 'bcadbcad', 'cdabcdab', 'dabcadcb', 'abcdabcd', 'bcadbcad', 'cdabcdab', 'dabcadcb']) == 8
    assert candidate(words = ['abacaxa', 'xyz', 'mnopqr', 'uvw', 'stuv', 'lmno', 'ijkl', 'hgf', 'edc', 'bac']) == 8
    assert candidate(words = ['abacax', 'zyzyzy', 'noonnoon', 'levellevel', 'rotorrotor', 'statsstats', 'civiccivic', 'deifieddeified']) == 7
    assert candidate(words = ['abcabcabc', 'bcabcbacb', 'cabacabac', 'aabbcc', 'bbaacc', 'ccaabb', 'abcabcabc', 'bcabcbacb', 'cabacabac', 'aabbcc', 'bbaacc', 'ccaabb', 'abcabcabc', 'bcabcbacb', 'cabacabac', 'aabbcc', 'bbaacc', 'ccaabb', 'abcabcabc', 'bcabcbacb', 'cabacabac', 'aabbcc', 'bbaacc', 'ccaabb', 'abcabcabc', 'bcabcbacb', 'cabacabac', 'aabbcc', 'bbaacc', 'ccaabb']) == 30
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == 26
    assert candidate(words = ['aabbcc', 'abcdef', 'zyxwvut', 'mnopqr', 'lkjihg', 'fedcba', 'utsrqponmlkjihgfedcba', 'abcdefghijklnmopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklnmopqrstuvwxyz']) == 9
    assert candidate(words = ['aabbcc', 'abcabc', 'abcdabcd', 'abcdeabcde', 'abcdefabcdef']) == 5
    assert candidate(words = ['racecar', 'level', 'deified', 'rotor', 'repaper', 'deed', 'civic', 'rotor', 'refer', 'redder']) == 10
    assert candidate(words = ['abacax', 'xaba', 'aa', 'bb', 'cccc', 'dddd', 'eeff', 'fffe', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']) == 27
    assert candidate(words = ['abccba', 'abcba', 'abba', 'aba', 'a', 'b', 'c', 'd', 'e']) == 9
    assert candidate(words = ['xyz', 'zyx', 'yzx', 'zyx', 'zyx', 'zyx', 'zyx', 'zyx', 'zyx', 'zyx', 'zyx', 'zyx', 'zyx', 'zyx', 'zyx', 'zyx', 'zyx', 'zyx', 'zyx', 'zyx']) == 20
    assert candidate(words = ['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'kl', 'lk', 'mn', 'nm', 'op', 'po', 'qr', 'rq', 'st', 'ts', 'uv', 'vu', 'wx', 'xw', 'yz', 'zy', 'ab', 'ba', 'cd', 'dc', 'ef', 'fe']) == 32
    assert candidate(words = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'ffff', 'gggg', 'hhhh', 'iiii', 'jjjj', 'kkkk', 'llll', 'mmmm', 'nnnn', 'oooo', 'pppp', 'qqqq', 'rrrr', 'ssss', 'tttt', 'uuuu', 'vvvv', 'wwww', 'xxxx', 'yyyy', 'zzzz']) == 26
    assert candidate(words = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']) == 52
    assert candidate(words = ['abcde', 'edcba', 'fghij', 'jihgf', 'klmno', 'onmlk', 'pqrst', 'tsrqp', 'uvwxy', 'yxwvu', 'zabcd', 'dcbae']) == 12
    assert candidate(words = ['aabbcc', 'abcabc', 'abacab', 'aabbccddeeff', 'bbccddeeffgg', 'ccddeeffgghh', 'ddeeffgghhiijj', 'eeffgghhiijjkkll', 'ffgghhiijjkkllmmnn', 'gghhiijjkkllmmnnoopp', 'hhiijjkkllmmnnooppqqrr', 'iijjkkllmmnnooppqqrrssttuuvv', 'jjkkllmmnnooppqqrrssttuuvvwxyz']) == 12
    assert candidate(words = ['racecar', 'madam', 'refer', 'level', 'deified', 'reviled']) == 6
