def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "abc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzXYZ") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzXYZ") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbcc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbcc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "AABBCC") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AABBCC") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "cCcCc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cCcCc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "AaBbCc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AaBbCc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "abBCab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abBCab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "XyZxYz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "XyZxYz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "A") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "A") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaAbcBC") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaAbcBC") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "bBbB") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bBbB") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aA") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aA") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "MixedCASEwithSPECIALSspecial") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MixedCASEwithSPECIALSspecial") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "nestedLoopNESTED") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "nestedLoopNESTED") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "kKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkK") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "kKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkK") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "LongStringWithNoSpecials") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LongStringWithNoSpecials") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "vVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvV") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "vVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvV") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefABCDEF") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefABCDEF") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "SpecialLettersTest") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SpecialLettersTest") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "MixedCASEwithSpecials") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MixedCASEwithSpecials") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "UniqueSpecialsABCDabcd") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "UniqueSpecialsABCDabcd") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaBBBBccccDDDDeeeeFFFFggggHHHHiiiiJJJjkkkkLLLLmmmmNNNNooooPPPqqqqRRRRssssTTTTuuuuVVVVwwwwXXXXyyyyZZZZ") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaBBBBccccDDDDeeeeFFFFggggHHHHiiiiJJJjkkkkLLLLmmmmNNNNooooPPPqqqqRRRRssssTTTTuuuuVVVVwwwwXXXXyyyyZZZZ") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "eEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEe") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "eEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEe") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAbBcC") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAbBcC") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcABC") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcABC") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefGHIJKLmnopQRstUVWxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefGHIJKLmnopQRstUVWxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "Python3.8") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Python3.8") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAbBC") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAbBC") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "worldWORLD") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "worldWORLD") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "xylophoneXYZ") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xylophoneXYZ") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "nestedCASECASEnested") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "nestedCASECASEnested") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAaAaAaAaAaAaAaAaAaA") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAaAaAaAaAaAaAaAaAaA") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "SpecialsAllOverAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SpecialsAllOverAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCdefGhIjkLmnopQrstUVwXyZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCdefGhIjkLmnopQrstUVwXyZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "UPPERlower") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "UPPERlower") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "zZyYxXwWvVuUtTsSrRpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zZyYxXwWvVuUtTsSrRpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == 25: {e}')
    
    total += 1
    try:
        result = candidate(word = "NoSpecial") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "NoSpecial") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "SpecialCharacters123") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SpecialCharacters123") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "OneSpecialA") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "OneSpecialA") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "SingleSpeciala") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SingleSpeciala") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbcDeEfGhIjKlMnOpQrStUvWxYz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbcDeEfGhIjKlMnOpQrStUvWxYz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "helloHELLO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "helloHELLO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "HelloWorld") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HelloWorld") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "MultipleUUppercases") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MultipleUUppercases") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "wWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwW") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "wWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwW") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "yYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyY") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "yYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyY") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYzAbCdEfGhIjKlMnOpQrStUvWxYz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYzAbCdEfGhIjKlMnOpQrStUvWxYz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "TrailingSpecialsAaBbCc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TrailingSpecialsAaBbCc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcABCabcABCabcABC") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcABCabcABCabcABC") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "JustOneSpecialCharacterb") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "JustOneSpecialCharacterb") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "iIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiI") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "iIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiI") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "noSpecial") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "noSpecial") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "NoSpecialCharacters") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "NoSpecialCharacters") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "SpecialCharacters") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SpecialCharacters") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "lowerCASEuppercase") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lowerCASEuppercase") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "UniqueUniqueUniqueUnique") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "UniqueUniqueUniqueUnique") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "CASEsensitive") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CASEsensitive") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "OneSpecialAa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "OneSpecialAa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "SingleSpecialA") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SingleSpecialA") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "jJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJ") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJ") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "bBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbB") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbB") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbCCddeeffGGhhiiJJkkllMMnnooppQQrrssttuuVVwwxxyyzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbCCddeeffGGhhiiJJkkllMMnnooppQQrrssttuuVVwwxxyyzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "MultipleMultipleMultiple") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MultipleMultipleMultiple") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "ComplexMixAaBbCc123!@#AaBbCc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ComplexMixAaBbCc123!@#AaBbCc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "TestCase") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TestCase") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "mMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmM") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmM") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "NestedSpecialsAaBBbbCCcc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "NestedSpecialsAaBBbbCCcc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "fFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFf") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "fFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFf") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "lLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlL") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlL") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "tTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtT") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "tTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtT") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdEFGHijKLMnopQRSTuvWXyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdEFGHijKLMnopQRSTuvWXyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "JustOneAa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "JustOneAa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "nNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnN") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "nNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnN") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "StartingWithSpecialsAaBbCc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "StartingWithSpecialsAaBbCc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "uniqueUnique") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uniqueUnique") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "gGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgG") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "gGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgG") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "xXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "AaAaAaAaAaBbBbBbBbCcCcCcCcDdDdDdDdEeEeEeEeFfFfFfFfGgGgGgGgHhHhHhHhIiIiIiIiJjJjJjJjKkKkKkKkLlLlLlLlMmMmMmMmNnNnNnNnOoOoOoOoPpPpPpPpQqQqQqQqRrRrRrRrSsSsSsSsTtTtTtTtUuUuUuUuVvVvVvVvWwWwWwWwXxXxXxXxYyYyYyYyZzZzZzZz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AaAaAaAaAaBbBbBbBbCcCcCcCcDdDdDdDdEeEeEeEeFfFfFfFfGgGgGgGgHhHhHhHhIiIiIiIiJjJjJjJjKkKkKkKkLlLlLlLlMmMmMmMmNnNnNnNnOoOoOoOoPpPpPpPpQqQqQqQqRrRrRrRrSsSsSsSsTtTtTtTtUuUuUuUuVvVvVvVvWwWwWwWwXxXxXxXxYyYyYyYyZzZzZzZz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "specialCharSPECIAL") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "specialCharSPECIAL") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "hHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhH") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "hHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhH") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "AlphabetSoup") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AlphabetSoup") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "AaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "RepeatRepeatREPEAT") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RepeatRepeatREPEAT") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "pPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpP") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpP") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aA1Bb2Cc3Dd4Ee5Ff6Gg7Hh8Ii9Jj0") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aA1Bb2Cc3Dd4Ee5Ff6Gg7Hh8Ii9Jj0") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "specialCharacters") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "specialCharacters") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "sSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsS") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "sSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsS") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAaAaA") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAaAaA") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "JustOneZz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "JustOneZz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCc") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCc") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "Zebra") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Zebra") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "EndingWithSpecialsAaBbCc") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EndingWithSpecialsAaBbCc") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "bbbbbbbbBBBBBBB") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bbbbbbbbBBBBBBB") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "RePeAtInGChaRaCtErS") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RePeAtInGChaRaCtErS") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzABCD") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzABCD") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "AaBbCc1234567890!@#$%^&*()") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AaBbCc1234567890!@#$%^&*()") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "repeatedCHARactersCHARacters") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "repeatedCHARactersCHARacters") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzabcdefghijklmnopqrstuvwxyz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzabcdefghijklmnopqrstuvwxyz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "UniqueCASE") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "UniqueCASE") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "doubleDOUBLEtrouble") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "doubleDOUBLEtrouble") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "PythonIsAwesome") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PythonIsAwesome") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "MixedCASE123") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MixedCASE123") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "QwErTyUiOpAsDfGhJkLzXcVbNm") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "QwErTyUiOpAsDfGhJkLzXcVbNm") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "rRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrR") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "rRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrR") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abCDefGHijKLmnopQRstUVwxYZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abCDefGHijKLmnopQRstUVwxYZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcABCdefDEFghiGHI") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcABCdefDEFghiGHI") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "pythonPYTHON") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pythonPYTHON") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "OverlapOverlap") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "OverlapOverlap") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "CASEcase") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CASEcase") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "testCaseTestCase") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "testCaseTestCase") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "specialCHARSareHERE") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "specialCHARSareHERE") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "SingleSpecialAa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SingleSpecialAa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "qQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQ") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQ") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaBBccDDeeFFggHHiiJJkkLLmmNNooPPqqRRssTTuuVVwwXXyyZZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaBBccDDeeFFggHHiiJJkkLLmmNNooPPqqRRssTTuuVVwwXXyyZZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "dDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "dDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "SsEeCcIiAaLlTtCcHaArAcCtTeErsRsS") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SsEeCcIiAaLlTtCcHaArAcCtTeErsRsS") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "JustOneSpecialCharacterB") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "JustOneSpecialCharacterB") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "bBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbB") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbB") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "NoRepeatsJustSpecialsAaBbCc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "NoRepeatsJustSpecialsAaBbCc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "MiXeDcAsEwItHiSmOvEs") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MiXeDcAsEwItHiSmOvEs") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "HelloWORLD") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HelloWORLD") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "SpecialCharactersTEST") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SpecialCharactersTEST") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "oOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoO") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "oOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoO") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "SpecialCHARacters") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SpecialCHARacters") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "zZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZ") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZ") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "MultiplELowercases") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MultiplELowercases") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "AabbCCddeEFFgghhIIjjKKllMMnnooppQQrrSsttUuvvWwXxyyZz") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AabbCCddeEFFgghhIIjjKKllMMnnooppQQrrSsttUuvvWwXxyyZz") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "MiXeDcAsE123") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MiXeDcAsE123") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "OverlapAaBbCcAaBbCc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "OverlapAaBbCcAaBbCc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "uniqueUnIQUE") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uniqueUnIQUE") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "helloWorldHELLO") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "helloWorldHELLO") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "specialSPECIAL") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "specialSPECIAL") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "PythonProgramming") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PythonProgramming") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "cCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "uUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuU") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuU") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "SpecialAndNormalChars123!@#") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SpecialAndNormalChars123!@#") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "Mississippi") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Mississippi") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "MixedCASEWithSOMEspecial") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MixedCASEWithSOMEspecial") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "NoSpecialHere") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "NoSpecialHere") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaaaaaAAAAAA") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaaaaaAAAAAA") == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "abc") == 0
    assert candidate(word = "xyzXYZ") == 3
    assert candidate(word = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 26
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 26
    assert candidate(word = "aabbcc") == 0
    assert candidate(word = "AABBCC") == 0
    assert candidate(word = "cCcCc") == 1
    assert candidate(word = "AaBbCc") == 3
    assert candidate(word = "abBCab") == 1
    assert candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYz") == 0
    assert candidate(word = "XyZxYz") == 3
    assert candidate(word = "a") == 0
    assert candidate(word = "A") == 0
    assert candidate(word = "aaAbcBC") == 3
    assert candidate(word = "bBbB") == 1
    assert candidate(word = "aA") == 1
    assert candidate(word = "") == 0
    assert candidate(word = "MixedCASEwithSPECIALSspecial") == 7
    assert candidate(word = "nestedLoopNESTED") == 5
    assert candidate(word = "kKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkKkK") == 1
    assert candidate(word = "LongStringWithNoSpecials") == 3
    assert candidate(word = "vVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvVvV") == 1
    assert candidate(word = "abcdefABCDEF") == 6
    assert candidate(word = "SpecialLettersTest") == 3
    assert candidate(word = "MixedCASEwithSpecials") == 4
    assert candidate(word = "UniqueSpecialsABCDabcd") == 6
    assert candidate(word = "aaaaBBBBccccDDDDeeeeFFFFggggHHHHiiiiJJJjkkkkLLLLmmmmNNNNooooPPPqqqqRRRRssssTTTTuuuuVVVVwwwwXXXXyyyyZZZZ") == 1
    assert candidate(word = "eEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEeEe") == 1
    assert candidate(word = "aAbBcC") == 3
    assert candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 1
    assert candidate(word = "abcABC") == 3
    assert candidate(word = "abcdefGHIJKLmnopQRstUVWxyz") == 0
    assert candidate(word = "Python3.8") == 0
    assert candidate(word = "aAbBC") == 2
    assert candidate(word = "worldWORLD") == 5
    assert candidate(word = "xylophoneXYZ") == 2
    assert candidate(word = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 26
    assert candidate(word = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM") == 26
    assert candidate(word = "nestedCASECASEnested") == 2
    assert candidate(word = "aAaAaAaAaAaAaAaAaAaA") == 1
    assert candidate(word = "SpecialsAllOverAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 26
    assert candidate(word = "AbCdefGhIjkLmnopQrstUVwXyZ") == 0
    assert candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") == 26
    assert candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 1
    assert candidate(word = "UPPERlower") == 2
    assert candidate(word = "zZyYxXwWvVuUtTsSrRpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == 25
    assert candidate(word = "NoSpecial") == 0
    assert candidate(word = "SpecialCharacters123") == 2
    assert candidate(word = "OneSpecialA") == 1
    assert candidate(word = "SingleSpeciala") == 0
    assert candidate(word = "AbcDeEfGhIjKlMnOpQrStUvWxYz") == 1
    assert candidate(word = "helloHELLO") == 4
    assert candidate(word = "HelloWorld") == 0
    assert candidate(word = "MultipleUUppercases") == 1
    assert candidate(word = "wWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwWwW") == 1
    assert candidate(word = "yYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyYyY") == 1
    assert candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYzAbCdEfGhIjKlMnOpQrStUvWxYz") == 0
    assert candidate(word = "TrailingSpecialsAaBbCc") == 4
    assert candidate(word = "abcABCabcABCabcABC") == 3
    assert candidate(word = "JustOneSpecialCharacterb") == 2
    assert candidate(word = "iIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiI") == 1
    assert candidate(word = "noSpecial") == 0
    assert candidate(word = "NoSpecialCharacters") == 2
    assert candidate(word = "SpecialCharacters") == 2
    assert candidate(word = "lowerCASEuppercase") == 4
    assert candidate(word = "UniqueUniqueUniqueUnique") == 1
    assert candidate(word = "CASEsensitive") == 2
    assert candidate(word = "OneSpecialAa") == 1
    assert candidate(word = "SingleSpecialA") == 1
    assert candidate(word = "jJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJ") == 1
    assert candidate(word = "bBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbB") == 1
    assert candidate(word = "aabbCCddeeffGGhhiiJJkkllMMnnooppQQrrssttuuVVwwxxyyzz") == 0
    assert candidate(word = "MultipleMultipleMultiple") == 0
    assert candidate(word = "ComplexMixAaBbCc123!@#AaBbCc") == 4
    assert candidate(word = "TestCase") == 1
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 26
    assert candidate(word = "mMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmMmM") == 1
    assert candidate(word = "NestedSpecialsAaBBbbCCcc") == 4
    assert candidate(word = "fFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFfFf") == 1
    assert candidate(word = "lLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlLlL") == 1
    assert candidate(word = "tTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtTtT") == 1
    assert candidate(word = "abcdEFGHijKLMnopQRSTuvWXyz") == 0
    assert candidate(word = "JustOneAa") == 1
    assert candidate(word = "nNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnNnN") == 1
    assert candidate(word = "StartingWithSpecialsAaBbCc") == 4
    assert candidate(word = "uniqueUnique") == 1
    assert candidate(word = "gGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgGgG") == 1
    assert candidate(word = "xXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX") == 1
    assert candidate(word = "AaAaAaAaAaBbBbBbBbCcCcCcCcDdDdDdDdEeEeEeEeFfFfFfFfGgGgGgGgHhHhHhHhIiIiIiIiJjJjJjJjKkKkKkKkLlLlLlLlMmMmMmMmNnNnNnNnOoOoOoOoPpPpPpPpQqQqQqQqRrRrRrRrSsSsSsSsTtTtTtTtUuUuUuUuVvVvVvVvWwWwWwWwXxXxXxXxYyYyYyYyZzZzZzZz") == 26
    assert candidate(word = "specialCharSPECIAL") == 7
    assert candidate(word = "hHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhHhH") == 1
    assert candidate(word = "AlphabetSoup") == 1
    assert candidate(word = "AaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa") == 1
    assert candidate(word = "RepeatRepeatREPEAT") == 4
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ") == 1
    assert candidate(word = "pPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpPpP") == 1
    assert candidate(word = "aA1Bb2Cc3Dd4Ee5Ff6Gg7Hh8Ii9Jj0") == 10
    assert candidate(word = "specialCharacters") == 1
    assert candidate(word = "sSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsSsS") == 1
    assert candidate(word = "aAaAaA") == 1
    assert candidate(word = "JustOneZz") == 1
    assert candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCc") == 26
    assert candidate(word = "Zebra") == 0
    assert candidate(word = "EndingWithSpecialsAaBbCc") == 5
    assert candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZ") == 0
    assert candidate(word = "bbbbbbbbBBBBBBB") == 1
    assert candidate(word = "RePeAtInGChaRaCtErS") == 3
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzABCD") == 4
    assert candidate(word = "AaBbCc1234567890!@#$%^&*()") == 3
    assert candidate(word = "repeatedCHARactersCHARacters") == 3
    assert candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzabcdefghijklmnopqrstuvwxyz") == 26
    assert candidate(word = "UniqueCASE") == 2
    assert candidate(word = "doubleDOUBLEtrouble") == 6
    assert candidate(word = "PythonIsAwesome") == 0
    assert candidate(word = "MixedCASE123") == 1
    assert candidate(word = "QwErTyUiOpAsDfGhJkLzXcVbNm") == 0
    assert candidate(word = "rRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrRrR") == 1
    assert candidate(word = "abCDefGHijKLmnopQRstUVwxYZ") == 0
    assert candidate(word = "abcABCdefDEFghiGHI") == 9
    assert candidate(word = "pythonPYTHON") == 6
    assert candidate(word = "OverlapOverlap") == 0
    assert candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZ") == 0
    assert candidate(word = "CASEcase") == 4
    assert candidate(word = "testCaseTestCase") == 1
    assert candidate(word = "specialCHARSareHERE") == 5
    assert candidate(word = "SingleSpecialAa") == 1
    assert candidate(word = "qQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQqQ") == 1
    assert candidate(word = "aaBBccDDeeFFggHHiiJJkkLLmmNNooPPqqRRssTTuuVVwwXXyyZZ") == 0
    assert candidate(word = "dDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDdDd") == 1
    assert candidate(word = "SsEeCcIiAaLlTtCcHaArAcCtTeErsRsS") == 8
    assert candidate(word = "JustOneSpecialCharacterB") == 2
    assert candidate(word = "bBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbB") == 1
    assert candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa") == 1
    assert candidate(word = "NoRepeatsJustSpecialsAaBbCc") == 4
    assert candidate(word = "MiXeDcAsEwItHiSmOvEs") == 4
    assert candidate(word = "HelloWORLD") == 2
    assert candidate(word = "SpecialCharactersTEST") == 4
    assert candidate(word = "ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa") == 26
    assert candidate(word = "oOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoO") == 1
    assert candidate(word = "SpecialCHARacters") == 4
    assert candidate(word = "zZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZ") == 1
    assert candidate(word = "MultiplELowercases") == 2
    assert candidate(word = "AabbCCddeEFFgghhIIjjKKllMMnnooppQQrrSsttUuvvWwXxyyZz") == 7
    assert candidate(word = "MiXeDcAsE123") == 1
    assert candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 26
    assert candidate(word = "OverlapAaBbCcAaBbCc") == 3
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 0
    assert candidate(word = "uniqueUnIQUE") == 4
    assert candidate(word = "helloWorldHELLO") == 4
    assert candidate(word = "specialSPECIAL") == 7
    assert candidate(word = "PythonProgramming") == 0
    assert candidate(word = "cCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCc") == 1
    assert candidate(word = "uUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuUuU") == 1
    assert candidate(word = "SpecialAndNormalChars123!@#") == 4
    assert candidate(word = "Mississippi") == 0
    assert candidate(word = "MixedCASEWithSOMEspecial") == 4
    assert candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890") == 26
    assert candidate(word = "NoSpecialHere") == 0
    assert candidate(word = "aaaaaaaaaAAAAAA") == 1


