# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(stickers = ['aaa', 'bbb'],target = "aabbbccc") == -1
    assert candidate(stickers = ['a', 'b', 'c'],target = "abc") == 3
    assert candidate(stickers = ['abc', 'abc'],target = "abcabc") == 2
    assert candidate(stickers = ['abcd'],target = "abcdabcd") == 2
    assert candidate(stickers = ['abc'],target = "d") == -1
    assert candidate(stickers = ['notice', 'possible'],target = "basicbasic") == -1
    assert candidate(stickers = ['abc'],target = "abcd") == -1
    assert candidate(stickers = ['abc', 'ab', 'bc'],target = "abc") == 1
    assert candidate(stickers = ['abc', 'def'],target = "abcdef") == 2
    assert candidate(stickers = ['a'],target = "a") == 1
    assert candidate(stickers = ['aabbcc', 'abc'],target = "aabbbccc") == 2
    assert candidate(stickers = ['hello', 'world'],target = "hold") == 2
    assert candidate(stickers = ['abc', 'def', 'ghi'],target = "adgbehcfi") == 3
    assert candidate(stickers = ['aabb', 'ccdd'],target = "abcd") == 2
    assert candidate(stickers = ['with', 'example', 'science'],target = "thehat") == 3
    assert candidate(stickers = ['hello', 'world'],target = "helloworld") == 2
    assert candidate(stickers = ['aaa', 'aa', 'a'],target = "aaaaaaaaa") == 3
    assert candidate(stickers = ['xyz', 'zyx', 'yxz'],target = "zyxyzyxyzyx") == 5
    assert candidate(stickers = ['hello', 'world', 'again'],target = "aginwodlloleh") == 3
    assert candidate(stickers = ['abcdef', 'ghijkl', 'mnopqr'],target = "abcdefghijklmnopqr") == 3
    assert candidate(stickers = ['mississippi', 'helloworld'],target = "mississippiworldhello") == 2
    assert candidate(stickers = ['aabb', 'bbcc', 'cdda'],target = "aabbccddaabb") == 4
    assert candidate(stickers = ['sun', 'moon', 'star'],target = "starstarsun") == 3
    assert candidate(stickers = ['one', 'two', 'three', 'four', 'five'],target = "onetwothreefourfive") == 5
    assert candidate(stickers = ['mississippi', 'pennsylvania'],target = "mississippipennsylvania") == 2
    assert candidate(stickers = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee'],target = "abcdeabcde") == 5
    assert candidate(stickers = ['flower', 'garden', 'sun', 'moon', 'star'],target = "flowergardenstar") == 3
    assert candidate(stickers = ['aabbcc', 'abcabc', 'aabbc'],target = "abcabcabc") == 2
    assert candidate(stickers = ['alphabet', 'soup', 'letters', 'words', 'sticker', 'pack'],target = "alphabetwordsoupstickersoup") == 5
    assert candidate(stickers = ['ab', 'bc', 'cd'],target = "abcdabcd") == 4
    assert candidate(stickers = ['quick', 'brown', 'fox'],target = "quickbrownfox") == 3
    assert candidate(stickers = ['abcd', 'efgh', 'ijkl'],target = "dgheijlkfabci") == 4
    assert candidate(stickers = ['apple', 'banana', 'cherry'],target = "bananaapple") == 2
    assert candidate(stickers = ['red', 'blue', 'green'],target = "bluegreenred") == 3
    assert candidate(stickers = ['abcd', 'dcba', 'abdc', 'bacd'],target = "abcdabcd") == 2
    assert candidate(stickers = ['zzz', 'zzzz', 'zzzzz'],target = "zzzzzzzzzzzzzzz") == 3
    assert candidate(stickers = ['programming', 'is', 'fun'],target = "funisprogramming") == 3
    assert candidate(stickers = ['leetcode', 'love', 'coding'],target = "lovecodingleetcode") == 3
    assert candidate(stickers = ['hello', 'world', 'python'],target = "pythonhello") == 2
    assert candidate(stickers = ['aabbcc', 'abc', 'abac'],target = "aabbccabc") == 2
    assert candidate(stickers = ['abacd', 'bdfgh', 'cdhij', 'efgik', 'ghklm'],target = "abcdefghijklim") == 4
    assert candidate(stickers = ['hello', 'world', 'again'],target = "againhelloagainworld") == 4
    assert candidate(stickers = ['puzzle', 'piece', 'fit'],target = "fittingpuzzle") == -1
    assert candidate(stickers = ['happy', 'birthday', 'friend'],target = "happybirthdayfriend") == 3
    assert candidate(stickers = ['aaa', 'bbb', 'ccc'],target = "aabbbccc") == 3
    assert candidate(stickers = ['hello', 'world', 'abc', 'def', 'ghi', 'jkl'],target = "helloworldabcdefghijk") == 6
    assert candidate(stickers = ['sunshine', 'rainbow', 'cloud'],target = "sunshinecloud") == 2
    assert candidate(stickers = ['xyz', 'abc', 'def', 'ghi'],target = "zyxwvutsrqponmlkjihgfedcba") == -1
    assert candidate(stickers = ['zoo', 'book', 'look'],target = "bookzoolook") == 3
    assert candidate(stickers = ['magic', 'wand', 'spell'],target = "spellmagic") == 2
    assert candidate(stickers = ['aabbcc', 'bbccdd', 'aaccdd'],target = "aabbccddee") == -1
    assert candidate(stickers = ['cat', 'dog', 'bird'],target = "cattog") == 3
    assert candidate(stickers = ['orange', 'juice', 'smoothie'],target = "smoothieorangejuice") == 3
    assert candidate(stickers = ['aabb', 'bbcc', 'ccdd'],target = "bbaaccd") == 2
    assert candidate(stickers = ['quick', 'brown', 'fox', 'jumps', 'over', 'lazy'],target = "quickbrownfoxjumpsoveralazydog") == -1
    assert candidate(stickers = ['algorithm', 'data', 'structure'],target = "datadstructure") == 3
    assert candidate(stickers = ['cat', 'bat', 'rat', 'car'],target = "catabtar") == 3
    assert candidate(stickers = ['zebra', 'lion', 'tiger'],target = "tigerlionzebra") == 3
    assert candidate(stickers = ['apple', 'banana', 'cherry'],target = "bananaapplecherry") == 3
    assert candidate(stickers = ['algorithm', 'data', 'structure'],target = "algorithmdatastructure") == 3
    assert candidate(stickers = ['repeat', 'again', 'once'],target = "repeatagainonce") == 3
    assert candidate(stickers = ['sticker', 'stamps', 'books'],target = "tsickerbomskps") == 3
    assert candidate(stickers = ['abcd', 'dcba', 'efgh', 'hgf', 'ijkl', 'lkji'],target = "abcdefghijklij") == 4
    assert candidate(stickers = ['abcdefg', 'ghijklm', 'nopqrstu', 'vwxyz'],target = "abcdefghijklmnopqrstuvwxyz") == 4
    assert candidate(stickers = ['aaaa', 'bbbb', 'cccc'],target = "aabbcc") == 3
    assert candidate(stickers = ['aabbccddeeff', 'bbccddeeffgghh', 'ccddeeffgghhiijj'],target = "aabbccddeeffgghhiijj") == 2
    assert candidate(stickers = ['sticker', 'book', 'a'],target = "stickers") == 2
    assert candidate(stickers = ['x', 'y', 'z'],target = "zyxzyxzyx") == 9
    assert candidate(stickers = ['abcd', 'efgh', 'ijkl'],target = "ijklabcdeffgh") == 4
    assert candidate(stickers = ['sticker', 'book', 'target'],target = "booktarget") == 2
    assert candidate(stickers = ['hello', 'world', 'python'],target = "pythonworldhello") == 3
    assert candidate(stickers = ['aabbcc', 'ddeeff', 'gghhii', 'jjkkll', 'mmnnoo'],target = "aabbccddeeffgghhiijjkkllmmnnoo") == 5
    assert candidate(stickers = ['jump', 'over', 'lazy'],target = "jumplazyover") == 3
    assert candidate(stickers = ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzabcd'],target = "abcdefghijklmnopqrstuvwxyz") == 5
    assert candidate(stickers = ['abcdefghij', 'klmnopqrst', 'uvwxyz', 'mnopqrstuv', 'wxyzabcde'],target = "zyxwvutsrqponmlkjihgfedcba") == 3
    assert candidate(stickers = ['hello', 'world', 'again'],target = "helloworldhelloagainworld") == 5
    assert candidate(stickers = ['unique', 'letters'],target = "uniquelettersuniqueletters") == 4
    assert candidate(stickers = ['cat', 'dog', 'bird'],target = "birdcatdog") == 3
    assert candidate(stickers = ['example', 'science', 'with'],target = "thehatexample") == 4
    assert candidate(stickers = ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yz'],target = "abcdefghijklmnopqrstuvwxyz") == 5
    assert candidate(stickers = ['laptop', 'phone', 'tablet'],target = "telephonetablet") == 4
    assert candidate(stickers = ['abcd', 'efgh', 'ijkl'],target = "abcdefghijlkl") == 4
    assert candidate(stickers = ['abcdef', 'ghijkl', 'mnopqr'],target = "mnopqrfedcba") == 2
    assert candidate(stickers = ['overlap', 'partial', 'coverage'],target = "overlappartialcoverage") == 3
    assert candidate(stickers = ['aabb', 'bbcc', 'ccdd', 'ddeeff', 'ffgg'],target = "aabbccddeeffgg") == 4
    assert candidate(stickers = ['zzz', 'yyy', 'xxx', 'www'],target = "zzzyyyxxxwww") == 4
    assert candidate(stickers = ['coding', 'is', 'fun'],target = "sindgnif") == 3
    assert candidate(stickers = ['happy', 'birthday', 'party'],target = "birthdaypartyparty") == 3
    assert candidate(stickers = ['zzzz', 'yyyy', 'xxxx'],target = "zyxwvutsrqponmlkjihgfedcba") == -1
    assert candidate(stickers = ['pizza', 'pie', 'cake'],target = "pizzacakepie") == 3
    assert candidate(stickers = ['fox', 'quick', 'brown'],target = "brownquickfox") == 3
    assert candidate(stickers = ['sticky', 'loop', 'again'],target = "programming") == -1
    assert candidate(stickers = ['python', 'java', 'cplus'],target = "javapythoncpluspython") == 4
    assert candidate(stickers = ['steak', 'egg', 'bacon'],target = "eggnestake") == 4
    assert candidate(stickers = ['xy', 'yz', 'zx'],target = "xyzyzxzyxzyzx") == 7
    assert candidate(stickers = ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx', 'yzabcd', 'efghij', 'klmnop', 'qrstuv', 'wxzyab'],target = "abcdefghijklmnopqrstuvwxyzabc") == 5
    assert candidate(stickers = ['one', 'two', 'three', 'four', 'five', 'six'],target = "onetwothreefourfivesix") == 6
    assert candidate(stickers = ['one', 'two', 'three'],target = "onetwothreeonetwothree") == 6
    assert candidate(stickers = ['dog', 'cat', 'bird'],target = "catdogbird") == 3
    assert candidate(stickers = ['one', 'two', 'three'],target = "onetwothree") == 3
    assert candidate(stickers = ['red', 'green', 'blue'],target = "greenbluegreengreen") == 4
    assert candidate(stickers = ['up', 'down', 'left', 'right'],target = "rightleftdownup") == 4
    assert candidate(stickers = ['red', 'blue', 'green', 'yellow', 'purple'],target = "bluegreenyellowpurple") == 4
    assert candidate(stickers = ['one', 'two', 'three'],target = "threetwoone") == 3
    assert candidate(stickers = ['quick', 'brown', 'fox'],target = "uqcfkibrowno") == 3
    assert candidate(stickers = ['a', 'ab', 'abc', 'abcd', 'abcde'],target = "abcdeabcde") == 2
    assert candidate(stickers = ['cat', 'dog', 'bird'],target = "cogbat") == 3
    assert candidate(stickers = ['programming', 'in', 'python'],target = "grammipnnoingtih") == 4
    assert candidate(stickers = ['aabbcc', 'bbccdd', 'ccddeeff', 'ddeeffgg'],target = "aabbccddeeffgg") == 2
    assert candidate(stickers = ['apple', 'banana', 'cherry', 'date'],target = "abacaxibananacherry") == -1
    assert candidate(stickers = ['abcdefgh', 'ijklmnop', 'qrstuvwx', 'yz'],target = "abcdefghijklmnopqrstuvwxyz") == 4
    assert candidate(stickers = ['abc', 'bcd', 'cde', 'def', 'efg'],target = "abcdefg") == 3
    assert candidate(stickers = ['red', 'blue', 'green'],target = "greengreenblue") == 3
    assert candidate(stickers = ['hello', 'world', 'python'],target = "worldhellopython") == 3
    assert candidate(stickers = ['zzz', 'yyy', 'xxx'],target = "zzzyyyxxx") == 3
    assert candidate(stickers = ['fast', 'food', 'truck'],target = "truckfastfood") == 3
    assert candidate(stickers = ['abcd', 'dcba', 'abcd'],target = "abcdabcdabcd") == 3
    assert candidate(stickers = ['aabbcc', 'ddeeff', 'gghhii'],target = "abcdefghi") == 3
    assert candidate(stickers = ['hello', 'world', 'foo', 'bar', 'baz'],target = "helloworldfoobarbaz") == 5
    assert candidate(stickers = ['hello', 'world', 'python', 'programming'],target = "helloprogrammingworld") == 3
    assert candidate(stickers = ['repeated', 'words', 'here'],target = "repeatedwordshere") == 3
    assert candidate(stickers = ['happy', 'new', 'year'],target = "happynewyear") == 3
    assert candidate(stickers = ['jump', 'high', 'long'],target = "highjumplong") == 3
    assert candidate(stickers = ['sticker', 'sticker', 'sticker'],target = "stickers") == 2
    assert candidate(stickers = ['ab', 'cd', 'ef', 'gh', 'ij', 'kl', 'mn', 'op', 'qr', 'st', 'uv', 'wx', 'yz'],target = "abcdefghijklmnopqrstuvwxyz") == 13
    assert candidate(stickers = ['ab', 'bc', 'ca'],target = "abcabcabc") == 5
    assert candidate(stickers = ['repeated', 'words', 'here', 'in', 'this', 'example'],target = "repeatedwordshereinthisexample") == 6
    assert candidate(stickers = ['abcd', 'efgh', 'ijkl'],target = "fedcbahjiglke") == 4
    assert candidate(stickers = ['hello', 'world', 'wide'],target = "worldwide") == 2
    assert candidate(stickers = ['abcdefg', 'hijklmn', 'opqrstu', 'vwxyz'],target = "abcdefghijklmnopqrstuvwxyz") == 4
    assert candidate(stickers = ['jump', 'over', 'lazy'],target = "lazyjumpover") == 3
    assert candidate(stickers = ['sun', 'moon', 'star'],target = "moonstarsun") == 3
    assert candidate(stickers = ['apple', 'orange', 'banana'],target = "poeplange") == 2
    assert candidate(stickers = ['one', 'two', 'three'],target = "threethreetwoone") == 4
    assert candidate(stickers = ['xylophone', 'piano', 'violin'],target = "xylophonepianoviolin") == 3
    assert candidate(stickers = ['aabbcc', 'bbccdd', 'ccddaa'],target = "aabbccbbccddccddaa") == 3
    assert candidate(stickers = ['abcdef', 'abcde', 'abcd'],target = "abcdef") == 1
    assert candidate(stickers = ['abcde', 'fghij', 'klmno'],target = "ejihfckgmldnbaio") == 4
    assert candidate(stickers = ['abcdef', 'ghijkl', 'mnopqr'],target = "jklmnopqrfgedbica") == 3
    assert candidate(stickers = ['abc', 'def', 'ghi', 'jkl'],target = "abcdefghijkln") == -1
    assert candidate(stickers = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy'],target = "abcdefghijklmnopqrstuvwxyz") == -1
    assert candidate(stickers = ['quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog'],target = "quickbrownfoxjumpsoverlazydog") == 7
    assert candidate(stickers = ['race', 'car', 'seat'],target = "crecarstae") == 3
    assert candidate(stickers = ['xy', 'yx', 'zz'],target = "zyxzyxzyx") == 5
    assert candidate(stickers = ['xy', 'yz', 'za', 'ax'],target = "xyzaxyzaxyza") == 6
    assert candidate(stickers = ['cat', 'dog', 'bird'],target = "birdcattwo") == -1
