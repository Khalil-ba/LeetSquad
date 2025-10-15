def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 1000,k = 500) == 955735232
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 500) == 955735232: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 50) == 788876615
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 50) == 788876615: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 10) == 21670
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 10) == 21670: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 50) == 445329159
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 50) == 445329159: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 20) == 230131
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 20) == 230131: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 5) == 1068
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 5) == 1068: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 4) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 4) == 49: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 500) == 334048938
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 500) == 334048938: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 1000) == 663677020
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 1000) == 663677020: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 10) == 573
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 10) == 573: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 5) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 5) == 71: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 100) == 959322173
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 100) == 959322173: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 250) == 340232605
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 250) == 340232605: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,k = 200) == 155930478
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,k = 200) == 155930478: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,k = 150) == 954108341
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,k = 150) == 954108341: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,k = 125) == 963392607
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,k = 125) == 963392607: {e}')
    
    total += 1
    try:
        result = candidate(n = 450,k = 350) == 817469743
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450,k = 350) == 817469743: {e}')
    
    total += 1
    try:
        result = candidate(n = 550,k = 350) == 753008434
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 550,k = 350) == 753008434: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 100) == 372936062
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 100) == 372936062: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,k = 700) == 867124875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,k = 700) == 867124875: {e}')
    
    total += 1
    try:
        result = candidate(n = 950,k = 600) == 304125714
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 950,k = 600) == 304125714: {e}')
    
    total += 1
    try:
        result = candidate(n = 650,k = 325) == 651704209
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 650,k = 325) == 651704209: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,k = 300) == 319486156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,k = 300) == 319486156: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 1) == 499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 1) == 499: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,k = 200) == 784163913
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,k = 200) == 784163913: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 600) == 423901727
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 600) == 423901727: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,k = 350) == 167531348
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,k = 350) == 167531348: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,k = 600) == 545089101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,k = 600) == 545089101: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 199) == 113707737
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 199) == 113707737: {e}')
    
    total += 1
    try:
        result = candidate(n = 350,k = 100) == 882052434
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 350,k = 100) == 882052434: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,k = 500) == 237860861
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,k = 500) == 237860861: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 150) == 691281198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 150) == 691281198: {e}')
    
    total += 1
    try:
        result = candidate(n = 850,k = 750) == 613893680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 850,k = 750) == 613893680: {e}')
    
    total += 1
    try:
        result = candidate(n = 550,k = 275) == 829312124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 550,k = 275) == 829312124: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,k = 250) == 998393645
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,k = 250) == 998393645: {e}')
    
    total += 1
    try:
        result = candidate(n = 700,k = 250) == 533593353
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700,k = 250) == 533593353: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,k = 700) == 199653602
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,k = 700) == 199653602: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 300) == 818876359
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 300) == 818876359: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 75) == 472228743
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 75) == 472228743: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 999) == 570203540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 999) == 570203540: {e}')
    
    total += 1
    try:
        result = candidate(n = 700,k = 350) == 622326263
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700,k = 350) == 622326263: {e}')
    
    total += 1
    try:
        result = candidate(n = 825,k = 412) == 680368220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 825,k = 412) == 680368220: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,k = 450) == 610615323
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,k = 450) == 610615323: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,k = 299) == 425310890
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,k = 299) == 425310890: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,k = 900) == 218855132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,k = 900) == 218855132: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,k = 399) == 759251773
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,k = 399) == 759251773: {e}')
    
    total += 1
    try:
        result = candidate(n = 990,k = 500) == 863155312
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 990,k = 500) == 863155312: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 100) == 777381270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 100) == 777381270: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 800) == 139677600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 800) == 139677600: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,k = 75) == 532579469
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,k = 75) == 532579469: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,k = 600) == 37939667
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,k = 600) == 37939667: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,k = 750) == 420581417
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,k = 750) == 420581417: {e}')
    
    total += 1
    try:
        result = candidate(n = 120,k = 119) == 156717557
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120,k = 119) == 156717557: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,k = 100) == 68842652
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,k = 100) == 68842652: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,k = 250) == 946579835
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,k = 250) == 946579835: {e}')
    
    total += 1
    try:
        result = candidate(n = 850,k = 700) == 259344610
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 850,k = 700) == 259344610: {e}')
    
    total += 1
    try:
        result = candidate(n = 950,k = 900) == 333369296
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 950,k = 900) == 333369296: {e}')
    
    total += 1
    try:
        result = candidate(n = 950,k = 450) == 946420580
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 950,k = 450) == 946420580: {e}')
    
    total += 1
    try:
        result = candidate(n = 650,k = 400) == 449625333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 650,k = 400) == 449625333: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,k = 149) == 480922327
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,k = 149) == 480922327: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,k = 300) == 64634329
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,k = 300) == 64634329: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,k = 100) == 86577949
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,k = 100) == 86577949: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 300) == 537290507
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 300) == 537290507: {e}')
    
    total += 1
    try:
        result = candidate(n = 998,k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 998,k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 350,k = 150) == 604337481
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 350,k = 150) == 604337481: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,k = 400) == 628007887
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,k = 400) == 628007887: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,k = 500) == 620935219
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,k = 500) == 620935219: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,k = 150) == 958391787
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,k = 150) == 958391787: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 100) == 725526442
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 100) == 725526442: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 200) == 785265253
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 200) == 785265253: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 25) == 913564693
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 25) == 913564693: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 550) == 430003494
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 550) == 430003494: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 1000,k = 500) == 955735232
    assert candidate(n = 100,k = 0) == 1
    assert candidate(n = 20,k = 50) == 788876615
    assert candidate(n = 1000,k = 0) == 1
    assert candidate(n = 10,k = 10) == 21670
    assert candidate(n = 3,k = 0) == 1
    assert candidate(n = 100,k = 50) == 445329159
    assert candidate(n = 10,k = 20) == 230131
    assert candidate(n = 10,k = 5) == 1068
    assert candidate(n = 6,k = 4) == 49
    assert candidate(n = 500,k = 500) == 334048938
    assert candidate(n = 4,k = 2) == 5
    assert candidate(n = 5,k = 3) == 15
    assert candidate(n = 3,k = 1) == 2
    assert candidate(n = 1000,k = 1000) == 663677020
    assert candidate(n = 7,k = 10) == 573
    assert candidate(n = 6,k = 5) == 71
    assert candidate(n = 100,k = 100) == 959322173
    assert candidate(n = 500,k = 250) == 340232605
    assert candidate(n = 400,k = 200) == 155930478
    assert candidate(n = 300,k = 150) == 954108341
    assert candidate(n = 250,k = 125) == 963392607
    assert candidate(n = 450,k = 350) == 817469743
    assert candidate(n = 550,k = 350) == 753008434
    assert candidate(n = 200,k = 100) == 372936062
    assert candidate(n = 900,k = 700) == 867124875
    assert candidate(n = 950,k = 600) == 304125714
    assert candidate(n = 650,k = 325) == 651704209
    assert candidate(n = 750,k = 300) == 319486156
    assert candidate(n = 500,k = 1) == 499
    assert candidate(n = 750,k = 200) == 784163913
    assert candidate(n = 500,k = 600) == 423901727
    assert candidate(n = 800,k = 350) == 167531348
    assert candidate(n = 800,k = 600) == 545089101
    assert candidate(n = 200,k = 199) == 113707737
    assert candidate(n = 350,k = 100) == 882052434
    assert candidate(n = 800,k = 500) == 237860861
    assert candidate(n = 200,k = 150) == 691281198
    assert candidate(n = 850,k = 750) == 613893680
    assert candidate(n = 550,k = 275) == 829312124
    assert candidate(n = 750,k = 250) == 998393645
    assert candidate(n = 700,k = 250) == 533593353
    assert candidate(n = 750,k = 700) == 199653602
    assert candidate(n = 200,k = 300) == 818876359
    assert candidate(n = 100,k = 75) == 472228743
    assert candidate(n = 999,k = 999) == 570203540
    assert candidate(n = 700,k = 350) == 622326263
    assert candidate(n = 825,k = 412) == 680368220
    assert candidate(n = 900,k = 450) == 610615323
    assert candidate(n = 300,k = 299) == 425310890
    assert candidate(n = 900,k = 900) == 218855132
    assert candidate(n = 400,k = 399) == 759251773
    assert candidate(n = 990,k = 500) == 863155312
    assert candidate(n = 600,k = 100) == 777381270
    assert candidate(n = 600,k = 800) == 139677600
    assert candidate(n = 150,k = 75) == 532579469
    assert candidate(n = 750,k = 600) == 37939667
    assert candidate(n = 800,k = 750) == 420581417
    assert candidate(n = 120,k = 119) == 156717557
    assert candidate(n = 500,k = 0) == 1
    assert candidate(n = 900,k = 100) == 68842652
    assert candidate(n = 800,k = 0) == 1
    assert candidate(n = 250,k = 250) == 946579835
    assert candidate(n = 850,k = 700) == 259344610
    assert candidate(n = 950,k = 900) == 333369296
    assert candidate(n = 950,k = 450) == 946420580
    assert candidate(n = 650,k = 400) == 449625333
    assert candidate(n = 150,k = 149) == 480922327
    assert candidate(n = 900,k = 300) == 64634329
    assert candidate(n = 300,k = 100) == 86577949
    assert candidate(n = 600,k = 300) == 537290507
    assert candidate(n = 998,k = 0) == 1
    assert candidate(n = 350,k = 150) == 604337481
    assert candidate(n = 800,k = 400) == 628007887
    assert candidate(n = 750,k = 500) == 620935219
    assert candidate(n = 400,k = 150) == 958391787
    assert candidate(n = 500,k = 100) == 725526442
    assert candidate(n = 600,k = 200) == 785265253
    assert candidate(n = 50,k = 25) == 913564693
    assert candidate(n = 600,k = 550) == 430003494


