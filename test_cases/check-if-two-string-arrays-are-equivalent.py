# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(word1 = ['abc', 'd', 'defg'],word2 = ['abcddefg']) == True
    assert candidate(word1 = ['x'],word2 = ['y']) == False
    assert candidate(word1 = ['different'],word2 = ['string']) == False
    assert candidate(word1 = ['hello', 'world'],word2 = ['helloworld']) == True
    assert candidate(word1 = ['one', 'two', 'three'],word2 = ['onetwothree']) == True
    assert candidate(word1 = ['abc'],word2 = ['a', 'b', 'c']) == True
    assert candidate(word1 = ['abc'],word2 = ['ab', 'c']) == True
    assert candidate(word1 = ['xyz'],word2 = ['x', 'y', 'z']) == True
    assert candidate(word1 = ['hello', 'world'],word2 = ['helloWorld']) == False
    assert candidate(word1 = ['ab', 'c'],word2 = ['a', 'bc']) == True
    assert candidate(word1 = ['a'],word2 = ['a']) == True
    assert candidate(word1 = ['a', 'cb'],word2 = ['ab', 'c']) == False
    assert candidate(word1 = ['hello'],word2 = ['hello']) == True
    assert candidate(word1 = ['test'],word2 = ['t', 'es', 't']) == True
    assert candidate(word1 = ['a', 'b'],word2 = ['ab']) == True
    assert candidate(word1 = ['same', 'string'],word2 = ['same', 'string']) == True
    assert candidate(word1 = ['a', 'b', 'c'],word2 = ['a', 'b', 'c']) == True
    assert candidate(word1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g'],word2 = ['abcdefg']) == True
    assert candidate(word1 = ['split', 'in', 'pieces'],word2 = ['spli', 'tin', 'pi', 'eces']) == True
    assert candidate(word1 = ['a', 'b', 'c', 'd', 'e', 'f'],word2 = ['abcdef']) == True
    assert candidate(word1 = ['complex', 'string', 'example'],word2 = ['com', 'plex', 'string', 'ex', 'ample']) == True
    assert candidate(word1 = ['a', 'b', 'c'],word2 = ['ab', 'c']) == True
    assert candidate(word1 = ['same', 'same', 'same'],word2 = ['same', 'same', 'same']) == True
    assert candidate(word1 = ['split', 'this', 'up'],word2 = ['splitthis', 'up']) == True
    assert candidate(word1 = ['a', 'b', 'c'],word2 = ['d', 'e', 'f']) == False
    assert candidate(word1 = ['xyz', '123', 'abc'],word2 = ['xyz1', '23abc']) == True
    assert candidate(word1 = ['abcdef'],word2 = ['abc', 'd', 'e', 'f']) == True
    assert candidate(word1 = ['abcd', 'efgh', 'ijkl'],word2 = ['abcdefgh', 'ijkl']) == True
    assert candidate(word1 = ['abc', 'def'],word2 = ['abcdefg']) == False
    assert candidate(word1 = ['abc', 'def', 'ghi'],word2 = ['abc', 'd', 'efghi']) == True
    assert candidate(word1 = ['complex', 'word'],word2 = ['c', 'o', 'm', 'p', 'l', 'e', 'x', 'word']) == True
    assert candidate(word1 = ['partial', 'match'],word2 = ['partialm', 'atch']) == True
    assert candidate(word1 = ['a', 'bc', 'def', 'ghij'],word2 = ['abc', 'defghij']) == True
    assert candidate(word1 = ['equal', 'strings'],word2 = ['equalstrings']) == True
    assert candidate(word1 = ['example'],word2 = ['ex', 'ample']) == True
    assert candidate(word1 = ['complex', 'example'],word2 = ['com', 'plexex', 'ample']) == True
    assert candidate(word1 = ['abcdefg', 'hijklmn'],word2 = ['abc', 'defghijklmn']) == True
    assert candidate(word1 = ['same'],word2 = ['s', 'a', 'm', 'e']) == True
    assert candidate(word1 = ['long', 'word', 'sequence'],word2 = ['l', 'ongw', 'ordsequ', 'ence']) == True
    assert candidate(word1 = ['a', 'very', 'long', 'string', 'here'],word2 = ['averylongstringhere']) == True
    assert candidate(word1 = ['same', 'string'],word2 = ['sam', 'e', 'string']) == True
    assert candidate(word1 = ['abc', 'defg', 'hijkl'],word2 = ['abcdefg', 'hijkl']) == True
    assert candidate(word1 = ['abc', 'def', 'ghi'],word2 = ['abcdef', 'ghi']) == True
    assert candidate(word1 = ['abc', 'def', 'ghi'],word2 = ['abcdefg', 'hi']) == True
    assert candidate(word1 = ['long', 'string', 'here'],word2 = ['longstring', 'here']) == True
    assert candidate(word1 = ['x', 'y', 'z'],word2 = ['xyz']) == True
    assert candidate(word1 = ['z'],word2 = ['z']) == True
    assert candidate(word1 = ['one', 'two', 'three', 'four'],word2 = ['onetwo', 'three', 'four']) == True
    assert candidate(word1 = ['one', 'two', 'three', 'four'],word2 = ['onetwo', 'threefour']) == True
    assert candidate(word1 = ['x', 'y', 'z'],word2 = ['x', 'yz']) == True
    assert candidate(word1 = ['xyz', 'uvw'],word2 = ['xy', 'zu', 'vw']) == True
    assert candidate(word1 = ['a', 'b', 'c', 'd', 'e'],word2 = ['abcd', 'e']) == True
    assert candidate(word1 = ['longerstring', 'here'],word2 = ['longerstringhere']) == True
    assert candidate(word1 = ['onetwothree'],word2 = ['one', 'two', 'three']) == True
    assert candidate(word1 = ['abc', 'def', 'ghi'],word2 = ['ab', 'cdef', 'ghi']) == True
    assert candidate(word1 = ['abcd'],word2 = ['ab', 'c', 'd']) == True
    assert candidate(word1 = ['one', 'two', 'three', 'four'],word2 = ['onetwothreefour']) == True
    assert candidate(word1 = ['almost', 'thesame'],word2 = ['almostthesame', 'extra']) == False
    assert candidate(word1 = ['split', 'into', 'multiple', 'parts'],word2 = ['splitint', 'omulti', 'pleparts']) == True
    assert candidate(word1 = ['ab', 'cde', 'f'],word2 = ['abc', 'def']) == True
    assert candidate(word1 = ['same', 'string', 'here'],word2 = ['samestringhere']) == True
    assert candidate(word1 = ['xyz', 'uvw', 'mnop'],word2 = ['xyzu', 'vw', 'mnop']) == True
    assert candidate(word1 = ['xyz', 'uvw', 'qrst'],word2 = ['xyzuvw', 'qrst']) == True
    assert candidate(word1 = ['same', 'string', 'here'],word2 = ['sam', 'e', 'stringhere']) == True
    assert candidate(word1 = ['longstringhere', 'another'],word2 = ['longstringhereanother']) == True
    assert candidate(word1 = ['this', 'is', 'a', 'test'],word2 = ['thi', 'sisa', 'test']) == True
    assert candidate(word1 = ['abc', 'defg', 'hijk', 'lmnop'],word2 = ['abcdefg', 'hijklmnop']) == True
    assert candidate(word1 = ['longstringhere', 'anotherlongstringhere'],word2 = ['longstringhereanotherlongstringhere']) == True
    assert candidate(word1 = ['a', 'b', 'c', 'd', 'e'],word2 = ['abcde']) == True
    assert candidate(word1 = ['part1', 'part2', 'part3'],word2 = ['part', '1part2', 'part3']) == True
    assert candidate(word1 = ['a', 'longer', 'string', 'here'],word2 = ['a', 'longerstring', 'here']) == True
    assert candidate(word1 = ['part1', 'part2'],word2 = ['part1part2']) == True
    assert candidate(word1 = ['a', 'b', 'c'],word2 = ['abc']) == True
    assert candidate(word1 = ['different', 'length'],word2 = ['differentlen', 'gth']) == True
    assert candidate(word1 = ['longstringone', 'longstringtwo'],word2 = ['longstringone', 'long', 'string', 'two']) == True
    assert candidate(word1 = ['same', 'string', 'here'],word2 = ['samestring', 'here']) == True
    assert candidate(word1 = ['short'],word2 = ['loooooooonger']) == False
    assert candidate(word1 = ['hello', 'world'],word2 = ['he', 'll', 'o', 'wor', 'ld']) == True
    assert candidate(word1 = ['hello', 'world', 'python'],word2 = ['hello', 'wor', 'ldpy', 'thon']) == True
    assert candidate(word1 = ['another', 'example', 'with', 'spaces'],word2 = ['anotherexam', 'plewithspaces']) == True
    assert candidate(word1 = ['xyz', 'uvw', 'rst'],word2 = ['xyzuvw', 'rst']) == True
    assert candidate(word1 = ['abc', 'def'],word2 = ['a', 'bc', 'd', 'ef']) == True
    assert candidate(word1 = ['this', 'is', 'a', 'test'],word2 = ['thisisatest']) == True
    assert candidate(word1 = ['samestringhere'],word2 = ['same', 'string', 'here']) == True
    assert candidate(word1 = ['abcd'],word2 = ['a', 'b', 'c', 'd']) == True
    assert candidate(word1 = ['abc', 'def', 'ghi'],word2 = ['abcdefghi']) == True
    assert candidate(word1 = ['a', 'a', 'a', 'a', 'a'],word2 = ['a', 'a', 'a', 'a', 'a']) == True
    assert candidate(word1 = ['a', 'a', 'a', 'a', 'a'],word2 = ['aaaaa']) == True
    assert candidate(word1 = ['mismatch', 'here'],word2 = ['mismatch', 'there']) == False
    assert candidate(word1 = ['one', 'two', 'three'],word2 = ['on', 'etwothree']) == True
    assert candidate(word1 = ['part', 'one'],word2 = ['p', 'artone']) == True
    assert candidate(word1 = ['equal', 'length', 'words'],word2 = ['equal', 'length', 'word']) == False
    assert candidate(word1 = ['abc', 'def', 'ghi'],word2 = ['abc', 'def', 'ghi']) == True
    assert candidate(word1 = ['equal', 'length'],word2 = ['equal', 'length']) == True
    assert candidate(word1 = ['longwordhere'],word2 = ['l', 'on', 'g', 'wo', 'rd', 'here']) == True
    assert candidate(word1 = ['longer', 'string', 'example'],word2 = ['longerstringexample']) == True
    assert candidate(word1 = ['singleword'],word2 = ['single', 'word']) == True
    assert candidate(word1 = ['different', 'sizes'],word2 = ['different', 'siz', 'es']) == True
    assert candidate(word1 = ['a'],word2 = ['b']) == False
    assert candidate(word1 = ['one', 'two', 'three'],word2 = ['one', 'twothree']) == True
    assert candidate(word1 = ['split', 'this', 'way'],word2 = ['sp', 'lit', 'thi', 'sway']) == True
    assert candidate(word1 = ['one', 'two', 'three'],word2 = ['onetwo', 'three']) == True
    assert candidate(word1 = ['this', 'is', 'a', 'test'],word2 = ['thisis', 'atest']) == True
    assert candidate(word1 = ['a', 'b', 'c', 'd'],word2 = ['abcd']) == True
    assert candidate(word1 = ['split', 'across', 'multiple', 'parts'],word2 = ['splitacrossmultip', 'leparts']) == True
