# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(sentence = "sentence ence sent") == False
    assert candidate(sentence = "hello olleh") == True
    assert candidate(sentence = "Aa Aa") == False
    assert candidate(sentence = "ab ba") == True
    assert candidate(sentence = "a") == True
    assert candidate(sentence = "Leetcode is cool") == False
    assert candidate(sentence = "b") == True
    assert candidate(sentence = "A aA A") == False
    assert candidate(sentence = "abcd dcba") == True
    assert candidate(sentence = "circular rular circul") == False
    assert candidate(sentence = "Zz zZ") == True
    assert candidate(sentence = "abc cba") == True
    assert candidate(sentence = "a a a a") == True
    assert candidate(sentence = "example ample exa") == False
    assert candidate(sentence = "A a A") == False
    assert candidate(sentence = "Zz") == False
    assert candidate(sentence = "eetcode") == True
    assert candidate(sentence = "abc cab bca") == True
    assert candidate(sentence = "abc bca cab") == False
    assert candidate(sentence = "B ba B") == False
    assert candidate(sentence = "leetcode exercises sound delightful") == True
    assert candidate(sentence = "b b b") == True
    assert candidate(sentence = "a b c a") == False
    assert candidate(sentence = "A a") == False
    assert candidate(sentence = "test tset") == True
    assert candidate(sentence = "aba") == True
    assert candidate(sentence = "mnopqr stuvwx yzab cd efgh ijklm nopqr") == False
    assert candidate(sentence = "world dlrow") == True
    assert candidate(sentence = "abcdefghijklmnopqrstuvwxyz zabcdefghijklmnopqrstuvwxy") == False
    assert candidate(sentence = "No lemon no melon") == False
    assert candidate(sentence = "Anna") == False
    assert candidate(sentence = "Able was I ere I saw Elba Able") == False
    assert candidate(sentence = "Was it a car or a cat I saw saw I tac a ro rac a si taW taW") == False
    assert candidate(sentence = "Madam In Eden Im Adam") == False
    assert candidate(sentence = "Circular logic confuses brains sourcing smiles") == False
    assert candidate(sentence = "Rotation noitator tor") == False
    assert candidate(sentence = "noon moon moon") == False
    assert candidate(sentence = "peep peep") == True
    assert candidate(sentence = "b aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa aaaaaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaaa aaaaaaaaaaaaaa aaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaa b") == False
    assert candidate(sentence = "Noon neons number nicely") == False
    assert candidate(sentence = "Madam madam madam") == False
    assert candidate(sentence = "refer level civic civic civic level refer") == False
    assert candidate(sentence = "xyyx xxyy") == False
    assert candidate(sentence = "kayak kayak kayak kayak") == True
    assert candidate(sentence = "rotor racecar level deed civic") == False
    assert candidate(sentence = "stats tacocat stats") == False
    assert candidate(sentence = "racecar civic madam") == False
    assert candidate(sentence = "Step on no pets no step on no pets") == False
    assert candidate(sentence = "Able was I I saw Elba Elba saw I I was Able") == False
    assert candidate(sentence = "tacocat") == True
    assert candidate(sentence = "a quick brown fox jumps over lazy a") == False
    assert candidate(sentence = "zoo online one nice Easter egg") == False
    assert candidate(sentence = "Word dOrw") == False
    assert candidate(sentence = "deed deed") == True
    assert candidate(sentence = "daemon daemon") == False
    assert candidate(sentence = "Palindrome emordnilaP") == True
    assert candidate(sentence = "madam racecar civic") == False
    assert candidate(sentence = "Circular arular ci") == False
    assert candidate(sentence = "Madam adaM") == False
    assert candidate(sentence = "A Santa at NASA") == False
    assert candidate(sentence = "sun sets slowly on nosy wonks") == False
    assert candidate(sentence = "madam racecar level deed civic kayak rotor") == False
    assert candidate(sentence = "abcde edcba") == True
    assert candidate(sentence = "Nested edset n") == False
    assert candidate(sentence = "kayak kayak") == True
    assert candidate(sentence = "Nurses run Nurses") == False
    assert candidate(sentence = "Programming gnostic stem ngram minnow winnow now") == False
    assert candidate(sentence = "rotor rotor") == True
    assert candidate(sentence = "redivider") == True
    assert candidate(sentence = "racecar civic level deed") == False
    assert candidate(sentence = "Abba aaaa aa a") == False
    assert candidate(sentence = "xylophone elephant monkey keen") == False
    assert candidate(sentence = "xyzzyx") == True
    assert candidate(sentence = "circularloop loop") == False
    assert candidate(sentence = "Alaska Kansas suck slyly yelling nasty nasty yaks yak salty knapsack sacks sacks sky kayak kayak kayak") == False
    assert candidate(sentence = "x y z x") == False
    assert candidate(sentence = "programming is simply programming") == False
    assert candidate(sentence = "zoo omega meal alpha") == False
    assert candidate(sentence = "Loop opLo") == False
    assert candidate(sentence = "Startling lightning bugs ignited giants") == False
    assert candidate(sentence = "xylophone one love evolution nation") == False
    assert candidate(sentence = "deed deed deed") == True
    assert candidate(sentence = "Palindrome emordnilaP laP") == False
    assert candidate(sentence = "noon odd level civic civic civic level odd noon") == False
    assert candidate(sentence = "Was it a car or a cat I saw Was") == False
    assert candidate(sentence = "Reflection noitcifilr") == False
    assert candidate(sentence = "ab ba ac ca") == True
    assert candidate(sentence = "racecar racecar") == True
    assert candidate(sentence = "abracadabra arachnophobia") == True
    assert candidate(sentence = "repaper repaper repaper") == True
    assert candidate(sentence = "Complex xs w x") == False
    assert candidate(sentence = "abcd defg ghij jkla") == True
    assert candidate(sentence = "Interstellar rstellar inter") == False
    assert candidate(sentence = "reviled devil level deed vile derevered") == False
    assert candidate(sentence = "Fascinating ideas inspire amazing minds") == False
    assert candidate(sentence = "Alphabet tebahpla A") == False
    assert candidate(sentence = "Unique new weird weed nude euqinu") == False
    assert candidate(sentence = "Wow wow") == False
    assert candidate(sentence = "tortoise einstein noodles stein snot not ossetia") == False
    assert candidate(sentence = "rotor kayak rotor") == False
    assert candidate(sentence = "kayak kayak kayak kayak kayak") == True
    assert candidate(sentence = "zebra apple orange night eagle") == False
    assert candidate(sentence = "Zebra apple orange elephant") == False
    assert candidate(sentence = "redder redder") == True
    assert candidate(sentence = "No lemon no melon no lemon no melon") == False
    assert candidate(sentence = "xylophone elephant monkey keen noodle leet teex") == False
    assert candidate(sentence = "Anna civic radar level rotor") == False
    assert candidate(sentence = "zoo omega anna apple") == False
    assert candidate(sentence = "Detartrated dater dated") == False
    assert candidate(sentence = "xylophone excellent noodles seen") == False
    assert candidate(sentence = "Madam madam") == False
    assert candidate(sentence = "level level") == True
    assert candidate(sentence = "abracadabra aracnidae earthworms mammals sloths") == False
    assert candidate(sentence = "level level level level") == True
    assert candidate(sentence = "Wow wow wow") == False
    assert candidate(sentence = "palindrome emordnilap") == True
    assert candidate(sentence = "Was it a car or a cat I saw seen saw I tac a ro rac a ti saw") == False
    assert candidate(sentence = "a aa aaa aaaa") == True
    assert candidate(sentence = "xylophone objective elegant elegant not") == False
    assert candidate(sentence = "b b b b b") == True
    assert candidate(sentence = "XYlophone emotion motion nation") == False
    assert candidate(sentence = "Zoos own cozy zones") == False
    assert candidate(sentence = "deified deified deified deified") == True
    assert candidate(sentence = "Was it a car or a cat I saw") == False
    assert candidate(sentence = "Zebra apple apple orange onion nginx") == False
    assert candidate(sentence = "cycle ycle c") == False
    assert candidate(sentence = "Wow") == False
    assert candidate(sentence = "Programming gamifies lessons yielding successes") == False
    assert candidate(sentence = "Rhythms mesmerize symphonies") == False
    assert candidate(sentence = "Madam Ada") == False
    assert candidate(sentence = "Madam Arora teaches malayalam Madam") == False
    assert candidate(sentence = "Rotator taro Rotator") == False
    assert candidate(sentence = "a a a a a a a a a a a a") == True
    assert candidate(sentence = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == True
    assert candidate(sentence = "Civic civic") == False
    assert candidate(sentence = "repaper deed deed deed deed deed deed deed deed deed deed deed deed deed deed deed deed deed deed deed deed") == False
    assert candidate(sentence = "kayak civic deed level odd noon") == False
    assert candidate(sentence = "Madam Arora teaches malayalam") == False
    assert candidate(sentence = "noon odd level deed civic kayak") == False
    assert candidate(sentence = "giraffe elephant noodle leet teex xxyy") == False
    assert candidate(sentence = "Echo Charlie Hotel Hotel Echo") == False
    assert candidate(sentence = "racecar madam rotator") == False
    assert candidate(sentence = "a b c d e f g h i j k l m n o p q r s t u v w x y z a") == False
    assert candidate(sentence = "solo ollas solar lassos") == False
    assert candidate(sentence = "madamrefer") == False
    assert candidate(sentence = "civic racecar level madam deed rotator redivider") == False
    assert candidate(sentence = "Tactocat civic") == False
    assert candidate(sentence = "Xylophones yield xenial xylophiles") == False
    assert candidate(sentence = "civic deed level civic civic") == False
    assert candidate(sentence = "Underground neutergnu") == False
    assert candidate(sentence = "rotor") == True
    assert candidate(sentence = "racecar") == True
    assert candidate(sentence = "singleword") == False
    assert candidate(sentence = "zoo ooz zoo") == False
    assert candidate(sentence = "redder redivider redivider") == True
    assert candidate(sentence = "xylophone one phone nova ava axolotl talontax") == False
    assert candidate(sentence = "ab ac ad ae af ag ah ai aj ak al am an ao ap aq ar as at au av aw ax ay az") == False
    assert candidate(sentence = "kayak kayak kayak kayak kayak kayak kayak kayak kayak kayak kayak kayak kayak kayak kayak kayak kayak kayak kayak kayak kayak") == True
    assert candidate(sentence = "a aa aaaa a") == True
    assert candidate(sentence = "Mushroom nrooms moss stamper reaper") == False
    assert candidate(sentence = "daemon nomad") == True
    assert candidate(sentence = "AbCd DeFg GhIj JkLa") == False
    assert candidate(sentence = "level deed deed level") == False
    assert candidate(sentence = "Stressed desserts") == False
    assert candidate(sentence = "stats stats") == True
    assert candidate(sentence = "A Santa at NASA A") == False
    assert candidate(sentence = "civic madam racecar") == False
    assert candidate(sentence = "repaper repaper") == True
    assert candidate(sentence = "Palindrome emordnilaP el") == False
    assert candidate(sentence = "Able was I I saw Elba") == False
    assert candidate(sentence = "Programming ngRams Make sense") == False
    assert candidate(sentence = "Mimi") == False
    assert candidate(sentence = "rotor rotor rotor") == True
    assert candidate(sentence = "rotor rotor rotor rotor") == True
    assert candidate(sentence = "A Toyota tacoma玛 its a Toyota tacoma玛") == False
    assert candidate(sentence = "rotator rotator") == True
    assert candidate(sentence = "No lemon no melon No") == False
    assert candidate(sentence = "Step on no pets") == False
    assert candidate(sentence = "A Santa at NASA at a Santa A") == False
    assert candidate(sentence = "Was it a car or a cat I saw saw I tac a ro rac a si taW") == False
    assert candidate(sentence = "a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa aaaaaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaaa aaaaaaaaaaaaaa aaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaa a") == True
    assert candidate(sentence = "redivider deified civic level rotator deed madam racecar") == False
    assert candidate(sentence = "a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa aaaaaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaaa aaaaaaaaaaaaaa aaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaa") == True
    assert candidate(sentence = "level level level") == True
    assert candidate(sentence = "deified deified") == True
    assert candidate(sentence = "Circular larriuC") == False
    assert candidate(sentence = "Symmetry try sym") == False
    assert candidate(sentence = "redivider redivider") == True
    assert candidate(sentence = "banana apple orange emitter") == False
    assert candidate(sentence = "reviled devil") == False
    assert candidate(sentence = "abracadabra arachnid did deep peeled Elba bar") == False
    assert candidate(sentence = "civic deed civic deed") == False
    assert candidate(sentence = "Wow kayak wow wow wow wow wow") == False
    assert candidate(sentence = "Anna annA") == True
    assert candidate(sentence = "Never odd or even") == False
    assert candidate(sentence = "Nurses run") == False
    assert candidate(sentence = "aaaaa aaaaa aaaaa") == True
    assert candidate(sentence = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A") == False
    assert candidate(sentence = "Zebra apple orchid night eagle") == False
    assert candidate(sentence = "repaid diaper") == True
    assert candidate(sentence = "Abc bcd def efg gfa") == False
    assert candidate(sentence = "Abc cba abc") == False
    assert candidate(sentence = "a a a a a a a a a a") == True
    assert candidate(sentence = "banana apple orange nice East West") == False
    assert candidate(sentence = "Python nohtyP") == True
    assert candidate(sentence = "Palindrome emordnilaP ndromePal") == False
    assert candidate(sentence = "a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a") == True
    assert candidate(sentence = "Cycle elc yc") == False
    assert candidate(sentence = "algorithm nom alg") == False
    assert candidate(sentence = "Anna annA annA") == False
    assert candidate(sentence = "Twisted tales weave intricate stories") == False
    assert candidate(sentence = "civic civic civic") == True
    assert candidate(sentence = "Rotor rotor") == False
    assert candidate(sentence = "Zoology yggdrasill lloisgoy zoo") == False
    assert candidate(sentence = "coding ngoding going on") == False
    assert candidate(sentence = "repaid repaid") == False
    assert candidate(sentence = "Data analytics sscientist teach harsh") == False
    assert candidate(sentence = "AB BA CA") == False
    assert candidate(sentence = "Mamad Madam Damda") == False
    assert candidate(sentence = "abacabadabacaba") == True
