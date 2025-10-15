def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(steps = 5,arrLen = 3) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 5,arrLen = 3) == 21: {e}')
    
    total += 1
    try:
        result = candidate(steps = 10,arrLen = 5) == 2187
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 10,arrLen = 5) == 2187: {e}')
    
    total += 1
    try:
        result = candidate(steps = 5,arrLen = 5) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 5,arrLen = 5) == 21: {e}')
    
    total += 1
    try:
        result = candidate(steps = 2,arrLen = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 2,arrLen = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(steps = 3,arrLen = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 3,arrLen = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(steps = 10,arrLen = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 10,arrLen = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(steps = 10,arrLen = 3) == 1682
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 10,arrLen = 3) == 1682: {e}')
    
    total += 1
    try:
        result = candidate(steps = 1,arrLen = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 1,arrLen = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(steps = 4,arrLen = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 4,arrLen = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(steps = 350,arrLen = 150) == 426619980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 350,arrLen = 150) == 426619980: {e}')
    
    total += 1
    try:
        result = candidate(steps = 20,arrLen = 10) == 50852018
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 20,arrLen = 10) == 50852018: {e}')
    
    total += 1
    try:
        result = candidate(steps = 100,arrLen = 1000000) == 345787718
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 100,arrLen = 1000000) == 345787718: {e}')
    
    total += 1
    try:
        result = candidate(steps = 200,arrLen = 10) == 27369014
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 200,arrLen = 10) == 27369014: {e}')
    
    total += 1
    try:
        result = candidate(steps = 300,arrLen = 500) == 337584699
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 300,arrLen = 500) == 337584699: {e}')
    
    total += 1
    try:
        result = candidate(steps = 200,arrLen = 1000) == 404113244
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 200,arrLen = 1000) == 404113244: {e}')
    
    total += 1
    try:
        result = candidate(steps = 250,arrLen = 100000) == 266783101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 250,arrLen = 100000) == 266783101: {e}')
    
    total += 1
    try:
        result = candidate(steps = 250,arrLen = 250) == 266783101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 250,arrLen = 250) == 266783101: {e}')
    
    total += 1
    try:
        result = candidate(steps = 1,arrLen = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 1,arrLen = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(steps = 200,arrLen = 50) == 228436718
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 200,arrLen = 50) == 228436718: {e}')
    
    total += 1
    try:
        result = candidate(steps = 400,arrLen = 150) == 792402924
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 400,arrLen = 150) == 792402924: {e}')
    
    total += 1
    try:
        result = candidate(steps = 100,arrLen = 5) == 361798919
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 100,arrLen = 5) == 361798919: {e}')
    
    total += 1
    try:
        result = candidate(steps = 300,arrLen = 300) == 337584699
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 300,arrLen = 300) == 337584699: {e}')
    
    total += 1
    try:
        result = candidate(steps = 150,arrLen = 100) == 924870032
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 150,arrLen = 100) == 924870032: {e}')
    
    total += 1
    try:
        result = candidate(steps = 300,arrLen = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 300,arrLen = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(steps = 400,arrLen = 10000) == 990505357
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 400,arrLen = 10000) == 990505357: {e}')
    
    total += 1
    try:
        result = candidate(steps = 100,arrLen = 20) == 227326058
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 100,arrLen = 20) == 227326058: {e}')
    
    total += 1
    try:
        result = candidate(steps = 400,arrLen = 500) == 990505357
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 400,arrLen = 500) == 990505357: {e}')
    
    total += 1
    try:
        result = candidate(steps = 400,arrLen = 20) == 378873335
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 400,arrLen = 20) == 378873335: {e}')
    
    total += 1
    try:
        result = candidate(steps = 450,arrLen = 1000) == 679622497
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 450,arrLen = 1000) == 679622497: {e}')
    
    total += 1
    try:
        result = candidate(steps = 100,arrLen = 250) == 345787718
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 100,arrLen = 250) == 345787718: {e}')
    
    total += 1
    try:
        result = candidate(steps = 7,arrLen = 7) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 7,arrLen = 7) == 127: {e}')
    
    total += 1
    try:
        result = candidate(steps = 300,arrLen = 10) == 202608062
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 300,arrLen = 10) == 202608062: {e}')
    
    total += 1
    try:
        result = candidate(steps = 100,arrLen = 500) == 345787718
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 100,arrLen = 500) == 345787718: {e}')
    
    total += 1
    try:
        result = candidate(steps = 250,arrLen = 2) == 771819109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 250,arrLen = 2) == 771819109: {e}')
    
    total += 1
    try:
        result = candidate(steps = 200,arrLen = 300) == 404113244
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 200,arrLen = 300) == 404113244: {e}')
    
    total += 1
    try:
        result = candidate(steps = 450,arrLen = 900) == 679622497
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 450,arrLen = 900) == 679622497: {e}')
    
    total += 1
    try:
        result = candidate(steps = 150,arrLen = 50) == 700273839
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 150,arrLen = 50) == 700273839: {e}')
    
    total += 1
    try:
        result = candidate(steps = 400,arrLen = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 400,arrLen = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(steps = 50,arrLen = 5) == 316310597
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 50,arrLen = 5) == 316310597: {e}')
    
    total += 1
    try:
        result = candidate(steps = 200,arrLen = 5) == 143744346
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 200,arrLen = 5) == 143744346: {e}')
    
    total += 1
    try:
        result = candidate(steps = 30,arrLen = 5) == 559846999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 30,arrLen = 5) == 559846999: {e}')
    
    total += 1
    try:
        result = candidate(steps = 300,arrLen = 1000) == 337584699
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 300,arrLen = 1000) == 337584699: {e}')
    
    total += 1
    try:
        result = candidate(steps = 150,arrLen = 200) == 924870032
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 150,arrLen = 200) == 924870032: {e}')
    
    total += 1
    try:
        result = candidate(steps = 20,arrLen = 5) == 44991659
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 20,arrLen = 5) == 44991659: {e}')
    
    total += 1
    try:
        result = candidate(steps = 100,arrLen = 1000) == 345787718
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 100,arrLen = 1000) == 345787718: {e}')
    
    total += 1
    try:
        result = candidate(steps = 300,arrLen = 100) == 266213554
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 300,arrLen = 100) == 266213554: {e}')
    
    total += 1
    try:
        result = candidate(steps = 350,arrLen = 350) == 47176184
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 350,arrLen = 350) == 47176184: {e}')
    
    total += 1
    try:
        result = candidate(steps = 125,arrLen = 75) == 534594928
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 125,arrLen = 75) == 534594928: {e}')
    
    total += 1
    try:
        result = candidate(steps = 150,arrLen = 10) == 809029961
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 150,arrLen = 10) == 809029961: {e}')
    
    total += 1
    try:
        result = candidate(steps = 450,arrLen = 250) == 679622497
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 450,arrLen = 250) == 679622497: {e}')
    
    total += 1
    try:
        result = candidate(steps = 250,arrLen = 1000) == 266783101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 250,arrLen = 1000) == 266783101: {e}')
    
    total += 1
    try:
        result = candidate(steps = 150,arrLen = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 150,arrLen = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(steps = 400,arrLen = 200) == 990505356
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 400,arrLen = 200) == 990505356: {e}')
    
    total += 1
    try:
        result = candidate(steps = 120,arrLen = 300) == 991528385
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 120,arrLen = 300) == 991528385: {e}')
    
    total += 1
    try:
        result = candidate(steps = 200,arrLen = 500000) == 404113244
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 200,arrLen = 500000) == 404113244: {e}')
    
    total += 1
    try:
        result = candidate(steps = 450,arrLen = 500) == 679622497
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 450,arrLen = 500) == 679622497: {e}')
    
    total += 1
    try:
        result = candidate(steps = 180,arrLen = 10) == 513914322
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 180,arrLen = 10) == 513914322: {e}')
    
    total += 1
    try:
        result = candidate(steps = 3,arrLen = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 3,arrLen = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(steps = 100,arrLen = 10) == 836991026
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 100,arrLen = 10) == 836991026: {e}')
    
    total += 1
    try:
        result = candidate(steps = 250,arrLen = 100) == 694490842
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 250,arrLen = 100) == 694490842: {e}')
    
    total += 1
    try:
        result = candidate(steps = 250,arrLen = 5000) == 266783101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 250,arrLen = 5000) == 266783101: {e}')
    
    total += 1
    try:
        result = candidate(steps = 250,arrLen = 10) == 321394621
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 250,arrLen = 10) == 321394621: {e}')
    
    total += 1
    try:
        result = candidate(steps = 50,arrLen = 10) == 48059843
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 50,arrLen = 10) == 48059843: {e}')
    
    total += 1
    try:
        result = candidate(steps = 250,arrLen = 50) == 739582172
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 250,arrLen = 50) == 739582172: {e}')
    
    total += 1
    try:
        result = candidate(steps = 400,arrLen = 2) == 99483769
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(steps = 400,arrLen = 2) == 99483769: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(steps = 5,arrLen = 3) == 21
    assert candidate(steps = 10,arrLen = 5) == 2187
    assert candidate(steps = 5,arrLen = 5) == 21
    assert candidate(steps = 2,arrLen = 4) == 2
    assert candidate(steps = 3,arrLen = 2) == 4
    assert candidate(steps = 10,arrLen = 1) == 1
    assert candidate(steps = 10,arrLen = 3) == 1682
    assert candidate(steps = 1,arrLen = 3) == 1
    assert candidate(steps = 4,arrLen = 2) == 8
    assert candidate(steps = 350,arrLen = 150) == 426619980
    assert candidate(steps = 20,arrLen = 10) == 50852018
    assert candidate(steps = 100,arrLen = 1000000) == 345787718
    assert candidate(steps = 200,arrLen = 10) == 27369014
    assert candidate(steps = 300,arrLen = 500) == 337584699
    assert candidate(steps = 200,arrLen = 1000) == 404113244
    assert candidate(steps = 250,arrLen = 100000) == 266783101
    assert candidate(steps = 250,arrLen = 250) == 266783101
    assert candidate(steps = 1,arrLen = 5) == 1
    assert candidate(steps = 200,arrLen = 50) == 228436718
    assert candidate(steps = 400,arrLen = 150) == 792402924
    assert candidate(steps = 100,arrLen = 5) == 361798919
    assert candidate(steps = 300,arrLen = 300) == 337584699
    assert candidate(steps = 150,arrLen = 100) == 924870032
    assert candidate(steps = 300,arrLen = 1) == 1
    assert candidate(steps = 400,arrLen = 10000) == 990505357
    assert candidate(steps = 100,arrLen = 20) == 227326058
    assert candidate(steps = 400,arrLen = 500) == 990505357
    assert candidate(steps = 400,arrLen = 20) == 378873335
    assert candidate(steps = 450,arrLen = 1000) == 679622497
    assert candidate(steps = 100,arrLen = 250) == 345787718
    assert candidate(steps = 7,arrLen = 7) == 127
    assert candidate(steps = 300,arrLen = 10) == 202608062
    assert candidate(steps = 100,arrLen = 500) == 345787718
    assert candidate(steps = 250,arrLen = 2) == 771819109
    assert candidate(steps = 200,arrLen = 300) == 404113244
    assert candidate(steps = 450,arrLen = 900) == 679622497
    assert candidate(steps = 150,arrLen = 50) == 700273839
    assert candidate(steps = 400,arrLen = 1) == 1
    assert candidate(steps = 50,arrLen = 5) == 316310597
    assert candidate(steps = 200,arrLen = 5) == 143744346
    assert candidate(steps = 30,arrLen = 5) == 559846999
    assert candidate(steps = 300,arrLen = 1000) == 337584699
    assert candidate(steps = 150,arrLen = 200) == 924870032
    assert candidate(steps = 20,arrLen = 5) == 44991659
    assert candidate(steps = 100,arrLen = 1000) == 345787718
    assert candidate(steps = 300,arrLen = 100) == 266213554
    assert candidate(steps = 350,arrLen = 350) == 47176184
    assert candidate(steps = 125,arrLen = 75) == 534594928
    assert candidate(steps = 150,arrLen = 10) == 809029961
    assert candidate(steps = 450,arrLen = 250) == 679622497
    assert candidate(steps = 250,arrLen = 1000) == 266783101
    assert candidate(steps = 150,arrLen = 1) == 1
    assert candidate(steps = 400,arrLen = 200) == 990505356
    assert candidate(steps = 120,arrLen = 300) == 991528385
    assert candidate(steps = 200,arrLen = 500000) == 404113244
    assert candidate(steps = 450,arrLen = 500) == 679622497
    assert candidate(steps = 180,arrLen = 10) == 513914322
    assert candidate(steps = 3,arrLen = 10) == 4
    assert candidate(steps = 100,arrLen = 10) == 836991026
    assert candidate(steps = 250,arrLen = 100) == 694490842
    assert candidate(steps = 250,arrLen = 5000) == 266783101
    assert candidate(steps = 250,arrLen = 10) == 321394621
    assert candidate(steps = 50,arrLen = 10) == 48059843
    assert candidate(steps = 250,arrLen = 50) == 739582172
    assert candidate(steps = 400,arrLen = 2) == 99483769


