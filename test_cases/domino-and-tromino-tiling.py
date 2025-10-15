def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 190242381
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 190242381: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 11: {e}')
    
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
        result = candidate(n = 500) == 603582422
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 603582422: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 979232805
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 979232805: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 1255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 1255: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 6105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 6105: {e}')
    
    total += 1
    try:
        result = candidate(n = 125) == 562894970
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125) == 562894970: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 451995198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 451995198: {e}')
    
    total += 1
    try:
        result = candidate(n = 650) == 5517492
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 650) == 5517492: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 768506587
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 768506587: {e}')
    
    total += 1
    try:
        result = candidate(n = 123) == 215563687
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123) == 215563687: {e}')
    
    total += 1
    try:
        result = candidate(n = 550) == 727269359
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 550) == 727269359: {e}')
    
    total += 1
    try:
        result = candidate(n = 600) == 771568221
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600) == 771568221: {e}')
    
    total += 1
    try:
        result = candidate(n = 450) == 795340037
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450) == 795340037: {e}')
    
    total += 1
    try:
        result = candidate(n = 501) == 210280741
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 501) == 210280741: {e}')
    
    total += 1
    try:
        result = candidate(n = 700) == 637136622
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700) == 637136622: {e}')
    
    total += 1
    try:
        result = candidate(n = 250) == 872044590
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250) == 872044590: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 326038248
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 326038248: {e}')
    
    total += 1
    try:
        result = candidate(n = 89) == 469785861
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 89) == 469785861: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 3418626
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 3418626: {e}')
    
    total += 1
    try:
        result = candidate(n = 150) == 773955023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150) == 773955023: {e}')
    
    total += 1
    try:
        result = candidate(n = 800) == 177362789
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800) == 177362789: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 627399438
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 627399438: {e}')
    
    total += 1
    try:
        result = candidate(n = 400) == 517656200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400) == 517656200: {e}')
    
    total += 1
    try:
        result = candidate(n = 750) == 533845494
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750) == 533845494: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 53: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 5
    assert candidate(n = 100) == 190242381
    assert candidate(n = 4) == 11
    assert candidate(n = 2) == 2
    assert candidate(n = 1) == 1
    assert candidate(n = 500) == 603582422
    assert candidate(n = 1000) == 979232805
    assert candidate(n = 10) == 1255
    assert candidate(n = 5) == 24
    assert candidate(n = 12) == 6105
    assert candidate(n = 125) == 562894970
    assert candidate(n = 50) == 451995198
    assert candidate(n = 650) == 5517492
    assert candidate(n = 300) == 768506587
    assert candidate(n = 123) == 215563687
    assert candidate(n = 550) == 727269359
    assert candidate(n = 600) == 771568221
    assert candidate(n = 450) == 795340037
    assert candidate(n = 501) == 210280741
    assert candidate(n = 700) == 637136622
    assert candidate(n = 250) == 872044590
    assert candidate(n = 999) == 326038248
    assert candidate(n = 89) == 469785861
    assert candidate(n = 20) == 3418626
    assert candidate(n = 150) == 773955023
    assert candidate(n = 800) == 177362789
    assert candidate(n = 200) == 627399438
    assert candidate(n = 400) == 517656200
    assert candidate(n = 750) == 533845494
    assert candidate(n = 6) == 53


