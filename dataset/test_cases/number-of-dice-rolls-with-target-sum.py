def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 15,k = 10,target = 100) == 794915145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 10,target = 100) == 794915145: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 6,target = 12) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 6,target = 12) == 125: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 30,target = 500) == 222616187
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 30,target = 500) == 222616187: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 6,target = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 6,target = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 5,target = 30) == 856945
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 5,target = 30) == 856945: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 4,target = 8) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 4,target = 8) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 2,target = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 2,target = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 4,target = 10) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 4,target = 10) == 101: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 6,target = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 6,target = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 2,target = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 2,target = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 4,target = 40) == 83372562
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 4,target = 40) == 83372562: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 10,target = 50) == 374894389
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 10,target = 50) == 374894389: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 5,target = 10) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 5,target = 10) == 121: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 10,target = 15) == 996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 10,target = 15) == 996: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 2,target = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 2,target = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 20,target = 400) == 239696222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 20,target = 400) == 239696222: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 5,target = 25) == 473694
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 5,target = 25) == 473694: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 8,target = 100) == 428096078
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 8,target = 100) == 428096078: {e}')
    
    total += 1
    try:
        result = candidate(n = 26,k = 10,target = 130) == 900662957
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 26,k = 10,target = 130) == 900662957: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,k = 20,target = 250) == 754162082
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,k = 20,target = 250) == 754162082: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 30,target = 800) == 740208408
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 30,target = 800) == 740208408: {e}')
    
    total += 1
    try:
        result = candidate(n = 29,k = 13,target = 385) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29,k = 13,target = 385) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 5,target = 60) == 49360405
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 5,target = 60) == 49360405: {e}')
    
    total += 1
    try:
        result = candidate(n = 27,k = 18,target = 380) == 570408071
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27,k = 18,target = 380) == 570408071: {e}')
    
    total += 1
    try:
        result = candidate(n = 27,k = 11,target = 243) == 976265632
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27,k = 11,target = 243) == 976265632: {e}')
    
    total += 1
    try:
        result = candidate(n = 14,k = 7,target = 98) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,k = 7,target = 98) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 15,target = 120) == 545528539
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 15,target = 120) == 545528539: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 6,target = 100) == 165343714
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 6,target = 100) == 165343714: {e}')
    
    total += 1
    try:
        result = candidate(n = 19,k = 14,target = 260) == 134596
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19,k = 14,target = 260) == 134596: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 8,target = 120) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 8,target = 120) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 5,target = 125) == 699555125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 5,target = 125) == 699555125: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 12,target = 200) == 740079054
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 12,target = 200) == 740079054: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 10,target = 150) == 166392150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 10,target = 150) == 166392150: {e}')
    
    total += 1
    try:
        result = candidate(n = 26,k = 12,target = 200) == 768259128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 26,k = 12,target = 200) == 768259128: {e}')
    
    total += 1
    try:
        result = candidate(n = 17,k = 9,target = 145) == 735471
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17,k = 9,target = 145) == 735471: {e}')
    
    total += 1
    try:
        result = candidate(n = 22,k = 14,target = 280) == 879336869
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22,k = 14,target = 280) == 879336869: {e}')
    
    total += 1
    try:
        result = candidate(n = 27,k = 11,target = 220) == 441656611
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27,k = 11,target = 220) == 441656611: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 10,target = 150) == 793899040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 10,target = 150) == 793899040: {e}')
    
    total += 1
    try:
        result = candidate(n = 16,k = 11,target = 105) == 811426869
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16,k = 11,target = 105) == 811426869: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 10,target = 250) == 128709914
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 10,target = 250) == 128709914: {e}')
    
    total += 1
    try:
        result = candidate(n = 22,k = 9,target = 180) == 44386487
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22,k = 9,target = 180) == 44386487: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,k = 15,target = 350) == 471189138
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,k = 15,target = 350) == 471189138: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 10,target = 150) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 10,target = 150) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 5,target = 90) == 337060208
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 5,target = 90) == 337060208: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 10,target = 150) == 182972231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 10,target = 150) == 182972231: {e}')
    
    total += 1
    try:
        result = candidate(n = 29,k = 25,target = 400) == 266275143
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29,k = 25,target = 400) == 266275143: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 6,target = 150) == 37027173
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 6,target = 150) == 37027173: {e}')
    
    total += 1
    try:
        result = candidate(n = 24,k = 9,target = 155) == 405028518
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24,k = 9,target = 155) == 405028518: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 7,target = 120) == 100947
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 7,target = 120) == 100947: {e}')
    
    total += 1
    try:
        result = candidate(n = 22,k = 7,target = 120) == 404679730
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22,k = 7,target = 120) == 404679730: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 8,target = 120) == 747503719
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 8,target = 120) == 747503719: {e}')
    
    total += 1
    try:
        result = candidate(n = 24,k = 14,target = 160) == 26411763
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24,k = 14,target = 160) == 26411763: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 15,target = 250) == 504797596
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 15,target = 250) == 504797596: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 6,target = 100) == 449826955
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 6,target = 100) == 449826955: {e}')
    
    total += 1
    try:
        result = candidate(n = 24,k = 15,target = 300) == 688942594
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24,k = 15,target = 300) == 688942594: {e}')
    
    total += 1
    try:
        result = candidate(n = 27,k = 11,target = 170) == 11802847
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27,k = 11,target = 170) == 11802847: {e}')
    
    total += 1
    try:
        result = candidate(n = 19,k = 9,target = 125) == 406671426
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19,k = 9,target = 125) == 406671426: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 7,target = 84) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 7,target = 84) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 20,target = 200) == 270319085
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 20,target = 200) == 270319085: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 15,target = 150) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 15,target = 150) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 26,k = 9,target = 180) == 843161626
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 26,k = 9,target = 180) == 843161626: {e}')
    
    total += 1
    try:
        result = candidate(n = 16,k = 6,target = 80) == 248705155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16,k = 6,target = 80) == 248705155: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 3,target = 30) == 8074
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 3,target = 30) == 8074: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 8,target = 150) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 8,target = 150) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 22,k = 10,target = 155) == 612108463
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22,k = 10,target = 155) == 612108463: {e}')
    
    total += 1
    try:
        result = candidate(n = 22,k = 15,target = 180) == 215154082
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22,k = 15,target = 180) == 215154082: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,k = 12,target = 200) == 507319147
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,k = 12,target = 200) == 507319147: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 8,target = 100) == 891516101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 8,target = 100) == 891516101: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,k = 9,target = 252) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,k = 9,target = 252) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 8,target = 160) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 8,target = 160) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 20,target = 350) == 690236765
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 20,target = 350) == 690236765: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 12,target = 150) == 800893074
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 12,target = 150) == 800893074: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 12,target = 75) == 6445237
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 12,target = 75) == 6445237: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 12,target = 360) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 12,target = 360) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 19,k = 13,target = 221) == 611881535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19,k = 13,target = 221) == 611881535: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 20,target = 400) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 20,target = 400) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,k = 6,target = 100) == 333372447
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,k = 6,target = 100) == 333372447: {e}')
    
    total += 1
    try:
        result = candidate(n = 14,k = 7,target = 90) == 203294
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,k = 7,target = 90) == 203294: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 6,target = 120) == 253411631
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 6,target = 120) == 253411631: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 6,target = 100) == 1078497
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 6,target = 100) == 1078497: {e}')
    
    total += 1
    try:
        result = candidate(n = 16,k = 7,target = 80) == 150185177
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16,k = 7,target = 80) == 150185177: {e}')
    
    total += 1
    try:
        result = candidate(n = 29,k = 7,target = 195) == 30259499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29,k = 7,target = 195) == 30259499: {e}')
    
    total += 1
    try:
        result = candidate(n = 27,k = 30,target = 800) == 254186856
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27,k = 30,target = 800) == 254186856: {e}')
    
    total += 1
    try:
        result = candidate(n = 19,k = 25,target = 450) == 359043931
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19,k = 25,target = 450) == 359043931: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 10,target = 150) == 366736536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 10,target = 150) == 366736536: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,k = 12,target = 250) == 782356560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,k = 12,target = 250) == 782356560: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 25,target = 750) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 25,target = 750) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 7,target = 85) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 7,target = 85) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 25,target = 400) == 656098604
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 25,target = 400) == 656098604: {e}')
    
    total += 1
    try:
        result = candidate(n = 22,k = 9,target = 175) == 592474733
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22,k = 9,target = 175) == 592474733: {e}')
    
    total += 1
    try:
        result = candidate(n = 22,k = 8,target = 160) == 781347627
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22,k = 8,target = 160) == 781347627: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,k = 18,target = 450) == 94890353
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,k = 18,target = 450) == 94890353: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 15,target = 350) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 15,target = 350) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 24,k = 18,target = 360) == 517019157
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24,k = 18,target = 360) == 517019157: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 12,target = 250) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 12,target = 250) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 22,k = 15,target = 170) == 332380631
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22,k = 15,target = 170) == 332380631: {e}')
    
    total += 1
    try:
        result = candidate(n = 14,k = 20,target = 180) == 267746915
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,k = 20,target = 180) == 267746915: {e}')
    
    total += 1
    try:
        result = candidate(n = 22,k = 6,target = 132) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22,k = 6,target = 132) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 27,k = 18,target = 350) == 91344166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27,k = 18,target = 350) == 91344166: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 12,target = 100) == 201258020
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 12,target = 100) == 201258020: {e}')
    
    total += 1
    try:
        result = candidate(n = 17,k = 9,target = 130) == 241842734
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17,k = 9,target = 130) == 241842734: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 15,target = 300) == 861212713
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 15,target = 300) == 861212713: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 7,target = 90) == 183069607
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 7,target = 90) == 183069607: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 20,target = 300) == 161591689
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 20,target = 300) == 161591689: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 10,target = 180) == 522663924
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 10,target = 180) == 522663924: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,k = 15,target = 300) == 813819263
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,k = 15,target = 300) == 813819263: {e}')
    
    total += 1
    try:
        result = candidate(n = 22,k = 7,target = 130) == 712806895
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22,k = 7,target = 130) == 712806895: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 20,target = 500) == 541650286
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 20,target = 500) == 541650286: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 15,k = 10,target = 100) == 794915145
    assert candidate(n = 4,k = 6,target = 12) == 125
    assert candidate(n = 30,k = 30,target = 500) == 222616187
    assert candidate(n = 2,k = 6,target = 7) == 6
    assert candidate(n = 10,k = 5,target = 30) == 856945
    assert candidate(n = 3,k = 4,target = 8) == 12
    assert candidate(n = 3,k = 2,target = 5) == 3
    assert candidate(n = 5,k = 4,target = 10) == 101
    assert candidate(n = 1,k = 6,target = 3) == 1
    assert candidate(n = 2,k = 2,target = 3) == 2
    assert candidate(n = 15,k = 4,target = 40) == 83372562
    assert candidate(n = 10,k = 10,target = 50) == 374894389
    assert candidate(n = 5,k = 5,target = 10) == 121
    assert candidate(n = 5,k = 10,target = 15) == 996
    assert candidate(n = 3,k = 2,target = 4) == 3
    assert candidate(n = 25,k = 20,target = 400) == 239696222
    assert candidate(n = 10,k = 5,target = 25) == 473694
    assert candidate(n = 18,k = 8,target = 100) == 428096078
    assert candidate(n = 26,k = 10,target = 130) == 900662957
    assert candidate(n = 28,k = 20,target = 250) == 754162082
    assert candidate(n = 30,k = 30,target = 800) == 740208408
    assert candidate(n = 29,k = 13,target = 385) == 0
    assert candidate(n = 15,k = 5,target = 60) == 49360405
    assert candidate(n = 27,k = 18,target = 380) == 570408071
    assert candidate(n = 27,k = 11,target = 243) == 976265632
    assert candidate(n = 14,k = 7,target = 98) == 1
    assert candidate(n = 12,k = 15,target = 120) == 545528539
    assert candidate(n = 25,k = 6,target = 100) == 165343714
    assert candidate(n = 19,k = 14,target = 260) == 134596
    assert candidate(n = 15,k = 8,target = 120) == 1
    assert candidate(n = 30,k = 5,target = 125) == 699555125
    assert candidate(n = 30,k = 12,target = 200) == 740079054
    assert candidate(n = 25,k = 10,target = 150) == 166392150
    assert candidate(n = 26,k = 12,target = 200) == 768259128
    assert candidate(n = 17,k = 9,target = 145) == 735471
    assert candidate(n = 22,k = 14,target = 280) == 879336869
    assert candidate(n = 27,k = 11,target = 220) == 441656611
    assert candidate(n = 30,k = 10,target = 150) == 793899040
    assert candidate(n = 16,k = 11,target = 105) == 811426869
    assert candidate(n = 30,k = 10,target = 250) == 128709914
    assert candidate(n = 22,k = 9,target = 180) == 44386487
    assert candidate(n = 28,k = 15,target = 350) == 471189138
    assert candidate(n = 15,k = 10,target = 150) == 1
    assert candidate(n = 30,k = 5,target = 90) == 337060208
    assert candidate(n = 18,k = 10,target = 150) == 182972231
    assert candidate(n = 29,k = 25,target = 400) == 266275143
    assert candidate(n = 30,k = 6,target = 150) == 37027173
    assert candidate(n = 24,k = 9,target = 155) == 405028518
    assert candidate(n = 18,k = 7,target = 120) == 100947
    assert candidate(n = 22,k = 7,target = 120) == 404679730
    assert candidate(n = 18,k = 8,target = 120) == 747503719
    assert candidate(n = 24,k = 14,target = 160) == 26411763
    assert candidate(n = 20,k = 15,target = 250) == 504797596
    assert candidate(n = 30,k = 6,target = 100) == 449826955
    assert candidate(n = 24,k = 15,target = 300) == 688942594
    assert candidate(n = 27,k = 11,target = 170) == 11802847
    assert candidate(n = 19,k = 9,target = 125) == 406671426
    assert candidate(n = 12,k = 7,target = 84) == 1
    assert candidate(n = 20,k = 20,target = 200) == 270319085
    assert candidate(n = 10,k = 15,target = 150) == 1
    assert candidate(n = 26,k = 9,target = 180) == 843161626
    assert candidate(n = 16,k = 6,target = 80) == 248705155
    assert candidate(n = 12,k = 3,target = 30) == 8074
    assert candidate(n = 18,k = 8,target = 150) == 0
    assert candidate(n = 22,k = 10,target = 155) == 612108463
    assert candidate(n = 22,k = 15,target = 180) == 215154082
    assert candidate(n = 28,k = 12,target = 200) == 507319147
    assert candidate(n = 20,k = 8,target = 100) == 891516101
    assert candidate(n = 28,k = 9,target = 252) == 1
    assert candidate(n = 20,k = 8,target = 160) == 1
    assert candidate(n = 20,k = 20,target = 350) == 690236765
    assert candidate(n = 25,k = 12,target = 150) == 800893074
    assert candidate(n = 12,k = 12,target = 75) == 6445237
    assert candidate(n = 30,k = 12,target = 360) == 1
    assert candidate(n = 19,k = 13,target = 221) == 611881535
    assert candidate(n = 20,k = 20,target = 400) == 1
    assert candidate(n = 28,k = 6,target = 100) == 333372447
    assert candidate(n = 14,k = 7,target = 90) == 203294
    assert candidate(n = 25,k = 6,target = 120) == 253411631
    assert candidate(n = 18,k = 6,target = 100) == 1078497
    assert candidate(n = 16,k = 7,target = 80) == 150185177
    assert candidate(n = 29,k = 7,target = 195) == 30259499
    assert candidate(n = 27,k = 30,target = 800) == 254186856
    assert candidate(n = 19,k = 25,target = 450) == 359043931
    assert candidate(n = 20,k = 10,target = 150) == 366736536
    assert candidate(n = 28,k = 12,target = 250) == 782356560
    assert candidate(n = 30,k = 25,target = 750) == 1
    assert candidate(n = 12,k = 7,target = 85) == 0
    assert candidate(n = 30,k = 25,target = 400) == 656098604
    assert candidate(n = 22,k = 9,target = 175) == 592474733
    assert candidate(n = 22,k = 8,target = 160) == 781347627
    assert candidate(n = 28,k = 18,target = 450) == 94890353
    assert candidate(n = 20,k = 15,target = 350) == 0
    assert candidate(n = 24,k = 18,target = 360) == 517019157
    assert candidate(n = 18,k = 12,target = 250) == 0
    assert candidate(n = 22,k = 15,target = 170) == 332380631
    assert candidate(n = 14,k = 20,target = 180) == 267746915
    assert candidate(n = 22,k = 6,target = 132) == 1
    assert candidate(n = 27,k = 18,target = 350) == 91344166
    assert candidate(n = 12,k = 12,target = 100) == 201258020
    assert candidate(n = 17,k = 9,target = 130) == 241842734
    assert candidate(n = 25,k = 15,target = 300) == 861212713
    assert candidate(n = 18,k = 7,target = 90) == 183069607
    assert candidate(n = 25,k = 20,target = 300) == 161591689
    assert candidate(n = 20,k = 10,target = 180) == 522663924
    assert candidate(n = 28,k = 15,target = 300) == 813819263
    assert candidate(n = 22,k = 7,target = 130) == 712806895
    assert candidate(n = 30,k = 20,target = 500) == 541650286


