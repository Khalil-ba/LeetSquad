def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(zero = 5,one = 5,limit = 4) == 242
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 5,one = 5,limit = 4) == 242: {e}')
    
    total += 1
    try:
        result = candidate(zero = 100,one = 100,limit = 50) == 375840050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 100,one = 100,limit = 50) == 375840050: {e}')
    
    total += 1
    try:
        result = candidate(zero = 5,one = 5,limit = 2) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 5,one = 5,limit = 2) == 84: {e}')
    
    total += 1
    try:
        result = candidate(zero = 4,one = 4,limit = 3) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 4,one = 4,limit = 3) == 62: {e}')
    
    total += 1
    try:
        result = candidate(zero = 2,one = 2,limit = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 2,one = 2,limit = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(zero = 3,one = 2,limit = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 3,one = 2,limit = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(zero = 5,one = 4,limit = 2) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 5,one = 4,limit = 2) == 45: {e}')
    
    total += 1
    try:
        result = candidate(zero = 4,one = 4,limit = 4) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 4,one = 4,limit = 4) == 70: {e}')
    
    total += 1
    try:
        result = candidate(zero = 10,one = 10,limit = 5) == 165114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 10,one = 10,limit = 5) == 165114: {e}')
    
    total += 1
    try:
        result = candidate(zero = 1,one = 1,limit = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 1,one = 1,limit = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(zero = 4,one = 5,limit = 3) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 4,one = 5,limit = 3) == 99: {e}')
    
    total += 1
    try:
        result = candidate(zero = 3,one = 3,limit = 2) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 3,one = 3,limit = 2) == 14: {e}')
    
    total += 1
    try:
        result = candidate(zero = 5,one = 5,limit = 3) == 194
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 5,one = 5,limit = 3) == 194: {e}')
    
    total += 1
    try:
        result = candidate(zero = 100,one = 100,limit = 10) == 474184186
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 100,one = 100,limit = 10) == 474184186: {e}')
    
    total += 1
    try:
        result = candidate(zero = 4,one = 3,limit = 4) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 4,one = 3,limit = 4) == 35: {e}')
    
    total += 1
    try:
        result = candidate(zero = 2,one = 3,limit = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 2,one = 3,limit = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(zero = 1,one = 2,limit = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 1,one = 2,limit = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(zero = 7,one = 8,limit = 4) == 5250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 7,one = 8,limit = 4) == 5250: {e}')
    
    total += 1
    try:
        result = candidate(zero = 100,one = 50,limit = 10) == 10967566
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 100,one = 50,limit = 10) == 10967566: {e}')
    
    total += 1
    try:
        result = candidate(zero = 75,one = 25,limit = 3) == 3276
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 75,one = 25,limit = 3) == 3276: {e}')
    
    total += 1
    try:
        result = candidate(zero = 7,one = 10,limit = 4) == 12948
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 7,one = 10,limit = 4) == 12948: {e}')
    
    total += 1
    try:
        result = candidate(zero = 9,one = 7,limit = 3) == 4848
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 9,one = 7,limit = 3) == 4848: {e}')
    
    total += 1
    try:
        result = candidate(zero = 20,one = 15,limit = 4) == 30552957
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 20,one = 15,limit = 4) == 30552957: {e}')
    
    total += 1
    try:
        result = candidate(zero = 100,one = 100,limit = 100) == 407336795
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 100,one = 100,limit = 100) == 407336795: {e}')
    
    total += 1
    try:
        result = candidate(zero = 10,one = 15,limit = 3) == 378412
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 10,one = 15,limit = 3) == 378412: {e}')
    
    total += 1
    try:
        result = candidate(zero = 9,one = 11,limit = 2) == 5344
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 9,one = 11,limit = 2) == 5344: {e}')
    
    total += 1
    try:
        result = candidate(zero = 150,one = 150,limit = 25) == 469749347
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 150,one = 150,limit = 25) == 469749347: {e}')
    
    total += 1
    try:
        result = candidate(zero = 12,one = 9,limit = 4) == 174530
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 12,one = 9,limit = 4) == 174530: {e}')
    
    total += 1
    try:
        result = candidate(zero = 10,one = 10,limit = 3) == 66486
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 10,one = 10,limit = 3) == 66486: {e}')
    
    total += 1
    try:
        result = candidate(zero = 12,one = 12,limit = 10) == 2703832
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 12,one = 12,limit = 10) == 2703832: {e}')
    
    total += 1
    try:
        result = candidate(zero = 50,one = 50,limit = 10) == 430250984
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 50,one = 50,limit = 10) == 430250984: {e}')
    
    total += 1
    try:
        result = candidate(zero = 50,one = 50,limit = 5) == 256686735
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 50,one = 50,limit = 5) == 256686735: {e}')
    
    total += 1
    try:
        result = candidate(zero = 20,one = 10,limit = 4) == 3741210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 20,one = 10,limit = 4) == 3741210: {e}')
    
    total += 1
    try:
        result = candidate(zero = 20,one = 18,limit = 6) == 378141764
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 20,one = 18,limit = 6) == 378141764: {e}')
    
    total += 1
    try:
        result = candidate(zero = 10,one = 5,limit = 3) == 546
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 10,one = 5,limit = 3) == 546: {e}')
    
    total += 1
    try:
        result = candidate(zero = 8,one = 6,limit = 4) == 2386
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 8,one = 6,limit = 4) == 2386: {e}')
    
    total += 1
    try:
        result = candidate(zero = 20,one = 20,limit = 10) == 431683431
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 20,one = 20,limit = 10) == 431683431: {e}')
    
    total += 1
    try:
        result = candidate(zero = 14,one = 14,limit = 4) == 21533230
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 14,one = 14,limit = 4) == 21533230: {e}')
    
    total += 1
    try:
        result = candidate(zero = 15,one = 12,limit = 5) == 13147531
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 15,one = 12,limit = 5) == 13147531: {e}')
    
    total += 1
    try:
        result = candidate(zero = 20,one = 10,limit = 2) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 20,one = 10,limit = 2) == 66: {e}')
    
    total += 1
    try:
        result = candidate(zero = 200,one = 150,limit = 15) == 120261210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 200,one = 150,limit = 15) == 120261210: {e}')
    
    total += 1
    try:
        result = candidate(zero = 150,one = 150,limit = 15) == 416993889
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 150,one = 150,limit = 15) == 416993889: {e}')
    
    total += 1
    try:
        result = candidate(zero = 75,one = 25,limit = 5) == 769798783
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 75,one = 25,limit = 5) == 769798783: {e}')
    
    total += 1
    try:
        result = candidate(zero = 15,one = 10,limit = 5) == 2249276
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 15,one = 10,limit = 5) == 2249276: {e}')
    
    total += 1
    try:
        result = candidate(zero = 7,one = 5,limit = 2) == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 7,one = 5,limit = 2) == 114: {e}')
    
    total += 1
    try:
        result = candidate(zero = 13,one = 10,limit = 5) == 914333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 13,one = 10,limit = 5) == 914333: {e}')
    
    total += 1
    try:
        result = candidate(zero = 25,one = 25,limit = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 25,one = 25,limit = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(zero = 17,one = 15,limit = 7) == 539683360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 17,one = 15,limit = 7) == 539683360: {e}')
    
    total += 1
    try:
        result = candidate(zero = 8,one = 12,limit = 2) == 1391
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 8,one = 12,limit = 2) == 1391: {e}')
    
    total += 1
    try:
        result = candidate(zero = 20,one = 20,limit = 5) == 89895606
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 20,one = 20,limit = 5) == 89895606: {e}')
    
    total += 1
    try:
        result = candidate(zero = 12,one = 12,limit = 6) == 2555112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 12,one = 12,limit = 6) == 2555112: {e}')
    
    total += 1
    try:
        result = candidate(zero = 20,one = 15,limit = 7) == 957788108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 20,one = 15,limit = 7) == 957788108: {e}')
    
    total += 1
    try:
        result = candidate(zero = 8,one = 7,limit = 3) == 3296
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 8,one = 7,limit = 3) == 3296: {e}')
    
    total += 1
    try:
        result = candidate(zero = 7,one = 5,limit = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 7,one = 5,limit = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(zero = 50,one = 50,limit = 4) == 507669790
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 50,one = 50,limit = 4) == 507669790: {e}')
    
    total += 1
    try:
        result = candidate(zero = 7,one = 8,limit = 2) == 720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 7,one = 8,limit = 2) == 720: {e}')
    
    total += 1
    try:
        result = candidate(zero = 15,one = 20,limit = 5) == 983489078
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 15,one = 20,limit = 5) == 983489078: {e}')
    
    total += 1
    try:
        result = candidate(zero = 6,one = 8,limit = 2) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 6,one = 8,limit = 2) == 300: {e}')
    
    total += 1
    try:
        result = candidate(zero = 7,one = 5,limit = 4) == 664
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 7,one = 5,limit = 4) == 664: {e}')
    
    total += 1
    try:
        result = candidate(zero = 6,one = 6,limit = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 6,one = 6,limit = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(zero = 15,one = 15,limit = 5) == 119126132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 15,one = 15,limit = 5) == 119126132: {e}')
    
    total += 1
    try:
        result = candidate(zero = 15,one = 8,limit = 5) == 277298
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 15,one = 8,limit = 5) == 277298: {e}')
    
    total += 1
    try:
        result = candidate(zero = 9,one = 15,limit = 3) == 112216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 9,one = 15,limit = 3) == 112216: {e}')
    
    total += 1
    try:
        result = candidate(zero = 10,one = 8,limit = 3) == 16025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 10,one = 8,limit = 3) == 16025: {e}')
    
    total += 1
    try:
        result = candidate(zero = 12,one = 8,limit = 6) == 114332
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 12,one = 8,limit = 6) == 114332: {e}')
    
    total += 1
    try:
        result = candidate(zero = 18,one = 12,limit = 5) == 52051889
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(zero = 18,one = 12,limit = 5) == 52051889: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(zero = 5,one = 5,limit = 4) == 242
    assert candidate(zero = 100,one = 100,limit = 50) == 375840050
    assert candidate(zero = 5,one = 5,limit = 2) == 84
    assert candidate(zero = 4,one = 4,limit = 3) == 62
    assert candidate(zero = 2,one = 2,limit = 3) == 6
    assert candidate(zero = 3,one = 2,limit = 1) == 1
    assert candidate(zero = 5,one = 4,limit = 2) == 45
    assert candidate(zero = 4,one = 4,limit = 4) == 70
    assert candidate(zero = 10,one = 10,limit = 5) == 165114
    assert candidate(zero = 1,one = 1,limit = 2) == 2
    assert candidate(zero = 4,one = 5,limit = 3) == 99
    assert candidate(zero = 3,one = 3,limit = 2) == 14
    assert candidate(zero = 5,one = 5,limit = 3) == 194
    assert candidate(zero = 100,one = 100,limit = 10) == 474184186
    assert candidate(zero = 4,one = 3,limit = 4) == 35
    assert candidate(zero = 2,one = 3,limit = 2) == 7
    assert candidate(zero = 1,one = 2,limit = 1) == 1
    assert candidate(zero = 7,one = 8,limit = 4) == 5250
    assert candidate(zero = 100,one = 50,limit = 10) == 10967566
    assert candidate(zero = 75,one = 25,limit = 3) == 3276
    assert candidate(zero = 7,one = 10,limit = 4) == 12948
    assert candidate(zero = 9,one = 7,limit = 3) == 4848
    assert candidate(zero = 20,one = 15,limit = 4) == 30552957
    assert candidate(zero = 100,one = 100,limit = 100) == 407336795
    assert candidate(zero = 10,one = 15,limit = 3) == 378412
    assert candidate(zero = 9,one = 11,limit = 2) == 5344
    assert candidate(zero = 150,one = 150,limit = 25) == 469749347
    assert candidate(zero = 12,one = 9,limit = 4) == 174530
    assert candidate(zero = 10,one = 10,limit = 3) == 66486
    assert candidate(zero = 12,one = 12,limit = 10) == 2703832
    assert candidate(zero = 50,one = 50,limit = 10) == 430250984
    assert candidate(zero = 50,one = 50,limit = 5) == 256686735
    assert candidate(zero = 20,one = 10,limit = 4) == 3741210
    assert candidate(zero = 20,one = 18,limit = 6) == 378141764
    assert candidate(zero = 10,one = 5,limit = 3) == 546
    assert candidate(zero = 8,one = 6,limit = 4) == 2386
    assert candidate(zero = 20,one = 20,limit = 10) == 431683431
    assert candidate(zero = 14,one = 14,limit = 4) == 21533230
    assert candidate(zero = 15,one = 12,limit = 5) == 13147531
    assert candidate(zero = 20,one = 10,limit = 2) == 66
    assert candidate(zero = 200,one = 150,limit = 15) == 120261210
    assert candidate(zero = 150,one = 150,limit = 15) == 416993889
    assert candidate(zero = 75,one = 25,limit = 5) == 769798783
    assert candidate(zero = 15,one = 10,limit = 5) == 2249276
    assert candidate(zero = 7,one = 5,limit = 2) == 114
    assert candidate(zero = 13,one = 10,limit = 5) == 914333
    assert candidate(zero = 25,one = 25,limit = 1) == 2
    assert candidate(zero = 17,one = 15,limit = 7) == 539683360
    assert candidate(zero = 8,one = 12,limit = 2) == 1391
    assert candidate(zero = 20,one = 20,limit = 5) == 89895606
    assert candidate(zero = 12,one = 12,limit = 6) == 2555112
    assert candidate(zero = 20,one = 15,limit = 7) == 957788108
    assert candidate(zero = 8,one = 7,limit = 3) == 3296
    assert candidate(zero = 7,one = 5,limit = 1) == 0
    assert candidate(zero = 50,one = 50,limit = 4) == 507669790
    assert candidate(zero = 7,one = 8,limit = 2) == 720
    assert candidate(zero = 15,one = 20,limit = 5) == 983489078
    assert candidate(zero = 6,one = 8,limit = 2) == 300
    assert candidate(zero = 7,one = 5,limit = 4) == 664
    assert candidate(zero = 6,one = 6,limit = 1) == 2
    assert candidate(zero = 15,one = 15,limit = 5) == 119126132
    assert candidate(zero = 15,one = 8,limit = 5) == 277298
    assert candidate(zero = 9,one = 15,limit = 3) == 112216
    assert candidate(zero = 10,one = 8,limit = 3) == 16025
    assert candidate(zero = 12,one = 8,limit = 6) == 114332
    assert candidate(zero = 18,one = 12,limit = 5) == 52051889


