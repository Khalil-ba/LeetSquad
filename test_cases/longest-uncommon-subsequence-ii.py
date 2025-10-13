# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(strs = ['aaa', 'aaa', 'aa']) == -1
    assert candidate(strs = ['a', 'b', 'c', 'd', 'e']) == 1
    assert candidate(strs = ['a', 'a', 'a', 'a']) == -1
    assert candidate(strs = ['xyz', 'xy', 'xz', 'yzz']) == 3
    assert candidate(strs = ['aabbcc', 'abc', 'aabbc', 'aabc']) == 6
    assert candidate(strs = ['abcd', 'abcde', 'ab', 'abc']) == 5
    assert candidate(strs = ['abcd', 'ab', 'bc', 'cd']) == 4
    assert candidate(strs = ['abc', 'abc', 'abcd']) == 4
    assert candidate(strs = ['aabbcc', 'abc', 'abbc', 'aabbc']) == 6
    assert candidate(strs = ['abc', 'def', 'ghi']) == 3
    assert candidate(strs = ['abcde', 'abc', 'de', 'a']) == 5
    assert candidate(strs = ['aba', 'cdc', 'eae']) == 3
    assert candidate(strs = ['a', 'b', 'c']) == 1
    assert candidate(strs = ['xyz', 'zyx', 'yxz', 'xzy', 'yzx', 'zxy', 'xyz', 'zyx']) == 3
    assert candidate(strs = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee', 'ffffff']) == 6
    assert candidate(strs = ['abcd', 'dcba', 'abcd', 'dcba', 'abcd', 'dcba', 'abcd', 'dcba']) == -1
    assert candidate(strs = ['abcd', 'abdc', 'acbd', 'dacb', 'cadb', 'bacd']) == 4
    assert candidate(strs = ['apple', 'apples', 'applesauce', 'appl', 'applf', 'applfs', 'applfsa', 'applfsau', 'applfsauc']) == 10
    assert candidate(strs = ['programming', 'programing', 'progamming', 'programmig', 'proogramming', 'programmiing']) == 12
    assert candidate(strs = ['mississippi', 'mississipi', 'mississipp', 'mississip', 'mississi', 'mississ', 'missis', 'missi', 'misi', 'msi', 'mi', 'm']) == 11
    assert candidate(strs = ['abcde', 'abxde', 'axcde', 'abxde', 'abcde', 'abcde']) == 5
    assert candidate(strs = ['abac', 'bca', 'cab', 'aaa', 'bbb', 'ccc']) == 4
    assert candidate(strs = ['banana', 'bananb', 'bananc', 'bandan', 'bandna', 'bandan', 'bandnaa', 'bandnaab', 'bandnaabc']) == 9
    assert candidate(strs = ['abcd', 'abdc', 'aebc', 'aecb', 'acbe']) == 4
    assert candidate(strs = ['abcd', 'abc', 'ab', 'a', 'aaaa', 'aaa', 'aa', 'a']) == 4
    assert candidate(strs = ['mnopqr', 'nopqrm', 'opqrmn', 'pqrmno', 'qrmnop', 'rmnopq']) == 6
    assert candidate(strs = ['abc', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']) == 10
    assert candidate(strs = ['pqr', 'pqrs', 'pqs', 'prs', 'qs', 'qrs', 'qr', 'rs', 'r', 's']) == 4
    assert candidate(strs = ['hello', 'world', 'hold', 'hero']) == 5
    assert candidate(strs = ['abcde', 'edcba', 'abdec', 'cabde', 'deabc', 'eabcd']) == 5
    assert candidate(strs = ['aabbcc', 'aabbbc', 'aabbcccc', 'aabbccdd', 'aabbccdde', 'aabbccddee']) == 10
    assert candidate(strs = ['aabbcc', 'abcabc', 'aabcbc', 'abacbc', 'aabbcc', 'aacbbc', 'aabbbc']) == 6
    assert candidate(strs = ['xxyy', 'xyxy', 'yxyx', 'xyyx', 'yxxxy', 'xyxxy', 'xxyxy', 'xyxyx']) == 5
    assert candidate(strs = ['abcabc', 'bcabca', 'cababc', 'abacbc', 'bcbcab', 'acbcab']) == 6
    assert candidate(strs = ['hello', 'hallo', 'hxllo', 'hell', 'helo', 'helo', 'heo', 'he', 'h', 'o']) == 5
    assert candidate(strs = ['abacax', 'bacaxa', 'caxaba', 'axabac', 'xacaba', 'cabaxa']) == 6
    assert candidate(strs = ['pqrst', 'pqrstu', 'pqrstu', 'pqrstu', 'pqr', 'pq', 'p']) == -1
    assert candidate(strs = ['unique', 'uniqe', 'unque', 'uniqu', 'uqnie', 'unieq', 'unqiue']) == 6
    assert candidate(strs = ['aab', 'aac', 'baa', 'bca', 'caa', 'cab', 'abc', 'acb']) == 3
    assert candidate(strs = ['x', 'xy', 'xyz', 'xyzz', 'xyzzz', 'xyzzzz', 'xyzzzzz', 'xyzzzzzz']) == 8
    assert candidate(strs = ['abcd', 'abcde', 'abcdef', 'ab', 'abcd']) == 6
    assert candidate(strs = ['aabbcc', 'bbaacc', 'ccabba', 'aaccbb', 'cabbba', 'bccaba']) == 6
    assert candidate(strs = ['aaaaa', 'aaaba', 'aabaa', 'abaab', 'abbaa']) == 5
    assert candidate(strs = ['abcdefg', 'bcdefga', 'cdefgab', 'defgabc', 'efgabcd', 'fgabcde']) == 7
    assert candidate(strs = ['abcde', 'edcba', 'bcdea', 'cdeab', 'decba']) == 5
    assert candidate(strs = ['hello', 'hallo', 'hxllo', 'hexlo', 'helxo']) == 5
    assert candidate(strs = ['abab', 'baba', 'abba', 'baab', 'abba']) == 4
    assert candidate(strs = ['abcdabcd', 'abcdeabc', 'abdcabdc', 'dacbdacb', 'dabcdbac', 'bacdabcd', 'abcdabdc']) == 8
    assert candidate(strs = ['aabbcc', 'aabcbc', 'abacbc', 'abcabc', 'abcbac', 'abccba']) == 6
    assert candidate(strs = ['banana', 'anana', 'nana', 'ana', 'na', 'a']) == 6
    assert candidate(strs = ['aaaaa', 'aaaba', 'aabaa', 'abaaa', 'baaaa']) == 5
    assert candidate(strs = ['abcde', 'abc', 'ab', 'a']) == 5
    assert candidate(strs = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba', 'abcd']) == 4
    assert candidate(strs = ['banana', 'anana', 'nana', 'ana', 'na', 'a', 'b']) == 6
    assert candidate(strs = ['longstring', 'longerstring', 'longeststring', 'longstringer', 'longstringest', 'longstringerer']) == 14
    assert candidate(strs = ['abcdef', 'abcfed', 'bacdef', 'badcfe', 'bcadef', 'bcdafe']) == 6
    assert candidate(strs = ['aaaa', 'aaab', 'aaba', 'abaa', 'abab', 'abba', 'bbaa', 'baab', 'baba', 'bbaa']) == 4
    assert candidate(strs = ['abcabc', 'bcabc', 'cabc', 'abc', 'ab', 'a', 'b', 'c']) == 6
    assert candidate(strs = ['aaaaa', 'aaab', 'aab', 'aba', 'baa', 'aaa']) == 5
    assert candidate(strs = ['mississippi', 'missisipi', 'missippi', 'mssippi', 'msissippi']) == 11
    assert candidate(strs = ['abcdefg', 'bcdefga', 'cdefgab', 'defgabc', 'efgabcd', 'fgabcde', 'gabcdef']) == 7
    assert candidate(strs = ['cat', 'dog', 'caterpillar', 'cattle', 'tall']) == 11
    assert candidate(strs = ['hello', 'hallo', 'hullo', 'hellu', 'hullo', 'helou']) == 5
    assert candidate(strs = ['aabbcc', 'abbccc', 'aabccc', 'aaabcc', 'aabbcc', 'aabbbc', 'aabbbc', 'aabccc', 'abbccc', 'abaccc']) == 6
    assert candidate(strs = ['abcd', 'abac', 'abca', 'acba', 'acab', 'aabc', 'abbc', 'aabb', 'abbb', 'bbbb']) == 4
    assert candidate(strs = ['ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']) == 7
    assert candidate(strs = ['abcd', 'abdc', 'acbd', 'dabc', 'dacb']) == 4
    assert candidate(strs = ['abcabc', 'ababc', 'abc', 'abcd', 'abcde']) == 6
    assert candidate(strs = ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']) == 4
    assert candidate(strs = ['abcdef', 'abdefc', 'acdefb', 'adefbc', 'aebcdf', 'afedcb']) == 6
    assert candidate(strs = ['hello', 'world', 'hold', 'wolf', 'hold', 'hold']) == 5
    assert candidate(strs = ['abcdefgh', 'bghcdefa', 'cdefghba', 'defghbac', 'efghbacd', 'fghbacde']) == 8
    assert candidate(strs = ['abcde', 'abced', 'acbed', 'acbde', 'adbec', 'adebc']) == 5
    assert candidate(strs = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']) == 3
    assert candidate(strs = ['abcde', 'edcba', 'cbade', 'badce', 'aecdb', 'bcdea', 'abced']) == 5
    assert candidate(strs = ['abcdefgh', 'bcdefgh', 'cdefgh', 'defgh', 'efgh', 'fgh', 'gh', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == 8
    assert candidate(strs = ['aaaa', 'aaab', 'aaba', 'abaa', 'baaa']) == 4
    assert candidate(strs = ['abcd', 'abdc', 'acbd', 'dacb', 'cabd']) == 4
    assert candidate(strs = ['aaaa', 'aaab', 'aabb', 'abbb', 'bbbb']) == 4
    assert candidate(strs = ['xyz', 'zyx', 'yz', 'zx', 'yx', 'x', 'y', 'z', '']) == 3
    assert candidate(strs = ['abcd', 'abcde', 'ab', 'abc', 'a', 'abcd', 'abcde', 'ab', 'abc', 'a']) == -1
    assert candidate(strs = ['aab', 'abc', 'abcd', 'abcde', 'abcdef']) == 6
    assert candidate(strs = ['abcd', 'abdc', 'acbd', 'adcb', 'bacd']) == 4
    assert candidate(strs = ['xyzz', 'zyxz', 'xzyz', 'zxzy', 'xzzy', 'zzxy']) == 4
    assert candidate(strs = ['banana', 'bandana', 'bandanna', 'band', 'anana']) == 8
    assert candidate(strs = ['aabbcc', 'aabbc', 'aabc', 'abc', 'aab', 'ab', 'ac', 'a', 'b', 'c', 'd']) == 6
    assert candidate(strs = ['abc', 'abc', 'abc', 'abcd']) == 4
    assert candidate(strs = ['apple', 'ale', 'app', 'appl', 'ample']) == 5
    assert candidate(strs = ['zzzzzzzzzz', 'zzzzzzzzz', 'zzzzzzzz', 'zzzzzzz', 'zzzzzz', 'zzzzz', 'zzzz', 'zzz', 'zz', 'z']) == 10
    assert candidate(strs = ['unique', 'distinct', 'different', 'separate', 'unequal', 'unique', 'distinct', 'different', 'separate', 'unequal']) == -1
    assert candidate(strs = ['sequence', 'subsequence', 'subseq', 'seq', 'sequencee']) == 11
    assert candidate(strs = ['aaaaa', 'aaaab', 'aaaba', 'aabaa', 'abaaa', 'baaaa', 'aabba', 'aabra', 'abaab', 'baaab', 'ababa', 'babaa', 'abaab', 'baaba', 'abaaa', 'baaaa', 'aabaa', 'abaaa', 'baaba', 'abaab']) == 5
    assert candidate(strs = ['zzzz', 'zzzzz', 'zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz', 'zzzzzzzzzz']) == 10
    assert candidate(strs = ['abcd', 'abdc', 'acbd', 'dacb', 'cdab', 'cabd']) == 4
    assert candidate(strs = ['xyz', 'xyx', 'xyy', 'xzy', 'yzy', 'yzz', 'zzy', 'zzyz', 'zzzy', 'zzzz']) == 4
    assert candidate(strs = ['apple', 'aple', 'appl', 'pple', 'aplp']) == 5
    assert candidate(strs = ['hello', 'hallo', 'hxllo', 'hexlo', 'hxllo', 'hxllo']) == 5
    assert candidate(strs = ['aaaabbbb', 'aaabbb', 'aabbb', 'abbb', 'bbb', 'bb', 'b']) == 8
    assert candidate(strs = ['pqr', 'qrp', 'rpq', 'prq', 'rqp', 'qpr', 'ppp', 'qqq', 'rrr']) == 3
    assert candidate(strs = ['qwerty', 'qwertyuiop', 'qwertyuio', 'qwertyui', 'qwer']) == 10
    assert candidate(strs = ['aaabbb', 'aabbbb', 'abbbbb', 'aaabbbb', 'aabbbbbb', 'abbbbbbb']) == 8
    assert candidate(strs = ['abcabcabc', 'abc', 'bc', 'c', 'bca', 'cab', 'bac', 'acb', 'cba', 'abcabc']) == 9
    assert candidate(strs = ['pqr', 'pqrs', 'pqrst', 'pqrstu', 'pqrstuv', 'pqrstuvw', 'pqrstuvwx', 'pqrstuvwxy']) == 10
    assert candidate(strs = ['xyz', 'xy', 'xz', 'yz', 'x', 'y', 'z', 'xyx', 'yzy', 'zxz']) == 3
    assert candidate(strs = ['xyz', 'xyx', 'xzy', 'yxz', 'yzy', 'zyx', 'zyz']) == 3
    assert candidate(strs = ['abcdefghij', 'abcdefghi', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']) == 10
