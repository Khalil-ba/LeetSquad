def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "UFO") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "UFO") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "aAeEiIoOuU") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAeEiIoOuU") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "Leetcode") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Leetcode") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgihjklmno") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgihjklmno") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "Regal") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Regal") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "Reinholdmes") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Reinholdmes") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "AbCdEfGh") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AbCdEfGh") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "textbook") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "textbook") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "cOdInGQuEsTiOn") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cOdInGQuEsTiOn") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "pYthOnPrOgRaMmInG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pYthOnPrOgRaMmInG") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "AaEeIiOoUu") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AaEeIiOoUu") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcode") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcode") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "Eve") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Eve") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "VoIcE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "VoIcE") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "Madam") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Madam") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgH") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgH") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "Margelet") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Margelet") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "book") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "book") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "Uncopyrightable") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Uncopyrightable") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "DAD") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DAD") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "MerryChristmas") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MerryChristmas") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "ComputerScience") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ComputerScience") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "ArtificialIntelligence") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ArtificialIntelligence") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "aAbBcCdDeEfFgG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAbBcCdDeEfFgG") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "Supercalifragilisticexpialidocious") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Supercalifragilisticexpialidocious") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "InDiCoRn") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "InDiCoRn") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "vowelvowelvowelvowelvowelvowel") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vowelvowelvowelvowelvowelvowel") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "LyoPHiNiC") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "LyoPHiNiC") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "VowelCOnsonAnt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "VowelCOnsonAnt") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "SyNtHeSiS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "SyNtHeSiS") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "CoMpUterScIeNcE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CoMpUterScIeNcE") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "Pneumonoultramicroscopicsilicovolcanoconiosis") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Pneumonoultramicroscopicsilicovolcanoconiosis") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "bBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "Supercalifragilisticexpialidocioussuper") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Supercalifragilisticexpialidocioussuper") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "EqUiVaLeNt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "EqUiVaLeNt") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "unevenNumberOfVowels") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "unevenNumberOfVowels") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "MachineLearning") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MachineLearning") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "QuantumComputing") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QuantumComputing") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "Pneumonoultramicroscopicsilicovolcanoconioses") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Pneumonoultramicroscopicsilicovolcanoconioses") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "DeViScIoN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DeViScIoN") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "AbCdEfGhIjKlMnOpQrStUvWxYz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AbCdEfGhIjKlMnOpQrStUvWxYz") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "CoRaL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CoRaL") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "Internationalization") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Internationalization") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "CaSeInSeNsItIvE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CaSeInSeNsItIvE") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "EvEnAnDdOuD") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "EvEnAnDdOuD") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "CoMpLeX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CoMpLeX") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "AbcDeFgHiJkLmNoPqRsTuVwXyZ") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AbcDeFgHiJkLmNoPqRsTuVwXyZ") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "Electroencephalographies") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Electroencephalographies") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "fAcEtImE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "fAcEtImE") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "AnALoGuIzAtIoN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AnALoGuIzAtIoN") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "sImPlEVoWaElStRiNg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "sImPlEVoWaElStRiNg") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "OpenAIChatGPT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OpenAIChatGPT") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "Incomprehensibility") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Incomprehensibility") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "ThEoReTiCaL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ThEoReTiCaL") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "VoWaElCoUnTiNg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "VoWaElCoUnTiNg") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "SiMpLy") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "SiMpLy") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "Electroencephalography") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Electroencephalography") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "Honorificabilitudinitatibus") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Honorificabilitudinitatibus") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "ConsonantsToo") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ConsonantsToo") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijABCDEFGHIJ") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijABCDEFGHIJ") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "METHINKSITISLIKEALITTLEIODEUCALYPTUS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "METHINKSITISLIKEALITTLEIODEUCALYPTUS") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "Alphabetization") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Alphabetization") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "HumanComputerInteraction") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "HumanComputerInteraction") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "AmOrAnGe") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AmOrAnGe") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "balancedString") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "balancedString") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "EuPoCrAtIc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "EuPoCrAtIc") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "MississippiRiverOdd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MississippiRiverOdd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "RoMaNiCa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "RoMaNiCa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aAaAaAaAaAbBbBbBbB") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAaAaAaAaAbBbBbBbB") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "MiwEldrom") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MiwEldrom") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "AQuickBrownFoxJumpsOverTheLazyDog") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AQuickBrownFoxJumpsOverTheLazyDog") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "MaRiNo") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MaRiNo") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "CloudComputing") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CloudComputing") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "DataScienceAndML") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DataScienceAndML") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "Hippopotomonstrosesquippedaliophobia") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Hippopotomonstrosesquippedaliophobia") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "ImAgInAtIoN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ImAgInAtIoN") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "Pseudopseudohypoparathyroidism") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Pseudopseudohypoparathyroidism") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "PaLInDoRoMa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "PaLInDoRoMa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "DatabaseManagement") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DatabaseManagement") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "ComplexExample") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ComplexExample") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "sYmMeTrIcVoWaEl") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "sYmMeTrIcVoWaEl") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "QwErTyUiOpAsDfGhJkLzXcVbNm") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QwErTyUiOpAsDfGhJkLzXcVbNm") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "cOmPlExStRiNgWitHaLoTOfVoWels") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cOmPlExStRiNgWitHaLoTOfVoWels") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "AlEpInAtIoN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AlEpInAtIoN") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "AEIOUaeiouAEIOUaeiou") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AEIOUaeiouAEIOUaeiou") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "Environmental") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Environmental") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "SyMmEtrY") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "SyMmEtrY") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "PaLInDrOmE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "PaLInDrOmE") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "Interpolation") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Interpolation") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "Floccinaucinihilipilifications") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Floccinaucinihilipilifications") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "AlphabetSymmetry") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AlphabetSymmetry") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "BiChRoChO") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "BiChRoChO") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "SoftwareEngineering") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "SoftwareEngineering") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "Mississippi") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Mississippi") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "NaturalLanguageProcessing") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "NaturalLanguageProcessing") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "VowelsInBoth") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "VowelsInBoth") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "FLUtTuAtIoNs") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "FLUtTuAtIoNs") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "SuPeRaLpHaBeT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "SuPeRaLpHaBeT") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "MaLiNoUs") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MaLiNoUs") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "InternetOfThings") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "InternetOfThings") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "PeRuKkIa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "PeRuKkIa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "TrAnSaPoRt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "TrAnSaPoRt") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "OddAndEven") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OddAndEven") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aEiOuUoIeA") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aEiOuUoIeA") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "Alphabetical") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Alphabetical") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "VowelsAEIOUaeiou") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "VowelsAEIOUaeiou") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "aEiOuUeIoA") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aEiOuUeIoA") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "SeNtEnCe") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "SeNtEnCe") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "RepetitionRepetition") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "RepetitionRepetition") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "MississippiRiver") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MississippiRiver") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "Vowelsareeverywhere") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Vowelsareeverywhere") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "vowelvowelvowelvowel") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "vowelvowelvowelvowel") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "DataStructure") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DataStructure") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "MississippiRiverside") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MississippiRiverside") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "aeiouAEIOUaeiouAEIOU") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aeiouAEIOUaeiouAEIOU") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "XiLoPhOnE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "XiLoPhOnE") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "Floccinaucinihilipilification") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Floccinaucinihilipilification") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "PythonCoding") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "PythonCoding") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "VowelsAreVowels") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "VowelsAreVowels") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aEiOuUaEiO") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aEiOuUaEiO") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "NotSoBalanced") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "NotSoBalanced") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "Engineering") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Engineering") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "SuBiT") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "SuBiT") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "ProgrammingIsFun") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ProgrammingIsFun") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "aEiOuAeIoU") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aEiOuAeIoU") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "Alphabetically") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Alphabetically") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "PyThOnIsFuN") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "PyThOnIsFuN") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "AnNiHaLiLaToR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AnNiHaLiLaToR") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "consonantsAEIOUconsonants") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "consonantsAEIOUconsonants") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "Thyroparathyroidectomized") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Thyroparathyroidectomized") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "EvenlyDistributed") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "EvenlyDistributed") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "DataAnalysis") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "DataAnalysis") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "CyberSecurity") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CyberSecurity") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "VoCaBuLaRy") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "VoCaBuLaRy") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "AEIOUaeiou") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AEIOUaeiou") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "CaThODoRiC") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CaThODoRiC") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "AlGoRiThM") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AlGoRiThM") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "Antidisestablishmentarianism") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Antidisestablishmentarianism") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "CoNtRoVeRtEdbUt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "CoNtRoVeRtEdbUt") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "BaLaNcEd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "BaLaNcEd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "BlockchainTechnology") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "BlockchainTechnology") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "SystemAnalysis") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "SystemAnalysis") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "VowelsAndConsonants") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "VowelsAndConsonants") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "hAlFVaLuEs") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hAlFVaLuEs") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "AlphabetSoup") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AlphabetSoup") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "Unbelievable") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Unbelievable") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "SplittingStrings") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "SplittingStrings") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "GrApHiTe") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "GrApHiTe") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "AnAgrAm") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AnAgrAm") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "evenNumberOfVowels") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "evenNumberOfVowels") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "RoTiCoRn") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "RoTiCoRn") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "bYtEcOdE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bYtEcOdE") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "BigDataAnalytics") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "BigDataAnalytics") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "FLYINGDUCK") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "FLYINGDUCK") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "ComplexityAnalysis") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ComplexityAnalysis") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "VowelsAreEven") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "VowelsAreEven") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "cHiCaGo") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cHiCaGo") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "PythonIsAwesome") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "PythonIsAwesome") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "FeBrIfIoN") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "FeBrIfIoN") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "Electroencephalographically") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Electroencephalographically") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "mIxEdCaSeTeStStRiNg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mIxEdCaSeTeStStRiNg") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "ProgrammingLanguage") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ProgrammingLanguage") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "MississippiUniversity") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MississippiUniversity") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "equalvowelcounts") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "equalvowelcounts") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "EnvironmentalStudies") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "EnvironmentalStudies") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "InDeXeS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "InDeXeS") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "Supercalifragilisticexpialidociousxyz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Supercalifragilisticexpialidociousxyz") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzXYZxyzXYZ") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzXYZxyzXYZ") == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "UFO") == False
    assert candidate(s = "aAeEiIoOuU") == True
    assert candidate(s = "Leetcode") == True
    assert candidate(s = "abcdefgihjklmno") == False
    assert candidate(s = "Regal") == True
    assert candidate(s = "Reinholdmes") == True
    assert candidate(s = "AbCdEfGh") == True
    assert candidate(s = "textbook") == False
    assert candidate(s = "cOdInGQuEsTiOn") == False
    assert candidate(s = "pYthOnPrOgRaMmInG") == False
    assert candidate(s = "AaEeIiOoUu") == True
    assert candidate(s = "leetcode") == True
    assert candidate(s = "Eve") == False
    assert candidate(s = "racecar") == False
    assert candidate(s = "VoIcE") == True
    assert candidate(s = "Madam") == True
    assert candidate(s = "abcdefgH") == True
    assert candidate(s = "Margelet") == False
    assert candidate(s = "book") == True
    assert candidate(s = "Uncopyrightable") == True
    assert candidate(s = "DAD") == False
    assert candidate(s = "MerryChristmas") == False
    assert candidate(s = "ComputerScience") == False
    assert candidate(s = "ArtificialIntelligence") == False
    assert candidate(s = "aAbBcCdDeEfFgG") == True
    assert candidate(s = "Supercalifragilisticexpialidocious") == False
    assert candidate(s = "InDiCoRn") == False
    assert candidate(s = "vowelvowelvowelvowelvowelvowel") == True
    assert candidate(s = "LyoPHiNiC") == False
    assert candidate(s = "VowelCOnsonAnt") == False
    assert candidate(s = "SyNtHeSiS") == False
    assert candidate(s = "CoMpUterScIeNcE") == False
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == True
    assert candidate(s = "Pneumonoultramicroscopicsilicovolcanoconiosis") == False
    assert candidate(s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == False
    assert candidate(s = "bBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == True
    assert candidate(s = "Supercalifragilisticexpialidocioussuper") == False
    assert candidate(s = "EqUiVaLeNt") == False
    assert candidate(s = "unevenNumberOfVowels") == True
    assert candidate(s = "MachineLearning") == True
    assert candidate(s = "QuantumComputing") == True
    assert candidate(s = "Pneumonoultramicroscopicsilicovolcanoconioses") == False
    assert candidate(s = "DeViScIoN") == True
    assert candidate(s = "AbCdEfGhIjKlMnOpQrStUvWxYz") == False
    assert candidate(s = "CoRaL") == True
    assert candidate(s = "Internationalization") == True
    assert candidate(s = "CaSeInSeNsItIvE") == True
    assert candidate(s = "EvEnAnDdOuD") == False
    assert candidate(s = "CoMpLeX") == True
    assert candidate(s = "AbcDeFgHiJkLmNoPqRsTuVwXyZ") == False
    assert candidate(s = "Electroencephalographies") == True
    assert candidate(s = "fAcEtImE") == True
    assert candidate(s = "AnALoGuIzAtIoN") == True
    assert candidate(s = "sImPlEVoWaElStRiNg") == True
    assert candidate(s = "OpenAIChatGPT") == False
    assert candidate(s = "Incomprehensibility") == False
    assert candidate(s = "ThEoReTiCaL") == False
    assert candidate(s = "VoWaElCoUnTiNg") == True
    assert candidate(s = "SiMpLy") == False
    assert candidate(s = "Electroencephalography") == False
    assert candidate(s = "Honorificabilitudinitatibus") == False
    assert candidate(s = "ConsonantsToo") == True
    assert candidate(s = "abcdefghijABCDEFGHIJ") == True
    assert candidate(s = "METHINKSITISLIKEALITTLEIODEUCALYPTUS") == False
    assert candidate(s = "Alphabetization") == False
    assert candidate(s = "HumanComputerInteraction") == True
    assert candidate(s = "AmOrAnGe") == True
    assert candidate(s = "balancedString") == False
    assert candidate(s = "EuPoCrAtIc") == False
    assert candidate(s = "MississippiRiverOdd") == False
    assert candidate(s = "RoMaNiCa") == True
    assert candidate(s = "aAaAaAaAaAbBbBbBbB") == False
    assert candidate(s = "MiwEldrom") == False
    assert candidate(s = "AQuickBrownFoxJumpsOverTheLazyDog") == False
    assert candidate(s = "MaRiNo") == False
    assert candidate(s = "CloudComputing") == False
    assert candidate(s = "DataScienceAndML") == False
    assert candidate(s = "Hippopotomonstrosesquippedaliophobia") == False
    assert candidate(s = "ImAgInAtIoN") == True
    assert candidate(s = "Pseudopseudohypoparathyroidism") == True
    assert candidate(s = "PaLInDoRoMa") == True
    assert candidate(s = "DatabaseManagement") == True
    assert candidate(s = "ComplexExample") == False
    assert candidate(s = "sYmMeTrIcVoWaEl") == False
    assert candidate(s = "QwErTyUiOpAsDfGhJkLzXcVbNm") == False
    assert candidate(s = "cOmPlExStRiNgWitHaLoTOfVoWels") == False
    assert candidate(s = "AlEpInAtIoN") == True
    assert candidate(s = "AEIOUaeiouAEIOUaeiou") == True
    assert candidate(s = "Environmental") == False
    assert candidate(s = "SyMmEtrY") == False
    assert candidate(s = "PaLInDrOmE") == True
    assert candidate(s = "Interpolation") == False
    assert candidate(s = "Floccinaucinihilipilifications") == True
    assert candidate(s = "AlphabetSymmetry") == False
    assert candidate(s = "BiChRoChO") == True
    assert candidate(s = "SoftwareEngineering") == True
    assert candidate(s = "Mississippi") == False
    assert candidate(s = "NaturalLanguageProcessing") == True
    assert candidate(s = "VowelsInBoth") == True
    assert candidate(s = "FLUtTuAtIoNs") == False
    assert candidate(s = "SuPeRaLpHaBeT") == False
    assert candidate(s = "MaLiNoUs") == True
    assert candidate(s = "InternetOfThings") == False
    assert candidate(s = "PeRuKkIa") == True
    assert candidate(s = "TrAnSaPoRt") == False
    assert candidate(s = "OddAndEven") == True
    assert candidate(s = "aEiOuUoIeA") == True
    assert candidate(s = "Alphabetical") == False
    assert candidate(s = "VowelsAEIOUaeiou") == False
    assert candidate(s = "aEiOuUeIoA") == True
    assert candidate(s = "SeNtEnCe") == False
    assert candidate(s = "RepetitionRepetition") == True
    assert candidate(s = "MississippiRiver") == True
    assert candidate(s = "Vowelsareeverywhere") == False
    assert candidate(s = "vowelvowelvowelvowel") == True
    assert candidate(s = "DataStructure") == True
    assert candidate(s = "MississippiRiverside") == False
    assert candidate(s = "aeiouAEIOUaeiouAEIOU") == True
    assert candidate(s = "XiLoPhOnE") == False
    assert candidate(s = "Floccinaucinihilipilification") == False
    assert candidate(s = "PythonCoding") == False
    assert candidate(s = "VowelsAreVowels") == True
    assert candidate(s = "aEiOuUaEiO") == True
    assert candidate(s = "NotSoBalanced") == False
    assert candidate(s = "Engineering") == False
    assert candidate(s = "SuBiT") == True
    assert candidate(s = "ProgrammingIsFun") == False
    assert candidate(s = "aEiOuAeIoU") == True
    assert candidate(s = "Alphabetically") == False
    assert candidate(s = "PyThOnIsFuN") == False
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == False
    assert candidate(s = "AnNiHaLiLaToR") == True
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == False
    assert candidate(s = "consonantsAEIOUconsonants") == False
    assert candidate(s = "Thyroparathyroidectomized") == False
    assert candidate(s = "EvenlyDistributed") == True
    assert candidate(s = "DataAnalysis") == False
    assert candidate(s = "CyberSecurity") == False
    assert candidate(s = "VoCaBuLaRy") == True
    assert candidate(s = "AEIOUaeiou") == True
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == False
    assert candidate(s = "CaThODoRiC") == True
    assert candidate(s = "AlGoRiThM") == False
    assert candidate(s = "Antidisestablishmentarianism") == False
    assert candidate(s = "CoNtRoVeRtEdbUt") == False
    assert candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == False
    assert candidate(s = "BaLaNcEd") == False
    assert candidate(s = "BlockchainTechnology") == True
    assert candidate(s = "SystemAnalysis") == True
    assert candidate(s = "VowelsAndConsonants") == True
    assert candidate(s = "hAlFVaLuEs") == False
    assert candidate(s = "AlphabetSoup") == False
    assert candidate(s = "Unbelievable") == True
    assert candidate(s = "SplittingStrings") == False
    assert candidate(s = "GrApHiTe") == False
    assert candidate(s = "AnAgrAm") == False
    assert candidate(s = "evenNumberOfVowels") == False
    assert candidate(s = "RoTiCoRn") == False
    assert candidate(s = "bYtEcOdE") == False
    assert candidate(s = "BigDataAnalytics") == False
    assert candidate(s = "FLYINGDUCK") == True
    assert candidate(s = "ComplexityAnalysis") == True
    assert candidate(s = "VowelsAreEven") == False
    assert candidate(s = "cHiCaGo") == True
    assert candidate(s = "PythonIsAwesome") == False
    assert candidate(s = "FeBrIfIoN") == False
    assert candidate(s = "Electroencephalographically") == True
    assert candidate(s = "mIxEdCaSeTeStStRiNg") == False
    assert candidate(s = "ProgrammingLanguage") == True
    assert candidate(s = "MississippiUniversity") == False
    assert candidate(s = "equalvowelcounts") == False
    assert candidate(s = "EnvironmentalStudies") == True
    assert candidate(s = "InDeXeS") == False
    assert candidate(s = "Supercalifragilisticexpialidociousxyz") == False
    assert candidate(s = "xyzXYZxyzXYZ") == True


