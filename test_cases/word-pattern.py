# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(pattern = "aaaa",s = "dog cat cat dog") == False
    assert candidate(pattern = "abc",s = "dog dog dog") == False
    assert candidate(pattern = "abcd",s = "dog cat elephant fish") == True
    assert candidate(pattern = "aaaa",s = "dog dog dog dog") == True
    assert candidate(pattern = "he",s = "unit") == False
    assert candidate(pattern = "abb",s = "dog cat cat") == True
    assert candidate(pattern = "abab",s = "dog cat dog cat") == True
    assert candidate(pattern = "title",s = "title") == False
    assert candidate(pattern = "abc",s = "b c a") == True
    assert candidate(pattern = "abba",s = "dog dog dog dog") == False
    assert candidate(pattern = "aaa",s = "aa aa aa") == True
    assert candidate(pattern = "abc",s = "dog cat fish") == True
    assert candidate(pattern = "abba",s = "dog cat cat fish") == False
    assert candidate(pattern = "hello",s = "hello world") == False
    assert candidate(pattern = "abba",s = "dog cat cat dog") == True
    assert candidate(pattern = "jquery",s = "jquery") == False
    assert candidate(pattern = "a",s = "dog") == True
    assert candidate(pattern = "xyzyx",s = "apple banana cherry banana apple") == True
    assert candidate(pattern = "aabbccddeeff",s = "repeat a b c d e f") == False
    assert candidate(pattern = "aabbaa",s = "sun moon sun moon sun moon") == False
    assert candidate(pattern = "aabb",s = "apple banana apple banana") == False
    assert candidate(pattern = "abacaba",s = "car boat airplane car boat car airplane") == False
    assert candidate(pattern = "aabbccddeeff",s = "apple banana apple banana cherry cherry date date egg egg fig fig") == False
    assert candidate(pattern = "abcdefabc",s = "alpha beta gamma delta epsilon feta alpha beta gamma") == True
    assert candidate(pattern = "mnop",s = "red red blue blue") == False
    assert candidate(pattern = "qrstuv",s = "quick red slow tall ugly very") == True
    assert candidate(pattern = "aabbaa",s = "cat dog dog cat cat dog") == False
    assert candidate(pattern = "abcdab",s = "alpha beta gamma delta alpha beta") == True
    assert candidate(pattern = "pqrstuvw",s = "penny quill red slow tall usual very wavy") == True
    assert candidate(pattern = "aabbcc",s = "apple banana apple banana cherry cherry") == False
    assert candidate(pattern = "abcdef",s = "zebra lion tiger elephant fox dog") == True
    assert candidate(pattern = "abcabcabc",s = "cat dog bird cat dog bird cat dog bird") == True
    assert candidate(pattern = "aaaa",s = "cat cat cat cat") == True
    assert candidate(pattern = "abcdefgh",s = "alphabet in sequence") == False
    assert candidate(pattern = "abcdabcd",s = "sky cloud sun moon sky cloud sun moon") == True
    assert candidate(pattern = "abcabcabc",s = "car car car bike bike bike truck truck truck") == False
    assert candidate(pattern = "mnopq",s = "moon night ocean planet quest") == True
    assert candidate(pattern = "zzzz",s = "zebra zebra zebra zebra") == True
    assert candidate(pattern = "abcdabcd",s = "cat dog elephant fox cat dog elephant fox") == True
    assert candidate(pattern = "qrstuv",s = "zebra lion tiger bear eagle fox") == True
    assert candidate(pattern = "aaaaabbbbb",s = "cat cat cat cat cat dog dog dog dog dog") == True
    assert candidate(pattern = "xyxzy",s = "sky yacht sky yacht sky") == False
    assert candidate(pattern = "abcba",s = "tree bush grass bush tree") == True
    assert candidate(pattern = "qrstuvwx",s = "continuing the test") == False
    assert candidate(pattern = "abcabcabc",s = "hi ho ha hi ho ha hi ho ha") == True
    assert candidate(pattern = "abba",s = "ant bear bear ant") == True
    assert candidate(pattern = "pqrstuvw",s = "eight distinct words") == False
    assert candidate(pattern = "abab",s = "red blue red blue") == True
    assert candidate(pattern = "aabbcc",s = "moon moon star star sun sun") == True
    assert candidate(pattern = "aabbccdd",s = "red blue red blue red blue red blue") == False
    assert candidate(pattern = "abcdefg",s = "zebra ostrich lion tiger elephant seal fox") == True
    assert candidate(pattern = "abab",s = "apple banana apple banana") == True
    assert candidate(pattern = "ijklmnop",s = "another set of words") == False
    assert candidate(pattern = "aabbcc",s = "up down up down up down") == False
    assert candidate(pattern = "aabbcc",s = "red blue green red blue green") == False
    assert candidate(pattern = "mnopqrstuv",s = "elephant monkey lion tiger unicorn vampire werewolf goblin") == False
    assert candidate(pattern = "abcdefghij",s = "alpha beta gamma delta epsilon zeta eta theta iota kappa") == True
    assert candidate(pattern = "mnop",s = "moon night opus pug") == True
    assert candidate(pattern = "abcabc",s = "elephant elephant elephant dog dog dog") == False
    assert candidate(pattern = "abcb",s = "sun moon sun moon") == False
    assert candidate(pattern = "mnop",s = "moon night opal night") == False
    assert candidate(pattern = "mnopq",s = "five different words needed") == False
    assert candidate(pattern = "mnopqr",s = "man on top quick red") == False
    assert candidate(pattern = "abacaba",s = "car bike bus car bike car bike") == False
    assert candidate(pattern = "stuv",s = "shoe train umbrella vacuum") == True
    assert candidate(pattern = "qrst",s = "quick red small tall") == True
    assert candidate(pattern = "zzzz",s = "unique unique unique unique") == True
    assert candidate(pattern = "xyyx",s = "apple banana banana apple") == True
    assert candidate(pattern = "mnop",s = "moon night ocean planet") == True
    assert candidate(pattern = "aabbcc",s = "ant bee cat ant bee cat") == False
    assert candidate(pattern = "abcabcabc",s = "car boat plane car boat plane car boat plane") == True
    assert candidate(pattern = "vwxyzabc",s = "final set of words") == False
    assert candidate(pattern = "mnopqr",s = "moon night ocean pond quiet rain") == True
    assert candidate(pattern = "abab",s = "sun moon sun moon") == True
    assert candidate(pattern = "aabbaa",s = "hello world hello world hello world") == False
    assert candidate(pattern = "aaaa",s = "wolf wolf wolf wolf") == True
    assert candidate(pattern = "aabb",s = "red blue red blue") == False
    assert candidate(pattern = "abba",s = "hello world world hello") == True
    assert candidate(pattern = "abcdefg",s = "red blue green yellow purple orange pink") == True
    assert candidate(pattern = "mnopqr",s = "one two three four five six seven") == False
    assert candidate(pattern = "mnop",s = "mountain ocean night planet") == True
    assert candidate(pattern = "zzzzzzzzzz",s = "zero zero zero zero zero zero zero zero zero zero") == True
    assert candidate(pattern = "abcabc",s = "x y z x y z") == True
    assert candidate(pattern = "zzzz",s = "kite kite kite kite") == True
    assert candidate(pattern = "abac",s = "tree bush apple tree") == False
    assert candidate(pattern = "abcdabcd",s = "first second third fourth first second third fourth") == True
    assert candidate(pattern = "abcabc",s = "one two three one two three") == True
    assert candidate(pattern = "abac",s = "car truck airplane car") == False
    assert candidate(pattern = "zxyzzx",s = "zebra ostrich xerus zebra zebra xerus") == False
    assert candidate(pattern = "xyzx",s = "flower garden weed flower") == True
    assert candidate(pattern = "wwww",s = "word word word word") == True
    assert candidate(pattern = "abcd",s = "one two three four") == True
    assert candidate(pattern = "abac",s = "mango orange mango cherry") == True
    assert candidate(pattern = "xyzyxzyz",s = "red blue red blue red blue red blue") == False
    assert candidate(pattern = "xyyx",s = "xerox yellow yellow xerox") == True
    assert candidate(pattern = "abcabcabc",s = "sun moon earth sun moon earth sun moon earth") == True
    assert candidate(pattern = "xyzxyz",s = "moon sun moon sun moon sun") == False
    assert candidate(pattern = "xyzzyx",s = "tree bush apple apple bush tree") == True
    assert candidate(pattern = "zzzz",s = "star star star star") == True
    assert candidate(pattern = "abcdabcd",s = "one two three four one two three four") == True
    assert candidate(pattern = "abcdefghij",s = "one two three four five six seven eight nine ten") == True
    assert candidate(pattern = "abacaba",s = "sun moon sun moon earth sun moon") == False
    assert candidate(pattern = "abababa",s = "moon sun moon sun moon sun moon") == True
    assert candidate(pattern = "qrqrqr",s = "queen rabbit queen rabbit queen rabbit") == True
    assert candidate(pattern = "abcba",s = "start middle end middle start") == True
    assert candidate(pattern = "aabbaabb",s = "apple banana apple banana apple banana") == False
    assert candidate(pattern = "xyzx",s = "apple banana cherry apple") == True
    assert candidate(pattern = "abac",s = "one two three one") == False
    assert candidate(pattern = "abab",s = "up down up down down up") == False
    assert candidate(pattern = "ababab",s = "house car house car house car") == True
    assert candidate(pattern = "mnop",s = "red blue red green") == False
    assert candidate(pattern = "xyzz",s = "apple banana cherry cherry") == True
    assert candidate(pattern = "abca",s = "red blue green red") == True
    assert candidate(pattern = "ghijklmn",s = "next set of words") == False
    assert candidate(pattern = "aabbcc",s = "cat dog bird cat dog bird") == False
    assert candidate(pattern = "efgh",s = "elephant fox giraffe hippo") == True
    assert candidate(pattern = "aba",s = "car bike car") == True
    assert candidate(pattern = "abcdeabcde",s = "apple banana cat dog elephant apple banana cat dog elephant") == True
    assert candidate(pattern = "qrstuv",s = "table chair desk bed lamp shelf") == True
    assert candidate(pattern = "aabb",s = "car bike car bike") == False
    assert candidate(pattern = "mnop",s = "this is just a test") == False
    assert candidate(pattern = "mnopqrst",s = "more words for testing") == False
    assert candidate(pattern = "qrst",s = "unique words map correctly") == True
    assert candidate(pattern = "abcdefg",s = "one two three four five six seven") == True
    assert candidate(pattern = "aabbcc",s = "lion tiger lion tiger lion tiger") == False
    assert candidate(pattern = "abcabcabc",s = "hello world hello world hello world") == False
    assert candidate(pattern = "zzzzzz",s = "same same same same same same") == True
    assert candidate(pattern = "mnopqr",s = "zebra lion monkey narwhal otter penguin") == True
    assert candidate(pattern = "mnopq",s = "monster ocean night planet quest") == True
    assert candidate(pattern = "qrst",s = "quick red slow tall") == True
    assert candidate(pattern = "xyzxyz",s = "one two three one two three") == True
    assert candidate(pattern = "abacda",s = "car bike car dog car bike") == False
    assert candidate(pattern = "xyxzy",s = "red blue red blue green") == False
    assert candidate(pattern = "abcdefghij",s = "elephant monkey gorilla bear lion eagle wolf chicken dog ant") == True
    assert candidate(pattern = "aabbcc",s = "hello world hello world hello world") == False
    assert candidate(pattern = "aabbcc",s = "sun moon sun moon sun moon") == False
    assert candidate(pattern = "ababab",s = "red blue red blue red blue") == True
    assert candidate(pattern = "zzzz",s = "same same same same") == True
    assert candidate(pattern = "abcde",s = "alpha beta gamma delta epsilon") == True
    assert candidate(pattern = "abac",s = "hello world hello hello") == False
    assert candidate(pattern = "abcd",s = "alpha bravo charlie delta") == True
    assert candidate(pattern = "zzzz",s = "zoo zoo zoo zoo") == True
    assert candidate(pattern = "abcdefg",s = "pencil pen eraser notebook ruler glue scissor") == True
    assert candidate(pattern = "xyyx",s = "car truck truck car") == True
    assert candidate(pattern = "xyz",s = "sun moon stars") == True
    assert candidate(pattern = "abcdefg",s = "alpha bravo charlie delta echo foxtrot golf") == True
    assert candidate(pattern = "abcabcabc",s = "dog cat dog cat dog cat dog") == False
