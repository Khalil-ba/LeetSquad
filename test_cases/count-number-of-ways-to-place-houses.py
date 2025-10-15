def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 20522904
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 20522904: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 402613600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 402613600: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 500478595
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 500478595: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 20736
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 20736: {e}')
    
    total += 1
    try:
        result = candidate(n = 4000) == 984988507
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4000) == 984988507: {e}')
    
    total += 1
    try:
        result = candidate(n = 7000) == 750848153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7000) == 750848153: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000) == 329423452
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000) == 329423452: {e}')
    
    total += 1
    try:
        result = candidate(n = 7500) == 39764836
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7500) == 39764836: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 245481867
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 245481867: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 169
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 169: {e}')
    
    total += 1
    try:
        result = candidate(n = 3000) == 511358621
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3000) == 511358621: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 30066266
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 30066266: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 64: {e}')
    
    total += 1
    try:
        result = candidate(n = 1001) == 307206160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1001) == 307206160: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 3025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 3025: {e}')
    
    total += 1
    try:
        result = candidate(n = 250) == 172820552
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250) == 172820552: {e}')
    
    total += 1
    try:
        result = candidate(n = 8000) == 823868594
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8000) == 823868594: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 851109891
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 851109891: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999) == 459963766
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999) == 459963766: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 313679521
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 313679521: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 2550409
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 2550409: {e}')
    
    total += 1
    try:
        result = candidate(n = 2500) == 968650195
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2500) == 968650195: {e}')
    
    total += 1
    try:
        result = candidate(n = 9000) == 641644802
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9000) == 641644802: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 450435314
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 450435314: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 7921
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 7921: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 441
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 441: {e}')
    
    total += 1
    try:
        result = candidate(n = 6000) == 337759600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6000) == 337759600: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 164765197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 164765197: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 1156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 1156: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 580030458
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 580030458: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 25
    assert candidate(n = 100) == 20522904
    assert candidate(n = 10000) == 402613600
    assert candidate(n = 2) == 9
    assert candidate(n = 1) == 4
    assert candidate(n = 1000) == 500478595
    assert candidate(n = 10) == 20736
    assert candidate(n = 4000) == 984988507
    assert candidate(n = 7000) == 750848153
    assert candidate(n = 2000) == 329423452
    assert candidate(n = 7500) == 39764836
    assert candidate(n = 50) == 245481867
    assert candidate(n = 5) == 169
    assert candidate(n = 3000) == 511358621
    assert candidate(n = 30) == 30066266
    assert candidate(n = 4) == 64
    assert candidate(n = 1001) == 307206160
    assert candidate(n = 8) == 3025
    assert candidate(n = 250) == 172820552
    assert candidate(n = 8000) == 823868594
    assert candidate(n = 5000) == 851109891
    assert candidate(n = 9999) == 459963766
    assert candidate(n = 20) == 313679521
    assert candidate(n = 15) == 2550409
    assert candidate(n = 2500) == 968650195
    assert candidate(n = 9000) == 641644802
    assert candidate(n = 200) == 450435314
    assert candidate(n = 9) == 7921
    assert candidate(n = 6) == 441
    assert candidate(n = 6000) == 337759600
    assert candidate(n = 500) == 164765197
    assert candidate(n = 7) == 1156
    assert candidate(n = 25) == 580030458


