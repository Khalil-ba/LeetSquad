# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(text = "jumped over the lazy dog",brokenLetters = "zg") == 3
    assert candidate(text = "nopqrstuvwxyz",brokenLetters = "xyz") == 0
    assert candidate(text = "xyzzzz",brokenLetters = "x") == 0
    assert candidate(text = "leet code",brokenLetters = "lt") == 1
    assert candidate(text = "programming is fun",brokenLetters = "fn") == 1
    assert candidate(text = "this is a test",brokenLetters = "xyz") == 4
    assert candidate(text = "mississippi",brokenLetters = "sip") == 0
    assert candidate(text = "python java cplusplus",brokenLetters = "ypx") == 1
    assert candidate(text = "same same same",brokenLetters = "aem") == 0
    assert candidate(text = "a b c d e",brokenLetters = "") == 5
    assert candidate(text = "aa bb cc dd ee ff gg hh ii jj kk ll mm nn oo pp qq rr ss tt uu vv ww xx yy zz",brokenLetters = "xyz") == 23
    assert candidate(text = "abcdefghijk",brokenLetters = "abcde") == 0
    assert candidate(text = "leet code",brokenLetters = "e") == 0
    assert candidate(text = "single",brokenLetters = "s") == 0
    assert candidate(text = "unique words",brokenLetters = "") == 2
    assert candidate(text = "single",brokenLetters = "") == 1
    assert candidate(text = "abc def ghi",brokenLetters = "xyz") == 3
    assert candidate(text = "python programming",brokenLetters = "p") == 0
    assert candidate(text = "a b c d e f g h i j k l m n o p q r s t u v w x y z",brokenLetters = "") == 26
    assert candidate(text = "a quick brown fox",brokenLetters = "") == 4
    assert candidate(text = "abcd efgh ijkl mnop qrst uvwx yz",brokenLetters = "aeiou") == 2
    assert candidate(text = "python programming",brokenLetters = "th") == 1
    assert candidate(text = "abcdefghij",brokenLetters = "") == 1
    assert candidate(text = "hello hello hello",brokenLetters = "lo") == 0
    assert candidate(text = "hello world",brokenLetters = "ad") == 1
    assert candidate(text = "every good boy does fine",brokenLetters = "f") == 4
    assert candidate(text = "hello world abcdefghijklmnopqrstuvwxyz",brokenLetters = "") == 3
    assert candidate(text = "a b c d e f g",brokenLetters = "xyz") == 7
    assert candidate(text = "extreme example with all letters",brokenLetters = "abcdefghijklmnopqrstuvwxyz") == 0
    assert candidate(text = "this is a simple test",brokenLetters = "sti") == 1
    assert candidate(text = "singleword",brokenLetters = "w") == 0
    assert candidate(text = "abcdefghij klmnopqrstuvwxyz",brokenLetters = "xyz") == 1
    assert candidate(text = "university of california berkeley",brokenLetters = "bcdfg") == 1
    assert candidate(text = "congratulations on your success",brokenLetters = "cns") == 1
    assert candidate(text = "every good boy does fine",brokenLetters = "bd") == 2
    assert candidate(text = "hello world from the other side",brokenLetters = "dfr") == 2
    assert candidate(text = "complexity arises from multiple factors",brokenLetters = "ae") == 1
    assert candidate(text = "all the letters of the alphabet",brokenLetters = "aeiou") == 0
    assert candidate(text = "keyboard malfunctioning example",brokenLetters = "kmb") == 0
    assert candidate(text = "short long longer longestword",brokenLetters = "nlg") == 1
    assert candidate(text = "repeated letters letters letters",brokenLetters = "r") == 0
    assert candidate(text = "quick brown fox jumps over the lazy dog",brokenLetters = "xyz") == 6
    assert candidate(text = "data structures and algorithms",brokenLetters = "dts") == 0
    assert candidate(text = "abcdef ghijklm nopqrst uvwxyz",brokenLetters = "mnop") == 2
    assert candidate(text = "multiple broken letters test",brokenLetters = "mlpt") == 1
    assert candidate(text = "abcdefghij klmnopqrstuvwxyz",brokenLetters = "jkl") == 0
    assert candidate(text = "mississippi river",brokenLetters = "is") == 0
    assert candidate(text = "no broken letters here",brokenLetters = "qwxz") == 4
    assert candidate(text = "programming is fun",brokenLetters = "funs") == 0
    assert candidate(text = "all unique characters",brokenLetters = "") == 3
    assert candidate(text = "quick brown fox jumps over the lazy dog",brokenLetters = "") == 8
    assert candidate(text = "hello world hello universe",brokenLetters = "d") == 3
    assert candidate(text = "supercalifragilisticexpialidocious",brokenLetters = "aeiou") == 0
    assert candidate(text = "special symbols are not included !@#$%^&*()",brokenLetters = "") == 6
    assert candidate(text = "brokenkeyboard faultydevice",brokenLetters = "bdf") == 0
    assert candidate(text = "sequential typing test",brokenLetters = "qseq") == 1
    assert candidate(text = "unique letters in words",brokenLetters = "aeiouy") == 0
    assert candidate(text = "python code implementation",brokenLetters = "py") == 1
    assert candidate(text = "a b c d e f g h i j k l m n o p q r s t u v w x y z",brokenLetters = "qz") == 24
    assert candidate(text = "a b c d e f g h i j k l m n o p q r s t u v w x y z",brokenLetters = "abcdefghijkl") == 14
    assert candidate(text = "complex words like supercalifragilisticexpialidocious",brokenLetters = "xyz") == 2
    assert candidate(text = "this is a simple test case",brokenLetters = "aeiou") == 0
    assert candidate(text = "one two three four five six seven eight nine ten",brokenLetters = "on") == 4
    assert candidate(text = "lets write some code",brokenLetters = "wrs") == 1
    assert candidate(text = "multiple broken letters scenario",brokenLetters = "aeiouy") == 0
    assert candidate(text = "complex problem solving required",brokenLetters = "abc") == 2
    assert candidate(text = "this is a simple test",brokenLetters = "s") == 1
    assert candidate(text = "all characters must be checked",brokenLetters = "aeiou") == 0
    assert candidate(text = "quick brown fox jumps over lazy dog",brokenLetters = "qz") == 5
    assert candidate(text = "various broken keys test",brokenLetters = "var") == 2
    assert candidate(text = "quick brown fox jumps over the lazy dog",brokenLetters = "qz") == 6
    assert candidate(text = "a quick brown fox jumps over the lazy dog",brokenLetters = "aeiou") == 0
    assert candidate(text = "beautiful scenery on the mountain top",brokenLetters = "mnt") == 0
    assert candidate(text = "vowels are often omitted",brokenLetters = "aeiou") == 0
    assert candidate(text = "mississippi river flows smoothly",brokenLetters = "m") == 2
    assert candidate(text = "hello world from another dimension",brokenLetters = "ad") == 2
    assert candidate(text = "singlewordwithoutspaces",brokenLetters = "s") == 0
    assert candidate(text = "abcdefghijklmnopqrstuvwxyz",brokenLetters = "xyz") == 0
    assert candidate(text = "fuzzy wuzzy was a bear",brokenLetters = "f") == 4
    assert candidate(text = "algorithms and data structures",brokenLetters = "da") == 1
    assert candidate(text = "make america great again",brokenLetters = "mag") == 0
    assert candidate(text = "hello hello hello world",brokenLetters = "d") == 3
    assert candidate(text = "a aa aaa aaaa aaaaa",brokenLetters = "a") == 0
    assert candidate(text = "mississippi river",brokenLetters = "m") == 1
    assert candidate(text = "many many words with many repeated letters",brokenLetters = "mny") == 4
    assert candidate(text = "abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz",brokenLetters = "") == 2
    assert candidate(text = "special characters are not considered",brokenLetters = "!@#$%^&*()") == 5
    assert candidate(text = "alibaba cloud is amazing",brokenLetters = "aim") == 1
    assert candidate(text = "boundary conditions and edge cases",brokenLetters = "bace") == 0
    assert candidate(text = "the quick brown fox jumps over the lazy dog",brokenLetters = "") == 9
    assert candidate(text = "algorithm data structures",brokenLetters = "abcde") == 0
    assert candidate(text = "xylophone xylophone xylophone",brokenLetters = "xy") == 0
    assert candidate(text = "complex problem solving",brokenLetters = "cps") == 0
    assert candidate(text = "longer words with various letters",brokenLetters = "wv") == 2
    assert candidate(text = "every good boy does fine",brokenLetters = "boyd") == 1
    assert candidate(text = "the quick brown fox jumps over the lazy dog",brokenLetters = "qxyz") == 6
    assert candidate(text = "programming in python is fun",brokenLetters = "pqf") == 2
    assert candidate(text = "this is a test case with many words",brokenLetters = "aeiou") == 0
    assert candidate(text = "repeated letters in words",brokenLetters = "r") == 1
    assert candidate(text = "mississippi river",brokenLetters = "r") == 1
    assert candidate(text = "edge cases require attention",brokenLetters = "ecr") == 0
    assert candidate(text = "short words",brokenLetters = "aef") == 2
    assert candidate(text = "all characters are broken here",brokenLetters = "abcdefghijklmnopqrstuvwxyz") == 0
    assert candidate(text = "this is a simple test",brokenLetters = "st") == 1
    assert candidate(text = "multiple words with repeated letters",brokenLetters = "w") == 3
    assert candidate(text = "python is a versatile programming language",brokenLetters = "p") == 4
    assert candidate(text = "this is a simple test case",brokenLetters = "") == 6
    assert candidate(text = "short words",brokenLetters = "ow") == 0
    assert candidate(text = "distinct distinct letters letters",brokenLetters = "distnl") == 0
    assert candidate(text = "the quick brown fox jumps over the lazy dog",brokenLetters = "aeiou") == 0
    assert candidate(text = "let us escape from this困境",brokenLetters = "et") == 2
    assert candidate(text = "broken keyboards are annoying sometimes",brokenLetters = "bks") == 2
    assert candidate(text = "various combinations",brokenLetters = "vbc") == 0
    assert candidate(text = "every good boy does fine and gets chocolate",brokenLetters = "xyz") == 6
    assert candidate(text = "hello world from mars",brokenLetters = "mr") == 1
    assert candidate(text = "various punctuations are missing",brokenLetters = "aeiou") == 0
    assert candidate(text = "quick brown fox jumps over the lazy dog",brokenLetters = "aeiou") == 0
    assert candidate(text = "unique words in this sentence",brokenLetters = "uie") == 1
    assert candidate(text = "multiple words with repeated letters",brokenLetters = "r") == 2
    assert candidate(text = "one two three four five",brokenLetters = "one") == 0
    assert candidate(text = "computer science",brokenLetters = "xyz") == 2
    assert candidate(text = "this is a simple test case",brokenLetters = "s") == 1
    assert candidate(text = "multiple spaces between words   are not allowed",brokenLetters = "") == 7
    assert candidate(text = "special characters !@#$%^&*()",brokenLetters = "s") == 1
    assert candidate(text = "banana apple orange",brokenLetters = "aeiou") == 0
    assert candidate(text = "abcdefghijklmnopqrstuvwxyz",brokenLetters = "nopqrstuvwxyz") == 0
    assert candidate(text = "abcdef ghijklm nopqrstuvwxyz",brokenLetters = "aeiou") == 0
    assert candidate(text = "spaceship traveling fast",brokenLetters = "spfc") == 1
    assert candidate(text = "unique characters only",brokenLetters = "uqnc") == 0
    assert candidate(text = "every good boy does fine",brokenLetters = "egbf") == 0
    assert candidate(text = "repeated repeated words words",brokenLetters = "dpw") == 0
    assert candidate(text = "abcdefghijklmnopqrstuvwxy z",brokenLetters = "z") == 1
    assert candidate(text = "complex problems require careful thought",brokenLetters = "th") == 4
    assert candidate(text = "all words can be typed",brokenLetters = "") == 5
    assert candidate(text = "abcdefg hijklm nopqrstuvwxyz",brokenLetters = "xyz") == 2
