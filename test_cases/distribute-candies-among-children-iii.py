def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 10,limit = 5) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,limit = 5) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,limit = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,limit = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,limit = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,limit = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,limit = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,limit = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,limit = 10) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,limit = 10) == 66: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,limit = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,limit = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,limit = 50) == 1326
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,limit = 50) == 1326: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,limit = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,limit = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,limit = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,limit = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000,limit = 100000000) == 5000000150000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000,limit = 100000000) == 5000000150000001: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,limit = 250) == 31626
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,limit = 250) == 31626: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,limit = 300) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,limit = 300) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,limit = 150) == 11476
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,limit = 150) == 11476: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,limit = 25) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,limit = 25) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 200000,limit = 10000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200000,limit = 10000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,limit = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,limit = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,limit = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,limit = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000000,limit = 10000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000000,limit = 10000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,limit = 100) == 1326
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,limit = 100) == 1326: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,limit = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,limit = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 90,limit = 35) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90,limit = 35) == 136: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,limit = 200) == 20301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,limit = 200) == 20301: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,limit = 50000) == 1250075001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,limit = 50000) == 1250075001: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,limit = 30) == 496
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,limit = 30) == 496: {e}')
    
    total += 1
    try:
        result = candidate(n = 75000000,limit = 25000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75000000,limit = 25000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,limit = 50) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,limit = 50) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,limit = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,limit = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,limit = 20) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,limit = 20) == 66: {e}')
    
    total += 1
    try:
        result = candidate(n = 60,limit = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60,limit = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,limit = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,limit = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,limit = 150) == 16476
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,limit = 150) == 16476: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,limit = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,limit = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,limit = 200) == 27801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,limit = 200) == 27801: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,limit = 200) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,limit = 200) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,limit = 10) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,limit = 10) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000,limit = 100000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000,limit = 100000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,limit = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,limit = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,limit = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,limit = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 90,limit = 90) == 4186
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90,limit = 90) == 4186: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,limit = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,limit = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,limit = 500) == 125751
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,limit = 500) == 125751: {e}')
    
    total += 1
    try:
        result = candidate(n = 99,limit = 99) == 5050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99,limit = 99) == 5050: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,limit = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,limit = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,limit = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,limit = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,limit = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,limit = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 125,limit = 100) == 7026
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125,limit = 100) == 7026: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,limit = 333) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,limit = 333) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 80,limit = 40) == 861
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80,limit = 40) == 861: {e}')
    
    total += 1
    try:
        result = candidate(n = 120,limit = 60) == 1891
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120,limit = 60) == 1891: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,limit = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,limit = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,limit = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,limit = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,limit = 25) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,limit = 25) == 351: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000,limit = 50000000) == 1250000075000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000,limit = 50000000) == 1250000075000001: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,limit = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,limit = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,limit = 500000) == 125000750001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,limit = 500000) == 125000750001: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,limit = 15) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,limit = 15) == 136: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,limit = 5000) == 12507501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,limit = 5000) == 12507501: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,limit = 40) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,limit = 40) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 99,limit = 33) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99,limit = 33) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,limit = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,limit = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,limit = 30000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,limit = 30000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,limit = 2500) == 3128751
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,limit = 2500) == 3128751: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999999,limit = 33333333) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999999,limit = 33333333) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,limit = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,limit = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,limit = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,limit = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,limit = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,limit = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 60,limit = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60,limit = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,limit = 75) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,limit = 75) == 351: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,limit = 30) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,limit = 30) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 175,limit = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 175,limit = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,limit = 100) == 5151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,limit = 100) == 5151: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,limit = 9) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,limit = 9) == 55: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000,limit = 5000000) == 12500007500001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000,limit = 5000000) == 12500007500001: {e}')
    
    total += 1
    try:
        result = candidate(n = 80,limit = 30) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80,limit = 30) == 66: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 10,limit = 5) == 21
    assert candidate(n = 3,limit = 3) == 10
    assert candidate(n = 5,limit = 2) == 3
    assert candidate(n = 7,limit = 3) == 6
    assert candidate(n = 20,limit = 10) == 66
    assert candidate(n = 1,limit = 1) == 3
    assert candidate(n = 100,limit = 50) == 1326
    assert candidate(n = 15,limit = 5) == 1
    assert candidate(n = 10,limit = 1) == 0
    assert candidate(n = 100000000,limit = 100000000) == 5000000150000001
    assert candidate(n = 500,limit = 250) == 31626
    assert candidate(n = 1000,limit = 300) == 0
    assert candidate(n = 150,limit = 150) == 11476
    assert candidate(n = 75,limit = 25) == 1
    assert candidate(n = 200000,limit = 10000) == 0
    assert candidate(n = 100,limit = 5) == 0
    assert candidate(n = 25,limit = 7) == 0
    assert candidate(n = 50000000,limit = 10000000) == 0
    assert candidate(n = 50,limit = 100) == 1326
    assert candidate(n = 100,limit = 1) == 0
    assert candidate(n = 90,limit = 35) == 136
    assert candidate(n = 200,limit = 200) == 20301
    assert candidate(n = 100000,limit = 50000) == 1250075001
    assert candidate(n = 30,limit = 30) == 496
    assert candidate(n = 75000000,limit = 25000000) == 1
    assert candidate(n = 150,limit = 50) == 1
    assert candidate(n = 500,limit = 100) == 0
    assert candidate(n = 50,limit = 20) == 66
    assert candidate(n = 60,limit = 20) == 1
    assert candidate(n = 7,limit = 2) == 0
    assert candidate(n = 200,limit = 150) == 16476
    assert candidate(n = 8,limit = 3) == 3
    assert candidate(n = 250,limit = 200) == 27801
    assert candidate(n = 1000,limit = 200) == 0
    assert candidate(n = 25,limit = 10) == 21
    assert candidate(n = 500000,limit = 100000) == 0
    assert candidate(n = 20,limit = 5) == 0
    assert candidate(n = 200,limit = 50) == 0
    assert candidate(n = 90,limit = 90) == 4186
    assert candidate(n = 300,limit = 100) == 1
    assert candidate(n = 1000,limit = 500) == 125751
    assert candidate(n = 99,limit = 99) == 5050
    assert candidate(n = 30,limit = 10) == 1
    assert candidate(n = 50,limit = 10) == 0
    assert candidate(n = 20,limit = 3) == 0
    assert candidate(n = 125,limit = 100) == 7026
    assert candidate(n = 999,limit = 333) == 1
    assert candidate(n = 80,limit = 40) == 861
    assert candidate(n = 120,limit = 60) == 1891
    assert candidate(n = 8,limit = 2) == 0
    assert candidate(n = 50,limit = 15) == 0
    assert candidate(n = 25,limit = 25) == 351
    assert candidate(n = 100000000,limit = 50000000) == 1250000075000001
    assert candidate(n = 45,limit = 10) == 0
    assert candidate(n = 1000000,limit = 500000) == 125000750001
    assert candidate(n = 15,limit = 15) == 136
    assert candidate(n = 10000,limit = 5000) == 12507501
    assert candidate(n = 150,limit = 40) == 0
    assert candidate(n = 99,limit = 33) == 1
    assert candidate(n = 15,limit = 1) == 0
    assert candidate(n = 100000,limit = 30000) == 0
    assert candidate(n = 5000,limit = 2500) == 3128751
    assert candidate(n = 99999999,limit = 33333333) == 1
    assert candidate(n = 2,limit = 10) == 6
    assert candidate(n = 12,limit = 4) == 1
    assert candidate(n = 200,limit = 10) == 0
    assert candidate(n = 60,limit = 15) == 0
    assert candidate(n = 200,limit = 75) == 351
    assert candidate(n = 100,limit = 30) == 0
    assert candidate(n = 175,limit = 50) == 0
    assert candidate(n = 100,limit = 100) == 5151
    assert candidate(n = 9,limit = 9) == 55
    assert candidate(n = 10000000,limit = 5000000) == 12500007500001
    assert candidate(n = 80,limit = 30) == 66


