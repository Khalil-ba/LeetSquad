def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "abcdef",ch = "f") == "fedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdef",ch = "f") == "fedcba": {e}')
    
    total += 1
    try:
        result = candidate(word = "madam",ch = "d") == "damam"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "madam",ch = "d") == "damam": {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefd",ch = "d") == "dcbaefd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefd",ch = "d") == "dcbaefd": {e}')
    
    total += 1
    try:
        result = candidate(word = "abcd",ch = "z") == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcd",ch = "z") == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(word = "a",ch = "a") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a",ch = "a") == "a": {e}')
    
    total += 1
    try:
        result = candidate(word = "python",ch = "y") == "ypthon"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "python",ch = "y") == "ypthon": {e}')
    
    total += 1
    try:
        result = candidate(word = "operation",ch = "p") == "poeration"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "operation",ch = "p") == "poeration": {e}')
    
    total += 1
    try:
        result = candidate(word = "xyxzxe",ch = "z") == "zxyxxe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyxzxe",ch = "z") == "zxyxxe": {e}')
    
    total += 1
    try:
        result = candidate(word = "segment",ch = "t") == "tnemges"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "segment",ch = "t") == "tnemges": {e}')
    
    total += 1
    try:
        result = candidate(word = "hello",ch = "l") == "lehlo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "hello",ch = "l") == "lehlo": {e}')
    
    total += 1
    try:
        result = candidate(word = "racecar",ch = "e") == "ecarcar"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "racecar",ch = "e") == "ecarcar": {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdef",ch = "g") == "abcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdef",ch = "g") == "abcdef": {e}')
    
    total += 1
    try:
        result = candidate(word = "example",ch = "m") == "maxeple"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "example",ch = "m") == "maxeple": {e}')
    
    total += 1
    try:
        result = candidate(word = "reverse",ch = "r") == "reverse"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "reverse",ch = "r") == "reverse": {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdef",ch = "a") == "abcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdef",ch = "a") == "abcdef": {e}')
    
    total += 1
    try:
        result = candidate(word = "supercalifragilisticexpialidocious",ch = "x") == "xecitsiligarfilacrepuspialidocious"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "supercalifragilisticexpialidocious",ch = "x") == "xecitsiligarfilacrepuspialidocious": {e}')
    
    total += 1
    try:
        result = candidate(word = "abracadabra",ch = "r") == "rbaacadabra"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abracadabra",ch = "r") == "rbaacadabra": {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxwvutsrqponmlkjihgfedcba",ch = "a") == "abcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxwvutsrqponmlkjihgfedcba",ch = "a") == "abcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(word = "",ch = "a") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "",ch = "a") == "": {e}')
    
    total += 1
    try:
        result = candidate(word = "unbelievable",ch = "e") == "ebnulievable"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "unbelievable",ch = "e") == "ebnulievable": {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyz",ch = "m") == "mlkjihgfedcbanopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyz",ch = "m") == "mlkjihgfedcbanopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(word = "supercalifragilisticexpialidocious",ch = "c") == "crepusalifragilisticexpialidocious"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "supercalifragilisticexpialidocious",ch = "c") == "crepusalifragilisticexpialidocious": {e}')
    
    total += 1
    try:
        result = candidate(word = "interview",ch = "w") == "weivretni"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "interview",ch = "w") == "weivretni": {e}')
    
    total += 1
    try:
        result = candidate(word = "unpredictable",ch = "d") == "derpnuictable"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "unpredictable",ch = "d") == "derpnuictable": {e}')
    
    total += 1
    try:
        result = candidate(word = "beautifulization",ch = "z") == "zilufituaebation"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "beautifulization",ch = "z") == "zilufituaebation": {e}')
    
    total += 1
    try:
        result = candidate(word = "characterization",ch = "c") == "characterization"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "characterization",ch = "c") == "characterization": {e}')
    
    total += 1
    try:
        result = candidate(word = "communication",ch = "m") == "mocmunication"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "communication",ch = "m") == "mocmunication": {e}')
    
    total += 1
    try:
        result = candidate(word = "reversethispart",ch = "e") == "erversethispart"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "reversethispart",ch = "e") == "erversethispart": {e}')
    
    total += 1
    try:
        result = candidate(word = "reinforce",ch = "e") == "erinforce"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "reinforce",ch = "e") == "erinforce": {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxwvutsrqponmlkjihgfedcba",ch = "q") == "qrstuvwxyzponmlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxwvutsrqponmlkjihgfedcba",ch = "q") == "qrstuvwxyzponmlkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(word = "unbelievable",ch = "l") == "lebnuievable"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "unbelievable",ch = "l") == "lebnuievable": {e}')
    
    total += 1
    try:
        result = candidate(word = "nothingtoreverse",ch = "x") == "nothingtoreverse"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "nothingtoreverse",ch = "x") == "nothingtoreverse": {e}')
    
    total += 1
    try:
        result = candidate(word = "characterization",ch = "a") == "ahcracterization"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "characterization",ch = "a") == "ahcracterization": {e}')
    
    total += 1
    try:
        result = candidate(word = "quickbrownfox",ch = "o") == "orbkciuqwnfox"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "quickbrownfox",ch = "o") == "orbkciuqwnfox": {e}')
    
    total += 1
    try:
        result = candidate(word = "banana",ch = "n") == "nabana"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "banana",ch = "n") == "nabana": {e}')
    
    total += 1
    try:
        result = candidate(word = "qwertyuiop",ch = "p") == "poiuytrewq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwertyuiop",ch = "p") == "poiuytrewq": {e}')
    
    total += 1
    try:
        result = candidate(word = "qwertyuiop",ch = "q") == "qwertyuiop"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwertyuiop",ch = "q") == "qwertyuiop": {e}')
    
    total += 1
    try:
        result = candidate(word = "boundary",ch = "d") == "dnuobary"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "boundary",ch = "d") == "dnuobary": {e}')
    
    total += 1
    try:
        result = candidate(word = "continuous",ch = "s") == "suounitnoc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "continuous",ch = "s") == "suounitnoc": {e}')
    
    total += 1
    try:
        result = candidate(word = "interoperability",ch = "i") == "interoperability"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "interoperability",ch = "i") == "interoperability": {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaa",ch = "a") == "aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaa",ch = "a") == "aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(word = "quizzically",ch = "q") == "quizzically"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "quizzically",ch = "q") == "quizzically": {e}')
    
    total += 1
    try:
        result = candidate(word = "congratulations",ch = "g") == "gnocratulations"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "congratulations",ch = "g") == "gnocratulations": {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeff",ch = "f") == "feeddccbbaaf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeff",ch = "f") == "feeddccbbaaf": {e}')
    
    total += 1
    try:
        result = candidate(word = "zyxwvutsrqponmlkjihgfedcba",ch = "m") == "mnopqrstuvwxyzlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zyxwvutsrqponmlkjihgfedcba",ch = "m") == "mnopqrstuvwxyzlkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(word = "concatenation",ch = "c") == "concatenation"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "concatenation",ch = "c") == "concatenation": {e}')
    
    total += 1
    try:
        result = candidate(word = "implementation",ch = "i") == "implementation"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "implementation",ch = "i") == "implementation": {e}')
    
    total += 1
    try:
        result = candidate(word = "establishment",ch = "b") == "batselishment"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "establishment",ch = "b") == "batselishment": {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijkllllllllllllllllllllllllllllllllllllllllllllllll",ch = "l") == "lkjihgfedcballlllllllllllllllllllllllllllllllllllllllllllll"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijkllllllllllllllllllllllllllllllllllllllllllllllll",ch = "l") == "lkjihgfedcballlllllllllllllllllllllllllllllllllllllllllllll": {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefg",ch = "g") == "gfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefg",ch = "g") == "gfedcba": {e}')
    
    total += 1
    try:
        result = candidate(word = "development",ch = "p") == "polevedment"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "development",ch = "p") == "polevedment": {e}')
    
    total += 1
    try:
        result = candidate(word = "unfortunately",ch = "r") == "rofnutunately"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "unfortunately",ch = "r") == "rofnutunately": {e}')
    
    total += 1
    try:
        result = candidate(word = "challenges",ch = "e") == "ellahcnges"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "challenges",ch = "e") == "ellahcnges": {e}')
    
    total += 1
    try:
        result = candidate(word = "thisisaverylongwordthatneedstoreversed",ch = "n") == "nolyrevasisihtgwordthatneedstoreversed"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "thisisaverylongwordthatneedstoreversed",ch = "n") == "nolyrevasisihtgwordthatneedstoreversed": {e}')
    
    total += 1
    try:
        result = candidate(word = "interview",ch = "e") == "etnirview"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "interview",ch = "e") == "etnirview": {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdeffedcba",ch = "f") == "fedcbafedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdeffedcba",ch = "f") == "fedcbafedcba": {e}')
    
    total += 1
    try:
        result = candidate(word = "classification",ch = "l") == "lcassification"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "classification",ch = "l") == "lcassification": {e}')
    
    total += 1
    try:
        result = candidate(word = "thisisateststring",ch = "t") == "thisisateststring"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "thisisateststring",ch = "t") == "thisisateststring": {e}')
    
    total += 1
    try:
        result = candidate(word = "mississippi",ch = "i") == "imssissippi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mississippi",ch = "i") == "imssissippi": {e}')
    
    total += 1
    try:
        result = candidate(word = "unbelievable",ch = "b") == "bnuelievable"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "unbelievable",ch = "b") == "bnuelievable": {e}')
    
    total += 1
    try:
        result = candidate(word = "mississippi",ch = "s") == "simsissippi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mississippi",ch = "s") == "simsissippi": {e}')
    
    total += 1
    try:
        result = candidate(word = "congratulations",ch = "l") == "lutargnocations"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "congratulations",ch = "l") == "lutargnocations": {e}')
    
    total += 1
    try:
        result = candidate(word = "synchronous",ch = "c") == "cnyshronous"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "synchronous",ch = "c") == "cnyshronous": {e}')
    
    total += 1
    try:
        result = candidate(word = "algorithm",ch = "l") == "lagorithm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "algorithm",ch = "l") == "lagorithm": {e}')
    
    total += 1
    try:
        result = candidate(word = "abracadabra",ch = "c") == "carbaadabra"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abracadabra",ch = "c") == "carbaadabra": {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzz",ch = "z") == "zzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzz",ch = "z") == "zzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(word = "development",ch = "l") == "levedopment"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "development",ch = "l") == "levedopment": {e}')
    
    total += 1
    try:
        result = candidate(word = "identification",ch = "i") == "identification"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "identification",ch = "i") == "identification": {e}')
    
    total += 1
    try:
        result = candidate(word = "beautiful",ch = "t") == "tuaebiful"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "beautiful",ch = "t") == "tuaebiful": {e}')
    
    total += 1
    try:
        result = candidate(word = "asdfghjklzxcvbnm",ch = "m") == "mnbvcxzlkjhgfdsa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "asdfghjklzxcvbnm",ch = "m") == "mnbvcxzlkjhgfdsa": {e}')
    
    total += 1
    try:
        result = candidate(word = "representation",ch = "r") == "representation"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "representation",ch = "r") == "representation": {e}')
    
    total += 1
    try:
        result = candidate(word = "congratulations",ch = "t") == "targnoculations"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "congratulations",ch = "t") == "targnoculations": {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",ch = "q") == "qppoonnmmllkkjjiihhggffeeddccbbaaqrrssttuuvvwwxxyyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",ch = "q") == "qppoonnmmllkkjjiihhggffeeddccbbaaqrrssttuuvvwwxxyyzz": {e}')
    
    total += 1
    try:
        result = candidate(word = "sequence",ch = "q") == "qesuence"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "sequence",ch = "q") == "qesuence": {e}')
    
    total += 1
    try:
        result = candidate(word = "environment",ch = "v") == "vneironment"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "environment",ch = "v") == "vneironment": {e}')
    
    total += 1
    try:
        result = candidate(word = "algorithm",ch = "g") == "glaorithm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "algorithm",ch = "g") == "glaorithm": {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",ch = "z") == "zyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaaz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",ch = "z") == "zyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaaz": {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyz",ch = "z") == "zyxwvutsrqponmlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyz",ch = "z") == "zyxwvutsrqponmlkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghij",ch = "e") == "edcbafghij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghij",ch = "e") == "edcbafghij": {e}')
    
    total += 1
    try:
        result = candidate(word = "solution",ch = "u") == "ulostion"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "solution",ch = "u") == "ulostion": {e}')
    
    total += 1
    try:
        result = candidate(word = "environment",ch = "n") == "nevironment"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "environment",ch = "n") == "nevironment": {e}')
    
    total += 1
    try:
        result = candidate(word = "environmentally",ch = "v") == "vneironmentally"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "environmentally",ch = "v") == "vneironmentally": {e}')
    
    total += 1
    try:
        result = candidate(word = "algorithm",ch = "o") == "oglarithm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "algorithm",ch = "o") == "oglarithm": {e}')
    
    total += 1
    try:
        result = candidate(word = "single",ch = "l") == "lgnise"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "single",ch = "l") == "lgnise": {e}')
    
    total += 1
    try:
        result = candidate(word = "supercalifragilisticexpialidocious",ch = "f") == "filacrepusragilisticexpialidocious"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "supercalifragilisticexpialidocious",ch = "f") == "filacrepusragilisticexpialidocious": {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefg",ch = "z") == "abcdefg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefg",ch = "z") == "abcdefg": {e}')
    
    total += 1
    try:
        result = candidate(word = "double",ch = "x") == "double"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "double",ch = "x") == "double": {e}')
    
    total += 1
    try:
        result = candidate(word = "algorithms",ch = "a") == "algorithms"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "algorithms",ch = "a") == "algorithms": {e}')
    
    total += 1
    try:
        result = candidate(word = "algorithm",ch = "r") == "roglaithm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "algorithm",ch = "r") == "roglaithm": {e}')
    
    total += 1
    try:
        result = candidate(word = "characterization",ch = "h") == "hcaracterization"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "characterization",ch = "h") == "hcaracterization": {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzzyx",ch = "z") == "zyxzyx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzzyx",ch = "z") == "zyxzyx": {e}')
    
    total += 1
    try:
        result = candidate(word = "subsequence",ch = "q") == "qesbusuence"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "subsequence",ch = "q") == "qesbusuence": {e}')
    
    total += 1
    try:
        result = candidate(word = "reversal",ch = "a") == "asreverl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "reversal",ch = "a") == "asreverl": {e}')
    
    total += 1
    try:
        result = candidate(word = "a",ch = "b") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a",ch = "b") == "a": {e}')
    
    total += 1
    try:
        result = candidate(word = "visualization",ch = "i") == "ivsualization"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "visualization",ch = "i") == "ivsualization": {e}')
    
    total += 1
    try:
        result = candidate(word = "incomprehensible",ch = "h") == "herpmocniensible"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "incomprehensible",ch = "h") == "herpmocniensible": {e}')
    
    total += 1
    try:
        result = candidate(word = "hellothere",ch = "e") == "ehllothere"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "hellothere",ch = "e") == "ehllothere": {e}')
    
    total += 1
    try:
        result = candidate(word = "reverseprefix",ch = "r") == "reverseprefix"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "reverseprefix",ch = "r") == "reverseprefix": {e}')
    
    total += 1
    try:
        result = candidate(word = "pneumonoultramicroscopicsilicovolcanoconiosis",ch = "o") == "omuenpnoultramicroscopicsilicovolcanoconiosis"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pneumonoultramicroscopicsilicovolcanoconiosis",ch = "o") == "omuenpnoultramicroscopicsilicovolcanoconiosis": {e}')
    
    total += 1
    try:
        result = candidate(word = "uniquecharacters",ch = "u") == "uniquecharacters"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uniquecharacters",ch = "u") == "uniquecharacters": {e}')
    
    total += 1
    try:
        result = candidate(word = "alphabetization",ch = "b") == "bahplaetization"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "alphabetization",ch = "b") == "bahplaetization": {e}')
    
    total += 1
    try:
        result = candidate(word = "standardization",ch = "i") == "idradnatszation"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "standardization",ch = "i") == "idradnatszation": {e}')
    
    total += 1
    try:
        result = candidate(word = "automation",ch = "o") == "otuamation"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "automation",ch = "o") == "otuamation": {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqr",ch = "r") == "rqponm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqr",ch = "r") == "rqponm": {e}')
    
    total += 1
    try:
        result = candidate(word = "pronunciation",ch = "u") == "unorpnciation"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pronunciation",ch = "u") == "unorpnciation": {e}')
    
    total += 1
    try:
        result = candidate(word = "abacaxa",ch = "a") == "abacaxa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abacaxa",ch = "a") == "abacaxa": {e}')
    
    total += 1
    try:
        result = candidate(word = "reversal",ch = "r") == "reversal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "reversal",ch = "r") == "reversal": {e}')
    
    total += 1
    try:
        result = candidate(word = "congratulations",ch = "u") == "utargnoclations"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "congratulations",ch = "u") == "utargnoclations": {e}')
    
    total += 1
    try:
        result = candidate(word = "performance",ch = "f") == "frepormance"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "performance",ch = "f") == "frepormance": {e}')
    
    total += 1
    try:
        result = candidate(word = "nevertheless",ch = "n") == "nevertheless"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "nevertheless",ch = "n") == "nevertheless": {e}')
    
    total += 1
    try:
        result = candidate(word = "multifaceted",ch = "f") == "fitlumaceted"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "multifaceted",ch = "f") == "fitlumaceted": {e}')
    
    total += 1
    try:
        result = candidate(word = "reversal",ch = "v") == "verersal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "reversal",ch = "v") == "verersal": {e}')
    
    total += 1
    try:
        result = candidate(word = "thisisaverylongwordthatshouldtestthelimitsofthefunction",ch = "t") == "thisisaverylongwordthatshouldtestthelimitsofthefunction"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "thisisaverylongwordthatshouldtestthelimitsofthefunction",ch = "t") == "thisisaverylongwordthatshouldtestthelimitsofthefunction": {e}')
    
    total += 1
    try:
        result = candidate(word = "sophistication",ch = "s") == "sophistication"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "sophistication",ch = "s") == "sophistication": {e}')
    
    total += 1
    try:
        result = candidate(word = "xylophone",ch = "o") == "olyxphone"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xylophone",ch = "o") == "olyxphone": {e}')
    
    total += 1
    try:
        result = candidate(word = "visualization",ch = "z") == "zilausivation"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "visualization",ch = "z") == "zilausivation": {e}')
    
    total += 1
    try:
        result = candidate(word = "pneumonoultramicroscopicsilicovolcanoconiosis",ch = "u") == "uenpmonoultramicroscopicsilicovolcanoconiosis"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pneumonoultramicroscopicsilicovolcanoconiosis",ch = "u") == "uenpmonoultramicroscopicsilicovolcanoconiosis": {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzxyzxyz",ch = "x") == "xyzxyzxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzxyzxyz",ch = "x") == "xyzxyzxyz": {e}')
    
    total += 1
    try:
        result = candidate(word = "challenge",ch = "e") == "ellahcnge"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "challenge",ch = "e") == "ellahcnge": {e}')
    
    total += 1
    try:
        result = candidate(word = "perseverance",ch = "v") == "vesreperance"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "perseverance",ch = "v") == "vesreperance": {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijk",ch = "i") == "ihgfedcbajk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijk",ch = "i") == "ihgfedcbajk": {e}')
    
    total += 1
    try:
        result = candidate(word = "mississippi",ch = "p") == "pississimpi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mississippi",ch = "p") == "pississimpi": {e}')
    
    total += 1
    try:
        result = candidate(word = "programming",ch = "g") == "gorpramming"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "programming",ch = "g") == "gorpramming": {e}')
    
    total += 1
    try:
        result = candidate(word = "responsibilities",ch = "s") == "serponsibilities"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "responsibilities",ch = "s") == "serponsibilities": {e}')
    
    total += 1
    try:
        result = candidate(word = "synchronization",ch = "n") == "nyschronization"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "synchronization",ch = "n") == "nyschronization": {e}')
    
    total += 1
    try:
        result = candidate(word = "floccinaucinihilipilification",ch = "f") == "floccinaucinihilipilification"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "floccinaucinihilipilification",ch = "f") == "floccinaucinihilipilification": {e}')
    
    total += 1
    try:
        result = candidate(word = "operationalization",ch = "o") == "operationalization"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "operationalization",ch = "o") == "operationalization": {e}')
    
    total += 1
    try:
        result = candidate(word = "specializations",ch = "a") == "aicepslizations"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "specializations",ch = "a") == "aicepslizations": {e}')
    
    total += 1
    try:
        result = candidate(word = "optimization",ch = "t") == "tpoimization"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "optimization",ch = "t") == "tpoimization": {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijk",ch = "h") == "hgfedcbaijk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijk",ch = "h") == "hgfedcbaijk": {e}')
    
    total += 1
    try:
        result = candidate(word = "xylophone",ch = "p") == "polyxhone"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xylophone",ch = "p") == "polyxhone": {e}')
    
    total += 1
    try:
        result = candidate(word = "hellohellohello",ch = "l") == "lehlohellohello"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "hellohellohello",ch = "l") == "lehlohellohello": {e}')
    
    total += 1
    try:
        result = candidate(word = "concatenation",ch = "n") == "noccatenation"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "concatenation",ch = "n") == "noccatenation": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "abcdef",ch = "f") == "fedcba"
    assert candidate(word = "madam",ch = "d") == "damam"
    assert candidate(word = "abcdefd",ch = "d") == "dcbaefd"
    assert candidate(word = "abcd",ch = "z") == "abcd"
    assert candidate(word = "a",ch = "a") == "a"
    assert candidate(word = "python",ch = "y") == "ypthon"
    assert candidate(word = "operation",ch = "p") == "poeration"
    assert candidate(word = "xyxzxe",ch = "z") == "zxyxxe"
    assert candidate(word = "segment",ch = "t") == "tnemges"
    assert candidate(word = "hello",ch = "l") == "lehlo"
    assert candidate(word = "racecar",ch = "e") == "ecarcar"
    assert candidate(word = "abcdef",ch = "g") == "abcdef"
    assert candidate(word = "example",ch = "m") == "maxeple"
    assert candidate(word = "reverse",ch = "r") == "reverse"
    assert candidate(word = "abcdef",ch = "a") == "abcdef"
    assert candidate(word = "supercalifragilisticexpialidocious",ch = "x") == "xecitsiligarfilacrepuspialidocious"
    assert candidate(word = "abracadabra",ch = "r") == "rbaacadabra"
    assert candidate(word = "zyxwvutsrqponmlkjihgfedcba",ch = "a") == "abcdefghijklmnopqrstuvwxyz"
    assert candidate(word = "",ch = "a") == ""
    assert candidate(word = "unbelievable",ch = "e") == "ebnulievable"
    assert candidate(word = "abcdefghijklmnopqrstuvwxyz",ch = "m") == "mlkjihgfedcbanopqrstuvwxyz"
    assert candidate(word = "supercalifragilisticexpialidocious",ch = "c") == "crepusalifragilisticexpialidocious"
    assert candidate(word = "interview",ch = "w") == "weivretni"
    assert candidate(word = "unpredictable",ch = "d") == "derpnuictable"
    assert candidate(word = "beautifulization",ch = "z") == "zilufituaebation"
    assert candidate(word = "characterization",ch = "c") == "characterization"
    assert candidate(word = "communication",ch = "m") == "mocmunication"
    assert candidate(word = "reversethispart",ch = "e") == "erversethispart"
    assert candidate(word = "reinforce",ch = "e") == "erinforce"
    assert candidate(word = "zyxwvutsrqponmlkjihgfedcba",ch = "q") == "qrstuvwxyzponmlkjihgfedcba"
    assert candidate(word = "unbelievable",ch = "l") == "lebnuievable"
    assert candidate(word = "nothingtoreverse",ch = "x") == "nothingtoreverse"
    assert candidate(word = "characterization",ch = "a") == "ahcracterization"
    assert candidate(word = "quickbrownfox",ch = "o") == "orbkciuqwnfox"
    assert candidate(word = "banana",ch = "n") == "nabana"
    assert candidate(word = "qwertyuiop",ch = "p") == "poiuytrewq"
    assert candidate(word = "qwertyuiop",ch = "q") == "qwertyuiop"
    assert candidate(word = "boundary",ch = "d") == "dnuobary"
    assert candidate(word = "continuous",ch = "s") == "suounitnoc"
    assert candidate(word = "interoperability",ch = "i") == "interoperability"
    assert candidate(word = "aaaaaa",ch = "a") == "aaaaaa"
    assert candidate(word = "quizzically",ch = "q") == "quizzically"
    assert candidate(word = "congratulations",ch = "g") == "gnocratulations"
    assert candidate(word = "aabbccddeeff",ch = "f") == "feeddccbbaaf"
    assert candidate(word = "zyxwvutsrqponmlkjihgfedcba",ch = "m") == "mnopqrstuvwxyzlkjihgfedcba"
    assert candidate(word = "concatenation",ch = "c") == "concatenation"
    assert candidate(word = "implementation",ch = "i") == "implementation"
    assert candidate(word = "establishment",ch = "b") == "batselishment"
    assert candidate(word = "abcdefghijkllllllllllllllllllllllllllllllllllllllllllllllll",ch = "l") == "lkjihgfedcballlllllllllllllllllllllllllllllllllllllllllllll"
    assert candidate(word = "abcdefg",ch = "g") == "gfedcba"
    assert candidate(word = "development",ch = "p") == "polevedment"
    assert candidate(word = "unfortunately",ch = "r") == "rofnutunately"
    assert candidate(word = "challenges",ch = "e") == "ellahcnges"
    assert candidate(word = "thisisaverylongwordthatneedstoreversed",ch = "n") == "nolyrevasisihtgwordthatneedstoreversed"
    assert candidate(word = "interview",ch = "e") == "etnirview"
    assert candidate(word = "abcdeffedcba",ch = "f") == "fedcbafedcba"
    assert candidate(word = "classification",ch = "l") == "lcassification"
    assert candidate(word = "thisisateststring",ch = "t") == "thisisateststring"
    assert candidate(word = "mississippi",ch = "i") == "imssissippi"
    assert candidate(word = "unbelievable",ch = "b") == "bnuelievable"
    assert candidate(word = "mississippi",ch = "s") == "simsissippi"
    assert candidate(word = "congratulations",ch = "l") == "lutargnocations"
    assert candidate(word = "synchronous",ch = "c") == "cnyshronous"
    assert candidate(word = "algorithm",ch = "l") == "lagorithm"
    assert candidate(word = "abracadabra",ch = "c") == "carbaadabra"
    assert candidate(word = "zzzzzzzzzzzzzzzz",ch = "z") == "zzzzzzzzzzzzzzzz"
    assert candidate(word = "development",ch = "l") == "levedopment"
    assert candidate(word = "identification",ch = "i") == "identification"
    assert candidate(word = "beautiful",ch = "t") == "tuaebiful"
    assert candidate(word = "asdfghjklzxcvbnm",ch = "m") == "mnbvcxzlkjhgfdsa"
    assert candidate(word = "representation",ch = "r") == "representation"
    assert candidate(word = "congratulations",ch = "t") == "targnoculations"
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",ch = "q") == "qppoonnmmllkkjjiihhggffeeddccbbaaqrrssttuuvvwwxxyyzz"
    assert candidate(word = "sequence",ch = "q") == "qesuence"
    assert candidate(word = "environment",ch = "v") == "vneironment"
    assert candidate(word = "algorithm",ch = "g") == "glaorithm"
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",ch = "z") == "zyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaaz"
    assert candidate(word = "abcdefghijklmnopqrstuvwxyz",ch = "z") == "zyxwvutsrqponmlkjihgfedcba"
    assert candidate(word = "abcdefghij",ch = "e") == "edcbafghij"
    assert candidate(word = "solution",ch = "u") == "ulostion"
    assert candidate(word = "environment",ch = "n") == "nevironment"
    assert candidate(word = "environmentally",ch = "v") == "vneironmentally"
    assert candidate(word = "algorithm",ch = "o") == "oglarithm"
    assert candidate(word = "single",ch = "l") == "lgnise"
    assert candidate(word = "supercalifragilisticexpialidocious",ch = "f") == "filacrepusragilisticexpialidocious"
    assert candidate(word = "abcdefg",ch = "z") == "abcdefg"
    assert candidate(word = "double",ch = "x") == "double"
    assert candidate(word = "algorithms",ch = "a") == "algorithms"
    assert candidate(word = "algorithm",ch = "r") == "roglaithm"
    assert candidate(word = "characterization",ch = "h") == "hcaracterization"
    assert candidate(word = "xyzzyx",ch = "z") == "zyxzyx"
    assert candidate(word = "subsequence",ch = "q") == "qesbusuence"
    assert candidate(word = "reversal",ch = "a") == "asreverl"
    assert candidate(word = "a",ch = "b") == "a"
    assert candidate(word = "visualization",ch = "i") == "ivsualization"
    assert candidate(word = "incomprehensible",ch = "h") == "herpmocniensible"
    assert candidate(word = "hellothere",ch = "e") == "ehllothere"
    assert candidate(word = "reverseprefix",ch = "r") == "reverseprefix"
    assert candidate(word = "pneumonoultramicroscopicsilicovolcanoconiosis",ch = "o") == "omuenpnoultramicroscopicsilicovolcanoconiosis"
    assert candidate(word = "uniquecharacters",ch = "u") == "uniquecharacters"
    assert candidate(word = "alphabetization",ch = "b") == "bahplaetization"
    assert candidate(word = "standardization",ch = "i") == "idradnatszation"
    assert candidate(word = "automation",ch = "o") == "otuamation"
    assert candidate(word = "mnopqr",ch = "r") == "rqponm"
    assert candidate(word = "pronunciation",ch = "u") == "unorpnciation"
    assert candidate(word = "abacaxa",ch = "a") == "abacaxa"
    assert candidate(word = "reversal",ch = "r") == "reversal"
    assert candidate(word = "congratulations",ch = "u") == "utargnoclations"
    assert candidate(word = "performance",ch = "f") == "frepormance"
    assert candidate(word = "nevertheless",ch = "n") == "nevertheless"
    assert candidate(word = "multifaceted",ch = "f") == "fitlumaceted"
    assert candidate(word = "reversal",ch = "v") == "verersal"
    assert candidate(word = "thisisaverylongwordthatshouldtestthelimitsofthefunction",ch = "t") == "thisisaverylongwordthatshouldtestthelimitsofthefunction"
    assert candidate(word = "sophistication",ch = "s") == "sophistication"
    assert candidate(word = "xylophone",ch = "o") == "olyxphone"
    assert candidate(word = "visualization",ch = "z") == "zilausivation"
    assert candidate(word = "pneumonoultramicroscopicsilicovolcanoconiosis",ch = "u") == "uenpmonoultramicroscopicsilicovolcanoconiosis"
    assert candidate(word = "xyzxyzxyz",ch = "x") == "xyzxyzxyz"
    assert candidate(word = "challenge",ch = "e") == "ellahcnge"
    assert candidate(word = "perseverance",ch = "v") == "vesreperance"
    assert candidate(word = "abcdefghijk",ch = "i") == "ihgfedcbajk"
    assert candidate(word = "mississippi",ch = "p") == "pississimpi"
    assert candidate(word = "programming",ch = "g") == "gorpramming"
    assert candidate(word = "responsibilities",ch = "s") == "serponsibilities"
    assert candidate(word = "synchronization",ch = "n") == "nyschronization"
    assert candidate(word = "floccinaucinihilipilification",ch = "f") == "floccinaucinihilipilification"
    assert candidate(word = "operationalization",ch = "o") == "operationalization"
    assert candidate(word = "specializations",ch = "a") == "aicepslizations"
    assert candidate(word = "optimization",ch = "t") == "tpoimization"
    assert candidate(word = "abcdefghijk",ch = "h") == "hgfedcbaijk"
    assert candidate(word = "xylophone",ch = "p") == "polyxhone"
    assert candidate(word = "hellohellohello",ch = "l") == "lehlohellohello"
    assert candidate(word = "concatenation",ch = "n") == "noccatenation"


