def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(str1 = "ABAB",str2 = "ABA") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABAB",str2 = "ABA") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABCDEFGH",str2 = "XYZ") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABCDEFGH",str2 = "XYZ") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABCABC",str2 = "ABC") == "ABC"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABCABC",str2 = "ABC") == "ABC": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABABAB",str2 = "ABA") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABABAB",str2 = "ABA") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABABAB",str2 = "ABAB") == "AB"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABABAB",str2 = "ABAB") == "AB": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABCABCABC",str2 = "ABCABC") == "ABC"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABCABCABC",str2 = "ABCABC") == "ABC": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABCD",str2 = "EFGH") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABCD",str2 = "EFGH") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "XYZXYZXYZ",str2 = "XYZXYZ") == "XYZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "XYZXYZXYZ",str2 = "XYZXYZ") == "XYZ": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "AAAAAAAAAA",str2 = "AAAAAAAAAA") == "AAAAAAAAAA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "AAAAAAAAAA",str2 = "AAAAAAAAAA") == "AAAAAAAAAA": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "GCDGCDGCD",str2 = "GCD") == "GCD"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "GCDGCDGCD",str2 = "GCD") == "GCD": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABCD",str2 = "ABCD") == "ABCD"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABCD",str2 = "ABCD") == "ABCD": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "HELLOHELLO",str2 = "HELLO") == "HELLO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "HELLOHELLO",str2 = "HELLO") == "HELLO": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "A",str2 = "A") == "A"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "A",str2 = "A") == "A": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "PQRS",str2 = "PQRS") == "PQRS"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "PQRS",str2 = "PQRS") == "PQRS": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "AAAA",str2 = "AA") == "AA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "AAAA",str2 = "AA") == "AA": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABCDEFG",str2 = "BCD") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABCDEFG",str2 = "BCD") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "LEET",str2 = "CODE") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "LEET",str2 = "CODE") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "HELLOHELLOHELLO",str2 = "HELLO") == "HELLO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "HELLOHELLOHELLO",str2 = "HELLO") == "HELLO": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABCDEF",str2 = "ABC") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABCDEF",str2 = "ABC") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABABABAB",str2 = "BABA") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABABABAB",str2 = "BABA") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "AAAAAAAAA",str2 = "AAAAA") == "A"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "AAAAAAAAA",str2 = "AAAAA") == "A": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "TATATATA",str2 = "TAT") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "TATATATA",str2 = "TAT") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABCABCABC",str2 = "ABC") == "ABC"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABCABCABC",str2 = "ABC") == "ABC": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABABABAB",str2 = "ABAB") == "ABAB"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABABABAB",str2 = "ABAB") == "ABAB": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "BANANABANANABANANABANANA",str2 = "BANANABANANA") == "BANANABANANA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "BANANABANANABANANABANANA",str2 = "BANANABANANA") == "BANANABANANA": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "XYXYXYXY",str2 = "XYXY") == "XYXY"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "XYXYXYXY",str2 = "XYXY") == "XYXY": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "DOUBLEDOUBLEDOUBLE",str2 = "DOUBLEDOUBLE") == "DOUBLE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "DOUBLEDOUBLEDOUBLE",str2 = "DOUBLEDOUBLE") == "DOUBLE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "SIMILARITYSIMILARITY",str2 = "SIMILARITY") == "SIMILARITY"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "SIMILARITYSIMILARITY",str2 = "SIMILARITY") == "SIMILARITY": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "REPREPREP",str2 = "REPRE") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "REPREPREP",str2 = "REPRE") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABACABACABAC",str2 = "ABAC") == "ABAC"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABACABACABAC",str2 = "ABAC") == "ABAC": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "DOGDOGDOGDOGDOGDOG",str2 = "DOGDOGDOG") == "DOGDOGDOG"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "DOGDOGDOGDOGDOGDOG",str2 = "DOGDOGDOG") == "DOGDOGDOG": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "XYZXYZXYZXYZXYZXYZ",str2 = "XYZXYZXYZXYZ") == "XYZXYZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "XYZXYZXYZXYZXYZXYZ",str2 = "XYZXYZXYZXYZ") == "XYZXYZ": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "PPPPPPPPPPPPPPPP",str2 = "PPPPPP") == "PP"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "PPPPPPPPPPPPPPPP",str2 = "PPPPPP") == "PP": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "MULTIPLEMULTIPLEMULTIPLE",str2 = "MULTIPLEMULTIPLE") == "MULTIPLE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "MULTIPLEMULTIPLEMULTIPLE",str2 = "MULTIPLEMULTIPLE") == "MULTIPLE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "MIXEDCASEMIXEDCASE",str2 = "MIXEDCASE") == "MIXEDCASE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "MIXEDCASEMIXEDCASE",str2 = "MIXEDCASE") == "MIXEDCASE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "XYXYXYXYXYXYXYXY",str2 = "XYXYXY") == "XY"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "XYXYXYXYXYXYXYXY",str2 = "XYXYXY") == "XY": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ANTEANTEANTEANTEANTEANTEANTEANTEANTE",str2 = "ANTEANTEANTEANTE") == "ANTE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ANTEANTEANTEANTEANTEANTEANTEANTEANTE",str2 = "ANTEANTEANTEANTE") == "ANTE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "QWQWQWQWQWQW",str2 = "QWQW") == "QWQW"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "QWQWQWQWQWQW",str2 = "QWQW") == "QWQW": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "PINEAPPLEPINEAPPLEPINEAPPLEPINEAPPLE",str2 = "PINEAPPLEPINEAPPLE") == "PINEAPPLEPINEAPPLE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "PINEAPPLEPINEAPPLEPINEAPPLEPINEAPPLE",str2 = "PINEAPPLEPINEAPPLE") == "PINEAPPLEPINEAPPLE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "MNMNMNMN",str2 = "MNMN") == "MNMN"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "MNMNMNMN",str2 = "MNMN") == "MNMN": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "XYZXYZXYZXYZXYZ",str2 = "XYZXYZXYZ") == "XYZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "XYZXYZXYZXYZXYZ",str2 = "XYZXYZXYZ") == "XYZ": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "REPORTEPORTEPORTE",str2 = "REPORTEPORTE") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "REPORTEPORTEPORTE",str2 = "REPORTEPORTE") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "RRRRRRRRRRRR",str2 = "RRRRRR") == "RRRRRR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "RRRRRRRRRRRR",str2 = "RRRRRR") == "RRRRRR": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "DIFFERENTLENGTHDIFFERENTLENGTH",str2 = "DIFFERENTLENGTH") == "DIFFERENTLENGTH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "DIFFERENTLENGTHDIFFERENTLENGTH",str2 = "DIFFERENTLENGTH") == "DIFFERENTLENGTH": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "SMALLSAME",str2 = "SAME") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "SMALLSAME",str2 = "SAME") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "MIXEDUPMIXEDUP",str2 = "MIXEDUP") == "MIXEDUP"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "MIXEDUPMIXEDUP",str2 = "MIXEDUP") == "MIXEDUP": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "UPPERCASEUPPERCASEUPPERCASE",str2 = "UPPERCASEUPPERCASE") == "UPPERCASE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "UPPERCASEUPPERCASEUPPERCASE",str2 = "UPPERCASEUPPERCASE") == "UPPERCASE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "LONGSTRINGLONGSTRINGLONGSTRINGLONGSTRING",str2 = "LONGSTRINGLONGSTRING") == "LONGSTRINGLONGSTRING"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "LONGSTRINGLONGSTRINGLONGSTRINGLONGSTRING",str2 = "LONGSTRINGLONGSTRING") == "LONGSTRINGLONGSTRING": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "LONGSTRINGLONGSTRINGLONGSTRING",str2 = "LONGSTRINGLONG") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "LONGSTRINGLONGSTRINGLONGSTRING",str2 = "LONGSTRINGLONG") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "SIMPLESIMPLESIMPLE",str2 = "SIMPLESIMPLE") == "SIMPLE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "SIMPLESIMPLESIMPLE",str2 = "SIMPLESIMPLE") == "SIMPLE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "AAAAABBBB",str2 = "AAAAA") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "AAAAABBBB",str2 = "AAAAA") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "SHORT",str2 = "VERYLONGSTRINGTHATISNOTAREPEAT") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "SHORT",str2 = "VERYLONGSTRINGTHATISNOTAREPEAT") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "AB",str2 = "BA") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "AB",str2 = "BA") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "PRIMEPRIMEPRIME",str2 = "PRIMEPRIME") == "PRIME"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "PRIMEPRIMEPRIME",str2 = "PRIMEPRIME") == "PRIME": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "MNMNMNMNMNMN",str2 = "MNMN") == "MNMN"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "MNMNMNMNMNMN",str2 = "MNMN") == "MNMN": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "BEEBEEBEEBEEBEEBEEBEEBEE",str2 = "BEEBEEBEEBEE") == "BEEBEEBEEBEE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "BEEBEEBEEBEEBEEBEEBEEBEE",str2 = "BEEBEEBEEBEE") == "BEEBEEBEEBEE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "GRAPEGRAPEGRAPEGRAPEGRAPEGRAPE",str2 = "GRAPEGRAPEGRAPE") == "GRAPEGRAPEGRAPE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "GRAPEGRAPEGRAPEGRAPEGRAPEGRAPE",str2 = "GRAPEGRAPEGRAPE") == "GRAPEGRAPEGRAPE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "TIGERTIGERTIGERTIGERTIGERTIGER",str2 = "TIGERTIGERTIGER") == "TIGERTIGERTIGER"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "TIGERTIGERTIGERTIGERTIGERTIGER",str2 = "TIGERTIGERTIGER") == "TIGERTIGERTIGER": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "SCIENCE",str2 = "SCIENCE") == "SCIENCE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "SCIENCE",str2 = "SCIENCE") == "SCIENCE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABCDEFGABCDEFG",str2 = "ABCDEFG") == "ABCDEFG"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABCDEFGABCDEFG",str2 = "ABCDEFG") == "ABCDEFG": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "XYZXYZXYZXYZXYZXYZXYZXYZ",str2 = "XYZXYZXYZ") == "XYZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "XYZXYZXYZXYZXYZXYZXYZXYZ",str2 = "XYZXYZXYZ") == "XYZ": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "MIXEDMIXEDMIXEDMIXED",str2 = "MIXEDMIXED") == "MIXEDMIXED"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "MIXEDMIXEDMIXEDMIXED",str2 = "MIXEDMIXED") == "MIXEDMIXED": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ALMOSTSAMEALMOSTSAME",str2 = "ALMOSTSAME") == "ALMOSTSAME"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ALMOSTSAMEALMOSTSAME",str2 = "ALMOSTSAME") == "ALMOSTSAME": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "APPLEAPPLEAPPLEAPPLEAPPLE",str2 = "APPLEAPPLEAPPLE") == "APPLE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "APPLEAPPLEAPPLEAPPLEAPPLE",str2 = "APPLEAPPLEAPPLE") == "APPLE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "MIXMIXMIXMIX",str2 = "MIXMIX") == "MIXMIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "MIXMIXMIXMIX",str2 = "MIXMIX") == "MIXMIX": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "MATHMATHMATHMATH",str2 = "MATH") == "MATH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "MATHMATHMATHMATH",str2 = "MATH") == "MATH": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "SIMPLESIMPLESIMPLESIMPLE",str2 = "SIMPLE") == "SIMPLE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "SIMPLESIMPLESIMPLESIMPLE",str2 = "SIMPLE") == "SIMPLE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "DUCKDUCKDUCKDUCKDUCKDUCKDUCKDUCK",str2 = "DUCKDUCKDUCKDUCK") == "DUCKDUCKDUCKDUCK"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "DUCKDUCKDUCKDUCKDUCKDUCKDUCKDUCK",str2 = "DUCKDUCKDUCKDUCK") == "DUCKDUCKDUCKDUCK": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "LONGLONGLONGLONGLONGLONG",str2 = "LONGLONGLONG") == "LONGLONGLONG"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "LONGLONGLONGLONGLONGLONG",str2 = "LONGLONGLONG") == "LONGLONGLONG": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ZAZAZAZAZA",str2 = "ZAZA") == "ZA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ZAZAZAZAZA",str2 = "ZAZA") == "ZA": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "AABAAABAAB",str2 = "AAB") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "AABAAABAAB",str2 = "AAB") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABCDEFABCDEF",str2 = "ABCDEF") == "ABCDEF"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABCDEFABCDEF",str2 = "ABCDEF") == "ABCDEF": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "PATTERNPATTERNPATTERN",str2 = "PATTERNPATTERN") == "PATTERN"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "PATTERNPATTERNPATTERN",str2 = "PATTERNPATTERN") == "PATTERN": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "UNIQUEUNIQUEUNIQUEUNIQUEUNIQUE",str2 = "UNIQUEUNIQUE") == "UNIQUE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "UNIQUEUNIQUEUNIQUEUNIQUEUNIQUE",str2 = "UNIQUEUNIQUE") == "UNIQUE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "A",str2 = "") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "A",str2 = "") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "WOWOWOWOWOWO",str2 = "WOWOWO") == "WOWOWO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "WOWOWOWOWOWO",str2 = "WOWOWO") == "WOWOWO": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "HELLOHELLOHELLOHELLO",str2 = "HELLOHELLOHELLO") == "HELLO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "HELLOHELLOHELLOHELLO",str2 = "HELLOHELLOHELLO") == "HELLO": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "REPEATREPEATREPEATREPEATREPEAT",str2 = "REPEATREPEAT") == "REPEAT"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "REPEATREPEATREPEATREPEATREPEAT",str2 = "REPEATREPEAT") == "REPEAT": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "IDENTICALIDENTICALIDENTICAL",str2 = "IDENTICALIDENTICAL") == "IDENTICAL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "IDENTICALIDENTICALIDENTICAL",str2 = "IDENTICALIDENTICAL") == "IDENTICAL": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABCDEFGABCDEFG",str2 = "DEFGABCD") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABCDEFGABCDEFG",str2 = "DEFGABCD") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "SAMESTRINGSAME",str2 = "SAME") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "SAMESTRINGSAME",str2 = "SAME") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "REPEATREPEATREPEAT",str2 = "REPEATREPEAT") == "REPEAT"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "REPEATREPEATREPEAT",str2 = "REPEATREPEAT") == "REPEAT": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "QQQQQQQQQQ",str2 = "QQQQ") == "QQ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "QQQQQQQQQQ",str2 = "QQQQ") == "QQ": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "FAMILYFAMILYFAMILY",str2 = "FAMILYFAMILY") == "FAMILY"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "FAMILYFAMILYFAMILY",str2 = "FAMILYFAMILY") == "FAMILY": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABCABCABCABCABCABC",str2 = "ABCABCABC") == "ABCABCABC"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABCABCABCABCABCABC",str2 = "ABCABCABC") == "ABCABCABC": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "",str2 = "A") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "",str2 = "A") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "UNIQUEUNIQUEUNIQUEUNIQUE",str2 = "UNIQUEUNIQUE") == "UNIQUEUNIQUE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "UNIQUEUNIQUEUNIQUEUNIQUE",str2 = "UNIQUEUNIQUE") == "UNIQUEUNIQUE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "LONGSTRINGLONGSTRING",str2 = "LONGSTRING") == "LONGSTRING"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "LONGSTRINGLONGSTRING",str2 = "LONGSTRING") == "LONGSTRING": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "UNIQUEUNIQUE",str2 = "UNIQUEUNIQUEUNIQUE") == "UNIQUE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "UNIQUEUNIQUE",str2 = "UNIQUEUNIQUEUNIQUE") == "UNIQUE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "MOUSEMOUSEMOUSEMOUSEMOUSEMOUSE",str2 = "MOUSEMOUSE") == "MOUSEMOUSE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "MOUSEMOUSEMOUSEMOUSEMOUSEMOUSE",str2 = "MOUSEMOUSE") == "MOUSEMOUSE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABABABABABAB",str2 = "ABAB") == "ABAB"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABABABABABAB",str2 = "ABAB") == "ABAB": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "HELLOWORLDHELLOWORLD",str2 = "HELLOWORLD") == "HELLOWORLD"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "HELLOWORLDHELLOWORLD",str2 = "HELLOWORLD") == "HELLOWORLD": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABCDABCD",str2 = "ABCDABCDABCD") == "ABCD"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABCDABCD",str2 = "ABCDABCDABCD") == "ABCD": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "SAMESAMESAME",str2 = "SAME") == "SAME"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "SAMESAMESAME",str2 = "SAME") == "SAME": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "QRSTQRSTQRST",str2 = "QRSTQRST") == "QRST"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "QRSTQRSTQRST",str2 = "QRSTQRST") == "QRST": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "KARMAKARMAKARMAKARMA",str2 = "KARMAKARMA") == "KARMAKARMA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "KARMAKARMAKARMAKARMA",str2 = "KARMAKARMA") == "KARMAKARMA": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "AAAAABAAAAAB",str2 = "AAAAAB") == "AAAAAB"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "AAAAABAAAAAB",str2 = "AAAAAB") == "AAAAAB": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "TTT",str2 = "TTTTTTT") == "T"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "TTT",str2 = "TTTTTTT") == "T": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "QQQQQQQQQQQQQQQQ",str2 = "QQQQ") == "QQQQ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "QQQQQQQQQQQQQQQQ",str2 = "QQQQ") == "QQQQ": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "AAAABBBBAAAABBBB",str2 = "AAAABBBB") == "AAAABBBB"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "AAAABBBBAAAABBBB",str2 = "AAAABBBB") == "AAAABBBB": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "QWQWQWQWQWQW",str2 = "QWQWQW") == "QWQWQW"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "QWQWQWQWQWQW",str2 = "QWQWQW") == "QWQWQW": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "PPPPPPPP",str2 = "PPPP") == "PPPP"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "PPPPPPPP",str2 = "PPPP") == "PPPP": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "SPAMSPAMSPAMSPAM",str2 = "SPAMSPAM") == "SPAMSPAM"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "SPAMSPAMSPAMSPAM",str2 = "SPAMSPAM") == "SPAMSPAM": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "PATTERNPATTERN",str2 = "PATTERN") == "PATTERN"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "PATTERNPATTERN",str2 = "PATTERN") == "PATTERN": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "XYZXYZXYZXYZXYZXYZ",str2 = "XYZXYZ") == "XYZXYZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "XYZXYZXYZXYZXYZXYZ",str2 = "XYZXYZ") == "XYZXYZ": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "SCREENSCREENSCREENSCREEN",str2 = "SCREEN") == "SCREEN"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "SCREENSCREENSCREENSCREEN",str2 = "SCREEN") == "SCREEN": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "PIZZAPIZZAPIZZAPIZZA",str2 = "PIZZAPIZZA") == "PIZZAPIZZA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "PIZZAPIZZAPIZZAPIZZA",str2 = "PIZZAPIZZA") == "PIZZAPIZZA": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ORANGEORANGEORANGEORANGEORANGEORANGEORANGEORANGE",str2 = "ORANGEORANGEORANGE") == "ORANGE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ORANGEORANGEORANGEORANGEORANGEORANGEORANGEORANGE",str2 = "ORANGEORANGEORANGE") == "ORANGE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "PRIMEPRIMEPRIMEPRIME",str2 = "PRIMEPRIME") == "PRIMEPRIME"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "PRIMEPRIMEPRIMEPRIME",str2 = "PRIMEPRIME") == "PRIMEPRIME": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "REPEATREPEATREPEAT",str2 = "REPEAT") == "REPEAT"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "REPEATREPEATREPEAT",str2 = "REPEAT") == "REPEAT": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "CODECODECODECODECODECODE",str2 = "CODECODECODE") == "CODECODECODE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "CODECODECODECODECODECODE",str2 = "CODECODECODE") == "CODECODECODE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "PROJECTORPROJECTORPROJECTORPROJECTOR",str2 = "PROJECTORPROJECTOR") == "PROJECTORPROJECTOR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "PROJECTORPROJECTORPROJECTORPROJECTOR",str2 = "PROJECTORPROJECTOR") == "PROJECTORPROJECTOR": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "PYTHONPYTHONPYTHON",str2 = "PYTHONPYTHON") == "PYTHON"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "PYTHONPYTHONPYTHON",str2 = "PYTHONPYTHON") == "PYTHON": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "CCCCCCCCCCCCCC",str2 = "CCCCCCCCC") == "C"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "CCCCCCCCCCCCCC",str2 = "CCCCCCCCC") == "C": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "PQPQPQ",str2 = "PQPQPQPQPQ") == "PQ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "PQPQPQ",str2 = "PQPQPQPQPQ") == "PQ": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "DESKDESKDESKDESK",str2 = "DESK") == "DESK"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "DESKDESKDESKDESK",str2 = "DESK") == "DESK": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "GUITARGUITARGUITAR",str2 = "GUITAR") == "GUITAR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "GUITARGUITARGUITAR",str2 = "GUITAR") == "GUITAR": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "QWQWQWQWQW",str2 = "QWQWQW") == "QW"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "QWQWQWQWQW",str2 = "QWQWQW") == "QW": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "LONGLONGLONGLONGLONG",str2 = "LONGLONGLONG") == "LONG"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "LONGLONGLONGLONGLONG",str2 = "LONGLONGLONG") == "LONG": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "DEVDEVDEVDEVDEV",str2 = "DEVDEV") == "DEV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "DEVDEVDEVDEVDEV",str2 = "DEVDEV") == "DEV": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "UNIQUEUNIQUEUNIQUEUNIQUEUNIQUE",str2 = "UNIQUEUNIQUEUNIQUE") == "UNIQUE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "UNIQUEUNIQUEUNIQUEUNIQUEUNIQUE",str2 = "UNIQUEUNIQUEUNIQUE") == "UNIQUE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "TREETREETREETREE",str2 = "TREETREE") == "TREETREE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "TREETREETREETREE",str2 = "TREETREE") == "TREETREE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "XYZXYZXYZXYZXYZXYZ",str2 = "XYZXYZXYZ") == "XYZXYZXYZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "XYZXYZXYZXYZXYZXYZ",str2 = "XYZXYZXYZ") == "XYZXYZXYZ": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "HELLOHELLOHELLOHELLOHELLO",str2 = "HELLOHELLOHELLO") == "HELLO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "HELLOHELLOHELLOHELLOHELLO",str2 = "HELLOHELLOHELLO") == "HELLO": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "SMALL",str2 = "SMALLSMALLSMALL") == "SMALL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "SMALL",str2 = "SMALLSMALLSMALL") == "SMALL": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "MNMNMNMNMN",str2 = "MNMN") == "MN"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "MNMNMNMNMN",str2 = "MNMN") == "MN": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABCABCABCABC",str2 = "ABCABC") == "ABCABC"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABCABCABCABC",str2 = "ABCABC") == "ABCABC": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "LONGERSTRINGLONGERSTRINGLONGERSTRING",str2 = "LONGERSTRINGLONGERSTRING") == "LONGERSTRING"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "LONGERSTRINGLONGERSTRINGLONGERSTRING",str2 = "LONGERSTRINGLONGERSTRING") == "LONGERSTRING": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "PATTERNPATTERNPATTERNPATTERN",str2 = "PATTERNPATTERN") == "PATTERNPATTERN"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "PATTERNPATTERNPATTERNPATTERN",str2 = "PATTERNPATTERN") == "PATTERNPATTERN": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "HELLOHELLOHELLOHELLOHELLOHELLO",str2 = "HELLOHELLOHELLOHELLOHELLO") == "HELLO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "HELLOHELLOHELLOHELLOHELLOHELLO",str2 = "HELLOHELLOHELLOHELLOHELLO") == "HELLO": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "DIFFERENTLENGTHS",str2 = "SOMEOTHERSTRING") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "DIFFERENTLENGTHS",str2 = "SOMEOTHERSTRING") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "MIXEDUP",str2 = "MIXEDUPMIXEDUP") == "MIXEDUP"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "MIXEDUP",str2 = "MIXEDUPMIXEDUP") == "MIXEDUP": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "KEYBOARDKEYBOARDKEYBOARDKEYBOARD",str2 = "KEYBOARDKEYBOARD") == "KEYBOARDKEYBOARD"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "KEYBOARDKEYBOARDKEYBOARDKEYBOARD",str2 = "KEYBOARDKEYBOARD") == "KEYBOARDKEYBOARD": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "FLOWERFLOWERFLOWERFLOWER",str2 = "FLOWERFLOWER") == "FLOWERFLOWER"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "FLOWERFLOWERFLOWERFLOWER",str2 = "FLOWERFLOWER") == "FLOWERFLOWER": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "LONGSTRING",str2 = "LONGSTRINGLONGSTRING") == "LONGSTRING"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "LONGSTRING",str2 = "LONGSTRINGLONGSTRING") == "LONGSTRING": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "SAMESTRINGSAMESTRINGSAMESTRING",str2 = "SAMESTRINGSAMESTRING") == "SAMESTRING"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "SAMESTRINGSAMESTRINGSAMESTRING",str2 = "SAMESTRINGSAMESTRING") == "SAMESTRING": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "NONONONONONO",str2 = "NONO") == "NONO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "NONONONONONO",str2 = "NONO") == "NONO": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABCDABCDABCDABCD",str2 = "ABCDABCD") == "ABCDABCD"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABCDABCDABCDABCD",str2 = "ABCDABCD") == "ABCDABCD": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "TESTTESTTESTTEST",str2 = "TESTTEST") == "TESTTEST"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "TESTTESTTESTTEST",str2 = "TESTTEST") == "TESTTEST": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "SAMELENGTH",str2 = "DIFFERENT") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "SAMELENGTH",str2 = "DIFFERENT") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "HELLOHELLOHELLO",str2 = "HELLOHELLO") == "HELLO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "HELLOHELLOHELLO",str2 = "HELLOHELLO") == "HELLO": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "DOGDOGDOGDOGDOG",str2 = "DOGDOG") == "DOG"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "DOGDOGDOGDOGDOG",str2 = "DOGDOG") == "DOG": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "CATCATCATCATCAT",str2 = "CATCAT") == "CAT"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "CATCATCATCATCAT",str2 = "CATCAT") == "CAT": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABABABABAB",str2 = "ABAB") == "AB"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABABABABAB",str2 = "ABAB") == "AB": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "LONGLONGLONGLONG",str2 = "LONG") == "LONG"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "LONGLONGLONGLONG",str2 = "LONG") == "LONG": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "COMPUTERCOMPUTERCOMPUTER",str2 = "COMPUTER") == "COMPUTER"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "COMPUTERCOMPUTERCOMPUTER",str2 = "COMPUTER") == "COMPUTER": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "RUBYRUBYRUBYRUBY",str2 = "RUBYRUBY") == "RUBYRUBY"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "RUBYRUBYRUBYRUBY",str2 = "RUBYRUBY") == "RUBYRUBY": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "BEEBEEBEEBEEBEE",str2 = "BEEBEE") == "BEE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "BEEBEEBEEBEEBEE",str2 = "BEEBEE") == "BEE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABABABABABAB",str2 = "ABABAB") == "ABABAB"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABABABABABAB",str2 = "ABABAB") == "ABABAB": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "BIGBIGBIGBIG",str2 = "BIG") == "BIG"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "BIGBIGBIGBIG",str2 = "BIG") == "BIG": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "APPLEAPPLEAPPLEAPPLEAPPLEAPPLE",str2 = "APPLEAPPLEAPPLE") == "APPLEAPPLEAPPLE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "APPLEAPPLEAPPLEAPPLEAPPLEAPPLE",str2 = "APPLEAPPLEAPPLE") == "APPLEAPPLEAPPLE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "AABBCCDDEEFF",str2 = "AABBCCDD") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "AABBCCDDEEFF",str2 = "AABBCCDD") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "UVUVUVUVUVUV",str2 = "UVUVUV") == "UVUVUV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "UVUVUVUVUVUV",str2 = "UVUVUV") == "UVUVUV": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "PPPPPPPPPP",str2 = "PPPP") == "PP"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "PPPPPPPPPP",str2 = "PPPP") == "PP": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "TESTTESTTESTTEST",str2 = "TESTTESTTEST") == "TEST"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "TESTTESTTESTTEST",str2 = "TESTTESTTEST") == "TEST": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "AABBCCDDEE",str2 = "AABBCC") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "AABBCCDDEE",str2 = "AABBCC") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "MIXMIXMIXMIXMIX",str2 = "MIXMIX") == "MIX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "MIXMIXMIXMIXMIX",str2 = "MIXMIX") == "MIX": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "PYTHONPYTHONPYTHONPYTHON",str2 = "PYTHONPYTHON") == "PYTHONPYTHON"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "PYTHONPYTHONPYTHONPYTHON",str2 = "PYTHONPYTHON") == "PYTHONPYTHON": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "",str2 = "") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "",str2 = "") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "PYTHONPYTHONPYTHONPYTHONPYTHON",str2 = "PYTHONPYTHON") == "PYTHON"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "PYTHONPYTHONPYTHONPYTHONPYTHON",str2 = "PYTHONPYTHON") == "PYTHON": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "AABBCCAABBCC",str2 = "AABBCC") == "AABBCC"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "AABBCCAABBCC",str2 = "AABBCC") == "AABBCC": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "LIONLIONLIONLIONLIONLION",str2 = "LIONLIONLION") == "LIONLIONLION"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "LIONLIONLIONLIONLIONLION",str2 = "LIONLIONLION") == "LIONLIONLION": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABCDEFGABCDEFGABCDEFG",str2 = "ABCDEFGABCDEFG") == "ABCDEFG"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABCDEFGABCDEFGABCDEFG",str2 = "ABCDEFGABCDEFG") == "ABCDEFG": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "MICROPHONEMICROPHONEMICROPHONE",str2 = "MICROPHONE") == "MICROPHONE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "MICROPHONEMICROPHONEMICROPHONE",str2 = "MICROPHONE") == "MICROPHONE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABABABABABABABAB",str2 = "ABABAB") == "AB"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABABABABABABABAB",str2 = "ABABAB") == "AB": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "XYZXYZXYZXYZ",str2 = "XYZXYZ") == "XYZXYZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "XYZXYZXYZXYZ",str2 = "XYZXYZ") == "XYZXYZ": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "HEADPHONESHEADPHONES",str2 = "HEADPHONESHEADPHONES") == "HEADPHONESHEADPHONES"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "HEADPHONESHEADPHONES",str2 = "HEADPHONESHEADPHONES") == "HEADPHONESHEADPHONES": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "ABCDEFGHABCDEFGHABCDEFGH",str2 = "ABCDEFGHABCDEFGH") == "ABCDEFGH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "ABCDEFGHABCDEFGHABCDEFGH",str2 = "ABCDEFGHABCDEFGH") == "ABCDEFGH": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "SPEAKERSPEAKERSPEAKERSPEAKERSPEAKER",str2 = "SPEAKERSPEAKER") == "SPEAKER"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "SPEAKERSPEAKERSPEAKERSPEAKERSPEAKER",str2 = "SPEAKERSPEAKER") == "SPEAKER": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "DIVIDEDIVIDE",str2 = "DIVIDE") == "DIVIDE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "DIVIDEDIVIDE",str2 = "DIVIDE") == "DIVIDE": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "JSJSJSJSJSJSJS",str2 = "JSJSJSJS") == "JS"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "JSJSJSJSJSJSJS",str2 = "JSJSJSJS") == "JS": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "CATCATCATCATCATCAT",str2 = "CATCATCAT") == "CATCATCAT"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "CATCATCATCATCATCAT",str2 = "CATCATCAT") == "CATCATCAT": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "NOTCOMMONNOTCOMMONNOTCOMMON",str2 = "NOTCOMMONNOT") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "NOTCOMMONNOTCOMMONNOTCOMMON",str2 = "NOTCOMMONNOT") == "": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "XZXZXZXZXZ",str2 = "XZXZ") == "XZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "XZXZXZXZXZ",str2 = "XZXZ") == "XZ": {e}')
    
    total += 1
    try:
        result = candidate(str1 = "DOGDOGDOGDOGDOGDOGDOGDOGDOGDOG",str2 = "DOGDOGDOGDOG") == "DOGDOG"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(str1 = "DOGDOGDOGDOGDOGDOGDOGDOGDOGDOG",str2 = "DOGDOGDOGDOG") == "DOGDOG": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(str1 = "ABAB",str2 = "ABA") == ""
    assert candidate(str1 = "ABCDEFGH",str2 = "XYZ") == ""
    assert candidate(str1 = "ABCABC",str2 = "ABC") == "ABC"
    assert candidate(str1 = "ABABAB",str2 = "ABA") == ""
    assert candidate(str1 = "ABABAB",str2 = "ABAB") == "AB"
    assert candidate(str1 = "ABCABCABC",str2 = "ABCABC") == "ABC"
    assert candidate(str1 = "ABCD",str2 = "EFGH") == ""
    assert candidate(str1 = "XYZXYZXYZ",str2 = "XYZXYZ") == "XYZ"
    assert candidate(str1 = "AAAAAAAAAA",str2 = "AAAAAAAAAA") == "AAAAAAAAAA"
    assert candidate(str1 = "GCDGCDGCD",str2 = "GCD") == "GCD"
    assert candidate(str1 = "ABCD",str2 = "ABCD") == "ABCD"
    assert candidate(str1 = "HELLOHELLO",str2 = "HELLO") == "HELLO"
    assert candidate(str1 = "A",str2 = "A") == "A"
    assert candidate(str1 = "PQRS",str2 = "PQRS") == "PQRS"
    assert candidate(str1 = "AAAA",str2 = "AA") == "AA"
    assert candidate(str1 = "ABCDEFG",str2 = "BCD") == ""
    assert candidate(str1 = "LEET",str2 = "CODE") == ""
    assert candidate(str1 = "HELLOHELLOHELLO",str2 = "HELLO") == "HELLO"
    assert candidate(str1 = "ABCDEF",str2 = "ABC") == ""
    assert candidate(str1 = "ABABABAB",str2 = "BABA") == ""
    assert candidate(str1 = "AAAAAAAAA",str2 = "AAAAA") == "A"
    assert candidate(str1 = "TATATATA",str2 = "TAT") == ""
    assert candidate(str1 = "ABCABCABC",str2 = "ABC") == "ABC"
    assert candidate(str1 = "ABABABAB",str2 = "ABAB") == "ABAB"
    assert candidate(str1 = "BANANABANANABANANABANANA",str2 = "BANANABANANA") == "BANANABANANA"
    assert candidate(str1 = "XYXYXYXY",str2 = "XYXY") == "XYXY"
    assert candidate(str1 = "DOUBLEDOUBLEDOUBLE",str2 = "DOUBLEDOUBLE") == "DOUBLE"
    assert candidate(str1 = "SIMILARITYSIMILARITY",str2 = "SIMILARITY") == "SIMILARITY"
    assert candidate(str1 = "REPREPREP",str2 = "REPRE") == ""
    assert candidate(str1 = "ABACABACABAC",str2 = "ABAC") == "ABAC"
    assert candidate(str1 = "DOGDOGDOGDOGDOGDOG",str2 = "DOGDOGDOG") == "DOGDOGDOG"
    assert candidate(str1 = "XYZXYZXYZXYZXYZXYZ",str2 = "XYZXYZXYZXYZ") == "XYZXYZ"
    assert candidate(str1 = "PPPPPPPPPPPPPPPP",str2 = "PPPPPP") == "PP"
    assert candidate(str1 = "MULTIPLEMULTIPLEMULTIPLE",str2 = "MULTIPLEMULTIPLE") == "MULTIPLE"
    assert candidate(str1 = "MIXEDCASEMIXEDCASE",str2 = "MIXEDCASE") == "MIXEDCASE"
    assert candidate(str1 = "XYXYXYXYXYXYXYXY",str2 = "XYXYXY") == "XY"
    assert candidate(str1 = "ANTEANTEANTEANTEANTEANTEANTEANTEANTE",str2 = "ANTEANTEANTEANTE") == "ANTE"
    assert candidate(str1 = "QWQWQWQWQWQW",str2 = "QWQW") == "QWQW"
    assert candidate(str1 = "PINEAPPLEPINEAPPLEPINEAPPLEPINEAPPLE",str2 = "PINEAPPLEPINEAPPLE") == "PINEAPPLEPINEAPPLE"
    assert candidate(str1 = "MNMNMNMN",str2 = "MNMN") == "MNMN"
    assert candidate(str1 = "XYZXYZXYZXYZXYZ",str2 = "XYZXYZXYZ") == "XYZ"
    assert candidate(str1 = "REPORTEPORTEPORTE",str2 = "REPORTEPORTE") == ""
    assert candidate(str1 = "RRRRRRRRRRRR",str2 = "RRRRRR") == "RRRRRR"
    assert candidate(str1 = "DIFFERENTLENGTHDIFFERENTLENGTH",str2 = "DIFFERENTLENGTH") == "DIFFERENTLENGTH"
    assert candidate(str1 = "SMALLSAME",str2 = "SAME") == ""
    assert candidate(str1 = "MIXEDUPMIXEDUP",str2 = "MIXEDUP") == "MIXEDUP"
    assert candidate(str1 = "UPPERCASEUPPERCASEUPPERCASE",str2 = "UPPERCASEUPPERCASE") == "UPPERCASE"
    assert candidate(str1 = "LONGSTRINGLONGSTRINGLONGSTRINGLONGSTRING",str2 = "LONGSTRINGLONGSTRING") == "LONGSTRINGLONGSTRING"
    assert candidate(str1 = "LONGSTRINGLONGSTRINGLONGSTRING",str2 = "LONGSTRINGLONG") == ""
    assert candidate(str1 = "SIMPLESIMPLESIMPLE",str2 = "SIMPLESIMPLE") == "SIMPLE"
    assert candidate(str1 = "AAAAABBBB",str2 = "AAAAA") == ""
    assert candidate(str1 = "SHORT",str2 = "VERYLONGSTRINGTHATISNOTAREPEAT") == ""
    assert candidate(str1 = "AB",str2 = "BA") == ""
    assert candidate(str1 = "PRIMEPRIMEPRIME",str2 = "PRIMEPRIME") == "PRIME"
    assert candidate(str1 = "MNMNMNMNMNMN",str2 = "MNMN") == "MNMN"
    assert candidate(str1 = "BEEBEEBEEBEEBEEBEEBEEBEE",str2 = "BEEBEEBEEBEE") == "BEEBEEBEEBEE"
    assert candidate(str1 = "GRAPEGRAPEGRAPEGRAPEGRAPEGRAPE",str2 = "GRAPEGRAPEGRAPE") == "GRAPEGRAPEGRAPE"
    assert candidate(str1 = "TIGERTIGERTIGERTIGERTIGERTIGER",str2 = "TIGERTIGERTIGER") == "TIGERTIGERTIGER"
    assert candidate(str1 = "SCIENCE",str2 = "SCIENCE") == "SCIENCE"
    assert candidate(str1 = "ABCDEFGABCDEFG",str2 = "ABCDEFG") == "ABCDEFG"
    assert candidate(str1 = "XYZXYZXYZXYZXYZXYZXYZXYZ",str2 = "XYZXYZXYZ") == "XYZ"
    assert candidate(str1 = "MIXEDMIXEDMIXEDMIXED",str2 = "MIXEDMIXED") == "MIXEDMIXED"
    assert candidate(str1 = "ALMOSTSAMEALMOSTSAME",str2 = "ALMOSTSAME") == "ALMOSTSAME"
    assert candidate(str1 = "APPLEAPPLEAPPLEAPPLEAPPLE",str2 = "APPLEAPPLEAPPLE") == "APPLE"
    assert candidate(str1 = "MIXMIXMIXMIX",str2 = "MIXMIX") == "MIXMIX"
    assert candidate(str1 = "MATHMATHMATHMATH",str2 = "MATH") == "MATH"
    assert candidate(str1 = "SIMPLESIMPLESIMPLESIMPLE",str2 = "SIMPLE") == "SIMPLE"
    assert candidate(str1 = "DUCKDUCKDUCKDUCKDUCKDUCKDUCKDUCK",str2 = "DUCKDUCKDUCKDUCK") == "DUCKDUCKDUCKDUCK"
    assert candidate(str1 = "LONGLONGLONGLONGLONGLONG",str2 = "LONGLONGLONG") == "LONGLONGLONG"
    assert candidate(str1 = "ZAZAZAZAZA",str2 = "ZAZA") == "ZA"
    assert candidate(str1 = "AABAAABAAB",str2 = "AAB") == ""
    assert candidate(str1 = "ABCDEFABCDEF",str2 = "ABCDEF") == "ABCDEF"
    assert candidate(str1 = "PATTERNPATTERNPATTERN",str2 = "PATTERNPATTERN") == "PATTERN"
    assert candidate(str1 = "UNIQUEUNIQUEUNIQUEUNIQUEUNIQUE",str2 = "UNIQUEUNIQUE") == "UNIQUE"
    assert candidate(str1 = "A",str2 = "") == ""
    assert candidate(str1 = "WOWOWOWOWOWO",str2 = "WOWOWO") == "WOWOWO"
    assert candidate(str1 = "HELLOHELLOHELLOHELLO",str2 = "HELLOHELLOHELLO") == "HELLO"
    assert candidate(str1 = "REPEATREPEATREPEATREPEATREPEAT",str2 = "REPEATREPEAT") == "REPEAT"
    assert candidate(str1 = "IDENTICALIDENTICALIDENTICAL",str2 = "IDENTICALIDENTICAL") == "IDENTICAL"
    assert candidate(str1 = "ABCDEFGABCDEFG",str2 = "DEFGABCD") == ""
    assert candidate(str1 = "SAMESTRINGSAME",str2 = "SAME") == ""
    assert candidate(str1 = "REPEATREPEATREPEAT",str2 = "REPEATREPEAT") == "REPEAT"
    assert candidate(str1 = "QQQQQQQQQQ",str2 = "QQQQ") == "QQ"
    assert candidate(str1 = "FAMILYFAMILYFAMILY",str2 = "FAMILYFAMILY") == "FAMILY"
    assert candidate(str1 = "ABCABCABCABCABCABC",str2 = "ABCABCABC") == "ABCABCABC"
    assert candidate(str1 = "",str2 = "A") == ""
    assert candidate(str1 = "UNIQUEUNIQUEUNIQUEUNIQUE",str2 = "UNIQUEUNIQUE") == "UNIQUEUNIQUE"
    assert candidate(str1 = "LONGSTRINGLONGSTRING",str2 = "LONGSTRING") == "LONGSTRING"
    assert candidate(str1 = "UNIQUEUNIQUE",str2 = "UNIQUEUNIQUEUNIQUE") == "UNIQUE"
    assert candidate(str1 = "MOUSEMOUSEMOUSEMOUSEMOUSEMOUSE",str2 = "MOUSEMOUSE") == "MOUSEMOUSE"
    assert candidate(str1 = "ABABABABABAB",str2 = "ABAB") == "ABAB"
    assert candidate(str1 = "HELLOWORLDHELLOWORLD",str2 = "HELLOWORLD") == "HELLOWORLD"
    assert candidate(str1 = "ABCDABCD",str2 = "ABCDABCDABCD") == "ABCD"
    assert candidate(str1 = "SAMESAMESAME",str2 = "SAME") == "SAME"
    assert candidate(str1 = "QRSTQRSTQRST",str2 = "QRSTQRST") == "QRST"
    assert candidate(str1 = "KARMAKARMAKARMAKARMA",str2 = "KARMAKARMA") == "KARMAKARMA"
    assert candidate(str1 = "AAAAABAAAAAB",str2 = "AAAAAB") == "AAAAAB"
    assert candidate(str1 = "TTT",str2 = "TTTTTTT") == "T"
    assert candidate(str1 = "QQQQQQQQQQQQQQQQ",str2 = "QQQQ") == "QQQQ"
    assert candidate(str1 = "AAAABBBBAAAABBBB",str2 = "AAAABBBB") == "AAAABBBB"
    assert candidate(str1 = "QWQWQWQWQWQW",str2 = "QWQWQW") == "QWQWQW"
    assert candidate(str1 = "PPPPPPPP",str2 = "PPPP") == "PPPP"
    assert candidate(str1 = "SPAMSPAMSPAMSPAM",str2 = "SPAMSPAM") == "SPAMSPAM"
    assert candidate(str1 = "PATTERNPATTERN",str2 = "PATTERN") == "PATTERN"
    assert candidate(str1 = "XYZXYZXYZXYZXYZXYZ",str2 = "XYZXYZ") == "XYZXYZ"
    assert candidate(str1 = "SCREENSCREENSCREENSCREEN",str2 = "SCREEN") == "SCREEN"
    assert candidate(str1 = "PIZZAPIZZAPIZZAPIZZA",str2 = "PIZZAPIZZA") == "PIZZAPIZZA"
    assert candidate(str1 = "ORANGEORANGEORANGEORANGEORANGEORANGEORANGEORANGE",str2 = "ORANGEORANGEORANGE") == "ORANGE"
    assert candidate(str1 = "PRIMEPRIMEPRIMEPRIME",str2 = "PRIMEPRIME") == "PRIMEPRIME"
    assert candidate(str1 = "REPEATREPEATREPEAT",str2 = "REPEAT") == "REPEAT"
    assert candidate(str1 = "CODECODECODECODECODECODE",str2 = "CODECODECODE") == "CODECODECODE"
    assert candidate(str1 = "PROJECTORPROJECTORPROJECTORPROJECTOR",str2 = "PROJECTORPROJECTOR") == "PROJECTORPROJECTOR"
    assert candidate(str1 = "PYTHONPYTHONPYTHON",str2 = "PYTHONPYTHON") == "PYTHON"
    assert candidate(str1 = "CCCCCCCCCCCCCC",str2 = "CCCCCCCCC") == "C"
    assert candidate(str1 = "PQPQPQ",str2 = "PQPQPQPQPQ") == "PQ"
    assert candidate(str1 = "DESKDESKDESKDESK",str2 = "DESK") == "DESK"
    assert candidate(str1 = "GUITARGUITARGUITAR",str2 = "GUITAR") == "GUITAR"
    assert candidate(str1 = "QWQWQWQWQW",str2 = "QWQWQW") == "QW"
    assert candidate(str1 = "LONGLONGLONGLONGLONG",str2 = "LONGLONGLONG") == "LONG"
    assert candidate(str1 = "DEVDEVDEVDEVDEV",str2 = "DEVDEV") == "DEV"
    assert candidate(str1 = "UNIQUEUNIQUEUNIQUEUNIQUEUNIQUE",str2 = "UNIQUEUNIQUEUNIQUE") == "UNIQUE"
    assert candidate(str1 = "TREETREETREETREE",str2 = "TREETREE") == "TREETREE"
    assert candidate(str1 = "XYZXYZXYZXYZXYZXYZ",str2 = "XYZXYZXYZ") == "XYZXYZXYZ"
    assert candidate(str1 = "HELLOHELLOHELLOHELLOHELLO",str2 = "HELLOHELLOHELLO") == "HELLO"
    assert candidate(str1 = "SMALL",str2 = "SMALLSMALLSMALL") == "SMALL"
    assert candidate(str1 = "MNMNMNMNMN",str2 = "MNMN") == "MN"
    assert candidate(str1 = "ABCABCABCABC",str2 = "ABCABC") == "ABCABC"
    assert candidate(str1 = "LONGERSTRINGLONGERSTRINGLONGERSTRING",str2 = "LONGERSTRINGLONGERSTRING") == "LONGERSTRING"
    assert candidate(str1 = "PATTERNPATTERNPATTERNPATTERN",str2 = "PATTERNPATTERN") == "PATTERNPATTERN"
    assert candidate(str1 = "HELLOHELLOHELLOHELLOHELLOHELLO",str2 = "HELLOHELLOHELLOHELLOHELLO") == "HELLO"
    assert candidate(str1 = "DIFFERENTLENGTHS",str2 = "SOMEOTHERSTRING") == ""
    assert candidate(str1 = "MIXEDUP",str2 = "MIXEDUPMIXEDUP") == "MIXEDUP"
    assert candidate(str1 = "KEYBOARDKEYBOARDKEYBOARDKEYBOARD",str2 = "KEYBOARDKEYBOARD") == "KEYBOARDKEYBOARD"
    assert candidate(str1 = "FLOWERFLOWERFLOWERFLOWER",str2 = "FLOWERFLOWER") == "FLOWERFLOWER"
    assert candidate(str1 = "LONGSTRING",str2 = "LONGSTRINGLONGSTRING") == "LONGSTRING"
    assert candidate(str1 = "SAMESTRINGSAMESTRINGSAMESTRING",str2 = "SAMESTRINGSAMESTRING") == "SAMESTRING"
    assert candidate(str1 = "NONONONONONO",str2 = "NONO") == "NONO"
    assert candidate(str1 = "ABCDABCDABCDABCD",str2 = "ABCDABCD") == "ABCDABCD"
    assert candidate(str1 = "TESTTESTTESTTEST",str2 = "TESTTEST") == "TESTTEST"
    assert candidate(str1 = "SAMELENGTH",str2 = "DIFFERENT") == ""
    assert candidate(str1 = "HELLOHELLOHELLO",str2 = "HELLOHELLO") == "HELLO"
    assert candidate(str1 = "DOGDOGDOGDOGDOG",str2 = "DOGDOG") == "DOG"
    assert candidate(str1 = "CATCATCATCATCAT",str2 = "CATCAT") == "CAT"
    assert candidate(str1 = "ABABABABAB",str2 = "ABAB") == "AB"
    assert candidate(str1 = "LONGLONGLONGLONG",str2 = "LONG") == "LONG"
    assert candidate(str1 = "COMPUTERCOMPUTERCOMPUTER",str2 = "COMPUTER") == "COMPUTER"
    assert candidate(str1 = "RUBYRUBYRUBYRUBY",str2 = "RUBYRUBY") == "RUBYRUBY"
    assert candidate(str1 = "BEEBEEBEEBEEBEE",str2 = "BEEBEE") == "BEE"
    assert candidate(str1 = "ABABABABABAB",str2 = "ABABAB") == "ABABAB"
    assert candidate(str1 = "BIGBIGBIGBIG",str2 = "BIG") == "BIG"
    assert candidate(str1 = "APPLEAPPLEAPPLEAPPLEAPPLEAPPLE",str2 = "APPLEAPPLEAPPLE") == "APPLEAPPLEAPPLE"
    assert candidate(str1 = "AABBCCDDEEFF",str2 = "AABBCCDD") == ""
    assert candidate(str1 = "UVUVUVUVUVUV",str2 = "UVUVUV") == "UVUVUV"
    assert candidate(str1 = "PPPPPPPPPP",str2 = "PPPP") == "PP"
    assert candidate(str1 = "TESTTESTTESTTEST",str2 = "TESTTESTTEST") == "TEST"
    assert candidate(str1 = "AABBCCDDEE",str2 = "AABBCC") == ""
    assert candidate(str1 = "MIXMIXMIXMIXMIX",str2 = "MIXMIX") == "MIX"
    assert candidate(str1 = "PYTHONPYTHONPYTHONPYTHON",str2 = "PYTHONPYTHON") == "PYTHONPYTHON"
    assert candidate(str1 = "",str2 = "") == ""
    assert candidate(str1 = "PYTHONPYTHONPYTHONPYTHONPYTHON",str2 = "PYTHONPYTHON") == "PYTHON"
    assert candidate(str1 = "AABBCCAABBCC",str2 = "AABBCC") == "AABBCC"
    assert candidate(str1 = "LIONLIONLIONLIONLIONLION",str2 = "LIONLIONLION") == "LIONLIONLION"
    assert candidate(str1 = "ABCDEFGABCDEFGABCDEFG",str2 = "ABCDEFGABCDEFG") == "ABCDEFG"
    assert candidate(str1 = "MICROPHONEMICROPHONEMICROPHONE",str2 = "MICROPHONE") == "MICROPHONE"
    assert candidate(str1 = "ABABABABABABABAB",str2 = "ABABAB") == "AB"
    assert candidate(str1 = "XYZXYZXYZXYZ",str2 = "XYZXYZ") == "XYZXYZ"
    assert candidate(str1 = "HEADPHONESHEADPHONES",str2 = "HEADPHONESHEADPHONES") == "HEADPHONESHEADPHONES"
    assert candidate(str1 = "ABCDEFGHABCDEFGHABCDEFGH",str2 = "ABCDEFGHABCDEFGH") == "ABCDEFGH"
    assert candidate(str1 = "SPEAKERSPEAKERSPEAKERSPEAKERSPEAKER",str2 = "SPEAKERSPEAKER") == "SPEAKER"
    assert candidate(str1 = "DIVIDEDIVIDE",str2 = "DIVIDE") == "DIVIDE"
    assert candidate(str1 = "JSJSJSJSJSJSJS",str2 = "JSJSJSJS") == "JS"
    assert candidate(str1 = "CATCATCATCATCATCAT",str2 = "CATCATCAT") == "CATCATCAT"
    assert candidate(str1 = "NOTCOMMONNOTCOMMONNOTCOMMON",str2 = "NOTCOMMONNOT") == ""
    assert candidate(str1 = "XZXZXZXZXZ",str2 = "XZXZ") == "XZ"
    assert candidate(str1 = "DOGDOGDOGDOGDOGDOGDOGDOGDOGDOG",str2 = "DOGDOGDOGDOG") == "DOGDOG"


