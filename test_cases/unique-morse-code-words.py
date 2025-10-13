# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(words = ['s', 'u', 'n']) == 3
    assert candidate(words = ['mnop', 'qrst', 'uvwx', 'yz']) == 4
    assert candidate(words = ['hello', 'world']) == 2
    assert candidate(words = ['a']) == 1
    assert candidate(words = ['morse', 'coding', 'challenge']) == 3
    assert candidate(words = ['hello', 'world']) == 2
    assert candidate(words = ['test', 'code', 'abcd']) == 3
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz']) == 1
    assert candidate(words = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']) == 7
    assert candidate(words = ['abcd', 'efgh', 'ijkl']) == 3
    assert candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']) == 8
    assert candidate(words = ['gin', 'zen', 'gig', 'msg']) == 2
    assert candidate(words = ['abcd', 'dcba', 'abba', 'baab']) == 4
    assert candidate(words = ['hello', 'world', 'python', 'challenge']) == 4
    assert candidate(words = ['single', 'letter', 'words', 'testcase', 'unique', 'morse', 'alphabet']) == 7
    assert candidate(words = ['abcd', 'dcba', 'mnop', 'ponm', 'qrst', 'tsrq', 'wxyz', 'zyxw']) == 8
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba']) == 2
    assert candidate(words = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee', 'fffff', 'ggggg', 'hhhhh', 'iiiii', 'jjjjj']) == 10
    assert candidate(words = ['internationalization', 'globalization', 'localization', 'standardization', 'representation']) == 5
    assert candidate(words = ['programming', 'is', 'fun']) == 3
    assert candidate(words = ['unique', 'representation', 'morse', 'code', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']) == 12
    assert candidate(words = ['aabbcc', 'bbaacc', 'ccabba', 'abacab', 'cabacb']) == 5
    assert candidate(words = ['zzzzzzzzzzzz', 'aaaaaaaaaaaa', 'bbbbbbbbbbbb', 'cccccccccccc', 'dddddddddddd', 'eeeeeeeeeeee', 'ffffffffffff']) == 7
    assert candidate(words = ['transform', 'transformation', 'form', 'formation']) == 4
    assert candidate(words = ['alice', 'bob', 'charlie', 'david']) == 4
    assert candidate(words = ['aabbcc', 'ddeeff', 'gghhiijj', 'kkllmm', 'nnoopp', 'qqrrss', 'ttuuvv', 'wwxxyy', 'zz']) == 9
    assert candidate(words = ['international', 'morse', 'code', 'challenge']) == 4
    assert candidate(words = ['hello', 'world', 'python', 'programming']) == 4
    assert candidate(words = ['abcdefghijk', 'lmnopqrst', 'uvwxyz']) == 3
    assert candidate(words = ['quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dogs']) == 7
    assert candidate(words = ['short', 'longerword', 'averyverylongwordindeed', 'tiny', 'big']) == 5
    assert candidate(words = ['aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz']) == 1
    assert candidate(words = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm']) == 10
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'mnopqrstuvwxyzabcde']) == 3
    assert candidate(words = ['short', 'longerword', 'evenlongerword', 'thelongestwordinthislist']) == 4
    assert candidate(words = ['qwen', 'alibaba', 'cloud', 'computing', 'solution', 'developer', 'engineer']) == 7
    assert candidate(words = ['alice', 'bob', 'charlie', 'david', 'eve', 'frank', 'grace', 'heidi', 'ivan', 'judy']) == 10
    assert candidate(words = ['repeated', 'words', 'in', 'this', 'list', 'repeated', 'words']) == 5
    assert candidate(words = ['unique', 'transformations', 'morse', 'code']) == 4
    assert candidate(words = ['algorithm', 'datastructure', 'interview', 'challenge']) == 4
    assert candidate(words = ['abracadabra', 'xylophone', 'quizzing', 'algorithm', 'datastructure']) == 5
    assert candidate(words = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj', 'kkk', 'lll', 'mmm', 'nnn', 'ooo', 'ppp', 'qqq', 'rrr', 'sss', 'ttt', 'uuu', 'vvv', 'www', 'xxx', 'yyy', 'zzz']) == 26
    assert candidate(words = ['aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'zzzyyxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa']) == 2
    assert candidate(words = ['unique', 'morse', 'code', 'representations', 'different', 'transformations', 'concatenation', 'english', 'alphabet', 'lowercase', 'letters']) == 11
    assert candidate(words = ['morse', 'code', 'test', 'challenge', 'unique', 'representations', 'programming']) == 7
    assert candidate(words = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee', 'fffff', 'ggggg', 'hhhhh', 'iiiii', 'jjjjj', 'kkkkk', 'lllll', 'mmmmm', 'nnnnn', 'ooooo', 'ppppp', 'qqqqq', 'rrrrr', 'sssss', 'ttttt', 'uuuuu', 'vvvvv', 'wwwww', 'xxxxx', 'yyyyy', 'zzzzz']) == 26
    assert candidate(words = ['repeat', 'repeat', 'repeat', 'repeat', 'unique']) == 2
    assert candidate(words = ['hello', 'world', 'this', 'is', 'a', 'test', 'case']) == 7
    assert candidate(words = ['repeated', 'words', 'are', 'here', 'repeated', 'words']) == 4
    assert candidate(words = ['repeated', 'words', 'are', 'transformed', 'into', 'morse', 'code', 'and', 'we', 'count', 'unique', 'representations']) == 12
    assert candidate(words = ['qz', 'jx', 'vk', 'bf']) == 4
    assert candidate(words = ['mississippi', 'bookkeeper', 'anagram', 'controller', 'algorithm']) == 5
    assert candidate(words = ['algorithms', 'data', 'structures', 'machine', 'learning']) == 5
    assert candidate(words = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee']) == 5
    assert candidate(words = ['qzj', 'xlt', 'bkw', 'fmo', 'hmu', 'fsz', 'qqt', 'ztl', 'rgj', 'zhm', 'gmo', 'bwz', 'pqt', 'kcu', 'wqt', 'hmr', 'pgt', 'xqt', 'nzm', 'nhu', 'xzm', 'cmu', 'pqh', 'pgj', 'xju', 'zmh', 'xmu']) == 27
    assert candidate(words = ['single', 'unique', 'distinct', 'different']) == 4
    assert candidate(words = ['same', 'same', 'same', 'same', 'same', 'different']) == 2
    assert candidate(words = ['singleword', 'anotherword', 'yetanotherword', 'onemoreword', 'lastword']) == 5
    assert candidate(words = ['transformation', 'representation', 'unique', 'words', 'list']) == 5
    assert candidate(words = ['morsetest', 'codeforces', 'competitive', 'algorithm']) == 4
    assert candidate(words = ['morse', 'code', 'morsecode', 'codemorse']) == 4
    assert candidate(words = ['repeat', 'repeat', 'repeat', 'different', 'words']) == 3
    assert candidate(words = ['zebra', 'yak', 'antelope', 'hippopotamus', 'elephant', 'giraffe']) == 6
    assert candidate(words = ['this', 'is', 'a', 'simple', 'test', 'case']) == 6
    assert candidate(words = ['amazingrace', 'triathlon', 'cycling', 'running', 'swimming', 'tri', 'duathlon', 'aquathlon']) == 8
    assert candidate(words = ['alice', 'bob', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india', 'juliett', 'kilo', 'lima', 'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo', 'sierra', 'tango', 'uniform', 'victor', 'whiskey', 'xray', 'yankee', 'zulu']) == 26
    assert candidate(words = ['karen', 'mike', 'nancy', 'olivia', 'peter', 'quincy', 'rachel', 'steve', 'tina', 'ulysses', 'victor', 'wendy', 'xander', 'yvonne', 'zach']) == 15
    assert candidate(words = ['qzj', 'xmv', 'nkt', 'hbw', 'lyf']) == 5
    assert candidate(words = ['programming', 'is', 'fun']) == 3
    assert candidate(words = ['unique', 'representations', 'morse', 'code', 'challenge']) == 5
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz']) == 3
    assert candidate(words = ['programming', 'challenge', 'python', 'codeforces']) == 4
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'mnopqrstuvwxyzabcdefghijkl']) == 3
    assert candidate(words = ['racecar', 'level', 'rotor', 'radar', 'deified', 'noon', 'kayak', 'reviler']) == 8
    assert candidate(words = ['qzcv', 'wqop', 'rgmo', 'mnlx', 'axta', 'qwkl', 'qzcv', 'wqop', 'rgmo', 'mnlx', 'axta', 'qwkl']) == 6
    assert candidate(words = ['unique', 'morse', 'representations', 'are', 'calculated', 'from', 'the', 'given', 'words']) == 9
    assert candidate(words = ['aabbccdd', 'bbaaddcc', 'ccddeeff', 'ddeeffcc', 'eeffccdd', 'ffccddeeff', 'ccddeeff', 'ddeeffcc', 'eeffccdd', 'ffccddeeff']) == 6
    assert candidate(words = ['transform', 'transformation', 'translate', 'translator', 'coding', 'decoding']) == 6
    assert candidate(words = ['python', 'java', 'csharp', 'javascript']) == 4
    assert candidate(words = ['repeat', 'repeat', 'repeat', 'repeat']) == 1
    assert candidate(words = ['hello', 'world', 'python', 'programming', 'challenge']) == 5
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'mnopqrstuvwxyzabcdefghijkl', 'fedcbazyxwvutsrqponmlkijgh']) == 4
