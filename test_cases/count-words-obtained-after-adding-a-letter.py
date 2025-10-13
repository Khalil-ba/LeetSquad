# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(startWords = ['ant', 'act', 'tack'],targetWords = ['tack', 'act', 'acti']) == 2
    assert candidate(startWords = ['ab', 'a'],targetWords = ['abc', 'abcd']) == 1
    assert candidate(startWords = ['pqrst', 'vwxyz', 'abcdef'],targetWords = ['qrstuvw', 'vwxyzab', 'abcdefg', 'pqrstuv', 'mnopqr']) == 1
    assert candidate(startWords = ['python', 'java', 'c'],targetWords = ['pythonx', 'javaz', 'cb']) == 3
    assert candidate(startWords = ['abcdexyz', 'mnopqr', 'stuv'],targetWords = ['abcdexyzw', 'mnopqrs', 'stuvq']) == 3
    assert candidate(startWords = ['python', 'java', 'csharp'],targetWords = ['pythonic', 'javacoffee', 'csharptool', 'pythonjava', 'javacsharp']) == 0
    assert candidate(startWords = ['abc', 'def', 'ghi', 'jkl', 'mno'],targetWords = ['abcd', 'abce', 'abcf', 'abck', 'abcm']) == 5
    assert candidate(startWords = ['xyz', 'uvw', 'rst'],targetWords = ['xyza', 'uvwq', 'rstv', 'rstw']) == 4
    assert candidate(startWords = ['abcd', 'bcde', 'cdef'],targetWords = ['abcde', 'bcdefg', 'abcdef', 'bcd']) == 1
    assert candidate(startWords = ['a', 'bc', 'def', 'ghij', 'klmno'],targetWords = ['ab', 'bcd', 'cdef', 'defgh', 'efghij', 'fghijk']) == 3
    assert candidate(startWords = ['abcde', 'fghij', 'klmno'],targetWords = ['bcdef', 'ghijk', 'klmnoa', 'mnopqr', 'stuvwx']) == 1
    assert candidate(startWords = ['hello', 'world', 'abc'],targetWords = ['helloa', 'worldb', 'abcd']) == 3
    assert candidate(startWords = ['mnopqr', 'stuvwx', 'yzabcd'],targetWords = ['mnopqrs', 'stuvwxy', 'yzabcde', 'mnopqrst', 'stuvwxyz', 'yzabcdef', 'mnopqrstuv', 'stuvwxyzab', 'yzabcdefg', 'mnopqrstu', 'stuvwxyzabc', 'yzabcdefg', 'mnopqrstuvw', 'stuvwxyzabcd', 'yzabcdefgh', 'mnopqrstuvwx', 'stuvwxyzabcde', 'yzabcdefgij', 'mnopqrstuvwxy', 'stuvwxyzabcdef', 'yzabcdefgijk']) == 3
    assert candidate(startWords = ['xyz', 'uvw', 'qrst'],targetWords = ['xyza', 'uvwxy', 'qrstuv', 'qrstuvw', 'uvwq']) == 2
    assert candidate(startWords = ['mnopqr', 'stuvwx', 'yzabcd', 'efghij', 'klmno'],targetWords = ['mnopqrs', 'stuvwxy', 'yzabcdx', 'efghijk', 'klmnop', 'abcdefgh']) == 5
    assert candidate(startWords = ['abc', 'def', 'ghi'],targetWords = ['abcd', 'abcf', 'defg', 'ghij']) == 4
    assert candidate(startWords = ['abc', 'def', 'ghi'],targetWords = ['abcd', 'efg', 'hij', 'defg', 'ghik']) == 3
    assert candidate(startWords = ['xyz', 'mnop', 'qrst'],targetWords = ['xyzw', 'mnopq', 'qrstuvw']) == 2
    assert candidate(startWords = ['a', 'b', 'c', 'd'],targetWords = ['ab', 'bc', 'cd', 'da', 'abc', 'bcd', 'cda', 'dab']) == 4
    assert candidate(startWords = ['abcdefghij', 'klmnopqr', 'stuvwxyz'],targetWords = ['abcdefghijk', 'klmnopqrs', 'stuvwxyzab', 'abcdefghijl', 'klmnopqrt', 'stuvwxyzabc', 'abcdefghijm', 'klmnopqru', 'stuvwxyzabcd', 'abcdefghijn', 'klmnopqrv', 'stuvwxyzabcde', 'abcdefghijo', 'klmnopqrw', 'stuvwxyzabcdef', 'abcdefghijp', 'klmnopqrx', 'stuvwxyzabcdefg', 'abcdefghirq', 'klmnopqry', 'stuvwxyzabcdefgh', 'abcdefghirs', 'klmnopqrz', 'stuvwxyzabcdefghi', 'abcdefghirt', 'klmnopqs', 'stuvwxyzabcdefghij', 'abcdefghiru', 'klmnopqt', 'stuvwxyzabcdefghijk', 'abcdefghirv', 'klmnopqu', 'stuvwxyzabcdefghijl', 'abcdefghirw', 'klmnopqv', 'stuvwxyzabcdefghijm', 'abcdefghirx', 'klmnopqw', 'stuvwxyzabcdefghijn', 'abcdefghiry', 'klmnopqx', 'stuvwxyzabcdefghijo', 'abcdefghirz', 'klmnopqy', 'stuvwxyzabcdefghijp', 'klmnopqz', 'stuvwxyzabcdefghirq']) == 14
    assert candidate(startWords = ['quick', 'brown', 'fox'],targetWords = ['quicks', 'brownf', 'foxj', 'quickm', 'brownx']) == 5
    assert candidate(startWords = ['a', 'b', 'c'],targetWords = ['ab', 'bc', 'ca', 'abc', 'abcd']) == 3
    assert candidate(startWords = ['abc', 'def', 'ghi'],targetWords = ['abcd', 'efg', 'ghij']) == 2
    assert candidate(startWords = ['zebra', 'dog', 'cat'],targetWords = ['zebrao', 'doge', 'taco']) == 3
    assert candidate(startWords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],targetWords = ['ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'ha']) == 8
    assert candidate(startWords = ['abcdefgh', 'ijklmnop', 'qrstuvwxyz'],targetWords = ['abcdefghi', 'ijklmnopq', 'qrstuvwxyzx', 'abcdefghjkl', 'ijklmnopqr']) == 2
    assert candidate(startWords = ['xyz', 'abc', 'uvw', 'def', 'ghi'],targetWords = ['xyzab', 'uvwxy', 'defgh', 'abcdef', 'mnopq']) == 0
    assert candidate(startWords = ['pqr', 'stu', 'vwx'],targetWords = ['pqrs', 'stuv', 'vwxy', 'pqrst', 'stuvw', 'vwxys', 'mnopq']) == 3
    assert candidate(startWords = ['quick', 'brown', 'fox'],targetWords = ['quickly', 'brownly', 'foxes', 'quickbrown', 'brownfox']) == 0
    assert candidate(startWords = ['a', 'b', 'c', 'd'],targetWords = ['ab', 'bc', 'cd', 'abc', 'abcd']) == 3
    assert candidate(startWords = ['aabbcc', 'ddeeff', 'gghhii'],targetWords = ['aabbccx', 'ddeeffx', 'gghhia', 'ddeeffg', 'gghhiih']) == 2
    assert candidate(startWords = ['abcdef', 'ghijkl', 'mnopqr', 'stuvwx'],targetWords = ['abcdefg', 'ghijklm', 'mnopqrs', 'stuvwxz', 'abcdefghijklmnopqrstuvwxyza', 'ghijklmnopqrstuvwxyz', 'mnopqrstuvwxyzabc', 'stuvwxyzmnopqr']) == 4
    assert candidate(startWords = ['abc', 'de', 'fgh', 'xyz'],targetWords = ['abcd', 'def', 'efg', 'xyzz']) == 2
    assert candidate(startWords = ['jump', 'over', 'lazy'],targetWords = ['jumpo', 'overj', 'lazyr', 'jumpr', 'overv']) == 4
    assert candidate(startWords = ['mnop', 'qrst', 'uvwx'],targetWords = ['mnopq', 'qrstu', 'vwxyz', 'mnopqr', 'qrstuv']) == 2
    assert candidate(startWords = ['abcd', 'efgh', 'ijkl'],targetWords = ['abcde', 'efghi', 'ijklm', 'abcdx', 'efghy', 'ijklz']) == 6
    assert candidate(startWords = ['hello', 'world', 'abc'],targetWords = ['helloz', 'worldy', 'abcd']) == 3
    assert candidate(startWords = ['mnop', 'qrst', 'uvwx'],targetWords = ['mnopq', 'qrstuv', 'uvwxy', 'mnopqr', 'qrstuvw', 'uvwxzy', 'mnopqrst', 'qrstuvwx', 'uvwxyza', 'mnopqrstuvwxyz']) == 2
    assert candidate(startWords = ['programming', 'is', 'fun'],targetWords = ['programmings', 'isis', 'funny', 'programmingis', 'isfun']) == 0
    assert candidate(startWords = ['jump', 'over', 'lazy'],targetWords = ['jumped', 'overly', 'lazily', 'jumpover', 'overlazy']) == 0
    assert candidate(startWords = ['abcdefghij'],targetWords = ['abcdefghijk', 'abcdefghijl', 'abcdefghijm', 'abcdefghijn', 'abcdefghijo', 'abcdefghijp', 'abcdefghijq', 'abcdefghijr', 'abcdefghjis', 'abcdefghijt', 'abcdefghiju', 'abcdefghijv', 'abcdefghijw', 'abcdefghijx', 'abcdefghijy', 'abcdefghijz']) == 16
    assert candidate(startWords = ['abc', 'bcd', 'efg'],targetWords = ['abcd', 'bcde', 'efgh']) == 3
    assert candidate(startWords = ['zebra', 'panda', 'giraffe'],targetWords = ['zebrac', 'pandaf', 'giraffeb', 'zebrad', 'pandaq']) == 5
    assert candidate(startWords = ['jump', 'over', 'lazy'],targetWords = ['jumper', 'overt', 'lazier']) == 1
    assert candidate(startWords = ['a', 'b', 'c'],targetWords = ['ab', 'bc', 'ca', 'abc', 'abcd', 'abcde']) == 3
    assert candidate(startWords = ['xyz', 'wxy', 'uvw'],targetWords = ['xyza', 'wxyb', 'uvwz', 'uvwxy']) == 3
    assert candidate(startWords = ['abcdefgh', 'ijklmnop', 'qrstuvwxyz', 'abcxyz', 'uvwxy'],targetWords = ['abcdefghi', 'ijklmnopq', 'qrstuvwxyzx', 'abcxyzw', 'uvwxyza', 'mnopqrstu']) == 3
    assert candidate(startWords = ['abcd', 'efgh', 'ijkl'],targetWords = ['abcde', 'efghi', 'jklmn', 'abcd']) == 2
    assert candidate(startWords = ['abcd', 'efgh', 'ijkl'],targetWords = ['abcde', 'efghi', 'ijklm', 'mnop']) == 3
    assert candidate(startWords = ['xyz', 'uvw', 'rst'],targetWords = ['xyza', 'uvwq', 'rstu', 'rstuv']) == 3
    assert candidate(startWords = ['abc', 'def', 'ghi'],targetWords = ['abcd', 'defg', 'ghij', 'hijk', 'mnop', 'qrst', 'uvw', 'xyz']) == 3
    assert candidate(startWords = ['quick', 'brown', 'fox'],targetWords = ['quickly', 'brownie', 'foxy', 'quicklybrown', 'brownief', 'quickbrown', 'quickfox', 'brownfox']) == 1
    assert candidate(startWords = ['abcdefghijklmnopqrstuvwxyz'],targetWords = ['abcdefghijklmnopqrstuvwxyza', 'abcdefghijklmnopqrstuvwxyzb']) == 0
    assert candidate(startWords = ['quick', 'brown', 'fox'],targetWords = ['quickly', 'brownish', 'foxy']) == 1
    assert candidate(startWords = ['apple', 'banana', 'cherry'],targetWords = ['appleb', 'bananac', 'cherryd', 'applef', 'bananag']) == 4
    assert candidate(startWords = ['abcd', 'efgh', 'ijkl'],targetWords = ['abcde', 'efghi', 'ijklm']) == 3
    assert candidate(startWords = ['one', 'two', 'three'],targetWords = ['onet', 'twot', 'threet', 'oneto', 'twoto', 'threeto', 'onetwo', 'twotwo', 'threetwo', 'onetwothree', 'twotwothree', 'threetwothree', 'onetwofour', 'twotwofour', 'threetwofour']) == 1
    assert candidate(startWords = ['abcd', 'efgh', 'ijkl'],targetWords = ['abcde', 'efghi', 'ijklm', 'mnopq']) == 3
    assert candidate(startWords = ['hello', 'world'],targetWords = ['hellow', 'worlds', 'dlrow']) == 2
    assert candidate(startWords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],targetWords = ['ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij', 'jk', 'kl', 'lm', 'mn', 'no', 'op', 'pq', 'qr', 'rs', 'st', 'tu', 'uv', 'vw', 'wx', 'xy', 'yz', 'za']) == 26
    assert candidate(startWords = ['zyxwvutsrqponmlkjihgfedcba'],targetWords = ['zyxwvutsrqponmlkjihgfedcbaz', 'zyxwvutsrqponmlkjihgfedcbay', 'zyxwvutsrqponmlkjihgfedcbax', 'zyxwvutsrqponmlkjihgfedcbaw']) == 0
    assert candidate(startWords = ['pqr', 'stu', 'vwx', 'yz', 'abc'],targetWords = ['pqrs', 'stuv', 'vwxy', 'yzab', 'uvwxy', 'mnopq']) == 3
    assert candidate(startWords = ['abcd', 'efgh', 'ijkl', 'mnop'],targetWords = ['abcde', 'efghi', 'ijklm', 'nopqr']) == 3
    assert candidate(startWords = ['hello', 'world'],targetWords = ['ehllo', 'dlrow', 'owrld', 'helloa', 'worldb']) == 2
    assert candidate(startWords = ['a', 'b', 'c', 'd'],targetWords = ['ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij', 'jk', 'kl', 'lm', 'mn', 'no', 'op', 'pq', 'qr', 'rs', 'st', 'tu', 'uv', 'vw', 'wx', 'xy', 'yz', 'za']) == 5
    assert candidate(startWords = ['mnopq', 'rstuv', 'wxyz'],targetWords = ['mnopqr', 'rstuvw', 'wxyza', 'mnopqs', 'rstuvx', 'wxyzab', 'mnopqt', 'rstuvy', 'wxyzac', 'mnopqu', 'rstuvz', 'wxyzad', 'mnopqv', 'rstuvw', 'wxyzae']) == 11
    assert candidate(startWords = ['abcdefghijklmnopqrstuvwxyz'],targetWords = ['abcdefghijklmnopqrstuvwxyza', 'abcdefghijklmnopqrstuvwxyzb', 'abcdefghijklmnopqrstuvwxyzc']) == 0
    assert candidate(startWords = ['a', 'b', 'c', 'd'],targetWords = ['ab', 'bc', 'cd', 'da']) == 4
