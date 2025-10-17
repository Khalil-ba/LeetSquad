def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 1000,m = 1000) == 498500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,m = 1000) == 498500: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 6) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 6) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 1) == -15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 1) == -15: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,m = 4) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,m = 4) == 90: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,m = 10) == 3950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,m = 10) == 3950: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,m = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,m = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,m = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,m = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 3) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 3) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,m = 50) == 172500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,m = 50) == 172500: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,m = 7) == 32508
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,m = 7) == 32508: {e}')
    
    total += 1
    try:
        result = candidate(n = 120,m = 13) == 6090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120,m = 13) == 6090: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,m = 7) == 22555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,m = 7) == 22555: {e}')
    
    total += 1
    try:
        result = candidate(n = 350,m = 7) == 43575
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 350,m = 7) == 43575: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,m = 20) == 287600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,m = 20) == 287600: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,m = 11) == 25809
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,m = 11) == 25809: {e}')
    
    total += 1
    try:
        result = candidate(n = 950,m = 19) == 403275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 950,m = 19) == 403275: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,m = 31) == 168520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,m = 31) == 168520: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,m = 25) == 258375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,m = 25) == 258375: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,m = 333) == 495504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,m = 333) == 495504: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,m = 29) == 168120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,m = 29) == 168120: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,m = 9) == 140502
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,m = 9) == 140502: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,m = 15) == 38850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,m = 15) == 38850: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,m = 999) == 498502
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,m = 999) == 498502: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,m = 17) == 441326
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,m = 17) == 441326: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,m = 23) == 293030
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,m = 23) == 293030: {e}')
    
    total += 1
    try:
        result = candidate(n = 700,m = 29) == 227950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700,m = 29) == 227950: {e}')
    
    total += 1
    try:
        result = candidate(n = 450,m = 19) == 90987
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450,m = 19) == 90987: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,m = 5) == 107700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,m = 5) == 107700: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,m = 19) == 251985
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,m = 19) == 251985: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,m = 25) == 41250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,m = 25) == 41250: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,m = 42) == 171480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,m = 42) == 171480: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,m = 29) == 376682
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,m = 29) == 376682: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,m = 11) == 36834
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,m = 11) == 36834: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,m = 13) == 423424
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,m = 13) == 423424: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,m = 37) == 76130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,m = 37) == 76130: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,m = 41) == 118854
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,m = 41) == 118854: {e}')
    
    total += 1
    try:
        result = candidate(n = 550,m = 11) == 123475
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 550,m = 11) == 123475: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,m = 4) == 22350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,m = 4) == 22350: {e}')
    
    total += 1
    try:
        result = candidate(n = 222,m = 37) == 23199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 222,m = 37) == 23199: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,m = 31) == 300250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,m = 31) == 300250: {e}')
    
    total += 1
    try:
        result = candidate(n = 450,m = 18) == 89775
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450,m = 18) == 89775: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,m = 20) == 161700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,m = 20) == 161700: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,m = 15) == 243375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,m = 15) == 243375: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,m = 19) == 161452
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,m = 19) == 161452: {e}')
    
    total += 1
    try:
        result = candidate(n = 650,m = 17) == 186381
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 650,m = 17) == 186381: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,m = 50) == 269625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,m = 50) == 269625: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,m = 11) == 409410
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,m = 11) == 409410: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,m = 41) == 76510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,m = 41) == 76510: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,m = 13) == 26435
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,m = 13) == 26435: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,m = 33) == 300600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,m = 33) == 300600: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,m = 13) == 105984
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,m = 13) == 105984: {e}')
    
    total += 1
    try:
        result = candidate(n = 950,m = 31) == 422895
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 950,m = 31) == 422895: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,m = 250) == 123750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,m = 250) == 123750: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,m = 19) == 40590
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,m = 19) == 40590: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,m = 30) == 117090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,m = 30) == 117090: {e}')
    
    total += 1
    try:
        result = candidate(n = 700,m = 11) == 200998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700,m = 11) == 200998: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,m = 400) == 318000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,m = 400) == 318000: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,m = 55) == 390490
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,m = 55) == 390490: {e}')
    
    total += 1
    try:
        result = candidate(n = 450,m = 2) == -225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450,m = 2) == -225: {e}')
    
    total += 1
    try:
        result = candidate(n = 375,m = 16) == 61668
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 375,m = 16) == 61668: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,m = 3) == 6834
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,m = 3) == 6834: {e}')
    
    total += 1
    try:
        result = candidate(n = 333,m = 3) == 18315
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 333,m = 3) == 18315: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,m = 17) == 27805
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,m = 17) == 27805: {e}')
    
    total += 1
    try:
        result = candidate(n = 350,m = 23) == 55905
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 350,m = 23) == 55905: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,m = 29) == 41960
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,m = 29) == 41960: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,m = 16) == 69800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,m = 16) == 69800: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,m = 7) == 89466
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,m = 7) == 89466: {e}')
    
    total += 1
    try:
        result = candidate(n = 333,m = 77) == 54071
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 333,m = 77) == 54071: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,m = 5) == 168375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,m = 5) == 168375: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,m = 17) == 17856
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,m = 17) == 17856: {e}')
    
    total += 1
    try:
        result = candidate(n = 450,m = 20) == 91355
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450,m = 20) == 91355: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,m = 11) == 147630
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,m = 11) == 147630: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,m = 17) == 282048
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,m = 17) == 282048: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,m = 25) == 114750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,m = 25) == 114750: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,m = 300) == 318600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,m = 300) == 318600: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,m = 19) == 4480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,m = 19) == 4480: {e}')
    
    total += 1
    try:
        result = candidate(n = 450,m = 30) == 94275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450,m = 30) == 94275: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,m = 16) == 279600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,m = 16) == 279600: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,m = 13) == 16980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,m = 13) == 16980: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,m = 29) == 262775
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,m = 29) == 262775: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,m = 5) == 74750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,m = 5) == 74750: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,m = 8) == 14900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,m = 8) == 14900: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,m = 42) == 268773
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,m = 42) == 268773: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,m = 11) == 65548
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,m = 11) == 65548: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,m = 9) == 314550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,m = 9) == 314550: {e}')
    
    total += 1
    try:
        result = candidate(n = 450,m = 23) == 92735
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450,m = 23) == 92735: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,m = 150) == 44250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,m = 150) == 44250: {e}')
    
    total += 1
    try:
        result = candidate(n = 420,m = 23) == 80544
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 420,m = 23) == 80544: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,m = 7) == 357358
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,m = 7) == 357358: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,m = 11) == 262584
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,m = 11) == 262584: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,m = 23) == 369570
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,m = 23) == 369570: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,m = 25) == 294000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,m = 25) == 294000: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,m = 12) == 149700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,m = 12) == 149700: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 1000,m = 1000) == 498500
    assert candidate(n = 5,m = 6) == 15
    assert candidate(n = 5,m = 1) == -15
    assert candidate(n = 20,m = 4) == 90
    assert candidate(n = 100,m = 10) == 3950
    assert candidate(n = 1,m = 1) == -1
    assert candidate(n = 7,m = 2) == 4
    assert candidate(n = 10,m = 3) == 19
    assert candidate(n = 600,m = 50) == 172500
    assert candidate(n = 300,m = 7) == 32508
    assert candidate(n = 120,m = 13) == 6090
    assert candidate(n = 250,m = 7) == 22555
    assert candidate(n = 350,m = 7) == 43575
    assert candidate(n = 800,m = 20) == 287600
    assert candidate(n = 250,m = 11) == 25809
    assert candidate(n = 950,m = 19) == 403275
    assert candidate(n = 600,m = 31) == 168520
    assert candidate(n = 750,m = 25) == 258375
    assert candidate(n = 999,m = 333) == 495504
    assert candidate(n = 600,m = 29) == 168120
    assert candidate(n = 600,m = 9) == 140502
    assert candidate(n = 300,m = 15) == 38850
    assert candidate(n = 1000,m = 999) == 498502
    assert candidate(n = 999,m = 17) == 441326
    assert candidate(n = 800,m = 23) == 293030
    assert candidate(n = 700,m = 29) == 227950
    assert candidate(n = 450,m = 19) == 90987
    assert candidate(n = 600,m = 5) == 107700
    assert candidate(n = 750,m = 19) == 251985
    assert candidate(n = 300,m = 25) == 41250
    assert candidate(n = 600,m = 42) == 171480
    assert candidate(n = 900,m = 29) == 376682
    assert candidate(n = 300,m = 11) == 36834
    assert candidate(n = 999,m = 13) == 423424
    assert candidate(n = 400,m = 37) == 76130
    assert candidate(n = 500,m = 41) == 118854
    assert candidate(n = 550,m = 11) == 123475
    assert candidate(n = 300,m = 4) == 22350
    assert candidate(n = 222,m = 37) == 23199
    assert candidate(n = 800,m = 31) == 300250
    assert candidate(n = 450,m = 18) == 89775
    assert candidate(n = 600,m = 20) == 161700
    assert candidate(n = 750,m = 15) == 243375
    assert candidate(n = 600,m = 19) == 161452
    assert candidate(n = 650,m = 17) == 186381
    assert candidate(n = 750,m = 50) == 269625
    assert candidate(n = 999,m = 11) == 409410
    assert candidate(n = 400,m = 41) == 76510
    assert candidate(n = 250,m = 13) == 26435
    assert candidate(n = 800,m = 33) == 300600
    assert candidate(n = 500,m = 13) == 105984
    assert candidate(n = 950,m = 31) == 422895
    assert candidate(n = 500,m = 250) == 123750
    assert candidate(n = 300,m = 19) == 40590
    assert candidate(n = 500,m = 30) == 117090
    assert candidate(n = 700,m = 11) == 200998
    assert candidate(n = 800,m = 400) == 318000
    assert candidate(n = 900,m = 55) == 390490
    assert candidate(n = 450,m = 2) == -225
    assert candidate(n = 375,m = 16) == 61668
    assert candidate(n = 200,m = 3) == 6834
    assert candidate(n = 333,m = 3) == 18315
    assert candidate(n = 250,m = 17) == 27805
    assert candidate(n = 350,m = 23) == 55905
    assert candidate(n = 300,m = 29) == 41960
    assert candidate(n = 400,m = 16) == 69800
    assert candidate(n = 500,m = 7) == 89466
    assert candidate(n = 333,m = 77) == 54071
    assert candidate(n = 750,m = 5) == 168375
    assert candidate(n = 200,m = 17) == 17856
    assert candidate(n = 450,m = 20) == 91355
    assert candidate(n = 600,m = 11) == 147630
    assert candidate(n = 800,m = 17) == 282048
    assert candidate(n = 500,m = 25) == 114750
    assert candidate(n = 800,m = 300) == 318600
    assert candidate(n = 100,m = 19) == 4480
    assert candidate(n = 450,m = 30) == 94275
    assert candidate(n = 800,m = 16) == 279600
    assert candidate(n = 200,m = 13) == 16980
    assert candidate(n = 750,m = 29) == 262775
    assert candidate(n = 500,m = 5) == 74750
    assert candidate(n = 200,m = 8) == 14900
    assert candidate(n = 750,m = 42) == 268773
    assert candidate(n = 400,m = 11) == 65548
    assert candidate(n = 900,m = 9) == 314550
    assert candidate(n = 450,m = 23) == 92735
    assert candidate(n = 300,m = 150) == 44250
    assert candidate(n = 420,m = 23) == 80544
    assert candidate(n = 999,m = 7) == 357358
    assert candidate(n = 800,m = 11) == 262584
    assert candidate(n = 900,m = 23) == 369570
    assert candidate(n = 800,m = 25) == 294000
    assert candidate(n = 600,m = 12) == 149700


