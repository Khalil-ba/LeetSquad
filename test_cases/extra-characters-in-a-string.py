# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = "abc",dictionary = ['a', 'b', 'c']) == 0
    assert candidate(s = "sayhelloworld",dictionary = ['hello', 'world']) == 3
    assert candidate(s = "abc",dictionary = ['d', 'e']) == 3
    assert candidate(s = "abcabcabc",dictionary = ['abcabc', 'abc']) == 0
    assert candidate(s = "abracadabra",dictionary = ['abra', 'cadabra', 'abc']) == 0
    assert candidate(s = "abc",dictionary = ['d', 'e', 'f']) == 3
    assert candidate(s = "applepenapple",dictionary = ['apple', 'pen']) == 0
    assert candidate(s = "catsandog",dictionary = ['cats', 'dog', 'sand', 'and', 'cat']) == 2
    assert candidate(s = "ab",dictionary = ['abc', 'def']) == 2
    assert candidate(s = "abcde",dictionary = ['a', 'b', 'c', 'd', 'e']) == 0
    assert candidate(s = "programming",dictionary = ['pro', 'gram', 'ming']) == 0
    assert candidate(s = "a",dictionary = ['b']) == 1
    assert candidate(s = "mississippi",dictionary = ['mis', 'is', 'ip', 'i', 'p']) == 2
    assert candidate(s = "leetscode",dictionary = ['leet', 'code', 'leetcode']) == 1
    assert candidate(s = "aabbcc",dictionary = ['a', 'b', 'c']) == 0
    assert candidate(s = "programmingisfun",dictionary = ['pro', 'gram', 'ming', 'is', 'fun', 'prog', 'am', 'ing', 'pr', 'gramm', 'ingis', 'funs']) == 0
    assert candidate(s = "dynamicprogramming",dictionary = ['dyn', 'ami', 'cpro', 'gram', 'ming', 'pro', 'gramming']) == 0
    assert candidate(s = "algorithm",dictionary = ['algo', 'rith', 'm', 'alg', 'ith', 'o', 'g', 'a', 'l', 'th', 'or', 'thm', 'al']) == 0
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",dictionary = ['a', 'z', 'abc', 'xyz', 'mnopqr', 'uvw', 'def', 'jkl']) == 5
    assert candidate(s = "substringsearch",dictionary = ['sub', 'string', 'search', 'substri', 'ngsea', 'rch', 'str', 'sea', 'subsearc', 'ubstringse']) == 0
    assert candidate(s = "encyclopedia",dictionary = ['ency', 'clop', 'edia', 'lo', 'pedia', 'cycle', 'en', 'dec', 'clo', 'opaedia']) == 0
    assert candidate(s = "thisisateststring",dictionary = ['this', 'is', 'a', 'test', 'string', 'isatest', 'teststr', 'str', 'ring', 'thi', 'sta', 'tes', 'ing', 'est', 'at']) == 0
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",dictionary = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == 0
    assert candidate(s = "optimization",dictionary = ['opt', 'imiz', 'tio', 'n', 'zat', 'ion', 'optim']) == 1
    assert candidate(s = "programmingisfun",dictionary = ['pro', 'gram', 'ming', 'is', 'fun', 'gramm', 'ing', 'program', 'mingis', 'funn']) == 0
    assert candidate(s = "thisisatest",dictionary = ['this', 'is', 'a', 'test', 'ate', 'st']) == 0
    assert candidate(s = "programmingchallenge",dictionary = ['pro', 'gram', 'ming', 'chall', 'lenge', 'ge']) == 2
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",dictionary = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']) == 0
    assert candidate(s = "encyclopedia",dictionary = ['ency', 'clopedia', 'encyclo', 'pedia', 'encyclope', 'dopia', 'edia', 'a', 'ei', 'lo', 'ope', 'dic', 'lope', 'dia', 'edia']) == 0
    assert candidate(s = "minimizingextra",dictionary = ['mini', 'min', 'zing', 'extra', 'ze', 'tra', 'minimize']) == 2
    assert candidate(s = "repeatedcharacters",dictionary = ['re', 'pe', 'at', 'ed', 'cha', 'rac', 'ters', 'ter', 'char', 'acters']) == 0
    assert candidate(s = "findingthesolution",dictionary = ['find', 'ing', 'the', 'solu', 'tion', 'solution', 'thesolu', 'tingthe', 'thesolu', 'solu', 'tionfind', 'ingthe', 'thesolution', 'ingthes']) == 0
    assert candidate(s = "mississippi",dictionary = ['mis', 'sis', 'ip', 'i', 'ss', 'p']) == 1
    assert candidate(s = "aaaaabbbbb",dictionary = ['a', 'b', 'aa', 'bb', 'ab', 'ba', 'aaa', 'bbb', 'aab', 'bba', 'aba', 'bab']) == 0
    assert candidate(s = "mississippi",dictionary = ['issi', 'ssippi', 'miss', 'ippi', 'is', 's', 'pi', 'p']) == 0
    assert candidate(s = "subsequences",dictionary = ['sub', 'seq', 'uen', 'ce', 's', 'quence', 'quencece']) == 0
    assert candidate(s = "backtracking",dictionary = ['back', 'track', 'ing', 'backtr', 'acking', 'tracki', 'ing']) == 0
    assert candidate(s = "abcdefghijk",dictionary = ['abc', 'def', 'gh', 'ijk', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']) == 0
    assert candidate(s = "abcdefghijabcdefghijabcdefghij",dictionary = ['abc', 'def', 'ghi', 'j', 'abcdefghij', 'abcdefgh', 'abcde', 'fghij', 'ab', 'cd', 'ef', 'gh', 'ij']) == 0
    assert candidate(s = "thisisaverylongstring",dictionary = ['this', 'is', 'a', 'very', 'long', 'string', 'thi', 'sis', 'verylong']) == 0
    assert candidate(s = "optimallybreakingstrings",dictionary = ['opti', 'mally', 'breaking', 'strings', 'opt', 'im', 'ally', 'break', 'ing', 'str', 'ing', 's', 'optimal', 'breaks', 'allybreak']) == 0
    assert candidate(s = "abracadabra",dictionary = ['abra', 'cad', 'bra', 'abc', 'rac']) == 0
    assert candidate(s = "mississippi",dictionary = ['mis', 'si', 'issi', 'pi', 'ppi', 'pis', 'missis', 'sippi', 'ippi', 'issipp']) == 0
    assert candidate(s = "xylophone",dictionary = ['xy', 'lo', 'phone', 'ph', 'one', 'xo', 'xyl', 'ylo', 'ho', 'ne', 'pho']) == 0
    assert candidate(s = "subsequences",dictionary = ['sub', 'seq', 'en', 'ce', 'qu', 'subseq', 'quence']) == 2
    assert candidate(s = "thecodinginterview",dictionary = ['the', 'coding', 'in', 'terview', 'inter', 'view', 'codingin', 'erview', 'viewint', 'nterview', 'inerview']) == 0
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",dictionary = ['a', 'z', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']) == 0
    assert candidate(s = "abracadabra",dictionary = ['abra', 'cad', 'bra', 'rac', 'ab', 'ad', 'a', 'b', 'c', 'd', 'r']) == 0
    assert candidate(s = "optimization",dictionary = ['opti', 'miz', 'ation', 'iza', 'ti', 'on']) == 0
    assert candidate(s = "mississippi",dictionary = ['mis', 'sis', 'ip', 'i', 'ss', 'is', 'pi', 'pp']) == 1
    assert candidate(s = "dynamicprogramming",dictionary = ['dynamic', 'program', 'gram', 'ming', 'pro', 'gramming']) == 0
    assert candidate(s = "constraints",dictionary = ['con', 'straint', 'stra', 'ints', 't', 'res', 'trai', 'ns', 'constra']) == 0
    assert candidate(s = "abcdabcdabcd",dictionary = ['ab', 'cd', 'abcd', 'abc', 'bcd', 'dabc']) == 0
    assert candidate(s = "watermelon",dictionary = ['water', 'melon', 'wa', 'ter', 'melon', 'wa', 'me', 'lo', 'on', 'terme', 'lono', 'wate', 'rme', 'lo', 'non', 'w', 'a', 't', 'e', 'r', 'm', 'e', 'l', 'o', 'n']) == 0
    assert candidate(s = "breakfast",dictionary = ['break', 'fast', 'bre', 'ak', 'fastbreak', 'breakfa', 'st']) == 0
    assert candidate(s = "subsequence",dictionary = ['sub', 'sequence', 'seq', 'uen', 'ce', 'subse', 'quen']) == 0
    assert candidate(s = "optimization",dictionary = ['opti', 'mize', 'optim', 'on', 'ize', 'miz', 'ization']) == 0
    assert candidate(s = "programming",dictionary = ['pro', 'gram', 'ming', 'ing', 'progr', 'amming']) == 0
    assert candidate(s = "alibabacloud",dictionary = ['ali', 'ba', 'bacloud', 'cloud', 'ib', 'baclou', 'bacla', 'baba', 'clouds', 'alibaba']) == 0
    assert candidate(s = "segmentation",dictionary = ['seg', 'men', 'tation', 'ment', 'entation', 'segmen', 't', 'ation']) == 0
    assert candidate(s = "algorithm",dictionary = ['algo', 'rithm', 'log', 'ith', 'm', 'a', 'thm', 'gor', 'orithm', 'ithm', 'gori', 'thmi']) == 0
    assert candidate(s = "beautiful",dictionary = ['be', 'autiful', 'aut', 'ful', 'at', 'beau', 'ti', 'ful', 'b', 'e', 'a', 'u', 't', 'i', 'f', 'u', 'l', 'beauti', 'ful', 'auti', 'ful', 'beaut', 'iful', 'bea', 'utiful', 'be', 'autiful', 'ti', 'ful', 'bea', 'ut', 'iful', 'beau', 'tiful', 'beaut', 'ifu', 'l']) == 0
    assert candidate(s = "quickbrownfoxjumpsoverthelazydog",dictionary = ['quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', 'qu', 'ick', 'br', 'own', 'fo', 'x', 'ump', 'so', 'ver', 'el', 'az', 'y']) == 0
    assert candidate(s = "example",dictionary = ['ex', 'ample', 'am', 'ple', 'e', 'xample']) == 0
    assert candidate(s = "dynamicprogramming",dictionary = ['dyn', 'amic', 'prog', 'ram', 'ming', 'gramming', 'pro', 'dynamic', 'grampro', 'mingprog', 'rammi']) == 0
    assert candidate(s = "mississippi",dictionary = ['mis', 'sis', 'sip', 'issi', 'ippi']) == 1
    assert candidate(s = "subsequence",dictionary = ['sub', 'seq', 'en', 'ce', 'subse', 'quence']) == 0
    assert candidate(s = "overlapping",dictionary = ['over', 'lap', 'ping', 'lap', 'pingo', 'ver', 'lap', 'laplap']) == 0
    assert candidate(s = "dynamicprogramming",dictionary = ['dyn', 'amic', 'pro', 'gram', 'ming', 'prog', 'dyna', 'micpro', 'grammi', 'amming']) == 0
    assert candidate(s = "programming",dictionary = ['pro', 'gram', 'ming', 'gramming', 'prog', 'program', 'mming', 'progr', 'gram', 'ming', 'gramm', 'pro', 'gram', 'ming', 'programming', 'gram', 'ming', 'pro', 'gram', 'ming', 'gramming', 'pro', 'gram', 'ming', 'gramm', 'pro', 'gram', 'ming', 'program', 'ming', 'pro', 'gramming', 'gram', 'ming', 'gramm', 'prog', 'ming', 'pro', 'gramming', 'pro', 'gram', 'ming', 'gramm', 'pro', 'gram', 'ming', 'gramming', 'prog', 'gram', 'ming', 'pro', 'gramming']) == 0
    assert candidate(s = "partitioning",dictionary = ['parti', 'tion', 'ion', 'part', 'itioning', 'parti', 'tion', 'ing']) == 0
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",dictionary = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']) == 0
    assert candidate(s = "optimization",dictionary = ['opt', 'im', 'iz', 'ation', 'iza', 'tio']) == 0
    assert candidate(s = "breakintothepieces",dictionary = ['break', 'into', 'the', 'pie', 'ces', 'iece', 'to', 'pieces', 'breakin', 'intothep']) == 0
    assert candidate(s = "fuzzywuzzy",dictionary = ['fuz', 'zy', 'wuz', 'z', 'wuzz', 'fuzzy', 'wuzzywuzz']) == 0
    assert candidate(s = "programmingcontest",dictionary = ['pro', 'gram', 'ming', 'con', 'test', 'gramming', 'est']) == 0
    assert candidate(s = "abcdefgabcdefg",dictionary = ['abc', 'def', 'gh', 'abcdef', 'bcde', 'fgh', 'abcd', 'efg', 'fg', 'abcdab', 'bcdefg']) == 0
    assert candidate(s = "pythonprogramming",dictionary = ['py', 'thon', 'pro', 'gram', 'ming', 'prog', 'python', 'gramming', 'ron', 'th', 'ing']) == 0
    assert candidate(s = "helloworld",dictionary = ['hello', 'wor', 'ld', 'hell', 'world', 'owor', 'orl', 'rld', 'hel', 'wo', 'rld', 'worl', 'hello', 'world', 'worldly', 'or', 'wor', 'ld', 'hell', 'world', 'hellworld', 'hell', 'wo', 'rld', 'hello', 'world']) == 0
    assert candidate(s = "programmingcontest",dictionary = ['pro', 'gram', 'ming', 'con', 'test', 'gramming', 'est', 'on', 'gramcon', 'estcontest']) == 0
    assert candidate(s = "onomatopoeia",dictionary = ['ono', 'mato', 'poei', 'a', 'ia', 'oeia', 'opoe', 'oe', 'onom', 'atopoeia']) == 0
    assert candidate(s = "mississippi",dictionary = ['mis', 'issi', 'ippi', 'sip', 'iss', 'is', 'i', 'pi', 'missis', 'sippi']) == 0
    assert candidate(s = "loremipsum",dictionary = ['lor', 'em', 'ip', 'sum', 'lorem', 'rem', 'ems', 'mip', 'ips', 'pum', 'ipsum']) == 0
    assert candidate(s = "interview",dictionary = ['inter', 'view', 'ter', 'iew', 'in', 'terview', 'nterv', 'vieww']) == 0
    assert candidate(s = "abracadabra",dictionary = ['ab', 'ra', 'cad', 'abra', 'brac']) == 0
    assert candidate(s = "programmingcontest",dictionary = ['pro', 'gram', 'ming', 'con', 'test', 'est', 'contest']) == 0
    assert candidate(s = "mississippi",dictionary = ['mis', 'sis', 'sip', 'i', 'ss', 'pi', 'pp']) == 0
    assert candidate(s = "dynamicprogramming",dictionary = ['dyn', 'amic', 'pro', 'gram', 'ming', 'gramm', 'prog', 'dyna', 'progr']) == 0
    assert candidate(s = "supercalifragilisticexpialidocious",dictionary = ['super', 'cali', 'fragilistic', 'expiali', 'docious', 'ex', 'pi', 'ali', 'ous']) == 0
    assert candidate(s = "supercalifragilisticexpialidocious",dictionary = ['super', 'cali', 'fragilistic', 'expiali', 'docious', 'superca', 'lifrag', 'istic', 'expialido', 'cious', 'superca', 'li', 'frag', 'ilistic', 'ex', 'pialido', 'california', 'super', 'superdocus']) == 0
    assert candidate(s = "supercalifragilisticexpialidocious",dictionary = ['super', 'cali', 'fragilistic', 'expiali', 'docious', 'frag', 'listic', 'exp', 'ali', 'do', 'cious', 'superca', 'li', 'fragi', 'list', 'expialidoc', 'supercalifrag', 'supercalifragilisticexpi', 'alidocious', 'istic', 'expialidoci', 'superca', 'lifragilisti', 'cexpialid', 'alidoc', 'expialido', 'fragilisticexpialidocious']) == 0
    assert candidate(s = "optimizationproblems",dictionary = ['opt', 'im', 'ization', 'prob', 'lems', 'ob', 'lem', 'pro', 'blem', 'blempro']) == 0
    assert candidate(s = "breakfast",dictionary = ['break', 'fast', 'bre', 'ak', 'fast', 'reak']) == 0
    assert candidate(s = "dictionary",dictionary = ['dic', 'tion', 'tio', 'nary', 'dict', 'ionar', 'ictionary', 'dictio', 'n']) == 0
    assert candidate(s = "backtracking",dictionary = ['back', 'track', 'ing', 'bac', 'ktrack', 'king']) == 0
    assert candidate(s = "algorithms",dictionary = ['algo', 'rithm', 'thms', 'log', 'rith', 'ms', 'algothm', 'rithms']) == 0
    assert candidate(s = "optimization",dictionary = ['opt', 'im', 'ization', 'iz', 'ation', 'optim', 'ize']) == 0
