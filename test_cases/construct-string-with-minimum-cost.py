# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(target = "xyz",words = ['x', 'y', 'z'],costs = [1, 2, 3]) == 6
    assert candidate(target = "abcd",words = ['a', 'b', 'c', 'd'],costs = [1, 1, 1, 1]) == 4
    assert candidate(target = "zzzz",words = ['zz', 'zzzz'],costs = [2, 1]) == 1
    assert candidate(target = "programming",words = ['pro', 'gram', 'ming'],costs = [10, 20, 30]) == 60
    assert candidate(target = "python",words = ['py', 'th', 'on'],costs = [5, 7, 8]) == 20
    assert candidate(target = "abacaba",words = ['a', 'b', 'c'],costs = [1, 2, 3]) == 11
    assert candidate(target = "hello",words = ['he', 'll', 'o'],costs = [3, 5, 2]) == 10
    assert candidate(target = "abcabc",words = ['abc', 'ab', 'c'],costs = [5, 3, 2]) == 10
    assert candidate(target = "abc",words = ['a', 'b', 'c'],costs = [1, 2, 3]) == 6
    assert candidate(target = "hello",words = ['h', 'he', 'hel', 'hell', 'hello'],costs = [5, 4, 3, 2, 1]) == 1
    assert candidate(target = "xyz",words = ['xy', 'y', 'z'],costs = [5, 3, 2]) == 7
    assert candidate(target = "aabbcc",words = ['aa', 'bb', 'cc'],costs = [1, 1, 1]) == 3
    assert candidate(target = "abcabcabc",words = ['abc', 'bc', 'c'],costs = [3, 2, 1]) == 9
    assert candidate(target = "abcde",words = ['a', 'bc', 'de'],costs = [2, 3, 4]) == 9
    assert candidate(target = "abcabc",words = ['abc', 'ab', 'c'],costs = [3, 2, 1]) == 6
    assert candidate(target = "zzzzz",words = ['z', 'zz', 'zzz'],costs = [1, 1, 1]) == 2
    assert candidate(target = "xyz",words = ['xy', 'yz', 'x'],costs = [2, 3, 1]) == 4
    assert candidate(target = "aaaa",words = ['z', 'zz', 'zzz'],costs = [1, 10, 100]) == -1
    assert candidate(target = "world",words = ['w', 'o', 'r', 'l', 'd'],costs = [2, 3, 4, 5, 6]) == 20
    assert candidate(target = "aabbcc",words = ['aa', 'bb', 'cc'],costs = [3, 4, 5]) == 12
    assert candidate(target = "abcdef",words = ['abdef', 'abc', 'd', 'def', 'ef'],costs = [100, 1, 1, 10, 5]) == 7
    assert candidate(target = "ababab",words = ['ab', 'aba', 'bab'],costs = [3, 4, 5]) == 9
    assert candidate(target = "testcase",words = ['tes', 't', 'case'],costs = [10, 2, 5]) == 17
    assert candidate(target = "abcde",words = ['a', 'bc', 'de'],costs = [1, 2, 3]) == 6
    assert candidate(target = "abcdefgabcdefg",words = ['abc', 'def', 'g', 'abcde', 'fg'],costs = [6, 7, 1, 5, 3]) == 16
    assert candidate(target = "aaaabbbbcccc",words = ['a', 'aa', 'aaa', 'aaaa', 'b', 'bb', 'bbb', 'bbbb', 'c', 'cc', 'ccc', 'cccc'],costs = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 12
    assert candidate(target = "xyxxyxyxyx",words = ['xy', 'yx', 'xxy', 'xyx'],costs = [1, 2, 3, 4]) == 9
    assert candidate(target = "zzzzzzzzzz",words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzz'],costs = [1, 3, 5, 7, 9]) == 10
    assert candidate(target = "mnopqr",words = ['mno', 'pqr', 'mnop', 'qr', 'qrs'],costs = [5, 6, 3, 8, 2]) == 11
    assert candidate(target = "xyzxyzxyz",words = ['xyz', 'xy', 'xz', 'yz'],costs = [10, 5, 6, 7]) == 30
    assert candidate(target = "aaaabbbbccccdddd",words = ['aaa', 'bbb', 'ccc', 'ddd', 'abcd'],costs = [10, 15, 20, 25, 30]) == -1
    assert candidate(target = "zzzzzzzzzzzzzzzzzzzz",words = ['zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz'],costs = [1, 2, 3, 4, 5]) == 10
    assert candidate(target = "hellohello",words = ['he', 'll', 'o', 'hello'],costs = [3, 2, 1, 5]) == 10
    assert candidate(target = "zzzzzzzzzz",words = ['z', 'zz', 'zzz', 'zzzz'],costs = [1, 3, 6, 10]) == 10
    assert candidate(target = "helloworld",words = ['he', 'll', 'lo', 'wor', 'orl', 'ld'],costs = [1, 2, 3, 4, 5, 6]) == -1
    assert candidate(target = "zzzzzzzzzzzz",words = ['zz', 'zzz', 'z'],costs = [4, 2, 7]) == 8
    assert candidate(target = "abcabcabcabc",words = ['abc', 'cab', 'bca'],costs = [10, 20, 30]) == 40
    assert candidate(target = "abcdabcdabcd",words = ['abcd', 'ab', 'cd', 'abc'],costs = [10, 5, 3, 8]) == 24
    assert candidate(target = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",words = ['aabb', 'ccdd', 'eef', 'gghh', 'iijj', 'kkl', 'mnoon', 'popp', 'qqr', 'rss', 'ttu', 'vvww', 'xxy', 'yzz'],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == -1
    assert candidate(target = "abcdefghi",words = ['abc', 'def', 'ghi', 'abcd', 'efgh', 'hij', 'abcd'],costs = [10, 20, 30, 15, 25, 35, 5]) == 60
    assert candidate(target = "aabbaabbccddcc",words = ['aa', 'bb', 'cc', 'dd'],costs = [1, 2, 3, 4]) == 16
    assert candidate(target = "xyxyxyxyxyxy",words = ['xy', 'yx', 'xxyy'],costs = [10, 5, 20]) == 60
    assert candidate(target = "zzzzzzzzzzzz",words = ['zzz', 'zzzz', 'zz', 'z'],costs = [15, 10, 8, 5]) == 30
    assert candidate(target = "mississippi",words = ['mis', 'issi', 'ppi', 'ippi', 'pi'],costs = [10, 12, 5, 8, 3]) == -1
    assert candidate(target = "abcdefghijklmnop",words = ['abcdefghijklmno', 'p', 'abcdefghijk', 'lmnop'],costs = [100, 1, 50, 50]) == 100
    assert candidate(target = "aaaaaaaaaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],costs = [1, 2, 3, 4, 5]) == 10
    assert candidate(target = "xyzxyzxyz",words = ['xy', 'z', 'xyz'],costs = [5, 1, 3]) == 9
    assert candidate(target = "alibaba",words = ['ali', 'ba', 'ba', 'b', 'a'],costs = [5, 10, 20, 1, 2]) == 11
    assert candidate(target = "abracadabra",words = ['a', 'b', 'r', 'ac', 'ad', 'abra'],costs = [1, 2, 3, 4, 5, 6]) == 21
    assert candidate(target = "bbaaccdd",words = ['bb', 'aa', 'cc', 'dd', 'abcd'],costs = [5, 6, 7, 8, 9]) == 26
    assert candidate(target = "xylophone",words = ['xy', 'lo', 'phone', 'pho', 'ne', 'on'],costs = [3, 1, 2, 5, 4, 6]) == 6
    assert candidate(target = "abcabcabcabc",words = ['abc', 'ab', 'bc', 'a', 'b', 'c'],costs = [5, 2, 3, 1, 1, 1]) == 12
    assert candidate(target = "abcdabcdabcd",words = ['ab', 'bc', 'cd', 'abcd'],costs = [1, 2, 3, 4]) == 12
    assert candidate(target = "aaaaaaaaaa",words = ['a', 'aa', 'aaa', 'aaaa'],costs = [5, 3, 2, 1]) == 5
    assert candidate(target = "abcdefghijk",words = ['abc', 'def', 'gh', 'ijk'],costs = [10, 20, 30, 40]) == 100
    assert candidate(target = "abracadabra",words = ['abr', 'aca', 'dab', 'ra'],costs = [10, 20, 30, 5]) == 65
    assert candidate(target = "abcdefghij",words = ['ab', 'cde', 'fgh', 'ij'],costs = [2, 3, 4, 1]) == 10
    assert candidate(target = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],costs = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 450
    assert candidate(target = "xyzabc",words = ['xy', 'zabc', 'xyz', 'ab', 'c'],costs = [5, 10, 3, 7, 2]) == 12
    assert candidate(target = "aabbccddeeff",words = ['aabb', 'ccdd', 'eeff', 'abcd'],costs = [10, 15, 20, 25]) == 45
    assert candidate(target = "zzzzzzzzzzz",words = ['zz', 'zzz', 'zzzz'],costs = [2, 5, 7]) == 13
    assert candidate(target = "zzzzzzzzzzzzzzzzzzzz",words = ['z', 'zz', 'zzz', 'zzzz'],costs = [1, 2, 3, 4]) == 20
    assert candidate(target = "xyxzyzyxzyzyxzyx",words = ['xyx', 'zyz', 'yx', 'xyz'],costs = [7, 6, 5, 4]) == -1
    assert candidate(target = "aaaaabbbbb",words = ['a', 'b', 'ab', 'ba'],costs = [1, 2, 3, 4]) == 15
    assert candidate(target = "mississippi",words = ['mis', 'issi', 'ppi', 'ss', 'ippi', 's', 'i', 'm'],costs = [1, 3, 5, 1, 2, 2, 1, 1]) == 7
    assert candidate(target = "hellohello",words = ['he', 'llo', 'ell', 'o'],costs = [2, 3, 1, 4]) == 10
    assert candidate(target = "pppppppppp",words = ['p', 'pp', 'ppp'],costs = [10, 5, 3]) == 16
    assert candidate(target = "zzzzzzzzzzzzzzzzzzzz",words = ['zzz', 'zz', 'z'],costs = [10, 5, 1]) == 20
    assert candidate(target = "abcdefghij",words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550
    assert candidate(target = "zzzzzzzzzz",words = ['zz', 'zzz', 'z'],costs = [1, 2, 10]) == 5
    assert candidate(target = "aabbccddeeff",words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff'],costs = [1, 2, 1, 2, 1, 2]) == 9
    assert candidate(target = "abcdefghi",words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
    assert candidate(target = "aabbccddeeff",words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'abcd', 'ef', 'fedc'],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 21
    assert candidate(target = "zzzzzzzzzzzzzzzzzzzz",words = ['z', 'zz', 'zzz'],costs = [1, 10, 100]) == 20
    assert candidate(target = "mnopqr",words = ['m', 'no', 'pqr', 'op', 'qr', 'mnop', 'nopqr'],costs = [1, 2, 3, 4, 5, 6, 7]) == 6
    assert candidate(target = "hellohellos",words = ['he', 'llo', 'hel', 'los', 'o', 's'],costs = [1, 2, 3, 4, 5, 6]) == 10
    assert candidate(target = "mamamamama",words = ['ma', 'am'],costs = [2, 1]) == 10
    assert candidate(target = "abcdabcdabcd",words = ['abcd', 'abc', 'bca', 'cab', 'dab'],costs = [10, 7, 8, 9, 6]) == 30
    assert candidate(target = "abcdabcdabcd",words = ['abcd', 'abc', 'cd', 'd', 'a', 'bc'],costs = [10, 20, 30, 40, 50, 60]) == 30
    assert candidate(target = "aaaabbbb",words = ['a', 'aa', 'aaa', 'aaaa'],costs = [4, 3, 2, 1]) == -1
    assert candidate(target = "abcdefghijklmnop",words = ['a', 'bc', 'def', 'ghij', 'klmno', 'p'],costs = [1, 2, 3, 4, 5, 6]) == 21
    assert candidate(target = "banana",words = ['ba', 'an', 'na', 'ana', 'nana', 'banana'],costs = [1, 2, 3, 4, 5, 6]) == 6
    assert candidate(target = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],costs = [3, 5, 4, 7, 6, 8, 9, 2, 1]) == 45
    assert candidate(target = "mnopqr",words = ['mno', 'pq', 'r', 'mnopq', 'qrs'],costs = [10, 7, 5, 20, 8]) == 22
    assert candidate(target = "aaabbbcccddd",words = ['aaa', 'bbb', 'ccc', 'ddd', 'ab', 'bc', 'cd'],costs = [5, 6, 7, 8, 3, 4, 5]) == 26
    assert candidate(target = "mississippi",words = ['mis', 'is', 'sip', 'i', 'p'],costs = [1, 2, 3, 4, 5]) == -1
    assert candidate(target = "abcdefg",words = ['abc', 'def', 'g', 'abcd', 'efg'],costs = [10, 20, 5, 15, 25]) == 35
    assert candidate(target = "aabbccddeeff",words = ['aab', 'bcc', 'dde', 'eff'],costs = [6, 7, 8, 9]) == 30
    assert candidate(target = "aaabbbcccddd",words = ['aaa', 'bbb', 'ccc', 'ddd', 'aab', 'bcc', 'dde'],costs = [10, 11, 12, 13, 9, 8, 7]) == 46
    assert candidate(target = "abababababab",words = ['aba', 'bab', 'ab'],costs = [3, 4, 1]) == 6
    assert candidate(target = "optimization",words = ['opt', 'im', 'iza', 'tion'],costs = [10, 20, 30, 40]) == 100
    assert candidate(target = "xyzxyzxyzxyz",words = ['xyz', 'xy', 'zxyz', 'zxy'],costs = [7, 5, 10, 8]) == 28
    assert candidate(target = "ababababab",words = ['aba', 'bab', 'ab', 'ba'],costs = [7, 8, 2, 3]) == 10
    assert candidate(target = "qwertyuiop",words = ['qwe', 'rty', 'ui', 'op'],costs = [7, 8, 5, 6]) == 26
    assert candidate(target = "aaaabbbbccccdddd",words = ['aaaa', 'bbbb', 'cccc', 'dddd', 'abc', 'bcd', 'cde', 'def'],costs = [4, 5, 6, 7, 8, 9, 10, 11]) == 22
    assert candidate(target = "abcabcabcabc",words = ['abc', 'bc', 'ca'],costs = [1, 2, 3]) == 4
    assert candidate(target = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],costs = [10, 15, 20, 25, 30, 35, 40, 45, 50]) == 270
    assert candidate(target = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],costs = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 45
    assert candidate(target = "xyxyxyxyxy",words = ['xy', 'yx', 'x', 'y'],costs = [4, 5, 1, 2]) == 15
    assert candidate(target = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz'],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 351
    assert candidate(target = "abcdefghij",words = ['abc', 'def', 'ghi', 'j', 'abcdefgh'],costs = [12, 15, 20, 5, 100]) == 52
    assert candidate(target = "abcdefghijklmnopqrstuvwxyz",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
    assert candidate(target = "ababababab",words = ['ab', 'aba', 'bab', 'aab'],costs = [100, 200, 300, 400]) == 500
    assert candidate(target = "mississippi",words = ['i', 's', 'p', 'is', 'pi', 'sis', 'issi'],costs = [1, 2, 3, 4, 5, 6, 7]) == -1
    assert candidate(target = "ababababab",words = ['ab', 'aba', 'bab', 'ba'],costs = [1, 3, 2, 4]) == 5
    assert candidate(target = "aabbccddeeff",words = ['ab', 'bc', 'cd', 'de', 'ef', 'fe', 'dc', 'cb', 'ba', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff'],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 75
    assert candidate(target = "lmnopqrstu",words = ['lmn', 'opq', 'rst', 'u'],costs = [1, 2, 3, 4]) == 10
    assert candidate(target = "aabbccddeeffgghhiijj",words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj'],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(target = "ababababab",words = ['aba', 'bab', 'ab', 'ba'],costs = [4, 5, 2, 3]) == 10
    assert candidate(target = "xyxxyxyxyx",words = ['xy', 'xxy', 'xyx', 'yxy'],costs = [5, 7, 6, 8]) == 22
    assert candidate(target = "mississippi",words = ['mis', 'issi', 'ppi', 'i', 'pi', 'miss', 'ippi'],costs = [3, 4, 2, 1, 5, 6, 7]) == 12
    assert candidate(target = "aaaaaaaabaaaaaaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],costs = [1, 3, 5, 7, 9]) == -1
    assert candidate(target = "abcdefghijklmnop",words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],costs = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == -1
    assert candidate(target = "ababababab",words = ['ab', 'aba', 'bab', 'ba', 'a', 'b'],costs = [2, 3, 4, 1, 5, 6]) == 9
    assert candidate(target = "abcdefgabcdefg",words = ['abc', 'def', 'gh', 'abcdef', 'gh', 'abcdefg'],costs = [10, 20, 30, 5, 50, 60]) == 120
    assert candidate(target = "abcdefghijklmnopqrstuvwxyz",words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == -1
    assert candidate(target = "abcabcabcabcabcabc",words = ['abc', 'abca', 'bcab', 'cabc', 'bca'],costs = [1, 2, 3, 4, 5]) == 6
    assert candidate(target = "abacabadabacaba",words = ['aba', 'cab', 'abc', 'bac'],costs = [3, 5, 2, 4]) == -1
    assert candidate(target = "qwertyqwerty",words = ['qw', 'er', 'ty', 'rt', 'yt'],costs = [1, 2, 3, 4, 5]) == 12
    assert candidate(target = "abcabcabcabcabc",words = ['ab', 'bc', 'ca', 'abc'],costs = [2, 1, 5, 3]) == 15
    assert candidate(target = "abcabcabcabcabcabc",words = ['abc', 'abcabc', 'abcabcabc', 'a', 'b', 'c'],costs = [10, 20, 30, 1, 2, 3]) == 36
    assert candidate(target = "qwertyuiopasdfghjklzxcvbnm",words = ['qwerty', 'uiop', 'asdf', 'ghjk', 'lzx', 'cvbn', 'm', 'qwer', 'tyui', 'opas', 'dfgh', 'jklz', 'xcvb', 'bnm'],costs = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 105
    assert candidate(target = "abacabadabacaba",words = ['aba', 'abac', 'abacaba', 'abacabad', 'abacabadaba'],costs = [5, 10, 15, 20, 25]) == 35
