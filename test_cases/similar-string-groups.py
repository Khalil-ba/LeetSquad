# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(strs = ['abc', 'bca', 'cab', 'cba', 'bac', 'acb']) == 1
    assert candidate(strs = ['ab', 'ba', 'abc', 'cab', 'bca']) == 1
    assert candidate(strs = ['aaaaa', 'aaabb', 'aaabc', 'aaaba', 'aaaaa']) == 1
    assert candidate(strs = ['tars', 'rats', 'arts', 'star']) == 2
    assert candidate(strs = ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']) == 1
    assert candidate(strs = ['abc', 'bca', 'cab', 'cba', 'acb', 'bac']) == 1
    assert candidate(strs = ['abcde', 'edcba', 'abced', 'decba', 'decab']) == 2
    assert candidate(strs = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yzw']) == 9
    assert candidate(strs = ['omv', 'ovm']) == 1
    assert candidate(strs = ['kite', 'peek', 'pink', 'pite', 'side', 'like', 'pipe', 'pike', 'lipk', 'kite', 'tape', 'pelt', 'pite', 'pink', 'pite']) == 1
    assert candidate(strs = ['aaa', 'aab', 'aba', 'baa', 'abb', 'bba', 'bab', 'bba', 'bbb', 'bbb']) == 1
    assert candidate(strs = ['aaaaaa', 'aaaabb', 'aaaabc', 'aaaaba', 'aaaaaa']) == 1
    assert candidate(strs = ['abc', 'bca', 'cab', 'acb', 'bac', 'cba']) == 1
    assert candidate(strs = ['abcdef', 'bcdefa', 'cdefab', 'defabc', 'efabcd', 'fabcde']) == 6
    assert candidate(strs = ['abcde', 'edcba', 'abced', 'deabc', 'decab', 'cdeab']) == 5
    assert candidate(strs = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']) == 1
    assert candidate(strs = ['a', 'a', 'a', 'a', 'a']) == 1
    assert candidate(strs = ['abcdefghijklmnopqrstuvwxyz', 'bcadefghijklmnopqrstuvwxyza', 'cdefghijklmnopqrstuvwxyzab']) == 3
    assert candidate(strs = ['aaaa', 'aada', 'aadaa', 'aadda', 'aaddd', 'adaaa', 'adaad', 'adaad', 'addaa', 'adada', 'adada', 'addaa', 'daaaa', 'daada', 'daada', 'dadaa', 'dadad', 'daada', 'dadaa', 'dadad', 'daada', 'ddaaa', 'ddada', 'ddaad', 'ddada', 'dddda']) == 1
    assert candidate(strs = ['zzzzzzzzzz', 'zzzzzzzzzy', 'zzzzzzzzzx', 'zzzzzzzzzw', 'zzzzzzzzzv', 'zzzzzzzzzu', 'zzzzzzzzzt', 'zzzzzzzzzs', 'zzzzzzzzzr', 'zzzzzzzzzq']) == 1
    assert candidate(strs = ['mnopqr', 'nopqmr', 'opqmnr', 'pqomnr', 'qpomnr', 'mnopqr', 'mnopqr', 'mnopqr', 'mnopqr', 'mnopqr', 'mnopqr', 'mnopqr', 'mnopqr', 'mnopqr', 'mnopqr', 'mnopqr', 'mnopqr', 'mnopqr', 'mnopqr', 'mnopqr']) == 3
    assert candidate(strs = ['abcde', 'edcba', 'abced', 'decba', 'decab', 'abcde', 'edcba', 'abced', 'decba', 'decab']) == 2
    assert candidate(strs = ['abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij']) == 1
    assert candidate(strs = ['abcdefgh', 'bcdefgha', 'cdefghab', 'defghabc', 'efghabcd', 'fghabcde', 'ghabcdef', 'habcdefg']) == 8
    assert candidate(strs = ['zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz']) == 1
    assert candidate(strs = ['abcdeabcde', 'edcbaedcba', 'abcedabced', 'decbaedcba', 'decabdecab', 'abcdeabced', 'abcdeabcdx']) == 3
    assert candidate(strs = ['abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik', 'abcdefghik']) == 1
    assert candidate(strs = ['aabbcc', 'ccaabb', 'bbaacc', 'aabbbc', 'bcaabb', 'abcabc', 'babcac', 'cabcab', 'bacbac', 'acbacb', 'acbbac', 'abacbc', 'cababc', 'cbaabc', 'acabbc', 'bcabac', 'abcbac', 'cabbac', 'bcacab', 'acbbca']) == 1
    assert candidate(strs = ['qwertyuiop', 'qeywrtuiop', 'qwrtypuioe', 'qwertyuiop', 'qwertyuipo']) == 3
    assert candidate(strs = ['abcabcabcabc', 'cbacbacbacba', 'bacbacbacbac', 'abcabcabcacb', 'cbacbacbacac', 'bacbacbacabc', 'abcabcabcaba', 'cbacbacbacad', 'bacbacbacaba', 'abcabcabcaca', 'cbacbacbacad', 'bacbacbacaca', 'abcabcabacba', 'cbacbacbacba', 'bacbacbacacb', 'abcabcabcabc', 'cbacbacbacac', 'bacbacbacabc']) == 3
    assert candidate(strs = ['abacabad', 'babadaba', 'bacabada', 'acabadab', 'adabacab', 'cabadaba', 'abadabac', 'badabaca']) == 4
    assert candidate(strs = ['abcdefghij', 'abcdefghji', 'abcdefghif', 'abcdefghig', 'abcdefghih']) == 1
    assert candidate(strs = ['abcdefghij', 'abcdefghik', 'abcdefghil', 'abcdefghim', 'abcdefghin', 'abcdefghio']) == 1
    assert candidate(strs = ['xyzzxy', 'zyxzyx', 'zzzyxy', 'zyzzxz', 'xyzzzx', 'zyxzyy', 'zyzzxy', 'zyzzxy']) == 1
    assert candidate(strs = ['abcdefg', 'gfedcba', 'fedcbag', 'gabcdef', 'bacdefg', 'gfeabcd', 'bcdefga', 'gfabcde', 'gefedcb', 'defgabc', 'gdefcab', 'fgedcba', 'gfabced', 'gfadebc', 'gbafced', 'gfacedb', 'gfebacd', 'gfbaced', 'gfbcdea', 'gfbedac', 'gfeadcb', 'gfecdba', 'gfdbeca', 'gfdecba']) == 13
    assert candidate(strs = ['abcdefghij', 'abcdefghik', 'abcdefghil', 'abcdefghim', 'abcdefghin']) == 1
    assert candidate(strs = ['abcdefgh', 'abcdefgh', 'bcdefgha', 'cdefghab', 'defghabc', 'efghabcd', 'fghabcde', 'ghabcdef', 'habcdefg', 'abcdefgha', 'abcdefghb', 'abcdefghc', 'abcdefghd', 'abcdefghi', 'abcdefghj']) == 8
    assert candidate(strs = ['abcdefgh', 'abcdefgh', 'aefghbcd', 'bcdefgha', 'ghabcdef', 'hgfedcba', 'abcdefgh']) == 5
    assert candidate(strs = ['xyzxyz', 'yzxyxz', 'zxyxyz', 'xyxzyz', 'yxzxzy', 'zxzyxy', 'xzyzxy', 'zyxzyx']) == 6
    assert candidate(strs = ['abcde', 'abced', 'abdec', 'abdec', 'abced', 'abcde', 'abced', 'abdec', 'abced', 'abcde', 'abced', 'abdec', 'abced', 'abcde', 'abced', 'abdec', 'abced', 'abcde']) == 1
    assert candidate(strs = ['abcdefghij', 'jihgfedcba', 'abcdefghij', 'abcdefghik', 'abcdefghil', 'abcdefghij', 'abcdefghim', 'abcdefghij', 'abcdefghin', 'abcdefghio']) == 2
    assert candidate(strs = ['abcdefg', 'bacdefg', 'cbadefg', 'dcabefg', 'edcabfg', 'fedcabc', 'gfedcab', 'hgfedca']) == 6
    assert candidate(strs = ['abcdefghij', 'bacdefghij', 'cabdefghij', 'abcdfehgij', 'abcdefghij', 'abcdefghik', 'abcdefghji']) == 2
    assert candidate(strs = ['abcd', 'dcba', 'cdab', 'bacd', 'cabd', 'acdb', 'adcb', 'bcda', 'cdba', 'bdca', 'dacb', 'cadb', 'bdac', 'abcd', 'dcba', 'cdab', 'bacd', 'cabd', 'acdb', 'adcb', 'bcda', 'cdba', 'bdca', 'dacb', 'cadb', 'bdac']) == 1
    assert candidate(strs = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'abc', 'acb', 'bac', 'bca', 'cab', 'cba', 'abc', 'acb', 'bac', 'bca', 'cab', 'cba']) == 1
    assert candidate(strs = ['aaaaabbbbb', 'aaaabbbbba', 'aaabbbbaaa', 'aabbbbaaaa', 'abbbbaaaaa', 'baaaaabbbb', 'baaaaabbbb', 'bbbbbaaaaa', 'bbbbbaaaab', 'bbbbbaaabb', 'bbbbbaabba', 'bbbbbaabbb', 'bbbbabbbbb', 'bbbbbaabaa', 'bbbbaabbbb', 'bbaaaaabbb', 'bbaaaabbbb', 'bbaaabbbbb', 'bbbaaaaabb', 'bbbaaaabbb', 'bbbaaabbbb', 'bbbbaaaabb', 'bbbbaaabbb', 'bbbbaabbbb', 'bbbbbaaaab', 'bbbbbaaabbb', 'bbbbbaabbb', 'bbbbabbbba', 'bbbbabbaaa', 'bbbbbaabaa', 'bbbbbaaabb', 'bbbbaaaaaa', 'bbbbaaaaba', 'bbbbaaabaa', 'bbbbaaabab', 'bbbbaaabra', 'bbbbbaaaaa', 'bbbbbaaaab', 'bbbbbaaaba', 'bbbbbaabaa', 'bbbbbaaabb']) == 1
    assert candidate(strs = ['abcd', 'acbd', 'adbc', 'cabd', 'dbca', 'dcba', 'dcab']) == 1
    assert candidate(strs = ['abababab', 'babababa', 'aabbaabb', 'bbaabbaa', 'abbaabba', 'baabbaab', 'abbaabba', 'baabbaab', 'bbaabbaa', 'aabbaabb', 'babababa', 'abababab']) == 6
    assert candidate(strs = ['lkjhgfedcba', 'lkjhgfedcba', 'lkjhgfedcba', 'lkjhgfedcba', 'lkjhgfedcba']) == 1
    assert candidate(strs = ['abcde', 'edcba', 'dbeca', 'decba', 'decab', 'cedab', 'aebcd', 'bcdea', 'debac', 'baced', 'acebd', 'bdeca', 'acdeb', 'bacde', 'abced', 'decba', 'edabc', 'abcde', 'acbde', 'baced', 'bcaed']) == 5
    assert candidate(strs = ['qwertyuiop', 'wertyuiopq', 'ertyuiopqw', 'rtyuiopqwe', 'tyuiopqrst', 'yuiopqrstu', 'uiopqrstuv', 'iopqrstuvw', 'opqrstuvwx', 'pqrstuvwxy', 'qrstuvwxyz', 'rstuvwxyzp', 'stuvwxyzpr', 'tuvwxyzprs', 'uvwxyzprst', 'vwxyzprstq', 'wxyzprstqu', 'xyzprstquv', 'yzprstquvx', 'zprstquvxy', 'prstquvxyz', 'rstquvxyza', 'stquvxyzab', 'tquvxyzabc', 'quvxyzabcd', 'uvxyzabcde', 'vxyzabcdef', 'xyzabcdefg', 'yzabcdefgq', 'zabcdefgqr', 'abcdefgqrs', 'bcdefgqrst', 'cdefgqrstu', 'defgqrstuv', 'efgqrstuvw', 'fgqrstuvwxyz', 'gqrstuvwxyzx', 'hqrstuvwxyzx', 'qrstuvwxyzxy', 'rstuvwxyzxyq', 'stuvwxyzxyqp', 'tuvwxyzxyqpr', 'uvwxyzxyqprs', 'vwxyzxyqprst', 'wxyzxyqprstu', 'xyzxyqprstuv', 'yzxyqprstuvw', 'zxyqprstuvwx', 'xyqprstuvwxy', 'yqprstuvwxyz', 'qprstuvwxyzx', 'prstuvwxyzxy', 'rstuvwxyzxyz', 'stuvwxyzxyza', 'tuvwxyzxyqza']) == 44
    assert candidate(strs = ['abcdefg', 'gfedcba', 'bacdefg', 'abcdefg', 'gfedcbx', 'abcdefg', 'gfedcbw']) == 2
    assert candidate(strs = ['aabbccddeeff', 'ffeeddccbaaa', 'aabbccddeeff', 'ffeeddccbaaa', 'aabbccddeeff', 'ffeeddccbaaa', 'aabbccddeeff', 'ffeeddccbaaa', 'aabbccddeeff', 'ffeeddccbaaa', 'aabbccddeeff', 'ffeeddccbaaa', 'aabbccddeeff', 'ffeeddccbaaa', 'aabbccddeeff', 'ffeeddccbaaa', 'aabbccddeeff', 'ffeeddccbaaa', 'aabbccddeeff', 'ffeeddccbaaa', 'aabbccddeeff', 'ffeeddccbaaa', 'aabbccddeeff', 'ffeeddccbaaa', 'aabbccddeeff', 'ffeeddccbaaa', 'aabbccddeeff', 'ffeeddccbaaa', 'aabbccddeeff', 'ffeeddccbaaa']) == 2
    assert candidate(strs = ['ababab', 'bababa', 'bbaaab', 'aababb', 'ababba', 'abbaab', 'aabbab', 'ababab', 'aabbaa']) == 1
    assert candidate(strs = ['aaaaaaaa', 'aaaaabaa', 'aaaabaab', 'aaabaaba', 'aabaaaba', 'abaabaaa', 'baaaaaab', 'baaabaaa', 'baabaaab', 'babaaaaa', 'abaaaaab', 'abaaabaa', 'abaabaab', 'baabaaba', 'aabaaaba', 'aaabaaba', 'baaabaaa', 'baaaaaab', 'abaaaaab', 'baaaabaa', 'aabaaaba', 'abaabaab', 'baabaaba', 'aabaaaba', 'baaaabaa', 'baaaaaab', 'abaaaaab', 'abaabaab', 'baabaaba', 'aabaaaba', 'baaaabaa', 'baaaaaab', 'abaaaaab', 'abaabaab', 'baabaaba', 'aabaaaba', 'baaaabaa', 'baaaaaab', 'abaaaaab']) == 1
    assert candidate(strs = ['abcdefghij', 'jihgfedcba', 'abcdefghij', 'ijhgfedcba', 'abcdefghij', 'jihgfedcba', 'abcdefghij', 'ijhgfedcba']) == 2
    assert candidate(strs = ['abacax', 'aacxab', 'abacax', 'bacaxa', 'cacxab', 'abcaxa']) == 3
