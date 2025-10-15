def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(lo = 1,hi = 10,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 1,hi = 10,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lo = 5,hi = 5,k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 5,hi = 5,k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(lo = 12,hi = 15,k = 2) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 12,hi = 15,k = 2) == 13: {e}')
    
    total += 1
    try:
        result = candidate(lo = 1,hi = 10,k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 1,hi = 10,k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(lo = 10,hi = 20,k = 5) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 10,hi = 20,k = 5) == 13: {e}')
    
    total += 1
    try:
        result = candidate(lo = 7,hi = 11,k = 4) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 7,hi = 11,k = 4) == 7: {e}')
    
    total += 1
    try:
        result = candidate(lo = 10,hi = 20,k = 3) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 10,hi = 20,k = 3) == 20: {e}')
    
    total += 1
    try:
        result = candidate(lo = 1,hi = 10,k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 1,hi = 10,k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(lo = 300,hi = 500,k = 100) == 370
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 300,hi = 500,k = 100) == 370: {e}')
    
    total += 1
    try:
        result = candidate(lo = 100,hi = 200,k = 1) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 100,hi = 200,k = 1) == 128: {e}')
    
    total += 1
    try:
        result = candidate(lo = 300,hi = 700,k = 150) == 613
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 300,hi = 700,k = 150) == 613: {e}')
    
    total += 1
    try:
        result = candidate(lo = 700,hi = 800,k = 18) == 794
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 700,hi = 800,k = 18) == 794: {e}')
    
    total += 1
    try:
        result = candidate(lo = 100,hi = 200,k = 75) == 183
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 100,hi = 200,k = 75) == 183: {e}')
    
    total += 1
    try:
        result = candidate(lo = 1,hi = 100,k = 100) == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 1,hi = 100,k = 100) == 97: {e}')
    
    total += 1
    try:
        result = candidate(lo = 700,hi = 800,k = 50) == 766
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 700,hi = 800,k = 50) == 766: {e}')
    
    total += 1
    try:
        result = candidate(lo = 800,hi = 900,k = 5) == 802
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 800,hi = 900,k = 5) == 802: {e}')
    
    total += 1
    try:
        result = candidate(lo = 900,hi = 1000,k = 50) == 988
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 900,hi = 1000,k = 50) == 988: {e}')
    
    total += 1
    try:
        result = candidate(lo = 600,hi = 800,k = 150) == 756
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 600,hi = 800,k = 150) == 756: {e}')
    
    total += 1
    try:
        result = candidate(lo = 800,hi = 1000,k = 50) == 912
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 800,hi = 1000,k = 50) == 912: {e}')
    
    total += 1
    try:
        result = candidate(lo = 500,hi = 900,k = 100) == 692
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 500,hi = 900,k = 100) == 692: {e}')
    
    total += 1
    try:
        result = candidate(lo = 400,hi = 600,k = 100) == 489
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 400,hi = 600,k = 100) == 489: {e}')
    
    total += 1
    try:
        result = candidate(lo = 400,hi = 700,k = 120) == 418
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 400,hi = 700,k = 120) == 418: {e}')
    
    total += 1
    try:
        result = candidate(lo = 750,hi = 850,k = 50) == 758
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 750,hi = 850,k = 50) == 758: {e}')
    
    total += 1
    try:
        result = candidate(lo = 300,hi = 400,k = 100) == 313
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 300,hi = 400,k = 100) == 313: {e}')
    
    total += 1
    try:
        result = candidate(lo = 5,hi = 25,k = 1) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 5,hi = 25,k = 1) == 8: {e}')
    
    total += 1
    try:
        result = candidate(lo = 300,hi = 350,k = 30) == 338
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 300,hi = 350,k = 30) == 338: {e}')
    
    total += 1
    try:
        result = candidate(lo = 950,hi = 1000,k = 25) == 984
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 950,hi = 1000,k = 25) == 984: {e}')
    
    total += 1
    try:
        result = candidate(lo = 200,hi = 300,k = 1) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 200,hi = 300,k = 1) == 256: {e}')
    
    total += 1
    try:
        result = candidate(lo = 800,hi = 900,k = 50) == 855
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 800,hi = 900,k = 50) == 855: {e}')
    
    total += 1
    try:
        result = candidate(lo = 800,hi = 900,k = 85) == 898
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 800,hi = 900,k = 85) == 898: {e}')
    
    total += 1
    try:
        result = candidate(lo = 500,hi = 600,k = 50) == 509
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 500,hi = 600,k = 50) == 509: {e}')
    
    total += 1
    try:
        result = candidate(lo = 250,hi = 450,k = 150) == 428
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 250,hi = 450,k = 150) == 428: {e}')
    
    total += 1
    try:
        result = candidate(lo = 150,hi = 450,k = 100) == 173
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 150,hi = 450,k = 100) == 173: {e}')
    
    total += 1
    try:
        result = candidate(lo = 300,hi = 350,k = 10) == 309
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 300,hi = 350,k = 10) == 309: {e}')
    
    total += 1
    try:
        result = candidate(lo = 300,hi = 600,k = 150) == 374
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 300,hi = 600,k = 150) == 374: {e}')
    
    total += 1
    try:
        result = candidate(lo = 100,hi = 200,k = 10) == 138
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 100,hi = 200,k = 10) == 138: {e}')
    
    total += 1
    try:
        result = candidate(lo = 400,hi = 600,k = 150) == 486
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 400,hi = 600,k = 150) == 486: {e}')
    
    total += 1
    try:
        result = candidate(lo = 900,hi = 1000,k = 10) == 965
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 900,hi = 1000,k = 10) == 965: {e}')
    
    total += 1
    try:
        result = candidate(lo = 250,hi = 500,k = 100) == 312
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 250,hi = 500,k = 100) == 312: {e}')
    
    total += 1
    try:
        result = candidate(lo = 300,hi = 400,k = 50) == 367
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 300,hi = 400,k = 50) == 367: {e}')
    
    total += 1
    try:
        result = candidate(lo = 500,hi = 1000,k = 250) == 658
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 500,hi = 1000,k = 250) == 658: {e}')
    
    total += 1
    try:
        result = candidate(lo = 300,hi = 350,k = 25) == 315
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 300,hi = 350,k = 25) == 315: {e}')
    
    total += 1
    try:
        result = candidate(lo = 200,hi = 300,k = 75) == 242
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 200,hi = 300,k = 75) == 242: {e}')
    
    total += 1
    try:
        result = candidate(lo = 50,hi = 150,k = 25) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 50,hi = 150,k = 25) == 56: {e}')
    
    total += 1
    try:
        result = candidate(lo = 250,hi = 350,k = 100) == 313
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 250,hi = 350,k = 100) == 313: {e}')
    
    total += 1
    try:
        result = candidate(lo = 50,hi = 75,k = 1) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 50,hi = 75,k = 1) == 64: {e}')
    
    total += 1
    try:
        result = candidate(lo = 500,hi = 1000,k = 150) == 943
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 500,hi = 1000,k = 150) == 943: {e}')
    
    total += 1
    try:
        result = candidate(lo = 100,hi = 800,k = 200) == 547
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 100,hi = 800,k = 200) == 547: {e}')
    
    total += 1
    try:
        result = candidate(lo = 100,hi = 500,k = 30) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 100,hi = 500,k = 30) == 150: {e}')
    
    total += 1
    try:
        result = candidate(lo = 1,hi = 500,k = 250) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 1,hi = 500,k = 250) == 465: {e}')
    
    total += 1
    try:
        result = candidate(lo = 400,hi = 600,k = 120) == 590
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 400,hi = 600,k = 120) == 590: {e}')
    
    total += 1
    try:
        result = candidate(lo = 1,hi = 100,k = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 1,hi = 100,k = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(lo = 200,hi = 300,k = 50) == 271
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 200,hi = 300,k = 50) == 271: {e}')
    
    total += 1
    try:
        result = candidate(lo = 250,hi = 750,k = 250) == 741
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 250,hi = 750,k = 250) == 741: {e}')
    
    total += 1
    try:
        result = candidate(lo = 300,hi = 400,k = 5) == 384
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 300,hi = 400,k = 5) == 384: {e}')
    
    total += 1
    try:
        result = candidate(lo = 400,hi = 600,k = 200) == 487
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 400,hi = 600,k = 200) == 487: {e}')
    
    total += 1
    try:
        result = candidate(lo = 1,hi = 500,k = 150) == 163
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 1,hi = 500,k = 150) == 163: {e}')
    
    total += 1
    try:
        result = candidate(lo = 150,hi = 250,k = 20) == 234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 150,hi = 250,k = 20) == 234: {e}')
    
    total += 1
    try:
        result = candidate(lo = 800,hi = 1000,k = 200) == 937
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 800,hi = 1000,k = 200) == 937: {e}')
    
    total += 1
    try:
        result = candidate(lo = 1,hi = 1000,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 1,hi = 1000,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lo = 999,hi = 1000,k = 1) == 999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 999,hi = 1000,k = 1) == 999: {e}')
    
    total += 1
    try:
        result = candidate(lo = 1,hi = 1000,k = 500) == 606
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 1,hi = 1000,k = 500) == 606: {e}')
    
    total += 1
    try:
        result = candidate(lo = 200,hi = 300,k = 100) == 231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 200,hi = 300,k = 100) == 231: {e}')
    
    total += 1
    try:
        result = candidate(lo = 200,hi = 300,k = 10) == 280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 200,hi = 300,k = 10) == 280: {e}')
    
    total += 1
    try:
        result = candidate(lo = 300,hi = 700,k = 250) == 699
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 300,hi = 700,k = 250) == 699: {e}')
    
    total += 1
    try:
        result = candidate(lo = 250,hi = 400,k = 100) == 263
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 250,hi = 400,k = 100) == 263: {e}')
    
    total += 1
    try:
        result = candidate(lo = 750,hi = 850,k = 30) == 813
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 750,hi = 850,k = 30) == 813: {e}')
    
    total += 1
    try:
        result = candidate(lo = 100,hi = 300,k = 150) == 242
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 100,hi = 300,k = 150) == 242: {e}')
    
    total += 1
    try:
        result = candidate(lo = 25,hi = 75,k = 25) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 25,hi = 75,k = 25) == 36: {e}')
    
    total += 1
    try:
        result = candidate(lo = 400,hi = 500,k = 100) == 487
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 400,hi = 500,k = 100) == 487: {e}')
    
    total += 1
    try:
        result = candidate(lo = 800,hi = 900,k = 80) == 874
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 800,hi = 900,k = 80) == 874: {e}')
    
    total += 1
    try:
        result = candidate(lo = 50,hi = 75,k = 25) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 50,hi = 75,k = 25) == 55: {e}')
    
    total += 1
    try:
        result = candidate(lo = 150,hi = 300,k = 75) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 150,hi = 300,k = 75) == 210: {e}')
    
    total += 1
    try:
        result = candidate(lo = 1,hi = 100,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 1,hi = 100,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lo = 500,hi = 1000,k = 300) == 754
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 500,hi = 1000,k = 300) == 754: {e}')
    
    total += 1
    try:
        result = candidate(lo = 600,hi = 700,k = 20) == 663
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 600,hi = 700,k = 20) == 663: {e}')
    
    total += 1
    try:
        result = candidate(lo = 800,hi = 900,k = 100) == 889
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 800,hi = 900,k = 100) == 889: {e}')
    
    total += 1
    try:
        result = candidate(lo = 200,hi = 400,k = 150) == 243
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 200,hi = 400,k = 150) == 243: {e}')
    
    total += 1
    try:
        result = candidate(lo = 100,hi = 200,k = 100) == 129
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 100,hi = 200,k = 100) == 129: {e}')
    
    total += 1
    try:
        result = candidate(lo = 100,hi = 200,k = 50) == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 100,hi = 200,k = 50) == 114: {e}')
    
    total += 1
    try:
        result = candidate(lo = 800,hi = 900,k = 25) == 882
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 800,hi = 900,k = 25) == 882: {e}')
    
    total += 1
    try:
        result = candidate(lo = 1,hi = 100,k = 50) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 1,hi = 100,k = 50) == 9: {e}')
    
    total += 1
    try:
        result = candidate(lo = 500,hi = 600,k = 25) == 538
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 500,hi = 600,k = 25) == 538: {e}')
    
    total += 1
    try:
        result = candidate(lo = 50,hi = 150,k = 50) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 50,hi = 150,k = 50) == 66: {e}')
    
    total += 1
    try:
        result = candidate(lo = 1000,hi = 1000,k = 1) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 1000,hi = 1000,k = 1) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(lo = 1,hi = 100,k = 75) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 1,hi = 100,k = 75) == 67: {e}')
    
    total += 1
    try:
        result = candidate(lo = 900,hi = 999,k = 15) == 985
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 900,hi = 999,k = 15) == 985: {e}')
    
    total += 1
    try:
        result = candidate(lo = 2,hi = 10,k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 2,hi = 10,k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(lo = 1,hi = 1000,k = 750) == 322
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 1,hi = 1000,k = 750) == 322: {e}')
    
    total += 1
    try:
        result = candidate(lo = 600,hi = 900,k = 150) == 718
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 600,hi = 900,k = 150) == 718: {e}')
    
    total += 1
    try:
        result = candidate(lo = 50,hi = 100,k = 15) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 50,hi = 100,k = 15) == 93: {e}')
    
    total += 1
    try:
        result = candidate(lo = 1,hi = 1,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 1,hi = 1,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(lo = 600,hi = 800,k = 100) == 676
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(lo = 600,hi = 800,k = 100) == 676: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(lo = 1,hi = 10,k = 1) == 1
    assert candidate(lo = 5,hi = 5,k = 1) == 5
    assert candidate(lo = 12,hi = 15,k = 2) == 13
    assert candidate(lo = 1,hi = 10,k = 5) == 5
    assert candidate(lo = 10,hi = 20,k = 5) == 13
    assert candidate(lo = 7,hi = 11,k = 4) == 7
    assert candidate(lo = 10,hi = 20,k = 3) == 20
    assert candidate(lo = 1,hi = 10,k = 3) == 4
    assert candidate(lo = 300,hi = 500,k = 100) == 370
    assert candidate(lo = 100,hi = 200,k = 1) == 128
    assert candidate(lo = 300,hi = 700,k = 150) == 613
    assert candidate(lo = 700,hi = 800,k = 18) == 794
    assert candidate(lo = 100,hi = 200,k = 75) == 183
    assert candidate(lo = 1,hi = 100,k = 100) == 97
    assert candidate(lo = 700,hi = 800,k = 50) == 766
    assert candidate(lo = 800,hi = 900,k = 5) == 802
    assert candidate(lo = 900,hi = 1000,k = 50) == 988
    assert candidate(lo = 600,hi = 800,k = 150) == 756
    assert candidate(lo = 800,hi = 1000,k = 50) == 912
    assert candidate(lo = 500,hi = 900,k = 100) == 692
    assert candidate(lo = 400,hi = 600,k = 100) == 489
    assert candidate(lo = 400,hi = 700,k = 120) == 418
    assert candidate(lo = 750,hi = 850,k = 50) == 758
    assert candidate(lo = 300,hi = 400,k = 100) == 313
    assert candidate(lo = 5,hi = 25,k = 1) == 8
    assert candidate(lo = 300,hi = 350,k = 30) == 338
    assert candidate(lo = 950,hi = 1000,k = 25) == 984
    assert candidate(lo = 200,hi = 300,k = 1) == 256
    assert candidate(lo = 800,hi = 900,k = 50) == 855
    assert candidate(lo = 800,hi = 900,k = 85) == 898
    assert candidate(lo = 500,hi = 600,k = 50) == 509
    assert candidate(lo = 250,hi = 450,k = 150) == 428
    assert candidate(lo = 150,hi = 450,k = 100) == 173
    assert candidate(lo = 300,hi = 350,k = 10) == 309
    assert candidate(lo = 300,hi = 600,k = 150) == 374
    assert candidate(lo = 100,hi = 200,k = 10) == 138
    assert candidate(lo = 400,hi = 600,k = 150) == 486
    assert candidate(lo = 900,hi = 1000,k = 10) == 965
    assert candidate(lo = 250,hi = 500,k = 100) == 312
    assert candidate(lo = 300,hi = 400,k = 50) == 367
    assert candidate(lo = 500,hi = 1000,k = 250) == 658
    assert candidate(lo = 300,hi = 350,k = 25) == 315
    assert candidate(lo = 200,hi = 300,k = 75) == 242
    assert candidate(lo = 50,hi = 150,k = 25) == 56
    assert candidate(lo = 250,hi = 350,k = 100) == 313
    assert candidate(lo = 50,hi = 75,k = 1) == 64
    assert candidate(lo = 500,hi = 1000,k = 150) == 943
    assert candidate(lo = 100,hi = 800,k = 200) == 547
    assert candidate(lo = 100,hi = 500,k = 30) == 150
    assert candidate(lo = 1,hi = 500,k = 250) == 465
    assert candidate(lo = 400,hi = 600,k = 120) == 590
    assert candidate(lo = 1,hi = 100,k = 10) == 3
    assert candidate(lo = 200,hi = 300,k = 50) == 271
    assert candidate(lo = 250,hi = 750,k = 250) == 741
    assert candidate(lo = 300,hi = 400,k = 5) == 384
    assert candidate(lo = 400,hi = 600,k = 200) == 487
    assert candidate(lo = 1,hi = 500,k = 150) == 163
    assert candidate(lo = 150,hi = 250,k = 20) == 234
    assert candidate(lo = 800,hi = 1000,k = 200) == 937
    assert candidate(lo = 1,hi = 1000,k = 1) == 1
    assert candidate(lo = 999,hi = 1000,k = 1) == 999
    assert candidate(lo = 1,hi = 1000,k = 500) == 606
    assert candidate(lo = 200,hi = 300,k = 100) == 231
    assert candidate(lo = 200,hi = 300,k = 10) == 280
    assert candidate(lo = 300,hi = 700,k = 250) == 699
    assert candidate(lo = 250,hi = 400,k = 100) == 263
    assert candidate(lo = 750,hi = 850,k = 30) == 813
    assert candidate(lo = 100,hi = 300,k = 150) == 242
    assert candidate(lo = 25,hi = 75,k = 25) == 36
    assert candidate(lo = 400,hi = 500,k = 100) == 487
    assert candidate(lo = 800,hi = 900,k = 80) == 874
    assert candidate(lo = 50,hi = 75,k = 25) == 55
    assert candidate(lo = 150,hi = 300,k = 75) == 210
    assert candidate(lo = 1,hi = 100,k = 1) == 1
    assert candidate(lo = 500,hi = 1000,k = 300) == 754
    assert candidate(lo = 600,hi = 700,k = 20) == 663
    assert candidate(lo = 800,hi = 900,k = 100) == 889
    assert candidate(lo = 200,hi = 400,k = 150) == 243
    assert candidate(lo = 100,hi = 200,k = 100) == 129
    assert candidate(lo = 100,hi = 200,k = 50) == 114
    assert candidate(lo = 800,hi = 900,k = 25) == 882
    assert candidate(lo = 1,hi = 100,k = 50) == 9
    assert candidate(lo = 500,hi = 600,k = 25) == 538
    assert candidate(lo = 50,hi = 150,k = 50) == 66
    assert candidate(lo = 1000,hi = 1000,k = 1) == 1000
    assert candidate(lo = 1,hi = 100,k = 75) == 67
    assert candidate(lo = 900,hi = 999,k = 15) == 985
    assert candidate(lo = 2,hi = 10,k = 5) == 10
    assert candidate(lo = 1,hi = 1000,k = 750) == 322
    assert candidate(lo = 600,hi = 900,k = 150) == 718
    assert candidate(lo = 50,hi = 100,k = 15) == 93
    assert candidate(lo = 1,hi = 1,k = 1) == 1
    assert candidate(lo = 600,hi = 800,k = 100) == 676


