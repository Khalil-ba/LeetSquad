def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(votes = ['ABC', 'ACB', 'ABC', 'ACB', 'ACB']) == "ACB"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ABC', 'ACB', 'ABC', 'ACB', 'ACB']) == "ACB": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['WXYZ', 'XYZW']) == "XWYZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['WXYZ', 'XYZW']) == "XWYZ": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['BCA', 'CAB', 'ACB', 'BAC', 'CBA', 'ABC']) == "ABC"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['BCA', 'CAB', 'ACB', 'BAC', 'CBA', 'ABC']) == "ABC": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['A', 'B', 'C', 'D', 'E']) == "ABCDE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['A', 'B', 'C', 'D', 'E']) == "ABCDE": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ABCDEF', 'BCDEFA', 'CDEFAB', 'DEFABC', 'EFABCD', 'FABCDE']) == "ABCDEF"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ABCDEF', 'BCDEFA', 'CDEFAB', 'DEFABC', 'EFABCD', 'FABCDE']) == "ABCDEF": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['BCA', 'CAB', 'CBA', 'ABC', 'ACB', 'BAC']) == "ABC"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['BCA', 'CAB', 'CBA', 'ABC', 'ACB', 'BAC']) == "ABC": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['A', 'A', 'A', 'A', 'A']) == "A"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['A', 'A', 'A', 'A', 'A']) == "A": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['BCA', 'CAB', 'ACB', 'ABC', 'ABC', 'ACB']) == "ACB"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['BCA', 'CAB', 'ACB', 'ABC', 'ABC', 'ACB']) == "ACB": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['A', 'A', 'A', 'A']) == "A"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['A', 'A', 'A', 'A']) == "A": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ZMNAGUEDSJYLBOPHRQICWFXTVK']) == "ZMNAGUEDSJYLBOPHRQICWFXTVK"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ZMNAGUEDSJYLBOPHRQICWFXTVK']) == "ZMNAGUEDSJYLBOPHRQICWFXTVK": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['RGB', 'GBR', 'BRG', 'RBB', 'BBR', 'RBB', 'RRG', 'GRR']) == "RBG"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['RGB', 'GBR', 'BRG', 'RBB', 'BBR', 'RBB', 'RRG', 'GRR']) == "RBG": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ZYXWVUTSRQPONMLKJIHGFEDCBA']) == "AZBYCXDWEVFUGTHSIRJQKPLOMN"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ZYXWVUTSRQPONMLKJIHGFEDCBA']) == "AZBYCXDWEVFUGTHSIRJQKPLOMN": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['BCA', 'CAB', 'ABC', 'ACB', 'BAC']) == "ABC"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['BCA', 'CAB', 'ABC', 'ACB', 'BAC']) == "ABC": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['GHIJKL', 'LKHGJI', 'HKLGJI', 'IGJLKH', 'JIGKHL', 'KGLHJI', 'GHILJK']) == "GHKILJ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['GHIJKL', 'LKHGJI', 'HKLGJI', 'IGJLKH', 'JIGKHL', 'KGLHJI', 'GHILJK']) == "GHKILJ": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['LMNO', 'NOLM', 'OLMN', 'MNLO', 'LNMO', 'ONML', 'MLOL', 'LONM', 'MOLN', 'NOML', 'OMNL', 'LMON', 'NLMO', 'OMLN', 'LMNO', 'NOLM', 'OLMN', 'MNLO', 'LNMO', 'ONML', 'MLOL', 'LONM', 'MOLN', 'NOML', 'OMNL']) == "OLMN"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['LMNO', 'NOLM', 'OLMN', 'MNLO', 'LNMO', 'ONML', 'MLOL', 'LONM', 'MOLN', 'NOML', 'OMNL', 'LMON', 'NLMO', 'OMLN', 'LMNO', 'NOLM', 'OLMN', 'MNLO', 'LNMO', 'ONML', 'MLOL', 'LONM', 'MOLN', 'NOML', 'OMNL']) == "OLMN": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ABCDEFGH', 'BCDEFGHA', 'CDEFGHAB', 'DEFGHABC', 'EFGHABCD', 'FGHABCDE', 'GHABCDEF', 'HABCDEFG']) == "ABCDEFGH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ABCDEFGH', 'BCDEFGHA', 'CDEFGHAB', 'DEFGHABC', 'EFGHABCD', 'FGHABCDE', 'GHABCDEF', 'HABCDEFG']) == "ABCDEFGH": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ABCDEFG', 'GFEDCBA', 'FBCDEAG', 'BCDEAFG', 'CDEABGF', 'DEABCFG', 'EABCDFG']) == "BCEDAFG"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ABCDEFG', 'GFEDCBA', 'FBCDEAG', 'BCDEAFG', 'CDEABGF', 'DEABCFG', 'EABCDFG']) == "BCEDAFG": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ABCD', 'BCDA', 'CDAB', 'DABC', 'ABCD', 'ABCD']) == "ABCD"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ABCD', 'BCDA', 'CDAB', 'DABC', 'ABCD', 'ABCD']) == "ABCD": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['QWOP', 'WOPQ', 'OPQW', 'PQWO', 'QWPO', 'WPOQ', 'OPWQ', 'POWQ']) == "PWOQ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['QWOP', 'WOPQ', 'OPQW', 'PQWO', 'QWPO', 'WPOQ', 'OPWQ', 'POWQ']) == "PWOQ": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['QWERTYUIOPASDFGHJKLZXCVBNM', 'MNBVCXZLKJHGFDSAPOIUYTREWQ', 'QWERTYUIOPASDFGHJKLZXCVBNM', 'MNBVCXZLKJHGFDSAPOIUYTREWQ', 'QWERTYUIOPASDFGHJKLZXCVBNM', 'MNBVCXZLKJHGFDSAPOIUYTREWQ', 'QWERTYUIOPASDFGHJKLZXCVBNM', 'MNBVCXZLKJHGFDSAPOIUYTREWQ', 'QWERTYUIOPASDFGHJKLZXCVBNM', 'MNBVCXZLKJHGFDSAPOIUYTREWQ']) == "MQNWBERVCTXYUZILKOJPAHGSDF"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['QWERTYUIOPASDFGHJKLZXCVBNM', 'MNBVCXZLKJHGFDSAPOIUYTREWQ', 'QWERTYUIOPASDFGHJKLZXCVBNM', 'MNBVCXZLKJHGFDSAPOIUYTREWQ', 'QWERTYUIOPASDFGHJKLZXCVBNM', 'MNBVCXZLKJHGFDSAPOIUYTREWQ', 'QWERTYUIOPASDFGHJKLZXCVBNM', 'MNBVCXZLKJHGFDSAPOIUYTREWQ', 'QWERTYUIOPASDFGHJKLZXCVBNM', 'MNBVCXZLKJHGFDSAPOIUYTREWQ']) == "MQNWBERVCTXYUZILKOJPAHGSDF": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['MNO', 'OMN', 'NMO', 'MON', 'NMN', 'OMM', 'NMM', 'MMM']) == "MNO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['MNO', 'OMN', 'NMO', 'MON', 'NMN', 'OMM', 'NMM', 'MMM']) == "MNO": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['UVWXYZ', 'VWXYZU', 'WXYZUV', 'XYZUVW', 'YZUVWX', 'ZUVWXY', 'UVWXYZ', 'VWXYZU', 'WXYZUV', 'XYZUVW', 'YZUVWX', 'ZUVWXY', 'UVWXYZ', 'VWXYZU', 'WXYZUV', 'XYZUVW', 'YZUVWX', 'ZUVWXY', 'UVWXYZ']) == "UVWXYZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['UVWXYZ', 'VWXYZU', 'WXYZUV', 'XYZUVW', 'YZUVWX', 'ZUVWXY', 'UVWXYZ', 'VWXYZU', 'WXYZUV', 'XYZUVW', 'YZUVWX', 'ZUVWXY', 'UVWXYZ', 'VWXYZU', 'WXYZUV', 'XYZUVW', 'YZUVWX', 'ZUVWXY', 'UVWXYZ']) == "UVWXYZ": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['MATH', 'TEAM', 'META', 'HATE', 'HEAT', 'MATE', 'TAME', 'TIME']) == "TMHAEI"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['MATH', 'TEAM', 'META', 'HATE', 'HEAT', 'MATE', 'TAME', 'TIME']) == "TMHAEI": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ZYX', 'XYZ', 'YZX', 'XZY', 'YXZ', 'ZXY']) == "XYZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ZYX', 'XYZ', 'YZX', 'XZY', 'YXZ', 'ZXY']) == "XYZ": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['PQRST', 'QPRST', 'RQPST', 'SPQRT', 'TQPRS', 'PQRST', 'QPRST', 'RQPST', 'SPQRT', 'TQPRS', 'PQRST', 'QPRST', 'RQPST', 'SPQRT', 'TQPRS']) == "QPRST"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['PQRST', 'QPRST', 'RQPST', 'SPQRT', 'TQPRS', 'PQRST', 'QPRST', 'RQPST', 'SPQRT', 'TQPRS', 'PQRST', 'QPRST', 'RQPST', 'SPQRT', 'TQPRS']) == "QPRST": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ABCD', 'BCDA', 'CDAB', 'DABC', 'ACBD']) == "ACBD"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ABCD', 'BCDA', 'CDAB', 'DABC', 'ACBD']) == "ACBD": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['PQR', 'QPR', 'RQP', 'PRQ', 'RPQ', 'QRP', 'PQR', 'RQP', 'QRP', 'PRQ']) == "PQR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['PQR', 'QPR', 'RQP', 'PRQ', 'RPQ', 'QRP', 'PQR', 'RQP', 'QRP', 'PRQ']) == "PQR": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ZYX', 'YZX', 'XZY', 'XYZ', 'YXZ', 'ZXY', 'YZX', 'ZXY']) == "ZYX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ZYX', 'YZX', 'XZY', 'XYZ', 'YXZ', 'ZXY', 'YZX', 'ZXY']) == "ZYX": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ABCDE', 'EDCBA', 'CBADE', 'BCADE', 'DECAB']) == "BCDEA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ABCDE', 'EDCBA', 'CBADE', 'BCADE', 'DECAB']) == "BCDEA": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ABC', 'BAC', 'BCA', 'CAB', 'CBA', 'ACB', 'BAC', 'CAB', 'CBA', 'BCA', 'ACB', 'CAB', 'CBA', 'BCA', 'ACB', 'BAC', 'CAB', 'CBA', 'BCA', 'ACB', 'BAC', 'CAB', 'CBA', 'BCA', 'ACB']) == "CBA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ABC', 'BAC', 'BCA', 'CAB', 'CBA', 'ACB', 'BAC', 'CAB', 'CBA', 'BCA', 'ACB', 'CAB', 'CBA', 'BCA', 'ACB', 'BAC', 'CAB', 'CBA', 'BCA', 'ACB', 'BAC', 'CAB', 'CBA', 'BCA', 'ACB']) == "CBA": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ABCD', 'BCDA', 'CDAB', 'DABC']) == "ABCD"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ABCD', 'BCDA', 'CDAB', 'DABC']) == "ABCD": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA']) == "AB"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA']) == "AB": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['QWERTYUIOPASDFGHJKLZXCVBNM', 'QWERTYUIOPASDFGHJKLZXCVBNM', 'QWERTYUIOPASDFGHJKLZXCVBNM']) == "QWERTYUIOPASDFGHJKLZXCVBNM"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['QWERTYUIOPASDFGHJKLZXCVBNM', 'QWERTYUIOPASDFGHJKLZXCVBNM', 'QWERTYUIOPASDFGHJKLZXCVBNM']) == "QWERTYUIOPASDFGHJKLZXCVBNM": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY']) == "XYZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY']) == "XYZ": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG']) == "IHGFEJ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG']) == "IHGFEJ": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['XYZ', 'YZX', 'ZXY', 'YXZ', 'XZY', 'ZYX', 'XYZ', 'YZX']) == "YXZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['XYZ', 'YZX', 'ZXY', 'YXZ', 'XZY', 'ZYX', 'XYZ', 'YZX']) == "YXZ": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA']) == "AB"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA']) == "AB": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['TLI', 'LIT', 'ITL', 'TIL', 'ILT', 'LTI', 'TIL', 'LTI', 'ILT', 'TLI']) == "TLI"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['TLI', 'LIT', 'ITL', 'TIL', 'ILT', 'LTI', 'TIL', 'LTI', 'ILT', 'TLI']) == "TLI": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['QWERTY', 'QWRETY', 'QWRTEY', 'QWRTYE', 'QWRYTE']) == "QWRETY"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['QWERTY', 'QWRETY', 'QWRTEY', 'QWRTYE', 'QWRYTE']) == "QWRETY": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ZEBRA', 'BRACE', 'BEZAR', 'RABZE', 'AREBZ', 'ZERBA']) == "BZRAEC"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ZEBRA', 'BRACE', 'BEZAR', 'RABZE', 'AREBZ', 'ZERBA']) == "BZRAEC": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ZYX', 'YXZ', 'XYZ', 'YZX', 'XZY', 'ZXY']) == "XYZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ZYX', 'YXZ', 'XYZ', 'YZX', 'XZY', 'ZXY']) == "XYZ": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['GHIJK', 'HIJKG', 'IJKGH', 'JKGHI', 'KGIJH', 'GHIJK', 'HGIJK', 'IGHJK', 'JGIHK', 'KGIJH']) == "GHIJK"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['GHIJK', 'HIJKG', 'IJKGH', 'JKGHI', 'KGIJH', 'GHIJK', 'HGIJK', 'IGHJK', 'JGIHK', 'KGIJH']) == "GHIJK": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['WXYZ', 'YZWX', 'ZWXY', 'XWYZ', 'WZYX', 'XYZW']) == "WXZY"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['WXYZ', 'YZWX', 'ZWXY', 'XWYZ', 'WZYX', 'XYZW']) == "WXZY": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['PQRSTU', 'QPRSTU', 'QRPTSU', 'QRSTUP', 'QPRTSU', 'QTRPSU', 'QTRSPU', 'QTSRPU', 'QTSPUR', 'QTPRSU', 'QTPSUR', 'QTUSPR', 'QTUSRP', 'QTURPS', 'QTURSP', 'QTUPRS', 'QTUPSR', 'QTRSPU', 'QTSRPU', 'QTRPUS', 'QTRUPS', 'QTPRSU', 'QTPSUR', 'QTUSPR', 'QTURPS', 'QTURSP', 'QTUPRS', 'QTUPSR']) == "QPTRUS"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['PQRSTU', 'QPRSTU', 'QRPTSU', 'QRSTUP', 'QPRTSU', 'QTRPSU', 'QTRSPU', 'QTSRPU', 'QTSPUR', 'QTPRSU', 'QTPSUR', 'QTUSPR', 'QTUSRP', 'QTURPS', 'QTURSP', 'QTUPRS', 'QTUPSR', 'QTRSPU', 'QTSRPU', 'QTRPUS', 'QTRUPS', 'QTPRSU', 'QTPSUR', 'QTUSPR', 'QTURPS', 'QTURSP', 'QTUPRS', 'QTUPSR']) == "QPTRUS": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ABCD', 'DCBA', 'BCAD', 'CADB', 'ACDB', 'DABC', 'BCDA']) == "ABDC"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ABCD', 'DCBA', 'BCAD', 'CADB', 'ACDB', 'DABC', 'BCDA']) == "ABDC": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['LOVE', 'VOTE', 'LEVO', 'OVEL', 'VOLE', 'ELOV']) == "VLOET"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['LOVE', 'VOTE', 'LEVO', 'OVEL', 'VOLE', 'ELOV']) == "VLOET": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['LMNO', 'MLON', 'OLNM', 'NOLM', 'ONML', 'MNLO', 'LOMN', 'LONM', 'NMLO', 'OMNL', 'NOLM', 'OLNM']) == "OLNM"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['LMNO', 'MLON', 'OLNM', 'NOLM', 'ONML', 'MNLO', 'LOMN', 'LONM', 'NMLO', 'OMNL', 'NOLM', 'OLNM']) == "OLNM": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'F', 'F', 'F', 'F', 'G', 'G', 'G', 'G', 'H', 'H', 'H', 'H', 'I', 'I', 'I', 'I', 'J', 'J', 'J', 'J', 'K', 'K', 'K', 'K', 'L', 'L', 'L', 'L', 'M', 'M', 'M', 'M', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'P', 'P', 'P', 'P', 'Q', 'Q', 'Q', 'Q', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', 'V', 'V', 'V', 'V', 'W', 'W', 'W', 'W', 'X', 'X', 'X', 'X', 'Y', 'Y', 'Y', 'Y', 'Z', 'Z', 'Z', 'Z']) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'F', 'F', 'F', 'F', 'G', 'G', 'G', 'G', 'H', 'H', 'H', 'H', 'I', 'I', 'I', 'I', 'J', 'J', 'J', 'J', 'K', 'K', 'K', 'K', 'L', 'L', 'L', 'L', 'M', 'M', 'M', 'M', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'P', 'P', 'P', 'P', 'Q', 'Q', 'Q', 'Q', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', 'V', 'V', 'V', 'V', 'W', 'W', 'W', 'W', 'X', 'X', 'X', 'X', 'Y', 'Y', 'Y', 'Y', 'Z', 'Z', 'Z', 'Z']) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ABCDEF', 'FEDCBA', 'DEFABC', 'BCDAFE', 'CBAFED', 'AFECBD', 'BDFECA']) == "BAFDCE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ABCDEF', 'FEDCBA', 'DEFABC', 'BCDAFE', 'CBAFED', 'AFECBD', 'BDFECA']) == "BAFDCE": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['AC', 'CA', 'AC', 'CA', 'AC', 'CA', 'AC', 'CA', 'AC', 'CA']) == "AC"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['AC', 'CA', 'AC', 'CA', 'AC', 'CA', 'AC', 'CA', 'AC', 'CA']) == "AC": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['LMNO', 'MLNO', 'NOLM', 'OLMN', 'NOML', 'OMNL', 'LONM', 'OLNM', 'MOLN', 'LNOM', 'LOMN', 'MONL', 'NLOM', 'LNMO', 'LNMN', 'OMLN', 'NOLM', 'NLMO', 'MOLN', 'ONLM', 'OMNL', 'LONM', 'OLNM', 'MOLN', 'LNOM', 'LOMN', 'MONL', 'NLOM', 'LNMO', 'LNMN']) == "LONM"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['LMNO', 'MLNO', 'NOLM', 'OLMN', 'NOML', 'OMNL', 'LONM', 'OLNM', 'MOLN', 'LNOM', 'LOMN', 'MONL', 'NLOM', 'LNMO', 'LNMN', 'OMLN', 'NOLM', 'NLMO', 'MOLN', 'ONLM', 'OMNL', 'LONM', 'OLNM', 'MOLN', 'LNOM', 'LOMN', 'MONL', 'NLOM', 'LNMO', 'LNMN']) == "LONM": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['PQRST', 'QPRST', 'RSPTQ', 'TRPQS', 'SQPTR', 'PRQST', 'PQRST', 'RQPTS', 'TQRS', 'SPRQT']) == "PRSTQ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['PQRST', 'QPRST', 'RSPTQ', 'TRPQS', 'SQPTR', 'PRQST', 'PQRST', 'RQPTS', 'TQRS', 'SPRQT']) == "PRSTQ": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['PQR', 'QRP', 'RPQ', 'PRQ', 'QPR', 'RQP', 'PQR', 'QRP', 'RPQ', 'PRQ', 'QPR', 'RQP']) == "PQR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['PQR', 'QRP', 'RPQ', 'PRQ', 'QPR', 'RQP', 'PQR', 'QRP', 'RPQ', 'PRQ', 'QPR', 'RQP']) == "PQR": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ABCDE', 'ACBDE', 'CABDE', 'BCADE', 'DCABE']) == "ACBDE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ABCDE', 'ACBDE', 'CABDE', 'BCADE', 'DCABE']) == "ACBDE": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['XYZ', 'YXZ', 'YZX', 'ZXY', 'ZYX', 'XZY', 'YZX', 'ZYX', 'XYZ', 'YXZ', 'XZY', 'XYZ']) == "XYZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['XYZ', 'YXZ', 'YZX', 'ZXY', 'ZYX', 'XZY', 'YZX', 'ZYX', 'XYZ', 'YXZ', 'XZY', 'XYZ']) == "XYZ": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['FGHIJK', 'GHIJKF', 'HIJKFG', 'IJKFGH', 'JKFGHI', 'KFGHIJ', 'FGHIJK', 'GHIJKF', 'HIJKFG', 'IJKFGH']) == "IHGFJK"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['FGHIJK', 'GHIJKF', 'HIJKFG', 'IJKFGH', 'JKFGHI', 'KFGHIJ', 'FGHIJK', 'GHIJKF', 'HIJKFG', 'IJKFGH']) == "IHGFJK": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ACBD', 'BDAC', 'CDAB', 'DABC', 'ABCD', 'BACD', 'CABD', 'DABC', 'ACDB', 'BCDA']) == "ABCD"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ACBD', 'BDAC', 'CDAB', 'DABC', 'ABCD', 'BACD', 'CABD', 'DABC', 'ACDB', 'BCDA']) == "ABCD": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ABCD', 'ABDC', 'ACBD', 'ACDB', 'ADBC', 'ADCB', 'BACD', 'BADC', 'BCAD', 'BCDA', 'BDAC', 'BDCA', 'CABD', 'CADB', 'CBAD', 'CBDA', 'CDAB', 'CDBA', 'DABC', 'DACB', 'DBAC', 'DBCA', 'DCAB', 'DCBA']) == "ABCD"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ABCD', 'ABDC', 'ACBD', 'ACDB', 'ADBC', 'ADCB', 'BACD', 'BADC', 'BCAD', 'BCDA', 'BDAC', 'BDCA', 'CABD', 'CADB', 'CBAD', 'CBDA', 'CDAB', 'CDBA', 'DABC', 'DACB', 'DBAC', 'DBCA', 'DCAB', 'DCBA']) == "ABCD": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['UVWX', 'VWXU', 'WXUV', 'XUVW', 'UVWX', 'VWXU', 'WXUV', 'XUVW', 'UVWX', 'VWXU']) == "VUWX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['UVWX', 'VWXU', 'WXUV', 'XUVW', 'UVWX', 'VWXU', 'WXUV', 'XUVW', 'UVWX', 'VWXU']) == "VUWX": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ZR', 'RZ', 'ZR', 'RZ', 'ZR']) == "ZR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ZR', 'RZ', 'ZR', 'RZ', 'ZR']) == "ZR": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['SUNNY', 'UNNYS', 'NUNYS', 'NNYSU', 'NUYNS', 'USNNY', 'NSUNY']) == "NUSY"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['SUNNY', 'UNNYS', 'NUNYS', 'NNYSU', 'NUYNS', 'USNNY', 'NSUNY']) == "NUSY": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['HELLO', 'OLLEH', 'LOHEL', 'LLOEH', 'HLOEL', 'ELOHL', 'ELLOH', 'OLEHL', 'LELOH', 'OHELL']) == "LOEH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['HELLO', 'OLLEH', 'LOHEL', 'LLOEH', 'HLOEL', 'ELOHL', 'ELLOH', 'OLEHL', 'LELOH', 'OHELL']) == "LOEH": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ACB', 'BAC', 'CBA', 'BCA', 'CAB', 'ACB', 'BAC', 'CBA', 'BCA', 'CAB', 'ACB', 'BAC', 'CBA']) == "CBA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ACB', 'BAC', 'CBA', 'BCA', 'CAB', 'ACB', 'BAC', 'CBA', 'BCA', 'CAB', 'ACB', 'BAC', 'CBA']) == "CBA": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'JEFGH', 'EFGIH', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'JEFGH', 'EFGIH', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'JEFGH', 'EFGIH', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'JEFGH', 'EFGIH']) == "EFGIJH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'JEFGH', 'EFGIH', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'JEFGH', 'EFGIH', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'JEFGH', 'EFGIH', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'JEFGH', 'EFGIH']) == "EFGIJH": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['QWRTY', 'QWYRT', 'WQRTY', 'WQYRT', 'RTQWY', 'RTYQW', 'YRQWT', 'YRTQW', 'TWQRY', 'TYWQR']) == "WQRTY"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['QWRTY', 'QWYRT', 'WQRTY', 'WQYRT', 'RTQWY', 'RTYQW', 'YRQWT', 'YRTQW', 'TWQRY', 'TYWQR']) == "WQRTY": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['PYTHON', 'TYHONP', 'YHTNPO', 'HNOTYP', 'NOTYHP', 'OTHNYP']) == "YTHONP"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['PYTHON', 'TYHONP', 'YHTNPO', 'HNOTYP', 'NOTYHP', 'OTHNYP']) == "YTHONP": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['MNO', 'NOM', 'OMN', 'MON', 'NMO', 'OMN', 'MNO']) == "MNO"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['MNO', 'NOM', 'OMN', 'MON', 'NMO', 'OMN', 'MNO']) == "MNO": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['MNO', 'OMN', 'NMO', 'MON', 'NOM', 'OMN']) == "MON"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['MNO', 'OMN', 'NMO', 'MON', 'NOM', 'OMN']) == "MON": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ABCD', 'DCBA', 'BCDA', 'CBAD', 'ADBC', 'BDAC', 'ACBD', 'CADB', 'DABC', 'DBCA']) == "ADBC"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ABCD', 'DCBA', 'BCDA', 'CBAD', 'ADBC', 'BDAC', 'ACBD', 'CADB', 'DABC', 'DBCA']) == "ADBC": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['FGHIJ', 'IJFGH', 'JFGHI', 'HGIJF', 'IGHFJ', 'GFHIJ']) == "IGFJH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['FGHIJ', 'IJFGH', 'JFGHI', 'HGIJF', 'IGHFJ', 'GFHIJ']) == "IGFJH": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['VWXYZ', 'YZWXV', 'ZWXYV', 'XWYZV', 'WZYXV', 'XYZWV', 'VWYZX', 'WVXYZ', 'XYZVW', 'YZXVW', 'ZXYVW', 'VZWXY', 'WXYVZ', 'XVZXY', 'YZVWX', 'ZVXYW', 'VXYWZ', 'XYWVZ', 'YWVZX', 'YVZXW', 'VZXWY', 'ZXWYV', 'XWYVZ']) == "XVYZW"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['VWXYZ', 'YZWXV', 'ZWXYV', 'XWYZV', 'WZYXV', 'XYZWV', 'VWYZX', 'WVXYZ', 'XYZVW', 'YZXVW', 'ZXYVW', 'VZWXY', 'WXYVZ', 'XVZXY', 'YZVWX', 'ZVXYW', 'VXYWZ', 'XYWVZ', 'YWVZX', 'YVZXW', 'VZXWY', 'ZXWYV', 'XWYVZ']) == "XVYZW": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['ABCDE', 'ABCDE', 'ABCDE', 'EABCD', 'DEABC']) == "AEDBC"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['ABCDE', 'ABCDE', 'ABCDE', 'EABCD', 'DEABC']) == "AEDBC": {e}')
    
    total += 1
    try:
        result = candidate(votes = ['UV', 'VU', 'UV', 'UV', 'VU', 'UV', 'UV', 'VU', 'VU', 'VU', 'UV', 'VU', 'VU', 'VU', 'VU', 'VU', 'VU', 'VU', 'VU', 'VU']) == "VU"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(votes = ['UV', 'VU', 'UV', 'UV', 'VU', 'UV', 'UV', 'VU', 'VU', 'VU', 'UV', 'VU', 'VU', 'VU', 'VU', 'VU', 'VU', 'VU', 'VU', 'VU']) == "VU": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(votes = ['ABC', 'ACB', 'ABC', 'ACB', 'ACB']) == "ACB"
    assert candidate(votes = ['WXYZ', 'XYZW']) == "XWYZ"
    assert candidate(votes = ['BCA', 'CAB', 'ACB', 'BAC', 'CBA', 'ABC']) == "ABC"
    assert candidate(votes = ['A', 'B', 'C', 'D', 'E']) == "ABCDE"
    assert candidate(votes = ['ABCDEF', 'BCDEFA', 'CDEFAB', 'DEFABC', 'EFABCD', 'FABCDE']) == "ABCDEF"
    assert candidate(votes = ['BCA', 'CAB', 'CBA', 'ABC', 'ACB', 'BAC']) == "ABC"
    assert candidate(votes = ['A', 'A', 'A', 'A', 'A']) == "A"
    assert candidate(votes = ['BCA', 'CAB', 'ACB', 'ABC', 'ABC', 'ACB']) == "ACB"
    assert candidate(votes = ['A', 'A', 'A', 'A']) == "A"
    assert candidate(votes = ['ZMNAGUEDSJYLBOPHRQICWFXTVK']) == "ZMNAGUEDSJYLBOPHRQICWFXTVK"
    assert candidate(votes = ['RGB', 'GBR', 'BRG', 'RBB', 'BBR', 'RBB', 'RRG', 'GRR']) == "RBG"
    assert candidate(votes = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ZYXWVUTSRQPONMLKJIHGFEDCBA']) == "AZBYCXDWEVFUGTHSIRJQKPLOMN"
    assert candidate(votes = ['BCA', 'CAB', 'ABC', 'ACB', 'BAC']) == "ABC"
    assert candidate(votes = ['GHIJKL', 'LKHGJI', 'HKLGJI', 'IGJLKH', 'JIGKHL', 'KGLHJI', 'GHILJK']) == "GHKILJ"
    assert candidate(votes = ['LMNO', 'NOLM', 'OLMN', 'MNLO', 'LNMO', 'ONML', 'MLOL', 'LONM', 'MOLN', 'NOML', 'OMNL', 'LMON', 'NLMO', 'OMLN', 'LMNO', 'NOLM', 'OLMN', 'MNLO', 'LNMO', 'ONML', 'MLOL', 'LONM', 'MOLN', 'NOML', 'OMNL']) == "OLMN"
    assert candidate(votes = ['ABCDEFGH', 'BCDEFGHA', 'CDEFGHAB', 'DEFGHABC', 'EFGHABCD', 'FGHABCDE', 'GHABCDEF', 'HABCDEFG']) == "ABCDEFGH"
    assert candidate(votes = ['ABCDEFG', 'GFEDCBA', 'FBCDEAG', 'BCDEAFG', 'CDEABGF', 'DEABCFG', 'EABCDFG']) == "BCEDAFG"
    assert candidate(votes = ['ABCD', 'BCDA', 'CDAB', 'DABC', 'ABCD', 'ABCD']) == "ABCD"
    assert candidate(votes = ['QWOP', 'WOPQ', 'OPQW', 'PQWO', 'QWPO', 'WPOQ', 'OPWQ', 'POWQ']) == "PWOQ"
    assert candidate(votes = ['QWERTYUIOPASDFGHJKLZXCVBNM', 'MNBVCXZLKJHGFDSAPOIUYTREWQ', 'QWERTYUIOPASDFGHJKLZXCVBNM', 'MNBVCXZLKJHGFDSAPOIUYTREWQ', 'QWERTYUIOPASDFGHJKLZXCVBNM', 'MNBVCXZLKJHGFDSAPOIUYTREWQ', 'QWERTYUIOPASDFGHJKLZXCVBNM', 'MNBVCXZLKJHGFDSAPOIUYTREWQ', 'QWERTYUIOPASDFGHJKLZXCVBNM', 'MNBVCXZLKJHGFDSAPOIUYTREWQ']) == "MQNWBERVCTXYUZILKOJPAHGSDF"
    assert candidate(votes = ['MNO', 'OMN', 'NMO', 'MON', 'NMN', 'OMM', 'NMM', 'MMM']) == "MNO"
    assert candidate(votes = ['UVWXYZ', 'VWXYZU', 'WXYZUV', 'XYZUVW', 'YZUVWX', 'ZUVWXY', 'UVWXYZ', 'VWXYZU', 'WXYZUV', 'XYZUVW', 'YZUVWX', 'ZUVWXY', 'UVWXYZ', 'VWXYZU', 'WXYZUV', 'XYZUVW', 'YZUVWX', 'ZUVWXY', 'UVWXYZ']) == "UVWXYZ"
    assert candidate(votes = ['MATH', 'TEAM', 'META', 'HATE', 'HEAT', 'MATE', 'TAME', 'TIME']) == "TMHAEI"
    assert candidate(votes = ['ZYX', 'XYZ', 'YZX', 'XZY', 'YXZ', 'ZXY']) == "XYZ"
    assert candidate(votes = ['PQRST', 'QPRST', 'RQPST', 'SPQRT', 'TQPRS', 'PQRST', 'QPRST', 'RQPST', 'SPQRT', 'TQPRS', 'PQRST', 'QPRST', 'RQPST', 'SPQRT', 'TQPRS']) == "QPRST"
    assert candidate(votes = ['ABCD', 'BCDA', 'CDAB', 'DABC', 'ACBD']) == "ACBD"
    assert candidate(votes = ['PQR', 'QPR', 'RQP', 'PRQ', 'RPQ', 'QRP', 'PQR', 'RQP', 'QRP', 'PRQ']) == "PQR"
    assert candidate(votes = ['ZYX', 'YZX', 'XZY', 'XYZ', 'YXZ', 'ZXY', 'YZX', 'ZXY']) == "ZYX"
    assert candidate(votes = ['ABCDE', 'EDCBA', 'CBADE', 'BCADE', 'DECAB']) == "BCDEA"
    assert candidate(votes = ['ABC', 'BAC', 'BCA', 'CAB', 'CBA', 'ACB', 'BAC', 'CAB', 'CBA', 'BCA', 'ACB', 'CAB', 'CBA', 'BCA', 'ACB', 'BAC', 'CAB', 'CBA', 'BCA', 'ACB', 'BAC', 'CAB', 'CBA', 'BCA', 'ACB']) == "CBA"
    assert candidate(votes = ['ABCD', 'BCDA', 'CDAB', 'DABC']) == "ABCD"
    assert candidate(votes = ['AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA']) == "AB"
    assert candidate(votes = ['QWERTYUIOPASDFGHJKLZXCVBNM', 'QWERTYUIOPASDFGHJKLZXCVBNM', 'QWERTYUIOPASDFGHJKLZXCVBNM']) == "QWERTYUIOPASDFGHJKLZXCVBNM"
    assert candidate(votes = ['XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY', 'XYZ', 'YZX', 'ZXY']) == "XYZ"
    assert candidate(votes = ['EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG']) == "IHGFEJ"
    assert candidate(votes = ['XYZ', 'YZX', 'ZXY', 'YXZ', 'XZY', 'ZYX', 'XYZ', 'YZX']) == "YXZ"
    assert candidate(votes = ['AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA', 'AB', 'BA']) == "AB"
    assert candidate(votes = ['TLI', 'LIT', 'ITL', 'TIL', 'ILT', 'LTI', 'TIL', 'LTI', 'ILT', 'TLI']) == "TLI"
    assert candidate(votes = ['QWERTY', 'QWRETY', 'QWRTEY', 'QWRTYE', 'QWRYTE']) == "QWRETY"
    assert candidate(votes = ['ZEBRA', 'BRACE', 'BEZAR', 'RABZE', 'AREBZ', 'ZERBA']) == "BZRAEC"
    assert candidate(votes = ['ZYX', 'YXZ', 'XYZ', 'YZX', 'XZY', 'ZXY']) == "XYZ"
    assert candidate(votes = ['GHIJK', 'HIJKG', 'IJKGH', 'JKGHI', 'KGIJH', 'GHIJK', 'HGIJK', 'IGHJK', 'JGIHK', 'KGIJH']) == "GHIJK"
    assert candidate(votes = ['WXYZ', 'YZWX', 'ZWXY', 'XWYZ', 'WZYX', 'XYZW']) == "WXZY"
    assert candidate(votes = ['PQRSTU', 'QPRSTU', 'QRPTSU', 'QRSTUP', 'QPRTSU', 'QTRPSU', 'QTRSPU', 'QTSRPU', 'QTSPUR', 'QTPRSU', 'QTPSUR', 'QTUSPR', 'QTUSRP', 'QTURPS', 'QTURSP', 'QTUPRS', 'QTUPSR', 'QTRSPU', 'QTSRPU', 'QTRPUS', 'QTRUPS', 'QTPRSU', 'QTPSUR', 'QTUSPR', 'QTURPS', 'QTURSP', 'QTUPRS', 'QTUPSR']) == "QPTRUS"
    assert candidate(votes = ['ABCD', 'DCBA', 'BCAD', 'CADB', 'ACDB', 'DABC', 'BCDA']) == "ABDC"
    assert candidate(votes = ['LOVE', 'VOTE', 'LEVO', 'OVEL', 'VOLE', 'ELOV']) == "VLOET"
    assert candidate(votes = ['LMNO', 'MLON', 'OLNM', 'NOLM', 'ONML', 'MNLO', 'LOMN', 'LONM', 'NMLO', 'OMNL', 'NOLM', 'OLNM']) == "OLNM"
    assert candidate(votes = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'F', 'F', 'F', 'F', 'G', 'G', 'G', 'G', 'H', 'H', 'H', 'H', 'I', 'I', 'I', 'I', 'J', 'J', 'J', 'J', 'K', 'K', 'K', 'K', 'L', 'L', 'L', 'L', 'M', 'M', 'M', 'M', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'P', 'P', 'P', 'P', 'Q', 'Q', 'Q', 'Q', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', 'V', 'V', 'V', 'V', 'W', 'W', 'W', 'W', 'X', 'X', 'X', 'X', 'Y', 'Y', 'Y', 'Y', 'Z', 'Z', 'Z', 'Z']) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert candidate(votes = ['ABCDEF', 'FEDCBA', 'DEFABC', 'BCDAFE', 'CBAFED', 'AFECBD', 'BDFECA']) == "BAFDCE"
    assert candidate(votes = ['AC', 'CA', 'AC', 'CA', 'AC', 'CA', 'AC', 'CA', 'AC', 'CA']) == "AC"
    assert candidate(votes = ['LMNO', 'MLNO', 'NOLM', 'OLMN', 'NOML', 'OMNL', 'LONM', 'OLNM', 'MOLN', 'LNOM', 'LOMN', 'MONL', 'NLOM', 'LNMO', 'LNMN', 'OMLN', 'NOLM', 'NLMO', 'MOLN', 'ONLM', 'OMNL', 'LONM', 'OLNM', 'MOLN', 'LNOM', 'LOMN', 'MONL', 'NLOM', 'LNMO', 'LNMN']) == "LONM"
    assert candidate(votes = ['PQRST', 'QPRST', 'RSPTQ', 'TRPQS', 'SQPTR', 'PRQST', 'PQRST', 'RQPTS', 'TQRS', 'SPRQT']) == "PRSTQ"
    assert candidate(votes = ['PQR', 'QRP', 'RPQ', 'PRQ', 'QPR', 'RQP', 'PQR', 'QRP', 'RPQ', 'PRQ', 'QPR', 'RQP']) == "PQR"
    assert candidate(votes = ['ABCDE', 'ACBDE', 'CABDE', 'BCADE', 'DCABE']) == "ACBDE"
    assert candidate(votes = ['XYZ', 'YXZ', 'YZX', 'ZXY', 'ZYX', 'XZY', 'YZX', 'ZYX', 'XYZ', 'YXZ', 'XZY', 'XYZ']) == "XYZ"
    assert candidate(votes = ['FGHIJK', 'GHIJKF', 'HIJKFG', 'IJKFGH', 'JKFGHI', 'KFGHIJ', 'FGHIJK', 'GHIJKF', 'HIJKFG', 'IJKFGH']) == "IHGFJK"
    assert candidate(votes = ['ACBD', 'BDAC', 'CDAB', 'DABC', 'ABCD', 'BACD', 'CABD', 'DABC', 'ACDB', 'BCDA']) == "ABCD"
    assert candidate(votes = ['ABCD', 'ABDC', 'ACBD', 'ACDB', 'ADBC', 'ADCB', 'BACD', 'BADC', 'BCAD', 'BCDA', 'BDAC', 'BDCA', 'CABD', 'CADB', 'CBAD', 'CBDA', 'CDAB', 'CDBA', 'DABC', 'DACB', 'DBAC', 'DBCA', 'DCAB', 'DCBA']) == "ABCD"
    assert candidate(votes = ['UVWX', 'VWXU', 'WXUV', 'XUVW', 'UVWX', 'VWXU', 'WXUV', 'XUVW', 'UVWX', 'VWXU']) == "VUWX"
    assert candidate(votes = ['ZR', 'RZ', 'ZR', 'RZ', 'ZR']) == "ZR"
    assert candidate(votes = ['SUNNY', 'UNNYS', 'NUNYS', 'NNYSU', 'NUYNS', 'USNNY', 'NSUNY']) == "NUSY"
    assert candidate(votes = ['HELLO', 'OLLEH', 'LOHEL', 'LLOEH', 'HLOEL', 'ELOHL', 'ELLOH', 'OLEHL', 'LELOH', 'OHELL']) == "LOEH"
    assert candidate(votes = ['ACB', 'BAC', 'CBA', 'BCA', 'CAB', 'ACB', 'BAC', 'CBA', 'BCA', 'CAB', 'ACB', 'BAC', 'CBA']) == "CBA"
    assert candidate(votes = ['EFGHI', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'JEFGH', 'EFGIH', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'JEFGH', 'EFGIH', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'JEFGH', 'EFGIH', 'FGHIJ', 'GHIJE', 'HIJEF', 'IJEFG', 'JEFGH', 'EFGIH']) == "EFGIJH"
    assert candidate(votes = ['QWRTY', 'QWYRT', 'WQRTY', 'WQYRT', 'RTQWY', 'RTYQW', 'YRQWT', 'YRTQW', 'TWQRY', 'TYWQR']) == "WQRTY"
    assert candidate(votes = ['PYTHON', 'TYHONP', 'YHTNPO', 'HNOTYP', 'NOTYHP', 'OTHNYP']) == "YTHONP"
    assert candidate(votes = ['MNO', 'NOM', 'OMN', 'MON', 'NMO', 'OMN', 'MNO']) == "MNO"
    assert candidate(votes = ['MNO', 'OMN', 'NMO', 'MON', 'NOM', 'OMN']) == "MON"
    assert candidate(votes = ['ABCD', 'DCBA', 'BCDA', 'CBAD', 'ADBC', 'BDAC', 'ACBD', 'CADB', 'DABC', 'DBCA']) == "ADBC"
    assert candidate(votes = ['FGHIJ', 'IJFGH', 'JFGHI', 'HGIJF', 'IGHFJ', 'GFHIJ']) == "IGFJH"
    assert candidate(votes = ['VWXYZ', 'YZWXV', 'ZWXYV', 'XWYZV', 'WZYXV', 'XYZWV', 'VWYZX', 'WVXYZ', 'XYZVW', 'YZXVW', 'ZXYVW', 'VZWXY', 'WXYVZ', 'XVZXY', 'YZVWX', 'ZVXYW', 'VXYWZ', 'XYWVZ', 'YWVZX', 'YVZXW', 'VZXWY', 'ZXWYV', 'XWYVZ']) == "XVYZW"
    assert candidate(votes = ['ABCDE', 'ABCDE', 'ABCDE', 'EABCD', 'DEABC']) == "AEDBC"
    assert candidate(votes = ['UV', 'VU', 'UV', 'UV', 'VU', 'UV', 'UV', 'VU', 'VU', 'VU', 'UV', 'VU', 'VU', 'VU', 'VU', 'VU', 'VU', 'VU', 'VU', 'VU']) == "VU"


