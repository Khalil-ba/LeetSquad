def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(columnNumber = 1) == "A"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 1) == "A": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 28) == "AB"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 28) == "AB": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 1045) == "ANE"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 1045) == "ANE": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 2147483647) == "FXSHRXW"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 2147483647) == "FXSHRXW": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 456976) == "YYYZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 456976) == "YYYZ": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 52) == "AZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 52) == "AZ": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 701) == "ZY"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 701) == "ZY": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 1048576) == "BGQCV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 1048576) == "BGQCV": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 26) == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 26) == "Z": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 134217728) == "KGRJXH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 134217728) == "KGRJXH": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 702) == "ZZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 702) == "ZZ": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 1047) == "ANG"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 1047) == "ANG": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 1046527) == "BGNCA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 1046527) == "BGNCA": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 351) == "MM"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 351) == "MM": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 27) == "AA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 27) == "AA": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 4194304) == "IDPOJ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 4194304) == "IDPOJ": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 466527) == "ZNCI"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 466527) == "ZNCI": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 1048575) == "BGQCU"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 1048575) == "BGQCU": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 703) == "AAA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 703) == "AAA": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 1234567) == "BRFGI"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 1234567) == "BRFGI": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 2702) == "CYX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 2702) == "CYX": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 16384) == "XFD"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 16384) == "XFD": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 1000) == "ALL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 1000) == "ALL": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 1379) == "BAA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 1379) == "BAA": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 123456) == "FZPH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 123456) == "FZPH": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 4095) == "FAM"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 4095) == "FAM": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 676) == "YZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 676) == "YZ": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 10000000) == "UVXWJ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 10000000) == "UVXWJ": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 14776336) == "AFHRLP"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 14776336) == "AFHRLP": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 1378) == "AZZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 1378) == "AZZ": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 140625) == "GYZQ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 140625) == "GYZQ": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 728) == "AAZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 728) == "AAZ": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 2704) == "CYZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 2704) == "CYZ": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 18278) == "ZZZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 18278) == "ZZZ": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 234567890) == "SSGWWX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 234567890) == "SSGWWX": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 255) == "IU"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 255) == "IU": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 99999999) == "HJUNYU"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 99999999) == "HJUNYU": {e}')
    
    total += 1
    try:
        result = candidate(columnNumber = 11829215) == "YVZUU"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(columnNumber = 11829215) == "YVZUU": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(columnNumber = 1) == "A"
    assert candidate(columnNumber = 28) == "AB"
    assert candidate(columnNumber = 1045) == "ANE"
    assert candidate(columnNumber = 2147483647) == "FXSHRXW"
    assert candidate(columnNumber = 456976) == "YYYZ"
    assert candidate(columnNumber = 52) == "AZ"
    assert candidate(columnNumber = 701) == "ZY"
    assert candidate(columnNumber = 1048576) == "BGQCV"
    assert candidate(columnNumber = 26) == "Z"
    assert candidate(columnNumber = 134217728) == "KGRJXH"
    assert candidate(columnNumber = 702) == "ZZ"
    assert candidate(columnNumber = 1047) == "ANG"
    assert candidate(columnNumber = 1046527) == "BGNCA"
    assert candidate(columnNumber = 351) == "MM"
    assert candidate(columnNumber = 27) == "AA"
    assert candidate(columnNumber = 4194304) == "IDPOJ"
    assert candidate(columnNumber = 466527) == "ZNCI"
    assert candidate(columnNumber = 1048575) == "BGQCU"
    assert candidate(columnNumber = 703) == "AAA"
    assert candidate(columnNumber = 1234567) == "BRFGI"
    assert candidate(columnNumber = 2702) == "CYX"
    assert candidate(columnNumber = 16384) == "XFD"
    assert candidate(columnNumber = 1000) == "ALL"
    assert candidate(columnNumber = 1379) == "BAA"
    assert candidate(columnNumber = 123456) == "FZPH"
    assert candidate(columnNumber = 4095) == "FAM"
    assert candidate(columnNumber = 676) == "YZ"
    assert candidate(columnNumber = 10000000) == "UVXWJ"
    assert candidate(columnNumber = 14776336) == "AFHRLP"
    assert candidate(columnNumber = 1378) == "AZZ"
    assert candidate(columnNumber = 140625) == "GYZQ"
    assert candidate(columnNumber = 728) == "AAZ"
    assert candidate(columnNumber = 2704) == "CYZ"
    assert candidate(columnNumber = 18278) == "ZZZ"
    assert candidate(columnNumber = 234567890) == "SSGWWX"
    assert candidate(columnNumber = 255) == "IU"
    assert candidate(columnNumber = 99999999) == "HJUNYU"
    assert candidate(columnNumber = 11829215) == "YVZUU"


