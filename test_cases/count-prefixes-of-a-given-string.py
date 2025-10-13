# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(words = ['hello', 'hell', 'he', 'h'],s = "hello") == 4
    assert candidate(words = ['short'],s = "shorter") == 1
    assert candidate(words = ['same', 'same'],s = "same") == 2
    assert candidate(words = ['hello'],s = "h") == 0
    assert candidate(words = ['hello'],s = "hello") == 1
    assert candidate(words = ['d', 'do', 'dog', 'doge'],s = "doge") == 4
    assert candidate(words = ['prefix'],s = "prefix") == 1
    assert candidate(words = ['same', 'same', 'same'],s = "same") == 3
    assert candidate(words = ['world'],s = "world") == 1
    assert candidate(words = ['a', 'b', 'c'],s = "abcde") == 1
    assert candidate(words = ['a'],s = "a") == 1
    assert candidate(words = ['not', 'a', 'prefix'],s = "example") == 0
    assert candidate(words = ['test', 'testing', 't'],s = "testing") == 3
    assert candidate(words = ['xyz', 'xy', 'x'],s = "xyz") == 3
    assert candidate(words = ['abcd'],s = "abc") == 0
    assert candidate(words = ['a', 'b', 'c'],s = "d") == 0
    assert candidate(words = ['test', 'testing', 'tested'],s = "testing") == 2
    assert candidate(words = ['a', 'a'],s = "aa") == 2
    assert candidate(words = ['abc'],s = "abc") == 1
    assert candidate(words = ['abc', 'abcd', 'abcde'],s = "abcdef") == 3
    assert candidate(words = ['z', 'zz', 'zzz'],s = "zzzz") == 3
    assert candidate(words = ['cat', 'bat', 'rat'],s = "car") == 0
    assert candidate(words = ['a', 'b', 'c', 'ab', 'bc', 'abc'],s = "abc") == 3
    assert candidate(words = ['h'],s = "hello") == 1
    assert candidate(words = ['a'],s = "b") == 0
    assert candidate(words = ['yes', 'no'],s = "yesman") == 1
    assert candidate(words = ['prefix'],s = "prefixing") == 1
    assert candidate(words = ['hello', 'he', 'h'],s = "hello") == 3
    assert candidate(words = ['test'],s = "testing") == 1
    assert candidate(words = ['a', 'ab', 'abc', 'abcd'],s = "abcd") == 4
    assert candidate(words = ['subsequence', 'subsequen', 'subsequen', 'subsequ', 'subsequ', 'subseq'],s = "subsequence") == 6
    assert candidate(words = ['ab', 'abc', 'abcd'],s = "abcd") == 3
    assert candidate(words = ['test', 'testing', 'tested', 'te'],s = "testing") == 3
    assert candidate(words = ['unique', 'uniq', 'un'],s = "unique") == 3
    assert candidate(words = ['different', 'dif', 'diff', 'differ'],s = "different") == 4
    assert candidate(words = ['partial', 'parti', 'part', 'par'],s = "partialmatch") == 4
    assert candidate(words = ['prefix', 'pre', 'pred'],s = "predicate") == 2
    assert candidate(words = ['example', 'examp', 'exam', 'exa', 'ex', 'e'],s = "example") == 6
    assert candidate(words = ['prefix', 'prefi', 'pref', 'pre'],s = "prefix") == 4
    assert candidate(words = ['abc', 'abcd', 'ab', 'a'],s = "abcd") == 4
    assert candidate(words = ['complex', 'com', 'comp', 'comple', 'complexe'],s = "complex") == 4
    assert candidate(words = ['prefix', 'prefi', 'prefixe', 'prefixex'],s = "prefixextension") == 4
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa'],s = "aaaaa") == 4
    assert candidate(words = ['example', 'ex', 'exa', 'exam', 'examp', 'examp'],s = "example") == 6
    assert candidate(words = ['complex', 'comple', 'compl', 'comp'],s = "complexity") == 4
    assert candidate(words = ['hello', 'hell', 'he'],s = "hello") == 3
    assert candidate(words = ['abcde', 'bcde', 'cde', 'de', 'e'],s = "abcde") == 1
    assert candidate(words = ['abc', 'def', 'ghi'],s = "abcdefghi") == 1
    assert candidate(words = ['not', 'no', 'n'],s = "note") == 3
    assert candidate(words = ['multiple', 'multip', 'multi', 'mult', 'mult'],s = "multiple") == 5
    assert candidate(words = ['word', 'words', 'wording'],s = "word") == 1
    assert candidate(words = ['prefix', 'pre', 'p'],s = "prefix") == 3
    assert candidate(words = ['overlap', 'over', 'ov', 'o'],s = "overlap") == 4
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],s = "aaaaaaaa") == 5
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],s = "aaaaa") == 5
    assert candidate(words = ['short', 'shorter', 'shortest'],s = "short") == 1
    assert candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg'],s = "abcdefgh") == 7
    assert candidate(words = ['short', 'shot', 'sh', 's'],s = "shortstory") == 3
    assert candidate(words = ['abcd', 'abc', 'ab', 'a'],s = "a") == 1
    assert candidate(words = ['longword', 'long', 'lo', 'l', 'lon', 'longw'],s = "longword") == 6
    assert candidate(words = ['a', 'b', 'c', 'd', 'e'],s = "abcde") == 1
    assert candidate(words = ['prefix', 'pre', 'p'],s = "prefix") == 3
    assert candidate(words = ['prefix', 'pre', 'pref', 'prefi', 'prefixe'],s = "prefix") == 4
    assert candidate(words = ['aaa', 'aa', 'a'],s = "aaaaa") == 3
    assert candidate(words = ['word', 'wording', 'worded', 'wordingword'],s = "wordingword") == 3
    assert candidate(words = ['test', 'testing', 'testi', 'testin'],s = "testingstring") == 4
    assert candidate(words = ['one', 'two', 'three', 'four'],s = "one") == 1
    assert candidate(words = ['different', 'diff', 'diffe', 'differen', 'differen'],s = "different") == 5
    assert candidate(words = ['unique', 'uniq', 'un', 'u'],s = "unique") == 4
    assert candidate(words = ['aaa', 'aa', 'a', 'aaaa'],s = "aaa") == 3
    assert candidate(words = ['abcd', 'bcde', 'cdef', 'defg'],s = "abcd") == 1
    assert candidate(words = ['not', 'no', 'n'],s = "note") == 3
    assert candidate(words = ['same', 'same', 'same', 'same'],s = "same") == 4
    assert candidate(words = ['test', 'testing', 'tea', 'te'],s = "testing") == 3
    assert candidate(words = ['longword', 'long', 'lo', 'l'],s = "longwordexample") == 4
    assert candidate(words = ['begin', 'beg', 'be', 'b'],s = "beginning") == 4
    assert candidate(words = ['overlap', 'over', 'o'],s = "overlap") == 3
    assert candidate(words = ['test', 'testing', 'tes', 't'],s = "testing") == 4
    assert candidate(words = ['xy', 'xyz', 'xyzz'],s = "xy") == 1
    assert candidate(words = ['one', 'two', 'three', 'four', 'five'],s = "fives") == 1
    assert candidate(words = ['longword', 'long', 'lo', 'l'],s = "longword") == 4
    assert candidate(words = ['example', 'ex', 'exa', 'exam', 'examp'],s = "example") == 5
    assert candidate(words = ['one', 'two', 'three'],s = "onetwothree") == 1
    assert candidate(words = ['abc', 'abcd', 'abcde'],s = "abcdef") == 3
    assert candidate(words = ['multiple', 'multi', 'mul', 'mu'],s = "multiples") == 4
    assert candidate(words = ['word', 'wor', 'wo', 'w'],s = "word") == 4
    assert candidate(words = ['banana', 'ban', 'ba', 'b'],s = "bananarama") == 4
    assert candidate(words = ['abcd', 'abc', 'ab', 'a'],s = "abcd") == 4
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa'],s = "aaaa") == 4
    assert candidate(words = ['prefix', 'pre', 'prefixx', 'prefixxx', 'prefixxxx'],s = "prefixx") == 3
    assert candidate(words = ['quick', 'qui', 'quic', 'quicks', 'quickb'],s = "quickbrownfox") == 4
    assert candidate(words = ['test', 'testing', 'tested'],s = "testing") == 2
    assert candidate(words = ['one', 'onetwo', 'onetwothree'],s = "onetwothree") == 3
    assert candidate(words = ['programming', 'prog', 'pro'],s = "programming") == 3
    assert candidate(words = ['part', 'partial', 'partially'],s = "partially") == 3
    assert candidate(words = ['aaa', 'aa', 'a', 'aaaa'],s = "aaaa") == 4
    assert candidate(words = ['one', 'two', 'three', 'four'],s = "one") == 1
    assert candidate(words = ['prefix', 'pre', 'prex', 'abc'],s = "prefix") == 2
    assert candidate(words = ['abc', 'abcd', 'abcde'],s = "abcdefg") == 3
    assert candidate(words = ['repeat', 'repe', 'rep', 're', 'r'],s = "repeat") == 5
    assert candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde'],s = "a") == 1
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],s = "aaaaaa") == 5
    assert candidate(words = ['complex', 'comp', 'com', 'co', 'c'],s = "complexity") == 5
    assert candidate(words = ['python', 'pyth', 'py'],s = "python") == 3
    assert candidate(words = ['xyz', 'xy', 'x'],s = "xy") == 2
    assert candidate(words = ['xyz', 'xy', 'x', ''],s = "xyz") == 4
    assert candidate(words = ['complex', 'com', 'co', 'c'],s = "complex") == 4
    assert candidate(words = ['prefix', 'prefixx', 'prefixxx', 'prefixxxx'],s = "prefix") == 1
    assert candidate(words = ['abc', 'abcd', 'abcde'],s = "abcdefg") == 3
    assert candidate(words = ['abc', 'def', 'ghi', 'abc'],s = "abcdefghi") == 2
    assert candidate(words = ['cat', 'cattle', 'cattleman'],s = "cattleman") == 3
    assert candidate(words = ['xyz', 'xy', 'x'],s = "xyz") == 3
    assert candidate(words = ['same', 'same', 'same'],s = "same") == 3
    assert candidate(words = ['prefix', 'pre', 'pref'],s = "prefix") == 3
    assert candidate(words = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef'],s = "fghijkl") == 0
    assert candidate(words = ['small', 'smaller', 'smallest', 'smallerest'],s = "smallerest") == 3
    assert candidate(words = ['substring', 'subs', 'sub', 'su'],s = "substringexample") == 4
    assert candidate(words = ['abc', 'abcd', 'abcde', 'abcdef'],s = "abcdefg") == 4
    assert candidate(words = ['test', 'testing', 'testi'],s = "test") == 1
    assert candidate(words = ['zz', 'zzz', 'zzzz'],s = "zzzz") == 3
    assert candidate(words = ['hello', 'he', 'hell'],s = "hello") == 3
    assert candidate(words = ['prefix', 'pre', 'pref', 'prex'],s = "prefix") == 3
    assert candidate(words = ['z', 'zz', 'zzz', 'zzzz'],s = "zzzzzz") == 4
    assert candidate(words = ['unique', 'uniq', 'uni', 'un', 'u'],s = "unique") == 5
    assert candidate(words = ['cat', 'dog', 'car', 'catch', 'cart'],s = "catch") == 2
    assert candidate(words = ['consistent', 'consist', 'consi', 'cons'],s = "consistency") == 3
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],s = "abcdefghij") == 1
    assert candidate(words = ['unique', 'uniq', 'uni', 'un'],s = "uniques") == 4
    assert candidate(words = ['hello', 'world', 'hel', 'wo', 'wor'],s = "helloworld") == 2
    assert candidate(words = ['overlap', 'over', 'ov', 'overlaplap'],s = "overlap") == 3
    assert candidate(words = ['matching', 'match', 'mat', 'ma', 'm'],s = "matching") == 5
    assert candidate(words = ['hello', 'hell', 'he', 'h', 'hellohello'],s = "hellohello") == 5
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa'],s = "aaaaaaaaa") == 4
    assert candidate(words = ['test', 'testing', 'testing123'],s = "test") == 1
    assert candidate(words = ['match', 'mat', 'ma', 'm'],s = "match") == 4
    assert candidate(words = ['example', 'exa', 'ex', 'e'],s = "example") == 4
    assert candidate(words = ['hello', 'hell', 'he', 'h'],s = "hello") == 4
    assert candidate(words = ['word', 'wording', 'wordings'],s = "word") == 1
    assert candidate(words = ['prefix', 'pre', 'p', 'programming'],s = "prefix") == 3
    assert candidate(words = ['a', 'ab', 'abc', 'abcd'],s = "abcde") == 4
    assert candidate(words = ['unique', 'uniqueness', 'uni', 'un'],s = "uniqueness") == 4
    assert candidate(words = ['one', 'on', 'o', 'ones'],s = "one") == 3
    assert candidate(words = ['word', 'wo', 'w'],s = "word") == 3
    assert candidate(words = ['prefix', 'pre', 'pr', 'p'],s = "prefix") == 4
    assert candidate(words = ['example', 'exam', 'ex', 'e'],s = "examples") == 4
    assert candidate(words = ['common', 'commo', 'comm', 'com', 'co', 'c'],s = "common") == 6
