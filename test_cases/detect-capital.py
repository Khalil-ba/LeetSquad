def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "AB") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AB") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "Python") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Python") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "python") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "python") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "USA") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "USA") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "ab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ab") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "hello") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "hello") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "gOOgle") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "gOOgle") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "Leetcode") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Leetcode") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABcD") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABcD") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "Google") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Google") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbcD") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbcD") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "a") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "A") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "A") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "leetcode") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "leetcode") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "HELLO") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HELLO") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "HelloWorld") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HelloWorld") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "FlaG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FlaG") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "HELloworld") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HELloworld") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "INSTAGRAMSERVICES") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INSTAGRAMSERVICES") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "mNoPqR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mNoPqR") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "FACEBOOK") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FACEBOOK") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "cYbErSeCUrIty") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cYbErSeCUrIty") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "RoaDmAP") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RoaDmAP") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AmaZoN") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AmaZoN") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "Aaaaaaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Aaaaaaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "QwErTyUiOp") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "QwErTyUiOp") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghij") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghij") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "INTERNET") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INTERNET") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "M") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "M") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "pRoGrAmMiNg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pRoGrAmMiNg") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "rANDOMIZE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "rANDOMIZE") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aMAzOaN") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aMAzOaN") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aNIMaTiOn") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aNIMaTiOn") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "dEveLopMeNt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "dEveLopMeNt") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "SNAPCHATWEB") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SNAPCHATWEB") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "SiMpLe") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SiMpLe") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aBCdEfGhI") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aBCdEfGhI") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCdEfGh") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCdEfGh") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "wEb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "wEb") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "sWift") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "sWift") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "TeChNiCaL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TeChNiCaL") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "bUG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bUG") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "sUpErCaLiFrAgIlIsTiCcExPiAlIdOiCiOuS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "sUpErCaLiFrAgIlIsTiCcExPiAlIdOiCiOuS") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "GoogleIsAmazing") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "GoogleIsAmazing") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AlibabaCloud") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AlibabaCloud") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCdEfGhIj") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCdEfGhIj") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "flag") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "flag") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "SNAPCHAT") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SNAPCHAT") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "alibaba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "alibaba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "lower") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lower") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "internationalization") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "internationalization") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABCDEFGHijklmnopqrstuvwxyz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABCDEFGHijklmnopqrstuvwxyz") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "cLoudCOmPUTInG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cLoudCOmPUTInG") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "world") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "world") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbcDefGhIjKlMnopQrstUvWxyZ") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbcDefGhIjKlMnopQrstUvWxyZ") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "TitleCase") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TitleCase") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "FLICKRWEB") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FLICKRWEB") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "HaRdWaRE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HaRdWaRE") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "fAceBoOk") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "fAceBoOk") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "JupyTeR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "JupyTeR") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "PYTHON") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PYTHON") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "CdEf") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CdEf") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "SuperCalifragilisticexpialidocious") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SuperCalifragilisticexpialidocious") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "MachiNeLEARNING") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MachiNeLEARNING") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "Internationalization") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Internationalization") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "APPLECOMPUTER") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "APPLECOMPUTER") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "eNd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "eNd") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "machinelearning") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "machinelearning") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "AuDiO") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AuDiO") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAaAaA") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAaAaA") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYzA") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYzA") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "iNTERNATIONALIZATION") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "iNTERNATIONALIZATION") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "pRoJeCt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pRoJeCt") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "FLICKR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FLICKR") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwen") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwen") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "lAnGuAgE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lAnGuAgE") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "physICs") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "physICs") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "cSHaRp") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cSHaRp") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "EDiToR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EDiToR") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "FaCeBoOk") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FaCeBoOk") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aB") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aB") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "oNE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "oNE") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aNATOMy") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aNATOMy") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "QwErTyUiOpAsDfGhJkLzXcVbNm") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "QwErTyUiOpAsDfGhJkLzXcVbNm") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "FACEBOOKINSTAGRAM") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FACEBOOKINSTAGRAM") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZ") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZ") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "MaChInE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MaChInE") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABc") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "java") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "java") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "CoMpLiCATED") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CoMpLiCATED") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "gOOGLE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "gOOGLE") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AMAZONWEB") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AMAZONWEB") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "Alibaba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Alibaba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "pROGRaMMiNG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pROGRaMMiNG") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "xMl") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xMl") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "RaDIo") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RaDIo") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "INternationalization") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INternationalization") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "iNtErNaTioNaL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "iNtErNaTioNaL") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "uSeR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uSeR") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "INSTAGRAM") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INSTAGRAM") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCdEfGhIjKlMnOpQrSt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCdEfGhIjKlMnOpQrSt") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABCDEFGHIjklmnopqr") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABCDEFGHIjklmnopqr") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "Zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "lowercase") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lowercase") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "MuSiC") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MuSiC") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "fAcEboOk") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "fAcEboOk") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "YOUTUBESERVICES") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "YOUTUBESERVICES") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aPpLiCaTiOn") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aPpLiCaTiOn") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "Ba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Ba") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "s") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "s") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCdEfGhIjKlMnOp") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCdEfGhIjKlMnOp") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "yOuTuBe") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "yOuTuBe") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "fRoM") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "fRoM") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "gRaphIcS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "gRaphIcS") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "cGraPhIcs") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cGraPhIcs") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "eCONoMiCS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "eCONoMiCS") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "SiNgEr") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SiNgEr") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefgh") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefgh") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "PRoDUCeR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PRoDUCeR") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "vIdEoGaMe") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "vIdEoGaMe") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "GOOGLESERVICES") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "GOOGLESERVICES") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "Z") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Z") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "z") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "z") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "BuSINESSiNTelligence") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "BuSINESSiNTelligence") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "EBAY") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EBAY") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "rEddIt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "rEddIt") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "CAPITALIZATION") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CAPITALIZATION") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "wOrLd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "wOrLd") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijKlmnopqrSTUVWXyz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijKlmnopqrSTUVWXyz") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "InValid") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "InValid") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "data") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "data") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "TWo") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TWo") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "wEbDeVeLopMeNt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "wEbDeVeLopMeNt") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "cDEF") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cDEF") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "RUsT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RUsT") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "MICROSOFTAZURE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MICROSOFTAZURE") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "MiCROsOfT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MiCROsOfT") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "UPPERlower") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "UPPERlower") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "MICROSOFTCLOUD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MICROSOFTCLOUD") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "openAI") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "openAI") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ViDIoGraPhEr") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ViDIoGraPhEr") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "YouTube") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "YouTube") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "hACK") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "hACK") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "Ab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Ab") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "jSoN") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jSoN") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "DiReCtOr") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DiReCtOr") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aPPlE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aPPlE") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ZyxWvuTsRqPoNmLkJiHgFeDcBa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ZyxWvuTsRqPoNmLkJiHgFeDcBa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "FACEBOOKWEB") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FACEBOOKWEB") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbcDefGhIjKlMnopQrstUvWxyz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbcDefGhIjKlMnopQrstUvWxyz") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "WRiTeR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "WRiTeR") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "tELEviSiOn") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "tELEviSiOn") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "FLICKRSERVICES") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FLICKRSERVICES") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "YOUTUBE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "YOUTUBE") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "ai") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ai") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "TUMBLRSERVICES") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TUMBLRSERVICES") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "artificialintelligence") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "artificialintelligence") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "bUiLd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bUiLd") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "gAmEs") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "gAmEs") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "GOOGLEWEB") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "GOOGLEWEB") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "PHp") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PHp") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "applecomputer") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "applecomputer") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "openai") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "openai") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "LoWeRuPPeR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LoWeRuPPeR") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ArtificialIntelligence") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ArtificialIntelligence") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "qwenai") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qwenai") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "TyPeScRiPT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TyPeScRiPT") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "wEbSiTe") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "wEbSiTe") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "pRoGrAmMaR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pRoGrAmMaR") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AMericA") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AMericA") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCdEfGhIjKl") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCdEfGhIjKl") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "cOdInG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cOdInG") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "SPSS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SPSS") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "JAVA") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "JAVA") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "hELLO") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "hELLO") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "PsYCHOLOgY") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PsYCHOLOgY") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aBcDeFgHiJ") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aBcDeFgHiJ") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "allUPPER") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "allUPPER") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "Defg") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Defg") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "tHISISATEST") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "tHISISATEST") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "TUMBLR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TUMBLR") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "OpenAI") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "OpenAI") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "wHiTtEr") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "wHiTtEr") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "PyThOnPrOgRaM") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PyThOnPrOgRaM") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "LeArNiNg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LeArNiNg") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AMAZONWEBSERVICES") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AMAZONWEBSERVICES") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "iOS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "iOS") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "FLaG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FLaG") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "QWENAI") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "QWENAI") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "bAcK") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bAcK") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ALLUPPERCASE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ALLUPPERCASE") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "SAP") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SAP") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "UPPERCASE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "UPPERCASE") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "STATA") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "STATA") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "FlAG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FlAG") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "SlAcK") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SlAcK") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "NeWs") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "NeWs") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "vIsUAlsTuDiOs") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "vIsUAlsTuDiOs") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "tWItTeR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "tWItTeR") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "LINKEDINSERVICES") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LINKEDINSERVICES") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "RuBuY") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RuBuY") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "THISISATEST") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "THISISATEST") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "ThIsIsAtEsT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ThIsIsAtEsT") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AAAAAAAAA") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AAAAAAAAA") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "AlLcaPslOcK") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AlLcaPslOcK") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "gOOgLE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "gOOgLE") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "PyThOn") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PyThOn") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "HELLOworld") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HELLOworld") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "MaThS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MaThS") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCdEfGhIjKlMnOpQrStUvWx") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCdEfGhIjKlMnOpQrStUvWx") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "tHIsSHOULDBEFalse") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "tHIsSHOULDBEFalse") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "Qwen") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Qwen") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "INTERNationalIZATION") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INTERNationalIZATION") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "PhYSIOlOGy") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PhYSIOlOGy") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "dEfInE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "dEfInE") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "MiXeD123") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MiXeD123") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "SNAPCHATSERVICES") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SNAPCHATSERVICES") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCDeFgHiJkLmNoPqRsTuVwXyZ") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCDeFgHiJkLmNoPqRsTuVwXyZ") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "GOOGLE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "GOOGLE") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "WRiTEr") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "WRiTEr") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AcTReSS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AcTReSS") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "gOOD") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "gOOD") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYz") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ArTIFICiALiNTelligence") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ArTIFICiALiNTelligence") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCd") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ValidCapital") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ValidCapital") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "microsoft") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "microsoft") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "LINKEDIN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LINKEDIN") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "EBAYSERVICES") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EBAYSERVICES") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "AMAZON") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AMAZON") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCdEf") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCdEf") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ORAcLe") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ORAcLe") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AMaZiNg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AMaZiNg") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "NeURALnETWORKS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "NeURALnETWORKS") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "mNopQr") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mNopQr") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ALIBABA") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ALIBABA") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "america") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "america") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "cOdE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cOdE") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "HTmL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "HTmL") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "GoogleSearch") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "GoogleSearch") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ThisIsATest") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ThisIsATest") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "DROPBOXWEB") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DROPBOXWEB") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "MACHINELEARNING") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MACHINELEARNING") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "Go") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Go") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "tEsT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "tEsT") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "gRaPhiCs") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "gRaPhiCs") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "OPENAI") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "OPENAI") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "DataSCIENCE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DataSCIENCE") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "hISToRY") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "hISToRY") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "oneTWOthreeFOUR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "oneTWOthreeFOUR") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "TUMBLRWEB") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TUMBLRWEB") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "MaNaGeR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MaNaGeR") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "mAkE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mAkE") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "mEsSeNger") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mEsSeNger") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "RoBOtIcs") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RoBOtIcs") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "sUPERCALIFRAGILISTICEXPIALIDOCIOUS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "sUPERCALIFRAGILISTICEXPIALIDOCIOUS") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCdEfGhIjKlMnOpQr") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCdEfGhIjKlMnOpQr") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "m") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "m") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "sOFTwaRE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "sOFTwaRE") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCdEfGhIjKlMn") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCdEfGhIjKlMn") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AI") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AI") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "RaCT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "RaCT") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "BingSearchEngine") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "BingSearchEngine") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ARTIFICIALINTELLIGENCE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ARTIFICIALINTELLIGENCE") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "oPeN") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "oPeN") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "mOVie") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mOVie") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AA") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AA") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqr") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqr") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "Aa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Aa") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "TWITTER") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TWITTER") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aLGoRiTHMs") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aLGoRiTHMs") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "tO") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "tO") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ZzZ") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ZzZ") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "MACHINE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MACHINE") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "GoOgLe") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "GoOgLe") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "INFORMATIONtechnology") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INFORMATIONtechnology") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "JSAvAsCrIpT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "JSAvAsCrIpT") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "kOTlIN") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "kOTlIN") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "MuSiCiAn") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MuSiCiAn") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "machine") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "machine") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "tIKtOk") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "tIKtOk") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopQR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopQR") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "yAmL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "yAmL") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abCdEfGhIjKlMnOpQrStUvWxYz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abCdEfGhIjKlMnOpQrStUvWxYz") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "singleLETTER") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "singleLETTER") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "youtube") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "youtube") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "sNAPcHaT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "sNAPcHaT") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "apple") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "apple") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCdEfGhIjKlMnOpQrStUv") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCdEfGhIjKlMnOpQrStUv") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "cODe") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cODe") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "cINeMa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cINeMa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "MICROSOFTWEB") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MICROSOFTWEB") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "alllower") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "alllower") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "THISisAteSt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "THISisAteSt") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "FLAG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FLAG") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "Data") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Data") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "OnEtwOthReEfOuR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "OnEtwOthReEfOuR") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "pRoGrEsS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pRoGrEsS") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABCDEFGH") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABCDEFGH") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "TWITTERWEB") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TWITTERWEB") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "leetCODe") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "leetCODe") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "fLAG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "fLAG") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "bA") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bA") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijKLMNOPQR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijKLMNOPQR") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "DISCoRd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DISCoRd") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "MakE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MakE") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "bing") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bing") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "gOOGLe") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "gOOGLe") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "vErSiOn") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "vErSiOn") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "eXpEriEnCe") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "eXpEriEnCe") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ThrEE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ThrEE") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "wItH") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "wItH") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "mICROSOFT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mICROSOFT") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "MaCHiNeViSiOn") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MaCHiNeViSiOn") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "qUaNtuMCoMpUtInG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "qUaNtuMCoMpUtInG") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "APPLEpie") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "APPLEpie") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AaAaAa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AaAaAa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "SAS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "SAS") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "MicroSoft") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MicroSoft") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "DaTaANaLYsIS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DaTaANaLYsIS") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "EBAYWEB") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "EBAYWEB") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "MiXeDLoWeRuPpEr") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MiXeDLoWeRuPpEr") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "MATLAB") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MATLAB") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "CamelCase") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CamelCase") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "micro") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "micro") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "onELETTER") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "onELETTER") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "MiCroSoFt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MiCroSoFt") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "fACeBoOk") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "fACeBoOk") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "DATA") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DATA") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "TWITTERSERVICES") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TWITTERSERVICES") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "sOuRcE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "sOuRcE") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "DEFG") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DEFG") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "CAPITAL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CAPITAL") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "JAVa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "JAVa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "dEsIgN") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "dEsIgN") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "FLAGship") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "FLAGship") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "BING") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "BING") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "QwertyUiopAsDfGhJkLzXcVbNm") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "QwertyUiopAsDfGhJkLzXcVbNm") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "GOOGLECLOUD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "GOOGLECLOUD") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "alibabacloud") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "alibabacloud") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "DeBuGgInG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DeBuGgInG") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "MIXEDcase") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MIXEDcase") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ApPlE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ApPlE") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "TwItTeR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TwItTeR") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ONE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ONE") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "cOMPUTERsCIENCE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cOMPUTERsCIENCE") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "PythonProgram") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PythonProgram") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "zXcVbNmKlJ") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zXcVbNmKlJ") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "QwenAI") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "QwenAI") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "NeTwORkS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "NeTwORkS") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ZePpElIn") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ZePpElIn") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AcTOr") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AcTOr") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "zYxWVuTsRqPoNmLkJiHgFeDcBa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zYxWVuTsRqPoNmLkJiHgFeDcBa") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "vIsIoN") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "vIsIoN") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "Three") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Three") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "INSTaGram") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INSTaGram") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "two") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "two") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "AMERICA") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AMERICA") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "MixedCASE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MixedCASE") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "jOuRnaLiSm") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "jOuRnaLiSm") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "lInKeDin") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "lInKeDin") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "AlGoRiThMs") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AlGoRiThMs") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "JaVaScRiPt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "JaVaScRiPt") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "INSTAGRAMFACEBOOK") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INSTAGRAMFACEBOOK") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "DeEPLEaRNING") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DeEPLEaRNING") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "APPLE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "APPLE") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "aNdRoId") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aNdRoId") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "LeetCode") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LeetCode") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "DROPBOX") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DROPBOX") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "Valid") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Valid") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "LINKEDINWEB") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LINKEDINWEB") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "INSTAGRAMWEB") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INSTAGRAMWEB") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "MachineLearning") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "MachineLearning") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "ALIBABACLOUD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ALIBABACLOUD") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "DataScience") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DataScience") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "CAPITALS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CAPITALS") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "oneTWOthree") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "oneTWOthree") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "YOUTUBEWEB") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "YOUTUBEWEB") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "LEETCODE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "LEETCODE") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "tWiTtEr") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "tWiTtEr") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "thisisatest") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "thisisatest") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "sCALA") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "sCALA") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "bLoGgInG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bLoGgInG") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "alllowercase") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "alllowercase") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "TeStCaSe") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "TeStCaSe") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "QWEN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "QWEN") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "cSs") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cSs") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAaAaAaAaA") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAaAaAaAaA") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "Supercalifragilisticexpialidocious") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Supercalifragilisticexpialidocious") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABCDEFGHIJ") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABCDEFGHIJ") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "INfOrMaTiOnSYsTEMS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "INfOrMaTiOnSYsTEMS") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "pInTeReSt") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "pInTeReSt") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "DROPBOXSERVICES") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "DROPBOXSERVICES") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "nOcaPslOcK") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "nOcaPslOcK") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "PERL") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "PERL") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "CoMpUtEr") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "CoMpUtEr") == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "AB") == True
    assert candidate(word = "Python") == True
    assert candidate(word = "python") == True
    assert candidate(word = "USA") == True
    assert candidate(word = "ab") == True
    assert candidate(word = "hello") == True
    assert candidate(word = "gOOgle") == False
    assert candidate(word = "Leetcode") == True
    assert candidate(word = "ABcD") == False
    assert candidate(word = "Google") == True
    assert candidate(word = "AbcD") == False
    assert candidate(word = "a") == True
    assert candidate(word = "A") == True
    assert candidate(word = "leetcode") == True
    assert candidate(word = "HELLO") == True
    assert candidate(word = "HelloWorld") == False
    assert candidate(word = "FlaG") == False
    assert candidate(word = "HELloworld") == False
    assert candidate(word = "INSTAGRAMSERVICES") == True
    assert candidate(word = "mNoPqR") == False
    assert candidate(word = "FACEBOOK") == True
    assert candidate(word = "cYbErSeCUrIty") == False
    assert candidate(word = "RoaDmAP") == False
    assert candidate(word = "AmaZoN") == False
    assert candidate(word = "Aaaaaaaaa") == True
    assert candidate(word = "QwErTyUiOp") == False
    assert candidate(word = "abcdefghij") == True
    assert candidate(word = "INTERNET") == True
    assert candidate(word = "M") == True
    assert candidate(word = "pRoGrAmMiNg") == False
    assert candidate(word = "rANDOMIZE") == False
    assert candidate(word = "aMAzOaN") == False
    assert candidate(word = "aNIMaTiOn") == False
    assert candidate(word = "dEveLopMeNt") == False
    assert candidate(word = "SNAPCHATWEB") == True
    assert candidate(word = "SiMpLe") == False
    assert candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") == False
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == False
    assert candidate(word = "aBCdEfGhI") == False
    assert candidate(word = "AbCdEfGh") == False
    assert candidate(word = "wEb") == False
    assert candidate(word = "sWift") == False
    assert candidate(word = "TeChNiCaL") == False
    assert candidate(word = "bUG") == False
    assert candidate(word = "sUpErCaLiFrAgIlIsTiCcExPiAlIdOiCiOuS") == False
    assert candidate(word = "GoogleIsAmazing") == False
    assert candidate(word = "AlibabaCloud") == False
    assert candidate(word = "AbCdEfGhIj") == False
    assert candidate(word = "flag") == True
    assert candidate(word = "SNAPCHAT") == True
    assert candidate(word = "alibaba") == True
    assert candidate(word = "lower") == True
    assert candidate(word = "internationalization") == True
    assert candidate(word = "ABCDEFGHijklmnopqrstuvwxyz") == False
    assert candidate(word = "cLoudCOmPUTInG") == False
    assert candidate(word = "world") == True
    assert candidate(word = "AbcDefGhIjKlMnopQrstUvWxyZ") == False
    assert candidate(word = "TitleCase") == False
    assert candidate(word = "FLICKRWEB") == True
    assert candidate(word = "HaRdWaRE") == False
    assert candidate(word = "fAceBoOk") == False
    assert candidate(word = "JupyTeR") == False
    assert candidate(word = "PYTHON") == True
    assert candidate(word = "CdEf") == False
    assert candidate(word = "SuperCalifragilisticexpialidocious") == False
    assert candidate(word = "MachiNeLEARNING") == False
    assert candidate(word = "Internationalization") == True
    assert candidate(word = "APPLECOMPUTER") == True
    assert candidate(word = "eNd") == False
    assert candidate(word = "machinelearning") == True
    assert candidate(word = "AuDiO") == False
    assert candidate(word = "aAaAaA") == False
    assert candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYzA") == False
    assert candidate(word = "iNTERNATIONALIZATION") == False
    assert candidate(word = "pRoJeCt") == False
    assert candidate(word = "FLICKR") == True
    assert candidate(word = "qwen") == True
    assert candidate(word = "lAnGuAgE") == False
    assert candidate(word = "physICs") == False
    assert candidate(word = "cSHaRp") == False
    assert candidate(word = "EDiToR") == False
    assert candidate(word = "FaCeBoOk") == False
    assert candidate(word = "aB") == False
    assert candidate(word = "oNE") == False
    assert candidate(word = "aNATOMy") == False
    assert candidate(word = "QwErTyUiOpAsDfGhJkLzXcVbNm") == False
    assert candidate(word = "FACEBOOKINSTAGRAM") == True
    assert candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZ") == False
    assert candidate(word = "MaChInE") == False
    assert candidate(word = "ABc") == False
    assert candidate(word = "java") == True
    assert candidate(word = "CoMpLiCATED") == False
    assert candidate(word = "gOOGLE") == False
    assert candidate(word = "AMAZONWEB") == True
    assert candidate(word = "Alibaba") == True
    assert candidate(word = "pROGRaMMiNG") == False
    assert candidate(word = "xMl") == False
    assert candidate(word = "RaDIo") == False
    assert candidate(word = "INternationalization") == False
    assert candidate(word = "iNtErNaTioNaL") == False
    assert candidate(word = "uSeR") == False
    assert candidate(word = "INSTAGRAM") == True
    assert candidate(word = "AbCdEfGhIjKlMnOpQrSt") == False
    assert candidate(word = "ABCDEFGHIjklmnopqr") == False
    assert candidate(word = "Zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == True
    assert candidate(word = "lowercase") == True
    assert candidate(word = "MuSiC") == False
    assert candidate(word = "fAcEboOk") == False
    assert candidate(word = "YOUTUBESERVICES") == True
    assert candidate(word = "aPpLiCaTiOn") == False
    assert candidate(word = "Ba") == True
    assert candidate(word = "s") == True
    assert candidate(word = "AbCdEfGhIjKlMnOp") == False
    assert candidate(word = "yOuTuBe") == False
    assert candidate(word = "fRoM") == False
    assert candidate(word = "gRaphIcS") == False
    assert candidate(word = "cGraPhIcs") == False
    assert candidate(word = "eCONoMiCS") == False
    assert candidate(word = "SiNgEr") == False
    assert candidate(word = "abcdefgh") == True
    assert candidate(word = "PRoDUCeR") == False
    assert candidate(word = "vIdEoGaMe") == False
    assert candidate(word = "GOOGLESERVICES") == True
    assert candidate(word = "Z") == True
    assert candidate(word = "z") == True
    assert candidate(word = "BuSINESSiNTelligence") == False
    assert candidate(word = "EBAY") == True
    assert candidate(word = "rEddIt") == False
    assert candidate(word = "CAPITALIZATION") == True
    assert candidate(word = "wOrLd") == False
    assert candidate(word = "abcdefghijKlmnopqrSTUVWXyz") == False
    assert candidate(word = "InValid") == False
    assert candidate(word = "data") == True
    assert candidate(word = "TWo") == False
    assert candidate(word = "wEbDeVeLopMeNt") == False
    assert candidate(word = "cDEF") == False
    assert candidate(word = "RUsT") == False
    assert candidate(word = "MICROSOFTAZURE") == True
    assert candidate(word = "MiCROsOfT") == False
    assert candidate(word = "UPPERlower") == False
    assert candidate(word = "MICROSOFTCLOUD") == True
    assert candidate(word = "openAI") == False
    assert candidate(word = "ViDIoGraPhEr") == False
    assert candidate(word = "YouTube") == False
    assert candidate(word = "hACK") == False
    assert candidate(word = "Ab") == True
    assert candidate(word = "jSoN") == False
    assert candidate(word = "DiReCtOr") == False
    assert candidate(word = "aPPlE") == False
    assert candidate(word = "ZyxWvuTsRqPoNmLkJiHgFeDcBa") == False
    assert candidate(word = "FACEBOOKWEB") == True
    assert candidate(word = "AbcDefGhIjKlMnopQrstUvWxyz") == False
    assert candidate(word = "WRiTeR") == False
    assert candidate(word = "tELEviSiOn") == False
    assert candidate(word = "FLICKRSERVICES") == True
    assert candidate(word = "YOUTUBE") == True
    assert candidate(word = "ai") == True
    assert candidate(word = "TUMBLRSERVICES") == True
    assert candidate(word = "artificialintelligence") == True
    assert candidate(word = "bUiLd") == False
    assert candidate(word = "gAmEs") == False
    assert candidate(word = "GOOGLEWEB") == True
    assert candidate(word = "PHp") == False
    assert candidate(word = "applecomputer") == True
    assert candidate(word = "openai") == True
    assert candidate(word = "LoWeRuPPeR") == False
    assert candidate(word = "ArtificialIntelligence") == False
    assert candidate(word = "qwenai") == True
    assert candidate(word = "TyPeScRiPT") == False
    assert candidate(word = "wEbSiTe") == False
    assert candidate(word = "pRoGrAmMaR") == False
    assert candidate(word = "AMericA") == False
    assert candidate(word = "AbCdEfGhIjKl") == False
    assert candidate(word = "cOdInG") == False
    assert candidate(word = "SPSS") == True
    assert candidate(word = "JAVA") == True
    assert candidate(word = "hELLO") == False
    assert candidate(word = "PsYCHOLOgY") == False
    assert candidate(word = "aBcDeFgHiJ") == False
    assert candidate(word = "allUPPER") == False
    assert candidate(word = "Defg") == True
    assert candidate(word = "tHISISATEST") == False
    assert candidate(word = "TUMBLR") == True
    assert candidate(word = "OpenAI") == False
    assert candidate(word = "wHiTtEr") == False
    assert candidate(word = "PyThOnPrOgRaM") == False
    assert candidate(word = "LeArNiNg") == False
    assert candidate(word = "AMAZONWEBSERVICES") == True
    assert candidate(word = "iOS") == False
    assert candidate(word = "FLaG") == False
    assert candidate(word = "QWENAI") == True
    assert candidate(word = "bAcK") == False
    assert candidate(word = "ALLUPPERCASE") == True
    assert candidate(word = "SAP") == True
    assert candidate(word = "UPPERCASE") == True
    assert candidate(word = "STATA") == True
    assert candidate(word = "FlAG") == False
    assert candidate(word = "SlAcK") == False
    assert candidate(word = "NeWs") == False
    assert candidate(word = "vIsUAlsTuDiOs") == False
    assert candidate(word = "tWItTeR") == False
    assert candidate(word = "LINKEDINSERVICES") == True
    assert candidate(word = "RuBuY") == False
    assert candidate(word = "THISISATEST") == True
    assert candidate(word = "ThIsIsAtEsT") == False
    assert candidate(word = "AAAAAAAAA") == True
    assert candidate(word = "AlLcaPslOcK") == False
    assert candidate(word = "gOOgLE") == False
    assert candidate(word = "PyThOn") == False
    assert candidate(word = "HELLOworld") == False
    assert candidate(word = "MaThS") == False
    assert candidate(word = "AbCdEfGhIjKlMnOpQrStUvWx") == False
    assert candidate(word = "tHIsSHOULDBEFalse") == False
    assert candidate(word = "Qwen") == True
    assert candidate(word = "INTERNationalIZATION") == False
    assert candidate(word = "PhYSIOlOGy") == False
    assert candidate(word = "dEfInE") == False
    assert candidate(word = "MiXeD123") == False
    assert candidate(word = "SNAPCHATSERVICES") == True
    assert candidate(word = "AbCDeFgHiJkLmNoPqRsTuVwXyZ") == False
    assert candidate(word = "GOOGLE") == True
    assert candidate(word = "WRiTEr") == False
    assert candidate(word = "AcTReSS") == False
    assert candidate(word = "gOOD") == False
    assert candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYz") == False
    assert candidate(word = "ArTIFICiALiNTelligence") == False
    assert candidate(word = "AbCd") == False
    assert candidate(word = "ValidCapital") == False
    assert candidate(word = "microsoft") == True
    assert candidate(word = "LINKEDIN") == True
    assert candidate(word = "EBAYSERVICES") == True
    assert candidate(word = "AMAZON") == True
    assert candidate(word = "AbCdEf") == False
    assert candidate(word = "ORAcLe") == False
    assert candidate(word = "AMaZiNg") == False
    assert candidate(word = "NeURALnETWORKS") == False
    assert candidate(word = "mNopQr") == False
    assert candidate(word = "ALIBABA") == True
    assert candidate(word = "america") == True
    assert candidate(word = "cOdE") == False
    assert candidate(word = "HTmL") == False
    assert candidate(word = "GoogleSearch") == False
    assert candidate(word = "ThisIsATest") == False
    assert candidate(word = "DROPBOXWEB") == True
    assert candidate(word = "MACHINELEARNING") == True
    assert candidate(word = "Go") == True
    assert candidate(word = "tEsT") == False
    assert candidate(word = "gRaPhiCs") == False
    assert candidate(word = "OPENAI") == True
    assert candidate(word = "DataSCIENCE") == False
    assert candidate(word = "hISToRY") == False
    assert candidate(word = "oneTWOthreeFOUR") == False
    assert candidate(word = "TUMBLRWEB") == True
    assert candidate(word = "MaNaGeR") == False
    assert candidate(word = "mAkE") == False
    assert candidate(word = "mEsSeNger") == False
    assert candidate(word = "RoBOtIcs") == False
    assert candidate(word = "sUPERCALIFRAGILISTICEXPIALIDOCIOUS") == False
    assert candidate(word = "AbCdEfGhIjKlMnOpQr") == False
    assert candidate(word = "m") == True
    assert candidate(word = "sOFTwaRE") == False
    assert candidate(word = "AbCdEfGhIjKlMn") == False
    assert candidate(word = "AI") == True
    assert candidate(word = "RaCT") == False
    assert candidate(word = "BingSearchEngine") == False
    assert candidate(word = "ARTIFICIALINTELLIGENCE") == True
    assert candidate(word = "oPeN") == False
    assert candidate(word = "mOVie") == False
    assert candidate(word = "AA") == True
    assert candidate(word = "mnopqr") == True
    assert candidate(word = "Aa") == True
    assert candidate(word = "abc") == True
    assert candidate(word = "TWITTER") == True
    assert candidate(word = "aLGoRiTHMs") == False
    assert candidate(word = "tO") == False
    assert candidate(word = "ZzZ") == False
    assert candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == True
    assert candidate(word = "MACHINE") == True
    assert candidate(word = "GoOgLe") == False
    assert candidate(word = "INFORMATIONtechnology") == False
    assert candidate(word = "JSAvAsCrIpT") == False
    assert candidate(word = "kOTlIN") == False
    assert candidate(word = "MuSiCiAn") == False
    assert candidate(word = "machine") == True
    assert candidate(word = "tIKtOk") == False
    assert candidate(word = "mnopQR") == False
    assert candidate(word = "yAmL") == False
    assert candidate(word = "abCdEfGhIjKlMnOpQrStUvWxYz") == False
    assert candidate(word = "singleLETTER") == False
    assert candidate(word = "youtube") == True
    assert candidate(word = "sNAPcHaT") == False
    assert candidate(word = "apple") == True
    assert candidate(word = "AbCdEfGhIjKlMnOpQrStUv") == False
    assert candidate(word = "cODe") == False
    assert candidate(word = "cINeMa") == False
    assert candidate(word = "MICROSOFTWEB") == True
    assert candidate(word = "alllower") == True
    assert candidate(word = "THISisAteSt") == False
    assert candidate(word = "FLAG") == True
    assert candidate(word = "Data") == True
    assert candidate(word = "OnEtwOthReEfOuR") == False
    assert candidate(word = "pRoGrEsS") == False
    assert candidate(word = "ABCDEFGH") == True
    assert candidate(word = "TWITTERWEB") == True
    assert candidate(word = "leetCODe") == False
    assert candidate(word = "fLAG") == False
    assert candidate(word = "bA") == False
    assert candidate(word = "abcdefghijKLMNOPQR") == False
    assert candidate(word = "DISCoRd") == False
    assert candidate(word = "MakE") == False
    assert candidate(word = "bing") == True
    assert candidate(word = "gOOGLe") == False
    assert candidate(word = "vErSiOn") == False
    assert candidate(word = "eXpEriEnCe") == False
    assert candidate(word = "ThrEE") == False
    assert candidate(word = "wItH") == False
    assert candidate(word = "mICROSOFT") == False
    assert candidate(word = "MaCHiNeViSiOn") == False
    assert candidate(word = "qUaNtuMCoMpUtInG") == False
    assert candidate(word = "APPLEpie") == False
    assert candidate(word = "AaAaAa") == False
    assert candidate(word = "SAS") == True
    assert candidate(word = "MicroSoft") == False
    assert candidate(word = "DaTaANaLYsIS") == False
    assert candidate(word = "EBAYWEB") == True
    assert candidate(word = "MiXeDLoWeRuPpEr") == False
    assert candidate(word = "MATLAB") == True
    assert candidate(word = "CamelCase") == False
    assert candidate(word = "micro") == True
    assert candidate(word = "onELETTER") == False
    assert candidate(word = "MiCroSoFt") == False
    assert candidate(word = "fACeBoOk") == False
    assert candidate(word = "DATA") == True
    assert candidate(word = "TWITTERSERVICES") == True
    assert candidate(word = "sOuRcE") == False
    assert candidate(word = "DEFG") == True
    assert candidate(word = "CAPITAL") == True
    assert candidate(word = "JAVa") == False
    assert candidate(word = "dEsIgN") == False
    assert candidate(word = "FLAGship") == False
    assert candidate(word = "BING") == True
    assert candidate(word = "QwertyUiopAsDfGhJkLzXcVbNm") == False
    assert candidate(word = "GOOGLECLOUD") == True
    assert candidate(word = "alibabacloud") == True
    assert candidate(word = "DeBuGgInG") == False
    assert candidate(word = "MIXEDcase") == False
    assert candidate(word = "ApPlE") == False
    assert candidate(word = "TwItTeR") == False
    assert candidate(word = "ONE") == True
    assert candidate(word = "cOMPUTERsCIENCE") == False
    assert candidate(word = "PythonProgram") == False
    assert candidate(word = "zXcVbNmKlJ") == False
    assert candidate(word = "QwenAI") == False
    assert candidate(word = "NeTwORkS") == False
    assert candidate(word = "ZePpElIn") == False
    assert candidate(word = "AcTOr") == False
    assert candidate(word = "zYxWVuTsRqPoNmLkJiHgFeDcBa") == False
    assert candidate(word = "vIsIoN") == False
    assert candidate(word = "Three") == True
    assert candidate(word = "INSTaGram") == False
    assert candidate(word = "two") == True
    assert candidate(word = "AMERICA") == True
    assert candidate(word = "MixedCASE") == False
    assert candidate(word = "jOuRnaLiSm") == False
    assert candidate(word = "lInKeDin") == False
    assert candidate(word = "AlGoRiThMs") == False
    assert candidate(word = "JaVaScRiPt") == False
    assert candidate(word = "INSTAGRAMFACEBOOK") == True
    assert candidate(word = "DeEPLEaRNING") == False
    assert candidate(word = "APPLE") == True
    assert candidate(word = "aNdRoId") == False
    assert candidate(word = "LeetCode") == False
    assert candidate(word = "DROPBOX") == True
    assert candidate(word = "Valid") == True
    assert candidate(word = "LINKEDINWEB") == True
    assert candidate(word = "INSTAGRAMWEB") == True
    assert candidate(word = "abcdefghijklmnopqrstuvwxyz") == True
    assert candidate(word = "MachineLearning") == False
    assert candidate(word = "ALIBABACLOUD") == True
    assert candidate(word = "DataScience") == False
    assert candidate(word = "CAPITALS") == True
    assert candidate(word = "oneTWOthree") == False
    assert candidate(word = "YOUTUBEWEB") == True
    assert candidate(word = "LEETCODE") == True
    assert candidate(word = "tWiTtEr") == False
    assert candidate(word = "thisisatest") == True
    assert candidate(word = "sCALA") == False
    assert candidate(word = "bLoGgInG") == False
    assert candidate(word = "alllowercase") == True
    assert candidate(word = "TeStCaSe") == False
    assert candidate(word = "QWEN") == True
    assert candidate(word = "cSs") == False
    assert candidate(word = "aAaAaAaAaA") == False
    assert candidate(word = "Supercalifragilisticexpialidocious") == True
    assert candidate(word = "ABCDEFGHIJ") == True
    assert candidate(word = "INfOrMaTiOnSYsTEMS") == False
    assert candidate(word = "pInTeReSt") == False
    assert candidate(word = "DROPBOXSERVICES") == True
    assert candidate(word = "nOcaPslOcK") == False
    assert candidate(word = "PERL") == True
    assert candidate(word = "CoMpUtEr") == False


