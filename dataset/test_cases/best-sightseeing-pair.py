def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(values = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == 1998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == 1998: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 3, 5, 7, 9, 11]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 3, 5, 7, 9, 11]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 198: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(values = [8, 1, 5, 2, 6]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [8, 1, 5, 2, 6]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(values = [1000, 1, 1000, 1, 1000]) == 1998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1000, 1, 1000, 1, 1000]) == 1998: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 5, 1, 7, 2]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 5, 1, 7, 2]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(values = [50, 40, 30, 20, 10]) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [50, 40, 30, 20, 10]) == 89: {e}')
    
    total += 1
    try:
        result = candidate(values = [3, 7, 2, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [3, 7, 2, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 20, 30, 40, 50]) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 20, 30, 40, 50]) == 89: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 5, 1, 2, 6, 3, 8, 1, 9, 4]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 5, 1, 2, 6, 3, 8, 1, 9, 4]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 5, 5, 5, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 5, 5, 5, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 999, 999, 1, 999, 999, 1, 999, 999, 1]) == 1997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 999, 999, 1, 999, 999, 1, 999, 999, 1]) == 1997: {e}')
    
    total += 1
    try:
        result = candidate(values = [3, 7, 2, 5, 10]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [3, 7, 2, 5, 10]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 1000, 2, 999, 3, 998, 4, 997]) == 1997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 1000, 2, 999, 3, 998, 4, 997]) == 1997: {e}')
    
    total += 1
    try:
        result = candidate(values = [9, 7, 5, 3, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [9, 7, 5, 3, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(values = [9, 4, 3, 2]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [9, 4, 3, 2]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 3, 5, 7, 1, 9, 2, 6]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 3, 5, 7, 1, 9, 2, 6]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(values = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5]) == 197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5]) == 197: {e}')
    
    total += 1
    try:
        result = candidate(values = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 198: {e}')
    
    total += 1
    try:
        result = candidate(values = [1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 1998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 1998: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 999, 2, 998, 3, 997, 4, 996, 5, 995]) == 1995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 999, 2, 998, 3, 997, 4, 996, 5, 995]) == 1995: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 5, 3, 7, 9, 2, 6, 8, 4, 10]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 5, 3, 7, 9, 2, 6, 8, 4, 10]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(values = [500, 400, 300, 200, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 899
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [500, 400, 300, 200, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 899: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 189: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5, 1000, 6, 7, 8, 9]) == 1005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5, 1000, 6, 7, 8, 9]) == 1005: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5, 60, 6, 70, 7, 80, 8, 90, 9, 100, 10]) == 188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5, 60, 6, 70, 7, 80, 8, 90, 9, 100, 10]) == 188: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 98: {e}')
    
    total += 1
    try:
        result = candidate(values = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 199: {e}')
    
    total += 1
    try:
        result = candidate(values = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200]) == 398
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200]) == 398: {e}')
    
    total += 1
    try:
        result = candidate(values = [50, 20, 30, 10, 40, 60, 70, 80, 90, 100, 110, 120]) == 229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [50, 20, 30, 10, 40, 60, 70, 80, 90, 100, 110, 120]) == 229: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 4, 3, 2, 1, 1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 1998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 4, 3, 2, 1, 1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 1998: {e}')
    
    total += 1
    try:
        result = candidate(values = [1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93]) == 197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93]) == 197: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 1, 20, 3, 30, 5, 40, 7, 50, 9, 60, 11, 70, 13, 80]) == 148
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 1, 20, 3, 30, 5, 40, 7, 50, 9, 60, 11, 70, 13, 80]) == 148: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50]) == 189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50]) == 189: {e}')
    
    total += 1
    try:
        result = candidate(values = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == 1998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == 1998: {e}')
    
    total += 1
    try:
        result = candidate(values = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985]) == 1996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985]) == 1996: {e}')
    
    total += 1
    try:
        result = candidate(values = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 999: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1000]) == 1008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1000]) == 1008: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 5, 2, 9, 3, 8, 4, 7, 5, 6, 2, 8, 4, 6, 1, 3, 5, 2, 8, 7, 4, 6, 1, 3, 5, 2, 8, 7, 4, 6]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 5, 2, 9, 3, 8, 4, 7, 5, 6, 2, 8, 4, 6, 1, 3, 5, 2, 8, 7, 4, 6, 1, 3, 5, 2, 8, 7, 4, 6]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(values = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980, 979, 978, 977, 976, 975, 974, 973, 972, 971, 970, 969, 968, 967, 966, 965, 964, 963, 962, 961, 960, 959, 958, 957, 956, 955, 954, 953, 952, 951, 950]) == 1996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980, 979, 978, 977, 976, 975, 974, 973, 972, 971, 970, 969, 968, 967, 966, 965, 964, 963, 962, 961, 960, 959, 958, 957, 956, 955, 954, 953, 952, 951, 950]) == 1996: {e}')
    
    total += 1
    try:
        result = candidate(values = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(values = [500, 100, 150, 200, 250, 300, 350, 400, 450, 500]) == 991
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [500, 100, 150, 200, 250, 300, 350, 400, 450, 500]) == 991: {e}')
    
    total += 1
    try:
        result = candidate(values = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980, 979, 978, 977, 976, 975, 974, 973, 972, 971, 970]) == 1996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980, 979, 978, 977, 976, 975, 974, 973, 972, 971, 970]) == 1996: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(values = [100, 1, 200, 3, 400, 5, 600, 7, 800, 9]) == 1398
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [100, 1, 200, 3, 400, 5, 600, 7, 800, 9]) == 1398: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6]) == 1997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6]) == 1997: {e}')
    
    total += 1
    try:
        result = candidate(values = [1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 389
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 389: {e}')
    
    total += 1
    try:
        result = candidate(values = [500, 10, 300, 20, 500, 10, 300, 20]) == 996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [500, 10, 300, 20, 500, 10, 300, 20]) == 996: {e}')
    
    total += 1
    try:
        result = candidate(values = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 98: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(values = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]) == 19499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]) == 19499: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 100, 2, 3, 100, 2, 3, 100, 2, 3, 100, 2, 3]) == 197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 100, 2, 3, 100, 2, 3, 100, 2, 3, 100, 2, 3]) == 197: {e}')
    
    total += 1
    try:
        result = candidate(values = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5]) == 898
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5]) == 898: {e}')
    
    total += 1
    try:
        result = candidate(values = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 1999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 1999: {e}')
    
    total += 1
    try:
        result = candidate(values = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5]) == 1995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5]) == 1995: {e}')
    
    total += 1
    try:
        result = candidate(values = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == 1998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == 1998: {e}')
    
    total += 1
    try:
        result = candidate(values = [800, 100, 900, 50, 10, 200, 300, 400, 500, 600]) == 1698
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [800, 100, 900, 50, 10, 200, 300, 400, 500, 600]) == 1698: {e}')
    
    total += 1
    try:
        result = candidate(values = [2, 3, 5, 5, 6, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [2, 3, 5, 5, 6, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 1000, 1, 999, 1, 998, 1, 997, 1, 996]) == 1997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 1000, 1, 999, 1, 998, 1, 997, 1, 996]) == 1997: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 1, 10, 1, 10, 1, 10, 1, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 1, 10, 1, 10, 1, 10, 1, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6, 995, 7, 994, 8, 993, 9, 992, 10, 991]) == 1997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6, 995, 7, 994, 8, 993, 9, 992, 10, 991]) == 1997: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1000]) == 1004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1000]) == 1004: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 5, 3, 7, 9, 2, 8, 6, 4, 10]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 5, 3, 7, 9, 2, 8, 6, 4, 10]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(values = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520]) == 1038
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520]) == 1038: {e}')
    
    total += 1
    try:
        result = candidate(values = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80, 70, 60, 50]) == 1899
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80, 70, 60, 50]) == 1899: {e}')
    
    total += 1
    try:
        result = candidate(values = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 1998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 1998: {e}')
    
    total += 1
    try:
        result = candidate(values = [500, 400, 300, 200, 100, 50, 25, 10, 5, 1]) == 899
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [500, 400, 300, 200, 100, 50, 25, 10, 5, 1]) == 899: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6, 995, 7, 994, 8]) == 1997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6, 995, 7, 994, 8]) == 1997: {e}')
    
    total += 1
    try:
        result = candidate(values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1990: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996]) == 1997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996]) == 1997: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 50, 15, 20, 80, 30, 40, 60, 25, 70]) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 50, 15, 20, 80, 30, 40, 60, 25, 70]) == 145: {e}')
    
    total += 1
    try:
        result = candidate(values = [800, 900, 100, 200, 300, 400, 500, 600, 700, 800, 900]) == 1791
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [800, 900, 100, 200, 300, 400, 500, 600, 700, 800, 900]) == 1791: {e}')
    
    total += 1
    try:
        result = candidate(values = [500, 499, 498, 497, 496, 495, 494, 493, 492, 491]) == 998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [500, 499, 498, 497, 496, 495, 494, 493, 492, 491]) == 998: {e}')
    
    total += 1
    try:
        result = candidate(values = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5, 994, 6, 993, 7, 992, 8, 991, 9, 990, 10, 989, 11, 988, 12, 987, 13, 986, 14, 985, 15, 984, 16, 983]) == 1995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5, 994, 6, 993, 7, 992, 8, 991, 9, 990, 10, 989, 11, 988, 12, 987, 13, 986, 14, 985, 15, 984, 16, 983]) == 1995: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1000, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1000, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1008: {e}')
    
    total += 1
    try:
        result = candidate(values = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 1998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 1998: {e}')
    
    total += 1
    try:
        result = candidate(values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1980: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5, 100, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5, 100, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 999, 2, 998, 3, 997, 4, 996, 5, 995, 6, 994, 7, 993, 8, 992, 9, 991, 10, 990, 11, 989, 12, 988, 13, 987, 14, 986, 15, 985, 16, 984]) == 1995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 999, 2, 998, 3, 997, 4, 996, 5, 995, 6, 994, 7, 993, 8, 992, 9, 991, 10, 990, 11, 989, 12, 988, 13, 987, 14, 986, 15, 985, 16, 984]) == 1995: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 1000, 2, 1000, 3, 1000, 4, 1000, 5, 1000, 6, 1000, 7, 1000, 8, 1000, 9, 1000, 10, 1000]) == 1998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 1000, 2, 1000, 3, 1000, 4, 1000, 5, 1000, 6, 1000, 7, 1000, 8, 1000, 9, 1000, 10, 1000]) == 1998: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 189: {e}')
    
    total += 1
    try:
        result = candidate(values = [500, 400, 300, 200, 100, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 899
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [500, 400, 300, 200, 100, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 899: {e}')
    
    total += 1
    try:
        result = candidate(values = [500, 1, 500, 1, 500, 1, 500, 1, 500, 1]) == 998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [500, 1, 500, 1, 500, 1, 500, 1, 500, 1]) == 998: {e}')
    
    total += 1
    try:
        result = candidate(values = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(values = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(values = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981]) == 1998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981]) == 1998: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(values = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == 1998
    assert candidate(values = [1, 3, 5, 7, 9, 11]) == 19
    assert candidate(values = [10, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 10
    assert candidate(values = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 198
    assert candidate(values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 18
    assert candidate(values = [8, 1, 5, 2, 6]) == 11
    assert candidate(values = [1000, 1, 1000, 1, 1000]) == 1998
    assert candidate(values = [10, 5, 1, 7, 2]) == 14
    assert candidate(values = [50, 40, 30, 20, 10]) == 89
    assert candidate(values = [3, 7, 2, 5]) == 10
    assert candidate(values = [10, 20, 30, 40, 50]) == 89
    assert candidate(values = [10, 5, 1, 2, 6, 3, 8, 1, 9, 4]) == 15
    assert candidate(values = [5, 5, 5, 5, 5]) == 9
    assert candidate(values = [1, 999, 999, 1, 999, 999, 1, 999, 999, 1]) == 1997
    assert candidate(values = [3, 7, 2, 5, 10]) == 14
    assert candidate(values = [1, 2]) == 2
    assert candidate(values = [1, 1000, 2, 999, 3, 998, 4, 997]) == 1997
    assert candidate(values = [9, 7, 5, 3, 1]) == 15
    assert candidate(values = [9, 4, 3, 2]) == 12
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
    assert candidate(values = [5, 3, 5, 7, 1, 9, 2, 6]) == 14
    assert candidate(values = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5]) == 197
    assert candidate(values = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 198
    assert candidate(values = [1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 1998
    assert candidate(values = [1, 999, 2, 998, 3, 997, 4, 996, 5, 995]) == 1995
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 38
    assert candidate(values = [1, 5, 3, 7, 9, 2, 6, 8, 4, 10]) == 16
    assert candidate(values = [500, 400, 300, 200, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 899
    assert candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 189
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
    assert candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100
    assert candidate(values = [1, 2, 3, 4, 5, 1000, 6, 7, 8, 9]) == 1005
    assert candidate(values = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5, 60, 6, 70, 7, 80, 8, 90, 9, 100, 10]) == 188
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 98
    assert candidate(values = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 199
    assert candidate(values = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200]) == 398
    assert candidate(values = [50, 20, 30, 10, 40, 60, 70, 80, 90, 100, 110, 120]) == 229
    assert candidate(values = [5, 4, 3, 2, 1, 1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 1998
    assert candidate(values = [1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1000
    assert candidate(values = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11]) == 28
    assert candidate(values = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93]) == 197
    assert candidate(values = [10, 1, 20, 3, 30, 5, 40, 7, 50, 9, 60, 11, 70, 13, 80]) == 148
    assert candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50]) == 189
    assert candidate(values = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == 1998
    assert candidate(values = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985]) == 1996
    assert candidate(values = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 999
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1000]) == 1008
    assert candidate(values = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 8
    assert candidate(values = [1, 5, 2, 9, 3, 8, 4, 7, 5, 6, 2, 8, 4, 6, 1, 3, 5, 2, 8, 7, 4, 6, 1, 3, 5, 2, 8, 7, 4, 6]) == 15
    assert candidate(values = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980, 979, 978, 977, 976, 975, 974, 973, 972, 971, 970, 969, 968, 967, 966, 965, 964, 963, 962, 961, 960, 959, 958, 957, 956, 955, 954, 953, 952, 951, 950]) == 1996
    assert candidate(values = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 28
    assert candidate(values = [500, 100, 150, 200, 250, 300, 350, 400, 450, 500]) == 991
    assert candidate(values = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980, 979, 978, 977, 976, 975, 974, 973, 972, 971, 970]) == 1996
    assert candidate(values = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 19
    assert candidate(values = [100, 1, 200, 3, 400, 5, 600, 7, 800, 9]) == 1398
    assert candidate(values = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6]) == 1997
    assert candidate(values = [1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1000
    assert candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 389
    assert candidate(values = [500, 10, 300, 20, 500, 10, 300, 20]) == 996
    assert candidate(values = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 98
    assert candidate(values = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2
    assert candidate(values = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
    assert candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == 100
    assert candidate(values = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]) == 19499
    assert candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9
    assert candidate(values = [1, 2, 3, 100, 2, 3, 100, 2, 3, 100, 2, 3, 100, 2, 3]) == 197
    assert candidate(values = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5]) == 898
    assert candidate(values = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 1999
    assert candidate(values = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5]) == 1995
    assert candidate(values = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == 1998
    assert candidate(values = [800, 100, 900, 50, 10, 200, 300, 400, 500, 600]) == 1698
    assert candidate(values = [2, 3, 5, 5, 6, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 30
    assert candidate(values = [1, 1000, 1, 999, 1, 998, 1, 997, 1, 996]) == 1997
    assert candidate(values = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 18
    assert candidate(values = [10, 1, 10, 1, 10, 1, 10, 1, 10]) == 18
    assert candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9
    assert candidate(values = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6, 995, 7, 994, 8, 993, 9, 992, 10, 991]) == 1997
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 18
    assert candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1000]) == 1004
    assert candidate(values = [1, 5, 3, 7, 9, 2, 8, 6, 4, 10]) == 15
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 28
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 48
    assert candidate(values = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520]) == 1038
    assert candidate(values = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80, 70, 60, 50]) == 1899
    assert candidate(values = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 1998
    assert candidate(values = [500, 400, 300, 200, 100, 50, 25, 10, 5, 1]) == 899
    assert candidate(values = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6, 995, 7, 994, 8]) == 1997
    assert candidate(values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1990
    assert candidate(values = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996]) == 1997
    assert candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000]) == 1000
    assert candidate(values = [10, 50, 15, 20, 80, 30, 40, 60, 25, 70]) == 145
    assert candidate(values = [800, 900, 100, 200, 300, 400, 500, 600, 700, 800, 900]) == 1791
    assert candidate(values = [500, 499, 498, 497, 496, 495, 494, 493, 492, 491]) == 998
    assert candidate(values = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5, 994, 6, 993, 7, 992, 8, 991, 9, 990, 10, 989, 11, 988, 12, 987, 13, 986, 14, 985, 15, 984, 16, 983]) == 1995
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1000, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1008
    assert candidate(values = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 1998
    assert candidate(values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1980
    assert candidate(values = [1, 2, 3, 4, 5, 100, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 105
    assert candidate(values = [1, 999, 2, 998, 3, 997, 4, 996, 5, 995, 6, 994, 7, 993, 8, 992, 9, 991, 10, 990, 11, 989, 12, 988, 13, 987, 14, 986, 15, 985, 16, 984]) == 1995
    assert candidate(values = [1, 1000, 2, 1000, 3, 1000, 4, 1000, 5, 1000, 6, 1000, 7, 1000, 8, 1000, 9, 1000, 10, 1000]) == 1998
    assert candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 189
    assert candidate(values = [500, 400, 300, 200, 100, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 899
    assert candidate(values = [500, 1, 500, 1, 500, 1, 500, 1, 500, 1]) == 998
    assert candidate(values = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 99
    assert candidate(values = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 38
    assert candidate(values = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981]) == 1998


