# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(words = ['sky', 'fly', 'why'],left = 0,right = 2) == 0
    assert candidate(words = ['apple', 'banana', 'orange', 'umbrella'],left = 0,right = 3) == 3
    assert candidate(words = ['are', 'amy', 'u'],left = 0,right = 2) == 2
    assert candidate(words = ['hey', 'aeo', 'mu', 'ooo', 'artro'],left = 1,right = 4) == 3
    assert candidate(words = ['up', 'open', 'over'],left = 1,right = 2) == 0
    assert candidate(words = ['ae', 'ea', 'ei', 'ie', 'ou'],left = 0,right = 4) == 5
    assert candidate(words = ['aeiou', 'uoiea', 'aeiou', 'uoiea', 'aeiou', 'uoiea'],left = 0,right = 5) == 6
    assert candidate(words = ['sky', 'fly', 'why', 'a', 'e'],left = 0,right = 4) == 2
    assert candidate(words = ['umbrella', 'encyclopedia', 'analysis', 'outstanding', 'initiative'],left = 1,right = 3) == 1
    assert candidate(words = ['ocean', 'mountain', 'forest', 'desert', 'rain'],left = 0,right = 4) == 0
    assert candidate(words = ['beautiful', 'world', 'with', 'diverse', 'languages'],left = 2,right = 4) == 0
    assert candidate(words = ['aeiou', 'uoiea', 'uiaeou', 'ouaei', 'eioua'],left = 0,right = 4) == 5
    assert candidate(words = ['xylophone', 'zephyr', 'orchestra', 'xylophone', 'aeiou', 'uoiea', 'uoiea'],left = 0,right = 6) == 4
    assert candidate(words = ['aaa', 'eee', 'iii', 'ooo', 'uuu', 'aaee', 'eeaa', 'aeea', 'aaea', 'eeea', 'eaae', 'eaeaa', 'aeaae', 'aaeae'],left = 0,right = 13) == 14
    assert candidate(words = ['queue', 'adieu', 'ice', 'ocean', 'earth'],left = 0,right = 3) == 2
    assert candidate(words = ['umbrella', 'moon', 'noon', 'noon', 'moon'],left = 2,right = 4) == 0
    assert candidate(words = ['algorithm', 'education', 'umbrella', 'icecream', 'operation', 'university'],left = 1,right = 5) == 1
    assert candidate(words = ['umbrella', 'opposite', 'idea', 'encyclopedia', 'algorithm', 'umbrella', 'opposite', 'idea', 'encyclopedia', 'algorithm'],left = 3,right = 7) == 4
    assert candidate(words = ['elephant', 'umbrella', 'apple', 'orange', 'ice', 'echo', 'umbrella'],left = 1,right = 6) == 6
    assert candidate(words = ['aviation', 'exhibition', 'occasion', 'environment', 'instrumentation'],left = 1,right = 3) == 0
    assert candidate(words = ['vowel', 'nonvowel', 'aeiou', 'bvowel', 'endvowel'],left = 0,right = 4) == 1
    assert candidate(words = ['aabb', 'abba', 'baab', 'baba', 'abab'],left = 0,right = 4) == 1
    assert candidate(words = ['example', 'samples', 'tests', 'inputs', 'outputs'],left = 0,right = 4) == 1
    assert candidate(words = ['xyz', 'uvw', 'qwe', 'rty', 'poi'],left = 0,right = 4) == 0
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],left = 0,right = 24) == 5
    assert candidate(words = ['environment', 'umbrella', 'education', 'algorithm', 'university', 'encyclopedia'],left = 2,right = 5) == 1
    assert candidate(words = ['beautiful', 'enormous', 'interesting', 'unexpected', 'odd'],left = 2,right = 4) == 0
    assert candidate(words = ['sequence', 'equal', 'education', 'algorithm', 'encyclopedia'],left = 0,right = 3) == 0
    assert candidate(words = ['eeeee', 'aaaaa', 'iiiii', 'ooooo', 'uuuuu', 'auaeu', 'eiaie', 'ouioo', 'uaeuu', 'ieoia'],left = 2,right = 9) == 8
    assert candidate(words = ['abcdefgh', 'ijklmnop', 'qrstuvwxyz', 'zyxwvutsr', 'qrstponmlkjihgfedcba'],left = 0,right = 4) == 0
    assert candidate(words = ['banana', 'orange', 'grape', 'kiwi', 'pear', 'peach', 'plum', 'grapefruit', 'blueberry', 'cherry'],left = 3,right = 9) == 0
    assert candidate(words = ['racecar', 'level', 'rotor', 'kayak', 'reviler'],left = 1,right = 4) == 0
    assert candidate(words = ['aerodynamic', 'encyclopedia', 'umbrella', 'idea', 'audio'],left = 1,right = 4) == 4
    assert candidate(words = ['umbrella', 'map', 'python', 'algorithm', 'encyclopedia'],left = 1,right = 4) == 1
    assert candidate(words = ['umbrella', 'opposite', 'idea', 'encyclopedia', 'algorithm'],left = 1,right = 4) == 3
    assert candidate(words = ['quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog'],left = 1,right = 5) == 0
    assert candidate(words = ['aardvark', 'elephant', 'iguana', 'okapi', 'umbrella'],left = 0,right = 4) == 3
    assert candidate(words = ['vowel', 'voewl', 'ovwle', 'wolve', 'volve'],left = 0,right = 4) == 1
    assert candidate(words = ['beautiful', 'umbrella', 'innovative', 'economic', 'outstanding', 'underwater'],left = 0,right = 5) == 2
    assert candidate(words = ['applepie', 'banana', 'orangejuice', 'grape', 'peach'],left = 1,right = 3) == 1
    assert candidate(words = ['ar', 'er', 'ir', 'or', 'ur'],left = 1,right = 4) == 0
    assert candidate(words = ['a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u'],left = 0,right = 9) == 10
    assert candidate(words = ['sequence', 'development', 'environment', 'assignment', 'information'],left = 1,right = 3) == 0
    assert candidate(words = ['a', 'e', 'i', 'o', 'u', 'aeiou'],left = 0,right = 5) == 6
    assert candidate(words = ['racecar', 'level', 'rotor', 'deified', 'repaper'],left = 1,right = 4) == 0
    assert candidate(words = ['orchid', 'ocean', 'octopus', 'ostrich', 'oak', 'oceanography'],left = 0,right = 5) == 0
    assert candidate(words = ['volcano', 'trident', 'ozone', 'ocean', 'mountain'],left = 2,right = 4) == 1
    assert candidate(words = ['zzzzz', 'yyyyy', 'xxxxx', 'wwwww', 'vvvvv'],left = 0,right = 4) == 0
    assert candidate(words = ['banana', 'anana', 'nana', 'ana', 'na', 'a'],left = 0,right = 9) == 3
    assert candidate(words = ['education', 'university', 'algorithm', 'openai'],left = 1,right = 3) == 1
    assert candidate(words = ['aeiou', 'bcd', 'efg', 'hij', 'klm', 'nop', 'qrst', 'uvw', 'xyz'],left = 2,right = 7) == 0
    assert candidate(words = ['aardvark', 'algorithm', 'antelope', 'antenna', 'apple', 'antiquity', 'apricot', 'atlas'],left = 1,right = 7) == 3
    assert candidate(words = ['algorithm', 'evaluation', 'interview', 'education', 'optimization'],left = 0,right = 4) == 0
    assert candidate(words = ['aeiou', 'uoiea', 'iouea', 'uaieo', 'oieau', 'aeo', 'uoiea', 'uoiea', 'uoiea', 'uoiea', 'uoiea', 'uoiea'],left = 0,right = 11) == 12
    assert candidate(words = ['abracadabra', 'alabama', 'alaska', 'aerodynamic', 'algorithm', 'azalea'],left = 1,right = 5) == 3
    assert candidate(words = ['start', 'end', 'begin', 'finish', 'conclude'],left = 0,right = 4) == 0
    assert candidate(words = ['education', 'is', 'awesome', 'and', 'effective'],left = 1,right = 4) == 2
    assert candidate(words = ['xyz', 'uvw', 'qrs', 'tuv', 'lmn', 'opq'],left = 1,right = 5) == 0
    assert candidate(words = ['aeiou', 'ueiou', 'ieoai', 'oeuia', 'uaeio'],left = 0,right = 4) == 5
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],left = 0,right = 14) == 4
    assert candidate(words = ['xylophone', 'xylophones', 'xylophonically', 'xylophonist', 'xylophonists'],left = 0,right = 4) == 0
    assert candidate(words = ['aeiou', 'uaeiou', 'aeu', 'aue', 'eua'],left = 0,right = 4) == 5
    assert candidate(words = ['xylophone', 'yacht', 'gymnymphilia', 'hydrangea', 'ivory'],left = 0,right = 4) == 0
    assert candidate(words = ['bcd', 'efg', 'hij', 'klm', 'nop'],left = 0,right = 4) == 0
    assert candidate(words = ['algorithm', 'education', 'umbrella', 'encyclopedia', 'ocean'],left = 2,right = 4) == 2
    assert candidate(words = ['a', 'e', 'i', 'o', 'u'],left = 0,right = 4) == 5
    assert candidate(words = ['umbrella', 'raincoat', 'scarf', 'boots', 'gloves', 'jacket', 'shoes', 'hat', 'mittens', 'gloves', 'umbrella', 'hat'],left = 0,right = 11) == 2
    assert candidate(words = ['a', 'a', 'a', 'a', 'a', 'a'],left = 0,right = 5) == 6
    assert candidate(words = ['education', 'algorithm', 'encyclopedia', 'under', 'umbrella'],left = 1,right = 4) == 2
    assert candidate(words = ['aeiou', 'uoiea', 'aieou', 'euoia', 'oueai'],left = 0,right = 4) == 5
    assert candidate(words = ['education', 'university', 'algorithm', 'optimization', 'encyclopedia'],left = 1,right = 4) == 1
    assert candidate(words = ['aabbcc', 'ddeeff', 'gghhii', 'jjkkll', 'mmnnoo'],left = 0,right = 4) == 0
    assert candidate(words = ['education', 'algorithm', 'umbrella', 'opposite', 'idea'],left = 0,right = 4) == 3
    assert candidate(words = ['aeiouaeiou', 'uoieauoiea', 'aieouaieou', 'euoiaeuoia', 'oueaioueai'],left = 1,right = 3) == 3
    assert candidate(words = ['aaa', 'eee', 'iii', 'ooo', 'uuu'],left = 0,right = 4) == 5
    assert candidate(words = ['education', 'umbrella', 'idea', 'algorithm', 'elephant'],left = 1,right = 4) == 2
    assert candidate(words = ['abacaxi', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince'],left = 0,right = 11) == 2
    assert candidate(words = ['sequential', 'programming', 'leads', 'to', 'complexity'],left = 1,right = 3) == 0
    assert candidate(words = ['aeiou', 'uoiea', 'ioeau', 'oaeiu', 'ueiao'],left = 0,right = 4) == 5
    assert candidate(words = ['aaaaa', 'eeeee', 'iiiii', 'ooooo', 'uuuuu'],left = 1,right = 3) == 3
    assert candidate(words = ['sequence', 'encounter', 'interval', 'equation', 'occasion'],left = 2,right = 4) == 0
    assert candidate(words = ['acoustic', 'analysis', 'bassoon', 'clarinet', 'didgeridoo', 'flute', 'guitar', 'harp', 'harp', 'piano', 'tuba'],left = 2,right = 10) == 0
    assert candidate(words = ['sequence', 'sequences', 'sequentially', 'sequenceable', 'sequenceless'],left = 2,right = 4) == 0
    assert candidate(words = ['ae', 'ea', 'oi', 'io', 'ou', 'uo'],left = 0,right = 5) == 6
    assert candidate(words = ['understanding', 'learning', 'grows', 'every', 'day'],left = 0,right = 2) == 0
    assert candidate(words = ['a', 'b', 'c', 'd', 'e'],left = 0,right = 4) == 2
    assert candidate(words = ['elephant', 'giraffe', 'hippo', 'iguana', 'jaguar'],left = 0,right = 4) == 1
    assert candidate(words = ['xylophone', 'xylo', 'yolo', 'mono', 'neon'],left = 1,right = 4) == 0
    assert candidate(words = ['sequence', 'structure', 'synergy', 'symmetry', 'spectrum', 'syzygy'],left = 2,right = 5) == 0
    assert candidate(words = ['vowel', 'testing', 'algorithm', 'education', 'umbrella', 'sequence', 'interview', 'exhibition', 'occasion', 'environment'],left = 3,right = 8) == 1
    assert candidate(words = ['algorithm', 'data', 'structure', 'programming', 'language'],left = 2,right = 4) == 0
    assert candidate(words = ['', 'a', 'e', 'i', 'o', 'u', 'aeiou', 'uoiea', 'euioa', 'aoieu'],left = 1,right = 9) == 9
    assert candidate(words = ['vowel', 'words', 'only', 'here', 'now'],left = 0,right = 4) == 0
    assert candidate(words = ['aeiou', 'eioua', 'iouae', 'ouaei', 'uaeio'],left = 0,right = 4) == 5
    assert candidate(words = ['vowel', 'vowels', 'vowelstring', 'vowelstrings', 'vowels', 'strings', 'string', 'vow', 'owel', 'vowels', 'vowel'],left = 3,right = 10) == 0
    assert candidate(words = ['vowel', 'start', 'end', 'middle', 'zone', 'sequence'],left = 2,right = 5) == 0
    assert candidate(words = ['sequence', 'queue', 'deque', 'peep', 'beep', 'keel', 'heel', 'heal', 'heap', 'heap', 'jeep', 'weep'],left = 1,right = 11) == 0
    assert candidate(words = ['elephant', 'antelope', 'giraffe', 'hippo', 'iguana', 'jackal', 'kangaroo', 'lemur'],left = 1,right = 7) == 2
    assert candidate(words = ['amazing', 'algorithm', 'umbrella', 'opposite', 'idea', 'beautiful', 'enormous', 'interesting', 'unexpected', 'odd'],left = 0,right = 9) == 3
