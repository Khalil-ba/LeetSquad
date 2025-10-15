def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "mMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "zZyYxXwWeE") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zZyYxXwWeE") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "zZyYxXwWvVuUtTrRsSqQpPoOnNmMlLkKiIjJhHgGfFeEdDcCbBaA") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zZyYxXwWvVuUtTrRsSqQpPoOnNmMlLkKiIjJhHgGfFeEdDcCbBaA") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "bBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyY") == "Y"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyY") == "Y": {e}')
    
    total += 1
    try:
        result = candidate(s = "alluppercase") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "alluppercase") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "ALLLOWERCASE") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ALLLOWERCASE") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "AbCdEfGhIjK") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AbCdEfGhIjK") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "NoUpperCaseHere") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "NoUpperCaseHere") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "bA") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bA") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "AbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "NnOoPpQqRrSsTtUuVvWwXxYyZz") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "NnOoPpQqRrSsTtUuVvWwXxYyZz") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "lEeTcOdE") == "E"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lEeTcOdE") == "E": {e}')
    
    total += 1
    try:
        result = candidate(s = "aBcDeFgHiJkLmNoPqRsTuVwXyZ") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aBcDeFgHiJkLmNoPqRsTuVwXyZ") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "arRAzFif") == "R"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "arRAzFif") == "R": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgHIJKLMnoPQRSTuVwxyz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgHIJKLMnoPQRSTuVwxyz") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "QwErTyUiOpAsDfGhJkLzXcVbNm") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QwErTyUiOpAsDfGhJkLzXcVbNm") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aA") == "A"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aA") == "A": {e}')
    
    total += 1
    try:
        result = candidate(s = "A") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "A") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "AaBbCc") == "C"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AaBbCc") == "C": {e}')
    
    total += 1
    try:
        result = candidate(s = "zZ") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zZ") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "MmQqEe") == "Q"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MmQqEe") == "Q": {e}')
    
    total += 1
    try:
        result = candidate(s = "aB") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aB") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "AbCdEfGhIjKlMnOpQrStUvWxYz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AbCdEfGhIjKlMnOpQrStUvWxYz") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "qUICkBrOwNBROWNfOX") == "W"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qUICkBrOwNBROWNfOX") == "W": {e}')
    
    total += 1
    try:
        result = candidate(s = "pUrPLe") == "P"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pUrPLe") == "P": {e}')
    
    total += 1
    try:
        result = candidate(s = "ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "aBcD") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aBcD") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "bLuE") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bLuE") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "xYzZaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwW") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xYzZaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwW") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "bBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "bAcBdCeCdFdEgFhG") == "G"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bAcBdCeCdFdEgFhG") == "G": {e}')
    
    total += 1
    try:
        result = candidate(s = "zZyYxXwWvVuUtTsSrRpPqQoOnNmMlLkKjJiIhHgGfFeEdDcCbBaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zZyYxXwWvVuUtTsSrRpPqQoOnNmMlLkKjJiIhHgGfFeEdDcCbBaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZzZyYxXwWvVuUtTsSrRpPqQoOnNmMlLkKjJiIhHgGfFeEdDcCbBaAaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZzZyYxXwWvVuUtTsSrRpPqQoOnNmMlLkKjJiIhHgGfFeEdDcCbBaAaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "hYsS") == "S"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hYsS") == "S": {e}')
    
    total += 1
    try:
        result = candidate(s = "thisIsAtEsTString") == "T"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisIsAtEsTString") == "T": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzXYZuvwUVWtTqsSRpqPRonmNMlLkKjJiIhHgGfFeEdDcCbBaA") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzXYZuvwUVWtTqsSRpqPRonmNMlLkKjJiIhHgGfFeEdDcCbBaA") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "AaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa") == "A"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa") == "A": {e}')
    
    total += 1
    try:
        result = candidate(s = "aAaaAAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == "A"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAaaAAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == "A": {e}')
    
    total += 1
    try:
        result = candidate(s = "noUpperLower") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noUpperLower") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "UnIqUe") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "UnIqUe") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "mAgEnTa") == "A"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mAgEnTa") == "A": {e}')
    
    total += 1
    try:
        result = candidate(s = "aAaAaAaAaAaA") == "A"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAaAaAaAaAaA") == "A": {e}')
    
    total += 1
    try:
        result = candidate(s = "AaaaBBbbbCCCCDDDdeeeFFGHHHIIIJJJ") == "D"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AaaaBBbbbCCCCDDDdeeeFFGHHHIIIJJJ") == "D": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzABCxyzABC") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzABCxyzABC") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aNdSoMeSpEcIaLChArAcTeRs") == "S"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aNdSoMeSpEcIaLChArAcTeRs") == "S": {e}')
    
    total += 1
    try:
        result = candidate(s = "withSomeDuPpLicaTeS") == "T"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "withSomeDuPpLicaTeS") == "T": {e}')
    
    total += 1
    try:
        result = candidate(s = "bBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBb") == "B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBb") == "B": {e}')
    
    total += 1
    try:
        result = candidate(s = "mNnOoPpQqRrSsTtUuVvWwXxYyZzLlKkJjIiHhGgFfEeDdCcBbAa") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mNnOoPpQqRrSsTtUuVvWwXxYyZzLlKkJjIiHhGgFfEeDdCcBbAa") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghiJklmnopqrStuvWxyzZ") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghiJklmnopqrStuvWxyzZ") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefGHIJKLmnopQRStuvWXYZ") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefGHIJKLmnopQRStuvWXYZ") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "mMnNoOpPqQrRsStTuUvVwWxXyYzZaAbBcCdDeEfFgGhHiIjJkKlL") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mMnNoOpPqQrRsStTuUvVwWxXyYzZaAbBcCdDeEfFgGhHiIjJkKlL") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "aBcDdEfGgHiJjKlMmNoPpQrRsStTuUvVwWxXyYzZ") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aBcDdEfGgHiJjKlMmNoPpQrRsStTuUvVwWxXyYzZ") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "gRaY") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "gRaY") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "butNoVaLiDgReaTtEsT") == "T"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "butNoVaLiDgReaTtEsT") == "T": {e}')
    
    total += 1
    try:
        result = candidate(s = "mIXeDuPpLeTeXt") == "T"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mIXeDuPpLeTeXt") == "T": {e}')
    
    total += 1
    try:
        result = candidate(s = "nNoOlLkKiIjJhHgGfFeEdDcCbBaA") == "O"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nNoOlLkKiIjJhHgGfFeEdDcCbBaA") == "O": {e}')
    
    total += 1
    try:
        result = candidate(s = "cYaN") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cYaN") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "sUpErCoMpLeXtExT") == "X"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "sUpErCoMpLeXtExT") == "X": {e}')
    
    total += 1
    try:
        result = candidate(s = "AbCdEfGhIjKlMnOpQrStUvWxYzZ") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AbCdEfGhIjKlMnOpQrStUvWxYzZ") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "mIxEdCaSeStRiNg") == "I"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mIxEdCaSeStRiNg") == "I": {e}')
    
    total += 1
    try:
        result = candidate(s = "MmLlKkJjIiHhGgFfEeDdCcBbAa") == "M"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MmLlKkJjIiHhGgFfEeDdCcBbAa") == "M": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgHIJKLmnopqRSTUVWxyz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgHIJKLmnopqRSTUVWxyz") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "mM") == "M"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mM") == "M": {e}')
    
    total += 1
    try:
        result = candidate(s = "AbcDefGhIjKlMnopQRStuvWXYZ") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AbcDefGhIjKlMnopQRStuvWXYZ") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "ZZZaaaBBBcccDDDeeeFFFgggHHHiiiJJJkkkLLLmmmNNNoooPPPqqqRRRsssTTTuuuVVVwwwXXXyyyzzz") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ZZZaaaBBBcccDDDeeeFFFgggHHHiiiJJJkkkLLLmmmNNNoooPPPqqqRRRsssTTTuuuVVVwwwXXXyyyzzz") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "tEsTiNgUpPeRaNdLoWeRcAsE") == "T"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "tEsTiNgUpPeRaNdLoWeRcAsE") == "T": {e}')
    
    total += 1
    try:
        result = candidate(s = "sUnShInESoNnY") == "S"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "sUnShInESoNnY") == "S": {e}')
    
    total += 1
    try:
        result = candidate(s = "xYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxY") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxY") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "mNnOoPpQqRrSsTtUuVvWwXxYyZz") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mNnOoPpQqRrSsTtUuVvWwXxYyZz") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "zZyYxXwWvVuUtTsSrRpPqQoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zZyYxXwWvVuUtTsSrRpPqQoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "zZaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyY") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zZaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyY") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "aNkLmNpQrStUvWxYzZ") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aNkLmNpQrStUvWxYzZ") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "sTrInGtEsTcAsE") == "T"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "sTrInGtEsTcAsE") == "T": {e}')
    
    total += 1
    try:
        result = candidate(s = "aAaAaAbBbBcCcCdDdDeEeEfFfFgGgGhHhHiIiIjJjJkKkKlLlLmMmMnNnNoOpPqQrRsStTuUvVwWxXyYzZzZyYxXwWvVuUtTsSrRpPqQoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAaAaAbBbBcCcCdDdDeEeEfFfFgGgGhHhHiIiIjJjJkKkKlLlLmMmMnNnNoOpPqQrRsStTuUvVwWxXyYzZzZyYxXwWvVuUtTsSrRpPqQoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "gReEn") == "E"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "gReEn") == "E": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopQRstUVwXYZ") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopQRstUVwXYZ") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrStuvWxyzZ") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrStuvWxyzZ") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZ") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZ") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "zZyYxXwWvVuUtTsSrRqQpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zZyYxXwWvVuUtTsSrRqQpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == "A"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == "A": {e}')
    
    total += 1
    try:
        result = candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaA") == "A"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaA") == "A": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijkLmnopqrstUvwxyz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijkLmnopqrstUvwxyz") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "AbCdEfGhIjKlMnOpQrStUvWxYzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AbCdEfGhIjKlMnOpQrStUvWxYzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "aNnBmMlLkKiIjJhHgGfFeEdDcCbBaA") == "N"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aNnBmMlLkKiIjJhHgGfFeEdDcCbBaA") == "N": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmooppqqrrssttuuvvwwxxyyzz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmooppqqrrssttuuvvwwxxyyzz") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aBcDxyzXYZaBcD") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aBcDxyzXYZaBcD") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "fUnNyCaSe") == "N"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "fUnNyCaSe") == "N": {e}')
    
    total += 1
    try:
        result = candidate(s = "oRaNgE") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "oRaNgE") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aBcDfEgHiJkLmNoPqRsTuVwXyZ") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aBcDfEgHiJkLmNoPqRsTuVwXyZ") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyZzXyZzXyZzXyZzXyZzXyZzXyZzXyZzXyZz") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyZzXyZzXyZzXyZzXyZzXyZzXyZzXyZzXyZz") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "bAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAxAyAz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAxAyAz") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == "A"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == "A": {e}')
    
    total += 1
    try:
        result = candidate(s = "qQwWeErRtTyYuUiIoOpPlLkKjJhHgGfFdDsSaAzZ") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qQwWeErRtTyYuUiIoOpPlLkKjJhHgGfFdDsSaAzZ") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzXYZabcABCdefDEFghiGHIjklJKLmnopMNOpqrQRstSTuvwUVWxyzXYZ") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzXYZabcABCdefDEFghiGHIjklJKLmnopMNOpqrQRstSTuvwUVWxyzXYZ") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "MiXeDcAsEnOnCaSeTeStStRiNg") == "T"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MiXeDcAsEnOnCaSeTeStStRiNg") == "T": {e}')
    
    total += 1
    try:
        result = candidate(s = "jUmBlEdTeXt") == "T"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "jUmBlEdTeXt") == "T": {e}')
    
    total += 1
    try:
        result = candidate(s = "aBcDefGHiJkLmNoPqRsTuVwXyZZzz") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aBcDefGHiJkLmNoPqRsTuVwXyZZzz") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "aAeEiIoOuUaAeEiIoOuUaAeEiIoOuU") == "U"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAeEiIoOuUaAeEiIoOuUaAeEiIoOuU") == "U": {e}')
    
    total += 1
    try:
        result = candidate(s = "abCDxyzXYZ") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abCDxyzXYZ") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "oNeTwOThReEfOuRfIvEsIxTEnElEvEnTiGoNeVeNtWeNtYtHrEe") == "W"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "oNeTwOThReEfOuRfIvEsIxTEnElEvEnTiGoNeVeNtWeNtYtHrEe") == "W": {e}')
    
    total += 1
    try:
        result = candidate(s = "mAgIc") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mAgIc") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == "Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "ABCDEFGhijklmNopqrStuvWxyz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ABCDEFGhijklmNopqrStuvWxyz") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "AbCdEfGhIjKlMnOpQrStUvWxYzAbCdEfGhIjKlMnOpQrStUvWxYz") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AbCdEfGhIjKlMnOpQrStUvWxYzAbCdEfGhIjKlMnOpQrStUvWxYz") == "": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z"
    assert candidate(s = "mMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z"
    assert candidate(s = "zZyYxXwWeE") == "Z"
    assert candidate(s = "zZyYxXwWvVuUtTrRsSqQpPoOnNmMlLkKiIjJhHgGfFeEdDcCbBaA") == "Z"
    assert candidate(s = "bBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyY") == "Y"
    assert candidate(s = "alluppercase") == ""
    assert candidate(s = "ALLLOWERCASE") == ""
    assert candidate(s = "aBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "Z"
    assert candidate(s = "AbCdEfGhIjK") == ""
    assert candidate(s = "a") == ""
    assert candidate(s = "NoUpperCaseHere") == ""
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == "Z"
    assert candidate(s = "bA") == ""
    assert candidate(s = "AbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z"
    assert candidate(s = "NnOoPpQqRrSsTtUuVvWwXxYyZz") == "Z"
    assert candidate(s = "lEeTcOdE") == "E"
    assert candidate(s = "aBcDeFgHiJkLmNoPqRsTuVwXyZ") == ""
    assert candidate(s = "") == ""
    assert candidate(s = "arRAzFif") == "R"
    assert candidate(s = "abcdefgHIJKLMnoPQRSTuVwxyz") == ""
    assert candidate(s = "QwErTyUiOpAsDfGhJkLzXcVbNm") == ""
    assert candidate(s = "aA") == "A"
    assert candidate(s = "A") == ""
    assert candidate(s = "AaBbCc") == "C"
    assert candidate(s = "zZ") == "Z"
    assert candidate(s = "MmQqEe") == "Q"
    assert candidate(s = "aB") == ""
    assert candidate(s = "AbCdEfGhIjKlMnOpQrStUvWxYz") == ""
    assert candidate(s = "qUICkBrOwNBROWNfOX") == "W"
    assert candidate(s = "pUrPLe") == "P"
    assert candidate(s = "ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa") == "Z"
    assert candidate(s = "aBcD") == ""
    assert candidate(s = "bLuE") == ""
    assert candidate(s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == ""
    assert candidate(s = "xYzZaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwW") == "Z"
    assert candidate(s = "bBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z"
    assert candidate(s = "bAcBdCeCdFdEgFhG") == "G"
    assert candidate(s = "zZyYxXwWvVuUtTsSrRpPqQoOnNmMlLkKjJiIhHgGfFeEdDcCbBaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == "Z"
    assert candidate(s = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZzZyYxXwWvVuUtTsSrRpPqQoOnNmMlLkKjJiIhHgGfFeEdDcCbBaAaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z"
    assert candidate(s = "hYsS") == "S"
    assert candidate(s = "thisIsAtEsTString") == "T"
    assert candidate(s = "xyzXYZuvwUVWtTqsSRpqPRonmNMlLkKjJiIhHgGfFeEdDcCbBaA") == "Z"
    assert candidate(s = "AaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa") == "A"
    assert candidate(s = "aAaaAAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == "A"
    assert candidate(s = "noUpperLower") == ""
    assert candidate(s = "UnIqUe") == ""
    assert candidate(s = "mAgEnTa") == "A"
    assert candidate(s = "aAaAaAaAaAaA") == "A"
    assert candidate(s = "AaaaBBbbbCCCCDDDdeeeFFGHHHIIIJJJ") == "D"
    assert candidate(s = "xyzABCxyzABC") == ""
    assert candidate(s = "aNdSoMeSpEcIaLChArAcTeRs") == "S"
    assert candidate(s = "withSomeDuPpLicaTeS") == "T"
    assert candidate(s = "bBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBb") == "B"
    assert candidate(s = "mNnOoPpQqRrSsTtUuVvWwXxYyZzLlKkJjIiHhGgFfEeDdCcBbAa") == "Z"
    assert candidate(s = "abcdefghiJklmnopqrStuvWxyzZ") == "Z"
    assert candidate(s = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z"
    assert candidate(s = "abcdefGHIJKLmnopQRStuvWXYZ") == ""
    assert candidate(s = "mMnNoOpPqQrRsStTuUvVwWxXyYzZaAbBcCdDeEfFgGhHiIjJkKlL") == "Z"
    assert candidate(s = "aBcDdEfGgHiJjKlMmNoPpQrRsStTuUvVwWxXyYzZ") == "Z"
    assert candidate(s = "gRaY") == ""
    assert candidate(s = "butNoVaLiDgReaTtEsT") == "T"
    assert candidate(s = "mIXeDuPpLeTeXt") == "T"
    assert candidate(s = "nNoOlLkKiIjJhHgGfFeEdDcCbBaA") == "O"
    assert candidate(s = "cYaN") == ""
    assert candidate(s = "sUpErCoMpLeXtExT") == "X"
    assert candidate(s = "AbCdEfGhIjKlMnOpQrStUvWxYzZ") == "Z"
    assert candidate(s = "mIxEdCaSeStRiNg") == "I"
    assert candidate(s = "MmLlKkJjIiHhGgFfEeDdCcBbAa") == "M"
    assert candidate(s = "abcdefgHIJKLmnopqRSTUVWxyz") == ""
    assert candidate(s = "mM") == "M"
    assert candidate(s = "AbcDefGhIjKlMnopQRStuvWXYZ") == ""
    assert candidate(s = "ZZZaaaBBBcccDDDeeeFFFgggHHHiiiJJJkkkLLLmmmNNNoooPPPqqqRRRsssTTTuuuVVVwwwXXXyyyzzz") == "Z"
    assert candidate(s = "tEsTiNgUpPeRaNdLoWeRcAsE") == "T"
    assert candidate(s = "sUnShInESoNnY") == "S"
    assert candidate(s = "xYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxYxY") == ""
    assert candidate(s = "mNnOoPpQqRrSsTtUuVvWwXxYyZz") == "Z"
    assert candidate(s = "zZyYxXwWvVuUtTsSrRpPqQoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == "Z"
    assert candidate(s = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789") == "Z"
    assert candidate(s = "zZaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyY") == "Z"
    assert candidate(s = "aNkLmNpQrStUvWxYzZ") == "Z"
    assert candidate(s = "sTrInGtEsTcAsE") == "T"
    assert candidate(s = "aAaAaAbBbBcCcCdDdDeEeEfFfFgGgGhHhHiIiIjJjJkKkKlLlLmMmMnNnNoOpPqQrRsStTuUvVwWxXyYzZzZyYxXwWvVuUtTsSrRpPqQoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == "Z"
    assert candidate(s = "gReEn") == "E"
    assert candidate(s = "mnopQRstUVwXYZ") == ""
    assert candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == "Z"
    assert candidate(s = "mnopqrStuvWxyzZ") == "Z"
    assert candidate(s = "aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZ") == ""
    assert candidate(s = "zZyYxXwWvVuUtTsSrRqQpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == "Z"
    assert candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == "A"
    assert candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaA") == "A"
    assert candidate(s = "abcdefghijkLmnopqrstUvwxyz") == ""
    assert candidate(s = "AbCdEfGhIjKlMnOpQrStUvWxYzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "Z"
    assert candidate(s = "aNnBmMlLkKiIjJhHgGfFeEdDcCbBaA") == "N"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == ""
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmooppqqrrssttuuvvwwxxyyzz") == ""
    assert candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "Z"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == ""
    assert candidate(s = "aBcDxyzXYZaBcD") == "Z"
    assert candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "Z"
    assert candidate(s = "fUnNyCaSe") == "N"
    assert candidate(s = "oRaNgE") == ""
    assert candidate(s = "aBcDfEgHiJkLmNoPqRsTuVwXyZ") == ""
    assert candidate(s = "xyZzXyZzXyZzXyZzXyZzXyZzXyZzXyZzXyZz") == "Z"
    assert candidate(s = "bAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAxAyAz") == ""
    assert candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == "A"
    assert candidate(s = "qQwWeErRtTyYuUiIoOpPlLkKjJhHgGfFdDsSaAzZ") == "Z"
    assert candidate(s = "xyzXYZabcABCdefDEFghiGHIjklJKLmnopMNOpqrQRstSTuvwUVWxyzXYZ") == "Z"
    assert candidate(s = "MiXeDcAsEnOnCaSeTeStStRiNg") == "T"
    assert candidate(s = "jUmBlEdTeXt") == "T"
    assert candidate(s = "aBcDefGHiJkLmNoPqRsTuVwXyZZzz") == "Z"
    assert candidate(s = "aAeEiIoOuUaAeEiIoOuUaAeEiIoOuU") == "U"
    assert candidate(s = "abCDxyzXYZ") == "Z"
    assert candidate(s = "oNeTwOThReEfOuRfIvEsIxTEnElEvEnTiGoNeVeNtWeNtYtHrEe") == "W"
    assert candidate(s = "mAgIc") == ""
    assert candidate(s = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == "Z"
    assert candidate(s = "ABCDEFGhijklmNopqrStuvWxyz") == ""
    assert candidate(s = "AbCdEfGhIjKlMnOpQrStUvWxYzAbCdEfGhIjKlMnOpQrStUvWxYz") == ""


