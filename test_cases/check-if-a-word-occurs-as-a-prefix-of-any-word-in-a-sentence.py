# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(sentence = "a ab abc abd",searchWord = "a") == 1
    assert candidate(sentence = "abcde fghij klmno",searchWord = "mnop") == -1
    assert candidate(sentence = "find prefix quickly",searchWord = "qui") == 3
    assert candidate(sentence = "prefix test",searchWord = "prefix") == 1
    assert candidate(sentence = "prefix test",searchWord = "testprefix") == -1
    assert candidate(sentence = "hello world",searchWord = "he") == 1
    assert candidate(sentence = "a aa aaa aaaa",searchWord = "aaaa") == 4
    assert candidate(sentence = "coding in python is fun",searchWord = "py") == 3
    assert candidate(sentence = "i love eating burger",searchWord = "burg") == 4
    assert candidate(sentence = "prefix prefixation prefixed pre",searchWord = "pre") == 1
    assert candidate(sentence = "i am tired",searchWord = "you") == -1
    assert candidate(sentence = "example test case",searchWord = "exa") == 1
    assert candidate(sentence = "start end",searchWord = "sta") == 1
    assert candidate(sentence = "no match here",searchWord = "none") == -1
    assert candidate(sentence = "the quick brown fox jumps over the lazy dog",searchWord = "qui") == 2
    assert candidate(sentence = "coding in python",searchWord = "py") == 3
    assert candidate(sentence = "prefix test",searchWord = "fix") == -1
    assert candidate(sentence = "prefix test",searchWord = "test") == 2
    assert candidate(sentence = "abc def ghi",searchWord = "def") == 2
    assert candidate(sentence = "no matches here",searchWord = "match") == 2
    assert candidate(sentence = "all words unique",searchWord = "word") == 2
    assert candidate(sentence = "a aa aaa aaaa",searchWord = "aaa") == 3
    assert candidate(sentence = "a aa aaa aaaa",searchWord = "a") == 1
    assert candidate(sentence = "unique words only here",searchWord = "word") == 2
    assert candidate(sentence = "prefix prefix prefix",searchWord = "pre") == 1
    assert candidate(sentence = "one two three",searchWord = "four") == -1
    assert candidate(sentence = "prefix test",searchWord = "tes") == 2
    assert candidate(sentence = "a aa aaa aaaa",searchWord = "aa") == 2
    assert candidate(sentence = "make america great again",searchWord = "am") == 2
    assert candidate(sentence = "prefix is the start",searchWord = "start") == 4
    assert candidate(sentence = "a b c d e f g",searchWord = "g") == 7
    assert candidate(sentence = "find the prefix",searchWord = "pre") == 3
    assert candidate(sentence = "this problem is an easy problem",searchWord = "pro") == 2
    assert candidate(sentence = "last word match",searchWord = "match") == 3
    assert candidate(sentence = "prefix test",searchWord = "pre") == 1
    assert candidate(sentence = "a ab abc abcd abcde",searchWord = "abc") == 3
    assert candidate(sentence = "mississippi missouri",searchWord = "miss") == 1
    assert candidate(sentence = "a aa aaa aaaa",searchWord = "aaaaa") == -1
    assert candidate(sentence = "multiple matches match matcher matching",searchWord = "mat") == 2
    assert candidate(sentence = "introduction to the world of algorithms and datastructures",searchWord = "data") == 8
    assert candidate(sentence = "abcdefghijklmnopqrstuvwxyz",searchWord = "abc") == 1
    assert candidate(sentence = "mississippi missouri missing",searchWord = "miss") == 1
    assert candidate(sentence = "prefix is present in the prefix",searchWord = "pre") == 1
    assert candidate(sentence = "unique words only unique",searchWord = "uniq") == 1
    assert candidate(sentence = "look at these examples",searchWord = "these") == 3
    assert candidate(sentence = "unique words only here",searchWord = "only") == 3
    assert candidate(sentence = "prefix suffix prefixsuffix",searchWord = "pre") == 1
    assert candidate(sentence = "testing for edge cases with different words",searchWord = "dif") == 6
    assert candidate(sentence = "python java c++ c#",searchWord = "c") == 3
    assert candidate(sentence = "one two three four five six seven eight nine ten",searchWord = "ten") == 10
    assert candidate(sentence = "aaaaa aaaaa aaaaa aaaaa",searchWord = "aaaa") == 1
    assert candidate(sentence = "algorithm datastructure code compiler bytecode",searchWord = "byte") == 5
    assert candidate(sentence = "finding exact match in the sentence",searchWord = "exac") == 2
    assert candidate(sentence = "hello world from the other side",searchWord = "from") == 3
    assert candidate(sentence = "singleword",searchWord = "single") == 1
    assert candidate(sentence = "this is a very very long sentence to test the code properly",searchWord = "very") == 4
    assert candidate(sentence = "multiple occurrences of the same prefix",searchWord = "same") == 5
    assert candidate(sentence = "prefix testing with prefix prefix prefix",searchWord = "pre") == 1
    assert candidate(sentence = "overlap overlapping overlapped overlap",searchWord = "overl") == 1
    assert candidate(sentence = "find the correct index",searchWord = "cor") == 3
    assert candidate(sentence = "python programming is powerful",searchWord = "pro") == 2
    assert candidate(sentence = "boundary conditions need testing",searchWord = "test") == 4
    assert candidate(sentence = "algorithm and data structures are important",searchWord = "and") == 2
    assert candidate(sentence = "substring matching problem",searchWord = "match") == 2
    assert candidate(sentence = "pneumonoultramicroscopicsilicovolcanoconiosis pneumonoultramicroscopicsilicovolcanoconiosis",searchWord = "pneumono") == 1
    assert candidate(sentence = "hello world hello universe",searchWord = "he") == 1
    assert candidate(sentence = "algorithm datastructure programming language compiler",searchWord = "pro") == 3
    assert candidate(sentence = "uniquewordsinthesentence",searchWord = "words") == -1
    assert candidate(sentence = "prefixprefixprefixprefix",searchWord = "pref") == 1
    assert candidate(sentence = "quick brown fox jumps over the lazy dog",searchWord = "qu") == 1
    assert candidate(sentence = "continuous conversation connection component",searchWord = "con") == 1
    assert candidate(sentence = "small big medium small",searchWord = "sm") == 1
    assert candidate(sentence = "algorithm and data structures",searchWord = "alg") == 1
    assert candidate(sentence = "prefix problem prefixing prefixer",searchWord = "pre") == 1
    assert candidate(sentence = "short longword reallylongword evenlongerword",searchWord = "long") == 2
    assert candidate(sentence = "binary search quicksort mergesort heapsort",searchWord = "sort") == -1
    assert candidate(sentence = "one two three four five six seven eight nine ten",searchWord = "fi") == 5
    assert candidate(sentence = "aaaaa aaaa aa a",searchWord = "a") == 1
    assert candidate(sentence = "prefix search in a list of words",searchWord = "sea") == 2
    assert candidate(sentence = "testing boundary conditions",searchWord = "boundary") == 2
    assert candidate(sentence = "testing edgecases with variouslengthwords",searchWord = "var") == 4
    assert candidate(sentence = "very very long sentence with many words to test the function",searchWord = "very") == 1
    assert candidate(sentence = "repeated repeated repeated",searchWord = "rep") == 1
    assert candidate(sentence = "searching for a longprefixword",searchWord = "longprefix") == 4
    assert candidate(sentence = "an apple a day keeps the doctor away",searchWord = "app") == 2
    assert candidate(sentence = "sun moon stars planets galaxies blackholes nebulas",searchWord = "black") == 6
    assert candidate(sentence = "every good boy does fine great boys deserve fine gifts",searchWord = "fi") == 5
    assert candidate(sentence = "abcdefgh abcdefghij abcdefghijk abcdefghijkl",searchWord = "abcdefg") == 1
    assert candidate(sentence = "another example to check",searchWord = "to") == 3
    assert candidate(sentence = "this is a simple test to check for prefix matching",searchWord = "tes") == 5
    assert candidate(sentence = "searching for exact prefix",searchWord = "sea") == 1
    assert candidate(sentence = "prefix prefix prefix prefix",searchWord = "pref") == 1
    assert candidate(sentence = "this is a simple sentence for testing",searchWord = "simple") == 4
    assert candidate(sentence = "hiddenprefixword is here",searchWord = "hidden") == 1
    assert candidate(sentence = "banana apple banana apple banana",searchWord = "ba") == 1
    assert candidate(sentence = "words with multiple spaces",searchWord = "mul") == 3
    assert candidate(sentence = "algorithm datastructure programming language",searchWord = "pro") == 3
    assert candidate(sentence = "prefixprefixprefixprefixprefix",searchWord = "prefix") == 1
    assert candidate(sentence = "prefix prefix prefix prefix prefix",searchWord = "pre") == 1
    assert candidate(sentence = "complex problem requiring careful thought",searchWord = "com") == 1
    assert candidate(sentence = "random words with no match",searchWord = "nomatch") == -1
    assert candidate(sentence = "python programming py pyth pytho",searchWord = "py") == 1
    assert candidate(sentence = "abcd efgh ijkl mnop qrst uvwx yz",searchWord = "yz") == 7
    assert candidate(sentence = "findingprefixsinthesentence",searchWord = "finding") == 1
    assert candidate(sentence = "prefix matching is important for search engines",searchWord = "search") == 6
    assert candidate(sentence = "abcdefghij abcdefghij abcdefghij",searchWord = "abcdefghijk") == -1
    assert candidate(sentence = "abracadabra abracadabra abracadabra",searchWord = "abra") == 1
    assert candidate(sentence = "nonmatchingprefix prefix",searchWord = "non") == 1
    assert candidate(sentence = "finding the first occurrence firstness",searchWord = "fir") == 3
    assert candidate(sentence = "prefix matching problem prefixing preposition",searchWord = "pre") == 1
    assert candidate(sentence = "none of these should match",searchWord = "non") == 1
    assert candidate(sentence = "prefix prefixing prefixation prefixed",searchWord = "prefix") == 1
    assert candidate(sentence = "multiple occurrences of a word word",searchWord = "word") == 5
    assert candidate(sentence = "all words are different",searchWord = "dif") == 4
    assert candidate(sentence = "prefixes are important in computer science",searchWord = "pre") == 1
    assert candidate(sentence = "mismatch mismatching mismatches",searchWord = "mis") == 1
    assert candidate(sentence = "the quick brown fox jumps over the lazy dog",searchWord = "do") == 9
    assert candidate(sentence = "xy xxy xxxy xxxxy xxxxyy xxxxyyy",searchWord = "xxxxy") == 4
    assert candidate(sentence = "the quick brown fox jumps over the lazy dog",searchWord = "dog") == 9
    assert candidate(sentence = "repeated repeated repeated repeated",searchWord = "repeat") == 1
    assert candidate(sentence = "quick brown fox jumps over lazy dog",searchWord = "quic") == 1
    assert candidate(sentence = "prefixprefixprefix prefixprefix prefix pre prefixing",searchWord = "prefixp") == 1
    assert candidate(sentence = "ab ac ad ae af ag ah ai aj",searchWord = "a") == 1
    assert candidate(sentence = "this is a simple test case",searchWord = "sim") == 4
    assert candidate(sentence = "prefixprefix prefixprefixer prefixprefixing",searchWord = "prefixpre") == 1
    assert candidate(sentence = "unique words with no match",searchWord = "xyz") == -1
    assert candidate(sentence = "abracadabra abracadabra abracadabra",searchWord = "abrac") == 1
    assert candidate(sentence = "continuous integration and continuous delivery",searchWord = "cont") == 1
    assert candidate(sentence = "searching for the prefix within",searchWord = "with") == 5
    assert candidate(sentence = "consecutive words with same start",searchWord = "con") == 1
    assert candidate(sentence = "short long longer longest",searchWord = "long") == 2
    assert candidate(sentence = "consistent consistent consistency consistently",searchWord = "consist") == 1
    assert candidate(sentence = "a short simple sentence",searchWord = "shor") == 2
    assert candidate(sentence = "searching for a unique prefix",searchWord = "uniq") == 4
    assert candidate(sentence = "a quick brown fox jumps over the lazy dog",searchWord = "fox") == 4
    assert candidate(sentence = "programming is fun and educational",searchWord = "edu") == 5
    assert candidate(sentence = "finding the veryfirst occurrence",searchWord = "ver") == 3
    assert candidate(sentence = "the quick brown fox jumps over the lazy dog",searchWord = "qu") == 2
    assert candidate(sentence = "prefix prefixing prefixed",searchWord = "prefix") == 1
    assert candidate(sentence = "boundary conditions are tricky",searchWord = "tri") == 4
    assert candidate(sentence = "complexity of the problem",searchWord = "com") == 1
    assert candidate(sentence = "a aa aaa aaaa aaaaa aaaaaa",searchWord = "aaaa") == 4
    assert candidate(sentence = "searching for a specific word",searchWord = "spec") == 4
    assert candidate(sentence = "multiple occurrences of the same prefix prefix prefix",searchWord = "pre") == 6
    assert candidate(sentence = "ab abc abcd abcde abcdef abcdefg abcdefgh abcdefghi abcdefghij",searchWord = "abcde") == 4
    assert candidate(sentence = "partial match is not allowed",searchWord = "parti") == 1
    assert candidate(sentence = "a b c d e f g h i j k l m n o p q r s t u v w x y z",searchWord = "z") == 26
    assert candidate(sentence = "one two three four five six seven eight nine ten",searchWord = "nine") == 9
    assert candidate(sentence = "prefixes prefixing prefix pre prefixed",searchWord = "pref") == 1
    assert candidate(sentence = "prefix prefixing prefixed pre prefixable",searchWord = "pre") == 1
    assert candidate(sentence = "a a aa aa aaa",searchWord = "aaa") == 5
    assert candidate(sentence = "looking for a specific starting sequence",searchWord = "spe") == 4
    assert candidate(sentence = "alibaba cloud offers many products like ecs ec2 s3",searchWord = "ec") == 7
    assert candidate(sentence = "algorithm data structure and algorithm",searchWord = "algo") == 1
    assert candidate(sentence = "overlapwording overlapword overlap",searchWord = "overlap") == 1
    assert candidate(sentence = "the quick brown fox jumps over the lazy dog",searchWord = "the") == 1
    assert candidate(sentence = "prefix prefix prefix",searchWord = "prefix") == 1
    assert candidate(sentence = "prefix prefix prefix prefix",searchWord = "prefix") == 1
    assert candidate(sentence = "shorter is better",searchWord = "short") == 1
    assert candidate(sentence = "algorithms and data structures",searchWord = "and") == 2
    assert candidate(sentence = "interview question with multiple prefixes prefix",searchWord = "pre") == 5
    assert candidate(sentence = "banana bandana band breadth",searchWord = "ban") == 1
    assert candidate(sentence = "algorithms and data structures are fundamental",searchWord = "data") == 3
    assert candidate(sentence = "practice makes perfect in programming",searchWord = "per") == 3
    assert candidate(sentence = "verylongwordthatwilltesttheboundariesofthisfunction",searchWord = "verylong") == 1
    assert candidate(sentence = "longerprefix longerpre long pre",searchWord = "longerpre") == 1
    assert candidate(sentence = "this is a simple sentence with repeated words repeated words",searchWord = "repe") == 7
    assert candidate(sentence = "a quick brown fox jumps over the lazy dog",searchWord = "do") == 9
    assert candidate(sentence = "multiple occurrences of words words",searchWord = "words") == 4
    assert candidate(sentence = "double double double trouble",searchWord = "double") == 1
    assert candidate(sentence = "complicated complex complication",searchWord = "comp") == 1
    assert candidate(sentence = "banana bandana bandanna banana bandana",searchWord = "band") == 2
