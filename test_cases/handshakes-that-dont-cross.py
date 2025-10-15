def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(numPeople = 18) == 4862
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 18) == 4862: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 16) == 1430
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 16) == 1430: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 8) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 8) == 14: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 12) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 12) == 132: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 20) == 16796
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 20) == 16796: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 10) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 10) == 42: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 14) == 429
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 14) == 429: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 900) == 876537848
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 900) == 876537848: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 128) == 887145589
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 128) == 887145589: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 256) == 707292517
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 256) == 707292517: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 600) == 718512182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 600) == 718512182: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 32) == 35357670
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 32) == 35357670: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 800) == 497153305
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 800) == 497153305: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 64) == 488309750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 64) == 488309750: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 60) == 475387402
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 60) == 475387402: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 50) == 946367425
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 50) == 946367425: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 40) == 564120378
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 40) == 564120378: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 70) == 93302951
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 70) == 93302951: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 80) == 602941373
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 80) == 602941373: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 512) == 962620544
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 512) == 962620544: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 768) == 696991831
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 768) == 696991831: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 90) == 205311759
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 90) == 205311759: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 450) == 113566864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 450) == 113566864: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 100) == 265470434
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 100) == 265470434: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 30) == 9694845
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 30) == 9694845: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 750) == 309104184
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 750) == 309104184: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 22) == 58786
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 22) == 58786: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 26) == 742900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 26) == 742900: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 24) == 208012
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 24) == 208012: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 400) == 868596491
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 400) == 868596491: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 700) == 834169133
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 700) == 834169133: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 500) == 217193473
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 500) == 217193473: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 300) == 516266904
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 300) == 516266904: {e}')
    
    total += 1
    try:
        result = candidate(numPeople = 200) == 558488487
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numPeople = 200) == 558488487: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(numPeople = 18) == 4862
    assert candidate(numPeople = 16) == 1430
    assert candidate(numPeople = 8) == 14
    assert candidate(numPeople = 12) == 132
    assert candidate(numPeople = 20) == 16796
    assert candidate(numPeople = 10) == 42
    assert candidate(numPeople = 4) == 2
    assert candidate(numPeople = 14) == 429
    assert candidate(numPeople = 6) == 5
    assert candidate(numPeople = 900) == 876537848
    assert candidate(numPeople = 128) == 887145589
    assert candidate(numPeople = 256) == 707292517
    assert candidate(numPeople = 600) == 718512182
    assert candidate(numPeople = 32) == 35357670
    assert candidate(numPeople = 800) == 497153305
    assert candidate(numPeople = 64) == 488309750
    assert candidate(numPeople = 2) == 1
    assert candidate(numPeople = 60) == 475387402
    assert candidate(numPeople = 50) == 946367425
    assert candidate(numPeople = 40) == 564120378
    assert candidate(numPeople = 70) == 93302951
    assert candidate(numPeople = 80) == 602941373
    assert candidate(numPeople = 512) == 962620544
    assert candidate(numPeople = 768) == 696991831
    assert candidate(numPeople = 90) == 205311759
    assert candidate(numPeople = 450) == 113566864
    assert candidate(numPeople = 100) == 265470434
    assert candidate(numPeople = 30) == 9694845
    assert candidate(numPeople = 750) == 309104184
    assert candidate(numPeople = 22) == 58786
    assert candidate(numPeople = 26) == 742900
    assert candidate(numPeople = 24) == 208012
    assert candidate(numPeople = 400) == 868596491
    assert candidate(numPeople = 700) == 834169133
    assert candidate(numPeople = 500) == 217193473
    assert candidate(numPeople = 300) == 516266904
    assert candidate(numPeople = 200) == 558488487


