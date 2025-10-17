def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "aAbBcCdDeEfFgG") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAbBcCdDeEfFgG") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "AaBbCc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AaBbCc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbCC") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbCC") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "Aabbcc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Aabbcc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abABcdCD") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abABcdCD") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "zZaA") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zZaA") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAbBcC") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAbBcC") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAb") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAb") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcABC") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcABC") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbBCab") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbBCab") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "ZzYyXx") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ZzYyXx") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjiIhHgGfFeEdDcCbBaA") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjiIhHgGfFeEdDcCbBaA") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "aA") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aA") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefgHIJKLmnopqrstuvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefgHIJKLmnopqrstuvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaAbcBC") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaAbcBC") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabB") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabB") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "Aa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Aa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccAABBCC") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccAABBCC") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "AaBbCcDdEeFf") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AaBbCcDdEeFf") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "AaBbCcDd") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AaBbCcDd") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "zZyYxXwWvVuUtTsSrRqQpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zZyYxXwWvVuUtTsSrRqQpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccAAABBBCCC") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccAAABBBCCC") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "zZyYxXwWvVuUtTsSrRpPqQoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zZyYxXwWvVuUtTsSrRpPqQoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaAAAAAaaaaaAAAAA") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaAAAAAaaaaaAAAAA") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcXYZabcXYZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcXYZabcXYZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzZ") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzZ") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdEFGhijklmNOPqrSTuvWXYZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdEFGhijklmNOPqrSTuvWXYZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAaAaAaAaAaAaAaAaAaA") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAaAaAaAaAaAaAaAaAaA") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAbBcCddeEfffGggHhhIiiJjjKkkLllMmmNnnOooPppQqqRrrSssTttUuuVvvWwwXxxYyyZzz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAbBcCddeEfffGggHhhIiiJjjKkkLllMmmNnnOooPppQqqRrrSssTttUuuVvvWwwXxxYyyZzz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "Zabcdefghijklmnopqrstuvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "Zabcdefghijklmnopqrstuvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "zZyYxXwWvVuUtTsSrRpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zZyYxXwWvVuUtTsSrRpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == 25: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aBcD") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aBcD") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZaAbB") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZaAbB") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCdeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZ") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCdeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZ") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzXYZabcABC") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzXYZabcABC") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzZzzzZzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzZzzzZzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYzAbCdEfGhIjKlMnOpQrStUvWxYz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYzAbCdEfGhIjKlMnOpQrStUvWxYz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 25: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcABCabcABCabcABC") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcABCabcABCabcABC") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abABcdCDefEfghGhijIJklKLmMnopNOPqrstQRstUVuvwVwxWXyzYZ") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abABcdCDefEfghGhijIJklKLmMnopNOPqrstQRstUVuvwVwxWXyzYZ") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYZZZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYZZZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAAAbBBBcCCCCdDDDD") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAAAbBBBcCCCCdDDDD") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 25: {e}')
    
    total += 1
    try:
        result = candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abCDcdEFefGHghIJijKLklMNmnOPopQRqrSTstUVuvWXwxYZyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abCDcdEFefGHghIJijKLklMNmnOPopQRqrSTstUVuvWXwxYZyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefABCDEFghijklGHJKLmnopQRStuTUvwVWXyYZ") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefABCDEFghijklGHJKLmnopQRStuTUvwVWXyYZ") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAAaBBBbcccC") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAAaBBBbcccC") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaBBBcccDDD") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaBBBcccDDD") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abABcdE") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abABcdE") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aBcDDefFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aBcDDefFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 21: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAbBcCdefGhIjKlMnopQrstUvwXyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAbBcCdefGhIjKlMnopQrstUvwXyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaBBBcccDDDeeeFFFgggHHHiiiJJJkkkLLLmmmNNNoooPPPqqqRRRsssTTTuuuVVVwwwXXXyyyZZZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaBBBcccDDDeeeFFFgggHHHiiiJJJkkkLLLmmmNNNoooPPPqqqRRRsssTTTuuuVVVwwwXXXyyyZZZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzabcdefghijklmnopqrstuvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzabcdefghijklmnopqrstuvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "ZZZZzzzzYYYYyyyyXXXXXXXXxxWWWWwwwwVVVVvvvvUUUUuuuuTTTTttttSSSSssssRRRRrrrrQQQQqqqqPPPPppppOOOOooooNNNNnnnnMMMMmmmmLLLLllllKKKKkkkkJJJJjjjjIIIIiiiiHHHHhhhhGGGGggggFFFFFFffffEEEEeeeeDDDDddddCCCCccccBBBBbbbbAAAAAAAAaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ZZZZzzzzYYYYyyyyXXXXXXXXxxWWWWwwwwVVVVvvvvUUUUuuuuTTTTttttSSSSssssRRRRrrrrQQQQqqqqPPPPppppOOOOooooNNNNnnnnMMMMmmmmLLLLllllKKKKkkkkJJJJjjjjIIIIiiiiHHHHhhhhGGGGggggFFFFFFffffEEEEeeeeDDDDddddCCCCccccBBBBbbbbAAAAAAAAaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefgHIJKLMNopqrstuvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefgHIJKLMNopqrstuvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYzABCD") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYzABCD") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "zZyYxXwWvVuUtTrRsSqQpPnNmMlLkKiIhHgGfFeEdDcCbBaA") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zZyYxXwWvVuUtTrRsSqQpPnNmMlLkKiIhHgGfFeEdDcCbBaA") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzAA") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzAA") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aB") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aB") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZaA") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZaA") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aBcDEfGHiJKlMNopQRsTuVwXyZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aBcDEfGHiJKlMNopQRsTuVwXyZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaAAAaaaAAAaaaAAA") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaAAAaaaAAAaaaAAA") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aBbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aBbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzZZZyyyYYYxxxXXXwwwWWWvvvVVVuuuUUUtttTTTsssSSSrrrRRRqqqQQQpppPPPoooOOOnnnNNNmmmMMMlllLLLkkkKKKjjjJJJiiiIIIhhhHHHgggGGGfffFFFeeeEEEdddDDDcccCCCbbbBBBaaaAAA") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzZZZyyyYYYxxxXXXwwwWWWvvvVVVuuuUUUtttTTTsssSSSrrrRRRqqqQQQpppPPPoooOOOnnnNNNmmmMMMlllLLLkkkKKKjjjJJJiiiIIIhhhHHHgggGGGfffFFFeeeEEEdddDDDcccCCCbbbBBBaaaAAA") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "aBcDefGhiJklMnoPqrStuVwxYz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aBcDefGhiJklMnoPqrStuVwxYz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaBBccDDeeFFggHHiiJJkkLLmmNNooPPqqRRssTTuuVVwwXXyyZZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaBBccDDeeFFggHHiiJJkkLLmmNNooPPqqRRssTTuuVVwwXXyyZZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaBBccDDeeFFggHHiiJjkkLLmmNNooPPqqRRssTTuuVVwwXXyyZZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaBBccDDeeFFggHHiiJjkkLLmmNNooPPqqRRssTTuuVVwwXXyyZZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzZ") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzZ") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstuNOPQRS") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstuNOPQRS") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAbC") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAbC") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzZ") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzZ") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word = "aAbCdeFghIjKlmNoPqRsTuVwXyZ") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aAbCdeFghIjKlmNoPqRsTuVwXyZ") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaAaabBBccCCCd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaAaabBBccCCCd") == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "aAbBcCdDeEfFgG") == 7
    assert candidate(word = "AaBbCc") == 0
    assert candidate(word = "aabbCC") == 0
    assert candidate(word = "Aabbcc") == 0
    assert candidate(word = "abABcdCD") == 4
    assert candidate(word = "zZaA") == 2
    assert candidate(word = "aAbBcC") == 3
    assert candidate(word = "aAb") == 1
    assert candidate(word = "abcABC") == 3
    assert candidate(word = "ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa") == 0
    assert candidate(word = "AbBCab") == 0
    assert candidate(word = "ZzYyXx") == 0
    assert candidate(word = "ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjiIhHgGfFeEdDcCbBaA") == 9
    assert candidate(word = "aA") == 1
    assert candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 0
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 0
    assert candidate(word = "abcdefgHIJKLmnopqrstuvwxyz") == 0
    assert candidate(word = "aaAbcBC") == 3
    assert candidate(word = "aabB") == 1
    assert candidate(word = "abc") == 0
    assert candidate(word = "Aa") == 0
    assert candidate(word = "aabbccAABBCC") == 3
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 26
    assert candidate(word = "AaBbCcDdEeFf") == 0
    assert candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZ") == 0
    assert candidate(word = "AaBbCcDd") == 0
    assert candidate(word = "zZyYxXwWvVuUtTsSrRqQpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == 26
    assert candidate(word = "aabbccAAABBBCCC") == 3
    assert candidate(word = "zZyYxXwWvVuUtTsSrRpPqQoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == 26
    assert candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 0
    assert candidate(word = "aaaaaAAAAAaaaaaAAAAA") == 0
    assert candidate(word = "abcXYZabcXYZ") == 0
    assert candidate(word = "zzzzZ") == 1
    assert candidate(word = "abcdEFGhijklmNOPqrSTuvWXYZ") == 0
    assert candidate(word = "aAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 0
    assert candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 0
    assert candidate(word = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 0
    assert candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYz") == 0
    assert candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 0
    assert candidate(word = "aAaAaAaAaAaAaAaAaAaA") == 0
    assert candidate(word = "aAbBcCddeEfffGggHhhIiiJjjKkkLllMmmNnnOooPppQqqRrrSssTttUuuVvvWwwXxxYyyZzz") == 4
    assert candidate(word = "Zabcdefghijklmnopqrstuvwxyz") == 0
    assert candidate(word = "zZyYxXwWvVuUtTsSrRpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA") == 25
    assert candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 0
    assert candidate(word = "aBcD") == 0
    assert candidate(word = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZaAbB") == 24
    assert candidate(word = "AbCdeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZ") == 2
    assert candidate(word = "xyzXYZabcABC") == 6
    assert candidate(word = "zzzzZzzzZzzzzzzz") == 0
    assert candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYzAbCdEfGhIjKlMnOpQrStUvWxYz") == 0
    assert candidate(word = "AbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 25
    assert candidate(word = "abcABCabcABCabcABC") == 0
    assert candidate(word = "abABcdCDefEfghGhijIJklKLmMnopNOPqrstQRstUVuvwVwxWXyzYZ") == 20
    assert candidate(word = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYZZZ") == 0
    assert candidate(word = "aAAAbBBBcCCCCdDDDD") == 4
    assert candidate(word = "AbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 25
    assert candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 0
    assert candidate(word = "abCDcdEFefGHghIJijKLklMNmnOPopQRqrSTstUVuvWXwxYZyz") == 0
    assert candidate(word = "abcdefABCDEFghijklGHJKLmnopQRStuTUvwVWXyYZ") == 16
    assert candidate(word = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ") == 0
    assert candidate(word = "aAAaBBBbcccC") == 1
    assert candidate(word = "aBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 0
    assert candidate(word = "aaaBBBcccDDD") == 0
    assert candidate(word = "abABcdE") == 2
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") == 0
    assert candidate(word = "aBcDDefFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 21
    assert candidate(word = "aAbBcCdefGhIjKlMnopQrstUvwXyz") == 3
    assert candidate(word = "aaaBBBcccDDDeeeFFFgggHHHiiiJJJkkkLLLmmmNNNoooPPPqqqRRRsssTTTuuuVVVwwwXXXyyyZZZ") == 0
    assert candidate(word = "aBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzabcdefghijklmnopqrstuvwxyz") == 0
    assert candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCc") == 0
    assert candidate(word = "ZZZZzzzzYYYYyyyyXXXXXXXXxxWWWWwwwwVVVVvvvvUUUUuuuuTTTTttttSSSSssssRRRRrrrrQQQQqqqqPPPPppppOOOOooooNNNNnnnnMMMMmmmmLLLLllllKKKKkkkkJJJJjjjjIIIIiiiiHHHHhhhhGGGGggggFFFFFFffffEEEEeeeeDDDDddddCCCCccccBBBBbbbbAAAAAAAAaaaa") == 0
    assert candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZ") == 0
    assert candidate(word = "abcdefgHIJKLMNopqrstuvwxyz") == 0
    assert candidate(word = "AbCdEfGhIjKlMnOpQrStUvWxYzABCD") == 2
    assert candidate(word = "zZyYxXwWvVuUtTrRsSqQpPnNmMlLkKiIhHgGfFeEdDcCbBaA") == 24
    assert candidate(word = "aAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0
    assert candidate(word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzAA") == 1
    assert candidate(word = "aB") == 0
    assert candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZaA") == 1
    assert candidate(word = "aBcDEfGHiJKlMNopQRsTuVwXyZ") == 0
    assert candidate(word = "aaaAAAaaaAAAaaaAAA") == 0
    assert candidate(word = "aBbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 0
    assert candidate(word = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 0
    assert candidate(word = "zzzZZZyyyYYYxxxXXXwwwWWWvvvVVVuuuUUUtttTTTsssSSSrrrRRRqqqQQQpppPPPoooOOOnnnNNNmmmMMMlllLLLkkkKKKjjjJJJiiiIIIhhhHHHgggGGGfffFFFeeeEEEdddDDDcccCCCbbbBBBaaaAAA") == 26
    assert candidate(word = "aBcDefGhiJklMnoPqrStuVwxYz") == 0
    assert candidate(word = "abcdefghijklmnopqrstuvwxyz") == 0
    assert candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 0
    assert candidate(word = "aaBBccDDeeFFggHHiiJJkkLLmmNNooPPqqRRssTTuuVVwwXXyyZZ") == 0
    assert candidate(word = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 0
    assert candidate(word = "aaBBccDDeeFFggHHiiJjkkLLmmNNooPPqqRRssTTuuVVwwXXyyZZ") == 0
    assert candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZ") == 0
    assert candidate(word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzZ") == 1
    assert candidate(word = "aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZ") == 0
    assert candidate(word = "mnopqrstuNOPQRS") == 6
    assert candidate(word = "aAbC") == 1
    assert candidate(word = "aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA") == 0
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzZ") == 1
    assert candidate(word = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ") == 26
    assert candidate(word = "aAbCdeFghIjKlmNoPqRsTuVwXyZ") == 1
    assert candidate(word = "aaAaabBBccCCCd") == 2


