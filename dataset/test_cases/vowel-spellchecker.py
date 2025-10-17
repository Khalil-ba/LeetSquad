def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(wordlist = ['aeiou', 'AEIOU'],queries = ['aeio', 'aeiou', 'AEIOU', 'eioua']) == ['', 'aeiou', 'AEIOU', 'aeiou']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['aeiou', 'AEIOU'],queries = ['aeio', 'aeiou', 'AEIOU', 'eioua']) == ['', 'aeiou', 'AEIOU', 'aeiou']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['aaaaa', 'Aaaaa'],queries = ['Aaaaa', 'aaaaa', 'aaAaa', 'aAaaa', 'AaAaa']) == ['Aaaaa', 'aaaaa', 'aaaaa', 'aaaaa', 'aaaaa']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['aaaaa', 'Aaaaa'],queries = ['Aaaaa', 'aaaaa', 'aaAaa', 'aAaaa', 'AaAaa']) == ['Aaaaa', 'aaaaa', 'aaaaa', 'aaaaa', 'aaaaa']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['yellow'],queries = ['YellOw']) == ['yellow']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['yellow'],queries = ['YellOw']) == ['yellow']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['apple', 'Apple', 'apples'],queries = ['apples', 'APPLES', 'applesa', 'applee']) == ['apples', 'apples', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['apple', 'Apple', 'apples'],queries = ['apples', 'APPLES', 'applesa', 'applee']) == ['apples', 'apples', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['KiTe', 'kite', 'hare', 'Hare'],queries = ['kite', 'Kite', 'KiTe', 'Hare', 'HARE', 'Hear', 'hear', 'keti', 'keet', 'keto']) == ['kite', 'KiTe', 'KiTe', 'Hare', 'hare', '', '', 'KiTe', '', 'KiTe']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['KiTe', 'kite', 'hare', 'Hare'],queries = ['kite', 'Kite', 'KiTe', 'Hare', 'HARE', 'Hear', 'hear', 'keti', 'keet', 'keto']) == ['kite', 'KiTe', 'KiTe', 'Hare', 'hare', '', '', 'KiTe', '', 'KiTe']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['onomatopoeia', 'ONOMATOPOEIA', 'Onomatopoeia', 'oNomatopoeia'],queries = ['onomatopoeia', 'ONOMATOPOEIA', 'Onomatopoeia', 'oNomatopoeia', 'onomatopeiaa', 'onomatopoei']) == ['onomatopoeia', 'ONOMATOPOEIA', 'Onomatopoeia', 'oNomatopoeia', 'onomatopoeia', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['onomatopoeia', 'ONOMATOPOEIA', 'Onomatopoeia', 'oNomatopoeia'],queries = ['onomatopoeia', 'ONOMATOPOEIA', 'Onomatopoeia', 'oNomatopoeia', 'onomatopeiaa', 'onomatopoei']) == ['onomatopoeia', 'ONOMATOPOEIA', 'Onomatopoeia', 'oNomatopoeia', 'onomatopoeia', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['umbrella', 'university', 'underground', 'unicorn', 'uppercut'],queries = ['UMBRELLA', 'UNIVERSITY', 'UNDERGROUND', 'UNICORN', 'UPPERCUT', 'umbrlla', 'universit', 'undergroand', 'unicor', 'upperct', 'Umbrella', 'Unversity', 'Uderground', 'Uinicorn', 'Uppercut']) == ['umbrella', 'university', 'underground', 'unicorn', 'uppercut', '', '', 'underground', '', '', 'umbrella', '', '', '', 'uppercut']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['umbrella', 'university', 'underground', 'unicorn', 'uppercut'],queries = ['UMBRELLA', 'UNIVERSITY', 'UNDERGROUND', 'UNICORN', 'UPPERCUT', 'umbrlla', 'universit', 'undergroand', 'unicor', 'upperct', 'Umbrella', 'Unversity', 'Uderground', 'Uinicorn', 'Uppercut']) == ['umbrella', 'university', 'underground', 'unicorn', 'uppercut', '', '', 'underground', '', '', 'umbrella', '', '', '', 'uppercut']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['bicycle', 'Bicycle', 'BIcycle', 'bIcycle', 'biCycle', 'bicyCLE'],queries = ['bicycle', 'Bicycle', 'BIcycle', 'bIcycle', 'biCycle', 'bicyCLE', 'bicyclE', 'bicyclE', 'bicycLe', 'bicyclE', 'bicycleE']) == ['bicycle', 'Bicycle', 'BIcycle', 'bIcycle', 'biCycle', 'bicyCLE', 'bicycle', 'bicycle', 'bicycle', 'bicycle', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['bicycle', 'Bicycle', 'BIcycle', 'bIcycle', 'biCycle', 'bicyCLE'],queries = ['bicycle', 'Bicycle', 'BIcycle', 'bIcycle', 'biCycle', 'bicyCLE', 'bicyclE', 'bicyclE', 'bicycLe', 'bicyclE', 'bicycleE']) == ['bicycle', 'Bicycle', 'BIcycle', 'bIcycle', 'biCycle', 'bicyCLE', 'bicycle', 'bicycle', 'bicycle', 'bicycle', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['dictionary', 'Dictionary', 'DICTIONARY', 'DictIoNaRy'],queries = ['dictioNary', 'DICTIONARY', 'dictionary', 'dIctionarY', 'DictioNaryy', 'dictionar']) == ['dictionary', 'DICTIONARY', 'dictionary', 'dictionary', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['dictionary', 'Dictionary', 'DICTIONARY', 'DictIoNaRy'],queries = ['dictioNary', 'DICTIONARY', 'dictionary', 'dIctionarY', 'DictioNaryy', 'dictionar']) == ['dictionary', 'DICTIONARY', 'dictionary', 'dictionary', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['banana', 'Banana', 'BANANA', 'banAnA'],queries = ['banana', 'Banana', 'BANANA', 'banAnA', 'bananA', 'bananaa', 'BANANAS']) == ['banana', 'Banana', 'BANANA', 'banAnA', 'banana', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['banana', 'Banana', 'BANANA', 'banAnA'],queries = ['banana', 'Banana', 'BANANA', 'banAnA', 'bananA', 'bananaa', 'BANANAS']) == ['banana', 'Banana', 'BANANA', 'banAnA', 'banana', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['interview', 'INTERVIEW', 'Interview', 'inTerView'],queries = ['interview', 'INTERVIEW', 'Interview', 'inTerView', 'interviw', 'intervew']) == ['interview', 'INTERVIEW', 'Interview', 'inTerView', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['interview', 'INTERVIEW', 'Interview', 'inTerView'],queries = ['interview', 'INTERVIEW', 'Interview', 'inTerView', 'interviw', 'intervew']) == ['interview', 'INTERVIEW', 'Interview', 'inTerView', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['university', 'UNIVERSITY', 'University', 'universitry', 'universitie'],queries = ['university', 'UNIVERSITY', 'University', 'universitry', 'universitie', 'universitry']) == ['university', 'UNIVERSITY', 'University', 'universitry', 'universitie', 'universitry']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['university', 'UNIVERSITY', 'University', 'universitry', 'universitie'],queries = ['university', 'UNIVERSITY', 'University', 'universitry', 'universitie', 'universitry']) == ['university', 'UNIVERSITY', 'University', 'universitry', 'universitie', 'universitry']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['AbCdE', 'abcdE', 'aBcDe', 'abCDE', 'abcde'],queries = ['AbCdE', 'Abcde', 'abcde', 'aBcDe', 'abCDE', 'ABCDE', 'abcde', 'AbCdF', 'AbCdEe']) == ['AbCdE', 'AbCdE', 'abcde', 'aBcDe', 'abCDE', 'AbCdE', 'abcde', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['AbCdE', 'abcdE', 'aBcDe', 'abCDE', 'abcde'],queries = ['AbCdE', 'Abcde', 'abcde', 'aBcDe', 'abCDE', 'ABCDE', 'abcde', 'AbCdF', 'AbCdEe']) == ['AbCdE', 'AbCdE', 'abcde', 'aBcDe', 'abCDE', 'AbCdE', 'abcde', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['AbCdE', 'abCDe', 'aBcDe', 'ABCDe', 'abcde', 'aBcde', 'abCde', 'ABCDE'],queries = ['abcde', 'ABCDE', 'AbCdE', 'abcde', 'aBcDe', 'ABcDe', 'abcdef', 'aBcde', 'ABCDe', 'abCDe']) == ['abcde', 'ABCDE', 'AbCdE', 'abcde', 'aBcDe', 'AbCdE', '', 'aBcde', 'ABCDe', 'abCDe']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['AbCdE', 'abCDe', 'aBcDe', 'ABCDe', 'abcde', 'aBcde', 'abCde', 'ABCDE'],queries = ['abcde', 'ABCDE', 'AbCdE', 'abcde', 'aBcDe', 'ABcDe', 'abcdef', 'aBcde', 'ABCDe', 'abCDe']) == ['abcde', 'ABCDE', 'AbCdE', 'abcde', 'aBcDe', 'AbCdE', '', 'aBcde', 'ABCDe', 'abCDe']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['xylophone', 'Xylophone', 'XYLOPHONE', 'xYlOpHoNe'],queries = ['xylophone', 'Xylophone', 'XYLOPHONE', 'xYlOpHoNe', 'xylopon', 'xylofon']) == ['xylophone', 'Xylophone', 'XYLOPHONE', 'xYlOpHoNe', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['xylophone', 'Xylophone', 'XYLOPHONE', 'xYlOpHoNe'],queries = ['xylophone', 'Xylophone', 'XYLOPHONE', 'xYlOpHoNe', 'xylopon', 'xylofon']) == ['xylophone', 'Xylophone', 'XYLOPHONE', 'xYlOpHoNe', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['umbrella', 'UmBrella', 'Umbrella', 'UMBRELLA'],queries = ['UMBRELLA', 'umbrELLA', 'umbrelLA', 'umbrella', 'UmBrelLA', 'UMBRELLAA', 'umbrellaa']) == ['UMBRELLA', 'umbrella', 'umbrella', 'umbrella', 'umbrella', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['umbrella', 'UmBrella', 'Umbrella', 'UMBRELLA'],queries = ['UMBRELLA', 'umbrELLA', 'umbrelLA', 'umbrella', 'UmBrelLA', 'UMBRELLAA', 'umbrellaa']) == ['UMBRELLA', 'umbrella', 'umbrella', 'umbrella', 'umbrella', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['umbrella', 'Umbrella', 'UMBRELLA', 'umbralla', 'Umbralla'],queries = ['umbrella', 'Umbrella', 'UMBRELLA', 'umbralla', 'Umbralla', 'umbrallaS', 'umbrellA', 'UmbrallA', 'UMbralla', 'UmbrAlla']) == ['umbrella', 'Umbrella', 'UMBRELLA', 'umbralla', 'Umbralla', '', 'umbrella', 'umbralla', 'umbralla', 'umbralla']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['umbrella', 'Umbrella', 'UMBRELLA', 'umbralla', 'Umbralla'],queries = ['umbrella', 'Umbrella', 'UMBRELLA', 'umbralla', 'Umbralla', 'umbrallaS', 'umbrellA', 'UmbrallA', 'UMbralla', 'UmbrAlla']) == ['umbrella', 'Umbrella', 'UMBRELLA', 'umbralla', 'Umbralla', '', 'umbrella', 'umbralla', 'umbralla', 'umbralla']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['beautiful', 'Beautiful', 'BEAUTIFUL', 'beautifull', 'beautifu', 'beautifulll'],queries = ['beautiful', 'Beautiful', 'BEAUTIFUL', 'beautifull', 'beautifu', 'beautifulll', 'beautifulll', 'beautifull', 'beautifuul', 'beautiul']) == ['beautiful', 'Beautiful', 'BEAUTIFUL', 'beautifull', 'beautifu', 'beautifulll', 'beautifulll', 'beautifull', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['beautiful', 'Beautiful', 'BEAUTIFUL', 'beautifull', 'beautifu', 'beautifulll'],queries = ['beautiful', 'Beautiful', 'BEAUTIFUL', 'beautifull', 'beautifu', 'beautifulll', 'beautifulll', 'beautifull', 'beautifuul', 'beautiul']) == ['beautiful', 'Beautiful', 'BEAUTIFUL', 'beautifull', 'beautifu', 'beautifulll', 'beautifulll', 'beautifull', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['banana', 'Banana', 'BANANA', 'bandana', 'BandAna'],queries = ['banana', 'Banana', 'BANANA', 'bandana', 'BANDANA', 'bandanna', 'bandanna', 'bndn', 'bandn']) == ['banana', 'Banana', 'BANANA', 'bandana', 'bandana', '', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['banana', 'Banana', 'BANANA', 'bandana', 'BandAna'],queries = ['banana', 'Banana', 'BANANA', 'bandana', 'BANDANA', 'bandanna', 'bandanna', 'bndn', 'bandn']) == ['banana', 'Banana', 'BANANA', 'bandana', 'bandana', '', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['beautiful', 'BeAuTiFuL', 'BEautiful', 'bEAUtIfUl', 'bEAUtIFuL'],queries = ['beautiful', 'BeAuTiFuL', 'BEautiful', 'bEAUtIfUl', 'bEAUtIFuL', 'beautifuls', 'BeAuTiFuLs', 'BEautifuls', 'bEAUtIfUls']) == ['beautiful', 'BeAuTiFuL', 'BEautiful', 'bEAUtIfUl', 'bEAUtIFuL', '', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['beautiful', 'BeAuTiFuL', 'BEautiful', 'bEAUtIfUl', 'bEAUtIFuL'],queries = ['beautiful', 'BeAuTiFuL', 'BEautiful', 'bEAUtIfUl', 'bEAUtIFuL', 'beautifuls', 'BeAuTiFuLs', 'BEautifuls', 'bEAUtIfUls']) == ['beautiful', 'BeAuTiFuL', 'BEautiful', 'bEAUtIfUl', 'bEAUtIFuL', '', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['environment', 'ENVIRONMENT', 'EnViRonMeNt', 'ENvIrOnMeNt', 'ENvIrOnMeNT'],queries = ['environment', 'ENVIRONMENT', 'EnViRonMeNt', 'ENvIrOnMeNt', 'ENvIrOnMeNT', 'environments', 'ENVIRONMENTs', 'EnViRonMeNts', 'ENvIrOnMeNts']) == ['environment', 'ENVIRONMENT', 'EnViRonMeNt', 'ENvIrOnMeNt', 'ENvIrOnMeNT', '', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['environment', 'ENVIRONMENT', 'EnViRonMeNt', 'ENvIrOnMeNt', 'ENvIrOnMeNT'],queries = ['environment', 'ENVIRONMENT', 'EnViRonMeNt', 'ENvIrOnMeNt', 'ENvIrOnMeNT', 'environments', 'ENVIRONMENTs', 'EnViRonMeNts', 'ENvIrOnMeNts']) == ['environment', 'ENVIRONMENT', 'EnViRonMeNt', 'ENvIrOnMeNt', 'ENvIrOnMeNT', '', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['algorithm', 'Algorithm', 'ALGORITHM', 'algorithem', 'algoritum', 'algorith', 'algorithmmm'],queries = ['algorithm', 'Algorithm', 'ALGORITHM', 'algorithem', 'algoritum', 'algorith', 'algorithmmm', 'algorithmmm', 'algorithmm', 'algorithmm']) == ['algorithm', 'Algorithm', 'ALGORITHM', 'algorithem', 'algoritum', 'algorith', 'algorithmmm', 'algorithmmm', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['algorithm', 'Algorithm', 'ALGORITHM', 'algorithem', 'algoritum', 'algorith', 'algorithmmm'],queries = ['algorithm', 'Algorithm', 'ALGORITHM', 'algorithem', 'algoritum', 'algorith', 'algorithmmm', 'algorithmmm', 'algorithmm', 'algorithmm']) == ['algorithm', 'Algorithm', 'ALGORITHM', 'algorithem', 'algoritum', 'algorith', 'algorithmmm', 'algorithmmm', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['education', 'environment', 'elevation', 'excavation', 'explanation'],queries = ['Education', 'Environment', 'Elevation', 'Excavation', 'Explanation', 'edication', 'enviroment', 'elevatoin', 'exacation', 'explanatoin', 'educatio', 'environmnt', 'elevatn', 'excavtn', 'explntion', 'educatoin', 'enivornment', 'elevtn', 'excavatn', 'explanatn', 'educati', 'environmt', 'elevtn', 'excavtn', 'explntn']) == ['education', 'environment', 'elevation', 'excavation', 'explanation', 'education', '', 'elevation', '', 'explanation', '', '', '', '', '', 'education', '', '', '', '', '', '', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['education', 'environment', 'elevation', 'excavation', 'explanation'],queries = ['Education', 'Environment', 'Elevation', 'Excavation', 'Explanation', 'edication', 'enviroment', 'elevatoin', 'exacation', 'explanatoin', 'educatio', 'environmnt', 'elevatn', 'excavtn', 'explntion', 'educatoin', 'enivornment', 'elevtn', 'excavatn', 'explanatn', 'educati', 'environmt', 'elevtn', 'excavtn', 'explntn']) == ['education', 'environment', 'elevation', 'excavation', 'explanation', 'education', '', 'elevation', '', 'explanation', '', '', '', '', '', 'education', '', '', '', '', '', '', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['education', 'EDUCATION', 'Education', 'edUcation'],queries = ['EDUCATION', 'education', 'Education', 'edUcation', 'educatiion', 'eduCation']) == ['EDUCATION', 'education', 'Education', 'edUcation', '', 'education']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['education', 'EDUCATION', 'Education', 'edUcation'],queries = ['EDUCATION', 'education', 'Education', 'edUcation', 'educatiion', 'eduCation']) == ['EDUCATION', 'education', 'Education', 'edUcation', '', 'education']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['elephant', 'ElEphant', 'ELEPHANT', 'elePHANT', 'eLePHANT'],queries = ['elephant', 'elePHANT', 'eLePHANT', 'elePHAN', 'ElePHAN', 'eLEPHAN', 'ELephAN', 'elePHANt']) == ['elephant', 'elePHANT', 'eLePHANT', '', '', '', '', 'elephant']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['elephant', 'ElEphant', 'ELEPHANT', 'elePHANT', 'eLePHANT'],queries = ['elephant', 'elePHANT', 'eLePHANT', 'elePHAN', 'ElePHAN', 'eLEPHAN', 'ELephAN', 'elePHANt']) == ['elephant', 'elePHANT', 'eLePHANT', '', '', '', '', 'elephant']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['education', 'EDUCATION', 'EduCation', 'educate', 'educating'],queries = ['education', 'EDUCATION', 'EduCation', 'educate', 'educatin', 'Educating']) == ['education', 'EDUCATION', 'EduCation', 'educate', '', 'educating']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['education', 'EDUCATION', 'EduCation', 'educate', 'educating'],queries = ['education', 'EDUCATION', 'EduCation', 'educate', 'educatin', 'Educating']) == ['education', 'EDUCATION', 'EduCation', 'educate', '', 'educating']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['elephant', 'giraffe', 'hippo', 'rhino', 'zebra', 'lemur'],queries = ['Elephant', 'Giraffe', 'Hippo', 'Rhino', 'Zebra', 'Lemur', 'elphant', 'giraff', 'hippo', 'rhin', 'zebr', 'lemr', 'elphantt', 'giraffe', 'hippp', 'rhinno', 'zebraa', 'lemur', 'elephant', 'giraffe', 'hippo', 'rhino', 'zebra', 'lemur', 'elephants', 'giraffes', 'hippos', 'rhinos', 'zebras', 'lemurs']) == ['elephant', 'giraffe', 'hippo', 'rhino', 'zebra', 'lemur', '', '', 'hippo', '', '', '', '', 'giraffe', '', '', '', 'lemur', 'elephant', 'giraffe', 'hippo', 'rhino', 'zebra', 'lemur', '', '', '', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['elephant', 'giraffe', 'hippo', 'rhino', 'zebra', 'lemur'],queries = ['Elephant', 'Giraffe', 'Hippo', 'Rhino', 'Zebra', 'Lemur', 'elphant', 'giraff', 'hippo', 'rhin', 'zebr', 'lemr', 'elphantt', 'giraffe', 'hippp', 'rhinno', 'zebraa', 'lemur', 'elephant', 'giraffe', 'hippo', 'rhino', 'zebra', 'lemur', 'elephants', 'giraffes', 'hippos', 'rhinos', 'zebras', 'lemurs']) == ['elephant', 'giraffe', 'hippo', 'rhino', 'zebra', 'lemur', '', '', 'hippo', '', '', '', '', 'giraffe', '', '', '', 'lemur', 'elephant', 'giraffe', 'hippo', 'rhino', 'zebra', 'lemur', '', '', '', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['algorithm', 'AlgoritHM', 'aLgoRitHm', 'alGoRiThM'],queries = ['algorithm', 'AlgoritHM', 'aLgoRitHm', 'alGoRiThM', 'algoriTHM', 'AlgoRiThM', 'aLGorIthM', 'AlGorIthM', 'algOrIthM']) == ['algorithm', 'AlgoritHM', 'aLgoRitHm', 'alGoRiThM', 'algorithm', 'algorithm', 'algorithm', 'algorithm', 'algorithm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['algorithm', 'AlgoritHM', 'aLgoRitHm', 'alGoRiThM'],queries = ['algorithm', 'AlgoritHM', 'aLgoRitHm', 'alGoRiThM', 'algoriTHM', 'AlgoRiThM', 'aLGorIthM', 'AlGorIthM', 'algOrIthM']) == ['algorithm', 'AlgoritHM', 'aLgoRitHm', 'alGoRiThM', 'algorithm', 'algorithm', 'algorithm', 'algorithm', 'algorithm']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['education', 'EDUCATION', 'EducAtion', 'eDUCAtion'],queries = ['EDUCATION', 'educAtion', 'eDUCAtion', 'EDucAtion', 'educAtioN', 'EDucAtioN', 'educatiOn', 'EDucatiOn']) == ['EDUCATION', 'education', 'eDUCAtion', 'education', 'education', 'education', 'education', 'education']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['education', 'EDUCATION', 'EducAtion', 'eDUCAtion'],queries = ['EDUCATION', 'educAtion', 'eDUCAtion', 'EDucAtion', 'educAtioN', 'EDucAtioN', 'educatiOn', 'EDucatiOn']) == ['EDUCATION', 'education', 'eDUCAtion', 'education', 'education', 'education', 'education', 'education']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['education', 'EDUCATION', 'EduCatiOn', 'eDUCaTIOn', 'EDuCAtIoN'],queries = ['education', 'EDUCATION', 'EduCatiOn', 'eDUCaTIOn', 'EDuCAtIoN', 'educations', 'EDUCATIONS', 'EduCatiOns', 'eDUCaTIOns']) == ['education', 'EDUCATION', 'EduCatiOn', 'eDUCaTIOn', 'EDuCAtIoN', '', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['education', 'EDUCATION', 'EduCatiOn', 'eDUCaTIOn', 'EDuCAtIoN'],queries = ['education', 'EDUCATION', 'EduCatiOn', 'eDUCaTIOn', 'EDuCAtIoN', 'educations', 'EDUCATIONS', 'EduCatiOns', 'eDUCaTIOns']) == ['education', 'EDUCATION', 'EduCatiOn', 'eDUCaTIOn', 'EDuCAtIoN', '', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['umbrella', 'uMBrElLa', 'UMBRELLA', 'umbrellA', 'umbralla'],queries = ['umbrella', 'uMBrElLa', 'UMBRELLA', 'umbrellA', 'umbralla', 'UMBRELLAA', 'uMBrElLAA', 'UMBRELLAAA', 'umbrallaA']) == ['umbrella', 'uMBrElLa', 'UMBRELLA', 'umbrellA', 'umbralla', '', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['umbrella', 'uMBrElLa', 'UMBRELLA', 'umbrellA', 'umbralla'],queries = ['umbrella', 'uMBrElLa', 'UMBRELLA', 'umbrellA', 'umbralla', 'UMBRELLAA', 'uMBrElLAA', 'UMBRELLAAA', 'umbrallaA']) == ['umbrella', 'uMBrElLa', 'UMBRELLA', 'umbrellA', 'umbralla', '', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['elephant', 'Elephant', 'ELEPHANT', 'elevnt', 'elphant', 'elefant', 'elephantt'],queries = ['elephant', 'Elephant', 'ELEPHANT', 'elevnt', 'elphant', 'elefant', 'elephantt', 'elphnt', 'elphntt', 'elphnta']) == ['elephant', 'Elephant', 'ELEPHANT', 'elevnt', 'elphant', 'elefant', 'elephantt', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['elephant', 'Elephant', 'ELEPHANT', 'elevnt', 'elphant', 'elefant', 'elephantt'],queries = ['elephant', 'Elephant', 'ELEPHANT', 'elevnt', 'elphant', 'elefant', 'elephantt', 'elphnt', 'elphntt', 'elphnta']) == ['elephant', 'Elephant', 'ELEPHANT', 'elevnt', 'elphant', 'elefant', 'elephantt', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['environment', 'Environment', 'ENVIRONMENT', 'environmnt', 'Environmnt', 'environMent'],queries = ['environment', 'Environment', 'ENVIRONMENT', 'environmnt', 'Environmnt', 'environMent', 'environMnt', 'environmEnt', 'environmEnts', 'environmEnt']) == ['environment', 'Environment', 'ENVIRONMENT', 'environmnt', 'Environmnt', 'environMent', 'environmnt', 'environment', '', 'environment']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['environment', 'Environment', 'ENVIRONMENT', 'environmnt', 'Environmnt', 'environMent'],queries = ['environment', 'Environment', 'ENVIRONMENT', 'environmnt', 'Environmnt', 'environMent', 'environMnt', 'environmEnt', 'environmEnts', 'environmEnt']) == ['environment', 'Environment', 'ENVIRONMENT', 'environmnt', 'Environmnt', 'environMent', 'environmnt', 'environment', '', 'environment']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['beautiful', 'Beautiful', 'BEAUTIFUL', 'beautifull', 'beautifu'],queries = ['beautiful', 'Beautiful', 'BEAUTIFUL', 'beautifull', 'beautifu', 'beautifull']) == ['beautiful', 'Beautiful', 'BEAUTIFUL', 'beautifull', 'beautifu', 'beautifull']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['beautiful', 'Beautiful', 'BEAUTIFUL', 'beautifull', 'beautifu'],queries = ['beautiful', 'Beautiful', 'BEAUTIFUL', 'beautifull', 'beautifu', 'beautifull']) == ['beautiful', 'Beautiful', 'BEAUTIFUL', 'beautifull', 'beautifu', 'beautifull']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['baNana', 'Banana', 'BANANA', 'baNANa'],queries = ['banana', 'BANANA', 'BaNaNa', 'bananA', 'baNANaa', 'bAnanaa']) == ['baNana', 'BANANA', 'baNana', 'baNana', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['baNana', 'Banana', 'BANANA', 'baNANa'],queries = ['banana', 'BANANA', 'BaNaNa', 'bananA', 'baNANaa', 'bAnanaa']) == ['baNana', 'BANANA', 'baNana', 'baNana', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['dictionary', 'Dictionary', 'DICTIONARY', 'dictionry', 'Dictionry'],queries = ['dictionary', 'Dictionary', 'DICTIONARY', 'dictionry', 'Dictionry', 'dictionryS', 'dictionryY', 'dictiOnary', 'dictioNary', 'dictionry']) == ['dictionary', 'Dictionary', 'DICTIONARY', 'dictionry', 'Dictionry', '', '', 'dictionary', 'dictionary', 'dictionry']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['dictionary', 'Dictionary', 'DICTIONARY', 'dictionry', 'Dictionry'],queries = ['dictionary', 'Dictionary', 'DICTIONARY', 'dictionry', 'Dictionry', 'dictionryS', 'dictionryY', 'dictiOnary', 'dictioNary', 'dictionry']) == ['dictionary', 'Dictionary', 'DICTIONARY', 'dictionry', 'Dictionry', '', '', 'dictionary', 'dictionary', 'dictionry']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['programming', 'Programming', 'PROGRAMMING', 'proGramMinG'],queries = ['programming', 'Programming', 'PROGRAMMING', 'proGramMinG', 'prograMMing', 'ProgramMiNG', 'PROgRaMMiNG', 'pRoGrAmMiNg', 'programmingg', 'proGramming']) == ['programming', 'Programming', 'PROGRAMMING', 'proGramMinG', 'programming', 'programming', 'programming', 'programming', '', 'programming']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['programming', 'Programming', 'PROGRAMMING', 'proGramMinG'],queries = ['programming', 'Programming', 'PROGRAMMING', 'proGramMinG', 'prograMMing', 'ProgramMiNG', 'PROgRaMMiNG', 'pRoGrAmMiNg', 'programmingg', 'proGramming']) == ['programming', 'Programming', 'PROGRAMMING', 'proGramMinG', 'programming', 'programming', 'programming', 'programming', '', 'programming']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['keyboard', 'KeyboArD', 'KEYBOARD', 'keyboARd'],queries = ['keyboard', 'keyboarD', 'KEYBOArd', 'KEYboArd', 'keyboARd', 'KEYboARd', 'keyboArD', 'KEYBOArD']) == ['keyboard', 'keyboard', 'keyboard', 'keyboard', 'keyboARd', 'keyboard', 'keyboard', 'keyboard']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['keyboard', 'KeyboArD', 'KEYBOARD', 'keyboARd'],queries = ['keyboard', 'keyboarD', 'KEYBOArd', 'KEYboArd', 'keyboARd', 'KEYboARd', 'keyboArD', 'KEYBOArD']) == ['keyboard', 'keyboard', 'keyboard', 'keyboard', 'keyboARd', 'keyboard', 'keyboard', 'keyboard']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['sequence', 'Sequence', 'SEQUENCE', 'sequense', 'sequnce', 'sequenec', 'sequencee'],queries = ['sequence', 'Sequence', 'SEQUENCE', 'sequense', 'sequnce', 'sequenec', 'sequencee', 'seqeunce', 'sequnce', 'sequnc']) == ['sequence', 'Sequence', 'SEQUENCE', 'sequense', 'sequnce', 'sequenec', 'sequencee', 'sequence', 'sequnce', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['sequence', 'Sequence', 'SEQUENCE', 'sequense', 'sequnce', 'sequenec', 'sequencee'],queries = ['sequence', 'Sequence', 'SEQUENCE', 'sequense', 'sequnce', 'sequenec', 'sequencee', 'seqeunce', 'sequnce', 'sequnc']) == ['sequence', 'Sequence', 'SEQUENCE', 'sequense', 'sequnce', 'sequenec', 'sequencee', 'sequence', 'sequnce', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['umbrella', 'Umbrella', 'UMBRELLA', 'UmBReLlA'],queries = ['umbrella', 'UMBRELLA', 'Umbrella', 'umBReLlA', 'Umbr3lla', 'umbrellaa', 'UMBRELLAA']) == ['umbrella', 'UMBRELLA', 'Umbrella', 'umbrella', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['umbrella', 'Umbrella', 'UMBRELLA', 'UmBReLlA'],queries = ['umbrella', 'UMBRELLA', 'Umbrella', 'umBReLlA', 'Umbr3lla', 'umbrellaa', 'UMBRELLAA']) == ['umbrella', 'UMBRELLA', 'Umbrella', 'umbrella', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['programming', 'ProgramMING', 'proGRaMMiNG', 'prograMMiNG', 'proGRammING'],queries = ['programming', 'ProgramMING', 'proGRaMMiNG', 'prograMMiNG', 'proGRammING', 'progrAMMING', 'prograMmING', 'progrAmmiNG']) == ['programming', 'ProgramMING', 'proGRaMMiNG', 'prograMMiNG', 'proGRammING', 'programming', 'programming', 'programming']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['programming', 'ProgramMING', 'proGRaMMiNG', 'prograMMiNG', 'proGRammING'],queries = ['programming', 'ProgramMING', 'proGRaMMiNG', 'prograMMiNG', 'proGRammING', 'progrAMMING', 'prograMmING', 'progrAmmiNG']) == ['programming', 'ProgramMING', 'proGRaMMiNG', 'prograMMiNG', 'proGRammING', 'programming', 'programming', 'programming']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['cAt', 'cAts', 'bAt', 'bat', 'bats', 'cAtBat'],queries = ['cats', 'CATS', 'cat', 'bat', 'bAts', 'CATBAT', 'caTbAt', 'batS', 'CAT', 'bAt']) == ['cAts', 'cAts', 'cAt', 'bat', 'bats', 'cAtBat', 'cAtBat', 'bats', 'cAt', 'bAt']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['cAt', 'cAts', 'bAt', 'bat', 'bats', 'cAtBat'],queries = ['cats', 'CATS', 'cat', 'bat', 'bAts', 'CATBAT', 'caTbAt', 'batS', 'CAT', 'bAt']) == ['cAts', 'cAts', 'cAt', 'bat', 'bats', 'cAtBat', 'cAtBat', 'bats', 'cAt', 'bAt']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['queue', 'Queue', 'QUEUE', 'qUeUe'],queries = ['queue', 'Queue', 'QUEUE', 'qUeUe', 'queuE', 'QUeUe', 'qUEUe', 'QUEue', 'quEUe', 'qUeue']) == ['queue', 'Queue', 'QUEUE', 'qUeUe', 'queue', 'queue', 'queue', 'queue', 'queue', 'queue']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['queue', 'Queue', 'QUEUE', 'qUeUe'],queries = ['queue', 'Queue', 'QUEUE', 'qUeUe', 'queuE', 'QUeUe', 'qUEUe', 'QUEue', 'quEUe', 'qUeue']) == ['queue', 'Queue', 'QUEUE', 'qUeUe', 'queue', 'queue', 'queue', 'queue', 'queue', 'queue']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['kiwi', 'Kiwi', 'KIWI', 'kIWi', 'KiwI'],queries = ['kiwi', 'Kiwi', 'KIWI', 'kIWi', 'KiwI', 'kiw', 'KIW', 'kiwiwi', 'kiwii']) == ['kiwi', 'Kiwi', 'KIWI', 'kIWi', 'KiwI', '', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['kiwi', 'Kiwi', 'KIWI', 'kIWi', 'KiwI'],queries = ['kiwi', 'Kiwi', 'KIWI', 'kIWi', 'KiwI', 'kiw', 'KIW', 'kiwiwi', 'kiwii']) == ['kiwi', 'Kiwi', 'KIWI', 'kIWi', 'KiwI', '', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['strawberry', 'Strawberry', 'STRAWBERRY', 'stRawberry', 'strAWberry', 'strawbERRY'],queries = ['strawberry', 'Strawberry', 'STRAWBERRY', 'stRawberry', 'strAWberry', 'strawbERRY', 'straw', 'strawberryy', 'strawberrrry']) == ['strawberry', 'Strawberry', 'STRAWBERRY', 'stRawberry', 'strAWberry', 'strawbERRY', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['strawberry', 'Strawberry', 'STRAWBERRY', 'stRawberry', 'strAWberry', 'strawbERRY'],queries = ['strawberry', 'Strawberry', 'STRAWBERRY', 'stRawberry', 'strAWberry', 'strawbERRY', 'straw', 'strawberryy', 'strawberrrry']) == ['strawberry', 'Strawberry', 'STRAWBERRY', 'stRawberry', 'strAWberry', 'strawbERRY', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['programming', 'PROGRAMMING', 'ProgRaMmInG', 'PROgRaMMiNg', 'pROgRaMMiNG'],queries = ['programming', 'PROGRAMMING', 'ProgRaMmInG', 'PROgRaMMiNg', 'pROgRaMMiNG', 'programmings', 'PROGRAMMINGs', 'ProgRaMmInGs', 'PROgRaMMiNgs']) == ['programming', 'PROGRAMMING', 'ProgRaMmInG', 'PROgRaMMiNg', 'pROgRaMMiNG', '', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['programming', 'PROGRAMMING', 'ProgRaMmInG', 'PROgRaMMiNg', 'pROgRaMMiNG'],queries = ['programming', 'PROGRAMMING', 'ProgRaMmInG', 'PROgRaMMiNg', 'pROgRaMMiNG', 'programmings', 'PROGRAMMINGs', 'ProgRaMmInGs', 'PROgRaMMiNgs']) == ['programming', 'PROGRAMMING', 'ProgRaMmInG', 'PROgRaMMiNg', 'pROgRaMMiNG', '', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['orange', 'Orange', 'ORANGE', 'oRANGE', 'orANGE'],queries = ['orange', 'Orange', 'ORANGE', 'oRANGE', 'orANGE', 'orang', 'ORANG', 'oranje', 'orng']) == ['orange', 'Orange', 'ORANGE', 'oRANGE', 'orANGE', '', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['orange', 'Orange', 'ORANGE', 'oRANGE', 'orANGE'],queries = ['orange', 'Orange', 'ORANGE', 'oRANGE', 'orANGE', 'orang', 'ORANG', 'oranje', 'orng']) == ['orange', 'Orange', 'ORANGE', 'oRANGE', 'orANGE', '', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['success', 'SUCCESS', 'Success', 'succes', 'succesful'],queries = ['success', 'SUCCESS', 'Success', 'succes', 'succesful', 'succesful']) == ['success', 'SUCCESS', 'Success', 'succes', 'succesful', 'succesful']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['success', 'SUCCESS', 'Success', 'succes', 'succesful'],queries = ['success', 'SUCCESS', 'Success', 'succes', 'succesful', 'succesful']) == ['success', 'SUCCESS', 'Success', 'succes', 'succesful', 'succesful']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['apple', 'orange', 'banana', 'grape', 'kiwi'],queries = ['Apple', 'ORANGE', 'BANANA', 'Grape', 'KIWI', 'aple', 'oranje', 'bananna', 'grapee', 'kiwii', 'appl', 'orang', 'banan', 'grap', 'kiw']) == ['apple', 'orange', 'banana', 'grape', 'kiwi', '', '', '', '', '', '', '', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['apple', 'orange', 'banana', 'grape', 'kiwi'],queries = ['Apple', 'ORANGE', 'BANANA', 'Grape', 'KIWI', 'aple', 'oranje', 'bananna', 'grapee', 'kiwii', 'appl', 'orang', 'banan', 'grap', 'kiw']) == ['apple', 'orange', 'banana', 'grape', 'kiwi', '', '', '', '', '', '', '', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['algorithm', 'ALGORITHM', 'AlGORITHM', 'alGORITHM'],queries = ['algorithm', 'ALGORITHM', 'AlGORITHM', 'alGORITHM', 'algorithM', 'algorithmm']) == ['algorithm', 'ALGORITHM', 'AlGORITHM', 'alGORITHM', 'algorithm', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['algorithm', 'ALGORITHM', 'AlGORITHM', 'alGORITHM'],queries = ['algorithm', 'ALGORITHM', 'AlGORITHM', 'alGORITHM', 'algorithM', 'algorithmm']) == ['algorithm', 'ALGORITHM', 'AlGORITHM', 'alGORITHM', 'algorithm', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['necessary', 'NECESSARY', 'Necessary', 'nessecary', 'nessecery'],queries = ['necessary', 'NECESSARY', 'Necessary', 'nessecary', 'nessecery', 'nessecery']) == ['necessary', 'NECESSARY', 'Necessary', 'nessecary', 'nessecery', 'nessecery']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['necessary', 'NECESSARY', 'Necessary', 'nessecary', 'nessecery'],queries = ['necessary', 'NECESSARY', 'Necessary', 'nessecary', 'nessecery', 'nessecery']) == ['necessary', 'NECESSARY', 'Necessary', 'nessecary', 'nessecery', 'nessecery']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['pneumonoultramicroscopicsilicovolcanoconiosis', 'pneumOnoultramicroscopicsilicovolcanoconiosis', 'Pneumonoultramicroscopicsilicovolcanoconiosis'],queries = ['pneumonoultramicroscopicsilicovolcanoconiosis', 'PNEUMONoultramicroscopicsilicovolcanoconiosis', 'pneumOnoultramicroscopicsilicovolcanoconiosis', 'PNEUMOnoultramicroscopicsilicovolcanoconiosis', 'pneumOnoultramicroscopicsilicovolcanoconiosa']) == ['pneumonoultramicroscopicsilicovolcanoconiosis', 'pneumonoultramicroscopicsilicovolcanoconiosis', 'pneumOnoultramicroscopicsilicovolcanoconiosis', 'pneumonoultramicroscopicsilicovolcanoconiosis', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['pneumonoultramicroscopicsilicovolcanoconiosis', 'pneumOnoultramicroscopicsilicovolcanoconiosis', 'Pneumonoultramicroscopicsilicovolcanoconiosis'],queries = ['pneumonoultramicroscopicsilicovolcanoconiosis', 'PNEUMONoultramicroscopicsilicovolcanoconiosis', 'pneumOnoultramicroscopicsilicovolcanoconiosis', 'PNEUMOnoultramicroscopicsilicovolcanoconiosis', 'pneumOnoultramicroscopicsilicovolcanoconiosa']) == ['pneumonoultramicroscopicsilicovolcanoconiosis', 'pneumonoultramicroscopicsilicovolcanoconiosis', 'pneumOnoultramicroscopicsilicovolcanoconiosis', 'pneumonoultramicroscopicsilicovolcanoconiosis', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['CompUter', 'compuTer', 'COMPUTer', 'compuTER', 'comPUTER', 'computER', 'COMputer', 'computeR'],queries = ['COMPUTER', 'computor', 'COMpuTer', 'compuTER', 'compUter', 'computerr']) == ['CompUter', 'CompUter', 'CompUter', 'compuTER', 'CompUter', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['CompUter', 'compuTer', 'COMPUTer', 'compuTER', 'comPUTER', 'computER', 'COMputer', 'computeR'],queries = ['COMPUTER', 'computor', 'COMpuTer', 'compuTER', 'compUter', 'computerr']) == ['CompUter', 'CompUter', 'CompUter', 'compuTER', 'CompUter', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['umbrella', 'Umbrella', 'UMBRELLA', 'umberella', 'UmbereLLa'],queries = ['umbrella', 'Umbrella', 'UMBRELLA', 'umberella', 'UmbereLLa', 'umbrrella', 'umbralla', 'umrellla', 'umbrela', 'umbrelal']) == ['umbrella', 'Umbrella', 'UMBRELLA', 'umberella', 'UmbereLLa', '', 'umbrella', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['umbrella', 'Umbrella', 'UMBRELLA', 'umberella', 'UmbereLLa'],queries = ['umbrella', 'Umbrella', 'UMBRELLA', 'umberella', 'UmbereLLa', 'umbrrella', 'umbralla', 'umrellla', 'umbrela', 'umbrelal']) == ['umbrella', 'Umbrella', 'UMBRELLA', 'umberella', 'UmbereLLa', '', 'umbrella', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['grape', 'Grape', 'GRape', 'gRAPE', 'grAPE'],queries = ['grape', 'Grape', 'GRape', 'gRAPE', 'grAPE', 'grapE', 'GrapeS']) == ['grape', 'Grape', 'GRape', 'gRAPE', 'grAPE', 'grape', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['grape', 'Grape', 'GRape', 'gRAPE', 'grAPE'],queries = ['grape', 'Grape', 'GRape', 'gRAPE', 'grAPE', 'grapE', 'GrapeS']) == ['grape', 'Grape', 'GRape', 'gRAPE', 'grAPE', 'grape', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['watermelon', 'Watermelon', 'WATERMELON', 'watERmelon', 'waterMELON'],queries = ['watermelon', 'Watermelon', 'WATERMELON', 'watERmelon', 'waterMELON', 'wtermelon', 'WATERMELLO', 'watermelonn', 'watermelont']) == ['watermelon', 'Watermelon', 'WATERMELON', 'watERmelon', 'waterMELON', '', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['watermelon', 'Watermelon', 'WATERMELON', 'watERmelon', 'waterMELON'],queries = ['watermelon', 'Watermelon', 'WATERMELON', 'watERmelon', 'waterMELON', 'wtermelon', 'WATERMELLO', 'watermelonn', 'watermelont']) == ['watermelon', 'Watermelon', 'WATERMELON', 'watERmelon', 'waterMELON', '', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['intelligence', 'Intelligence', 'INTELLIGENCE', 'intelligENce', 'intelligenCE', 'INTElligenCE'],queries = ['intelligence', 'Intelligence', 'INTELLIGENCE', 'intelligENce', 'intelligenCE', 'INTElligenCE', 'intelligenCe', 'INTElligenCe', 'INTElligence']) == ['intelligence', 'Intelligence', 'INTELLIGENCE', 'intelligENce', 'intelligenCE', 'INTElligenCE', 'intelligence', 'intelligence', 'intelligence']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['intelligence', 'Intelligence', 'INTELLIGENCE', 'intelligENce', 'intelligenCE', 'INTElligenCE'],queries = ['intelligence', 'Intelligence', 'INTELLIGENCE', 'intelligENce', 'intelligenCE', 'INTElligenCE', 'intelligenCe', 'INTElligenCe', 'INTElligence']) == ['intelligence', 'Intelligence', 'INTELLIGENCE', 'intelligENce', 'intelligenCE', 'INTElligenCE', 'intelligence', 'intelligence', 'intelligence']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['relationship', 'Relationship', 'RELATIONSHIP', 'relashionship', 'Relashionship'],queries = ['relationship', 'Relationship', 'RELATIONSHIP', 'relashionship', 'Relashionship', 'relaship', 'relashionships', 'Relashionships', 'RELashionship', 'relashionship']) == ['relationship', 'Relationship', 'RELATIONSHIP', 'relashionship', 'Relashionship', '', '', '', 'relashionship', 'relashionship']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['relationship', 'Relationship', 'RELATIONSHIP', 'relashionship', 'Relashionship'],queries = ['relationship', 'Relationship', 'RELATIONSHIP', 'relashionship', 'Relashionship', 'relaship', 'relashionships', 'Relashionships', 'RELashionship', 'relashionship']) == ['relationship', 'Relationship', 'RELATIONSHIP', 'relashionship', 'Relashionship', '', '', '', 'relashionship', 'relashionship']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['education', 'EDUCATION', 'eDucAtIoN', 'educatiOn', 'edUcatioN', 'edUcatioN', 'educAtiOn', 'edUcaTion', 'eDUCatiOn'],queries = ['education', 'EDUCATION', 'eDucAtIoN', 'educatiOn', 'edUcatioN', 'edUcatioN', 'educAtiOn', 'edUcaTion', 'eDUCatiOn', 'educatioN']) == ['education', 'EDUCATION', 'eDucAtIoN', 'educatiOn', 'edUcatioN', 'edUcatioN', 'educAtiOn', 'edUcaTion', 'eDUCatiOn', 'education']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['education', 'EDUCATION', 'eDucAtIoN', 'educatiOn', 'edUcatioN', 'edUcatioN', 'educAtiOn', 'edUcaTion', 'eDUCatiOn'],queries = ['education', 'EDUCATION', 'eDucAtIoN', 'educatiOn', 'edUcatioN', 'edUcatioN', 'educAtiOn', 'edUcaTion', 'eDUCatiOn', 'educatioN']) == ['education', 'EDUCATION', 'eDucAtIoN', 'educatiOn', 'edUcatioN', 'edUcatioN', 'educAtiOn', 'edUcaTion', 'eDUCatiOn', 'education']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['elephant', 'Elephant', 'elePHant', 'ELEPHANT'],queries = ['elephant', 'Elephant', 'elePHant', 'ELEPHANT', 'elphant', 'ELPHNT', 'elefant', 'elphantt']) == ['elephant', 'Elephant', 'elePHant', 'ELEPHANT', '', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['elephant', 'Elephant', 'elePHant', 'ELEPHANT'],queries = ['elephant', 'Elephant', 'elePHant', 'ELEPHANT', 'elphant', 'ELPHNT', 'elefant', 'elphantt']) == ['elephant', 'Elephant', 'elePHant', 'ELEPHANT', '', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['developer', 'DEVELOPER', 'DevEloPer', 'develoPER', 'develoPer', 'DEveloPer'],queries = ['developer', 'DEVELOPER', 'DevEloPer', 'develoPER', 'develoPer', 'DEveloPer', 'devEloPer', 'DEvelOpEr']) == ['developer', 'DEVELOPER', 'DevEloPer', 'develoPER', 'develoPer', 'DEveloPer', 'developer', 'developer']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['developer', 'DEVELOPER', 'DevEloPer', 'develoPER', 'develoPer', 'DEveloPer'],queries = ['developer', 'DEVELOPER', 'DevEloPer', 'develoPER', 'develoPer', 'DEveloPer', 'devEloPer', 'DEvelOpEr']) == ['developer', 'DEVELOPER', 'DevEloPer', 'develoPER', 'develoPer', 'DEveloPer', 'developer', 'developer']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['flying', 'FLYING', 'FlyIng', 'FLyInG', 'fLyInG', 'FLYing'],queries = ['flying', 'FLYING', 'flyIng', 'FLyInG', 'fLyInG', 'FLYing', 'FLyInG', 'FLYINGg', 'FLYINGgg']) == ['flying', 'FLYING', 'flying', 'FLyInG', 'fLyInG', 'FLYing', 'FLyInG', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['flying', 'FLYING', 'FlyIng', 'FLyInG', 'fLyInG', 'FLYing'],queries = ['flying', 'FLYING', 'flyIng', 'FLyInG', 'fLyInG', 'FLYing', 'FLyInG', 'FLYINGg', 'FLYINGgg']) == ['flying', 'FLYING', 'flying', 'FLyInG', 'fLyInG', 'FLYing', 'FLyInG', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['algorithm', 'algoritm', 'algorithmic', 'algorithem', 'algoritm', 'algorit', 'algorithmically'],queries = ['Algorithm', 'Algoritm', 'Algorithmic', 'Algorithem', 'Algoritm', 'Algorit', 'Algorithmically', 'alorithm', 'algrthm', 'algorithmc', 'algrthm', 'algrthm', 'algorithmiclly', 'alorithm', 'algrthm', 'algorithmc', 'algrthm', 'algrthm', 'algorithmc', 'alorithm', 'algrthm', 'algorithmc', 'algrthm', 'algrthm', 'algorithmc']) == ['algorithm', 'algoritm', 'algorithmic', 'algorithem', 'algoritm', 'algorit', 'algorithmically', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['algorithm', 'algoritm', 'algorithmic', 'algorithem', 'algoritm', 'algorit', 'algorithmically'],queries = ['Algorithm', 'Algoritm', 'Algorithmic', 'Algorithem', 'Algoritm', 'Algorit', 'Algorithmically', 'alorithm', 'algrthm', 'algorithmc', 'algrthm', 'algrthm', 'algorithmiclly', 'alorithm', 'algrthm', 'algorithmc', 'algrthm', 'algrthm', 'algorithmc', 'alorithm', 'algrthm', 'algorithmc', 'algrthm', 'algrthm', 'algorithmc']) == ['algorithm', 'algoritm', 'algorithmic', 'algorithem', 'algoritm', 'algorit', 'algorithmically', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['fantastic', 'Fantastic', 'FANTASTIC', 'fantastiv', 'Fantastiv'],queries = ['fantastic', 'Fantastic', 'FANTASTIC', 'fantastiv', 'Fantastiv', 'fantasticv', 'fantastivv', 'Fantastiv', 'fantasticIv', 'FANTASTIc']) == ['fantastic', 'Fantastic', 'FANTASTIC', 'fantastiv', 'Fantastiv', '', '', 'Fantastiv', '', 'fantastic']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['fantastic', 'Fantastic', 'FANTASTIC', 'fantastiv', 'Fantastiv'],queries = ['fantastic', 'Fantastic', 'FANTASTIC', 'fantastiv', 'Fantastiv', 'fantasticv', 'fantastivv', 'Fantastiv', 'fantasticIv', 'FANTASTIc']) == ['fantastic', 'Fantastic', 'FANTASTIC', 'fantastiv', 'Fantastiv', '', '', 'Fantastiv', '', 'fantastic']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['important', 'IMPORTANT', 'Important', 'imporant', 'impotant'],queries = ['important', 'IMPORTANT', 'Important', 'imporant', 'impotant', 'imporant']) == ['important', 'IMPORTANT', 'Important', 'imporant', 'impotant', 'imporant']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['important', 'IMPORTANT', 'Important', 'imporant', 'impotant'],queries = ['important', 'IMPORTANT', 'Important', 'imporant', 'impotant', 'imporant']) == ['important', 'IMPORTANT', 'Important', 'imporant', 'impotant', 'imporant']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['machine', 'MACHINE', 'MachInE', 'MACHiNe'],queries = ['machine', 'MACHINE', 'MachInE', 'MACHiNe', 'machines', 'MACHINES', 'MachInES', 'MACHiNES', 'machinne']) == ['machine', 'MACHINE', 'MachInE', 'MACHiNe', '', '', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['machine', 'MACHINE', 'MachInE', 'MACHiNe'],queries = ['machine', 'MACHINE', 'MachInE', 'MACHiNe', 'machines', 'MACHINES', 'MachInES', 'MACHiNES', 'machinne']) == ['machine', 'MACHINE', 'MachInE', 'MACHiNe', '', '', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['community', 'COMMUNITY', 'Community', 'commuinty', 'communiti'],queries = ['community', 'COMMUNITY', 'Community', 'commuinty', 'communiti', 'commuinty']) == ['community', 'COMMUNITY', 'Community', 'commuinty', 'communiti', 'commuinty']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['community', 'COMMUNITY', 'Community', 'commuinty', 'communiti'],queries = ['community', 'COMMUNITY', 'Community', 'commuinty', 'communiti', 'commuinty']) == ['community', 'COMMUNITY', 'Community', 'commuinty', 'communiti', 'commuinty']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['orchid', 'Orchid', 'ORCHID', 'orchd', 'orhid', 'orckid', 'orchidd'],queries = ['orchid', 'Orchid', 'ORCHID', 'orchd', 'orhid', 'orckid', 'orchidd', 'orchiddd', 'orchidd', 'orchidds']) == ['orchid', 'Orchid', 'ORCHID', 'orchd', 'orhid', 'orckid', 'orchidd', '', 'orchidd', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['orchid', 'Orchid', 'ORCHID', 'orchd', 'orhid', 'orckid', 'orchidd'],queries = ['orchid', 'Orchid', 'ORCHID', 'orchd', 'orhid', 'orckid', 'orchidd', 'orchiddd', 'orchidd', 'orchidds']) == ['orchid', 'Orchid', 'ORCHID', 'orchd', 'orhid', 'orckid', 'orchidd', '', 'orchidd', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['grape', 'Grape', 'GRAPE', 'grapefruit', 'GrapeFruit'],queries = ['grape', 'Grape', 'GRAPE', 'grapefruit', 'GrapeFruit', 'grApE', 'Grapefruit', 'grapeFruit', 'GRape', 'grapeFruitS']) == ['grape', 'Grape', 'GRAPE', 'grapefruit', 'GrapeFruit', 'grape', 'grapefruit', 'grapefruit', 'grape', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['grape', 'Grape', 'GRAPE', 'grapefruit', 'GrapeFruit'],queries = ['grape', 'Grape', 'GRAPE', 'grapefruit', 'GrapeFruit', 'grApE', 'Grapefruit', 'grapeFruit', 'GRape', 'grapeFruitS']) == ['grape', 'Grape', 'GRAPE', 'grapefruit', 'GrapeFruit', 'grape', 'grapefruit', 'grapefruit', 'grape', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['intelligent', 'Intelligent', 'INTELLIGENT', 'inteligent', 'inteligents'],queries = ['intelligent', 'Intelligent', 'INTELLIGENT', 'inteligent', 'inteligents', 'intilignt']) == ['intelligent', 'Intelligent', 'INTELLIGENT', 'inteligent', 'inteligents', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['intelligent', 'Intelligent', 'INTELLIGENT', 'inteligent', 'inteligents'],queries = ['intelligent', 'Intelligent', 'INTELLIGENT', 'inteligent', 'inteligents', 'intilignt']) == ['intelligent', 'Intelligent', 'INTELLIGENT', 'inteligent', 'inteligents', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['aabbcc', 'abc', 'aebec', 'accbba', 'aabbccaa'],queries = ['aabbcc', 'abc', 'aebec', 'accbba', 'aabbccaa', 'AABBCC', 'ABC', 'AEBEC', 'ACCBBA', 'AABBCCAA', 'aabbc', 'abcc', 'aebc', 'accbb', 'aabbc', 'abcc', 'aebc', 'accbb', 'aabbc', 'abcc', 'aebc', 'accbb', 'aabbc', 'abcc', 'aebc', 'accbb', 'aabbc', 'abcc', 'aebc', 'accbb']) == ['aabbcc', 'abc', 'aebec', 'accbba', 'aabbccaa', 'aabbcc', 'abc', 'aebec', 'accbba', 'aabbccaa', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['aabbcc', 'abc', 'aebec', 'accbba', 'aabbccaa'],queries = ['aabbcc', 'abc', 'aebec', 'accbba', 'aabbccaa', 'AABBCC', 'ABC', 'AEBEC', 'ACCBBA', 'AABBCCAA', 'aabbc', 'abcc', 'aebc', 'accbb', 'aabbc', 'abcc', 'aebc', 'accbb', 'aabbc', 'abcc', 'aebc', 'accbb', 'aabbc', 'abcc', 'aebc', 'accbb', 'aabbc', 'abcc', 'aebc', 'accbb']) == ['aabbcc', 'abc', 'aebec', 'accbba', 'aabbccaa', 'aabbcc', 'abc', 'aebec', 'accbba', 'aabbccaa', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['water', 'Water', 'WATER', 'waTer', 'wateR', 'watER', 'wAtEr', 'waTEr'],queries = ['water', 'Water', 'WATER', 'waTer', 'wateR', 'watER', 'wAtEr', 'waTEr', 'wateR', 'waTer', 'watER', 'wAtEr', 'waTEr', 'wAter']) == ['water', 'Water', 'WATER', 'waTer', 'wateR', 'watER', 'wAtEr', 'waTEr', 'wateR', 'waTer', 'watER', 'wAtEr', 'waTEr', 'water']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['water', 'Water', 'WATER', 'waTer', 'wateR', 'watER', 'wAtEr', 'waTEr'],queries = ['water', 'Water', 'WATER', 'waTer', 'wateR', 'watER', 'wAtEr', 'waTEr', 'wateR', 'waTer', 'watER', 'wAtEr', 'waTEr', 'wAter']) == ['water', 'Water', 'WATER', 'waTer', 'wateR', 'watER', 'wAtEr', 'waTEr', 'wateR', 'waTer', 'watER', 'wAtEr', 'waTEr', 'water']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['banana', 'Banana', 'BANANA', 'banAna'],queries = ['banana', 'Banana', 'BANANA', 'banAna', 'BaNANA', 'bAnAnA', 'bananA', 'BaNANa']) == ['banana', 'Banana', 'BANANA', 'banAna', 'banana', 'banana', 'banana', 'banana']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['banana', 'Banana', 'BANANA', 'banAna'],queries = ['banana', 'Banana', 'BANANA', 'banAna', 'BaNANA', 'bAnAnA', 'bananA', 'BaNANa']) == ['banana', 'Banana', 'BANANA', 'banAna', 'banana', 'banana', 'banana', 'banana']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['umbrella', 'Umbrella', 'uMbReLlA', 'UMbrella'],queries = ['umbrella', 'Umbrella', 'uMbReLlA', 'UMbrella', 'umbrellA', 'UmBrella', 'UMBRELLA', 'umBRELLa', 'umbrela']) == ['umbrella', 'Umbrella', 'uMbReLlA', 'UMbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['umbrella', 'Umbrella', 'uMbReLlA', 'UMbrella'],queries = ['umbrella', 'Umbrella', 'uMbReLlA', 'UMbrella', 'umbrellA', 'UmBrella', 'UMBRELLA', 'umBRELLa', 'umbrela']) == ['umbrella', 'Umbrella', 'uMbReLlA', 'UMbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['environment', 'ENVIRONMENT', 'Environment', 'enviroment', 'evniroment'],queries = ['environment', 'ENVIRONMENT', 'Environment', 'enviroment', 'evniroment', 'envirnoment']) == ['environment', 'ENVIRONMENT', 'Environment', 'enviroment', 'evniroment', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['environment', 'ENVIRONMENT', 'Environment', 'enviroment', 'evniroment'],queries = ['environment', 'ENVIRONMENT', 'Environment', 'enviroment', 'evniroment', 'envirnoment']) == ['environment', 'ENVIRONMENT', 'Environment', 'enviroment', 'evniroment', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['umbrella', 'uMBrElLa', 'UMBRELLA', 'umbrellA'],queries = ['umbrella', 'uMBrElLa', 'UMBRELLA', 'umbrellA', 'umbrellaA', 'UMBRELLAa', 'uMBrElLaa', 'umbrellaa', 'umbrellaAA']) == ['umbrella', 'uMBrElLa', 'UMBRELLA', 'umbrellA', '', '', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['umbrella', 'uMBrElLa', 'UMBRELLA', 'umbrellA'],queries = ['umbrella', 'uMBrElLa', 'UMBRELLA', 'umbrellA', 'umbrellaA', 'UMBRELLAa', 'uMBrElLaa', 'umbrellaa', 'umbrellaAA']) == ['umbrella', 'uMBrElLa', 'UMBRELLA', 'umbrellA', '', '', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['umbrella', 'UMBRELLA', 'Umbrella', 'umBrella'],queries = ['Umbrella', 'umbrella', 'UMBRELLA', 'uMBRELLA', 'umbralla', 'umbrellaa']) == ['Umbrella', 'umbrella', 'UMBRELLA', 'umbrella', 'umbrella', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['umbrella', 'UMBRELLA', 'Umbrella', 'umBrella'],queries = ['Umbrella', 'umbrella', 'UMBRELLA', 'uMBRELLA', 'umbralla', 'umbrellaa']) == ['Umbrella', 'umbrella', 'UMBRELLA', 'umbrella', 'umbrella', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['education', 'Education', 'EDUCATION', 'educatin', 'Educatin', 'educatiOn'],queries = ['education', 'Education', 'EDUCATION', 'educatin', 'Educatin', 'educatiOn', 'edUcation', 'educAtion', 'educatiOns', 'educatiOn']) == ['education', 'Education', 'EDUCATION', 'educatin', 'Educatin', 'educatiOn', 'education', 'education', '', 'educatiOn']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['education', 'Education', 'EDUCATION', 'educatin', 'Educatin', 'educatiOn'],queries = ['education', 'Education', 'EDUCATION', 'educatin', 'Educatin', 'educatiOn', 'edUcation', 'educAtion', 'educatiOns', 'educatiOn']) == ['education', 'Education', 'EDUCATION', 'educatin', 'Educatin', 'educatiOn', 'education', 'education', '', 'educatiOn']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['rhythm', 'Rhythm', 'RYTHM', 'rhythem', 'rythum'],queries = ['rhythm', 'Rhythm', 'RYTHM', 'rhythem', 'rythum', 'rhythmm', 'rhyth', 'rythmm', 'rhythmz', 'rhythmzz']) == ['rhythm', 'Rhythm', 'RYTHM', 'rhythem', 'rythum', '', '', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['rhythm', 'Rhythm', 'RYTHM', 'rhythem', 'rythum'],queries = ['rhythm', 'Rhythm', 'RYTHM', 'rhythem', 'rythum', 'rhythmm', 'rhyth', 'rythmm', 'rhythmz', 'rhythmzz']) == ['rhythm', 'Rhythm', 'RYTHM', 'rhythem', 'rythum', '', '', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['sequence', 'Sequence', 'SEQUENCE', 'sequnce', 'Sequnce', 'sequeNce'],queries = ['sequence', 'Sequence', 'SEQUENCE', 'sequnce', 'Sequnce', 'sequeNce', 'sequnce', 'Sequense', 'SEQUENSe', 'sequenze']) == ['sequence', 'Sequence', 'SEQUENCE', 'sequnce', 'Sequnce', 'sequeNce', 'sequnce', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['sequence', 'Sequence', 'SEQUENCE', 'sequnce', 'Sequnce', 'sequeNce'],queries = ['sequence', 'Sequence', 'SEQUENCE', 'sequnce', 'Sequnce', 'sequeNce', 'sequnce', 'Sequense', 'SEQUENSe', 'sequenze']) == ['sequence', 'Sequence', 'SEQUENCE', 'sequnce', 'Sequnce', 'sequeNce', 'sequnce', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['communication', 'Communication', 'COMMUNICATION', 'commnication', 'Commnication'],queries = ['communication', 'Communication', 'COMMUNICATION', 'commnication', 'Commnication', 'communiCation', 'commNicAtion', 'ComMunication', 'COMMunIcAtion', 'communIcAtion']) == ['communication', 'Communication', 'COMMUNICATION', 'commnication', 'Commnication', 'communication', 'commnication', 'communication', 'communication', 'communication']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['communication', 'Communication', 'COMMUNICATION', 'commnication', 'Commnication'],queries = ['communication', 'Communication', 'COMMUNICATION', 'commnication', 'Commnication', 'communiCation', 'commNicAtion', 'ComMunication', 'COMMunIcAtion', 'communIcAtion']) == ['communication', 'Communication', 'COMMUNICATION', 'commnication', 'Commnication', 'communication', 'commnication', 'communication', 'communication', 'communication']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['quIckBrOwnFox', 'QUICKBROWNFOX', 'QuickBrownFox', 'quiCKBrOwnFoX', 'QUICKbrownfox'],queries = ['quickbrownfox', 'QUICKBROWNFOX', 'QuiCKBrOwnFoX', 'QUICKbrownfox', 'quickBRownfox', 'quickbrownfoX', 'quickbrOwnfox', 'QUICKBROWNfOX']) == ['quIckBrOwnFox', 'QUICKBROWNFOX', 'quIckBrOwnFox', 'QUICKbrownfox', 'quIckBrOwnFox', 'quIckBrOwnFox', 'quIckBrOwnFox', 'quIckBrOwnFox']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['quIckBrOwnFox', 'QUICKBROWNFOX', 'QuickBrownFox', 'quiCKBrOwnFoX', 'QUICKbrownfox'],queries = ['quickbrownfox', 'QUICKBROWNFOX', 'QuiCKBrOwnFoX', 'QUICKbrownfox', 'quickBRownfox', 'quickbrownfoX', 'quickbrOwnfox', 'QUICKBROWNfOX']) == ['quIckBrOwnFox', 'QUICKBROWNFOX', 'quIckBrOwnFox', 'QUICKbrownfox', 'quIckBrOwnFox', 'quIckBrOwnFox', 'quIckBrOwnFox', 'quIckBrOwnFox']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['elephant', 'Elephant', 'ELEPHANT', 'eLEPHANT', 'eLEpHANT'],queries = ['elephant', 'Elephant', 'ELEPHANT', 'eLEPHANT', 'eLEpHANT', 'elephants', 'Elephants', 'ELEPHANTs', 'eLEPHANTs']) == ['elephant', 'Elephant', 'ELEPHANT', 'eLEPHANT', 'eLEpHANT', '', '', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['elephant', 'Elephant', 'ELEPHANT', 'eLEPHANT', 'eLEpHANT'],queries = ['elephant', 'Elephant', 'ELEPHANT', 'eLEPHANT', 'eLEpHANT', 'elephants', 'Elephants', 'ELEPHANTs', 'eLEPHANTs']) == ['elephant', 'Elephant', 'ELEPHANT', 'eLEPHANT', 'eLEpHANT', '', '', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['Supercalifragilisticexpialidocious', 'supercalifragilisticexpialidocious', 'SuPeRcAlIfRaGiLiStIcExPiAlIdOcIoUs', 'SUPErcALifRAGilistiCexpiALIdOcIOUs'],queries = ['supercalifragilisticexpialidocious', 'SUPErcALifRAGilistiCexpiALIdOcIOUs', 'SuPeRcAlIfRaGiLiStIcExPiAlIdOcIoUs', 'supercalifragilisticexpialidociosa']) == ['supercalifragilisticexpialidocious', 'SUPErcALifRAGilistiCexpiALIdOcIOUs', 'SuPeRcAlIfRaGiLiStIcExPiAlIdOcIoUs', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['Supercalifragilisticexpialidocious', 'supercalifragilisticexpialidocious', 'SuPeRcAlIfRaGiLiStIcExPiAlIdOcIoUs', 'SUPErcALifRAGilistiCexpiALIdOcIOUs'],queries = ['supercalifragilisticexpialidocious', 'SUPErcALifRAGilistiCexpiALIdOcIOUs', 'SuPeRcAlIfRaGiLiStIcExPiAlIdOcIoUs', 'supercalifragilisticexpialidociosa']) == ['supercalifragilisticexpialidocious', 'SUPErcALifRAGilistiCexpiALIdOcIOUs', 'SuPeRcAlIfRaGiLiStIcExPiAlIdOcIoUs', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['ambiguity', 'ambiguos', 'Ambiguity', 'AMBIGUITY', 'ambiguous', 'amgibuity'],queries = ['ambiguity', 'AMBIGUITY', 'Ambiguity', 'ambiguous', 'AmbiguiTy', 'amgibuity']) == ['ambiguity', 'AMBIGUITY', 'Ambiguity', 'ambiguous', 'ambiguity', 'amgibuity']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['ambiguity', 'ambiguos', 'Ambiguity', 'AMBIGUITY', 'ambiguous', 'amgibuity'],queries = ['ambiguity', 'AMBIGUITY', 'Ambiguity', 'ambiguous', 'AmbiguiTy', 'amgibuity']) == ['ambiguity', 'AMBIGUITY', 'Ambiguity', 'ambiguous', 'ambiguity', 'amgibuity']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['supercalifragilisticexpialidocious', 'SUPERCALIFRAGILISTICEXPIALIDOCIOUS', 'Supercalifragilisticexpialidocious', 'suPercalifragilisticexpialidocious'],queries = ['supercalifragilisticexpialidocious', 'SUPERCALIFRAGILISTICEXPIALIDOCIOUS', 'Supercalifragilisticexpialidocious', 'suPercalifragilisticexpialidocious', 'supercalifragilisticexpialido', 'supercalifragilisticexpialidocius']) == ['supercalifragilisticexpialidocious', 'SUPERCALIFRAGILISTICEXPIALIDOCIOUS', 'Supercalifragilisticexpialidocious', 'suPercalifragilisticexpialidocious', '', '']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['supercalifragilisticexpialidocious', 'SUPERCALIFRAGILISTICEXPIALIDOCIOUS', 'Supercalifragilisticexpialidocious', 'suPercalifragilisticexpialidocious'],queries = ['supercalifragilisticexpialidocious', 'SUPERCALIFRAGILISTICEXPIALIDOCIOUS', 'Supercalifragilisticexpialidocious', 'suPercalifragilisticexpialidocious', 'supercalifragilisticexpialido', 'supercalifragilisticexpialidocius']) == ['supercalifragilisticexpialidocious', 'SUPERCALIFRAGILISTICEXPIALIDOCIOUS', 'Supercalifragilisticexpialidocious', 'suPercalifragilisticexpialidocious', '', '']: {e}')
    
    total += 1
    try:
        result = candidate(wordlist = ['algorithm', 'AlgorithM', 'ALGORITHM', 'algoritm', 'Algoritm'],queries = ['algorithm', 'AlgorithM', 'ALGORITHM', 'algoritm', 'Algoritm', 'algorithM', 'algoritm', 'AlgorIthm', 'algoRitm', 'AlgoRithm']) == ['algorithm', 'AlgorithM', 'ALGORITHM', 'algoritm', 'Algoritm', 'algorithm', 'algoritm', 'algorithm', 'algoritm', 'algorithm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(wordlist = ['algorithm', 'AlgorithM', 'ALGORITHM', 'algoritm', 'Algoritm'],queries = ['algorithm', 'AlgorithM', 'ALGORITHM', 'algoritm', 'Algoritm', 'algorithM', 'algoritm', 'AlgorIthm', 'algoRitm', 'AlgoRithm']) == ['algorithm', 'AlgorithM', 'ALGORITHM', 'algoritm', 'Algoritm', 'algorithm', 'algoritm', 'algorithm', 'algoritm', 'algorithm']: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(wordlist = ['aeiou', 'AEIOU'],queries = ['aeio', 'aeiou', 'AEIOU', 'eioua']) == ['', 'aeiou', 'AEIOU', 'aeiou']
    assert candidate(wordlist = ['aaaaa', 'Aaaaa'],queries = ['Aaaaa', 'aaaaa', 'aaAaa', 'aAaaa', 'AaAaa']) == ['Aaaaa', 'aaaaa', 'aaaaa', 'aaaaa', 'aaaaa']
    assert candidate(wordlist = ['yellow'],queries = ['YellOw']) == ['yellow']
    assert candidate(wordlist = ['apple', 'Apple', 'apples'],queries = ['apples', 'APPLES', 'applesa', 'applee']) == ['apples', 'apples', '', '']
    assert candidate(wordlist = ['KiTe', 'kite', 'hare', 'Hare'],queries = ['kite', 'Kite', 'KiTe', 'Hare', 'HARE', 'Hear', 'hear', 'keti', 'keet', 'keto']) == ['kite', 'KiTe', 'KiTe', 'Hare', 'hare', '', '', 'KiTe', '', 'KiTe']
    assert candidate(wordlist = ['onomatopoeia', 'ONOMATOPOEIA', 'Onomatopoeia', 'oNomatopoeia'],queries = ['onomatopoeia', 'ONOMATOPOEIA', 'Onomatopoeia', 'oNomatopoeia', 'onomatopeiaa', 'onomatopoei']) == ['onomatopoeia', 'ONOMATOPOEIA', 'Onomatopoeia', 'oNomatopoeia', 'onomatopoeia', '']
    assert candidate(wordlist = ['umbrella', 'university', 'underground', 'unicorn', 'uppercut'],queries = ['UMBRELLA', 'UNIVERSITY', 'UNDERGROUND', 'UNICORN', 'UPPERCUT', 'umbrlla', 'universit', 'undergroand', 'unicor', 'upperct', 'Umbrella', 'Unversity', 'Uderground', 'Uinicorn', 'Uppercut']) == ['umbrella', 'university', 'underground', 'unicorn', 'uppercut', '', '', 'underground', '', '', 'umbrella', '', '', '', 'uppercut']
    assert candidate(wordlist = ['bicycle', 'Bicycle', 'BIcycle', 'bIcycle', 'biCycle', 'bicyCLE'],queries = ['bicycle', 'Bicycle', 'BIcycle', 'bIcycle', 'biCycle', 'bicyCLE', 'bicyclE', 'bicyclE', 'bicycLe', 'bicyclE', 'bicycleE']) == ['bicycle', 'Bicycle', 'BIcycle', 'bIcycle', 'biCycle', 'bicyCLE', 'bicycle', 'bicycle', 'bicycle', 'bicycle', '']
    assert candidate(wordlist = ['dictionary', 'Dictionary', 'DICTIONARY', 'DictIoNaRy'],queries = ['dictioNary', 'DICTIONARY', 'dictionary', 'dIctionarY', 'DictioNaryy', 'dictionar']) == ['dictionary', 'DICTIONARY', 'dictionary', 'dictionary', '', '']
    assert candidate(wordlist = ['banana', 'Banana', 'BANANA', 'banAnA'],queries = ['banana', 'Banana', 'BANANA', 'banAnA', 'bananA', 'bananaa', 'BANANAS']) == ['banana', 'Banana', 'BANANA', 'banAnA', 'banana', '', '']
    assert candidate(wordlist = ['interview', 'INTERVIEW', 'Interview', 'inTerView'],queries = ['interview', 'INTERVIEW', 'Interview', 'inTerView', 'interviw', 'intervew']) == ['interview', 'INTERVIEW', 'Interview', 'inTerView', '', '']
    assert candidate(wordlist = ['university', 'UNIVERSITY', 'University', 'universitry', 'universitie'],queries = ['university', 'UNIVERSITY', 'University', 'universitry', 'universitie', 'universitry']) == ['university', 'UNIVERSITY', 'University', 'universitry', 'universitie', 'universitry']
    assert candidate(wordlist = ['AbCdE', 'abcdE', 'aBcDe', 'abCDE', 'abcde'],queries = ['AbCdE', 'Abcde', 'abcde', 'aBcDe', 'abCDE', 'ABCDE', 'abcde', 'AbCdF', 'AbCdEe']) == ['AbCdE', 'AbCdE', 'abcde', 'aBcDe', 'abCDE', 'AbCdE', 'abcde', '', '']
    assert candidate(wordlist = ['AbCdE', 'abCDe', 'aBcDe', 'ABCDe', 'abcde', 'aBcde', 'abCde', 'ABCDE'],queries = ['abcde', 'ABCDE', 'AbCdE', 'abcde', 'aBcDe', 'ABcDe', 'abcdef', 'aBcde', 'ABCDe', 'abCDe']) == ['abcde', 'ABCDE', 'AbCdE', 'abcde', 'aBcDe', 'AbCdE', '', 'aBcde', 'ABCDe', 'abCDe']
    assert candidate(wordlist = ['xylophone', 'Xylophone', 'XYLOPHONE', 'xYlOpHoNe'],queries = ['xylophone', 'Xylophone', 'XYLOPHONE', 'xYlOpHoNe', 'xylopon', 'xylofon']) == ['xylophone', 'Xylophone', 'XYLOPHONE', 'xYlOpHoNe', '', '']
    assert candidate(wordlist = ['umbrella', 'UmBrella', 'Umbrella', 'UMBRELLA'],queries = ['UMBRELLA', 'umbrELLA', 'umbrelLA', 'umbrella', 'UmBrelLA', 'UMBRELLAA', 'umbrellaa']) == ['UMBRELLA', 'umbrella', 'umbrella', 'umbrella', 'umbrella', '', '']
    assert candidate(wordlist = ['umbrella', 'Umbrella', 'UMBRELLA', 'umbralla', 'Umbralla'],queries = ['umbrella', 'Umbrella', 'UMBRELLA', 'umbralla', 'Umbralla', 'umbrallaS', 'umbrellA', 'UmbrallA', 'UMbralla', 'UmbrAlla']) == ['umbrella', 'Umbrella', 'UMBRELLA', 'umbralla', 'Umbralla', '', 'umbrella', 'umbralla', 'umbralla', 'umbralla']
    assert candidate(wordlist = ['beautiful', 'Beautiful', 'BEAUTIFUL', 'beautifull', 'beautifu', 'beautifulll'],queries = ['beautiful', 'Beautiful', 'BEAUTIFUL', 'beautifull', 'beautifu', 'beautifulll', 'beautifulll', 'beautifull', 'beautifuul', 'beautiul']) == ['beautiful', 'Beautiful', 'BEAUTIFUL', 'beautifull', 'beautifu', 'beautifulll', 'beautifulll', 'beautifull', '', '']
    assert candidate(wordlist = ['banana', 'Banana', 'BANANA', 'bandana', 'BandAna'],queries = ['banana', 'Banana', 'BANANA', 'bandana', 'BANDANA', 'bandanna', 'bandanna', 'bndn', 'bandn']) == ['banana', 'Banana', 'BANANA', 'bandana', 'bandana', '', '', '', '']
    assert candidate(wordlist = ['beautiful', 'BeAuTiFuL', 'BEautiful', 'bEAUtIfUl', 'bEAUtIFuL'],queries = ['beautiful', 'BeAuTiFuL', 'BEautiful', 'bEAUtIfUl', 'bEAUtIFuL', 'beautifuls', 'BeAuTiFuLs', 'BEautifuls', 'bEAUtIfUls']) == ['beautiful', 'BeAuTiFuL', 'BEautiful', 'bEAUtIfUl', 'bEAUtIFuL', '', '', '', '']
    assert candidate(wordlist = ['environment', 'ENVIRONMENT', 'EnViRonMeNt', 'ENvIrOnMeNt', 'ENvIrOnMeNT'],queries = ['environment', 'ENVIRONMENT', 'EnViRonMeNt', 'ENvIrOnMeNt', 'ENvIrOnMeNT', 'environments', 'ENVIRONMENTs', 'EnViRonMeNts', 'ENvIrOnMeNts']) == ['environment', 'ENVIRONMENT', 'EnViRonMeNt', 'ENvIrOnMeNt', 'ENvIrOnMeNT', '', '', '', '']
    assert candidate(wordlist = ['algorithm', 'Algorithm', 'ALGORITHM', 'algorithem', 'algoritum', 'algorith', 'algorithmmm'],queries = ['algorithm', 'Algorithm', 'ALGORITHM', 'algorithem', 'algoritum', 'algorith', 'algorithmmm', 'algorithmmm', 'algorithmm', 'algorithmm']) == ['algorithm', 'Algorithm', 'ALGORITHM', 'algorithem', 'algoritum', 'algorith', 'algorithmmm', 'algorithmmm', '', '']
    assert candidate(wordlist = ['education', 'environment', 'elevation', 'excavation', 'explanation'],queries = ['Education', 'Environment', 'Elevation', 'Excavation', 'Explanation', 'edication', 'enviroment', 'elevatoin', 'exacation', 'explanatoin', 'educatio', 'environmnt', 'elevatn', 'excavtn', 'explntion', 'educatoin', 'enivornment', 'elevtn', 'excavatn', 'explanatn', 'educati', 'environmt', 'elevtn', 'excavtn', 'explntn']) == ['education', 'environment', 'elevation', 'excavation', 'explanation', 'education', '', 'elevation', '', 'explanation', '', '', '', '', '', 'education', '', '', '', '', '', '', '', '', '']
    assert candidate(wordlist = ['education', 'EDUCATION', 'Education', 'edUcation'],queries = ['EDUCATION', 'education', 'Education', 'edUcation', 'educatiion', 'eduCation']) == ['EDUCATION', 'education', 'Education', 'edUcation', '', 'education']
    assert candidate(wordlist = ['elephant', 'ElEphant', 'ELEPHANT', 'elePHANT', 'eLePHANT'],queries = ['elephant', 'elePHANT', 'eLePHANT', 'elePHAN', 'ElePHAN', 'eLEPHAN', 'ELephAN', 'elePHANt']) == ['elephant', 'elePHANT', 'eLePHANT', '', '', '', '', 'elephant']
    assert candidate(wordlist = ['education', 'EDUCATION', 'EduCation', 'educate', 'educating'],queries = ['education', 'EDUCATION', 'EduCation', 'educate', 'educatin', 'Educating']) == ['education', 'EDUCATION', 'EduCation', 'educate', '', 'educating']
    assert candidate(wordlist = ['elephant', 'giraffe', 'hippo', 'rhino', 'zebra', 'lemur'],queries = ['Elephant', 'Giraffe', 'Hippo', 'Rhino', 'Zebra', 'Lemur', 'elphant', 'giraff', 'hippo', 'rhin', 'zebr', 'lemr', 'elphantt', 'giraffe', 'hippp', 'rhinno', 'zebraa', 'lemur', 'elephant', 'giraffe', 'hippo', 'rhino', 'zebra', 'lemur', 'elephants', 'giraffes', 'hippos', 'rhinos', 'zebras', 'lemurs']) == ['elephant', 'giraffe', 'hippo', 'rhino', 'zebra', 'lemur', '', '', 'hippo', '', '', '', '', 'giraffe', '', '', '', 'lemur', 'elephant', 'giraffe', 'hippo', 'rhino', 'zebra', 'lemur', '', '', '', '', '', '']
    assert candidate(wordlist = ['algorithm', 'AlgoritHM', 'aLgoRitHm', 'alGoRiThM'],queries = ['algorithm', 'AlgoritHM', 'aLgoRitHm', 'alGoRiThM', 'algoriTHM', 'AlgoRiThM', 'aLGorIthM', 'AlGorIthM', 'algOrIthM']) == ['algorithm', 'AlgoritHM', 'aLgoRitHm', 'alGoRiThM', 'algorithm', 'algorithm', 'algorithm', 'algorithm', 'algorithm']
    assert candidate(wordlist = ['education', 'EDUCATION', 'EducAtion', 'eDUCAtion'],queries = ['EDUCATION', 'educAtion', 'eDUCAtion', 'EDucAtion', 'educAtioN', 'EDucAtioN', 'educatiOn', 'EDucatiOn']) == ['EDUCATION', 'education', 'eDUCAtion', 'education', 'education', 'education', 'education', 'education']
    assert candidate(wordlist = ['education', 'EDUCATION', 'EduCatiOn', 'eDUCaTIOn', 'EDuCAtIoN'],queries = ['education', 'EDUCATION', 'EduCatiOn', 'eDUCaTIOn', 'EDuCAtIoN', 'educations', 'EDUCATIONS', 'EduCatiOns', 'eDUCaTIOns']) == ['education', 'EDUCATION', 'EduCatiOn', 'eDUCaTIOn', 'EDuCAtIoN', '', '', '', '']
    assert candidate(wordlist = ['umbrella', 'uMBrElLa', 'UMBRELLA', 'umbrellA', 'umbralla'],queries = ['umbrella', 'uMBrElLa', 'UMBRELLA', 'umbrellA', 'umbralla', 'UMBRELLAA', 'uMBrElLAA', 'UMBRELLAAA', 'umbrallaA']) == ['umbrella', 'uMBrElLa', 'UMBRELLA', 'umbrellA', 'umbralla', '', '', '', '']
    assert candidate(wordlist = ['elephant', 'Elephant', 'ELEPHANT', 'elevnt', 'elphant', 'elefant', 'elephantt'],queries = ['elephant', 'Elephant', 'ELEPHANT', 'elevnt', 'elphant', 'elefant', 'elephantt', 'elphnt', 'elphntt', 'elphnta']) == ['elephant', 'Elephant', 'ELEPHANT', 'elevnt', 'elphant', 'elefant', 'elephantt', '', '', '']
    assert candidate(wordlist = ['environment', 'Environment', 'ENVIRONMENT', 'environmnt', 'Environmnt', 'environMent'],queries = ['environment', 'Environment', 'ENVIRONMENT', 'environmnt', 'Environmnt', 'environMent', 'environMnt', 'environmEnt', 'environmEnts', 'environmEnt']) == ['environment', 'Environment', 'ENVIRONMENT', 'environmnt', 'Environmnt', 'environMent', 'environmnt', 'environment', '', 'environment']
    assert candidate(wordlist = ['beautiful', 'Beautiful', 'BEAUTIFUL', 'beautifull', 'beautifu'],queries = ['beautiful', 'Beautiful', 'BEAUTIFUL', 'beautifull', 'beautifu', 'beautifull']) == ['beautiful', 'Beautiful', 'BEAUTIFUL', 'beautifull', 'beautifu', 'beautifull']
    assert candidate(wordlist = ['baNana', 'Banana', 'BANANA', 'baNANa'],queries = ['banana', 'BANANA', 'BaNaNa', 'bananA', 'baNANaa', 'bAnanaa']) == ['baNana', 'BANANA', 'baNana', 'baNana', '', '']
    assert candidate(wordlist = ['dictionary', 'Dictionary', 'DICTIONARY', 'dictionry', 'Dictionry'],queries = ['dictionary', 'Dictionary', 'DICTIONARY', 'dictionry', 'Dictionry', 'dictionryS', 'dictionryY', 'dictiOnary', 'dictioNary', 'dictionry']) == ['dictionary', 'Dictionary', 'DICTIONARY', 'dictionry', 'Dictionry', '', '', 'dictionary', 'dictionary', 'dictionry']
    assert candidate(wordlist = ['programming', 'Programming', 'PROGRAMMING', 'proGramMinG'],queries = ['programming', 'Programming', 'PROGRAMMING', 'proGramMinG', 'prograMMing', 'ProgramMiNG', 'PROgRaMMiNG', 'pRoGrAmMiNg', 'programmingg', 'proGramming']) == ['programming', 'Programming', 'PROGRAMMING', 'proGramMinG', 'programming', 'programming', 'programming', 'programming', '', 'programming']
    assert candidate(wordlist = ['keyboard', 'KeyboArD', 'KEYBOARD', 'keyboARd'],queries = ['keyboard', 'keyboarD', 'KEYBOArd', 'KEYboArd', 'keyboARd', 'KEYboARd', 'keyboArD', 'KEYBOArD']) == ['keyboard', 'keyboard', 'keyboard', 'keyboard', 'keyboARd', 'keyboard', 'keyboard', 'keyboard']
    assert candidate(wordlist = ['sequence', 'Sequence', 'SEQUENCE', 'sequense', 'sequnce', 'sequenec', 'sequencee'],queries = ['sequence', 'Sequence', 'SEQUENCE', 'sequense', 'sequnce', 'sequenec', 'sequencee', 'seqeunce', 'sequnce', 'sequnc']) == ['sequence', 'Sequence', 'SEQUENCE', 'sequense', 'sequnce', 'sequenec', 'sequencee', 'sequence', 'sequnce', '']
    assert candidate(wordlist = ['umbrella', 'Umbrella', 'UMBRELLA', 'UmBReLlA'],queries = ['umbrella', 'UMBRELLA', 'Umbrella', 'umBReLlA', 'Umbr3lla', 'umbrellaa', 'UMBRELLAA']) == ['umbrella', 'UMBRELLA', 'Umbrella', 'umbrella', '', '', '']
    assert candidate(wordlist = ['programming', 'ProgramMING', 'proGRaMMiNG', 'prograMMiNG', 'proGRammING'],queries = ['programming', 'ProgramMING', 'proGRaMMiNG', 'prograMMiNG', 'proGRammING', 'progrAMMING', 'prograMmING', 'progrAmmiNG']) == ['programming', 'ProgramMING', 'proGRaMMiNG', 'prograMMiNG', 'proGRammING', 'programming', 'programming', 'programming']
    assert candidate(wordlist = ['cAt', 'cAts', 'bAt', 'bat', 'bats', 'cAtBat'],queries = ['cats', 'CATS', 'cat', 'bat', 'bAts', 'CATBAT', 'caTbAt', 'batS', 'CAT', 'bAt']) == ['cAts', 'cAts', 'cAt', 'bat', 'bats', 'cAtBat', 'cAtBat', 'bats', 'cAt', 'bAt']
    assert candidate(wordlist = ['queue', 'Queue', 'QUEUE', 'qUeUe'],queries = ['queue', 'Queue', 'QUEUE', 'qUeUe', 'queuE', 'QUeUe', 'qUEUe', 'QUEue', 'quEUe', 'qUeue']) == ['queue', 'Queue', 'QUEUE', 'qUeUe', 'queue', 'queue', 'queue', 'queue', 'queue', 'queue']
    assert candidate(wordlist = ['kiwi', 'Kiwi', 'KIWI', 'kIWi', 'KiwI'],queries = ['kiwi', 'Kiwi', 'KIWI', 'kIWi', 'KiwI', 'kiw', 'KIW', 'kiwiwi', 'kiwii']) == ['kiwi', 'Kiwi', 'KIWI', 'kIWi', 'KiwI', '', '', '', '']
    assert candidate(wordlist = ['strawberry', 'Strawberry', 'STRAWBERRY', 'stRawberry', 'strAWberry', 'strawbERRY'],queries = ['strawberry', 'Strawberry', 'STRAWBERRY', 'stRawberry', 'strAWberry', 'strawbERRY', 'straw', 'strawberryy', 'strawberrrry']) == ['strawberry', 'Strawberry', 'STRAWBERRY', 'stRawberry', 'strAWberry', 'strawbERRY', '', '', '']
    assert candidate(wordlist = ['programming', 'PROGRAMMING', 'ProgRaMmInG', 'PROgRaMMiNg', 'pROgRaMMiNG'],queries = ['programming', 'PROGRAMMING', 'ProgRaMmInG', 'PROgRaMMiNg', 'pROgRaMMiNG', 'programmings', 'PROGRAMMINGs', 'ProgRaMmInGs', 'PROgRaMMiNgs']) == ['programming', 'PROGRAMMING', 'ProgRaMmInG', 'PROgRaMMiNg', 'pROgRaMMiNG', '', '', '', '']
    assert candidate(wordlist = ['orange', 'Orange', 'ORANGE', 'oRANGE', 'orANGE'],queries = ['orange', 'Orange', 'ORANGE', 'oRANGE', 'orANGE', 'orang', 'ORANG', 'oranje', 'orng']) == ['orange', 'Orange', 'ORANGE', 'oRANGE', 'orANGE', '', '', '', '']
    assert candidate(wordlist = ['success', 'SUCCESS', 'Success', 'succes', 'succesful'],queries = ['success', 'SUCCESS', 'Success', 'succes', 'succesful', 'succesful']) == ['success', 'SUCCESS', 'Success', 'succes', 'succesful', 'succesful']
    assert candidate(wordlist = ['apple', 'orange', 'banana', 'grape', 'kiwi'],queries = ['Apple', 'ORANGE', 'BANANA', 'Grape', 'KIWI', 'aple', 'oranje', 'bananna', 'grapee', 'kiwii', 'appl', 'orang', 'banan', 'grap', 'kiw']) == ['apple', 'orange', 'banana', 'grape', 'kiwi', '', '', '', '', '', '', '', '', '', '']
    assert candidate(wordlist = ['algorithm', 'ALGORITHM', 'AlGORITHM', 'alGORITHM'],queries = ['algorithm', 'ALGORITHM', 'AlGORITHM', 'alGORITHM', 'algorithM', 'algorithmm']) == ['algorithm', 'ALGORITHM', 'AlGORITHM', 'alGORITHM', 'algorithm', '']
    assert candidate(wordlist = ['necessary', 'NECESSARY', 'Necessary', 'nessecary', 'nessecery'],queries = ['necessary', 'NECESSARY', 'Necessary', 'nessecary', 'nessecery', 'nessecery']) == ['necessary', 'NECESSARY', 'Necessary', 'nessecary', 'nessecery', 'nessecery']
    assert candidate(wordlist = ['pneumonoultramicroscopicsilicovolcanoconiosis', 'pneumOnoultramicroscopicsilicovolcanoconiosis', 'Pneumonoultramicroscopicsilicovolcanoconiosis'],queries = ['pneumonoultramicroscopicsilicovolcanoconiosis', 'PNEUMONoultramicroscopicsilicovolcanoconiosis', 'pneumOnoultramicroscopicsilicovolcanoconiosis', 'PNEUMOnoultramicroscopicsilicovolcanoconiosis', 'pneumOnoultramicroscopicsilicovolcanoconiosa']) == ['pneumonoultramicroscopicsilicovolcanoconiosis', 'pneumonoultramicroscopicsilicovolcanoconiosis', 'pneumOnoultramicroscopicsilicovolcanoconiosis', 'pneumonoultramicroscopicsilicovolcanoconiosis', '']
    assert candidate(wordlist = ['CompUter', 'compuTer', 'COMPUTer', 'compuTER', 'comPUTER', 'computER', 'COMputer', 'computeR'],queries = ['COMPUTER', 'computor', 'COMpuTer', 'compuTER', 'compUter', 'computerr']) == ['CompUter', 'CompUter', 'CompUter', 'compuTER', 'CompUter', '']
    assert candidate(wordlist = ['umbrella', 'Umbrella', 'UMBRELLA', 'umberella', 'UmbereLLa'],queries = ['umbrella', 'Umbrella', 'UMBRELLA', 'umberella', 'UmbereLLa', 'umbrrella', 'umbralla', 'umrellla', 'umbrela', 'umbrelal']) == ['umbrella', 'Umbrella', 'UMBRELLA', 'umberella', 'UmbereLLa', '', 'umbrella', '', '', '']
    assert candidate(wordlist = ['grape', 'Grape', 'GRape', 'gRAPE', 'grAPE'],queries = ['grape', 'Grape', 'GRape', 'gRAPE', 'grAPE', 'grapE', 'GrapeS']) == ['grape', 'Grape', 'GRape', 'gRAPE', 'grAPE', 'grape', '']
    assert candidate(wordlist = ['watermelon', 'Watermelon', 'WATERMELON', 'watERmelon', 'waterMELON'],queries = ['watermelon', 'Watermelon', 'WATERMELON', 'watERmelon', 'waterMELON', 'wtermelon', 'WATERMELLO', 'watermelonn', 'watermelont']) == ['watermelon', 'Watermelon', 'WATERMELON', 'watERmelon', 'waterMELON', '', '', '', '']
    assert candidate(wordlist = ['intelligence', 'Intelligence', 'INTELLIGENCE', 'intelligENce', 'intelligenCE', 'INTElligenCE'],queries = ['intelligence', 'Intelligence', 'INTELLIGENCE', 'intelligENce', 'intelligenCE', 'INTElligenCE', 'intelligenCe', 'INTElligenCe', 'INTElligence']) == ['intelligence', 'Intelligence', 'INTELLIGENCE', 'intelligENce', 'intelligenCE', 'INTElligenCE', 'intelligence', 'intelligence', 'intelligence']
    assert candidate(wordlist = ['relationship', 'Relationship', 'RELATIONSHIP', 'relashionship', 'Relashionship'],queries = ['relationship', 'Relationship', 'RELATIONSHIP', 'relashionship', 'Relashionship', 'relaship', 'relashionships', 'Relashionships', 'RELashionship', 'relashionship']) == ['relationship', 'Relationship', 'RELATIONSHIP', 'relashionship', 'Relashionship', '', '', '', 'relashionship', 'relashionship']
    assert candidate(wordlist = ['education', 'EDUCATION', 'eDucAtIoN', 'educatiOn', 'edUcatioN', 'edUcatioN', 'educAtiOn', 'edUcaTion', 'eDUCatiOn'],queries = ['education', 'EDUCATION', 'eDucAtIoN', 'educatiOn', 'edUcatioN', 'edUcatioN', 'educAtiOn', 'edUcaTion', 'eDUCatiOn', 'educatioN']) == ['education', 'EDUCATION', 'eDucAtIoN', 'educatiOn', 'edUcatioN', 'edUcatioN', 'educAtiOn', 'edUcaTion', 'eDUCatiOn', 'education']
    assert candidate(wordlist = ['elephant', 'Elephant', 'elePHant', 'ELEPHANT'],queries = ['elephant', 'Elephant', 'elePHant', 'ELEPHANT', 'elphant', 'ELPHNT', 'elefant', 'elphantt']) == ['elephant', 'Elephant', 'elePHant', 'ELEPHANT', '', '', '', '']
    assert candidate(wordlist = ['developer', 'DEVELOPER', 'DevEloPer', 'develoPER', 'develoPer', 'DEveloPer'],queries = ['developer', 'DEVELOPER', 'DevEloPer', 'develoPER', 'develoPer', 'DEveloPer', 'devEloPer', 'DEvelOpEr']) == ['developer', 'DEVELOPER', 'DevEloPer', 'develoPER', 'develoPer', 'DEveloPer', 'developer', 'developer']
    assert candidate(wordlist = ['flying', 'FLYING', 'FlyIng', 'FLyInG', 'fLyInG', 'FLYing'],queries = ['flying', 'FLYING', 'flyIng', 'FLyInG', 'fLyInG', 'FLYing', 'FLyInG', 'FLYINGg', 'FLYINGgg']) == ['flying', 'FLYING', 'flying', 'FLyInG', 'fLyInG', 'FLYing', 'FLyInG', '', '']
    assert candidate(wordlist = ['algorithm', 'algoritm', 'algorithmic', 'algorithem', 'algoritm', 'algorit', 'algorithmically'],queries = ['Algorithm', 'Algoritm', 'Algorithmic', 'Algorithem', 'Algoritm', 'Algorit', 'Algorithmically', 'alorithm', 'algrthm', 'algorithmc', 'algrthm', 'algrthm', 'algorithmiclly', 'alorithm', 'algrthm', 'algorithmc', 'algrthm', 'algrthm', 'algorithmc', 'alorithm', 'algrthm', 'algorithmc', 'algrthm', 'algrthm', 'algorithmc']) == ['algorithm', 'algoritm', 'algorithmic', 'algorithem', 'algoritm', 'algorit', 'algorithmically', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    assert candidate(wordlist = ['fantastic', 'Fantastic', 'FANTASTIC', 'fantastiv', 'Fantastiv'],queries = ['fantastic', 'Fantastic', 'FANTASTIC', 'fantastiv', 'Fantastiv', 'fantasticv', 'fantastivv', 'Fantastiv', 'fantasticIv', 'FANTASTIc']) == ['fantastic', 'Fantastic', 'FANTASTIC', 'fantastiv', 'Fantastiv', '', '', 'Fantastiv', '', 'fantastic']
    assert candidate(wordlist = ['important', 'IMPORTANT', 'Important', 'imporant', 'impotant'],queries = ['important', 'IMPORTANT', 'Important', 'imporant', 'impotant', 'imporant']) == ['important', 'IMPORTANT', 'Important', 'imporant', 'impotant', 'imporant']
    assert candidate(wordlist = ['machine', 'MACHINE', 'MachInE', 'MACHiNe'],queries = ['machine', 'MACHINE', 'MachInE', 'MACHiNe', 'machines', 'MACHINES', 'MachInES', 'MACHiNES', 'machinne']) == ['machine', 'MACHINE', 'MachInE', 'MACHiNe', '', '', '', '', '']
    assert candidate(wordlist = ['community', 'COMMUNITY', 'Community', 'commuinty', 'communiti'],queries = ['community', 'COMMUNITY', 'Community', 'commuinty', 'communiti', 'commuinty']) == ['community', 'COMMUNITY', 'Community', 'commuinty', 'communiti', 'commuinty']
    assert candidate(wordlist = ['orchid', 'Orchid', 'ORCHID', 'orchd', 'orhid', 'orckid', 'orchidd'],queries = ['orchid', 'Orchid', 'ORCHID', 'orchd', 'orhid', 'orckid', 'orchidd', 'orchiddd', 'orchidd', 'orchidds']) == ['orchid', 'Orchid', 'ORCHID', 'orchd', 'orhid', 'orckid', 'orchidd', '', 'orchidd', '']
    assert candidate(wordlist = ['grape', 'Grape', 'GRAPE', 'grapefruit', 'GrapeFruit'],queries = ['grape', 'Grape', 'GRAPE', 'grapefruit', 'GrapeFruit', 'grApE', 'Grapefruit', 'grapeFruit', 'GRape', 'grapeFruitS']) == ['grape', 'Grape', 'GRAPE', 'grapefruit', 'GrapeFruit', 'grape', 'grapefruit', 'grapefruit', 'grape', '']
    assert candidate(wordlist = ['intelligent', 'Intelligent', 'INTELLIGENT', 'inteligent', 'inteligents'],queries = ['intelligent', 'Intelligent', 'INTELLIGENT', 'inteligent', 'inteligents', 'intilignt']) == ['intelligent', 'Intelligent', 'INTELLIGENT', 'inteligent', 'inteligents', '']
    assert candidate(wordlist = ['aabbcc', 'abc', 'aebec', 'accbba', 'aabbccaa'],queries = ['aabbcc', 'abc', 'aebec', 'accbba', 'aabbccaa', 'AABBCC', 'ABC', 'AEBEC', 'ACCBBA', 'AABBCCAA', 'aabbc', 'abcc', 'aebc', 'accbb', 'aabbc', 'abcc', 'aebc', 'accbb', 'aabbc', 'abcc', 'aebc', 'accbb', 'aabbc', 'abcc', 'aebc', 'accbb', 'aabbc', 'abcc', 'aebc', 'accbb']) == ['aabbcc', 'abc', 'aebec', 'accbba', 'aabbccaa', 'aabbcc', 'abc', 'aebec', 'accbba', 'aabbccaa', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    assert candidate(wordlist = ['water', 'Water', 'WATER', 'waTer', 'wateR', 'watER', 'wAtEr', 'waTEr'],queries = ['water', 'Water', 'WATER', 'waTer', 'wateR', 'watER', 'wAtEr', 'waTEr', 'wateR', 'waTer', 'watER', 'wAtEr', 'waTEr', 'wAter']) == ['water', 'Water', 'WATER', 'waTer', 'wateR', 'watER', 'wAtEr', 'waTEr', 'wateR', 'waTer', 'watER', 'wAtEr', 'waTEr', 'water']
    assert candidate(wordlist = ['banana', 'Banana', 'BANANA', 'banAna'],queries = ['banana', 'Banana', 'BANANA', 'banAna', 'BaNANA', 'bAnAnA', 'bananA', 'BaNANa']) == ['banana', 'Banana', 'BANANA', 'banAna', 'banana', 'banana', 'banana', 'banana']
    assert candidate(wordlist = ['umbrella', 'Umbrella', 'uMbReLlA', 'UMbrella'],queries = ['umbrella', 'Umbrella', 'uMbReLlA', 'UMbrella', 'umbrellA', 'UmBrella', 'UMBRELLA', 'umBRELLa', 'umbrela']) == ['umbrella', 'Umbrella', 'uMbReLlA', 'UMbrella', 'umbrella', 'umbrella', 'umbrella', 'umbrella', '']
    assert candidate(wordlist = ['environment', 'ENVIRONMENT', 'Environment', 'enviroment', 'evniroment'],queries = ['environment', 'ENVIRONMENT', 'Environment', 'enviroment', 'evniroment', 'envirnoment']) == ['environment', 'ENVIRONMENT', 'Environment', 'enviroment', 'evniroment', '']
    assert candidate(wordlist = ['umbrella', 'uMBrElLa', 'UMBRELLA', 'umbrellA'],queries = ['umbrella', 'uMBrElLa', 'UMBRELLA', 'umbrellA', 'umbrellaA', 'UMBRELLAa', 'uMBrElLaa', 'umbrellaa', 'umbrellaAA']) == ['umbrella', 'uMBrElLa', 'UMBRELLA', 'umbrellA', '', '', '', '', '']
    assert candidate(wordlist = ['umbrella', 'UMBRELLA', 'Umbrella', 'umBrella'],queries = ['Umbrella', 'umbrella', 'UMBRELLA', 'uMBRELLA', 'umbralla', 'umbrellaa']) == ['Umbrella', 'umbrella', 'UMBRELLA', 'umbrella', 'umbrella', '']
    assert candidate(wordlist = ['education', 'Education', 'EDUCATION', 'educatin', 'Educatin', 'educatiOn'],queries = ['education', 'Education', 'EDUCATION', 'educatin', 'Educatin', 'educatiOn', 'edUcation', 'educAtion', 'educatiOns', 'educatiOn']) == ['education', 'Education', 'EDUCATION', 'educatin', 'Educatin', 'educatiOn', 'education', 'education', '', 'educatiOn']
    assert candidate(wordlist = ['rhythm', 'Rhythm', 'RYTHM', 'rhythem', 'rythum'],queries = ['rhythm', 'Rhythm', 'RYTHM', 'rhythem', 'rythum', 'rhythmm', 'rhyth', 'rythmm', 'rhythmz', 'rhythmzz']) == ['rhythm', 'Rhythm', 'RYTHM', 'rhythem', 'rythum', '', '', '', '', '']
    assert candidate(wordlist = ['sequence', 'Sequence', 'SEQUENCE', 'sequnce', 'Sequnce', 'sequeNce'],queries = ['sequence', 'Sequence', 'SEQUENCE', 'sequnce', 'Sequnce', 'sequeNce', 'sequnce', 'Sequense', 'SEQUENSe', 'sequenze']) == ['sequence', 'Sequence', 'SEQUENCE', 'sequnce', 'Sequnce', 'sequeNce', 'sequnce', '', '', '']
    assert candidate(wordlist = ['communication', 'Communication', 'COMMUNICATION', 'commnication', 'Commnication'],queries = ['communication', 'Communication', 'COMMUNICATION', 'commnication', 'Commnication', 'communiCation', 'commNicAtion', 'ComMunication', 'COMMunIcAtion', 'communIcAtion']) == ['communication', 'Communication', 'COMMUNICATION', 'commnication', 'Commnication', 'communication', 'commnication', 'communication', 'communication', 'communication']
    assert candidate(wordlist = ['quIckBrOwnFox', 'QUICKBROWNFOX', 'QuickBrownFox', 'quiCKBrOwnFoX', 'QUICKbrownfox'],queries = ['quickbrownfox', 'QUICKBROWNFOX', 'QuiCKBrOwnFoX', 'QUICKbrownfox', 'quickBRownfox', 'quickbrownfoX', 'quickbrOwnfox', 'QUICKBROWNfOX']) == ['quIckBrOwnFox', 'QUICKBROWNFOX', 'quIckBrOwnFox', 'QUICKbrownfox', 'quIckBrOwnFox', 'quIckBrOwnFox', 'quIckBrOwnFox', 'quIckBrOwnFox']
    assert candidate(wordlist = ['elephant', 'Elephant', 'ELEPHANT', 'eLEPHANT', 'eLEpHANT'],queries = ['elephant', 'Elephant', 'ELEPHANT', 'eLEPHANT', 'eLEpHANT', 'elephants', 'Elephants', 'ELEPHANTs', 'eLEPHANTs']) == ['elephant', 'Elephant', 'ELEPHANT', 'eLEPHANT', 'eLEpHANT', '', '', '', '']
    assert candidate(wordlist = ['Supercalifragilisticexpialidocious', 'supercalifragilisticexpialidocious', 'SuPeRcAlIfRaGiLiStIcExPiAlIdOcIoUs', 'SUPErcALifRAGilistiCexpiALIdOcIOUs'],queries = ['supercalifragilisticexpialidocious', 'SUPErcALifRAGilistiCexpiALIdOcIOUs', 'SuPeRcAlIfRaGiLiStIcExPiAlIdOcIoUs', 'supercalifragilisticexpialidociosa']) == ['supercalifragilisticexpialidocious', 'SUPErcALifRAGilistiCexpiALIdOcIOUs', 'SuPeRcAlIfRaGiLiStIcExPiAlIdOcIoUs', '']
    assert candidate(wordlist = ['ambiguity', 'ambiguos', 'Ambiguity', 'AMBIGUITY', 'ambiguous', 'amgibuity'],queries = ['ambiguity', 'AMBIGUITY', 'Ambiguity', 'ambiguous', 'AmbiguiTy', 'amgibuity']) == ['ambiguity', 'AMBIGUITY', 'Ambiguity', 'ambiguous', 'ambiguity', 'amgibuity']
    assert candidate(wordlist = ['supercalifragilisticexpialidocious', 'SUPERCALIFRAGILISTICEXPIALIDOCIOUS', 'Supercalifragilisticexpialidocious', 'suPercalifragilisticexpialidocious'],queries = ['supercalifragilisticexpialidocious', 'SUPERCALIFRAGILISTICEXPIALIDOCIOUS', 'Supercalifragilisticexpialidocious', 'suPercalifragilisticexpialidocious', 'supercalifragilisticexpialido', 'supercalifragilisticexpialidocius']) == ['supercalifragilisticexpialidocious', 'SUPERCALIFRAGILISTICEXPIALIDOCIOUS', 'Supercalifragilisticexpialidocious', 'suPercalifragilisticexpialidocious', '', '']
    assert candidate(wordlist = ['algorithm', 'AlgorithM', 'ALGORITHM', 'algoritm', 'Algoritm'],queries = ['algorithm', 'AlgorithM', 'ALGORITHM', 'algoritm', 'Algoritm', 'algorithM', 'algoritm', 'AlgorIthm', 'algoRitm', 'AlgoRithm']) == ['algorithm', 'AlgorithM', 'ALGORITHM', 'algoritm', 'Algoritm', 'algorithm', 'algoritm', 'algorithm', 'algoritm', 'algorithm']


