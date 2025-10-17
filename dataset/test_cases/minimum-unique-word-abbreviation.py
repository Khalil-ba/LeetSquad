def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(target = "internationalization",dictionary = ['international', 'intermittent', 'interact']) == "20"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "internationalization",dictionary = ['international', 'intermittent', 'interact']) == "20": {e}')
    
    total += 1
    try:
        result = candidate(target = "apple",dictionary = ['blade', 'plain', 'amber']) == "3l1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "apple",dictionary = ['blade', 'plain', 'amber']) == "3l1": {e}')
    
    total += 1
    try:
        result = candidate(target = "cat",dictionary = ['dog', 'dot']) == "c2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "cat",dictionary = ['dog', 'dot']) == "c2": {e}')
    
    total += 1
    try:
        result = candidate(target = "internationalization",dictionary = ['international', 'interstate', 'interpersonal']) == "20"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "internationalization",dictionary = ['international', 'interstate', 'interpersonal']) == "20": {e}')
    
    total += 1
    try:
        result = candidate(target = "internationalization",dictionary = ['inter', 'national', 'ization']) == "20"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "internationalization",dictionary = ['inter', 'national', 'ization']) == "20": {e}')
    
    total += 1
    try:
        result = candidate(target = "a",dictionary = ['b']) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "a",dictionary = ['b']) == "a": {e}')
    
    total += 1
    try:
        result = candidate(target = "apple",dictionary = ['blade']) == "a4"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "apple",dictionary = ['blade']) == "a4": {e}')
    
    total += 1
    try:
        result = candidate(target = "test",dictionary = ['tent', 'sett', 'text']) == "2s1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "test",dictionary = ['tent', 'sett', 'text']) == "2s1": {e}')
    
    total += 1
    try:
        result = candidate(target = "abcd",dictionary = ['abcde', 'abfde', 'abgde']) == "4"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "abcd",dictionary = ['abcde', 'abfde', 'abgde']) == "4": {e}')
    
    total += 1
    try:
        result = candidate(target = "a",dictionary = []) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "a",dictionary = []) == "1": {e}')
    
    total += 1
    try:
        result = candidate(target = "a",dictionary = ['b', 'c', 'd']) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "a",dictionary = ['b', 'c', 'd']) == "a": {e}')
    
    total += 1
    try:
        result = candidate(target = "congratulations",dictionary = ['congratulate', 'congregate', 'congruity', 'congruity', 'congruity']) == "15"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "congratulations",dictionary = ['congratulate', 'congregate', 'congruity', 'congruity', 'congruity']) == "15": {e}')
    
    total += 1
    try:
        result = candidate(target = "pneumonoultramicroscopicsilicovolcanoconiosis",dictionary = ['pneumo', 'ultra', 'microscopic', 'silico', 'volcano', 'coniosis', 'supercalifragilisticexpialidocious']) == "45"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "pneumonoultramicroscopicsilicovolcanoconiosis",dictionary = ['pneumo', 'ultra', 'microscopic', 'silico', 'volcano', 'coniosis', 'supercalifragilisticexpialidocious']) == "45": {e}')
    
    total += 1
    try:
        result = candidate(target = "quantification",dictionary = ['quantific', 'quantificat', 'quantificatio', 'quantificati', 'quantificati', 'quantificati', 'quantificati', 'quantificati', 'quantificati', 'quantificati']) == "14"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "quantification",dictionary = ['quantific', 'quantificat', 'quantificatio', 'quantificati', 'quantificati', 'quantificati', 'quantificati', 'quantificati', 'quantificati', 'quantificati']) == "14": {e}')
    
    total += 1
    try:
        result = candidate(target = "unbelievable",dictionary = ['unbeleviable', 'unelevable', 'unbelieveable', 'unbelivable', 'unbelievablee']) == "7v4"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "unbelievable",dictionary = ['unbeleviable', 'unelevable', 'unbelieveable', 'unbelivable', 'unbelievablee']) == "7v4": {e}')
    
    total += 1
    try:
        result = candidate(target = "antidisestablishmentarianism",dictionary = ['antisemitism', 'establishment', 'disestablishment', 'disestablishmentarianism', 'antidisestablishmentarian']) == "28"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "antidisestablishmentarianism",dictionary = ['antisemitism', 'establishment', 'disestablishment', 'disestablishmentarianism', 'antidisestablishmentarian']) == "28": {e}')
    
    total += 1
    try:
        result = candidate(target = "characterization",dictionary = ['character', 'characteristic', 'charisma', 'charitable']) == "16"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "characterization",dictionary = ['character', 'characteristic', 'charisma', 'charitable']) == "16": {e}')
    
    total += 1
    try:
        result = candidate(target = "environmental",dictionary = ['environment', 'environments', 'environmentalist', 'environmentalists', 'environmentally']) == "13"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "environmental",dictionary = ['environment', 'environments', 'environmentalist', 'environmentalists', 'environmentally']) == "13": {e}')
    
    total += 1
    try:
        result = candidate(target = "incomprehensibilities",dictionary = ['incomprehensible', 'incomprehension', 'incomprehensibly', 'incomprehensiveness']) == "21"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "incomprehensibilities",dictionary = ['incomprehensible', 'incomprehension', 'incomprehensibly', 'incomprehensiveness']) == "21": {e}')
    
    total += 1
    try:
        result = candidate(target = "abcdefghijklmnopqrstuvwxyz",dictionary = ['abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqr', 'abcdefghijklmnopq', 'abcdefghijklmnop', 'abcdefghijklmno', 'abcdefghijk', 'abcdefghij', 'abcdefghi', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']) == "26"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "abcdefghijklmnopqrstuvwxyz",dictionary = ['abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqr', 'abcdefghijklmnopq', 'abcdefghijklmnop', 'abcdefghijklmno', 'abcdefghijk', 'abcdefghij', 'abcdefghi', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']) == "26": {e}')
    
    total += 1
    try:
        result = candidate(target = "methodology",dictionary = ['method', 'methodical', 'methodically', 'methodologies', 'methodological', 'methodologist']) == "11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "methodology",dictionary = ['method', 'methodical', 'methodically', 'methodologies', 'methodological', 'methodologist']) == "11": {e}')
    
    total += 1
    try:
        result = candidate(target = "abcdefghij",dictionary = ['abcdefghi', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'bcdefghij', 'cdefghij', 'defghij', 'efghij', 'fghij', 'ghij', 'hij', 'ij', 'j']) == "10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "abcdefghij",dictionary = ['abcdefghi', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'bcdefghij', 'cdefghij', 'defghij', 'efghij', 'fghij', 'ghij', 'hij', 'ij', 'j']) == "10": {e}')
    
    total += 1
    try:
        result = candidate(target = "optimization",dictionary = ['optimizationg', 'optimizat', 'optimiza', 'optimiz', 'optimize', 'optimi', 'optim', 'opti', 'opt', 'op', 'o', 'optimizationnn']) == "12"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "optimization",dictionary = ['optimizationg', 'optimizat', 'optimiza', 'optimiz', 'optimize', 'optimi', 'optim', 'opti', 'opt', 'op', 'o', 'optimizationnn']) == "12": {e}')
    
    total += 1
    try:
        result = candidate(target = "unfortunately",dictionary = ['unsurprisingly', 'unofficially', 'unaccountably', 'underrepresented']) == "10e2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "unfortunately",dictionary = ['unsurprisingly', 'unofficially', 'unaccountably', 'underrepresented']) == "10e2": {e}')
    
    total += 1
    try:
        result = candidate(target = "honorificabilitudinitatibus",dictionary = ['honorificabilitudinitatib', 'honorificabilitudinitati', 'honorificabilitudinit', 'honorificabilitudini']) == "27"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "honorificabilitudinitatibus",dictionary = ['honorificabilitudinitatib', 'honorificabilitudinitati', 'honorificabilitudinit', 'honorificabilitudini']) == "27": {e}')
    
    total += 1
    try:
        result = candidate(target = "microprocessors",dictionary = ['microscopic', 'microphones', 'microorganisms']) == "15"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "microprocessors",dictionary = ['microscopic', 'microphones', 'microorganisms']) == "15": {e}')
    
    total += 1
    try:
        result = candidate(target = "supercalifragilisticexpialidocious",dictionary = ['supercalifragilistic', 'supercalifragilisticexp', 'superfragilisticexpialidocious']) == "34"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "supercalifragilisticexpialidocious",dictionary = ['supercalifragilistic', 'supercalifragilisticexp', 'superfragilisticexpialidocious']) == "34": {e}')
    
    total += 1
    try:
        result = candidate(target = "antidisestablishmentarianism",dictionary = ['antidisestablishmentarianisms', 'antidisestablishmentarian', 'antidisestablishmentaria', 'antidisestablishmentari', 'antidisestablishmentar']) == "28"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "antidisestablishmentarianism",dictionary = ['antidisestablishmentarianisms', 'antidisestablishmentarian', 'antidisestablishmentaria', 'antidisestablishmentari', 'antidisestablishmentar']) == "28": {e}')
    
    total += 1
    try:
        result = candidate(target = "onomatopoeia",dictionary = ['onomatopoetic', 'onomatopoeic', 'onomatopoet', 'onomatopoeias', 'onomatopoe']) == "11a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "onomatopoeia",dictionary = ['onomatopoetic', 'onomatopoeic', 'onomatopoet', 'onomatopoeias', 'onomatopoe']) == "11a": {e}')
    
    total += 1
    try:
        result = candidate(target = "unbelievable",dictionary = ['incredible', 'unbeliever', 'unbelief', 'believable', 'unbelieveable']) == "12"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "unbelievable",dictionary = ['incredible', 'unbeliever', 'unbelief', 'believable', 'unbelieveable']) == "12": {e}')
    
    total += 1
    try:
        result = candidate(target = "communication",dictionary = ['communicate', 'communicator', 'communicative', 'communications', 'communicates']) == "12n"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "communication",dictionary = ['communicate', 'communicator', 'communicative', 'communications', 'communicates']) == "12n": {e}')
    
    total += 1
    try:
        result = candidate(target = "electroencephalography",dictionary = ['electro', 'encephalogram', 'graphy', 'electronic']) == "22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "electroencephalography",dictionary = ['electro', 'encephalogram', 'graphy', 'electronic']) == "22": {e}')
    
    total += 1
    try:
        result = candidate(target = "supercalifragilisticexpialidocious",dictionary = ['supercalifragilistic', 'califragilisticexpialidocious', 'superfragilistic', 'califragilistic', 'fragilisticexpialidocious']) == "34"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "supercalifragilisticexpialidocious",dictionary = ['supercalifragilistic', 'califragilisticexpialidocious', 'superfragilistic', 'califragilistic', 'fragilisticexpialidocious']) == "34": {e}')
    
    total += 1
    try:
        result = candidate(target = "universality",dictionary = ['universe', 'universals', 'universally', 'universal', 'universes']) == "12"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "universality",dictionary = ['universe', 'universals', 'universally', 'universal', 'universes']) == "12": {e}')
    
    total += 1
    try:
        result = candidate(target = "floccinaucinihilipilification",dictionary = ['floccinaucinihilipilific', 'floccinaucinihil', 'floccinauc', 'floccina', 'flocc']) == "29"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "floccinaucinihilipilification",dictionary = ['floccinaucinihilipilific', 'floccinaucinihil', 'floccinauc', 'floccina', 'flocc']) == "29": {e}')
    
    total += 1
    try:
        result = candidate(target = "mississippi",dictionary = ['missisippi', 'mississipi', 'missisippi', 'mississipi', 'mississipp', 'missisippi', 'mississipi', 'mississipp', 'mississippii', 'mississippii', 'mississippiii', 'mississippiiii', 'mississippiiiii', 'mississippiiiiii', 'mississippiiiiiii', 'mississippiiiiiiii', 'mississippiiiiiiiii', 'mississippiiiiiiiiii', 'mississippiiiiiiiiiii', 'mississippiiiiiiiiiiii']) == "11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "mississippi",dictionary = ['missisippi', 'mississipi', 'missisippi', 'mississipi', 'mississipp', 'missisippi', 'mississipi', 'mississipp', 'mississippii', 'mississippii', 'mississippiii', 'mississippiiii', 'mississippiiiii', 'mississippiiiiii', 'mississippiiiiiii', 'mississippiiiiiiii', 'mississippiiiiiiiii', 'mississippiiiiiiiiii', 'mississippiiiiiiiiiii', 'mississippiiiiiiiiiiii']) == "11": {e}')
    
    total += 1
    try:
        result = candidate(target = "algorithm",dictionary = ['algorith', 'algorithmm', 'algorithem', 'algorit', 'algori', 'algor', 'algo', 'alg', 'al', 'a', 'algorithmically']) == "9"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "algorithm",dictionary = ['algorith', 'algorithmm', 'algorithem', 'algorit', 'algori', 'algor', 'algo', 'alg', 'al', 'a', 'algorithmically']) == "9": {e}')
    
    total += 1
    try:
        result = candidate(target = "antidisestablishmentarianism",dictionary = ['antidisestablishmentarian', 'disestablishmentarianism', 'antidisestablishment', 'disestablishmentarian']) == "28"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "antidisestablishmentarianism",dictionary = ['antidisestablishmentarian', 'disestablishmentarianism', 'antidisestablishment', 'disestablishmentarian']) == "28": {e}')
    
    total += 1
    try:
        result = candidate(target = "counterdemonstration",dictionary = ['counter', 'demonstration', 'counterdemonstrate', 'counterdemonstrations', 'counterdemonstrat', 'counterdemonstrator']) == "20"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "counterdemonstration",dictionary = ['counter', 'demonstration', 'counterdemonstrate', 'counterdemonstrations', 'counterdemonstrat', 'counterdemonstrator']) == "20": {e}')
    
    total += 1
    try:
        result = candidate(target = "electroencephalograph",dictionary = ['electrocardiogram', 'electromyography', 'electrochemical', 'electroconductive']) == "21"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "electroencephalograph",dictionary = ['electrocardiogram', 'electromyography', 'electrochemical', 'electroconductive']) == "21": {e}')
    
    total += 1
    try:
        result = candidate(target = "abcdefghijklmnopqrstuvwxyz",dictionary = ['abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwyz', 'abcdefgh', 'mnopqrstuvwxyz']) == "26"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "abcdefghijklmnopqrstuvwxyz",dictionary = ['abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwyz', 'abcdefgh', 'mnopqrstuvwxyz']) == "26": {e}')
    
    total += 1
    try:
        result = candidate(target = "xxyyzz",dictionary = ['xxxyyy', 'xxyyy', 'xxzyy', 'xyyzz', 'xxyyz', 'xyzzz', 'xxzzz', 'xyzzy']) == "5z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "xxyyzz",dictionary = ['xxxyyy', 'xxyyy', 'xxzyy', 'xyyzz', 'xxyyz', 'xyzzz', 'xxzzz', 'xyzzy']) == "5z": {e}')
    
    total += 1
    try:
        result = candidate(target = "universality",dictionary = ['universal', 'universe', 'universalize', 'universally', 'universals']) == "11y"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "universality",dictionary = ['universal', 'universe', 'universalize', 'universally', 'universals']) == "11y": {e}')
    
    total += 1
    try:
        result = candidate(target = "algorithm",dictionary = ['algebra', 'algorithmic', 'alge', 'rithm', 'algo', 'rith', 'logarithm', 'algor', 'rithmo', 'algorith']) == "a8"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "algorithm",dictionary = ['algebra', 'algorithmic', 'alge', 'rithm', 'algo', 'rith', 'logarithm', 'algor', 'rithmo', 'algorith']) == "a8": {e}')
    
    total += 1
    try:
        result = candidate(target = "floccinaucinihilipilification",dictionary = ['floccinaucinihilipilifications', 'floccinaucinihilipilific', 'floccinaucinihilipilifics', 'floccinaucinihilipilificated']) == "29"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "floccinaucinihilipilification",dictionary = ['floccinaucinihilipilifications', 'floccinaucinihilipilific', 'floccinaucinihilipilifics', 'floccinaucinihilipilificated']) == "29": {e}')
    
    total += 1
    try:
        result = candidate(target = "development",dictionary = ['develop', 'developed', 'developing', 'developmental', 'developments', 'developer']) == "11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "development",dictionary = ['develop', 'developed', 'developing', 'developmental', 'developments', 'developer']) == "11": {e}')
    
    total += 1
    try:
        result = candidate(target = "supercalifragilisticexpialidocious",dictionary = ['supercalifragile', 'superduper', 'supercaliber', 'supercal']) == "34"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "supercalifragilisticexpialidocious",dictionary = ['supercalifragile', 'superduper', 'supercaliber', 'supercal']) == "34": {e}')
    
    total += 1
    try:
        result = candidate(target = "supercalifragilisticexpialidocious",dictionary = ['super', 'cali', 'fragilistic', 'expialidocious', 'supercalifragilisticexpialido']) == "34"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "supercalifragilisticexpialidocious",dictionary = ['super', 'cali', 'fragilistic', 'expialidocious', 'supercalifragilisticexpialido']) == "34": {e}')
    
    total += 1
    try:
        result = candidate(target = "floccinaucinihilipilification",dictionary = ['floccinaucinihilipilificat', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati']) == "29"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "floccinaucinihilipilification",dictionary = ['floccinaucinihilipilificat', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati']) == "29": {e}')
    
    total += 1
    try:
        result = candidate(target = "pneumonoultramicroscopicsilicovolcanoconiosis",dictionary = ['pneumonoultramicroscopic', 'silicovolcanoconiosis', 'ultramicroscopic', 'pneumonoconiosis']) == "45"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "pneumonoultramicroscopicsilicovolcanoconiosis",dictionary = ['pneumonoultramicroscopic', 'silicovolcanoconiosis', 'ultramicroscopic', 'pneumonoconiosis']) == "45": {e}')
    
    total += 1
    try:
        result = candidate(target = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",dictionary = ['aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz', 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzz', 'aabbcde', 'mnopqr', 'stuvwx', 'yz']) == "52"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",dictionary = ['aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz', 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzz', 'aabbcde', 'mnopqr', 'stuvwx', 'yz']) == "52": {e}')
    
    total += 1
    try:
        result = candidate(target = "electroencephalographically",dictionary = ['electroencephalograph', 'electroencephalographs', 'electroencephalographing', 'electroencephalography']) == "27"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "electroencephalographically",dictionary = ['electroencephalograph', 'electroencephalographs', 'electroencephalographing', 'electroencephalography']) == "27": {e}')
    
    total += 1
    try:
        result = candidate(target = "floccinaucinihilipilification",dictionary = ['floccinaucinihilipilifications', 'floccinaucinihilipilific', 'floccinaucinihilipilic', 'floccinaucinihilipi']) == "29"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "floccinaucinihilipilification",dictionary = ['floccinaucinihilipilifications', 'floccinaucinihilipilific', 'floccinaucinihilipilic', 'floccinaucinihilipi']) == "29": {e}')
    
    total += 1
    try:
        result = candidate(target = "individual",dictionary = ['individuality', 'individuals', 'individualism', 'individualist', 'individualistic']) == "10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "individual",dictionary = ['individuality', 'individuals', 'individualism', 'individualist', 'individualistic']) == "10": {e}')
    
    total += 1
    try:
        result = candidate(target = "floccinaucinihilipilification",dictionary = ['floccinaucinihilipilify', 'floccinaucinihilipilified', 'floccinaucinihilipilifies', 'floccinaucinihilipilifying']) == "29"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "floccinaucinihilipilification",dictionary = ['floccinaucinihilipilify', 'floccinaucinihilipilified', 'floccinaucinihilipilifies', 'floccinaucinihilipilifying']) == "29": {e}')
    
    total += 1
    try:
        result = candidate(target = "microprocessor",dictionary = ['micro', 'processor', 'microchip', 'microwave']) == "14"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "microprocessor",dictionary = ['micro', 'processor', 'microchip', 'microwave']) == "14": {e}')
    
    total += 1
    try:
        result = candidate(target = "pneumonoultramicroscopicsilicovolcanoconiosis",dictionary = ['pneumonoultramicroscopicsilicovolcanoconiosi', 'pneumonoultramicroscopicsilicovolcanoconio', 'pneumonoultramicroscopicsilicovolcanoconi', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon']) == "45"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "pneumonoultramicroscopicsilicovolcanoconiosis",dictionary = ['pneumonoultramicroscopicsilicovolcanoconiosi', 'pneumonoultramicroscopicsilicovolcanoconio', 'pneumonoultramicroscopicsilicovolcanoconi', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon']) == "45": {e}')
    
    total += 1
    try:
        result = candidate(target = "thyroparathyroidectomize",dictionary = ['thyroparathyroidectomy', 'thyroparathyroidectomying', 'thyroparathyroidectomized', 'thyroparathyroidectomizes']) == "24"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "thyroparathyroidectomize",dictionary = ['thyroparathyroidectomy', 'thyroparathyroidectomying', 'thyroparathyroidectomized', 'thyroparathyroidectomizes']) == "24": {e}')
    
    total += 1
    try:
        result = candidate(target = "floccinaucinihilipilification",dictionary = ['floccinaucinihilipilifications', 'floccinaucinihilipilific', 'floccinaucinihilipili', 'floccinaucinihilipi', 'floccinaucinihilip']) == "29"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "floccinaucinihilipilification",dictionary = ['floccinaucinihilipilifications', 'floccinaucinihilipilific', 'floccinaucinihilipili', 'floccinaucinihilipi', 'floccinaucinihilip']) == "29": {e}')
    
    total += 1
    try:
        result = candidate(target = "unquestionableness",dictionary = ['question', 'unquestionable', 'unquestionably', 'unquestionablenes']) == "18"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "unquestionableness",dictionary = ['question', 'unquestionable', 'unquestionably', 'unquestionablenes']) == "18": {e}')
    
    total += 1
    try:
        result = candidate(target = "acknowledgment",dictionary = ['acknowledge', 'acknowledged', 'acknowledges', 'acknowledging']) == "14"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "acknowledgment",dictionary = ['acknowledge', 'acknowledged', 'acknowledges', 'acknowledging']) == "14": {e}')
    
    total += 1
    try:
        result = candidate(target = "supercalifragilisticexpialidocious",dictionary = ['supercalifragilistic', 'califragilistic', 'expialidocious', 'supercal']) == "34"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "supercalifragilisticexpialidocious",dictionary = ['supercalifragilistic', 'califragilistic', 'expialidocious', 'supercal']) == "34": {e}')
    
    total += 1
    try:
        result = candidate(target = "environment",dictionary = ['envoy', 'enterprise', 'envelope', 'evaluate']) == "11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "environment",dictionary = ['envoy', 'enterprise', 'envelope', 'evaluate']) == "11": {e}')
    
    total += 1
    try:
        result = candidate(target = "programming",dictionary = ['program', 'programs', 'programmatic', 'programmer', 'programmed', 'programmers']) == "10g"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "programming",dictionary = ['program', 'programs', 'programmatic', 'programmer', 'programmed', 'programmers']) == "10g": {e}')
    
    total += 1
    try:
        result = candidate(target = "supercalifragilisticexpialidocious",dictionary = ['super', 'califragilistic', 'expialidocious', 'supercal', 'fragilistic', 'expi', 'alidocious', 'supercali', 'fragil', 'expiali', 'docious']) == "34"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "supercalifragilisticexpialidocious",dictionary = ['super', 'califragilistic', 'expialidocious', 'supercal', 'fragilistic', 'expi', 'alidocious', 'supercali', 'fragil', 'expiali', 'docious']) == "34": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(target = "internationalization",dictionary = ['international', 'intermittent', 'interact']) == "20"
    assert candidate(target = "apple",dictionary = ['blade', 'plain', 'amber']) == "3l1"
    assert candidate(target = "cat",dictionary = ['dog', 'dot']) == "c2"
    assert candidate(target = "internationalization",dictionary = ['international', 'interstate', 'interpersonal']) == "20"
    assert candidate(target = "internationalization",dictionary = ['inter', 'national', 'ization']) == "20"
    assert candidate(target = "a",dictionary = ['b']) == "a"
    assert candidate(target = "apple",dictionary = ['blade']) == "a4"
    assert candidate(target = "test",dictionary = ['tent', 'sett', 'text']) == "2s1"
    assert candidate(target = "abcd",dictionary = ['abcde', 'abfde', 'abgde']) == "4"
    assert candidate(target = "a",dictionary = []) == "1"
    assert candidate(target = "a",dictionary = ['b', 'c', 'd']) == "a"
    assert candidate(target = "congratulations",dictionary = ['congratulate', 'congregate', 'congruity', 'congruity', 'congruity']) == "15"
    assert candidate(target = "pneumonoultramicroscopicsilicovolcanoconiosis",dictionary = ['pneumo', 'ultra', 'microscopic', 'silico', 'volcano', 'coniosis', 'supercalifragilisticexpialidocious']) == "45"
    assert candidate(target = "quantification",dictionary = ['quantific', 'quantificat', 'quantificatio', 'quantificati', 'quantificati', 'quantificati', 'quantificati', 'quantificati', 'quantificati', 'quantificati']) == "14"
    assert candidate(target = "unbelievable",dictionary = ['unbeleviable', 'unelevable', 'unbelieveable', 'unbelivable', 'unbelievablee']) == "7v4"
    assert candidate(target = "antidisestablishmentarianism",dictionary = ['antisemitism', 'establishment', 'disestablishment', 'disestablishmentarianism', 'antidisestablishmentarian']) == "28"
    assert candidate(target = "characterization",dictionary = ['character', 'characteristic', 'charisma', 'charitable']) == "16"
    assert candidate(target = "environmental",dictionary = ['environment', 'environments', 'environmentalist', 'environmentalists', 'environmentally']) == "13"
    assert candidate(target = "incomprehensibilities",dictionary = ['incomprehensible', 'incomprehension', 'incomprehensibly', 'incomprehensiveness']) == "21"
    assert candidate(target = "abcdefghijklmnopqrstuvwxyz",dictionary = ['abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqr', 'abcdefghijklmnopq', 'abcdefghijklmnop', 'abcdefghijklmno', 'abcdefghijk', 'abcdefghij', 'abcdefghi', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']) == "26"
    assert candidate(target = "methodology",dictionary = ['method', 'methodical', 'methodically', 'methodologies', 'methodological', 'methodologist']) == "11"
    assert candidate(target = "abcdefghij",dictionary = ['abcdefghi', 'abcdefgh', 'abcdefg', 'abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a', 'bcdefghij', 'cdefghij', 'defghij', 'efghij', 'fghij', 'ghij', 'hij', 'ij', 'j']) == "10"
    assert candidate(target = "optimization",dictionary = ['optimizationg', 'optimizat', 'optimiza', 'optimiz', 'optimize', 'optimi', 'optim', 'opti', 'opt', 'op', 'o', 'optimizationnn']) == "12"
    assert candidate(target = "unfortunately",dictionary = ['unsurprisingly', 'unofficially', 'unaccountably', 'underrepresented']) == "10e2"
    assert candidate(target = "honorificabilitudinitatibus",dictionary = ['honorificabilitudinitatib', 'honorificabilitudinitati', 'honorificabilitudinit', 'honorificabilitudini']) == "27"
    assert candidate(target = "microprocessors",dictionary = ['microscopic', 'microphones', 'microorganisms']) == "15"
    assert candidate(target = "supercalifragilisticexpialidocious",dictionary = ['supercalifragilistic', 'supercalifragilisticexp', 'superfragilisticexpialidocious']) == "34"
    assert candidate(target = "antidisestablishmentarianism",dictionary = ['antidisestablishmentarianisms', 'antidisestablishmentarian', 'antidisestablishmentaria', 'antidisestablishmentari', 'antidisestablishmentar']) == "28"
    assert candidate(target = "onomatopoeia",dictionary = ['onomatopoetic', 'onomatopoeic', 'onomatopoet', 'onomatopoeias', 'onomatopoe']) == "11a"
    assert candidate(target = "unbelievable",dictionary = ['incredible', 'unbeliever', 'unbelief', 'believable', 'unbelieveable']) == "12"
    assert candidate(target = "communication",dictionary = ['communicate', 'communicator', 'communicative', 'communications', 'communicates']) == "12n"
    assert candidate(target = "electroencephalography",dictionary = ['electro', 'encephalogram', 'graphy', 'electronic']) == "22"
    assert candidate(target = "supercalifragilisticexpialidocious",dictionary = ['supercalifragilistic', 'califragilisticexpialidocious', 'superfragilistic', 'califragilistic', 'fragilisticexpialidocious']) == "34"
    assert candidate(target = "universality",dictionary = ['universe', 'universals', 'universally', 'universal', 'universes']) == "12"
    assert candidate(target = "floccinaucinihilipilification",dictionary = ['floccinaucinihilipilific', 'floccinaucinihil', 'floccinauc', 'floccina', 'flocc']) == "29"
    assert candidate(target = "mississippi",dictionary = ['missisippi', 'mississipi', 'missisippi', 'mississipi', 'mississipp', 'missisippi', 'mississipi', 'mississipp', 'mississippii', 'mississippii', 'mississippiii', 'mississippiiii', 'mississippiiiii', 'mississippiiiiii', 'mississippiiiiiii', 'mississippiiiiiiii', 'mississippiiiiiiiii', 'mississippiiiiiiiiii', 'mississippiiiiiiiiiii', 'mississippiiiiiiiiiiii']) == "11"
    assert candidate(target = "algorithm",dictionary = ['algorith', 'algorithmm', 'algorithem', 'algorit', 'algori', 'algor', 'algo', 'alg', 'al', 'a', 'algorithmically']) == "9"
    assert candidate(target = "antidisestablishmentarianism",dictionary = ['antidisestablishmentarian', 'disestablishmentarianism', 'antidisestablishment', 'disestablishmentarian']) == "28"
    assert candidate(target = "counterdemonstration",dictionary = ['counter', 'demonstration', 'counterdemonstrate', 'counterdemonstrations', 'counterdemonstrat', 'counterdemonstrator']) == "20"
    assert candidate(target = "electroencephalograph",dictionary = ['electrocardiogram', 'electromyography', 'electrochemical', 'electroconductive']) == "21"
    assert candidate(target = "abcdefghijklmnopqrstuvwxyz",dictionary = ['abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwyz', 'abcdefgh', 'mnopqrstuvwxyz']) == "26"
    assert candidate(target = "xxyyzz",dictionary = ['xxxyyy', 'xxyyy', 'xxzyy', 'xyyzz', 'xxyyz', 'xyzzz', 'xxzzz', 'xyzzy']) == "5z"
    assert candidate(target = "universality",dictionary = ['universal', 'universe', 'universalize', 'universally', 'universals']) == "11y"
    assert candidate(target = "algorithm",dictionary = ['algebra', 'algorithmic', 'alge', 'rithm', 'algo', 'rith', 'logarithm', 'algor', 'rithmo', 'algorith']) == "a8"
    assert candidate(target = "floccinaucinihilipilification",dictionary = ['floccinaucinihilipilifications', 'floccinaucinihilipilific', 'floccinaucinihilipilifics', 'floccinaucinihilipilificated']) == "29"
    assert candidate(target = "development",dictionary = ['develop', 'developed', 'developing', 'developmental', 'developments', 'developer']) == "11"
    assert candidate(target = "supercalifragilisticexpialidocious",dictionary = ['supercalifragile', 'superduper', 'supercaliber', 'supercal']) == "34"
    assert candidate(target = "supercalifragilisticexpialidocious",dictionary = ['super', 'cali', 'fragilistic', 'expialidocious', 'supercalifragilisticexpialido']) == "34"
    assert candidate(target = "floccinaucinihilipilification",dictionary = ['floccinaucinihilipilificat', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati', 'floccinaucinihilipilificati']) == "29"
    assert candidate(target = "pneumonoultramicroscopicsilicovolcanoconiosis",dictionary = ['pneumonoultramicroscopic', 'silicovolcanoconiosis', 'ultramicroscopic', 'pneumonoconiosis']) == "45"
    assert candidate(target = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",dictionary = ['aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz', 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzz', 'aabbcde', 'mnopqr', 'stuvwx', 'yz']) == "52"
    assert candidate(target = "electroencephalographically",dictionary = ['electroencephalograph', 'electroencephalographs', 'electroencephalographing', 'electroencephalography']) == "27"
    assert candidate(target = "floccinaucinihilipilification",dictionary = ['floccinaucinihilipilifications', 'floccinaucinihilipilific', 'floccinaucinihilipilic', 'floccinaucinihilipi']) == "29"
    assert candidate(target = "individual",dictionary = ['individuality', 'individuals', 'individualism', 'individualist', 'individualistic']) == "10"
    assert candidate(target = "floccinaucinihilipilification",dictionary = ['floccinaucinihilipilify', 'floccinaucinihilipilified', 'floccinaucinihilipilifies', 'floccinaucinihilipilifying']) == "29"
    assert candidate(target = "microprocessor",dictionary = ['micro', 'processor', 'microchip', 'microwave']) == "14"
    assert candidate(target = "pneumonoultramicroscopicsilicovolcanoconiosis",dictionary = ['pneumonoultramicroscopicsilicovolcanoconiosi', 'pneumonoultramicroscopicsilicovolcanoconio', 'pneumonoultramicroscopicsilicovolcanoconi', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon', 'pneumonoultramicroscopicsilicovolcanocon']) == "45"
    assert candidate(target = "thyroparathyroidectomize",dictionary = ['thyroparathyroidectomy', 'thyroparathyroidectomying', 'thyroparathyroidectomized', 'thyroparathyroidectomizes']) == "24"
    assert candidate(target = "floccinaucinihilipilification",dictionary = ['floccinaucinihilipilifications', 'floccinaucinihilipilific', 'floccinaucinihilipili', 'floccinaucinihilipi', 'floccinaucinihilip']) == "29"
    assert candidate(target = "unquestionableness",dictionary = ['question', 'unquestionable', 'unquestionably', 'unquestionablenes']) == "18"
    assert candidate(target = "acknowledgment",dictionary = ['acknowledge', 'acknowledged', 'acknowledges', 'acknowledging']) == "14"
    assert candidate(target = "supercalifragilisticexpialidocious",dictionary = ['supercalifragilistic', 'califragilistic', 'expialidocious', 'supercal']) == "34"
    assert candidate(target = "environment",dictionary = ['envoy', 'enterprise', 'envelope', 'evaluate']) == "11"
    assert candidate(target = "programming",dictionary = ['program', 'programs', 'programmatic', 'programmer', 'programmed', 'programmers']) == "10g"
    assert candidate(target = "supercalifragilisticexpialidocious",dictionary = ['super', 'califragilistic', 'expialidocious', 'supercal', 'fragilistic', 'expi', 'alidocious', 'supercali', 'fragil', 'expiali', 'docious']) == "34"


