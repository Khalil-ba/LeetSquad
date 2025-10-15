def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000000000) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000000000) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 27) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 18017459) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18017459) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 619) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 619) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 239) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 239) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 53) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 53) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == 35: {e}')
    
    total += 1
    try:
        result = candidate(n = 587) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 587) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 787) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 787) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000019) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000019) == 34: {e}')
    
    total += 1
    try:
        result = candidate(n = 971) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 971) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 43) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 43) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 887) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 887) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 983) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 983) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 523) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 523) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 379) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 379) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 103) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 103) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 37) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 937) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 937) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 487) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 487) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 223) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 223) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 211) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 211) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 23) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 73) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 73) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 941) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 941) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 827) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 827) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 547) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 547) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 251) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 251) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 181) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 181) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 333333333) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 333333333) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 193) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 193) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048576) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048576) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 131) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 241) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 241) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 263) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 263) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 347) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 347) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000013) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000013) == 34: {e}')
    
    total += 1
    try:
        result = candidate(n = 857) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 857) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 383) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 383) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 997) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 997) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 569) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 569) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 929) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 929) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 571) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 571) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 491) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 491) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 643) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 643) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 246813579) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 246813579) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575) == 23: {e}')
    
    total += 1
    try:
        result = candidate(n = 823543) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 823543) == 23: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 353) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 353) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 313) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 313) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 829) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 829) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 167) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 167) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 1111111111) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111111111) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 467) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 467) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 54321) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 54321) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 97) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 97) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 29) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 317) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 317) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 433) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 433) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 131071) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131071) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 789456123) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 789456123) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 1999999998) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1999999998) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 271) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 271) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 797) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 797) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 107) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 107) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 163) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 163) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 557) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 557) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 653) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 653) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 631) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 631) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 991) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 991) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 617) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 617) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 389) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 389) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 751) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 751) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 625000000) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 625000000) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 401) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 401) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000002) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000002) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 44) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 44) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 137) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 137) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 919) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 919) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 257) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 257) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 811) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 811) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 509) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 509) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777215) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777215) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 777777777) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 777777777) == 33: {e}')
    
    total += 1
    try:
        result = candidate(n = 101) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 907) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 907) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 821) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 821) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 421) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 421) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 479) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 479) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 89) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 89) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 953) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 953) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 877) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 877) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 71) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 71) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000001) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000001) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 599) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 599) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 593) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 593) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 151) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 151) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 293) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 293) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 691) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 691) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 41) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 41) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 647) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 647) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 727) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 727) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 209) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 209) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 83) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 83) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 661) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 661) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 283) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 283) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 499) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 499) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 577) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 577) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000011) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000011) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 739) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 739) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 881) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 881) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 659) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 659) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 79) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 79) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 63) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 269) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 269) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 61) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 61) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 373) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 373) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 227) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 227) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 563) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 563) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 47) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 47) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 4096) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4096) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 113) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 113) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 233) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 233) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 911) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 911) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 863) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 863) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 859) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 859) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 359) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 359) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 443) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 443) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 135792468) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 135792468) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 78125) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 78125) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 191) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 191) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 125000000) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125000000) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 311) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 311) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 457) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 457) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 179) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 179) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 337) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 337) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 773) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 773) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 733) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 733) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 419) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 419) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 314159265) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 314159265) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 65536) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65536) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 967) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 967) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 127) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 127) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000007) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000007) == 34: {e}')
    
    total += 1
    try:
        result = candidate(n = 947) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 947) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567890) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567890) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 307) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 307) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 503) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 503) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 397) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 397) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 3125000000) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3125000000) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 26) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 26) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 281) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 281) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 743) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 743) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 1800000000) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1800000000) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 3125) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3125) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 1999999999) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1999999999) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 899999999) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 899999999) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 719) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 719) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 222222222) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 222222222) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 59049) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 59049) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 601) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 601) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000003) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000003) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 367) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 367) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 125) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 839) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 839) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 277) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 277) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 19683) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19683) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 613) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 613) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 89123456) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 89123456) == 27: {e}')
    
    total += 1
    try:
        result = candidate(n = 197) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 197) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 157) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 157) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 769) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 769) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 673) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 673) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 439) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 439) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 1500000000) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1500000000) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 331) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 331) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 173) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 173) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 67) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 607) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 607) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 349) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 349) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 431) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 431) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 666666666) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 666666666) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 683) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 683) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 449) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 449) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 677) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 677) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 809) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 809) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 977) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 977) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 897654321) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 897654321) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 463) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 463) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 757) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 757) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 521) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 521) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 853) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 853) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 883) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 883) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 709) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 709) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 701) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 701) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 823) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 823) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 149) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 149) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 139) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 139) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 461) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 461) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 541) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 541) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 641) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 641) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 761) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 761) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 109) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 109) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 229) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 229) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 199) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 199) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 409) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 409) == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 2
    assert candidate(n = 2000000000) == 32
    assert candidate(n = 100) == 8
    assert candidate(n = 1000) == 10
    assert candidate(n = 5) == 4
    assert candidate(n = 4) == 3
    assert candidate(n = 2) == 2
    assert candidate(n = 8) == 4
    assert candidate(n = 27) == 4
    assert candidate(n = 20) == 5
    assert candidate(n = 1000000000) == 31
    assert candidate(n = 18017459) == 28
    assert candidate(n = 15) == 5
    assert candidate(n = 9) == 3
    assert candidate(n = 1000000) == 20
    assert candidate(n = 6) == 3
    assert candidate(n = 1) == 1
    assert candidate(n = 10) == 4
    assert candidate(n = 25) == 6
    assert candidate(n = 619) == 12
    assert candidate(n = 239) == 11
    assert candidate(n = 53) == 8
    assert candidate(n = 2147483647) == 35
    assert candidate(n = 587) == 12
    assert candidate(n = 787) == 11
    assert candidate(n = 1000000019) == 34
    assert candidate(n = 971) == 13
    assert candidate(n = 43) == 7
    assert candidate(n = 887) == 13
    assert candidate(n = 983) == 11
    assert candidate(n = 523) == 10
    assert candidate(n = 379) == 9
    assert candidate(n = 103) == 9
    assert candidate(n = 37) == 6
    assert candidate(n = 937) == 11
    assert candidate(n = 487) == 8
    assert candidate(n = 223) == 9
    assert candidate(n = 211) == 11
    assert candidate(n = 23) == 7
    assert candidate(n = 73) == 7
    assert candidate(n = 941) == 12
    assert candidate(n = 827) == 13
    assert candidate(n = 547) == 10
    assert candidate(n = 251) == 10
    assert candidate(n = 181) == 8
    assert candidate(n = 333333333) == 29
    assert candidate(n = 193) == 9
    assert candidate(n = 1048576) == 21
    assert candidate(n = 131) == 10
    assert candidate(n = 241) == 9
    assert candidate(n = 263) == 10
    assert candidate(n = 347) == 11
    assert candidate(n = 1000000013) == 34
    assert candidate(n = 857) == 13
    assert candidate(n = 383) == 11
    assert candidate(n = 997) == 11
    assert candidate(n = 569) == 10
    assert candidate(n = 929) == 12
    assert candidate(n = 571) == 10
    assert candidate(n = 491) == 10
    assert candidate(n = 11) == 5
    assert candidate(n = 643) == 12
    assert candidate(n = 246813579) == 30
    assert candidate(n = 1048575) == 23
    assert candidate(n = 823543) == 23
    assert candidate(n = 500000000) == 31
    assert candidate(n = 353) == 10
    assert candidate(n = 313) == 10
    assert candidate(n = 829) == 11
    assert candidate(n = 167) == 9
    assert candidate(n = 1111111111) == 31
    assert candidate(n = 467) == 12
    assert candidate(n = 54321) == 20
    assert candidate(n = 97) == 8
    assert candidate(n = 29) == 6
    assert candidate(n = 317) == 11
    assert candidate(n = 433) == 9
    assert candidate(n = 131071) == 21
    assert candidate(n = 789456123) == 31
    assert candidate(n = 1999999998) == 31
    assert candidate(n = 271) == 8
    assert candidate(n = 797) == 12
    assert candidate(n = 107) == 10
    assert candidate(n = 163) == 7
    assert candidate(n = 557) == 12
    assert candidate(n = 653) == 10
    assert candidate(n = 631) == 12
    assert candidate(n = 991) == 10
    assert candidate(n = 617) == 12
    assert candidate(n = 389) == 11
    assert candidate(n = 751) == 11
    assert candidate(n = 625000000) == 28
    assert candidate(n = 401) == 11
    assert candidate(n = 1000000002) == 31
    assert candidate(n = 44) == 7
    assert candidate(n = 137) == 9
    assert candidate(n = 919) == 11
    assert candidate(n = 17) == 6
    assert candidate(n = 257) == 10
    assert candidate(n = 811) == 9
    assert candidate(n = 509) == 11
    assert candidate(n = 16777215) == 24
    assert candidate(n = 777777777) == 33
    assert candidate(n = 101) == 9
    assert candidate(n = 907) == 12
    assert candidate(n = 821) == 11
    assert candidate(n = 421) == 12
    assert candidate(n = 479) == 12
    assert candidate(n = 89) == 9
    assert candidate(n = 953) == 13
    assert candidate(n = 877) == 11
    assert candidate(n = 71) == 10
    assert candidate(n = 1000000001) == 32
    assert candidate(n = 599) == 12
    assert candidate(n = 81) == 5
    assert candidate(n = 593) == 11
    assert candidate(n = 151) == 9
    assert candidate(n = 293) == 10
    assert candidate(n = 691) == 11
    assert candidate(n = 41) == 7
    assert candidate(n = 647) == 13
    assert candidate(n = 727) == 11
    assert candidate(n = 209) == 10
    assert candidate(n = 83) == 7
    assert candidate(n = 661) == 10
    assert candidate(n = 123456789) == 28
    assert candidate(n = 283) == 10
    assert candidate(n = 499) == 10
    assert candidate(n = 577) == 10
    assert candidate(n = 1000000011) == 32
    assert candidate(n = 739) == 9
    assert candidate(n = 881) == 11
    assert candidate(n = 659) == 11
    assert candidate(n = 79) == 8
    assert candidate(n = 63) == 6
    assert candidate(n = 269) == 11
    assert candidate(n = 61) == 7
    assert candidate(n = 373) == 10
    assert candidate(n = 999999999) == 30
    assert candidate(n = 227) == 10
    assert candidate(n = 563) == 12
    assert candidate(n = 47) == 8
    assert candidate(n = 4096) == 13
    assert candidate(n = 113) == 8
    assert candidate(n = 233) == 10
    assert candidate(n = 911) == 13
    assert candidate(n = 863) == 15
    assert candidate(n = 859) == 13
    assert candidate(n = 359) == 12
    assert candidate(n = 443) == 11
    assert candidate(n = 135792468) == 28
    assert candidate(n = 78125) == 18
    assert candidate(n = 191) == 9
    assert candidate(n = 125000000) == 29
    assert candidate(n = 311) == 12
    assert candidate(n = 457) == 10
    assert candidate(n = 179) == 11
    assert candidate(n = 337) == 9
    assert candidate(n = 773) == 12
    assert candidate(n = 733) == 9
    assert candidate(n = 419) == 12
    assert candidate(n = 314159265) == 28
    assert candidate(n = 65536) == 17
    assert candidate(n = 967) == 12
    assert candidate(n = 127) == 8
    assert candidate(n = 1000000007) == 34
    assert candidate(n = 947) == 13
    assert candidate(n = 987654321) == 29
    assert candidate(n = 1234567890) == 29
    assert candidate(n = 307) == 10
    assert candidate(n = 503) == 12
    assert candidate(n = 397) == 10
    assert candidate(n = 3125000000) == 30
    assert candidate(n = 26) == 6
    assert candidate(n = 281) == 10
    assert candidate(n = 743) == 11
    assert candidate(n = 1800000000) == 31
    assert candidate(n = 3125) == 15
    assert candidate(n = 1999999999) == 32
    assert candidate(n = 899999999) == 36
    assert candidate(n = 13) == 5
    assert candidate(n = 719) == 14
    assert candidate(n = 222222222) == 29
    assert candidate(n = 59049) == 11
    assert candidate(n = 601) == 11
    assert candidate(n = 1000000003) == 32
    assert candidate(n = 367) == 10
    assert candidate(n = 125) == 9
    assert candidate(n = 839) == 11
    assert candidate(n = 277) == 10
    assert candidate(n = 19683) == 10
    assert candidate(n = 613) == 11
    assert candidate(n = 89123456) == 27
    assert candidate(n = 197) == 10
    assert candidate(n = 157) == 9
    assert candidate(n = 769) == 11
    assert candidate(n = 673) == 10
    assert candidate(n = 439) == 10
    assert candidate(n = 1500000000) == 32
    assert candidate(n = 331) == 9
    assert candidate(n = 173) == 9
    assert candidate(n = 67) == 8
    assert candidate(n = 607) == 12
    assert candidate(n = 349) == 10
    assert candidate(n = 431) == 14
    assert candidate(n = 666666666) == 30
    assert candidate(n = 683) == 12
    assert candidate(n = 449) == 10
    assert candidate(n = 677) == 11
    assert candidate(n = 809) == 13
    assert candidate(n = 977) == 10
    assert candidate(n = 897654321) == 30
    assert candidate(n = 463) == 11
    assert candidate(n = 757) == 9
    assert candidate(n = 521) == 12
    assert candidate(n = 853) == 13
    assert candidate(n = 1024) == 11
    assert candidate(n = 883) == 11
    assert candidate(n = 709) == 11
    assert candidate(n = 701) == 12
    assert candidate(n = 823) == 11
    assert candidate(n = 149) == 9
    assert candidate(n = 19) == 5
    assert candidate(n = 139) == 9
    assert candidate(n = 461) == 11
    assert candidate(n = 541) == 9
    assert candidate(n = 641) == 11
    assert candidate(n = 761) == 11
    assert candidate(n = 109) == 7
    assert candidate(n = 31) == 6
    assert candidate(n = 229) == 9
    assert candidate(n = 199) == 9
    assert candidate(n = 7) == 4
    assert candidate(n = 409) == 10


