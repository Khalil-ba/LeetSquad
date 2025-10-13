# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = "aaabaaa",words = ['aa', 'aaa', 'aaaa', 'aabaaa']) == 1
    assert candidate(s = "aaabaaa",words = ['aaa', 'aab', 'aaaaa', 'aaabaa', 'aaaba']) == 2
    assert candidate(s = "abcd",words = ['abc', 'abcd', 'abdc', 'aabbccdd']) == 1
    assert candidate(s = "abcd",words = ['abc', 'abcd', 'abcde']) == 1
    assert candidate(s = "aaabbbcccddd",words = ['aabbccddd', 'aabbbcccddd', 'aabbbcccdd']) == 3
    assert candidate(s = "a",words = ['a', 'aa', 'aaa', 'aaaa']) == 1
    assert candidate(s = "aabbcc",words = ['aabbcc', 'aabbc', 'aaabc']) == 1
    assert candidate(s = "abcd",words = ['aabbccdd', 'abccdd', 'abbbccdd', 'aabbcccddd']) == 0
    assert candidate(s = "heeellooo",words = ['hello', 'hi', 'helo']) == 1
    assert candidate(s = "aaabaaa",words = ['aab', 'aaab', 'aaaab', 'aaaba', 'aaaaaaab']) == 1
    assert candidate(s = "abcd",words = ['abc', 'ab', 'abcd', 'abcde']) == 1
    assert candidate(s = "aaa",words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']) == 3
    assert candidate(s = "abcd",words = ['abc', 'abcd', 'abcde', 'ab', 'a']) == 1
    assert candidate(s = "aaabbb",words = ['aabb', 'aabbbb', 'aaabbbb']) == 1
    assert candidate(s = "abcd",words = ['abc', 'ab', 'abcd', 'abcde', 'aabbccdd']) == 1
    assert candidate(s = "zzzzzyyyyy",words = ['zzyy', 'zy', 'zyy']) == 3
    assert candidate(s = "heeellloooopppp",words = ['helloppp', 'heellooppp', 'helooppp', 'helllopppp', 'heeelllooooooo', 'hello']) == 4
    assert candidate(s = "ttttuuuuuuuuuuuuvvv",words = ['tuv', 'tttuuuuuuuuuuvvv', 'ttttuuuuuuuuuuu', 'ttttuuuuuuuuuvv', 'ttttuuuuuuuuuuuuv']) == 4
    assert candidate(s = "heeeloooooo",words = ['hello', 'heeellooo', 'helllooo', 'heellooo', 'heeelloo']) == 0
    assert candidate(s = "aaaabbbbcccc",words = ['aabbcc', 'aaabbbcccc', 'aaaabbbbccc', 'aaaabbbcccc', 'aaaaabbbbcccc']) == 4
    assert candidate(s = "aaaabbbbccccddddeeee",words = ['aabcd', 'abbbcd', 'abccde', 'abcde', 'aaaaabbbbccccddddeee']) == 2
    assert candidate(s = "mmmmnnnnnnoooopppppp",words = ['mnop', 'mmnnnnoooppp', 'mmmmmnnnnnnnoooooopppppp', 'mmnnoopp', 'mmnnoooopppp']) == 4
    assert candidate(s = "xxxxxyyyyyyzzzzzz",words = ['xyzz', 'xxxyyyyzzz', 'xxxxxyyyzzzzz', 'xxxxxyyyyyyzzzz', 'xxxxxyyyyyyzzzzzz']) == 5
    assert candidate(s = "llllaaaabbbbccccddddeeeee",words = ['laabcd', 'labbbccddeee', 'labcde', 'laaaabbbbccccddddeee', 'lbbbcccddddeeee']) == 3
    assert candidate(s = "abbbcccddd",words = ['abc', 'abbc', 'abbcc', 'abbbcccd', 'abbbcccddd', 'abbbcccdd', 'abbbccccd', 'abbbccccdd']) == 3
    assert candidate(s = "mmmmnnnnoooopppp",words = ['mno', 'mmnnnnooooppp', 'mmmmnnnnoooop', 'mmmmnnnnoooopppp', 'mmmmnnnnoooppp']) == 4
    assert candidate(s = "heeellloooowooorlddd",words = ['helo', 'hello', 'helooworld', 'heeellooworld', 'heeelllooooowooorlddd']) == 2
    assert candidate(s = "mmmmmmmnnnnnnn",words = ['mmnn', 'mmmnnn', 'mmmmnnnn', 'mmmmmn', 'mmmmnn', 'mmmmmnnn', 'mmmmmmnnnnn', 'mmmmmmnnnn']) == 8
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",words = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'zzzzz', 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'aabbbccddeeefffgghhhiiiijjjkkklllmmmnnnooooppppqqqqrrrrsssss', 'aabbccddeeefffgggiiiijjjkkklllmmmnnnoooopppqqqqrrrrrrsssss', 'aabbccddeeffgghhiijjkkklllmmmmmnnnnnoooooopppppqqqqqqrrrrrrssssss']) == 1
    assert candidate(s = "xyzzzzzyyyyyyyy",words = ['xyz', 'xyyz', 'xyzz', 'xyzzz', 'xyzzzz', 'xyzzzzzyyyyy', 'xyzzzzzyyyyyy', 'xyzzzzzyyyyyyyy']) == 3
    assert candidate(s = "zzzzzzzyyyyyyy",words = ['zzzyyyy', 'zzzzzyyy', 'zzzyyyyyyy', 'zzzzzzzzyy', 'zyyyyyyy']) == 4
    assert candidate(s = "mississippiiii",words = ['mississippi', 'missisiiippi', 'mississippiiiii', 'missisipi', 'misisipi']) == 1
    assert candidate(s = "xxyyzzzz",words = ['xxyyz', 'xxyyzz', 'xxxyyyzzzz', 'xxyyzzz', 'xyzzz']) == 3
    assert candidate(s = "aabbccccddddeeeffggg",words = ['aabbccddeeffg', 'aabbcccddddeffgg', 'aabbbccccddddeeeffggg', 'aabbbcccddddeeeffgg', 'aabbccccdddddeeeffggg']) == 2
    assert candidate(s = "xxxxxxyyyyyyzzzzzz",words = ['xyzz', 'xyzzz', 'xyyz', 'xxxyyyyzzz', 'xxxxxyyyyyyzzzzzz']) == 5
    assert candidate(s = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",words = ['qq', 'qqq', 'qqqq', 'qqqqqq', 'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq']) == 4
    assert candidate(s = "ttttttttttttuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvvvvvvvv",words = ['tuv', 'ttuuuvvv', 'ttttuuuuuuuvvvvvvv', 'tttuuuuuuvvvvvvvvvv', 'ttttuuuuuuuuuuuvvvvvvvvvvvvvvvvvv']) == 5
    assert candidate(s = "ppppqqqqrrrrssss",words = ['pqrst', 'pqrs', 'ppqrs', 'ppqqrrss', 'ppqqqrrrssss', 'ppqqqqrrrrsssss']) == 4
    assert candidate(s = "helloooooworlddddd",words = ['hellooworld', 'hellooworlddd', 'hellllooworld', 'helloooworldddddd', 'hellooooooworlddddd']) == 2
    assert candidate(s = "mississippiissi",words = ['mississippissi', 'misisipi', 'mississippi', 'mississsippi', 'mississippiii']) == 0
    assert candidate(s = "aabbccddeee",words = ['abcde', 'aabbcdeee', 'aaabbbcccdddeee', 'aabbccdde', 'aabccdeee']) == 1
    assert candidate(s = "ppppqqqqrrrssss",words = ['pqr', 'ppqqrrsss', 'pppqqqrrrrssss', 'ppqqrrsssss', 'ppqqrrr']) == 1
    assert candidate(s = "abcdefghijklllllmnopqrstuvwxyz",words = ['abcdefghijklmopqrstuvwxyz', 'abcdefghijklllmmnopqrstuvwxyz', 'abcdefghijkllllmnopqrstuvwxyz', 'abcdefghijklllllmnopqrstuvwxy', 'abcdefghijklllllmnopqrstuvwxyz']) == 2
    assert candidate(s = "hhheeelllllooooworrlldd",words = ['helloworld', 'hhhellooooworld', 'hheeellllllooooworld', 'hellooworld', 'hheellooworl']) == 0
    assert candidate(s = "ssssaaafffff",words = ['saff', 'ssaff', 'ssaaaff', 'ssaaaafff', 'ssaaaaaffff', 'ssssaaaafffff']) == 3
    assert candidate(s = "abcdefghijjjjjjjklmnopqrstuvwxyz",words = ['abcdefghijklnopqrstuvwxyz', 'abcdefghijjjklmnopqrstuvwxyz', 'abcdefghijjjjjjklmnopqrstuvwxyz', 'abcdefghijjjjjjjklmnopqrstuv', 'abcdefghijjjjjjjmnopqrstuvwxyz']) == 2
    assert candidate(s = "abcdefghiiiiijjjjjjkkkkkkk",words = ['abcdefghijjk', 'abcdefghijk', 'abcdefghiiijjjjkk', 'abcdefghiiijjjjjjkkkkk', 'abcdefghiiijjjjjjkkkkkkk']) == 5
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",words = ['abcdefghijklmnopqrstuvwxyzz', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyzzz', 'abcdefghijklmnopqrstuvwxyzzzz', 'abcdefghijklmnopqrstuvwxyzzzzz']) == 0
    assert candidate(s = "aaaaaaabbbbcccdd",words = ['aabbbccdd', 'aaabbbcccdd', 'aaaabbbcccdd', 'aaaaabbbcccdd', 'aaaaaaabbbcccdd', 'aaaaaaabbbcccd', 'aaaaaaabbbbccdd', 'aaaaaaabbbbcccdd']) == 7
    assert candidate(s = "qqqqqqqqqqqwwweeeerrrrttttt",words = ['qqqqqqqwwwreeeeeerttt', 'qqqwwwreeert', 'qqqqqqqwwwreeerrttt', 'qqqqqqqqqqqwwweeeerrrtttt', 'qqqqqqqwwweeeerrrtttt']) == 2
    assert candidate(s = "abcdeeeeef",words = ['abcdeeef', 'abcdeeeef', 'abcdeeeeeef', 'abcdfeeeef', 'abcdef']) == 3
    assert candidate(s = "abcdefghijjkkklllllmmmmmmmnnnnnnnnnooooooooooopppppppppppppppqqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrrssssssssssssssssttttttttttttttttttuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwxxyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzz",words = ['abcdefghijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'abcdefghijjkkkllllmmmmnnnnooooopppqqqqrrrrsssssttttuvvvvwwwwxxyyyyzzzz', 'abcdefghijjkkklllllmmmmmmnnnnnnnooooooooooopppppppppppppppqqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrrssssssssssssssssttttttttttttttttttuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwxxyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzz']) == 3
    assert candidate(s = "abbbccdddd",words = ['abcdd', 'abbbccdd', 'abbbccccdd', 'abbbccdddd', 'aabbccddd']) == 2
    assert candidate(s = "ppppqqqqrrr",words = ['pqr', 'pppqqrr', 'ppqqqrrr', 'pppqqqqrrr', 'ppppqqqrrr']) == 5
    assert candidate(s = "aaaaaabbcccddeeeee",words = ['aabccddee', 'aaabbbcccdddeeee', 'aaaabbbcccdddeee', 'aaaaabbcccddeeee', 'aaaaabbbbccccddeeeeee']) == 1
    assert candidate(s = "llllllmmmnnnnoo",words = ['lmno', 'lllmmnno', 'lllllmmnnnoo', 'lllmmmnnnnoo', 'llllllmmmnnno']) == 2
    assert candidate(s = "aabbccddeeefffggg",words = ['aabbccddeefffggg', 'aabbbcccdddeeefffggg', 'aabbccddeeeffffgggg', 'aabbccddeeeffg', 'aabbcddfeeeffggg']) == 2
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",words = ['z', 'zz', 'zzz', 'zzzz', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz']) == 4
    assert candidate(s = "ttrrreeee",words = ['tree', 'ttrree', 'ttrreee', 'ttreee', 'ttrre', 'ttre', 'trreee', 'ttreere']) == 5
    assert candidate(s = "mmmaaa",words = ['maa', 'maaaa', 'mmmaaa', 'mmma', 'mmmaaaam']) == 3
    assert candidate(s = "sssssssssssssssssssssssssssss",words = ['s', 'ss', 'sss', 'sssss', 'sssssss', 'sssssssssssssssssssssssssssss']) == 6
    assert candidate(s = "nnnnooouuuuuuuuu",words = ['no', 'noon', 'nou', 'noou', 'noonnouuuu', 'nnoooouuuuuuuu', 'nnooouuuuuuuuu', 'nnnooouuuuuuuuu']) == 4
    assert candidate(s = "aaabbbccc",words = ['aabbccc', 'aaabccc', 'aaabbbcc', 'aabbbccc', 'aaabbbccccc']) == 4
    assert candidate(s = "aaabbbcccddd",words = ['ab', 'aabbccddd', 'aabbbcccddd', 'aaabbbcccdd', 'aaabbbcccd']) == 4
    assert candidate(s = "aaaabbbbccccdddd",words = ['aabbccdd', 'aaabbbcccddd', 'aaaabbbbccccdddd', 'aabbbbccccdddd', 'aaaabbbcccdddd']) == 5
    assert candidate(s = "qqqqqqqqqqqqqqqqq",words = ['q', 'qq', 'qqq', 'qqqq', 'qqqqq', 'qqqqqq', 'qqqqqqqq', 'qqqqqqqqqqqqqqqqq']) == 8
    assert candidate(s = "xxxyyyzzz",words = ['xyzz', 'xxyyz', 'xxyyzz', 'xxxyyyzzz', 'xxxyyzzz', 'xxxxyyzzz', 'xxxyyyyzzz']) == 5
    assert candidate(s = "abbbbbccccdddd",words = ['abc', 'abcd', 'abbc', 'abcdd', 'abbbbbccccdddd']) == 3
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbcccccccccc",words = ['aabbbccc', 'aaaaaaaaabbbbbbbbbbcccccccc', 'aaaaaaaaabbbbbbbbcccccccccc', 'aaaaaaaaaabbbbbbbbbbcccccc', 'aaaaaaaaaabbbbbbbbbbccccccccccc']) == 4
    assert candidate(s = "mississiissippii",words = ['mississippi', 'mississiippii', 'mississsippii', 'mississssippiii', 'mississssiiiiippiii']) == 0
    assert candidate(s = "xyzzzzzzzzzxyzzzzzzzzzxyzzzzzzzzz",words = ['xyzyxzy', 'xyzzzxyzzzxyzzz', 'xyzzzzxyzzzzxyzzzz', 'xyzzzzzzzzxyzzzzzzzzxyzzzzzzzz', 'xyzzzzzzzzzxyzzzzzzzzxzzzzzzzzzz']) == 3
