# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(words = ['abcd', 'abdc', 'cdab', 'cdba', 'dcba', 'bacd']) == 4
    assert candidate(words = ['abcd', 'abdc', 'cdab', 'cdba']) == 3
    assert candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr']) == 6
    assert candidate(words = ['aabb', 'bbaa', 'abab', 'baba', 'abba', 'baab']) == 3
    assert candidate(words = ['aabb', 'abab', 'baba', 'bbaa', 'abba', 'baab']) == 3
    assert candidate(words = ['abcde', 'edcba', 'acebd', 'decab', 'bdeca', 'cabed']) == 4
    assert candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']) == 3
    assert candidate(words = ['abcde', 'abced', 'adcbe', 'aebcd', 'eabcd', 'ebacd']) == 5
    assert candidate(words = ['aabb', 'bbaa', 'abab', 'baba', 'aaaa', 'bbbb']) == 5
    assert candidate(words = ['abcd', 'cdab', 'cbad', 'xyzz', 'zzxy', 'zzyx']) == 3
    assert candidate(words = ['abcde', 'edcba', 'abced', 'decba']) == 2
    assert candidate(words = ['aabb', 'bbaa', 'abab', 'baba']) == 3
    assert candidate(words = ['mnopqr', 'nopqr', 'opqr', 'pqr', 'qr', 'r', 'mnopqrs', 'nopqrs', 'opqrs', 'pqr', 'qr', 'r', 'mnopqrst', 'nopqrst', 'opqrst', 'pqrst', 'qrst', 'rst', 'st', 't']) == 17
    assert candidate(words = ['abcdeabcde', 'cdeabcdeab', 'deabcdeabc', 'eabcdeabcd', 'abcdecdeab', 'bacdecdeba', 'cabdecdeab', 'cbadecdeba', 'abcdefedcb', 'fedcbaedcb', 'gfedcbedcb', 'bacdefedcb', 'defabcdecb', 'cabfedecba', 'cbafedecba', 'dcbaefdcba', 'efabcdecba', 'fedcbaecba', 'gfedcbedcb', 'bacdefecba']) == 12
    assert candidate(words = ['abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij']) == 1
    assert candidate(words = ['xxyyzz', 'yyzzxx', 'zzxxyy', 'yxzyxz', 'yzyxzx', 'zyzyyx', 'zyxzyx', 'xyzzyx']) == 3
    assert candidate(words = ['aabbcc', 'bbaacc', 'ccabba', 'aabbcc', 'bbaacc', 'ccabba', 'aabbcc', 'bbaacc']) == 1
    assert candidate(words = ['aabbcc', 'bbaacc', 'ababcc', 'babcac', 'cabcab', 'acbacb']) == 3
    assert candidate(words = ['zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz', 'zzzzzzzzzz']) == 1
    assert candidate(words = ['abcdef', 'bacdef', 'decfab', 'fedcba', 'fedbac', 'defacb']) == 6
    assert candidate(words = ['aabbccddeeff', 'bbaaccddeeff', 'aacbbddeeff', 'ddffeeaabbbc', 'effeeddabbcc', 'bbccddfeea', 'ccddeeffaabb', 'effddcbaabbb']) == 6
    assert candidate(words = ['abcdefg', 'gfedcba', 'bdfhace', 'fhdbaec', 'acegfb', 'bfhacd', 'fhbdcae', 'gacfbde']) == 7
    assert candidate(words = ['xyzzxy', 'zzxyxy', 'zxyzyx', 'xyzyzx', 'zyxzyx', 'yxzyxz', 'zyxzyx', 'zxzyzx']) == 5
    assert candidate(words = ['xyxzyxzyx', 'yxzyxzyxy', 'xzyxzyxzy', 'zyxzyxzyx', 'yxyxzyxzy', 'xyzzyxzyx']) == 4
    assert candidate(words = ['aabbcc', 'bbaacc', 'abacbc', 'babcac', 'aabbccdd', 'ddccbb', 'abcdabcd', 'cdabcdab', 'abcdabdc', 'abcdabcd', 'abcdabcd', 'abcdabcd', 'abcdabcd', 'abcdabcd', 'abcdabcd', 'abcdabcd', 'abcdabcd', 'abcdabcd', 'abcdabcd', 'abcdabcd']) == 7
    assert candidate(words = ['abcdefghij', 'abcdefghji', 'jihgfedcba', 'ihgfedcbaj', 'jihgfedabc', 'abcdefghij', 'cbadefghij']) == 3
    assert candidate(words = ['aaaabbbb', 'bbbaaa', 'abababab', 'babaabab', 'bababaab', 'abababba']) == 5
    assert candidate(words = ['abcdabcd', 'cdabcdab', 'bacdbacd', 'dcbadabc', 'badcabcd', 'dcababcd', 'abcdadcb']) == 5
    assert candidate(words = ['abcdef', 'fedcba', 'gfedcb', 'bacdef', 'defabc', 'cabfed', 'cbafed', 'dcbaef', 'efabcd', 'fedabc', 'gfedcb', 'bacdef', 'defabc', 'cabfed', 'cbafed', 'dcbaef', 'efabcd', 'fedabc', 'gfedcb', 'bacdef']) == 5
    assert candidate(words = ['abcdefghij', 'bacdefghij', 'cbadefghij', 'abcdefghij', 'ijabcdefgh', 'hgfedcba', 'abcdefghij', 'bacdefghij']) == 3
    assert candidate(words = ['aabbcc', 'bbaaccaabb', 'ababcc', 'aabcbcba', 'ccbaab', 'bccabaab', 'abccbaab', 'baccbaab', 'aabbccba', 'bbaabbcc']) == 7
    assert candidate(words = ['abcdabcd', 'cdabcdab', 'cbadabcd', 'xyzzxyzz', 'zzxyzzxy', 'zzyxzzyx']) == 3
    assert candidate(words = ['abac', 'baca', 'caba', 'acba', 'abca', 'baca', 'caba', 'acba']) == 4
    assert candidate(words = ['abcdef', 'bacdef', 'cbadef', 'abcdefg', 'gfedcba', 'fedcbag', 'gfedabc', 'gfdecba']) == 5
    assert candidate(words = ['abcdefgh', 'ghfedcba', 'abcdghfe', 'bacdefgh', 'hgfedcba', 'abcdefgh', 'ghfedcba', 'bacdefgh']) == 5
    assert candidate(words = ['aabbcc', 'bbaacc', 'abacbc', 'accabb', 'abcabc', 'cbaabc']) == 2
    assert candidate(words = ['mnopqr', 'qrpmno', 'pqmron', 'opmqrn', 'rnmqpo', 'nqrpom', 'mnopqr', 'qrpmno', 'pqmron', 'opmqrn', 'rnmqpo', 'nqrpom']) == 6
    assert candidate(words = ['abcdef', 'acbedf', 'abefcd', 'efabcd', 'cbadef', 'fedcba']) == 3
    assert candidate(words = ['abcdefghij', 'jihgfedcba', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij', 'abcdefghij']) == 2
    assert candidate(words = ['abcde', 'edcba', 'deabc', 'cdeab', 'bcdea', 'aebcd', 'abced', 'bcdea', 'cdeab', 'deabc', 'edcba', 'abcde']) == 4
    assert candidate(words = ['abcdefg', 'bacdefg', 'cbadefg', 'dcbaefg', 'edcbafg', 'fedcgb', 'gfedcba']) == 4
    assert candidate(words = ['aabbccddeeff', 'bbaaccddeeff', 'aacbbddeeff', 'deeffaabbcc', 'efdeaabbcc', 'ccddeeffaabb']) == 4
    assert candidate(words = ['aabbccddeeff', 'bbaaccddeeff', 'abbaccddeeff', 'aabbccceeffd', 'aabbccddeff', 'bbaaccddeeff', 'abbaccddeeff', 'aabbccceeffd', 'aabbccddeff', 'bbaaccddeeff', 'abbaccddeeff', 'aabbccceeffd', 'aabbccddeff', 'bbaaccddeeff', 'abbaccddeeff', 'aabbccceeffd', 'aabbccddeff', 'bbaaccddeeff', 'abbaccddeeff', 'aabbccceeffd']) == 3
    assert candidate(words = ['abcdef', 'defabc', 'bcdefa', 'efabcd', 'fabcde', 'abcdefg', 'defabce', 'bcdefag', 'efabcdg', 'fabcdeg', 'abcdefh', 'defabceg', 'bcdefagh', 'efabcdgh', 'fabcdegh', 'abcdef', 'defabc', 'bcdefa', 'efabcd', 'fabcde', 'abcdefg', 'defabce', 'bcdefag', 'efabcdg', 'fabcdeg', 'abcdefh', 'defabceg', 'bcdefagh', 'efabcdgh', 'fabcdegh']) == 9
    assert candidate(words = ['abcdef', 'fedcba', 'bdfeca', 'fdbeca', 'acefbd', 'bfecad', 'fdbeca', 'gacfbde', 'abcdefg', 'gfedcba', 'bdfhace', 'fhdbaec', 'acegfb', 'bfhacd', 'fhbdcae', 'gacfbde', 'mnopqr', 'qrpmno', 'pqmron', 'opmqrn', 'rnmqpo', 'nqrpom', 'mnopqr', 'qrpmno', 'pqmron', 'opmqrn', 'rnmqpo', 'nqrpom']) == 17
    assert candidate(words = ['aabbccddeeff', 'bbaaddccffee', 'aacccbbbddffee', 'ddffeeaaabbbcc', 'bbccddaaffee', 'ffeeddaabbcc', 'ccddeeffaabbbb', 'ddeeffaacccbbbbb']) == 5
    assert candidate(words = ['abcabc', 'bacbac', 'cababc', 'abcbac', 'baccab', 'acbacb', 'acbbac', 'bacbac']) == 4
    assert candidate(words = ['abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh', 'abcdefgh']) == 1
    assert candidate(words = ['pqrstuvw', 'qrstuvwp', 'rstuvwqp', 'stuvwqpr', 'tuvwqprs', 'uvwqprst', 'vwqprstu', 'wqprstuv', 'qprstuvw', 'prstuvqw', 'rstuvqwp', 'stuvqprw', 'tuvqprws', 'uvqprwst', 'vqprwstu', 'qprwstuv']) == 8
    assert candidate(words = ['mnopqr', 'opqrmn', 'pqrmon', 'qrmpno', 'rmpnoq', 'mpnoqr', 'nqrmpo', 'qrpmno']) == 5
    assert candidate(words = ['abcdef', 'defabc', 'bcadef', 'fedcba', 'defacb', 'efabcd']) == 4
    assert candidate(words = ['abcdef', 'fedcba', 'efabcd', 'cdefab', 'bacdef', 'defabc', 'fabcde', 'abcdefg', 'gfedcba', 'zzzzzz', 'zzzzzz', 'zzzzzz', 'zzzzzz', 'zzzzzz', 'zzzzzz', 'zzzzzz', 'zzzzzz', 'zzzzzz', 'zzzzzz', 'zzzzzz']) == 5
    assert candidate(words = ['abcdefgh', 'efghabcd', 'hgfedcba', 'cdabefgh', 'bacdefgh', 'cbadefgh', 'fedcbaab', 'ghfedcba', 'abcdabef', 'efghabcdab']) == 7
    assert candidate(words = ['abcdefg', 'gfedcba', 'cdabefg', 'efgabcd', 'fedcbag', 'bacdefg']) == 4
    assert candidate(words = ['abcdefghijk', 'abcdefghijk', 'abcdefghijk', 'abcdefghijk', 'abcdefghijk', 'abcdefghijk']) == 1
    assert candidate(words = ['abcdefg', 'gfedcba', 'cebgfad', 'bacdfeg', 'adgfceb', 'fdgecab']) == 4
    assert candidate(words = ['aaabbbccc', 'bbbaaaccc', 'aabbccabb', 'bbccaaabb', 'ccbbbaaab', 'aabbbccc', 'bbbaaaccc', 'aabbccabb']) == 5
    assert candidate(words = ['xyzxyz', 'zyxzyx', 'yzxyzx', 'xzyzxz', 'zyxzxy', 'zxyxzy']) == 4
    assert candidate(words = ['aabbccdd', 'bbaaddcc', 'ababcdcd', 'babcadcd', 'cbadcbad', 'dcbadabc', 'abcdabcd', 'badcabcd']) == 4
    assert candidate(words = ['abcdabcd', 'cdabcdab', 'bacdbacd', 'abcdcdab', 'cdababcd', 'bacdabcd', 'abcdabcd', 'cdabcdab']) == 3
    assert candidate(words = ['zzzzzzzz', 'zzzzzzzz', 'zzzzzzzz', 'zzzzzzzz', 'zzzzzzzz', 'zzzzzzzz']) == 1
    assert candidate(words = ['abcdefgh', 'bacdefgh', 'decfghab', 'fedghabc', 'fedcbagh', 'defghacb', 'gfedcbah', 'hgfedcba']) == 6
    assert candidate(words = ['aabbccddeeff', 'bbaaddeeccff', 'ababcdcdefef', 'babaabcdcdef', 'ccddeeffabcd', 'ddaabbccdefe', 'abcdccddeeff', 'ccddeeffaabb', 'bbccddeeffaa', 'aabbddeeffcc', 'fedcbafedcba', 'defcbafedcba', 'efcbadfedcba', 'cdefbafedcba', 'bacdefedcba', 'abcdefedcba', 'fedcbadefcba', 'defcbadefcba', 'efcbadfedcba', 'cdefbafedcba', 'bacdefedcba', 'abcdebcdfa', 'defcbedabcfa', 'efcbadefabcf', 'cdefbafedabcf', 'bacdefedabcf', 'abcdebcfabcf']) == 14
    assert candidate(words = ['abcdefgh', 'hgfedcba', 'efghabcd', 'cdefghab', 'bacdefgh', 'defghcab', 'fghabcde', 'ghabcdef', 'habcdefg', 'abcdefghg', 'gfedcbaa', 'efghabcd', 'cdefghab', 'bacdefgh', 'defghcab', 'fghabcde', 'ghabcdef', 'habcdefg', 'abcdefghh', 'gfedcbab']) == 8
    assert candidate(words = ['abcdefghij', 'jihgfedcba', 'bacdefghij', 'jihgfedcba', 'bacdefghij', 'jihgfedcba']) == 3
    assert candidate(words = ['abcdefghij', 'jihgfedcba', 'bdfhjacegi', 'fhjdgbacae', 'acegfbidhj', 'bfhacdijeg', 'fhbdcaejg', 'gacfbdehji']) == 8
    assert candidate(words = ['aabbcc', 'bbaacc', 'abacbc', 'cababc', 'acbacb', 'bcabac', 'cabcab', 'abcabc']) == 3
    assert candidate(words = ['aabbccdd', 'bbaaddcc', 'ababcdcd', 'babaabcd', 'ccddabcd', 'ddaabbcc', 'abcdccdd', 'ccddabba', 'bbccddaa', 'aabbddcc']) == 4
    assert candidate(words = ['abcdefgh', 'bacdefgh', 'cbadefgh', 'abcdfehg', 'gfedcba', 'hgfedcba', 'abcdefgh', 'bacdefgh']) == 5
    assert candidate(words = ['aabbccddeeff', 'bbaacceeddff', 'aabcbceddeff', 'aabbccddfeef', 'bbaacceeddff', 'aabcbceddeff', 'aabbccddeeff', 'bbaacceeddff']) == 2
    assert candidate(words = ['abcdefgh', 'acegbdfh', 'agbfcehd', 'hgfedcba', 'efghabcd', 'ceafghbd']) == 5
    assert candidate(words = ['aabbccddeeff', 'ffeeddccbbaa', 'bbaaccddffee', 'ffeeddccbbaa', 'aabbccddeeff', 'ffeeddccbbaa']) == 1
    assert candidate(words = ['zzzzzz', 'zzzzzz', 'zzzzzz', 'zzzzzz', 'zzzzzz', 'zzzzzz']) == 1
    assert candidate(words = ['abcdef', 'bacdef', 'cbadef', 'defabc', 'fedcba', 'efdcba', 'fabced']) == 5
    assert candidate(words = ['abcdefgh', 'bacdefgh', 'cbadefgh', 'defghabc', 'fedcbagh', 'efdcgbah', 'gahfedcb', 'hgfedcba']) == 6
    assert candidate(words = ['aabbccddeeff', 'bbaaccddeeff', 'ababccddeeff', 'bbacacddeeff', 'aabbccddeeff', 'aabbcdeeffcc', 'aaabbbcccddd']) == 5
    assert candidate(words = ['xyzxyz', 'yzxzyx', 'zxyxyz', 'xyzyxz', 'yzxyzx', 'zxyzxy', 'xyzxzy', 'yzzxyx', 'zyxxyz', 'xzyzyx']) == 5
    assert candidate(words = ['xyzabc', 'yzxcba', 'zxcbya', 'zyxcba', 'yxzabc', 'yxzcba', 'zxycba']) == 4
    assert candidate(words = ['abcdefg', 'gfedcba', 'bacdefg', 'gfedcba', 'bacdefg', 'gfedcba']) == 2
    assert candidate(words = ['ababab', 'bababa', 'ababab', 'bababa', 'ababab', 'bababa', 'ababab', 'bababa', 'ababab', 'bababa', 'ababab', 'bababa']) == 2
    assert candidate(words = ['mnopqr', 'mopnqr', 'mpnoqr', 'mnopqr', 'pmonqr', 'pmqnor', 'npoqmr', 'qmonpr']) == 5
