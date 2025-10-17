def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 101) == [2, 99]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101) == [2, 99]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1010) == [11, 999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1010) == [11, 999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == [2, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == [2, 9]: {e}')
    
    total += 1
    try:
        result = candidate(n = 104) == [5, 99]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 104) == [5, 99]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1001) == [2, 999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1001) == [2, 999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999) == [1, 9998]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999) == [1, 9998]: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == [1, 99]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == [1, 99]: {e}')
    
    total += 1
    try:
        result = candidate(n = 210) == [11, 199]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 210) == [11, 199]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9801) == [2, 9799]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9801) == [2, 9799]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2345) == [1, 2344]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2345) == [1, 2344]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2100) == [111, 1989]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2100) == [111, 1989]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1111) == [112, 999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111) == [112, 999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10606) == [611, 9995]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10606) == [611, 9995]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8888) == [1, 8887]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8888) == [1, 8887]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == [1, 999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == [1, 999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 43) == [1, 42]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 43) == [1, 42]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10202) == [211, 9991]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10202) == [211, 9991]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1357) == [1, 1356]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1357) == [1, 1356]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10001) == [2, 9999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10001) == [2, 9999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 32109) == [111, 31998]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32109) == [111, 31998]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6789) == [1, 6788]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6789) == [1, 6788]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6005) == [6, 5999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6005) == [6, 5999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8181) == [2, 8179]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8181) == [2, 8179]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2468) == [1, 2467]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2468) == [1, 2467]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2048) == [49, 1999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2048) == [49, 1999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == [1, 998]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == [1, 998]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3030) == [31, 2999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3030) == [31, 2999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9012) == [13, 8999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9012) == [13, 8999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 87654) == [1, 87653]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 87654) == [1, 87653]: {e}')
    
    total += 1
    try:
        result = candidate(n = 43210) == [11, 43199]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 43210) == [11, 43199]: {e}')
    
    total += 1
    try:
        result = candidate(n = 54321) == [2, 54319]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 54321) == [2, 54319]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9090) == [91, 8999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9090) == [91, 8999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 65) == [1, 64]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65) == [1, 64]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345) == [1, 12344]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345) == [1, 12344]: {e}')
    
    total += 1
    try:
        result = candidate(n = 21) == [2, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21) == [2, 19]: {e}')
    
    total += 1
    try:
        result = candidate(n = 432) == [1, 431]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 432) == [1, 431]: {e}')
    
    total += 1
    try:
        result = candidate(n = 543) == [1, 542]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 543) == [1, 542]: {e}')
    
    total += 1
    try:
        result = candidate(n = 87) == [1, 86]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 87) == [1, 86]: {e}')
    
    total += 1
    try:
        result = candidate(n = 98) == [1, 97]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98) == [1, 97]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10303) == [311, 9992]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10303) == [311, 9992]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2023) == [24, 1999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2023) == [24, 1999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10505) == [511, 9994]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10505) == [511, 9994]: {e}')
    
    total += 1
    try:
        result = candidate(n = 65432) == [1, 65431]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65432) == [1, 65431]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9998) == [1, 9997]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9998) == [1, 9997]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7007) == [8, 6999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7007) == [8, 6999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10101) == [112, 9989]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10101) == [112, 9989]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7070) == [71, 6999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7070) == [71, 6999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6543) == [1, 6542]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6543) == [1, 6542]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10404) == [411, 9993]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10404) == [411, 9993]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7777) == [1, 7776]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7777) == [1, 7776]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8080) == [81, 7999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8080) == [81, 7999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4999) == [1, 4998]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4999) == [1, 4998]: {e}')
    
    total += 1
    try:
        result = candidate(n = 98765) == [1, 98764]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98765) == [1, 98764]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9876) == [1, 9875]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9876) == [1, 9875]: {e}')
    
    total += 1
    try:
        result = candidate(n = 987) == [1, 986]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987) == [1, 986]: {e}')
    
    total += 1
    try:
        result = candidate(n = 76543) == [1, 76542]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 76543) == [1, 76542]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8901) == [2, 8899]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8901) == [2, 8899]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5678) == [1, 5677]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5678) == [1, 5677]: {e}')
    
    total += 1
    try:
        result = candidate(n = 67890) == [1, 67889]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67890) == [1, 67889]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4004) == [5, 3999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4004) == [5, 3999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000) == [1, 1999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000) == [1, 1999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4567) == [1, 4566]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4567) == [1, 4566]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6006) == [7, 5999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6006) == [7, 5999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8008) == [9, 7999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8008) == [9, 7999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6666) == [1, 6665]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6666) == [1, 6665]: {e}')
    
    total += 1
    try:
        result = candidate(n = 76) == [1, 75]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 76) == [1, 75]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4680) == [1, 4679]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4680) == [1, 4679]: {e}')
    
    total += 1
    try:
        result = candidate(n = 765) == [1, 764]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 765) == [1, 764]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2020) == [21, 1999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2020) == [21, 1999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3050) == [51, 2999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3050) == [51, 2999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 32) == [1, 31]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32) == [1, 31]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023) == [24, 999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023) == [24, 999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7890) == [1, 7889]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7890) == [1, 7889]: {e}')
    
    total += 1
    try:
        result = candidate(n = 90123) == [124, 89999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90123) == [124, 89999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7654) == [1, 7653]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7654) == [1, 7653]: {e}')
    
    total += 1
    try:
        result = candidate(n = 876) == [1, 875]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 876) == [1, 875]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7006) == [7, 6999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7006) == [7, 6999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 21098) == [1111, 19987]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21098) == [1111, 19987]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5050) == [51, 4999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5050) == [51, 4999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5002) == [3, 4999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5002) == [3, 4999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9997) == [1, 9996]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9997) == [1, 9996]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3003) == [4, 2999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3003) == [4, 2999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8765) == [1, 8764]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8765) == [1, 8764]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10987) == [988, 9999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10987) == [988, 9999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 321) == [2, 319]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 321) == [2, 319]: {e}')
    
    total += 1
    try:
        result = candidate(n = 23456) == [1, 23455]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23456) == [1, 23455]: {e}')
    
    total += 1
    try:
        result = candidate(n = 56789) == [1, 56788]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 56789) == [1, 56788]: {e}')
    
    total += 1
    try:
        result = candidate(n = 89012) == [13, 88999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 89012) == [13, 88999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3333) == [1, 3332]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3333) == [1, 3332]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3456) == [1, 3455]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3456) == [1, 3455]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1098) == [99, 999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1098) == [99, 999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == [1, 9999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == [1, 9999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5432) == [1, 5431]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5432) == [1, 5431]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2109) == [111, 1998]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2109) == [111, 1998]: {e}')
    
    total += 1
    try:
        result = candidate(n = 54) == [1, 53]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 54) == [1, 53]: {e}')
    
    total += 1
    try:
        result = candidate(n = 654) == [1, 653]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 654) == [1, 653]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8642) == [1, 8641]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8642) == [1, 8641]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5555) == [1, 5554]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5555) == [1, 5554]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3210) == [11, 3199]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3210) == [11, 3199]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9009) == [11, 8998]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9009) == [11, 8998]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6060) == [61, 5999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6060) == [61, 5999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5005) == [6, 4999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5005) == [6, 4999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4444) == [1, 4443]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4444) == [1, 4443]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4321) == [2, 4319]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4321) == [2, 4319]: {e}')
    
    total += 1
    try:
        result = candidate(n = 34567) == [1, 34566]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 34567) == [1, 34566]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2222) == [1, 2221]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2222) == [1, 2221]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6234) == [1, 6233]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6234) == [1, 6233]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10707) == [711, 9996]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10707) == [711, 9996]: {e}')
    
    total += 1
    try:
        result = candidate(n = 109) == [11, 98]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 109) == [11, 98]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4040) == [41, 3999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4040) == [41, 3999]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234) == [1, 1233]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234) == [1, 1233]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7272) == [1, 7271]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7272) == [1, 7271]: {e}')
    
    total += 1
    try:
        result = candidate(n = 45678) == [1, 45677]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45678) == [1, 45677]: {e}')
    
    total += 1
    try:
        result = candidate(n = 78901) == [2, 78899]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 78901) == [2, 78899]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 101) == [2, 99]
    assert candidate(n = 1010) == [11, 999]
    assert candidate(n = 11) == [2, 9]
    assert candidate(n = 104) == [5, 99]
    assert candidate(n = 1001) == [2, 999]
    assert candidate(n = 2) == [1, 1]
    assert candidate(n = 9999) == [1, 9998]
    assert candidate(n = 100) == [1, 99]
    assert candidate(n = 210) == [11, 199]
    assert candidate(n = 9801) == [2, 9799]
    assert candidate(n = 2345) == [1, 2344]
    assert candidate(n = 2100) == [111, 1989]
    assert candidate(n = 1111) == [112, 999]
    assert candidate(n = 10606) == [611, 9995]
    assert candidate(n = 8888) == [1, 8887]
    assert candidate(n = 1000) == [1, 999]
    assert candidate(n = 43) == [1, 42]
    assert candidate(n = 10202) == [211, 9991]
    assert candidate(n = 1357) == [1, 1356]
    assert candidate(n = 10001) == [2, 9999]
    assert candidate(n = 32109) == [111, 31998]
    assert candidate(n = 6789) == [1, 6788]
    assert candidate(n = 6005) == [6, 5999]
    assert candidate(n = 8181) == [2, 8179]
    assert candidate(n = 2468) == [1, 2467]
    assert candidate(n = 2048) == [49, 1999]
    assert candidate(n = 999) == [1, 998]
    assert candidate(n = 3030) == [31, 2999]
    assert candidate(n = 9012) == [13, 8999]
    assert candidate(n = 87654) == [1, 87653]
    assert candidate(n = 43210) == [11, 43199]
    assert candidate(n = 54321) == [2, 54319]
    assert candidate(n = 9090) == [91, 8999]
    assert candidate(n = 65) == [1, 64]
    assert candidate(n = 12345) == [1, 12344]
    assert candidate(n = 21) == [2, 19]
    assert candidate(n = 432) == [1, 431]
    assert candidate(n = 543) == [1, 542]
    assert candidate(n = 87) == [1, 86]
    assert candidate(n = 98) == [1, 97]
    assert candidate(n = 10303) == [311, 9992]
    assert candidate(n = 2023) == [24, 1999]
    assert candidate(n = 10505) == [511, 9994]
    assert candidate(n = 65432) == [1, 65431]
    assert candidate(n = 9998) == [1, 9997]
    assert candidate(n = 7007) == [8, 6999]
    assert candidate(n = 10101) == [112, 9989]
    assert candidate(n = 7070) == [71, 6999]
    assert candidate(n = 6543) == [1, 6542]
    assert candidate(n = 10404) == [411, 9993]
    assert candidate(n = 7777) == [1, 7776]
    assert candidate(n = 8080) == [81, 7999]
    assert candidate(n = 4999) == [1, 4998]
    assert candidate(n = 98765) == [1, 98764]
    assert candidate(n = 9876) == [1, 9875]
    assert candidate(n = 987) == [1, 986]
    assert candidate(n = 76543) == [1, 76542]
    assert candidate(n = 8901) == [2, 8899]
    assert candidate(n = 5678) == [1, 5677]
    assert candidate(n = 67890) == [1, 67889]
    assert candidate(n = 4004) == [5, 3999]
    assert candidate(n = 2000) == [1, 1999]
    assert candidate(n = 4567) == [1, 4566]
    assert candidate(n = 6006) == [7, 5999]
    assert candidate(n = 8008) == [9, 7999]
    assert candidate(n = 6666) == [1, 6665]
    assert candidate(n = 76) == [1, 75]
    assert candidate(n = 4680) == [1, 4679]
    assert candidate(n = 765) == [1, 764]
    assert candidate(n = 2020) == [21, 1999]
    assert candidate(n = 3050) == [51, 2999]
    assert candidate(n = 32) == [1, 31]
    assert candidate(n = 1023) == [24, 999]
    assert candidate(n = 7890) == [1, 7889]
    assert candidate(n = 90123) == [124, 89999]
    assert candidate(n = 7654) == [1, 7653]
    assert candidate(n = 876) == [1, 875]
    assert candidate(n = 7006) == [7, 6999]
    assert candidate(n = 21098) == [1111, 19987]
    assert candidate(n = 5050) == [51, 4999]
    assert candidate(n = 5002) == [3, 4999]
    assert candidate(n = 9997) == [1, 9996]
    assert candidate(n = 3003) == [4, 2999]
    assert candidate(n = 8765) == [1, 8764]
    assert candidate(n = 10987) == [988, 9999]
    assert candidate(n = 321) == [2, 319]
    assert candidate(n = 23456) == [1, 23455]
    assert candidate(n = 56789) == [1, 56788]
    assert candidate(n = 89012) == [13, 88999]
    assert candidate(n = 3333) == [1, 3332]
    assert candidate(n = 3456) == [1, 3455]
    assert candidate(n = 1098) == [99, 999]
    assert candidate(n = 10000) == [1, 9999]
    assert candidate(n = 5432) == [1, 5431]
    assert candidate(n = 2109) == [111, 1998]
    assert candidate(n = 54) == [1, 53]
    assert candidate(n = 654) == [1, 653]
    assert candidate(n = 8642) == [1, 8641]
    assert candidate(n = 5555) == [1, 5554]
    assert candidate(n = 3210) == [11, 3199]
    assert candidate(n = 9009) == [11, 8998]
    assert candidate(n = 6060) == [61, 5999]
    assert candidate(n = 5005) == [6, 4999]
    assert candidate(n = 4444) == [1, 4443]
    assert candidate(n = 4321) == [2, 4319]
    assert candidate(n = 34567) == [1, 34566]
    assert candidate(n = 2222) == [1, 2221]
    assert candidate(n = 6234) == [1, 6233]
    assert candidate(n = 10707) == [711, 9996]
    assert candidate(n = 109) == [11, 98]
    assert candidate(n = 4040) == [41, 3999]
    assert candidate(n = 1234) == [1, 1233]
    assert candidate(n = 7272) == [1, 7271]
    assert candidate(n = 45678) == [1, 45677]
    assert candidate(n = 78901) == [2, 78899]


