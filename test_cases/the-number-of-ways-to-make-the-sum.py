def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == 250024994
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 250024994: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 1276
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 1276: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 121: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 12502501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 12502501: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 56: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 125251
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 125251: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 326
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 326: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999) == 249974994
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999) == 249974994: {e}')
    
    total += 1
    try:
        result = candidate(n = 45) == 254
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45) == 254: {e}')
    
    total += 1
    try:
        result = candidate(n = 105) == 1379
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 105) == 1379: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == 301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == 301: {e}')
    
    total += 1
    try:
        result = candidate(n = 125) == 1954
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125) == 1954: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 7500) == 7033126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7500) == 7033126: {e}')
    
    total += 1
    try:
        result = candidate(n = 90000) == 12522494
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90000) == 12522494: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000) == 312512501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000) == 312512501: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 11326
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 11326: {e}')
    
    total += 1
    try:
        result = candidate(n = 123) == 1892
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123) == 1892: {e}')
    
    total += 1
    try:
        result = candidate(n = 60) == 466
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60) == 466: {e}')
    
    total += 1
    try:
        result = candidate(n = 60000) == 450015001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60000) == 450015001: {e}')
    
    total += 1
    try:
        result = candidate(n = 600) == 45151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600) == 45151: {e}')
    
    total += 1
    try:
        result = candidate(n = 30000) == 112507501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30000) == 112507501: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == 1226
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == 1226: {e}')
    
    total += 1
    try:
        result = candidate(n = 501) == 31376
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 501) == 31376: {e}')
    
    total += 1
    try:
        result = candidate(n = 80) == 821
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80) == 821: {e}')
    
    total += 1
    try:
        result = candidate(n = 51) == 326
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 51) == 326: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 250) == 7876
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250) == 7876: {e}')
    
    total += 1
    try:
        result = candidate(n = 20000) == 50005001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20000) == 50005001: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 124751
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 124751: {e}')
    
    total += 1
    try:
        result = candidate(n = 79) == 781
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 79) == 781: {e}')
    
    total += 1
    try:
        result = candidate(n = 35) == 154
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35) == 154: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 3126251
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 3126251: {e}')
    
    total += 1
    try:
        result = candidate(n = 75) == 704
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75) == 704: {e}')
    
    total += 1
    try:
        result = candidate(n = 40000) == 200010001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40000) == 200010001: {e}')
    
    total += 1
    try:
        result = candidate(n = 77) == 742
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 77) == 742: {e}')
    
    total += 1
    try:
        result = candidate(n = 150) == 2851
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150) == 2851: {e}')
    
    total += 1
    try:
        result = candidate(n = 800) == 80201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800) == 80201: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 5051
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 5051: {e}')
    
    total += 1
    try:
        result = candidate(n = 400) == 20101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400) == 20101: {e}')
    
    total += 1
    try:
        result = candidate(n = 750) == 70501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750) == 70501: {e}')
    
    total += 1
    try:
        result = candidate(n = 120) == 1831
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120) == 1831: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 31376
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 31376: {e}')
    
    total += 1
    try:
        result = candidate(n = 55) == 379
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55) == 379: {e}')
    
    total += 1
    try:
        result = candidate(n = 70000) == 612517501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 70000) == 612517501: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 79: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 2
    assert candidate(n = 100000) == 250024994
    assert candidate(n = 100) == 1276
    assert candidate(n = 30) == 121
    assert candidate(n = 4) == 4
    assert candidate(n = 12) == 22
    assert candidate(n = 10000) == 12502501
    assert candidate(n = 6) == 7
    assert candidate(n = 20) == 56
    assert candidate(n = 2) == 2
    assert candidate(n = 1) == 1
    assert candidate(n = 1000) == 125251
    assert candidate(n = 10) == 16
    assert candidate(n = 5) == 4
    assert candidate(n = 50) == 326
    assert candidate(n = 99999) == 249974994
    assert candidate(n = 45) == 254
    assert candidate(n = 105) == 1379
    assert candidate(n = 49) == 301
    assert candidate(n = 125) == 1954
    assert candidate(n = 7) == 7
    assert candidate(n = 7500) == 7033126
    assert candidate(n = 90000) == 12522494
    assert candidate(n = 50000) == 312512501
    assert candidate(n = 300) == 11326
    assert candidate(n = 123) == 1892
    assert candidate(n = 60) == 466
    assert candidate(n = 60000) == 450015001
    assert candidate(n = 600) == 45151
    assert candidate(n = 30000) == 112507501
    assert candidate(n = 99) == 1226
    assert candidate(n = 501) == 31376
    assert candidate(n = 80) == 821
    assert candidate(n = 51) == 326
    assert candidate(n = 8) == 11
    assert candidate(n = 250) == 7876
    assert candidate(n = 20000) == 50005001
    assert candidate(n = 999) == 124751
    assert candidate(n = 79) == 781
    assert candidate(n = 35) == 154
    assert candidate(n = 5000) == 3126251
    assert candidate(n = 75) == 704
    assert candidate(n = 40000) == 200010001
    assert candidate(n = 77) == 742
    assert candidate(n = 150) == 2851
    assert candidate(n = 800) == 80201
    assert candidate(n = 11) == 16
    assert candidate(n = 15) == 29
    assert candidate(n = 200) == 5051
    assert candidate(n = 400) == 20101
    assert candidate(n = 750) == 70501
    assert candidate(n = 120) == 1831
    assert candidate(n = 500) == 31376
    assert candidate(n = 55) == 379
    assert candidate(n = 70000) == 612517501
    assert candidate(n = 25) == 79


