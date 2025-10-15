def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 625) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 625) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 576) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 576) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 729) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 729) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 144) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 144) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 900) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 324) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 324) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 841) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 841) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 289) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 289) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 484) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 484) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 225) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 225) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 784) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 784) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 101) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 169) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 169) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 256) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 36) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 36) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 529) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 529) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 676) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 676) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 961) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 961) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 400) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 196) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 196) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 121) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 121) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 361) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 361) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 441) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 441) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1089) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1089) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 7225) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7225) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 13689) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13689) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 63841) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63841) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 73081) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 73081) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 48601) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 48601) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 12544) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12544) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 14400) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14400) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 5929) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5929) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 15625) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15625) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4761) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4761) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 27) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 90409) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90409) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 34081) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 34081) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 66109) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 66109) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 6241) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6241) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 8821) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8821) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 16807) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16807) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2809) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2809) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 10201) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10201) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 11881) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11881) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 823543) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 823543) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 57201) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 57201) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 9604) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9604) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 30025) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30025) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2601) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2601) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 68401) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 68401) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 5329) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5329) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 14641) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14641) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 3025) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3025) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 12321) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12321) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 32041) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32041) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1009) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1009) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1681) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1681) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 13456) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13456) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1225) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1225) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 24025) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24025) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 38161) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 38161) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 7921) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7921) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 18769) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18769) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2401) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2401) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 10609) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10609) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 95657) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 95657) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2025) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2025) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 5625) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5625) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 10404) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10404) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 61609) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 61609) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4489) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4489) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2209) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2209) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 75469) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75469) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388608) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388608) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 12769) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12769) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 52849) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 52849) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 55025) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55025) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4225) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4225) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 3969) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3969) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777216) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777216) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 11236) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11236) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 93019) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 93019) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 11449) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11449) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 343) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 343) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 42301) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 42301) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 6561) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6561) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 98329) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98329) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 36121) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 36121) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 101025) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101025) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 12996) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12996) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 12100) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12100) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 77881) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 77881) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 44389) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 44389) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 14161) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14161) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 5041) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5041) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 8361) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8361) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 85309) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 85309) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 80329) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80329) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 82801) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 82801) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2097152) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2097152) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1849) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1849) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 3481) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3481) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 6889) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6889) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 28099) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28099) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 46489) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 46489) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 70729) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 70729) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 10816) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10816) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 22201) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22201) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 13924) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13924) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 11025) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11025) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4194304) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4194304) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 87841) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 87841) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1369) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1369) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 59401) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 59401) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 13225) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13225) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 40225) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40225) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 11664) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11664) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 50721) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50721) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 7569) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7569) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 3721) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3721) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 3249) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3249) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 20449) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20449) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 9409) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9409) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 9216) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9216) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 26041) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 26041) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1521) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1521) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 625) == False
    assert candidate(n = 3) == False
    assert candidate(n = 576) == False
    assert candidate(n = 729) == False
    assert candidate(n = 144) == False
    assert candidate(n = 49) == True
    assert candidate(n = 900) == False
    assert candidate(n = 324) == False
    assert candidate(n = 100) == False
    assert candidate(n = 841) == True
    assert candidate(n = 5) == False
    assert candidate(n = 289) == True
    assert candidate(n = 4) == True
    assert candidate(n = 64) == False
    assert candidate(n = 16) == False
    assert candidate(n = 10000) == False
    assert candidate(n = 484) == False
    assert candidate(n = 2) == False
    assert candidate(n = 225) == False
    assert candidate(n = 784) == False
    assert candidate(n = 1024) == False
    assert candidate(n = 101) == False
    assert candidate(n = 169) == True
    assert candidate(n = 256) == False
    assert candidate(n = 36) == False
    assert candidate(n = 529) == True
    assert candidate(n = 20) == False
    assert candidate(n = 676) == False
    assert candidate(n = 81) == False
    assert candidate(n = 15) == False
    assert candidate(n = 961) == True
    assert candidate(n = 400) == False
    assert candidate(n = 9) == True
    assert candidate(n = 196) == False
    assert candidate(n = 121) == True
    assert candidate(n = 361) == True
    assert candidate(n = 441) == False
    assert candidate(n = 7) == False
    assert candidate(n = 10) == False
    assert candidate(n = 25) == True
    assert candidate(n = 1089) == False
    assert candidate(n = 7225) == False
    assert candidate(n = 13689) == False
    assert candidate(n = 63841) == False
    assert candidate(n = 73081) == False
    assert candidate(n = 48601) == False
    assert candidate(n = 12544) == False
    assert candidate(n = 14400) == False
    assert candidate(n = 5929) == False
    assert candidate(n = 15625) == False
    assert candidate(n = 4761) == False
    assert candidate(n = 27) == False
    assert candidate(n = 90409) == False
    assert candidate(n = 34081) == False
    assert candidate(n = 66109) == False
    assert candidate(n = 6241) == True
    assert candidate(n = 8821) == False
    assert candidate(n = 16807) == False
    assert candidate(n = 2809) == True
    assert candidate(n = 10201) == True
    assert candidate(n = 11881) == True
    assert candidate(n = 823543) == False
    assert candidate(n = 57201) == False
    assert candidate(n = 1) == False
    assert candidate(n = 9604) == False
    assert candidate(n = 30025) == False
    assert candidate(n = 2601) == False
    assert candidate(n = 68401) == False
    assert candidate(n = 5329) == True
    assert candidate(n = 14641) == False
    assert candidate(n = 3025) == False
    assert candidate(n = 12321) == False
    assert candidate(n = 32041) == True
    assert candidate(n = 1009) == False
    assert candidate(n = 1681) == True
    assert candidate(n = 13456) == False
    assert candidate(n = 1225) == False
    assert candidate(n = 24025) == False
    assert candidate(n = 38161) == False
    assert candidate(n = 7921) == True
    assert candidate(n = 18769) == True
    assert candidate(n = 2401) == False
    assert candidate(n = 10609) == True
    assert candidate(n = 95657) == False
    assert candidate(n = 2025) == False
    assert candidate(n = 5625) == False
    assert candidate(n = 10404) == False
    assert candidate(n = 61609) == False
    assert candidate(n = 4489) == True
    assert candidate(n = 2209) == True
    assert candidate(n = 75469) == False
    assert candidate(n = 8388608) == False
    assert candidate(n = 12769) == True
    assert candidate(n = 52849) == False
    assert candidate(n = 55025) == False
    assert candidate(n = 4225) == False
    assert candidate(n = 3969) == False
    assert candidate(n = 16777216) == False
    assert candidate(n = 11236) == False
    assert candidate(n = 93019) == False
    assert candidate(n = 11449) == True
    assert candidate(n = 343) == False
    assert candidate(n = 42301) == False
    assert candidate(n = 6561) == False
    assert candidate(n = 98329) == False
    assert candidate(n = 36121) == False
    assert candidate(n = 101025) == False
    assert candidate(n = 12996) == False
    assert candidate(n = 12100) == False
    assert candidate(n = 77881) == False
    assert candidate(n = 44389) == False
    assert candidate(n = 14161) == False
    assert candidate(n = 5041) == True
    assert candidate(n = 8361) == False
    assert candidate(n = 85309) == False
    assert candidate(n = 80329) == False
    assert candidate(n = 82801) == False
    assert candidate(n = 2097152) == False
    assert candidate(n = 1849) == True
    assert candidate(n = 3481) == True
    assert candidate(n = 6889) == True
    assert candidate(n = 28099) == False
    assert candidate(n = 46489) == False
    assert candidate(n = 70729) == False
    assert candidate(n = 10816) == False
    assert candidate(n = 22201) == True
    assert candidate(n = 13924) == False
    assert candidate(n = 11025) == False
    assert candidate(n = 4194304) == False
    assert candidate(n = 87841) == False
    assert candidate(n = 1369) == True
    assert candidate(n = 59401) == False
    assert candidate(n = 13225) == False
    assert candidate(n = 40225) == False
    assert candidate(n = 11664) == False
    assert candidate(n = 50721) == False
    assert candidate(n = 7569) == False
    assert candidate(n = 3721) == True
    assert candidate(n = 3249) == False
    assert candidate(n = 20449) == False
    assert candidate(n = 9409) == True
    assert candidate(n = 9216) == False
    assert candidate(n = 26041) == False
    assert candidate(n = 1521) == False


