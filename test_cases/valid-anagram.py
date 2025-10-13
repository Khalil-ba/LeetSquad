# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(s = "abcde",t = "edcba") == True
    assert candidate(s = "abc",t = "abcd") == False
    assert candidate(s = "apple",t = "pale") == False
    assert candidate(s = "hello",t = "bello") == False
    assert candidate(s = "aacc",t = "ccac") == False
    assert candidate(s = "abc",t = "def") == False
    assert candidate(s = "abc",t = "cba") == True
    assert candidate(s = "abcd",t = "abce") == False
    assert candidate(s = "anagram",t = "nagaram") == True
    assert candidate(s = "rat",t = "car") == False
    assert candidate(s = "a",t = "a") == True
    assert candidate(s = "ab",t = "ba") == True
    assert candidate(s = "listen",t = "silent") == True
    assert candidate(s = "abcd",t = "dcba") == True
    assert candidate(s = "triangle",t = "integral") == True
    assert candidate(s = "aabbcc",t = "abcabc") == True
    assert candidate(s = "",t = "") == True
    assert candidate(s = "ababababababababab",t = "bababababababababa") == True
    assert candidate(s = "hello world",t = "worldhello") == False
    assert candidate(s = "theeyes",t = "theysee") == True
    assert candidate(s = "repeatedcharactershere",t = "repeatedcharactershere") == True
    assert candidate(s = "ababababab",t = "bababababa") == True
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zzxxyywwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == True
    assert candidate(s = "the quick brown fox",t = "xof nworb kciuq eht") == True
    assert candidate(s = "astronomer",t = "moonstarer") == True
    assert candidate(s = "thisisananagram",t = "isanagramthis") == False
    assert candidate(s = "spaces should be ignored",t = "should be ignored spaces") == True
    assert candidate(s = "aabbcc",t = "ccbbaa") == True
    assert candidate(s = "special!@#$%^&*()characters",t = "characters)!@#$%^&*()special") == False
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz",t = "zzzzyyyxxxwwwwvvvvuuuuttttssssrrrrqqqqppppooooonnnnmmmmllllkkkkjjjjiiiigggghhhhffffffeeeeeeeeddccccbbbbaaaa") == False
    assert candidate(s = "anagram",t = "nagarams") == False
    assert candidate(s = "dormitory",t = "dirtyroom") == True
    assert candidate(s = "1234567890",t = "0987654321") == True
    assert candidate(s = "anananana",t = "naanaanna") == True
    assert candidate(s = "",t = "a") == False
    assert candidate(s = "thisisanagramtest",t = "agamnartisiesttst") == False
    assert candidate(s = "hello world",t = "world hello") == True
    assert candidate(s = "a gentleman",t = "elegant man") == True
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zzyyxxwwvvuuttrrssqqppoonnmmllkkjjiihhggffeeddccbbaa") == True
    assert candidate(s = "aabbcc",t = "aabbc") == False
    assert candidate(s = "school master",t = "the classroom") == True
    assert candidate(s = "thisisaverylongstringthatwearetesting",t = "averylongstringthatwearetestingthisis") == True
    assert candidate(s = "thequickbrownfoxjumpsoverthelazydog",t = "godzylathedelvropmusfixnworbquickthe") == False
    assert candidate(s = "thisisananagram",t = "isananagramthis") == True
    assert candidate(s = "funeral",t = "real fun") == False
    assert candidate(s = "unitedstates",t = "adtenisestatesu") == False
    assert candidate(s = "mississippi",t = "mississipi") == False
    assert candidate(s = "elevenplus",t = "twelvestop") == False
    assert candidate(s = "a",t = "b") == False
    assert candidate(s = "anagramanagramanagram",t = "nagaramnagaramnagaram") == True
    assert candidate(s = "aabbccdd",t = "ddbbaacc") == True
    assert candidate(s = "aquickbrownfoxjumpsoverthelazydog",t = "quickbrownfoxjumpsoverthelazydoga") == True
    assert candidate(s = "abcdeabced",t = "abcedabcde") == True
    assert candidate(s = "aquickbrownfoxjumpsoverthelazydog",t = "thelazydogjumpsoveraquickbrownfox") == True
    assert candidate(s = "pythonprogramming",t = "nohtypgnimmargorp") == True
    assert candidate(s = "forty five",t = "over fifty") == True
    assert candidate(s = "a!@#b$%^c&*()",t = "c&*()b$%^a!@#") == True
    assert candidate(s = "aquickbrownfoxjumpsoverthelazydog",t = "quickbrownfoxjumpsoverthelazygod") == False
    assert candidate(s = "noon",t = "noon") == True
    assert candidate(s = "anagrammatic",t = "icnagarammat") == True
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(s = "abacabadabacaba",t = "bacabacabacaba") == False
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggeeffddeebbaa") == False
    assert candidate(s = "the quick brown fox jumps over the lazy dog",t = "dog lazy the over jumps fox brown quick the") == True
    assert candidate(s = "conversation",t = "voices rant on") == False
    assert candidate(s = "eleven plus two",t = "twelve plus one") == True
    assert candidate(s = "the eyes",t = "they see") == True
    assert candidate(s = "conversation",t = "voicesranton") == True
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggeeffddccbbbaa") == False
    assert candidate(s = "anagramanagram",t = "nagaramnagaram") == True
    assert candidate(s = "this is a test",t = "test a is this") == True
    assert candidate(s = "night",t = "thing") == True
    assert candidate(s = "aaabbbccc",t = "bbbaaacc") == False
    assert candidate(s = "samecharacters",t = "charactersames") == True
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zzyxwvuttsrqponmlkjihgfeddcbaabbccddeeffgghhiijjkkllmmnnooppqqrrss") == False
    assert candidate(s = "mississippi",t = "ssmissippii") == True
    assert candidate(s = "abcabcabcabcabcabc",t = "abcabcabcabcabcabc") == True
    assert candidate(s = "xxyyzz",t = "zzxxyy") == True
    assert candidate(s = "thequickbrownfoxjumpsoverthelazydog",t = "thequickbrownfoxjumpsoverthelazygod") == True
    assert candidate(s = "elevenpluszwo",t = "twelvezillion") == False
    assert candidate(s = "notanagramhere",t = "anagramherenot") == True
    assert candidate(s = "uniqueanagram",t = "nagramuniqueanagram") == False
    assert candidate(s = "fluster",t = "restful") == True
    assert candidate(s = "dormitory",t = "dirty room") == False
    assert candidate(s = "aaaaaa",t = "aaaaa") == False
    assert candidate(s = "punishments",t = "ninepunishment") == False
    assert candidate(s = "thirty",t = "typhrirt") == False
    assert candidate(s = "racecar",t = "carrace") == True
    assert candidate(s = "ab",t = "aabb") == False
    assert candidate(s = "a",t = "") == False
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",t = "mnbvcxzlkjhgfdsapoiuytrewq") == True
    assert candidate(s = "abacax",t = "aacxab") == True
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(s = "questionnaire",t = "reinquirequest") == False
    assert candidate(s = "anagramatically",t = "gramaticallyanagram") == False
    assert candidate(s = "uniquecharacters",t = "uniquecharactersx") == False
    assert candidate(s = "abcdabcdabcd",t = "dcbaabcdabcd") == True
    assert candidate(s = "adobe",t = "abode") == True
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zzzyyxwwvvuuttssrrqqppoonnmlkkjjiihhggffeeeeddccbaab") == False
    assert candidate(s = "clint eastwood",t = "old west action") == False
    assert candidate(s = "abcabcabcabc",t = "cbacbacbacba") == True
    assert candidate(s = "schoolmaster",t = "theclassroom") == True
    assert candidate(s = "embarrassing",t = "backgroundsere") == False
    assert candidate(s = "racecar",t = "racecar") == True
    assert candidate(s = "nematocysts",t = "cytoplasmnets") == False
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zzyyxxwwvvuuttsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbaa") == False
