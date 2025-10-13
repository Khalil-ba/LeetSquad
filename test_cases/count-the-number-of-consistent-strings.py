# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(allowed = "ijkl",words = ['i', 'j', 'k', 'l', 'ij', 'ik', 'il', 'jk', 'jl', 'kl', 'ijkl']) == 11
    assert candidate(allowed = "abcdef",words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']) == 6
    assert candidate(allowed = "cad",words = ['cc', 'acd', 'b', 'ba', 'bac', 'bad', 'ac', 'd']) == 4
    assert candidate(allowed = "gh",words = ['g', 'h', 'gh']) == 3
    assert candidate(allowed = "xyz",words = ['xy', 'yz', 'xzy', 'zxy', 'zyx', 'xyz']) == 6
    assert candidate(allowed = "xyz",words = ['x', 'y', 'z', 'xy', 'xz', 'yz', 'xyz']) == 7
    assert candidate(allowed = "uvw",words = ['u', 'v', 'w', 'uv', 'uw', 'vw', 'uvw']) == 7
    assert candidate(allowed = "mnop",words = ['m', 'n', 'o', 'p', 'mn', 'mo', 'mp', 'no', 'np', 'op', 'mno', 'mnp', 'mop', 'nop', 'mnop']) == 15
    assert candidate(allowed = "mnop",words = ['m', 'n', 'o', 'p', 'mn', 'mo', 'mp', 'no', 'np', 'op', 'mno', 'mnp', 'mop', 'nop', 'mnop']) == 15
    assert candidate(allowed = "ab",words = ['ad', 'bd', 'aaab', 'baa', 'badab']) == 2
    assert candidate(allowed = "abc",words = ['a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']) == 7
    assert candidate(allowed = "qrst",words = ['qr', 'qs', 'qt', 'rs', 'rt', 'st', 'qrs', 'qrt', 'qst', 'rst', 'qrst']) == 11
    assert candidate(allowed = "qwerty",words = ['q', 'w', 'e', 'r', 't', 'y', 'qw', 'we', 'er', 'rt', 'ty', 'yq', 'qr', 're', 'et', 'ty', 'yr', 're', 'et', 'ty', 'qwer', 'wert', 'erty', 'rtye', 'tyer', 'yert', 'erty', 'rtye', 'tyer', 'yert']) == 30
    assert candidate(allowed = "xyz",words = ['xzy', 'zyx', 'xyzz', 'zyzzx', 'xzyzyx', 'zyzxzy', 'xyzxyz', 'zyxzyxzyx']) == 8
    assert candidate(allowed = "abcdef",words = ['abc', 'bcd', 'cde', 'def', 'abcf', 'bcde', 'cdef', 'abcdef', 'af', 'bf', 'cf', 'df', 'ef', 'f', 'a', 'b', 'c', 'd', 'e']) == 19
    assert candidate(allowed = "abcdefg",words = ['abc', 'def', 'ghi', 'abcd', 'efg', 'abdefg', 'abcdef', 'abcdefg', 'xyz']) == 7
    assert candidate(allowed = "mnopqr",words = ['mnop', 'opqr', 'mnqr', 'mpqr', 'mnoq', 'mnpq', 'mnopq', 'mnopqr', 'mnoqr', 'mnopqr', 'qrmpno', 'rpmnqo', 'qrmp', 'mnpqr', 'pqmno']) == 15
    assert candidate(allowed = "xyz",words = ['x', 'y', 'z', 'xy', 'xz', 'yz', 'xyz', 'xyzz', 'zxy', 'yxz', 'zyx', 'zzz']) == 12
    assert candidate(allowed = "abcdef",words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'fedcba', 'defabc', 'cbadef', 'abcdefg', 'abcdefh', 'abcdefi', 'abcdefj', 'abcdefk', 'abcdefl', 'abcdefm', 'abef', 'acd', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz', 'ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij', 'jk', 'kl', 'lm', 'mn', 'no', 'op', 'pq', 'qr', 'rs', 'st', 'tu', 'uv', 'vw', 'wx', 'xy', 'yz', 'za', 'abab', 'acac', 'adad', 'aeae', 'afaf', 'agag', 'ahah', 'aiai', 'ajaj', 'akak', 'alal', 'amam', 'anan', 'aoao', 'apap', 'aqaq', 'arar', 'asas', 'atat', 'auau', 'avav', 'awaw', 'axax', 'ayay', 'azaz']) == 24
    assert candidate(allowed = "tuvwxy",words = ['tuv', 'uvw', 'vwx', 'wxy', 'tuvw', 'uvwx', 'vwx', 'wxy', 'tuvwx', 'uvwxy', 'tuvwxy', 'tuvwxyu', 'tuvwxyv', 'tuvwxyw', 'tuvwxyx', 'tuvwxyy']) == 16
    assert candidate(allowed = "ijklmno",words = ['ijkl', 'ijkm', 'ilkn', 'ijln', 'ikln', 'jklm', 'jkmn', 'jlmn', 'klnm', 'ijklmnop', 'ijklmnoi', 'ijklmnopq', 'ijklmnopqrstuvwxyz', 'ijklmnolikj', 'ijklmnlijklmn', 'mnopijk', 'mnopilkmn']) == 12
    assert candidate(allowed = "mnopqrstuvw",words = ['mnop', 'qrstuv', 'w', 'mnopqr', 'stuvw', 'mnopqrstuvw', 'mnopqrstuvww', 'mnopqrstuvwww', 'mnopqrstuvwq', 'mnopqrstuvwqq', 'mnopqrstuvwrr', 'mnopqrstuvwsss', 'mnopqrstuvwttt', 'mnopqrstuvwuuu', 'mnopqrstuvwvvv', 'mnopqrstuvwwww']) == 16
    assert candidate(allowed = "qrstuv",words = ['qrst', 'uv', 'qrs', 'tu', 'rqs', 'vut', 'qrtuv', 'tuvqr', 'usvrtq', 'rqstuv', 'uvtqrs', 'qrsutv', 'rqvstu']) == 13
    assert candidate(allowed = "pqrs",words = ['pq', 'qr', 'rs', 'sp', 'pqrs', 'prqs', 'psrq', 'sqrp', 'rqps', 'rspq', 'pqs', 'qsr', 'rsq', 'spq', 'qrp', 'rps', 'sqr', 'prq', 'qsp', 'rqs', 'spr', 'psr', 'qrs', 'rsq', 'spq', 'pqr', 'qrs', 'rsp', 'spr', 'psr', 'srp', 'rps', 'qsp', 'psq']) == 34
    assert candidate(allowed = "mnopqr",words = ['mno', 'mnp', 'mqr', 'npr', 'opq', 'orq', 'pqr', 'mnop', 'mnoq', 'mnopqr', 'pqor', 'nopr', 'mnopq', 'nopqr', 'mnopqrs', 'mnoprq', 'mnopqrr', 'mnopqrs', 'mnopqrs', 'mnopqrs', 'mnopqrs', 'mnopqrs', 'mnopqrs', 'mnopqrs', 'mnopqrs', 'mnopqrs', 'mnopqrs', 'mnopqrs', 'mnopqrs']) == 16
    assert candidate(allowed = "jklm",words = ['jj', 'kk', 'll', 'mm', 'jk', 'jl', 'jm', 'kl', 'km', 'lm', 'jkl', 'jkm', 'jlm', 'klm', 'jklm', 'jkll', 'jjkkllmm', 'klmklm', 'jkljkl', 'mnop', 'qrst', 'uvwxy', 'z']) == 19
    assert candidate(allowed = "klmnopqrstuvwxyz",words = ['klmnopqrstuvwxyzz', 'klmnopqrstuvwxzz', 'klmnopqrstuvwxxz', 'klmnopqrstuvvvvv', 'klmnopqrsssssss', 'klmnopqqqqqqqq', 'klllllllllll', 'kkkkkkkkkkkk', 'jjjjjjjjjjjj', 'iiiiiiiiiiii', 'hhhhhhhhhhhh', 'gggggggggggg', 'ffffffffffff', 'eeeeeeeeeeee', 'dddddddddddd', 'cccccccccc', 'bbbbbbbbbb', 'aaaaaaaaaa']) == 8
    assert candidate(allowed = "mno",words = ['m', 'n', 'o', 'mn', 'no', 'om', 'mno', 'mon', 'nom', 'omn', 'nmo', 'nom', 'omn', 'mon', 'mno', 'mno', 'nom', 'omn', 'mon', 'mno', 'nom', 'omn', 'mon', 'mno', 'nom', 'omn', 'mon', 'mno', 'nom', 'omn', 'mon', 'mno']) == 32
    assert candidate(allowed = "abcdefghij",words = ['abcdefghij', 'abcdefghijk', 'abcdefghi', 'abcdefg', 'abcde', 'abcd', 'abc', 'ab', 'a', 'jihgfedcba', 'abcdefghijabcdefghij', 'abcdefghijabcdefghijk', 'abcdefghijabcdefghi', 'abcdefghijabcdefg', 'abcdefghijabcde', 'abcdefghijabcd', 'abcdefghijabc', 'abcdefghijab', 'abcdefghija']) == 17
    assert candidate(allowed = "ijkl",words = ['ij', 'kl', 'ik', 'jl', 'ikl', 'jkl', 'ijk', 'ijkl', 'ijl', 'ikjl', 'likj', 'ljk', 'lkij', 'lijk', 'ilkj', 'lkji']) == 16
    assert candidate(allowed = "xyz",words = ['xy', 'yz', 'xz', 'xyz', 'zyx', 'yxz', 'xzy', 'zy', 'yx', 'zx']) == 10
    assert candidate(allowed = "xyz",words = ['x', 'y', 'z', 'xy', 'xz', 'yz', 'xyz', 'xzy', 'yzx', 'zyx', 'zyz', 'zxz', 'yzy', 'xyx', 'xxy', 'xxz', 'xyy', 'xzz', 'yyy', 'yzz', 'zzz']) == 21
    assert candidate(allowed = "abcdefghij",words = ['abcdefghij', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'ab', 'cd', 'ef', 'gh', 'ij', 'abcd', 'efgh', 'ijkl', 'abcdefghi', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'abcdefghijk', 'abcdefghijj', 'abcdefghiij', 'abcdefghhij', 'abcdefghiiij']) == 31
    assert candidate(allowed = "xyz",words = ['xyzzy', 'zyx', 'zxyx', 'zzyzxzy', 'xyzabc', 'xzyz']) == 5
    assert candidate(allowed = "fv",words = ['f', 'v', 'fv', 'vf', 'ff', 'vv', 'ffff', 'vvvv', 'fvfv', 'vfvf', 'fvvf', 'vvff', 'fvff', 'vvvf', 'fvvv', 'ffvv', 'f', 'v', 'fv', 'vf', 'ff', 'vv', 'ffff', 'vvvv', 'fvfv', 'vfvf', 'fvvf', 'vvff', 'fvff', 'vvvf', 'fvvv', 'ffvv', 'f', 'v', 'fv', 'vf', 'ff', 'vv', 'ffff', 'vvvv']) == 40
    assert candidate(allowed = "qrst",words = ['qqqq', 'rrrr', 'ssss', 'tttt', 'qqrr', 'qqss', 'qqtt', 'rrss', 'rrtt', 'sstt', 'qqrrss', 'qqrrtt', 'qqsstt', 'rrsstt', 'qqrrsstt', 'qqrrssttt']) == 16
    assert candidate(allowed = "abcdefghij",words = ['abcdefghij', 'abcdefghi', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'abcdefghijabcdefghij', 'abcdefghijabcdefgh', 'abcdefghijabcdef', 'abcdefghijabcd', 'abcdefghijabc', 'abcdefghijab', 'abcdefghija']) == 17
    assert candidate(allowed = "xyz",words = ['xy', 'xz', 'yz', 'xyz', 'xx', 'yy', 'zz', 'xyx', 'yzy', 'zxz', 'xyxy', 'xzyz', 'yzxy', 'xyzx', 'xzyzx', 'yzxyz', 'xyzyx', 'zxyxz', 'yxzyz', 'zyxzy']) == 20
    assert candidate(allowed = "abcdef",words = ['a', 'b', 'c', 'd', 'e', 'f', 'ab', 'cd', 'ef', 'abc', 'def', 'abcdef', 'abcdefg', 'abcdefabc']) == 13
    assert candidate(allowed = "qrstuv",words = ['qrst', 'qrsu', 'rstuv', 'qrstu', 'quv', 'qrs', 'qrtuv', 'qru', 'quvtsr', 'quvz']) == 9
    assert candidate(allowed = "abcdef",words = ['abc', 'def', 'abcdef', 'aabbcc', 'ddeeff', 'abcdeff', 'abcdefg']) == 6
    assert candidate(allowed = "ijklmnop",words = ['ijkl', 'mnop', 'ijkm', 'klnm', 'ijlmo', 'ijkmnop', 'ijklmnopq', 'ijklmno', 'ijklnop']) == 8
    assert candidate(allowed = "jklmno",words = ['jk', 'kl', 'lm', 'mn', 'no', 'jkl', 'klm', 'lmn', 'mno', 'jklm', 'klmn', 'lmno', 'jklmo', 'klmno', 'jklmno', 'jklmnou', 'klmnop', 'jklmnop']) == 15
    assert candidate(allowed = "abcdef",words = ['abc', 'def', 'abcd', 'abef', 'acdf', 'bcde', 'acde', 'bcdf', 'abcf', 'abcdef', 'afecbd', 'fedcba']) == 12
    assert candidate(allowed = "qrst",words = ['q', 'r', 's', 't', 'qr', 'qs', 'qt', 'rs', 'rt', 'st', 'qrs', 'qrt', 'qst', 'rst', 'qrst']) == 15
    assert candidate(allowed = "wxyz",words = ['w', 'x', 'y', 'z', 'wx', 'wxyz', 'xy', 'yz', 'wxy', 'wxyz', 'wxzy', 'xywz', 'yzwx', 'zxyw']) == 14
    assert candidate(allowed = "abcd",words = ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'da', 'abc', 'bcd', 'cda', 'dab', 'abcd', 'bcda', 'cdab', 'dabc', 'abdc', 'bacd', 'cabd', 'dabc', 'acbd', 'badc', 'cabd', 'dacb', 'acdb', 'bdac', 'cadb', 'dbac', 'dcab', 'dcba']) == 30
    assert candidate(allowed = "xyz",words = ['xyzz', 'zyx', 'zxy', 'xxxyyyzzz', 'zzzz', 'yyyxxx', 'abc', 'xyzzyx', 'zzzxxx', 'xyxyxy']) == 9
    assert candidate(allowed = "abcdef",words = ['abc', 'def', 'abcdef', 'abcd', 'abcf', 'defa', 'bcde', 'fabc', 'aabbccdd', 'fedcba']) == 10
    assert candidate(allowed = "qz",words = ['qqqz', 'zqq', 'q', 'z', 'zzzz', 'qqqq', 'qzqz', 'zqzq', 'zzzq', 'zqqz']) == 10
    assert candidate(allowed = "xyz",words = ['xy', 'yz', 'xz', 'xyz', 'xzy', 'yxz', 'zxy', 'zyx', 'yzz', 'zzz']) == 10
    assert candidate(allowed = "jkl",words = ['j', 'k', 'l', 'jk', 'kl', 'lj', 'jkl', 'klj', 'lkj', 'kjl', 'jlk', 'lk', 'kj', 'jl', 'kl', 'jk', 'lj', 'kl', 'jl', 'kj', 'jl', 'kj', 'lk', 'jk', 'kl', 'jl', 'kj', 'lk', 'jk', 'kl', 'jl', 'kj']) == 32
    assert candidate(allowed = "mnopqr",words = ['mnop', 'mnopqr', 'mnopq', 'mnopqrs', 'mnopqrst', 'mnopqrstuv', 'mnopqrstu', 'mnopqrst', 'mnopqrstuvw', 'mnopqrstuvwx', 'mnopqrstuvwxy', 'mnopqrstuvwxyz', 'mno', 'pqrs', 'qrst', 'uvwx', 'vwxyz']) == 4
    assert candidate(allowed = "uvw",words = ['uvw', 'uv', 'uw', 'vw', 'u', 'v', 'w', 'uvvw', 'uwwv', 'vwwu', 'vvvuuuwww', 'wuvuvuvuv']) == 12
    assert candidate(allowed = "mnopqr",words = ['mnop', 'nopq', 'opqr', 'mnopq', 'nopqr', 'mnopqr', 'mnopqr', 'mnopqrs', 'mnopqrst', 'mnopqrstu', 'mnopqrstuv', 'mnopqrstuvw', 'mnopqrstuvwx', 'mnopqrstuvwxy', 'mnopqrstuvwxyz']) == 7
    assert candidate(allowed = "abcdefghij",words = ['abcde', 'fghij', 'abcdefghij', 'abcdefghi', 'efgij', 'hijabc', 'defghij', 'bcdefghij', 'abcdefghijk', 'ijabcdefgh', 'abcdeffghij', 'abcdefghijj', 'jihgfedcba', 'abcdefghijkk', 'abcdefghijjj']) == 13
    assert candidate(allowed = "abcdef",words = ['abc', 'def', 'abcdef', 'abcd', 'defg', 'fedcba', 'aabbccddeeff', 'zzzzz']) == 6
    assert candidate(allowed = "abcdefghij",words = ['abcdefghij', 'abcdefghi', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'abcdefghijk', 'abcdefghijj', 'abcdefghiij', 'abcdefghhij', 'abcdefghiiij', 'abcdefghijjj', 'abcdefghiiijj', 'abcdefghijjjj', 'abcdefghiiijjj', 'abcdefghijjjjj', 'abcdefghijjjjjj', 'abcdefghijjjjjjj', 'abcdefghijjjjjjjj', 'abcdefghijjjjjjjjj', 'abcdefghijjjjjjjjjj', 'abcdefghijjjjjjjjjjj', 'abcdefghijjjjjjjjjjjj', 'abcdefghijjjjjjjjjjjjj']) == 27
    assert candidate(allowed = "abcdefg",words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgi', 'abcdefgh', 'abcdefgabcdefg']) == 8
    assert candidate(allowed = "pqrstuvw",words = ['pqrs', 'qrst', 'rstu', 'stuv', 'tuvw', 'pqrsrstuvw', 'uvws', 'uvwpqr', 'rstuvwq', 'pqrstuvwz', 'uvwstu', 'qrpstu', 'vwstupqr']) == 12
    assert candidate(allowed = "pqrst",words = ['p', 'q', 'r', 's', 't', 'pq', 'qr', 'rs', 'st', 'pqrs', 'qrst', 'pqrst', 'pqrs', 'pqst', 'prst', 'qrstu', 'pqrstv']) == 15
    assert candidate(allowed = "tuvwxy",words = ['tu', 'tv', 'tw', 'tx', 'ty', 'tvwxy', 'uwxyt', 'wxtyv', 'xytuw', 'tuvxy', 'wxytv', 'xyzut', 'ytuvwx', 'uvxtyw', 'tuvwxyuvwx', 'txyuvw', 'ytxwuv', 'utxwvy', 'wxuytv', 'tvxyw', 'tuvwxytvwx', 'tuvwxytuvwxy']) == 21
    assert candidate(allowed = "lmnopq",words = ['lmn', 'opq', 'lmnop', 'lmnopq', 'pqonm', 'qlmnp', 'pqlno', 'opqmn', 'nopql', 'mnopq', 'lmnopqrr', 'plmqon', 'opqlnm', 'qponml', 'mnopql']) == 14
    assert candidate(allowed = "xyz",words = ['xx', 'yy', 'zz', 'xy', 'yz', 'zx', 'xyz', 'zxy', 'yxz']) == 9
    assert candidate(allowed = "xyz",words = ['xzy', 'zyx', 'zyzx', 'xxxyyyzzz', 'xzyxzyxzy']) == 5
    assert candidate(allowed = "mnopqrstuvwxyz",words = ['mnopqrstuvwxyz', 'mnopqrstuvwxy', 'mnopqrstuvwx', 'mnopqrstuvw', 'mnopqrstu', 'mnopqrst', 'mnopqrs', 'mnopqr', 'mnopq', 'mnop', 'mno', 'mn', 'm', 'nopqrstuvwxyz', 'opqrstuvwxy', 'pqrstuvwx', 'qrstuvw', 'rstuv', 'stuv', 'tuv', 'uv', 'v', 'mnopqrstuvwxyza', 'nopqrstuvwxyzb', 'mnopqrstuvwxc', 'mnopqrstuvxd', 'mnopqrstvxe', 'mnopqrsvxf', 'mnopqrvxg', 'mnopqruxh', 'mnopquxi', 'mnopqxi', 'mnopxi', 'mnoxi', 'moxi', 'moxi', 'oxi', 'oxi', 'oxiz', 'mnoxyz', 'mnopxyz', 'mnopqxyz', 'mnopqrxyz', 'mnopqrstxyz', 'mnopqrstuxyz', 'mnopqrstuvxyz', 'mnopqrstuvwxyz', 'mnopqrstuvwxyzabc', 'mnopqrstuvwxyzabcd', 'mnopqrstuvwxyzabcde', 'mnopqrstuvwxyzabcdef', 'mnopqrstuvwxyzabcdefg']) == 30
