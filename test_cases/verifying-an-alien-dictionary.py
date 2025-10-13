# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(words = ['a', 'b', 'c', 'd', 'e'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['kuvp', 'q'],order = "ngxlkthsjuoqcpavbfdermiyzw") == True
    assert candidate(words = ['zzz', 'zzzz'],order = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(words = ['abc', 'ab'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['hello', 'hello', 'hello'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['apple', 'app'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['app', 'apple'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['aaa'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['hello', 'leetcode'],order = "hlabcdefgijkmnopqrstuvwxyz") == True
    assert candidate(words = ['zoo', 'zoop'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['a', 'b', 'c'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['abc', 'acb'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['kz', 'kzc'],order = "zabklmncopqrstuvwxy") == True
    assert candidate(words = ['a', 'b', 'c'],order = "cba") == False
    assert candidate(words = ['kuvp', 'q'],order = "ngxlkthsjuoqcpavbfderimyzw") == True
    assert candidate(words = ['zzz', 'zaz'],order = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(words = ['z', 'z'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['aaa', 'aa'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['word', 'world', 'row'],order = "worldabcefghijkmnpqstuvxyz") == False
    assert candidate(words = ['abc', 'acb', 'bac'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['wrt', 'wrf', 'er', 'ett', 'rftt'],order = "wertfabcghijklmnopqsudvyxz") == False
    assert candidate(words = ['banana', 'apple', 'orange'],order = "zyxcbaedfghijklmnopqrstuvw") == True
    assert candidate(words = ['abcd', 'abcde', 'abcd'],order = "fedcbazyxwvutsrqponmlkjhig") == False
    assert candidate(words = ['aaa', 'aab', 'aac'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['cat', 'dog', 'bird'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['same', 'sake', 'saki'],order = "askdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['aaa', 'aaab', 'aaac'],order = "abcdefghijkmnopqrstuvwxyzl") == True
    assert candidate(words = ['banana', 'bandana', 'bandwidth'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['xyz', 'xyzz', 'xyza'],order = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(words = ['a', 'b', 'c', 'd', 'e'],order = "edcba") == False
    assert candidate(words = ['short', 'shorter', 'shortest'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['banana', 'bandana', 'bandit'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['a', 'b', 'c', 'd'],order = "cbaedfghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['xyz', 'xyy', 'xyx'],order = "xyzabcdefghijklmnopqrstuvw") == False
    assert candidate(words = ['a', 'b', 'c', 'd', 'e'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['mismatch', 'mis', 'misleading'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['dog', 'cat'],order = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(words = ['zebra', 'dog', 'cat'],order = "dogcatzebraabcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['abc', 'abz', 'abcde'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['long', 'longer', 'longest'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['app', 'apple', 'apples'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['word', 'world', 'wor'],order = "worldabcefghijkmnpqstuvxyz") == False
    assert candidate(words = ['apple', 'apples', 'app', 'appl'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['dog', 'cat', 'bird'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['alien', 'algorithm', 'all'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['aa', 'a'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['zebra', 'zebraa'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['banana', 'bandana', 'apple'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['zebra', 'zoo', 'zoom', 'zoology'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['same', 'same', 'same'],order = "fedcbazyxwvutsrqponmlkjhig") == True
    assert candidate(words = ['abcd', 'abce', 'abcf'],order = "acegbdfhijklmnopqrstuvwxyz") == False
    assert candidate(words = ['one', 'only', 'on', 'once'],order = "onabcdefghijkmplqstuvxyzwer") == False
    assert candidate(words = ['aaa', 'aa', 'aaaa', 'aaaaa'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['abc', 'acb', 'bac'],order = "cbafehidgjklmponqrstuvwxzy") == False
    assert candidate(words = ['zzz', 'zz', 'z', ''],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['aaa', 'aab', 'aac'],order = "cbafehidgjklmponqrstuvwxzy") == False
    assert candidate(words = ['xylophone', 'xylometer', 'xylography'],order = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(words = ['abcd', 'abcde', 'abcdeg', 'abcdef', 'abcdefg'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['same', 'same', 'same'],order = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(words = ['zebra', 'dog', 'duck', 'dove'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['zz', 'zzz', 'zzzz', 'zzzzz'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['word', 'wor', 'worl', 'world'],order = "worldabcefghijkmnpqstuvxyz") == False
    assert candidate(words = ['abcd', 'abce', 'abcf'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['short', 'shorter', 'shortest'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['cat', 'bat', 'rat'],order = "abcdefghirjklmnopqrstuvwxyzct") == False
    assert candidate(words = ['zebra', 'zealot', 'zest'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['a', 'b', 'c'],order = "cbaz") == False
    assert candidate(words = ['zebra', 'zebr', 'zebraa'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['apple', 'apples', 'app'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['xww', 'xwx', 'xw'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['xyz', 'xy', 'x'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['word', 'world', 'wor', 'worl'],order = "worldabcefghijkmnpqstuvxyz") == False
    assert candidate(words = ['zyx', 'zy', 'zxy'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['xyz', 'xya', 'xyb'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['word', 'world', 'worlds', 'worldwide'],order = "worldabcdefghijklnmpqstuvxyz") == False
    assert candidate(words = ['word', 'world', 'wordly'],order = "worldabcefghijkmnpqstuvxyz") == False
    assert candidate(words = ['long', 'longer', 'longest'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['aa', 'a'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['longest', 'longer', 'long'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['a', 'b', 'a'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['a', 'b', 'c', 'd', 'e'],order = "edcba") == False
    assert candidate(words = ['same', 'same', 'same'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['special', 'spectacular', 'spectacularly'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['special', 'spectacular', 'spectacularly'],order = "abcdefghijklmnopqrstuvwxyze") == False
    assert candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'],order = "abcdefghijkmnopqrstuvwxyzl") == False
    assert candidate(words = ['zz', 'z', 'zzz'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'],order = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(words = ['banana', 'bandana', 'band', 'bad'],order = "badnecghijklmopqrstuvwxyzf") == False
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['one', 'onetwo', 'onefour'],order = "onetwofourmnbvcxzlkjhgfdsapq") == True
    assert candidate(words = ['zyx', 'zy', 'z', ''],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['this', 'thisis', 'thisisatest'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['abc', 'ab', 'abcd'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['jjg', 'jja', 'jj', 'jjb'],order = "jgfedcbaopqrstuvwxyznhimkl") == False
    assert candidate(words = ['banana', 'bandana', 'band'],order = "banxyzklmnopqrstuvwedcfghij") == False
    assert candidate(words = ['racecar', 'racecars', 'racecarx'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['abcd', 'abce', 'abcf'],order = "mnopqrstuvwxyzabcdefghijkl") == True
    assert candidate(words = ['apple', 'app', 'application'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['zz', 'zzz', 'zzzz', 'zzzzz'],order = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(words = ['aaa', 'aa', 'a'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['apple', 'apples', 'banana'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['apple', 'app', 'application'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['abcd', 'dcba', 'abcd'],order = "abcdexyz") == False
    assert candidate(words = ['abc', 'ab', 'a'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['abc', 'abcd', 'ab'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['abcd', 'abc'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['aaa', 'aa', 'a'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['abc', 'abb', 'aaa'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['abcd', 'abc', 'ab', 'a'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['mismatch', 'mis', 'misleading'],order = "abcdefghijklmnopqrstuvwxyze") == False
    assert candidate(words = ['aaa', 'aab', 'aac', 'aad'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['prefix', 'pre', 'prelude'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['apple', 'apples', 'app'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['apple', 'app', 'application'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['word', 'world', 'wordplay'],order = "worldabcefghijkmnpqstuvxyz") == False
    assert candidate(words = ['zz', 'za', 'zb'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['z', 'za', 'zb', 'zab'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['dog', 'cat', 'bird'],order = "dogcatbirdwxyzefghijklmnpqrstuvwxyz") == False
    assert candidate(words = ['ab', 'abc', 'abcd', 'abcde'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['apple', 'apples', 'app'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['zzzz', 'zzz', 'zzzzz'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['longer', 'long', 'lon'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['hello', 'hallo', 'halloween'],order = "hlabcdefgijkmnopqrstuvwxyz") == False
    assert candidate(words = ['hello', 'helloo', 'hell', 'hellp'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['interstellar', 'inter', 'intergalactic'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['banana', 'apple', 'orange'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['word', 'world', 'wordld'],order = "worldabcefghijkmnpqstuvxyz") == False
    assert candidate(words = ['abc', 'ab', 'abcd'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['aaaa', 'bbbb', 'cccc', 'ddd'],order = "abcdefgihjklmnopqrstuvwxyz") == True
    assert candidate(words = ['a', 'b', 'a'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['cba', 'cbcd'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['same', 'sam', 'samesame'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['ab', 'abc', 'abcd', 'abcde'],order = "edcba") == True
    assert candidate(words = ['apple', 'apples', 'application'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['xx', 'xy', 'xz', 'ya', 'yb', 'yc'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['word', 'world', 'row', 'wordz'],order = "worldabcefghijkmnpqstuvxyz") == False
    assert candidate(words = ['hello', 'hell', 'he', 'h'],order = "hlabcdefgijkmnopqrstuvwxyz") == False
    assert candidate(words = ['aaa', 'aa', 'a'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['hello', 'hell', 'hel', 'he', 'h'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['same', 'same', 'same'],order = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(words = ['zyx', 'zy', 'z'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'],order = "bacdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['abc', 'abd', 'abcd'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['hello', 'hallo', 'hella'],order = "hlabcdefgijkmnopqrstuvwxyz") == False
    assert candidate(words = ['alien', 'algorithm', 'alliance'],order = "abcdefghijklmonpqrsuvwxyztefgh") == False
    assert candidate(words = ['abc', 'abcd', 'ab'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['same', 'some', 'sand'],order = "samponedcbjklfgtqrhxvziwuy") == False
    assert candidate(words = ['aaaaa', 'aaaab', 'aaaba'],order = "abcdefghijklmnopqrstuvwzyx") == False
    assert candidate(words = ['same', 'samee', 'sameee'],order = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(words = ['abc', 'abb', 'ab'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['xylophone', 'xylo', 'xylophones'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['fgh', 'fg', 'f'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['prefix', 'pre', 'prelude'],order = "abcdefghijklmnopqrstuvwxyze") == False
    assert candidate(words = ['apple', 'apply', 'app'],order = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(words = ['banana', 'bandana', 'bandanaa'],order = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(words = ['aab', 'aac', 'aaa', 'aad'],order = "abcdefghijklmnopqrstuvwxyz") == False
