def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 1000,k = 500) == 596728287
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 500) == 596728287: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 3) == 9330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 3) == 9330: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 10) == 378340883
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 10) == 378340883: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 5) == 206085257
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 5) == 206085257: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 3) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 3) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 1000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 1000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 300) == 813183219
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 300) == 813183219: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 5) == 966649451
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 5) == 966649451: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,k = 400) == 650941527
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,k = 400) == 650941527: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,k = 500) == 342539373
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,k = 500) == 342539373: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 100) == 161201312
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 100) == 161201312: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 250) == 676349352
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 250) == 676349352: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,k = 200) == 679937489
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,k = 200) == 679937489: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,k = 150) == 568085204
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,k = 150) == 568085204: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,k = 125) == 124953151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,k = 125) == 124953151: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,k = 150) == 4371823
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,k = 150) == 4371823: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,k = 100) == 311535191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,k = 100) == 311535191: {e}')
    
    total += 1
    try:
        result = candidate(n = 994,k = 993) == 493521
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 994,k = 993) == 493521: {e}')
    
    total += 1
    try:
        result = candidate(n = 993,k = 992) == 492528
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 993,k = 992) == 492528: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 3) == 665269768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 3) == 665269768: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 400) == 683659184
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 400) == 683659184: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 999) == 499500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 999) == 499500: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 998) == 498501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 998) == 498501: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 850,k = 350) == 712690888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 850,k = 350) == 712690888: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,k = 500) == 284510904
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,k = 500) == 284510904: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,k = 200) == 571331062
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,k = 200) == 571331062: {e}')
    
    total += 1
    try:
        result = candidate(n = 850,k = 849) == 360825
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 850,k = 849) == 360825: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,k = 500) == 956879971
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,k = 500) == 956879971: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 150) == 794694748
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 150) == 794694748: {e}')
    
    total += 1
    try:
        result = candidate(n = 950,k = 475) == 232624618
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 950,k = 475) == 232624618: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 5) == 417567540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 5) == 417567540: {e}')
    
    total += 1
    try:
        result = candidate(n = 990,k = 495) == 515680544
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 990,k = 495) == 515680544: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,k = 250) == 737835972
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,k = 250) == 737835972: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 50) == 260006047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 50) == 260006047: {e}')
    
    total += 1
    try:
        result = candidate(n = 700,k = 699) == 244650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700,k = 699) == 244650: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,k = 3) == 321610892
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,k = 3) == 321610892: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 2) == 695241506
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 2) == 695241506: {e}')
    
    total += 1
    try:
        result = candidate(n = 700,k = 350) == 301962055
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700,k = 350) == 301962055: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 500) == 285828216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 500) == 285828216: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,k = 899) == 404550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,k = 899) == 404550: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,k = 450) == 503243704
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,k = 450) == 503243704: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 5) == 42525
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 5) == 42525: {e}')
    
    total += 1
    try:
        result = candidate(n = 997,k = 996) == 496506
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 997,k = 996) == 496506: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,k = 100) == 917829186
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,k = 100) == 917829186: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 499) == 124750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 499) == 124750: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 50) == 554366381
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 50) == 554366381: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,k = 799) == 319600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,k = 799) == 319600: {e}')
    
    total += 1
    try:
        result = candidate(n = 995,k = 994) == 494515
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 995,k = 994) == 494515: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 900) == 702608248
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 900) == 702608248: {e}')
    
    total += 1
    try:
        result = candidate(n = 850,k = 700) == 922581560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 850,k = 700) == 922581560: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 600) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 600) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 10) == 684028799
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 10) == 684028799: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 599) == 179700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 599) == 179700: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,k = 300) == 1679831
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,k = 300) == 1679831: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,k = 375) == 867329310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,k = 375) == 867329310: {e}')
    
    total += 1
    try:
        result = candidate(n = 700,k = 700) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700,k = 700) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 650,k = 200) == 747665402
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 650,k = 200) == 747665402: {e}')
    
    total += 1
    try:
        result = candidate(n = 996,k = 995) == 495510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 996,k = 995) == 495510: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 2) == 823229628
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 2) == 823229628: {e}')
    
    total += 1
    try:
        result = candidate(n = 998,k = 500) == 576595067
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 998,k = 500) == 576595067: {e}')
    
    total += 1
    try:
        result = candidate(n = 950,k = 850) == 996415676
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 950,k = 850) == 996415676: {e}')
    
    total += 1
    try:
        result = candidate(n = 998,k = 997) == 497503
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 998,k = 997) == 497503: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 500) == 903541535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 500) == 903541535: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 200) == 358751836
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 200) == 358751836: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 25) == 231522025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 25) == 231522025: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 1000,k = 500) == 596728287
    assert candidate(n = 3,k = 2) == 3
    assert candidate(n = 1,k = 1) == 1
    assert candidate(n = 5,k = 1) == 1
    assert candidate(n = 10,k = 10) == 1
    assert candidate(n = 10,k = 3) == 9330
    assert candidate(n = 10,k = 1) == 1
    assert candidate(n = 999,k = 999) == 1
    assert candidate(n = 100,k = 10) == 378340883
    assert candidate(n = 20,k = 5) == 206085257
    assert candidate(n = 4,k = 2) == 7
    assert candidate(n = 5,k = 3) == 25
    assert candidate(n = 1000,k = 1) == 1
    assert candidate(n = 1000,k = 1000) == 1
    assert candidate(n = 600,k = 300) == 813183219
    assert candidate(n = 500,k = 5) == 966649451
    assert candidate(n = 800,k = 400) == 650941527
    assert candidate(n = 750,k = 500) == 342539373
    assert candidate(n = 500,k = 100) == 161201312
    assert candidate(n = 500,k = 250) == 676349352
    assert candidate(n = 400,k = 200) == 679937489
    assert candidate(n = 300,k = 150) == 568085204
    assert candidate(n = 250,k = 125) == 124953151
    assert candidate(n = 250,k = 150) == 4371823
    assert candidate(n = 150,k = 100) == 311535191
    assert candidate(n = 994,k = 993) == 493521
    assert candidate(n = 993,k = 992) == 492528
    assert candidate(n = 1000,k = 3) == 665269768
    assert candidate(n = 600,k = 400) == 683659184
    assert candidate(n = 1000,k = 999) == 499500
    assert candidate(n = 999,k = 998) == 498501
    assert candidate(n = 7,k = 1) == 1
    assert candidate(n = 850,k = 350) == 712690888
    assert candidate(n = 900,k = 500) == 284510904
    assert candidate(n = 300,k = 200) == 571331062
    assert candidate(n = 850,k = 849) == 360825
    assert candidate(n = 800,k = 500) == 956879971
    assert candidate(n = 20,k = 20) == 1
    assert candidate(n = 200,k = 150) == 794694748
    assert candidate(n = 950,k = 475) == 232624618
    assert candidate(n = 1000,k = 5) == 417567540
    assert candidate(n = 990,k = 495) == 515680544
    assert candidate(n = 750,k = 250) == 737835972
    assert candidate(n = 100,k = 50) == 260006047
    assert candidate(n = 700,k = 699) == 244650
    assert candidate(n = 750,k = 3) == 321610892
    assert candidate(n = 500,k = 2) == 695241506
    assert candidate(n = 700,k = 350) == 301962055
    assert candidate(n = 600,k = 500) == 285828216
    assert candidate(n = 900,k = 899) == 404550
    assert candidate(n = 999,k = 1) == 1
    assert candidate(n = 900,k = 450) == 503243704
    assert candidate(n = 10,k = 5) == 42525
    assert candidate(n = 997,k = 996) == 496506
    assert candidate(n = 3,k = 3) == 1
    assert candidate(n = 250,k = 100) == 917829186
    assert candidate(n = 500,k = 499) == 124750
    assert candidate(n = 600,k = 50) == 554366381
    assert candidate(n = 800,k = 799) == 319600
    assert candidate(n = 995,k = 994) == 494515
    assert candidate(n = 1000,k = 900) == 702608248
    assert candidate(n = 850,k = 700) == 922581560
    assert candidate(n = 600,k = 600) == 1
    assert candidate(n = 1000,k = 10) == 684028799
    assert candidate(n = 600,k = 599) == 179700
    assert candidate(n = 900,k = 300) == 1679831
    assert candidate(n = 750,k = 375) == 867329310
    assert candidate(n = 700,k = 700) == 1
    assert candidate(n = 2,k = 2) == 1
    assert candidate(n = 650,k = 200) == 747665402
    assert candidate(n = 996,k = 995) == 495510
    assert candidate(n = 600,k = 2) == 823229628
    assert candidate(n = 998,k = 500) == 576595067
    assert candidate(n = 950,k = 850) == 996415676
    assert candidate(n = 998,k = 997) == 497503
    assert candidate(n = 999,k = 500) == 903541535
    assert candidate(n = 600,k = 200) == 358751836
    assert candidate(n = 50,k = 25) == 231522025


