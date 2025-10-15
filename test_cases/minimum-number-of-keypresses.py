def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "mmmmmmmmmmmmmmmm") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mmmmmmmmmmmmmmmm") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 102: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijkl") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijkl") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello世界") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello世界") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzz") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzz") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzzzz") == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzzzz") == 76: {e}')
    
    total += 1
    try:
        result = candidate(s = "apple") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "apple") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "thequickbrownfoxjumpsoverthelazydog") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thequickbrownfoxjumpsoverthelazydog") == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "optimization") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "optimization") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbccccdddd") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbccccdddd") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithmanycharactersandletters") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithmanycharactersandletters") == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "allthesametheallthesametheallthesamethe") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "allthesametheallthesametheallthesamethe") == 39: {e}')
    
    total += 1
    try:
        result = candidate(s = "exampleofaverylongstringthatneedsmanykeypresses") == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "exampleofaverylongstringthatneedsmanykeypresses") == 61: {e}')
    
    total += 1
    try:
        result = candidate(s = "datastructuresandalgorithms") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "datastructuresandalgorithms") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "verylongstringwithvariouscharactersandfrequencies") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "verylongstringwithvariouscharactersandfrequencies") == 64: {e}')
    
    total += 1
    try:
        result = candidate(s = "algorithmoptimization") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "algorithmoptimization") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaananabay") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaananabay") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "averylongstringthatincludesmanylettersrepeatedmultipletimes") == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "averylongstringthatincludesmanylettersrepeatedmultipletimes") == 73: {e}')
    
    total += 1
    try:
        result = candidate(s = "shortstring") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "shortstring") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbcccccccc") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbcccccccc") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "oneoneonetwoonetwoonethreeoneoneonetwoonetwothree") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "oneoneonetwoonetwoonethreeoneoneonetwoonetwothree") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "frequencydistribution") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "frequencydistribution") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzaaayyxbbbxxccc") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzaaayyxbbbxxccc") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 64: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 56: {e}')
    
    total += 1
    try:
        result = candidate(s = "cloudcomputingisthemostmodernwayofdeliveringservices") == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cloudcomputingisthemostmodernwayofdeliveringservices") == 71: {e}')
    
    total += 1
    try:
        result = candidate(s = "uniquecharactersarespecialtoo") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uniquecharactersarespecialtoo") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "keypadmappingoptimization") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "keypadmappingoptimization") == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 153: {e}')
    
    total += 1
    try:
        result = candidate(s = "occurrencesoflettersareirrelevant") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "occurrencesoflettersareirrelevant") == 37: {e}')
    
    total += 1
    try:
        result = candidate(s = "complexityanalysiscomplexityanalysis") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "complexityanalysiscomplexityanalysis") == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "frequencydistributionoflettersinenglish") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "frequencydistributionoflettersinenglish") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "equalfrequencyaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 117
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "equalfrequencyaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 117: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbccccccccdddddddd") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbccccccccdddddddd") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijkabcdefghijkabcdefghijkabcdefghijkabcdefghijk") == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijkabcdefghijkabcdefghijkabcdefghijkabcdefghijk") == 65: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithrepeatedcharacters") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithrepeatedcharacters") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohellohellohellohellohellohellohellohello") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohellohellohellohellohellohellohellohello") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "frequenciesoffrequentelementsandcharacters") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "frequenciesoffrequentelementsandcharacters") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "frequencydistributionofcharacters") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "frequencydistributionofcharacters") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "repeatedlettersllllllllllllllll") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeatedlettersllllllllllllllll") == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "pythonprogrammingchallenge") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pythonprogrammingchallenge") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "uniquenesschecking") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uniquenesschecking") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 102: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 104: {e}')
    
    total += 1
    try:
        result = candidate(s = "algorithms") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "algorithms") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 398
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 398: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == 56: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringthatweneedtotestthealgorithm") == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringthatweneedtotestthealgorithm") == 59: {e}')
    
    total += 1
    try:
        result = candidate(s = "repeatedcharactersrepeatedcharactersrepeatedcharacters") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeatedcharactersrepeatedcharactersrepeatedcharacters") == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringthatcontainsmanycharactersandshouldrequiremultiplekeypresses") == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringthatcontainsmanycharactersandshouldrequiremultiplekeypresses") == 106: {e}')
    
    total += 1
    try:
        result = candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "optimizationiskeytoefficientcoding") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "optimizationiskeytoefficientcoding") == 41: {e}')
    
    total += 1
    try:
        result = candidate(s = "xylophoneisamusicalinstrument") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xylophoneisamusicalinstrument") == 37: {e}')
    
    total += 1
    try:
        result = candidate(s = "pressingbuttonsforlongstrings") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pressingbuttonsforlongstrings") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "pythonprogrammingisfun") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pythonprogrammingisfun") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippiissimississippi") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippiissimississippi") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaabbbbbbbbccccccccddddddd") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaabbbbbbbbccccccccddddddd") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "toimpressyourinterviewerwithcomplexstrings") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "toimpressyourinterviewerwithcomplexstrings") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaananabana") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaananabana") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "algorithmsanddatastructures") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "algorithmsanddatastructures") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithmanycharacters") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithmanycharacters") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydog") == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydog") == 120: {e}')
    
    total += 1
    try:
        result = candidate(s = "pythonisaveryversatilelanguage") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pythonisaveryversatilelanguage") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "optimizationofthekeypadlayout") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "optimizationofthekeypadlayout") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 28: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "mmmmmmmmmmmmmmmm") == 16
    assert candidate(s = "mississippi") == 11
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 51
    assert candidate(s = "banana") == 6
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 102
    assert candidate(s = "abcdefghijkl") == 15
    assert candidate(s = "hello世界") == 7
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz") == 26
    assert candidate(s = "programming") == 11
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzz") == 24
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzzzzzzzz") == 76
    assert candidate(s = "apple") == 5
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 51
    assert candidate(s = "thequickbrownfoxjumpsoverthelazydog") == 60
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm") == 51
    assert candidate(s = "abacabadabacaba") == 15
    assert candidate(s = "optimization") == 12
    assert candidate(s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 52
    assert candidate(s = "aabbbccccdddd") == 13
    assert candidate(s = "thisisaverylongstringwithmanycharactersandletters") == 60
    assert candidate(s = "allthesametheallthesametheallthesamethe") == 39
    assert candidate(s = "exampleofaverylongstringthatneedsmanykeypresses") == 61
    assert candidate(s = "datastructuresandalgorithms") == 33
    assert candidate(s = "verylongstringwithvariouscharactersandfrequencies") == 64
    assert candidate(s = "algorithmoptimization") == 24
    assert candidate(s = "bananaananabay") == 14
    assert candidate(s = "averylongstringthatincludesmanylettersrepeatedmultipletimes") == 73
    assert candidate(s = "shortstring") == 11
    assert candidate(s = "aaaaaaaaaabbbbbbbbcccccccc") == 26
    assert candidate(s = "oneoneonetwoonetwoonethreeoneoneonetwoonetwothree") == 49
    assert candidate(s = "frequencydistribution") == 26
    assert candidate(s = "zzzaaayyxbbbxxccc") == 17
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 64
    assert candidate(s = "abracadabra") == 11
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 56
    assert candidate(s = "cloudcomputingisthemostmodernwayofdeliveringservices") == 71
    assert candidate(s = "uniquecharactersarespecialtoo") == 34
    assert candidate(s = "keypadmappingoptimization") == 29
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 153
    assert candidate(s = "occurrencesoflettersareirrelevant") == 37
    assert candidate(s = "complexityanalysiscomplexityanalysis") == 44
    assert candidate(s = "frequencydistributionoflettersinenglish") == 48
    assert candidate(s = "equalfrequencyaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 117
    assert candidate(s = "aaaaaaaaaabbbbbbbbccccccccdddddddd") == 34
    assert candidate(s = "abcdefghijkabcdefghijkabcdefghijkabcdefghijkabcdefghijk") == 65
    assert candidate(s = "thisisaverylongstringwithrepeatedcharacters") == 52
    assert candidate(s = "hellohellohellohellohellohellohellohellohellohello") == 50
    assert candidate(s = "frequenciesoffrequentelementsandcharacters") == 50
    assert candidate(s = "frequencydistributionofcharacters") == 42
    assert candidate(s = "repeatedlettersllllllllllllllll") == 31
    assert candidate(s = "pythonprogrammingchallenge") == 32
    assert candidate(s = "uniquenesschecking") == 19
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 51
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 102
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzz") == 104
    assert candidate(s = "algorithms") == 11
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 398
    assert candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == 56
    assert candidate(s = "thisisaverylongstringthatweneedtotestthealgorithm") == 59
    assert candidate(s = "repeatedcharactersrepeatedcharactersrepeatedcharacters") == 54
    assert candidate(s = "thisisaverylongstringthatcontainsmanycharactersandshouldrequiremultiplekeypresses") == 106
    assert candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis") == 52
    assert candidate(s = "optimizationiskeytoefficientcoding") == 41
    assert candidate(s = "xylophoneisamusicalinstrument") == 37
    assert candidate(s = "pressingbuttonsforlongstrings") == 33
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 52
    assert candidate(s = "pythonprogrammingisfun") == 27
    assert candidate(s = "mississippiissimississippi") == 26
    assert candidate(s = "aaaaaaaaaaabbbbbbbbccccccccddddddd") == 34
    assert candidate(s = "toimpressyourinterviewerwithcomplexstrings") == 52
    assert candidate(s = "bananaananabana") == 15
    assert candidate(s = "algorithmsanddatastructures") == 33
    assert candidate(s = "thisisaverylongstringwithmanycharacters") == 48
    assert candidate(s = "thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydog") == 120
    assert candidate(s = "pythonisaveryversatilelanguage") == 38
    assert candidate(s = "optimizationofthekeypadlayout") == 36
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 28


