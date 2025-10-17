def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 10,k = 1) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 1) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 500) == 761367694
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 500) == 761367694: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 4) == 735
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 4) == 735: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 50) == 768969154
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 50) == 768969154: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 11) == 647427950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 11) == 647427950: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 3) == 1172700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 3) == 1172700: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,k = 200) == 321592380
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,k = 200) == 321592380: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,k = 150) == 266738846
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,k = 150) == 266738846: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 20) == 997277428
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 20) == 997277428: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 100) == 515897308
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 100) == 515897308: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,k = 40) == 957213722
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,k = 40) == 957213722: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 400) == 156741878
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 400) == 156741878: {e}')
    
    total += 1
    try:
        result = candidate(n = 90,k = 45) == 884068127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90,k = 45) == 884068127: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 999) == 499500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 999) == 499500: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,k = 200) == 692591146
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,k = 200) == 692591146: {e}')
    
    total += 1
    try:
        result = candidate(n = 70,k = 35) == 834330443
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 70,k = 35) == 834330443: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 10) == 513911237
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 10) == 513911237: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 15) == 439815546
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 15) == 439815546: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,k = 40) == 539248312
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,k = 40) == 539248312: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,k = 35) == 48172892
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,k = 35) == 48172892: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,k = 10) == 650177568
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,k = 10) == 650177568: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,k = 200) == 252157911
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,k = 200) == 252157911: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 20) == 506372014
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 20) == 506372014: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 2) == 540925953
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 2) == 540925953: {e}')
    
    total += 1
    try:
        result = candidate(n = 700,k = 350) == 411412946
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700,k = 350) == 411412946: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 1) == 22779421
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 1) == 22779421: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 499) == 23728871
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 499) == 23728871: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,k = 450) == 911433285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,k = 450) == 911433285: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,k = 900) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,k = 900) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,k = 75) == 309130836
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,k = 75) == 309130836: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 4) == 6769
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 4) == 6769: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 10) == 451985432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 10) == 451985432: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 10) == 283914142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 10) == 283914142: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,k = 100) == 677105109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,k = 100) == 677105109: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 15) == 729045180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 15) == 729045180: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,k = 249) == 31125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,k = 249) == 31125: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,k = 200) == 168555168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,k = 200) == 168555168: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 1000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 1000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 1) == 756641425
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 1) == 756641425: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 7) == 409322830
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 7) == 409322830: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 599) == 179700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 599) == 179700: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,k = 300) == 156733966
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,k = 300) == 156733966: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 300) == 326283128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 300) == 326283128: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,k = 375) == 43563744
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,k = 375) == 43563744: {e}')
    
    total += 1
    try:
        result = candidate(n = 700,k = 30) == 785311933
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700,k = 30) == 785311933: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,k = 400) == 551599071
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,k = 400) == 551599071: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 50) == 982286335
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 50) == 982286335: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 500) == 975713359
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 500) == 975713359: {e}')
    
    total += 1
    try:
        result = candidate(n = 350,k = 175) == 62253251
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 350,k = 175) == 62253251: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,k = 250) == 585657508
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,k = 250) == 585657508: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 250) == 112330193
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 250) == 112330193: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 25) == 253549512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 25) == 253549512: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 10,k = 1) == 362880
    assert candidate(n = 1000,k = 500) == 761367694
    assert candidate(n = 7,k = 4) == 735
    assert candidate(n = 1,k = 1) == 1
    assert candidate(n = 3,k = 2) == 3
    assert candidate(n = 100,k = 50) == 768969154
    assert candidate(n = 5,k = 5) == 1
    assert candidate(n = 20,k = 11) == 647427950
    assert candidate(n = 4,k = 3) == 6
    assert candidate(n = 10,k = 3) == 1172700
    assert candidate(n = 400,k = 200) == 321592380
    assert candidate(n = 300,k = 150) == 266738846
    assert candidate(n = 500,k = 20) == 997277428
    assert candidate(n = 200,k = 100) == 515897308
    assert candidate(n = 75,k = 40) == 957213722
    assert candidate(n = 600,k = 400) == 156741878
    assert candidate(n = 90,k = 45) == 884068127
    assert candidate(n = 1000,k = 999) == 499500
    assert candidate(n = 300,k = 200) == 692591146
    assert candidate(n = 70,k = 35) == 834330443
    assert candidate(n = 25,k = 10) == 513911237
    assert candidate(n = 30,k = 15) == 439815546
    assert candidate(n = 900,k = 40) == 539248312
    assert candidate(n = 75,k = 35) == 48172892
    assert candidate(n = 400,k = 10) == 650177568
    assert candidate(n = 800,k = 200) == 252157911
    assert candidate(n = 50,k = 20) == 506372014
    assert candidate(n = 999,k = 999) == 1
    assert candidate(n = 500,k = 2) == 540925953
    assert candidate(n = 700,k = 350) == 411412946
    assert candidate(n = 999,k = 1) == 22779421
    assert candidate(n = 999,k = 499) == 23728871
    assert candidate(n = 900,k = 450) == 911433285
    assert candidate(n = 900,k = 900) == 1
    assert candidate(n = 150,k = 75) == 309130836
    assert candidate(n = 8,k = 4) == 6769
    assert candidate(n = 100,k = 10) == 451985432
    assert candidate(n = 30,k = 10) == 283914142
    assert candidate(n = 750,k = 100) == 677105109
    assert candidate(n = 25,k = 15) == 729045180
    assert candidate(n = 250,k = 249) == 31125
    assert candidate(n = 250,k = 200) == 168555168
    assert candidate(n = 1000,k = 1000) == 1
    assert candidate(n = 1000,k = 1) == 756641425
    assert candidate(n = 15,k = 7) == 409322830
    assert candidate(n = 600,k = 599) == 179700
    assert candidate(n = 800,k = 300) == 156733966
    assert candidate(n = 600,k = 300) == 326283128
    assert candidate(n = 750,k = 375) == 43563744
    assert candidate(n = 700,k = 30) == 785311933
    assert candidate(n = 800,k = 400) == 551599071
    assert candidate(n = 500,k = 50) == 982286335
    assert candidate(n = 999,k = 500) == 975713359
    assert candidate(n = 350,k = 175) == 62253251
    assert candidate(n = 400,k = 250) == 585657508
    assert candidate(n = 500,k = 250) == 112330193
    assert candidate(n = 50,k = 25) == 253549512


