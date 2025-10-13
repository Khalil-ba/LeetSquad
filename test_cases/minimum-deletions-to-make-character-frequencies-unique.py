# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = "aab") == 0
    assert candidate(s = "aabacabadabaeabafabagabahabaiabajabakabalabamabanabaoabapabaqabarabasabataabuabavabawabaxabayabajabaz") == 22
    assert candidate(s = "abcabcabc") == 3
    assert candidate(s = "aabbbcccddddeeeeeffffffggggggghhhhhhhhiiiiiiiii") == 2
    assert candidate(s = "zzzzzzzzzz") == 0
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzz") == 24
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 25
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 49
    assert candidate(s = "ceabaacb") == 2
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
    assert candidate(s = "aaabbbcc") == 2
    assert candidate(s = "aabbccddeeffgghhii") == 15
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 25
    assert candidate(s = "a") == 0
    assert candidate(s = "zzzzzzzzzzyyyyyyyyyxxxxxxxwwwwwwvvvvuuuuutttttsssssrrrrqqqqppppooooonnnnmmmmlllkkkjjjiii") == 41
    assert candidate(s = "aabbccddeeefffggg") == 11
    assert candidate(s = "aabbccddeeefffhhhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 48
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzz") == 47
    assert candidate(s = "pppppppppooooooonnnnnmmmllllllkkkkjjjjiiiiiiiihhhhhhhggggggg") == 15
    assert candidate(s = "aabbbccccddddeeeee") == 3
    assert candidate(s = "abababababababababab") == 1
    assert candidate(s = "zzzzzzzzzzzyyyyyyyxxxxxxxwwwwwwvvvvuuuutttssrrqponmlkjihgfedcba") == 24
    assert candidate(s = "aabbbcccddddeeeeeffffffggggggghhhhhhhhiiiiiiiiijjjjjjjjjj") == 2
