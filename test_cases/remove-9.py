def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 80000000) == "176472328"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80000000) == "176472328": {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == "16"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == "16": {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == "100"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == "100": {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == "10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == "10": {e}')
    
    total += 1
    try:
        result = candidate(n = 88888888) == "205230561"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 88888888) == "205230561": {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == "277266780"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == "277266780": {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == "22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == "22": {e}')
    
    total += 1
    try:
        result = candidate(n = 8000000) == "16042838"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8000000) == "16042838": {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == "121"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == "121": {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == "1331"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == "1331": {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == "11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == "11": {e}')
    
    total += 1
    try:
        result = candidate(n = 800000000) == "2052305618"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800000000) == "2052305618": {e}')
    
    total += 1
    try:
        result = candidate(n = 88) == "107"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 88) == "107": {e}')
    
    total += 1
    try:
        result = candidate(n = 77777777) == "172315042"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 77777777) == "172315042": {e}')
    
    total += 1
    try:
        result = candidate(n = 9999999) == "20731370"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999999) == "20731370": {e}')
    
    total += 1
    try:
        result = candidate(n = 12345) == "17836"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345) == "17836": {e}')
    
    total += 1
    try:
        result = candidate(n = 67890) == "113113"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67890) == "113113": {e}')
    
    total += 1
    try:
        result = candidate(n = 87654321) == "202838110"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 87654321) == "202838110": {e}')
    
    total += 1
    try:
        result = candidate(n = 8888) == "13165"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8888) == "13165": {e}')
    
    total += 1
    try:
        result = candidate(n = 300000) == "506463"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300000) == "506463": {e}')
    
    total += 1
    try:
        result = candidate(n = 50000) == "75525"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000) == "75525": {e}')
    
    total += 1
    try:
        result = candidate(n = 799999999) == "2052305617"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 799999999) == "2052305617": {e}')
    
    total += 1
    try:
        result = candidate(n = 600000) == "1114036"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600000) == "1114036": {e}')
    
    total += 1
    try:
        result = candidate(n = 25000000) == "52033487"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25000000) == "52033487": {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == "5"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == "5": {e}')
    
    total += 1
    try:
        result = candidate(n = 888888) == "1604283"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888) == "1604283": {e}')
    
    total += 1
    try:
        result = candidate(n = 250000) == "420837"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250000) == "420837": {e}')
    
    total += 1
    try:
        result = candidate(n = 750000) == "1362723"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750000) == "1362723": {e}')
    
    total += 1
    try:
        result = candidate(n = 67891011) == "151665856"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67891011) == "151665856": {e}')
    
    total += 1
    try:
        result = candidate(n = 75000000) == "166111583"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75000000) == "166111583": {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == "14641"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == "14641": {e}')
    
    total += 1
    try:
        result = candidate(n = 800000001) == "2052305620"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800000001) == "2052305620": {e}')
    
    total += 1
    try:
        result = candidate(n = 43210987) == "100270287"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 43210987) == "100270287": {e}')
    
    total += 1
    try:
        result = candidate(n = 50000000) == "114067085"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000000) == "114067085": {e}')
    
    total += 1
    try:
        result = candidate(n = 888) == "1186"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888) == "1186": {e}')
    
    total += 1
    try:
        result = candidate(n = 12345678) == "25206070"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345678) == "25206070": {e}')
    
    total += 1
    try:
        result = candidate(n = 8888888) == "17647232"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8888888) == "17647232": {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000) == "20731371"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000) == "20731371": {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == "8"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == "8": {e}')
    
    total += 1
    try:
        result = candidate(n = 98765432) == "225753628"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98765432) == "225753628": {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == "162151"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == "162151": {e}')
    
    total += 1
    try:
        result = candidate(n = 99999999) == "228145180"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999999) == "228145180": {e}')
    
    total += 1
    try:
        result = candidate(n = 7654321) == "15355671"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7654321) == "15355671": {e}')
    
    total += 1
    try:
        result = candidate(n = 456789) == "765533"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 456789) == "765533": {e}')
    
    total += 1
    try:
        result = candidate(n = 88888) == "144834"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 88888) == "144834": {e}')
    
    total += 1
    try:
        result = candidate(n = 499999999) == "1254748044"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 499999999) == "1254748044": {e}')
    
    total += 1
    try:
        result = candidate(n = 500000) == "841775"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000) == "841775": {e}')
    
    total += 1
    try:
        result = candidate(n = 400000000) == "1025602754"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400000000) == "1025602754": {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000) == "1254748045"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000) == "1254748045": {e}')
    
    total += 1
    try:
        result = candidate(n = 11111111) == "22814518"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11111111) == "22814518": {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == "1783661"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == "1783661": {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567) == "2281451"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567) == "2281451": {e}')
    
    total += 1
    try:
        result = candidate(n = 999999) == "1783660"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999) == "1783660": {e}')
    
    total += 1
    try:
        result = candidate(n = 123456) == "207313"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456) == "207313": {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 56789012) == "127764782"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 56789012) == "127764782": {e}')
    
    total += 1
    try:
        result = candidate(n = 79999999) == "176472327"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 79999999) == "176472327": {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000) == "228145181"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000) == "228145181": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 80000000) == "176472328"
    assert candidate(n = 15) == "16"
    assert candidate(n = 81) == "100"
    assert candidate(n = 9) == "10"
    assert candidate(n = 88888888) == "205230561"
    assert candidate(n = 123456789) == "277266780"
    assert candidate(n = 20) == "22"
    assert candidate(n = 8000000) == "16042838"
    assert candidate(n = 100) == "121"
    assert candidate(n = 1000) == "1331"
    assert candidate(n = 10) == "11"
    assert candidate(n = 800000000) == "2052305618"
    assert candidate(n = 88) == "107"
    assert candidate(n = 77777777) == "172315042"
    assert candidate(n = 9999999) == "20731370"
    assert candidate(n = 12345) == "17836"
    assert candidate(n = 67890) == "113113"
    assert candidate(n = 87654321) == "202838110"
    assert candidate(n = 8888) == "13165"
    assert candidate(n = 300000) == "506463"
    assert candidate(n = 50000) == "75525"
    assert candidate(n = 799999999) == "2052305617"
    assert candidate(n = 600000) == "1114036"
    assert candidate(n = 25000000) == "52033487"
    assert candidate(n = 5) == "5"
    assert candidate(n = 888888) == "1604283"
    assert candidate(n = 250000) == "420837"
    assert candidate(n = 750000) == "1362723"
    assert candidate(n = 67891011) == "151665856"
    assert candidate(n = 75000000) == "166111583"
    assert candidate(n = 10000) == "14641"
    assert candidate(n = 800000001) == "2052305620"
    assert candidate(n = 43210987) == "100270287"
    assert candidate(n = 50000000) == "114067085"
    assert candidate(n = 888) == "1186"
    assert candidate(n = 12345678) == "25206070"
    assert candidate(n = 8888888) == "17647232"
    assert candidate(n = 10000000) == "20731371"
    assert candidate(n = 8) == "8"
    assert candidate(n = 98765432) == "225753628"
    assert candidate(n = 100000) == "162151"
    assert candidate(n = 99999999) == "228145180"
    assert candidate(n = 7654321) == "15355671"
    assert candidate(n = 456789) == "765533"
    assert candidate(n = 88888) == "144834"
    assert candidate(n = 499999999) == "1254748044"
    assert candidate(n = 500000) == "841775"
    assert candidate(n = 400000000) == "1025602754"
    assert candidate(n = 500000000) == "1254748045"
    assert candidate(n = 11111111) == "22814518"
    assert candidate(n = 1000000) == "1783661"
    assert candidate(n = 1234567) == "2281451"
    assert candidate(n = 999999) == "1783660"
    assert candidate(n = 123456) == "207313"
    assert candidate(n = 1) == "1"
    assert candidate(n = 56789012) == "127764782"
    assert candidate(n = 79999999) == "176472327"
    assert candidate(n = 100000000) == "228145181"


