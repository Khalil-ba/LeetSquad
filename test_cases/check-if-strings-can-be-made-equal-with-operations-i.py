def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "cdab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "cdab") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "acbd",s2 = "bdac") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "acbd",s2 = "bdac") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abab",s2 = "abcd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abab",s2 = "abcd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abdc",s2 = "cdab") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abdc",s2 = "cdab") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "dacb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "dacb") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abab",s2 = "baba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abab",s2 = "baba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "abcd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "abcd") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabb",s2 = "bbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabb",s2 = "bbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "dcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "dcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzz",s2 = "zzzz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzz",s2 = "zzzz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zabc",s2 = "cbaz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zabc",s2 = "cbaz") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "efef",s2 = "fefo") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "efef",s2 = "fefo") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "dcab") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "dcab") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "dbca") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "dbca") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "qrst",s2 = "tqsr") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "qrst",s2 = "tqsr") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mnop",s2 = "ponq") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mnop",s2 = "ponq") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ijkl",s2 = "lkji") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ijkl",s2 = "lkji") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "cabd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "cabd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "wxxy",s2 = "yxwx") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "wxxy",s2 = "yxwx") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "abdc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "abdc") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "qrst",s2 = "tsqr") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "qrst",s2 = "tsqr") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abba",s2 = "baab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abba",s2 = "baab") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "cadb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "cadb") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "cdac") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "cdac") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "wxyz",s2 = "yxwz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "wxyz",s2 = "yxwz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abac",s2 = "cabd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abac",s2 = "cabd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mnop",s2 = "npom") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mnop",s2 = "npom") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ijkl",s2 = "lkij") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ijkl",s2 = "lkij") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "efgh",s2 = "fegh") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "efgh",s2 = "fegh") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "pqrs",s2 = "rqps") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "pqrs",s2 = "rqps") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "uvwx",s2 = "xwvu") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "uvwx",s2 = "xwvu") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "wxyz",s2 = "xywz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "wxyz",s2 = "xywz") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxy",s2 = "yxyx") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxy",s2 = "yxyx") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "efgh",s2 = "hgfq") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "efgh",s2 = "hgfq") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "dbac") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "dbac") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabb",s2 = "abab") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabb",s2 = "abab") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mnop",s2 = "ponm") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mnop",s2 = "ponm") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "bdca") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "bdca") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "qrst",s2 = "tsrf") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "qrst",s2 = "tsrf") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "qrst",s2 = "tsrq") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "qrst",s2 = "tsrq") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "badc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "badc") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "qrst",s2 = "tqrs") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "qrst",s2 = "tqrs") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "adcb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "adcb") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mnop",s2 = "pmno") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mnop",s2 = "pmno") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abba",s2 = "baba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abba",s2 = "baba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "bacd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "bacd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abca",s2 = "acba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abca",s2 = "acba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "bdac") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "bdac") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mnop",s2 = "onmp") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mnop",s2 = "onmp") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "lwxy",s2 = "xylw") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "lwxy",s2 = "xylw") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzza",s2 = "zzaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzza",s2 = "zzaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "acdb") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "acdb") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzz",s2 = "zzaz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzz",s2 = "zzaz") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabb",s2 = "abba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabb",s2 = "abba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "acbd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "acbd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "wxyz",s2 = "xyzw") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "wxyz",s2 = "xyzw") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyz",s2 = "zyxz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyz",s2 = "zyxz") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "dabc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "dabc") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "pqrs",s2 = "rspq") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "pqrs",s2 = "rspq") == True: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zyxw",s2 = "xwyz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zyxw",s2 = "xwyz") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "abca") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "abca") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abca",s2 = "cabd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abca",s2 = "cabd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mnop",s2 = "nopm") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mnop",s2 = "nopm") == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s1 = "abcd",s2 = "cdab") == True
    assert candidate(s1 = "acbd",s2 = "bdac") == True
    assert candidate(s1 = "abab",s2 = "abcd") == False
    assert candidate(s1 = "abdc",s2 = "cdab") == False
    assert candidate(s1 = "abcd",s2 = "dacb") == False
    assert candidate(s1 = "abab",s2 = "baba") == False
    assert candidate(s1 = "abcd",s2 = "abcd") == True
    assert candidate(s1 = "aabb",s2 = "bbaa") == True
    assert candidate(s1 = "abcd",s2 = "dcba") == False
    assert candidate(s1 = "zzzz",s2 = "zzzz") == True
    assert candidate(s1 = "zabc",s2 = "cbaz") == False
    assert candidate(s1 = "efef",s2 = "fefo") == False
    assert candidate(s1 = "abcd",s2 = "dcab") == False
    assert candidate(s1 = "abcd",s2 = "dbca") == False
    assert candidate(s1 = "qrst",s2 = "tqsr") == False
    assert candidate(s1 = "mnop",s2 = "ponq") == False
    assert candidate(s1 = "ijkl",s2 = "lkji") == False
    assert candidate(s1 = "abcd",s2 = "cabd") == False
    assert candidate(s1 = "wxxy",s2 = "yxwx") == False
    assert candidate(s1 = "abcd",s2 = "abdc") == False
    assert candidate(s1 = "qrst",s2 = "tsqr") == False
    assert candidate(s1 = "abba",s2 = "baab") == True
    assert candidate(s1 = "abcd",s2 = "cadb") == False
    assert candidate(s1 = "abcd",s2 = "cdac") == False
    assert candidate(s1 = "wxyz",s2 = "yxwz") == True
    assert candidate(s1 = "abac",s2 = "cabd") == False
    assert candidate(s1 = "mnop",s2 = "npom") == False
    assert candidate(s1 = "ijkl",s2 = "lkij") == False
    assert candidate(s1 = "efgh",s2 = "fegh") == False
    assert candidate(s1 = "pqrs",s2 = "rqps") == True
    assert candidate(s1 = "uvwx",s2 = "xwvu") == False
    assert candidate(s1 = "wxyz",s2 = "xywz") == False
    assert candidate(s1 = "xyxy",s2 = "yxyx") == False
    assert candidate(s1 = "efgh",s2 = "hgfq") == False
    assert candidate(s1 = "abcd",s2 = "dbac") == False
    assert candidate(s1 = "aabb",s2 = "abab") == False
    assert candidate(s1 = "mnop",s2 = "ponm") == False
    assert candidate(s1 = "abcd",s2 = "bdca") == False
    assert candidate(s1 = "qrst",s2 = "tsrf") == False
    assert candidate(s1 = "qrst",s2 = "tsrq") == False
    assert candidate(s1 = "abcd",s2 = "badc") == False
    assert candidate(s1 = "qrst",s2 = "tqrs") == False
    assert candidate(s1 = "abcd",s2 = "adcb") == True
    assert candidate(s1 = "mnop",s2 = "pmno") == False
    assert candidate(s1 = "abba",s2 = "baba") == False
    assert candidate(s1 = "abcd",s2 = "bacd") == False
    assert candidate(s1 = "abca",s2 = "acba") == False
    assert candidate(s1 = "abcd",s2 = "bdac") == False
    assert candidate(s1 = "mnop",s2 = "onmp") == True
    assert candidate(s1 = "lwxy",s2 = "xylw") == True
    assert candidate(s1 = "zzza",s2 = "zzaa") == False
    assert candidate(s1 = "abcd",s2 = "acdb") == False
    assert candidate(s1 = "zzzz",s2 = "zzaz") == False
    assert candidate(s1 = "aabb",s2 = "abba") == True
    assert candidate(s1 = "abcd",s2 = "acbd") == False
    assert candidate(s1 = "wxyz",s2 = "xyzw") == False
    assert candidate(s1 = "xxyz",s2 = "zyxz") == False
    assert candidate(s1 = "abcd",s2 = "dabc") == False
    assert candidate(s1 = "pqrs",s2 = "rspq") == True
    assert candidate(s1 = "zyxw",s2 = "xwyz") == False
    assert candidate(s1 = "abcd",s2 = "abca") == False
    assert candidate(s1 = "abca",s2 = "cabd") == False
    assert candidate(s1 = "mnop",s2 = "nopm") == False


