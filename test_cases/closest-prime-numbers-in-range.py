def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(left = 500,right = 550) == [521, 523]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 500,right = 550) == [521, 523]: {e}')
    
    total += 1
    try:
        result = candidate(left = 1000,right = 1100) == [1019, 1021]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1000,right = 1100) == [1019, 1021]: {e}')
    
    total += 1
    try:
        result = candidate(left = 10000,right = 10020) == [10007, 10009]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 10000,right = 10020) == [10007, 10009]: {e}')
    
    total += 1
    try:
        result = candidate(left = 1000,right = 1010) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1000,right = 1010) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(left = 999983,right = 999999) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999983,right = 999999) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(left = 20,right = 30) == [23, 29]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 20,right = 30) == [23, 29]: {e}')
    
    total += 1
    try:
        result = candidate(left = 100,right = 110) == [101, 103]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 100,right = 110) == [101, 103]: {e}')
    
    total += 1
    try:
        result = candidate(left = 500,right = 600) == [521, 523]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 500,right = 600) == [521, 523]: {e}')
    
    total += 1
    try:
        result = candidate(left = 1,right = 10) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1,right = 10) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(left = 7,right = 11) == [7, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 7,right = 11) == [7, 11]: {e}')
    
    total += 1
    try:
        result = candidate(left = 500,right = 520) == [503, 509]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 500,right = 520) == [503, 509]: {e}')
    
    total += 1
    try:
        result = candidate(left = 30,right = 50) == [41, 43]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 30,right = 50) == [41, 43]: {e}')
    
    total += 1
    try:
        result = candidate(left = 5000,right = 6000) == [5009, 5011]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 5000,right = 6000) == [5009, 5011]: {e}')
    
    total += 1
    try:
        result = candidate(left = 100000,right = 100010) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 100000,right = 100010) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(left = 500,right = 510) == [503, 509]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 500,right = 510) == [503, 509]: {e}')
    
    total += 1
    try:
        result = candidate(left = 1000,right = 1020) == [1009, 1013]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1000,right = 1020) == [1009, 1013]: {e}')
    
    total += 1
    try:
        result = candidate(left = 100000,right = 100020) == [100003, 100019]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 100000,right = 100020) == [100003, 100019]: {e}')
    
    total += 1
    try:
        result = candidate(left = 500000,right = 500010) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 500000,right = 500010) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(left = 999950,right = 1000000) == [999959, 999961]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999950,right = 1000000) == [999959, 999961]: {e}')
    
    total += 1
    try:
        result = candidate(left = 10000,right = 10010) == [10007, 10009]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 10000,right = 10010) == [10007, 10009]: {e}')
    
    total += 1
    try:
        result = candidate(left = 4,right = 6) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 4,right = 6) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(left = 104743,right = 104759) == [104743, 104759]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 104743,right = 104759) == [104743, 104759]: {e}')
    
    total += 1
    try:
        result = candidate(left = 1,right = 1) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1,right = 1) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(left = 999900,right = 1000000) == [999959, 999961]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999900,right = 1000000) == [999959, 999961]: {e}')
    
    total += 1
    try:
        result = candidate(left = 10,right = 19) == [11, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 10,right = 19) == [11, 13]: {e}')
    
    total += 1
    try:
        result = candidate(left = 5000,right = 5500) == [5009, 5011]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 5000,right = 5500) == [5009, 5011]: {e}')
    
    total += 1
    try:
        result = candidate(left = 100000,right = 100100) == [100043, 100049]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 100000,right = 100100) == [100043, 100049]: {e}')
    
    total += 1
    try:
        result = candidate(left = 999990,right = 1000000) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999990,right = 1000000) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(left = 100000,right = 100001) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 100000,right = 100001) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(left = 800000,right = 810000) == [800117, 800119]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 800000,right = 810000) == [800117, 800119]: {e}')
    
    total += 1
    try:
        result = candidate(left = 500000,right = 510000) == [500111, 500113]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 500000,right = 510000) == [500111, 500113]: {e}')
    
    total += 1
    try:
        result = candidate(left = 200000,right = 210000) == [200381, 200383]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 200000,right = 210000) == [200381, 200383]: {e}')
    
    total += 1
    try:
        result = candidate(left = 1,right = 29) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1,right = 29) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(left = 999979,right = 1000037) == [999979, 999983]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999979,right = 1000037) == [999979, 999983]: {e}')
    
    total += 1
    try:
        result = candidate(left = 1000000,right = 1000010) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1000000,right = 1000010) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(left = 5000,right = 5010) == [5003, 5009]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 5000,right = 5010) == [5003, 5009]: {e}')
    
    total += 1
    try:
        result = candidate(left = 300000,right = 310000) == [300149, 300151]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 300000,right = 310000) == [300149, 300151]: {e}')
    
    total += 1
    try:
        result = candidate(left = 104740,right = 104760) == [104743, 104759]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 104740,right = 104760) == [104743, 104759]: {e}')
    
    total += 1
    try:
        result = candidate(left = 100000,right = 100050) == [100043, 100049]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 100000,right = 100050) == [100043, 100049]: {e}')
    
    total += 1
    try:
        result = candidate(left = 140000,right = 150000) == [140069, 140071]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 140000,right = 150000) == [140069, 140071]: {e}')
    
    total += 1
    try:
        result = candidate(left = 800,right = 850) == [809, 811]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 800,right = 850) == [809, 811]: {e}')
    
    total += 1
    try:
        result = candidate(left = 1000000,right = 1000006) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1000000,right = 1000006) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(left = 541,right = 547) == [541, 547]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 541,right = 547) == [541, 547]: {e}')
    
    total += 1
    try:
        result = candidate(left = 1487,right = 1600) == [1487, 1489]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1487,right = 1600) == [1487, 1489]: {e}')
    
    total += 1
    try:
        result = candidate(left = 700000,right = 700100) == [700079, 700081]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 700000,right = 700100) == [700079, 700081]: {e}')
    
    total += 1
    try:
        result = candidate(left = 100,right = 200) == [101, 103]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 100,right = 200) == [101, 103]: {e}')
    
    total += 1
    try:
        result = candidate(left = 50000,right = 50100) == [50021, 50023]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 50000,right = 50100) == [50021, 50023]: {e}')
    
    total += 1
    try:
        result = candidate(left = 999000,right = 999100) == [999023, 999029]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999000,right = 999100) == [999023, 999029]: {e}')
    
    total += 1
    try:
        result = candidate(left = 200000,right = 200100) == [200029, 200033]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 200000,right = 200100) == [200029, 200033]: {e}')
    
    total += 1
    try:
        result = candidate(left = 999983,right = 999983) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999983,right = 999983) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(left = 999950,right = 1000050) == [999959, 999961]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999950,right = 1000050) == [999959, 999961]: {e}')
    
    total += 1
    try:
        result = candidate(left = 300000,right = 300050) == [300017, 300023]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 300000,right = 300050) == [300017, 300023]: {e}')
    
    total += 1
    try:
        result = candidate(left = 100000,right = 101000) == [100151, 100153]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 100000,right = 101000) == [100151, 100153]: {e}')
    
    total += 1
    try:
        result = candidate(left = 50000,right = 51000) == [50021, 50023]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 50000,right = 51000) == [50021, 50023]: {e}')
    
    total += 1
    try:
        result = candidate(left = 600000,right = 600010) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 600000,right = 600010) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(left = 200000,right = 201000) == [200381, 200383]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 200000,right = 201000) == [200381, 200383]: {e}')
    
    total += 1
    try:
        result = candidate(left = 14,right = 16) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 14,right = 16) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(left = 900000,right = 910000) == [900089, 900091]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 900000,right = 910000) == [900089, 900091]: {e}')
    
    total += 1
    try:
        result = candidate(left = 10000,right = 10050) == [10007, 10009]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 10000,right = 10050) == [10007, 10009]: {e}')
    
    total += 1
    try:
        result = candidate(left = 999983,right = 1000033) == [999983, 1000003]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999983,right = 1000033) == [999983, 1000003]: {e}')
    
    total += 1
    try:
        result = candidate(left = 1,right = 100) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1,right = 100) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(left = 3000,right = 3010) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 3000,right = 3010) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(left = 600000,right = 600100) == [600071, 600073]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 600000,right = 600100) == [600071, 600073]: {e}')
    
    total += 1
    try:
        result = candidate(left = 987654,right = 987700) == [987659, 987697]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 987654,right = 987700) == [987659, 987697]: {e}')
    
    total += 1
    try:
        result = candidate(left = 123456,right = 123556) == [123491, 123493]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 123456,right = 123556) == [123491, 123493]: {e}')
    
    total += 1
    try:
        result = candidate(left = 2,right = 3) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 2,right = 3) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(left = 770000,right = 770100) == [770039, 770041]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 770000,right = 770100) == [770039, 770041]: {e}')
    
    total += 1
    try:
        result = candidate(left = 100000,right = 110000) == [100151, 100153]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 100000,right = 110000) == [100151, 100153]: {e}')
    
    total += 1
    try:
        result = candidate(left = 5000,right = 5100) == [5009, 5011]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 5000,right = 5100) == [5009, 5011]: {e}')
    
    total += 1
    try:
        result = candidate(left = 800000,right = 800100) == [800053, 800057]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 800000,right = 800100) == [800053, 800057]: {e}')
    
    total += 1
    try:
        result = candidate(left = 2,right = 5) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 2,right = 5) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(left = 1000000,right = 1000050) == [1000037, 1000039]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1000000,right = 1000050) == [1000037, 1000039]: {e}')
    
    total += 1
    try:
        result = candidate(left = 14,right = 20) == [17, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 14,right = 20) == [17, 19]: {e}')
    
    total += 1
    try:
        result = candidate(left = 50000,right = 50010) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 50000,right = 50010) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(left = 345678,right = 345778) == [345731, 345733]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 345678,right = 345778) == [345731, 345733]: {e}')
    
    total += 1
    try:
        result = candidate(left = 654321,right = 654421) == [654343, 654349]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 654321,right = 654421) == [654343, 654349]: {e}')
    
    total += 1
    try:
        result = candidate(left = 200000,right = 200050) == [200029, 200033]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 200000,right = 200050) == [200029, 200033]: {e}')
    
    total += 1
    try:
        result = candidate(left = 999990,right = 999998) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999990,right = 999998) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(left = 300000,right = 300100) == [300017, 300023]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 300000,right = 300100) == [300017, 300023]: {e}')
    
    total += 1
    try:
        result = candidate(left = 500000,right = 500100) == [500029, 500041]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 500000,right = 500100) == [500029, 500041]: {e}')
    
    total += 1
    try:
        result = candidate(left = 100000,right = 100500) == [100151, 100153]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 100000,right = 100500) == [100151, 100153]: {e}')
    
    total += 1
    try:
        result = candidate(left = 987654,right = 987754) == [987697, 987713]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 987654,right = 987754) == [987697, 987713]: {e}')
    
    total += 1
    try:
        result = candidate(left = 1,right = 1000000) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1,right = 1000000) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(left = 700000,right = 710000) == [700079, 700081]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 700000,right = 710000) == [700079, 700081]: {e}')
    
    total += 1
    try:
        result = candidate(left = 950,right = 1000) == [967, 971]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 950,right = 1000) == [967, 971]: {e}')
    
    total += 1
    try:
        result = candidate(left = 2,right = 2) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 2,right = 2) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(left = 500000,right = 501000) == [500111, 500113]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 500000,right = 501000) == [500111, 500113]: {e}')
    
    total += 1
    try:
        result = candidate(left = 560030,right = 560050) == [560039, 560047]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 560030,right = 560050) == [560039, 560047]: {e}')
    
    total += 1
    try:
        result = candidate(left = 3,right = 5) == [3, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 3,right = 5) == [3, 5]: {e}')
    
    total += 1
    try:
        result = candidate(left = 800000,right = 800200) == [800117, 800119]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 800000,right = 800200) == [800117, 800119]: {e}')
    
    total += 1
    try:
        result = candidate(left = 200,right = 300) == [227, 229]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 200,right = 300) == [227, 229]: {e}')
    
    total += 1
    try:
        result = candidate(left = 999990,right = 1000010) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999990,right = 1000010) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(left = 1487,right = 1601) == [1487, 1489]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1487,right = 1601) == [1487, 1489]: {e}')
    
    total += 1
    try:
        result = candidate(left = 1000000,right = 1000100) == [1000037, 1000039]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1000000,right = 1000100) == [1000037, 1000039]: {e}')
    
    total += 1
    try:
        result = candidate(left = 150000,right = 150100) == [150089, 150091]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 150000,right = 150100) == [150089, 150091]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(left = 500,right = 550) == [521, 523]
    assert candidate(left = 1000,right = 1100) == [1019, 1021]
    assert candidate(left = 10000,right = 10020) == [10007, 10009]
    assert candidate(left = 1000,right = 1010) == [-1, -1]
    assert candidate(left = 999983,right = 999999) == [-1, -1]
    assert candidate(left = 20,right = 30) == [23, 29]
    assert candidate(left = 100,right = 110) == [101, 103]
    assert candidate(left = 500,right = 600) == [521, 523]
    assert candidate(left = 1,right = 10) == [2, 3]
    assert candidate(left = 7,right = 11) == [7, 11]
    assert candidate(left = 500,right = 520) == [503, 509]
    assert candidate(left = 30,right = 50) == [41, 43]
    assert candidate(left = 5000,right = 6000) == [5009, 5011]
    assert candidate(left = 100000,right = 100010) == [-1, -1]
    assert candidate(left = 500,right = 510) == [503, 509]
    assert candidate(left = 1000,right = 1020) == [1009, 1013]
    assert candidate(left = 100000,right = 100020) == [100003, 100019]
    assert candidate(left = 500000,right = 500010) == [-1, -1]
    assert candidate(left = 999950,right = 1000000) == [999959, 999961]
    assert candidate(left = 10000,right = 10010) == [10007, 10009]
    assert candidate(left = 4,right = 6) == [-1, -1]
    assert candidate(left = 104743,right = 104759) == [104743, 104759]
    assert candidate(left = 1,right = 1) == [-1, -1]
    assert candidate(left = 999900,right = 1000000) == [999959, 999961]
    assert candidate(left = 10,right = 19) == [11, 13]
    assert candidate(left = 5000,right = 5500) == [5009, 5011]
    assert candidate(left = 100000,right = 100100) == [100043, 100049]
    assert candidate(left = 999990,right = 1000000) == [-1, -1]
    assert candidate(left = 100000,right = 100001) == [-1, -1]
    assert candidate(left = 800000,right = 810000) == [800117, 800119]
    assert candidate(left = 500000,right = 510000) == [500111, 500113]
    assert candidate(left = 200000,right = 210000) == [200381, 200383]
    assert candidate(left = 1,right = 29) == [2, 3]
    assert candidate(left = 999979,right = 1000037) == [999979, 999983]
    assert candidate(left = 1000000,right = 1000010) == [-1, -1]
    assert candidate(left = 5000,right = 5010) == [5003, 5009]
    assert candidate(left = 300000,right = 310000) == [300149, 300151]
    assert candidate(left = 104740,right = 104760) == [104743, 104759]
    assert candidate(left = 100000,right = 100050) == [100043, 100049]
    assert candidate(left = 140000,right = 150000) == [140069, 140071]
    assert candidate(left = 800,right = 850) == [809, 811]
    assert candidate(left = 1000000,right = 1000006) == [-1, -1]
    assert candidate(left = 541,right = 547) == [541, 547]
    assert candidate(left = 1487,right = 1600) == [1487, 1489]
    assert candidate(left = 700000,right = 700100) == [700079, 700081]
    assert candidate(left = 100,right = 200) == [101, 103]
    assert candidate(left = 50000,right = 50100) == [50021, 50023]
    assert candidate(left = 999000,right = 999100) == [999023, 999029]
    assert candidate(left = 200000,right = 200100) == [200029, 200033]
    assert candidate(left = 999983,right = 999983) == [-1, -1]
    assert candidate(left = 999950,right = 1000050) == [999959, 999961]
    assert candidate(left = 300000,right = 300050) == [300017, 300023]
    assert candidate(left = 100000,right = 101000) == [100151, 100153]
    assert candidate(left = 50000,right = 51000) == [50021, 50023]
    assert candidate(left = 600000,right = 600010) == [-1, -1]
    assert candidate(left = 200000,right = 201000) == [200381, 200383]
    assert candidate(left = 14,right = 16) == [-1, -1]
    assert candidate(left = 900000,right = 910000) == [900089, 900091]
    assert candidate(left = 10000,right = 10050) == [10007, 10009]
    assert candidate(left = 999983,right = 1000033) == [999983, 1000003]
    assert candidate(left = 1,right = 100) == [2, 3]
    assert candidate(left = 3000,right = 3010) == [-1, -1]
    assert candidate(left = 600000,right = 600100) == [600071, 600073]
    assert candidate(left = 987654,right = 987700) == [987659, 987697]
    assert candidate(left = 123456,right = 123556) == [123491, 123493]
    assert candidate(left = 2,right = 3) == [2, 3]
    assert candidate(left = 770000,right = 770100) == [770039, 770041]
    assert candidate(left = 100000,right = 110000) == [100151, 100153]
    assert candidate(left = 5000,right = 5100) == [5009, 5011]
    assert candidate(left = 800000,right = 800100) == [800053, 800057]
    assert candidate(left = 2,right = 5) == [2, 3]
    assert candidate(left = 1000000,right = 1000050) == [1000037, 1000039]
    assert candidate(left = 14,right = 20) == [17, 19]
    assert candidate(left = 50000,right = 50010) == [-1, -1]
    assert candidate(left = 345678,right = 345778) == [345731, 345733]
    assert candidate(left = 654321,right = 654421) == [654343, 654349]
    assert candidate(left = 200000,right = 200050) == [200029, 200033]
    assert candidate(left = 999990,right = 999998) == [-1, -1]
    assert candidate(left = 300000,right = 300100) == [300017, 300023]
    assert candidate(left = 500000,right = 500100) == [500029, 500041]
    assert candidate(left = 100000,right = 100500) == [100151, 100153]
    assert candidate(left = 987654,right = 987754) == [987697, 987713]
    assert candidate(left = 1,right = 1000000) == [2, 3]
    assert candidate(left = 700000,right = 710000) == [700079, 700081]
    assert candidate(left = 950,right = 1000) == [967, 971]
    assert candidate(left = 2,right = 2) == [-1, -1]
    assert candidate(left = 500000,right = 501000) == [500111, 500113]
    assert candidate(left = 560030,right = 560050) == [560039, 560047]
    assert candidate(left = 3,right = 5) == [3, 5]
    assert candidate(left = 800000,right = 800200) == [800117, 800119]
    assert candidate(left = 200,right = 300) == [227, 229]
    assert candidate(left = 999990,right = 1000010) == [-1, -1]
    assert candidate(left = 1487,right = 1601) == [1487, 1489]
    assert candidate(left = 1000000,right = 1000100) == [1000037, 1000039]
    assert candidate(left = 150000,right = 150100) == [150089, 150091]


