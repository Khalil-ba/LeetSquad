# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(words = ['abc', 'abcabc', 'bc', 'abcabcabc']) == 3
    assert candidate(words = ['xyz', 'xyzxyz', 'zyx', 'z', 'x']) == 1
    assert candidate(words = ['hello', 'hellohello', 'hellohellohello']) == 3
    assert candidate(words = ['z', 'zaz', 'zzz', 'zazaz']) == 4
    assert candidate(words = ['aaa', 'aaaa', 'aaaaa', 'aa', 'a']) == 3
    assert candidate(words = ['cat', 'tac', 'catcat', 'tacatc']) == 1
    assert candidate(words = ['prefix', 'prefixprefix', 'fixpre', 'refixpre']) == 1
    assert candidate(words = ['repeat', 'repeattorepeat', 'eat', 'eateateat']) == 2
    assert candidate(words = ['suffix', 'suffixsuffix', 'fixsuf', 'ffixsuf']) == 1
    assert candidate(words = ['pa', 'papa', 'ma', 'mama']) == 2
    assert candidate(words = ['m', 'mnm', 'nmn', 'mnmnm']) == 3
    assert candidate(words = ['test', 'testing', 'testtest', 'sett']) == 1
    assert candidate(words = ['y', 'yxy', 'xyx', 'yxyxy']) == 3
    assert candidate(words = ['hello', 'hellohello', 'world', 'worldworld']) == 2
    assert candidate(words = ['x', 'xx', 'xxx', 'xxxx']) == 6
    assert candidate(words = ['z', 'zzz', 'zzzzz', 'zzzzzzz']) == 6
    assert candidate(words = ['dog', 'dogcat', 'dogcatdog']) == 1
    assert candidate(words = ['a', 'aba', 'ababa', 'aa']) == 4
    assert candidate(words = ['t', 'tt', 'ttt', 'tttt', 'ttttt', 'tttttt']) == 15
    assert candidate(words = ['aabb', 'aabbcc', 'aabbccaabb']) == 1
    assert candidate(words = ['abc', 'abcabc', 'ab', 'a']) == 1
    assert candidate(words = ['z', 'zzz', 'zzzz', 'zzzzz']) == 6
    assert candidate(words = ['abab', 'ab']) == 0
    assert candidate(words = ['x', 'xx', 'xxx', 'xxxx']) == 6
    assert candidate(words = ['s', 'ss', 'sss', 'ssss', 'sssss']) == 10
    assert candidate(words = ['a', 'b', 'c', 'd']) == 0
    assert candidate(words = ['hello', 'hellohello', 'lohel', 'ohelloh']) == 1
    assert candidate(words = ['test', 'testtest', 'sttes', 'ttest']) == 1
    assert candidate(words = ['abc', 'abcabc', 'abcabcabc']) == 3
    assert candidate(words = ['abc', 'abcabc', 'bcb', 'bcbcbcb']) == 2
    assert candidate(words = ['xy', 'xyxy', 'yxyx', 'xyxyxy', 'yxyxyx', 'xyxyxyxy', 'yxyxyxyx', 'xyxyxyxyxy']) == 13
    assert candidate(words = ['abc', 'cab', 'bac', 'abcabc', 'abcabcabc', 'cababcabc', 'bacbacbac']) == 4
    assert candidate(words = ['abab', 'baba', 'ab', 'ba', 'aba', 'bab', 'ababab', 'bababa', 'abababa', 'bababab', 'abababab', 'babababa']) == 12
    assert candidate(words = ['ab', 'baba', 'abab', 'bababa', 'ababab', 'babababa', 'abababab', 'bababababa']) == 12
    assert candidate(words = ['abab', 'baba', 'ababa', 'babab', 'ababab', 'bababa', 'abababa', 'bababab', 'abababab', 'babababa']) == 8
    assert candidate(words = ['noon', 'noonnoon', 'noonnoonnoon', 'noonoonoonnoon', 'noonnoonnoonnoon']) == 7
    assert candidate(words = ['aabb', 'bbaa', 'aabbcc', 'ccaabb', 'aabbccaabb', 'bbaaabbbaa', 'ccaabbaacc']) == 2
    assert candidate(words = ['aaaaa', 'baaaaa', 'caaaaa', 'daaaaa', 'eaaaaa', 'faaaaa', 'baaaaaa', 'caaaaaa']) == 0
    assert candidate(words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz', 'zzzzzzz']) == 21
    assert candidate(words = ['aabb', 'aabbcc', 'aabbccaabb', 'aabbccaabbcc', 'aabbccaabbccaabb', 'aabbccaabbccaabbcc']) == 6
    assert candidate(words = ['abcde', 'abcdeabcde', 'bcdeabcde', 'cdeabcde', 'deabcde', 'eabcde', 'abcdeabcdeabcde']) == 3
    assert candidate(words = ['ababab', 'bababa', 'abab', 'baba', 'aba', 'ba', 'a', 'b', 'ab', 'ba', 'aba', 'bab', 'abb', 'bba']) == 4
    assert candidate(words = ['ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']) == 0
    assert candidate(words = ['abc', 'cab', 'bac', 'abcabc', 'bcabc', 'abcabcabc']) == 3
    assert candidate(words = ['aaaa', 'aaa', 'aa', 'a', 'abcabcabc', 'abcabc', 'abc', 'ab', 'a', 'abcabcabcabc', 'abcabcabcabcabcabcabc', 'abcabcabcabcabc', 'abcabcabcabcabcabcabcabcabc', 'abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc', 'abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc']) == 33
    assert candidate(words = ['pqr', 'pqrpqr', 'qrpqrpqr', 'rpqrpqrpqr', 'pqrpqrpqr', 'qrpqrpqr', 'rpqrpqrpqr', 'pqrpqrpqr']) == 8
    assert candidate(words = ['aba', 'abacaba', 'cabacabac', 'abcabcabc']) == 1
    assert candidate(words = ['abcabc', 'abc', 'abcabcabc', 'abca', 'abcb', 'abcab', 'abcabcab', 'a', 'aa', 'aaa']) == 6
    assert candidate(words = ['racecar', 'racecaracecar', 'car', 'racecaracecaracecar']) == 3
    assert candidate(words = ['xyz', 'xyzxyz', 'xyzxyzxyz', 'xyxzyx', 'xyzzyx']) == 3
    assert candidate(words = ['zzz', 'zzzz', 'zzzzz', 'zzzzzz', 'zzzzzzz', 'zzzzzzzz']) == 15
    assert candidate(words = ['aaaa', 'aaa', 'aa', 'a', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa', 'aaaaaab', 'aaaaaaab', 'aaaaaaaab']) == 30
    assert candidate(words = ['mama', 'mamama', 'mamamama', 'ma', 'm', 'mam', 'mamam', 'mamama', 'mamamam', 'mamamama']) == 17
    assert candidate(words = ['aaa', 'aaaa', 'aaaaa', 'aa', 'a', 'aaaaaa', 'aaaaaaa']) == 14
    assert candidate(words = ['test', 'testtest', 'tset', 'sett', 'sttest', 'testset']) == 1
    assert candidate(words = ['ababab', 'bababa', 'ab', 'aba', 'baba', 'bababab', 'bababa', 'abab', 'bab']) == 3
    assert candidate(words = ['repeat', 'peatre', 'eatrep', 'atrep', 'trepeat', 'peatpeatpeat']) == 0
    assert candidate(words = ['xyzzyx', 'zyxzyxzyx', 'xyzzyxzyxzyx', 'zyxzyxzyxzyxzyx', 'xyzzyxzyxzyxzyxzyx']) == 1
    assert candidate(words = ['abcd', 'dcba', 'cdab', 'abcdabcd', 'cdabcdcd', 'dcabcd', 'abcdabdc', 'abcdabcdabcd']) == 3
    assert candidate(words = ['mnop', 'mnopm', 'nopmnop', 'mnopm', 'mnopm', 'mnopmnopm', 'nopmnopm', 'mnopmnopm', 'mnopmnopmnop', 'mnopmnopmnopm', 'nopmnopmnopm']) == 17
    assert candidate(words = ['xyz', 'xyzyx', 'zyxzyxzyx', 'zxzyx', 'xyzxyzxyz', 'xyzzyxzyxzyx']) == 1
    assert candidate(words = ['hello', 'hellohello', 'hell', 'hellohellohello', 'lohel']) == 3
    assert candidate(words = ['mnop', 'opmnop', 'nopmnop', 'mnopmnop', 'opmnopmnop', 'nopmnopnop', 'mnopmnopmnop']) == 4
    assert candidate(words = ['abcabc', 'abc', 'bcabc', 'abcabcabc', 'abcabca']) == 2
    assert candidate(words = ['pqr', 'pqrpqr', 'pqrpqrpqr', 'pqrpqrpqrpqr', 'pqrpqrpqrpqrpqr', 'pqrpqrpqrpqrpqrpqr', 'pqrpqrpqrpqrpqrpqrpqr']) == 21
    assert candidate(words = ['abcabcabc', 'bcabcabcab', 'cabcabcab', 'abcabc', 'bcabc', 'cabc', 'abc', 'bc', 'c']) == 0
    assert candidate(words = ['aaa', 'aaabaaa', 'baaabaaa', 'aaabaaba', 'abaabaaa', 'aaabaaba', 'baaabaaa']) == 3
    assert candidate(words = ['abcdabcd', 'abcd', 'abcde', 'abcdeabcd', 'abcdeabcde']) == 2
    assert candidate(words = ['hello', 'hellohello', 'hellohellohello', 'world', 'worldworld', 'worldworldworld']) == 6
    assert candidate(words = ['aaaa', 'aa', 'a', 'aaaaaa', 'aaa']) == 5
    assert candidate(words = ['abcd', 'abcdabcd', 'abcdabcdabcd', 'abcdabcdabcdabcd', 'abcdabcdabcdabcdabcd']) == 10
    assert candidate(words = ['xyz', 'xyzxyz', 'xyzxyzxyz', 'xy']) == 3
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']) == 10
    assert candidate(words = ['same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same', 'same']) == 45
    assert candidate(words = ['aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa']) == 21
    assert candidate(words = ['aaaa', 'aa', 'a', 'aaaaaa', 'aaa', 'aaaaaaa']) == 10
    assert candidate(words = ['xyz', 'xyzxyz', 'xyzxyzxyz', 'xy', 'xyxy', 'xyxyxy']) == 6
    assert candidate(words = ['abcd', 'cdabcd', 'abcdabcd', 'abcdabcdabcd', 'dabcdabcd']) == 3
    assert candidate(words = ['zzz', 'zzzz', 'zzzzz', 'zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzzz', 'zzzzzzzzzzzz', 'zzzzzzzzzzzzz']) == 55
    assert candidate(words = ['aabbcc', 'aabb', 'cc', 'aabbccaabbcc', 'aabbccaa', 'bbccaa']) == 1
    assert candidate(words = ['ab', 'abcba', 'abcabcba', 'a', 'aba', 'abababa']) == 3
    assert candidate(words = ['abacaba', 'aba', 'abacababa', 'a']) == 1
    assert candidate(words = ['xyz', 'xyzyx', 'xyzxyz', 'xyzxyzyx', 'xyzxyzyxyz']) == 2
    assert candidate(words = ['level', 'levellevel', 'levellevellevel', 'llevevllevevllevell']) == 3
    assert candidate(words = ['xyxy', 'yxyx', 'xyxyxy', 'yxyxyx', 'xyxyxyxy', 'yxyxyxyx', 'xyxyxyxyxy', 'yxyxyxyxyx']) == 12
    assert candidate(words = ['ab', 'aba', 'abab', 'ababa', 'abababa', 'ababababa', 'abababababa', 'ababababababa', 'abababababababa', 'ababababababababa', 'abababababababababa']) == 37
    assert candidate(words = ['xyz', 'xyzxyz', 'zyxzyx', 'xyzzyxxyz', 'xyz']) == 3
    assert candidate(words = ['aaa', 'aaaa', 'aaaaa', 'aaaaaa']) == 6
    assert candidate(words = ['abc', 'cab', 'bac', 'abcabc', 'abcabcabc', 'abcabcabcabc']) == 6
    assert candidate(words = ['abcabc', 'abc', 'abcabcabc', 'a', 'aa', 'aaa', 'aaaa']) == 8
    assert candidate(words = ['aaa', 'aa', 'a', 'aaaa', 'aaaaa']) == 7
    assert candidate(words = ['ab', 'abc', 'ababc', 'abcababc']) == 1
    assert candidate(words = ['p', 'pp', 'ppp', 'pppp', 'ppppp', 'pppppp', 'ppppppp']) == 21
    assert candidate(words = ['xyz', 'xyzyx', 'xyzxyz', 'zyxzyxzyx']) == 1
    assert candidate(words = ['zzz', 'zzzz', 'zz', 'z', 'zzzzz', 'zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz', 'zzzzzzzzzz']) == 40
    assert candidate(words = ['ab', 'aba', 'abab', 'ababa', 'ababab', 'abababa']) == 6
    assert candidate(words = ['deified', 'deifieddeified', 'deifieddeifieddeified', 'deifieddeifieddeifieddeified', 'deifieddeifieddeifieddeifieddeified']) == 10
    assert candidate(words = ['abcdabcd', 'abcdeabcde', 'abcdefabcdef', 'abcd', 'abcde', 'abcdef', 'abc', 'ab', 'a', 'ababab', 'abcabcabc']) == 2
    assert candidate(words = ['xyz', 'xyzxyz', 'xyzxyzxyz', 'xyx']) == 3
    assert candidate(words = ['pqr', 'pqrpqr', 'rpqrpqr', 'pqrpqrpqr', 'qpqrpqrpqr', 'pqrqpqrpqrpqr', 'pqrpqrpqrpqr', 'rpqrpqrpqrpqr', 'pqrpqrpqrpqrpqr', 'qpqrpqrpqrpqrpqr']) == 12
    assert candidate(words = ['abcd', 'abcdabcd', 'abcde', 'abcdeabcde', 'ab', 'abab', 'abc', 'abcabc', 'a', 'aaaa']) == 5
    assert candidate(words = ['xyz', 'xyzxyz', 'xyzxyzxyz', 'xyzxyzxyzxyz']) == 6
    assert candidate(words = ['abcd', 'abcdabcd', 'bcdabcde', 'cdabcde', 'dabcde', 'abcde']) == 1
    assert candidate(words = ['mnop', 'nopm', 'opmn', 'pqrs', 'rspq', 'srpq', 'qpsr', 'mnopmnop', 'nopmnopm', 'opmnopno']) == 2
    assert candidate(words = ['x', 'xx', 'xxx', 'xxxx', 'xxxxx', 'xxxxxx', 'xxxxxxx', 'xxxxxxxx', 'xxxxxxxxx', 'xxxxxxxxxx']) == 45
    assert candidate(words = ['hello', 'hellohello', 'hellohellohello', 'hellohellohellohello', 'hellohellohellohellohello']) == 10
    assert candidate(words = ['radar', 'radarradar', 'radarradarradar', 'radarradarradarradar', 'radarradarradarradarradar']) == 10
    assert candidate(words = ['pqr', 'pqrpqr', 'pq', 'pqpq', 'prq', 'prqprq', 'pr', 'prpr', 'qpr', 'qprqpr']) == 5
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa']) == 28
    assert candidate(words = ['abc', 'bac', 'cab', 'abcabc', 'bacbac', 'cabcab', 'abcabca', 'bcabcabc', 'cababcab', 'abcabcabca']) == 5
    assert candidate(words = ['abc', 'abca', 'abcabc', 'cabcabc']) == 1
    assert candidate(words = ['abcabc', 'abc', 'abcabcabcabc', 'abcabcabc', 'abcabcabcabcabcabc']) == 8
    assert candidate(words = ['rotor', 'rotorrotor', 'rotorrotorrotor', 'torotorotor']) == 3
    assert candidate(words = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop']) == 0
    assert candidate(words = ['aabb', 'bbaa', 'aabbcc', 'ccbaab', 'aabbccbaab']) == 0
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa']) == 15
    assert candidate(words = ['ababab', 'ab', 'abab', 'abababab', 'baba', 'abababa']) == 4
    assert candidate(words = ['xy', 'xyxy', 'xyxyxy', 'xyxyxyxy', 'xyxyxyxyxy']) == 10
    assert candidate(words = ['banana', 'ban', 'banana', 'nan', 'banananan', 'ananan']) == 1
