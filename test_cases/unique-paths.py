def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(m = 20,n = 30) == 11541847896480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 30) == 11541847896480: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 7) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 7) == 28: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 5) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 5) == 70: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10) == 48620
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10) == 48620: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(m = 30,n = 20) == 11541847896480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 30,n = 20) == 11541847896480: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(m = 40,n = 30) == 13750991318793417920
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 40,n = 30) == 13750991318793417920: {e}')
    
    total += 1
    try:
        result = candidate(m = 67,n = 33) == 65814642035034133075191231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 67,n = 33) == 65814642035034133075191231: {e}')
    
    total += 1
    try:
        result = candidate(m = 30,n = 30) == 30067266499541040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 30,n = 30) == 30067266499541040: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 95) == 3612280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 95) == 3612280: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 15) == 40116600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 15) == 40116600: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 50) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 50) == 1: {e}')
    
    total += 1
    try:
        result = candidate(m = 30,n = 40) == 13750991318793417920
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 30,n = 40) == 13750991318793417920: {e}')
    
    total += 1
    try:
        result = candidate(m = 99,n = 99) == 5716592448890534420436582360196242777068052430850904489000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 99,n = 99) == 5716592448890534420436582360196242777068052430850904489000: {e}')
    
    total += 1
    try:
        result = candidate(m = 25,n = 75) == 45931679871275969889300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 25,n = 75) == 45931679871275969889300: {e}')
    
    total += 1
    try:
        result = candidate(m = 90,n = 10) == 1573664496040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 90,n = 10) == 1573664496040: {e}')
    
    total += 1
    try:
        result = candidate(m = 75,n = 75) == 23362265873332749085315221863910685052043000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 75,n = 75) == 23362265873332749085315221863910685052043000: {e}')
    
    total += 1
    try:
        result = candidate(m = 30,n = 25) == 779255311989700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 30,n = 25) == 779255311989700: {e}')
    
    total += 1
    try:
        result = candidate(m = 75,n = 25) == 45931679871275969889300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 75,n = 25) == 45931679871275969889300: {e}')
    
    total += 1
    try:
        result = candidate(m = 30,n = 70) == 6230496325796261023265040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 30,n = 70) == 6230496325796261023265040: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 5) == 4421275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 5) == 4421275: {e}')
    
    total += 1
    try:
        result = candidate(m = 80,n = 80) == 23156006494021191956342707682359261381151378400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 80,n = 80) == 23156006494021191956342707682359261381151378400: {e}')
    
    total += 1
    try:
        result = candidate(m = 40,n = 10) == 1677106640
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 40,n = 10) == 1677106640: {e}')
    
    total += 1
    try:
        result = candidate(m = 80,n = 20) == 86623575014757120480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 80,n = 20) == 86623575014757120480: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 8) == 330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 8) == 330: {e}')
    
    total += 1
    try:
        result = candidate(m = 99,n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 99,n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 100) == 4421275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 100) == 4421275: {e}')
    
    total += 1
    try:
        result = candidate(m = 99,n = 2) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 99,n = 2) == 99: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 90) == 1573664496040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 90) == 1573664496040: {e}')
    
    total += 1
    try:
        result = candidate(m = 60,n = 60) == 24356699707654619143838606602026720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 60,n = 60) == 24356699707654619143838606602026720: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 99) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 99) == 99: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 99) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 99) == 1: {e}')
    
    total += 1
    try:
        result = candidate(m = 45,n = 35) == 14429347509452441488650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 45,n = 35) == 14429347509452441488650: {e}')
    
    total += 1
    try:
        result = candidate(m = 55,n = 45) == 15362117803534044899180148240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 55,n = 45) == 15362117803534044899180148240: {e}')
    
    total += 1
    try:
        result = candidate(m = 50,n = 2) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 50,n = 2) == 50: {e}')
    
    total += 1
    try:
        result = candidate(m = 60,n = 40) == 3332420398982499757882998720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 60,n = 40) == 3332420398982499757882998720: {e}')
    
    total += 1
    try:
        result = candidate(m = 50,n = 50) == 25477612258980856902730428600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 50,n = 50) == 25477612258980856902730428600: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 100) == 22750883079422934966181954039568885395604168260154104734000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 100) == 22750883079422934966181954039568885395604168260154104734000: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 5) == 3060
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 5) == 3060: {e}')
    
    total += 1
    try:
        result = candidate(m = 99,n = 100) == 11375441539711467483090977019784442697802084130077052367000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 99,n = 100) == 11375441539711467483090977019784442697802084130077052367000: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 80) == 86623575014757120480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 80) == 86623575014757120480: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 20) == 818809200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 20) == 818809200: {e}')
    
    total += 1
    try:
        result = candidate(m = 45,n = 55) == 15362117803534044899180148240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 45,n = 55) == 15362117803534044899180148240: {e}')
    
    total += 1
    try:
        result = candidate(m = 25,n = 25) == 32247603683100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 25,n = 25) == 32247603683100: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 50) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 50) == 50: {e}')
    
    total += 1
    try:
        result = candidate(m = 40,n = 60) == 3332420398982499757882998720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 40,n = 60) == 3332420398982499757882998720: {e}')
    
    total += 1
    try:
        result = candidate(m = 50,n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 50,n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(m = 70,n = 30) == 6230496325796261023265040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 70,n = 30) == 6230496325796261023265040: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 25) == 9669554100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 25) == 9669554100: {e}')
    
    total += 1
    try:
        result = candidate(m = 33,n = 67) == 65814642035034133075191231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 33,n = 67) == 65814642035034133075191231: {e}')
    
    total += 1
    try:
        result = candidate(m = 35,n = 45) == 14429347509452441488650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 35,n = 45) == 14429347509452441488650: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(m = 20,n = 30) == 11541847896480
    assert candidate(m = 1,n = 100) == 1
    assert candidate(m = 3,n = 7) == 28
    assert candidate(m = 5,n = 5) == 70
    assert candidate(m = 10,n = 10) == 48620
    assert candidate(m = 5,n = 3) == 15
    assert candidate(m = 30,n = 20) == 11541847896480
    assert candidate(m = 1,n = 1) == 1
    assert candidate(m = 3,n = 2) == 3
    assert candidate(m = 100,n = 1) == 1
    assert candidate(m = 40,n = 30) == 13750991318793417920
    assert candidate(m = 67,n = 33) == 65814642035034133075191231
    assert candidate(m = 30,n = 30) == 30067266499541040
    assert candidate(m = 5,n = 95) == 3612280
    assert candidate(m = 15,n = 15) == 40116600
    assert candidate(m = 1,n = 50) == 1
    assert candidate(m = 30,n = 40) == 13750991318793417920
    assert candidate(m = 99,n = 99) == 5716592448890534420436582360196242777068052430850904489000
    assert candidate(m = 25,n = 75) == 45931679871275969889300
    assert candidate(m = 90,n = 10) == 1573664496040
    assert candidate(m = 75,n = 75) == 23362265873332749085315221863910685052043000
    assert candidate(m = 30,n = 25) == 779255311989700
    assert candidate(m = 75,n = 25) == 45931679871275969889300
    assert candidate(m = 30,n = 70) == 6230496325796261023265040
    assert candidate(m = 100,n = 5) == 4421275
    assert candidate(m = 80,n = 80) == 23156006494021191956342707682359261381151378400
    assert candidate(m = 40,n = 10) == 1677106640
    assert candidate(m = 80,n = 20) == 86623575014757120480
    assert candidate(m = 5,n = 8) == 330
    assert candidate(m = 99,n = 1) == 1
    assert candidate(m = 5,n = 100) == 4421275
    assert candidate(m = 99,n = 2) == 99
    assert candidate(m = 10,n = 90) == 1573664496040
    assert candidate(m = 60,n = 60) == 24356699707654619143838606602026720
    assert candidate(m = 2,n = 99) == 99
    assert candidate(m = 1,n = 99) == 1
    assert candidate(m = 45,n = 35) == 14429347509452441488650
    assert candidate(m = 55,n = 45) == 15362117803534044899180148240
    assert candidate(m = 50,n = 2) == 50
    assert candidate(m = 60,n = 40) == 3332420398982499757882998720
    assert candidate(m = 50,n = 50) == 25477612258980856902730428600
    assert candidate(m = 100,n = 100) == 22750883079422934966181954039568885395604168260154104734000
    assert candidate(m = 15,n = 5) == 3060
    assert candidate(m = 99,n = 100) == 11375441539711467483090977019784442697802084130077052367000
    assert candidate(m = 20,n = 80) == 86623575014757120480
    assert candidate(m = 15,n = 20) == 818809200
    assert candidate(m = 45,n = 55) == 15362117803534044899180148240
    assert candidate(m = 25,n = 25) == 32247603683100
    assert candidate(m = 2,n = 50) == 50
    assert candidate(m = 40,n = 60) == 3332420398982499757882998720
    assert candidate(m = 50,n = 1) == 1
    assert candidate(m = 70,n = 30) == 6230496325796261023265040
    assert candidate(m = 15,n = 25) == 9669554100
    assert candidate(m = 33,n = 67) == 65814642035034133075191231
    assert candidate(m = 35,n = 45) == 14429347509452441488650


