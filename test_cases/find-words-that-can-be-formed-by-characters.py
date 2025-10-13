# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(words = ['abcd', 'ab', 'bc', 'cd'],chars = "abcd") == 10
    assert candidate(words = ['cat', 'bt', 'hat', 'tree'],chars = "atach") == 6
    assert candidate(words = ['zxcvbnm', 'asdfghjkl', 'qwertyuiop'],chars = "qwertyuiopasdfghjklzxcvbnm") == 26
    assert candidate(words = ['abc', 'def', 'ghi'],chars = "abcdefghi") == 9
    assert candidate(words = ['xyz', 'zyx', 'wxy'],chars = "xyzzyxw") == 9
    assert candidate(words = ['apple', 'banana', 'cherry'],chars = "abc") == 0
    assert candidate(words = ['abc', 'abc', 'abc'],chars = "aabbcc") == 9
    assert candidate(words = ['test', 'case', 'word'],chars = "tcws") == 0
    assert candidate(words = ['a', 'b', 'c'],chars = "abcde") == 3
    assert candidate(words = ['a', 'b', 'c'],chars = "abcabcabc") == 3
    assert candidate(words = ['abcd', 'dcba', 'abcd'],chars = "abcd") == 12
    assert candidate(words = ['hello', 'world', 'leetcode'],chars = "welldonehoneyr") == 10
    assert candidate(words = ['zzz', 'yyy', 'xxx'],chars = "zyxzyx") == 0
    assert candidate(words = ['one', 'two', 'three'],chars = "onetwothree") == 11
    assert candidate(words = ['python', 'java', 'c++'],chars = "pythjavacp") == 4
    assert candidate(words = ['zzz', 'yyy', 'xxx'],chars = "zyxwvutsrqponmlkjihgfedcba") == 0
    assert candidate(words = ['a', 'b', 'c'],chars = "abc") == 3
    assert candidate(words = ['apple', 'apple', 'apple'],chars = "ppale") == 15
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa'],chars = "aaaaa") == 10
    assert candidate(words = ['aabbcc', 'abc', 'abc'],chars = "aabbcc") == 12
    assert candidate(words = ['aaa', 'bbb', 'ccc'],chars = "aabbcc") == 0
    assert candidate(words = ['abcd', 'efgh', 'ijkl'],chars = "abcdefgh") == 8
    assert candidate(words = ['aaa', 'bbb', 'ccc'],chars = "abc") == 0
    assert candidate(words = ['apple', 'banana', 'cherry'],chars = "abcde") == 0
    assert candidate(words = ['test', 'code', 'contest'],chars = "testcode") == 8
    assert candidate(words = ['challenge', 'python', 'code', 'fun'],chars = "nclhpgfouitay") == 9
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba'],chars = "abcdefghijklmnopqrstuvwxyz") == 52
    assert candidate(words = ['programming', 'language', 'python', 'java'],chars = "npgmajoasrivl") == 4
    assert candidate(words = ['', 'a', 'aa', 'aaa', 'aaaa'],chars = "a") == 1
    assert candidate(words = ['banana', 'ananas', 'panama', 'manana'],chars = "anamnb") == 0
    assert candidate(words = ['aabb', 'bbcc', 'ccdd', 'ddee', 'eeff', 'ffgg', 'gghh', 'hhiijj', 'kkll', 'mmnn', 'oorr', 'ppqq', 'sstt', 'uuvv', 'wwxx', 'yyzz'],chars = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 66
    assert candidate(words = ['complex', 'words', 'here'],chars = "owcpxlehre") == 4
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'abacax'],chars = "abcdefghijklmnopqrstuvwxyz") == 52
    assert candidate(words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],chars = "oentwfhivxsg") == 21
    assert candidate(words = ['xxyyzz', 'yyzzxx', 'zzxxyy'],chars = "xyzxyz") == 18
    assert candidate(words = ['aabbccddeeff', 'aabbccddeeffgg', 'aabbccddeeffgghh', 'aabbccddeeffgghhiijj'],chars = "aabbccddeeffgghhiijj") == 62
    assert candidate(words = ['zzzz', 'zzz', 'zz', 'z'],chars = "zzzzzzzzzz") == 10
    assert candidate(words = ['xylophone', 'guitar', 'drum', 'bassoon', 'violin'],chars = "guitardrumxyz") == 10
    assert candidate(words = ['leetcode', 'challenge', 'contest', 'question'],chars = "oelhctganegqisun") == 8
    assert candidate(words = ['abacax', 'banana', 'grape'],chars = "aaabbnagpr") == 0
    assert candidate(words = ['ab', 'ba', 'abc', 'bca', 'acb', 'cab', 'cba', 'bac', 'bca', 'acb', 'cab', 'cba', 'bac', 'bca', 'acb', 'cab', 'cba', 'bac', 'bca', 'acb', 'cab', 'cba', 'bac', 'bca', 'acb', 'cab', 'cba', 'bac', 'bca', 'acb', 'cab', 'cba'],chars = "abc") == 94
    assert candidate(words = ['alibaba', 'babala', 'baliba', 'lalala'],chars = "balibalab") == 19
    assert candidate(words = ['aabbcc', 'bbccdd', 'aaccdd'],chars = "aabbbccdd") == 18
    assert candidate(words = ['abcdefghij', 'jihgfedcba', 'hgfedcb', 'fedcbghij'],chars = "abcdefghij") == 36
    assert candidate(words = ['aabbccddeeffgg', 'bbccddeeffgghh', 'ccddeeffgghhiijj'],chars = "abcdefghij") == 0
    assert candidate(words = ['algorithm', 'data', 'structure', 'binary', 'search'],chars = "lgarithmtdastrucetubynrseahc") == 25
    assert candidate(words = ['abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk'],chars = "abcdefghij") == 27
    assert candidate(words = ['abcdabcd', 'dcbaabcd', 'abcd', 'abcd'],chars = "abcdabcd") == 24
    assert candidate(words = ['programming', 'challenge', 'difficulty', 'algorithm'],chars = "progaminld") == 0
    assert candidate(words = ['aabbcc', 'aabbc', 'aabb', 'aa', 'a'],chars = "aabbbcccc") == 18
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba'],chars = "abcdefghijklmnopqrstuvwxyz") == 52
    assert candidate(words = ['multiple', 'words', 'with', 'same', 'letters'],chars = "mlpuwihswtael") == 16
    assert candidate(words = ['abcd', 'abcde', 'abcdef'],chars = "abcdefg") == 15
    assert candidate(words = ['hello', 'world', 'python', 'programming'],chars = "helloworldpython") == 16
    assert candidate(words = ['abc', 'abcd', 'abcde', 'abcdef', 'abcdefg'],chars = "abcdefg") == 25
    assert candidate(words = ['aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz', 'zz', 'yy', 'xx'],chars = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 58
    assert candidate(words = ['optimization', 'algorithm', 'datastructure'],chars = "odginatrlhms") == 9
    assert candidate(words = ['short', 'longerword', 'evenlonger', 'longestword', 'tiny'],chars = "longestword") == 11
    assert candidate(words = ['algorithm', 'data', 'structure'],chars = "algorithmdstuct") == 9
    assert candidate(words = ['aabbcc', 'abcabc', 'abacbc'],chars = "aabbcc") == 18
    assert candidate(words = ['aabbccddeeff', 'gghhiijjkk', 'llmmnnoopp', 'qqrrssttuu', 'vvwwxxyyzz'],chars = "abcdefghijklmnopqrstuvwxyz") == 0
    assert candidate(words = ['mississippi', 'tennessee', 'delaware', 'georgia', 'alabama'],chars = "mississippitennessegeorgiaalamaba") == 34
    assert candidate(words = ['unique', 'words', 'here'],chars = "unewordhsere") == 9
    assert candidate(words = ['x', 'xx', 'xxx', 'xxxx', 'xxxxx', 'xxxxxx', 'xxxxxxx', 'xxxxxxxx', 'xxxxxxxxx', 'xxxxxxxxxx'],chars = "x") == 1
    assert candidate(words = ['abcd', 'dcba', 'dcba', 'abcd', 'abcd'],chars = "abcdabcdabcd") == 20
    assert candidate(words = ['aaaaaabbbbcccc', 'bbbbbcccccc', 'cccccccc', 'ddddd'],chars = "aabbbccccdddd") == 0
    assert candidate(words = ['repeated', 'repeated', 'repeated', 'repeated'],chars = "repeead") == 0
    assert candidate(words = ['programming', 'code', 'challenge'],chars = "mprogainlce") == 0
    assert candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'],chars = "abc") == 18
    assert candidate(words = ['repeat', 'repear', 'preear', 'pareer'],chars = "reapeart") == 24
    assert candidate(words = ['unique', 'unigue', 'uneque'],chars = "unequiq") == 6
    assert candidate(words = ['programming', 'is', 'fun'],chars = "gimnoprrstu") == 2
    assert candidate(words = ['mississippi', 'mississippi', 'mississippi', 'mississippi'],chars = "misp") == 0
    assert candidate(words = ['abcdefg', 'bcdefga', 'cdefgab'],chars = "abcdefg") == 21
    assert candidate(words = ['abcdefghij', 'jihgfedcba', 'abcde', 'edcba'],chars = "abcdefghijabcdefghij") == 30
    assert candidate(words = ['abcd', 'dcba', 'abdc', 'dabc'],chars = "abcd") == 16
    assert candidate(words = ['unique', 'characters', 'only', 'here'],chars = "uneicharstolonhyer") == 8
    assert candidate(words = ['repeated', 'letters', 'example'],chars = "repateledmx") == 15
    assert candidate(words = ['programming', 'python', 'java', 'coding'],chars = "gnimmargorpthonavajgnidoc") == 21
    assert candidate(words = ['aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz'],chars = "abcdefghijklmnopqrstuvwxyz") == 0
    assert candidate(words = ['mississippi', 'missouri', 'mismatch', 'miss'],chars = "mississippi") == 15
    assert candidate(words = ['abcdefghijk', 'klmno', 'pqrstuvw', 'xyz', 'mnopqr', 'stuv', 'wxyz'],chars = "abcdefghijklmnopqrstuvwxyz") == 41
    assert candidate(words = ['abacax', 'banana', 'grape'],chars = "aabacax") == 6
    assert candidate(words = ['programming', 'python', 'java'],chars = "pgoramythnvaj") == 10
    assert candidate(words = ['unique', 'words', 'only', 'once'],chars = "nuqowinco") == 0
    assert candidate(words = ['programming', 'python', 'java', 'algorithm'],chars = "pgmnoaahjy") == 0
    assert candidate(words = ['aabbccddeeff', 'zzzzzzzzzz', 'yyyyyyyyyy'],chars = "abcdefzy") == 0
    assert candidate(words = ['aaaaaaaa', 'bbbbbbbb', 'cccccccc', 'dddddddd'],chars = "abcd") == 0
    assert candidate(words = ['longerword', 'evenlongerword', 'superduperlongword'],chars = "lorenwdsupem") == 0
    assert candidate(words = ['repeated', 'characters', 'here', 'are', 'some'],chars = "reepeaddttcharseom") == 19
    assert candidate(words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],chars = "enifxsv") == 7
    assert candidate(words = ['testtest', 'testtest', 'testtest'],chars = "ttttseeeesss") == 24
    assert candidate(words = ['abcd', 'dcba', 'efgh', 'hgfe'],chars = "abcdefgh") == 16
    assert candidate(words = ['qwerty', 'asdfgh', 'zxcvbn'],chars = "qwertyasdfghzxcvbn") == 18
    assert candidate(words = ['abacax', 'bacax', 'cax', 'ax', 'x'],chars = "abacax") == 17
    assert candidate(words = ['mississippi', 'babbling', 'bookkeeper'],chars = "bmkpeorins") == 0
    assert candidate(words = ['repeated', 'characters', 'example', 'strings', 'test'],chars = "eeptxsa") == 0
    assert candidate(words = ['this', 'is', 'a', 'test', 'case'],chars = "tastciehins") == 15
    assert candidate(words = ['banana', 'bandana', 'bandanna'],chars = "bandanabandana") == 21
    assert candidate(words = ['encyclopedia', 'dictionary', 'thesaurus'],chars = "ctheosuraind") == 0
    assert candidate(words = ['longword', 'another', 'wordset'],chars = "longanotwrheds") == 22
    assert candidate(words = ['repeated', 'characters', 'in', 'strings'],chars = "repachint") == 2
    assert candidate(words = ['unique', 'words', 'only', 'once'],chars = "euqinowrsc") == 4
    assert candidate(words = ['encyclopedia', 'dictionary', 'encyclopedia', 'encyclopediab'],chars = "encyclopedia") == 24
    assert candidate(words = ['banana', 'apple', 'orange', 'grape', 'peach'],chars = "aapplleeorrnggbnpppe") == 16
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],chars = "zyxwvutsrqponmlkjihgfedcba") == 26
    assert candidate(words = ['abracadabra', 'barack', 'rac', 'cabra'],chars = "abracadabra") == 19
    assert candidate(words = ['abcdefgh', 'ijklmnop', 'qrstuvwx', 'yz'],chars = "abcdefghijklmnopqrstuvwxyz") == 26
    assert candidate(words = ['algorithm', 'datastructure', 'programming'],chars = "datastructureprogramming") == 24
    assert candidate(words = ['one', 'two', 'three', 'four', 'five'],chars = "onethreefourfive") == 16
    assert candidate(words = ['mississippi', 'baby', 'racecar', 'level', 'rotor'],chars = "ississippiabaycerracelevrotor") == 12
    assert candidate(words = ['repetition', 'representation', 'reform'],chars = "repitnfom") == 0
    assert candidate(words = ['longwordhere', 'anotherlongword', 'shortword'],chars = "lnwordhertahoes") == 9
    assert candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],chars = "abcdefghijklmnopqrstuvwxyz") == 26
    assert candidate(words = ['abcd', 'abce', 'abcf'],chars = "abcd") == 4
    assert candidate(words = ['abcd', 'abac', 'aabc', 'abcc', 'accc'],chars = "abcc") == 4
    assert candidate(words = ['mississippi', 'elephant', 'umbrella', 'java', 'python'],chars = "ieelmpstuvy") == 0
    assert candidate(words = ['aabbcc', 'abcabc', 'ccabba', 'baccab'],chars = "aabbcc") == 24
    assert candidate(words = ['algorithm', 'data', 'structure'],chars = "gahlimstrucotad") == 13
    assert candidate(words = ['abcdefgh', 'ijklmnop', 'qrstuvwx', 'yzabcd', 'efghij', 'klmnopqr', 'stuvwx', 'yzabcd', 'efghij', 'klmnopqr', 'stuvwx'],chars = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == 76
    assert candidate(words = ['abcdabcd', 'abcdabcdabcd', 'abcdabcdabcdabcd', 'abcd'],chars = "abcdabcdabcdabcd") == 40
    assert candidate(words = ['supercalifragilisticexpialidocious', 'antidisestablishmentarianism', 'floccinaucinihilipilification'],chars = "supercalifragilisticexpialidociousantidisestablishmentarianismfloccinaucinihilipilification") == 91
    assert candidate(words = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba', 'mnopqrstuvwxyzabcde'],chars = "abcdefghijklmnopqrstuvwxyzzzzzzzzzz") == 71
    assert candidate(words = ['elephant', 'giraffe', 'hippopotamus'],chars = "eplhgaifeotmups") == 0
    assert candidate(words = ['repeat', 'repeat', 'repeat', 'repeat'],chars = "eprta") == 0
    assert candidate(words = ['hello', 'world', 'leetcode', 'challenge'],chars = "helloworldleetcodechallenge") == 27
    assert candidate(words = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yz'],chars = "abcdefghijklmnopqrstuvwxyz") == 26
    assert candidate(words = ['stackoverflow', 'overflow', 'underflow', 'flow'],chars = "flowover") == 12
    assert candidate(words = ['supercalifragilisticexpialidocious', 'supercalifragilistic', 'califragilistic', 'expialidocious'],chars = "supercalifragilisticexpialidocious") == 83
    assert candidate(words = ['umbrella', 'balloon', 'orange'],chars = "mnbaylobnragoe") == 6
    assert candidate(words = ['xylophone', 'triangle', 'piano', 'drum', 'guitar'],chars = "tpirangedumxylophone") == 32
    assert candidate(words = ['abcdefg', 'hijklmn', 'opqrstu', 'vwxyz'],chars = "zyxwvutsrqponmlkjihgfedcba") == 26
    assert candidate(words = ['character', 'char', 'act', 'react', 'actchar'],chars = "character") == 28
    assert candidate(words = ['programming', 'language', 'python', 'java', 'javascript', 'c', 'cpp'],chars = "pgoramlngyjtahivsc") == 21
