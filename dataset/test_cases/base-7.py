def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = -1000000) == "-11333311"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -1000000) == "-11333311": {e}')
    
    total += 1
    try:
        result = candidate(num = 49) == "100"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 49) == "100": {e}')
    
    total += 1
    try:
        result = candidate(num = 165) == "324"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 165) == "324": {e}')
    
    total += 1
    try:
        result = candidate(num = -10000000) == "-150666343"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -10000000) == "-150666343": {e}')
    
    total += 1
    try:
        result = candidate(num = 0) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 0) == "0": {e}')
    
    total += 1
    try:
        result = candidate(num = 10000000) == "150666343"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10000000) == "150666343": {e}')
    
    total += 1
    try:
        result = candidate(num = 16807) == "100000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 16807) == "100000": {e}')
    
    total += 1
    try:
        result = candidate(num = 100) == "202"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100) == "202": {e}')
    
    total += 1
    try:
        result = candidate(num = -7) == "-10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -7) == "-10": {e}')
    
    total += 1
    try:
        result = candidate(num = 16) == "22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 16) == "22": {e}')
    
    total += 1
    try:
        result = candidate(num = 500000) == "4151504"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 500000) == "4151504": {e}')
    
    total += 1
    try:
        result = candidate(num = -40353607) == "-1000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -40353607) == "-1000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 1234567) == "13331215"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234567) == "13331215": {e}')
    
    total += 1
    try:
        result = candidate(num = -9999999) == "-150666342"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -9999999) == "-150666342": {e}')
    
    total += 1
    try:
        result = candidate(num = -4826464) == "-56011216"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -4826464) == "-56011216": {e}')
    
    total += 1
    try:
        result = candidate(num = -9876543) == "-146643405"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -9876543) == "-146643405": {e}')
    
    total += 1
    try:
        result = candidate(num = 823543) == "10000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 823543) == "10000000": {e}')
    
    total += 1
    try:
        result = candidate(num = -5764801) == "-100000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -5764801) == "-100000000": {e}')
    
    total += 1
    try:
        result = candidate(num = -987654) == "-11252313"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -987654) == "-11252313": {e}')
    
    total += 1
    try:
        result = candidate(num = -500000) == "-4151504"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -500000) == "-4151504": {e}')
    
    total += 1
    try:
        result = candidate(num = -1) == "-1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -1) == "-1": {e}')
    
    total += 1
    try:
        result = candidate(num = 117649) == "1000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 117649) == "1000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 40353607) == "1000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 40353607) == "1000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = -2401) == "-10000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -2401) == "-10000": {e}')
    
    total += 1
    try:
        result = candidate(num = 5764801) == "100000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5764801) == "100000000": {e}')
    
    total += 1
    try:
        result = candidate(num = -117649) == "-1000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -117649) == "-1000000": {e}')
    
    total += 1
    try:
        result = candidate(num = -16807) == "-100000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -16807) == "-100000": {e}')
    
    total += 1
    try:
        result = candidate(num = -1234567) == "-13331215"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -1234567) == "-13331215": {e}')
    
    total += 1
    try:
        result = candidate(num = -343) == "-1000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -343) == "-1000": {e}')
    
    total += 1
    try:
        result = candidate(num = 2401) == "10000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2401) == "10000": {e}')
    
    total += 1
    try:
        result = candidate(num = 1049600) == "11631026"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1049600) == "11631026": {e}')
    
    total += 1
    try:
        result = candidate(num = 7) == "10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 7) == "10": {e}')
    
    total += 1
    try:
        result = candidate(num = -823543) == "-10000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -823543) == "-10000000": {e}')
    
    total += 1
    try:
        result = candidate(num = 9999999) == "150666342"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9999999) == "150666342": {e}')
    
    total += 1
    try:
        result = candidate(num = 1) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1) == "1": {e}')
    
    total += 1
    try:
        result = candidate(num = 6827346) == "112013541"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 6827346) == "112013541": {e}')
    
    total += 1
    try:
        result = candidate(num = 343) == "1000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 343) == "1000": {e}')
    
    total += 1
    try:
        result = candidate(num = 9876543) == "146643405"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9876543) == "146643405": {e}')
    
    total += 1
    try:
        result = candidate(num = -282475249) == "-10000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -282475249) == "-10000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = -49) == "-100"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -49) == "-100": {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000) == "11333311"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000) == "11333311": {e}')
    
    total += 1
    try:
        result = candidate(num = 4826464) == "56011216"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4826464) == "56011216": {e}')
    
    total += 1
    try:
        result = candidate(num = 282475249) == "10000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 282475249) == "10000000000": {e}')
    
    total += 1
    try:
        result = candidate(num = -64) == "-121"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -64) == "-121": {e}')
    
    total += 1
    try:
        result = candidate(num = 64) == "121"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 64) == "121": {e}')
    
    total += 1
    try:
        result = candidate(num = 117648) == "666666"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 117648) == "666666": {e}')
    
    total += 1
    try:
        result = candidate(num = -6827346) == "-112013541"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -6827346) == "-112013541": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = -1000000) == "-11333311"
    assert candidate(num = 49) == "100"
    assert candidate(num = 165) == "324"
    assert candidate(num = -10000000) == "-150666343"
    assert candidate(num = 0) == "0"
    assert candidate(num = 10000000) == "150666343"
    assert candidate(num = 16807) == "100000"
    assert candidate(num = 100) == "202"
    assert candidate(num = -7) == "-10"
    assert candidate(num = 16) == "22"
    assert candidate(num = 500000) == "4151504"
    assert candidate(num = -40353607) == "-1000000000"
    assert candidate(num = 1234567) == "13331215"
    assert candidate(num = -9999999) == "-150666342"
    assert candidate(num = -4826464) == "-56011216"
    assert candidate(num = -9876543) == "-146643405"
    assert candidate(num = 823543) == "10000000"
    assert candidate(num = -5764801) == "-100000000"
    assert candidate(num = -987654) == "-11252313"
    assert candidate(num = -500000) == "-4151504"
    assert candidate(num = -1) == "-1"
    assert candidate(num = 117649) == "1000000"
    assert candidate(num = 40353607) == "1000000000"
    assert candidate(num = -2401) == "-10000"
    assert candidate(num = 5764801) == "100000000"
    assert candidate(num = -117649) == "-1000000"
    assert candidate(num = -16807) == "-100000"
    assert candidate(num = -1234567) == "-13331215"
    assert candidate(num = -343) == "-1000"
    assert candidate(num = 2401) == "10000"
    assert candidate(num = 1049600) == "11631026"
    assert candidate(num = 7) == "10"
    assert candidate(num = -823543) == "-10000000"
    assert candidate(num = 9999999) == "150666342"
    assert candidate(num = 1) == "1"
    assert candidate(num = 6827346) == "112013541"
    assert candidate(num = 343) == "1000"
    assert candidate(num = 9876543) == "146643405"
    assert candidate(num = -282475249) == "-10000000000"
    assert candidate(num = -49) == "-100"
    assert candidate(num = 1000000) == "11333311"
    assert candidate(num = 4826464) == "56011216"
    assert candidate(num = 282475249) == "10000000000"
    assert candidate(num = -64) == "-121"
    assert candidate(num = 64) == "121"
    assert candidate(num = 117648) == "666666"
    assert candidate(num = -6827346) == "-112013541"


