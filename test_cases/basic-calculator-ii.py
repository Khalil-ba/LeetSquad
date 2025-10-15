def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "2 - 3 + 4") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2 - 3 + 4") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = " 1000000000 - 500000000 + 250000000") == 750000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 1000000000 - 500000000 + 250000000") == 750000000: {e}')
    
    total += 1
    try:
        result = candidate(s = "30 + 2 * 6 / (3 - 1)") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "30 + 2 * 6 / (3 - 1)") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 * ( 2 + 12 ) / 14") == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 * ( 2 + 12 ) / 14") == 200: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 + 1 * 1 + 1") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 + 1 * 1 + 1") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "2*3+4/5") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2*3+4/5") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "3 + 5 / ( 2 + 3 )") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3 + 5 / ( 2 + 3 )") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "0 + 0") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0 + 0") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "100*2+12") == 212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100*2+12") == 212: {e}')
    
    total += 1
    try:
        result = candidate(s = "2147483647 + 1 - 1") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2147483647 + 1 - 1") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "100000 + 100000 - 50000 * 2 + 25000 * 4 / 5") == 120000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100000 + 100000 - 50000 * 2 + 25000 * 4 / 5") == 120000: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 * 2 + 12") == 212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 * 2 + 12") == 212: {e}')
    
    total += 1
    try:
        result = candidate(s = " 200 - 3 * 50 + 25") == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 200 - 3 * 50 + 25") == 75: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 + 2 * 6") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 + 2 * 6") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "3+2*2") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3+2*2") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = " 30 + 2 * 6 - 12 / 3 ") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 30 + 2 * 6 - 12 / 3 ") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "100*(2+12)/14") == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100*(2+12)/14") == 200: {e}')
    
    total += 1
    try:
        result = candidate(s = " 3+5 / 2 ") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 3+5 / 2 ") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10") == 3628800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10") == 3628800: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 * 2 / 25") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 * 2 / 25") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = " 0 + 0 * 1 / 1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 0 + 0 * 1 / 1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = " 3/2 ") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 3/2 ") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "3 + 5 - ( 2 + 3 )") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3 + 5 - ( 2 + 3 )") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "2147483647 - 2147483646") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2147483647 - 2147483646") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "3+5 / 2 * 3") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3+5 / 2 * 3") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "3 + 2 * 2 + 1 - 5 / 2") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3 + 2 * 2 + 1 - 5 / 2") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 * 5 + 3") == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 * 5 + 3") == 53: {e}')
    
    total += 1
    try:
        result = candidate(s = "3+5-2*3/4") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3+5-2*3/4") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "3 + 5 / 2 + 3") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3 + 5 / 2 + 3") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000 / 10 / 10") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000 / 10 / 10") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "3 + 5 / 2 - 8 * 3 + 4 / 2") == -17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3 + 5 / 2 - 8 * 3 + 4 / 2") == -17: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = " 30 / 3 + 10 * 2 - 5") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 30 / 3 + 10 * 2 - 5") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "100*(2+12)") == 212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100*(2+12)") == 212: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 * ( 2 + 12 )") == 212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 * ( 2 + 12 )") == 212: {e}')
    
    total += 1
    try:
        result = candidate(s = " 1 + 2 * 3 / 4 + 5 * 6 - 7") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 1 + 2 * 3 / 4 + 5 * 6 - 7") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "( 2 + 6 ) * 3 + 8") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "( 2 + 6 ) * 3 + 8") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "(2 + 6 * 3 + 5 - (3 * 14 / 7 + 2) * 5) + 3") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(2 + 6 * 3 + 5 - (3 * 14 / 7 + 2) * 5) + 3") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "2147483647 / 1") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2147483647 / 1") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 - 1 + 1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 - 1 + 1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "2*3+4/5*6-7+8") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2*3+4/5*6-7+8") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 + 2 - 5") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 + 2 - 5") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = " 30 /3 + 10 * 2 ") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 30 /3 + 10 * 2 ") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "2 * 3 + 4 / 5") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2 * 3 + 4 / 5") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "3 + 2 * 2 + 1") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3 + 2 * 2 + 1") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "10+2*6") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10+2*6") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "3 + ( 2 * 2 )") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3 + ( 2 * 2 )") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "123 + 456 * 789 / 100 - 987") == 2733
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123 + 456 * 789 / 100 - 987") == 2733: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000 - 500 * 2 + 250 / 5") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000 - 500 * 2 + 250 / 5") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = " 100000 - 50000 * 2 + 25000 / 5000 * 20000") == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 100000 - 50000 * 2 + 25000 / 5000 * 20000") == 100000: {e}')
    
    total += 1
    try:
        result = candidate(s = "987654 * 321 / 123 - 456789 + 987654") == 3108401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "987654 * 321 / 123 - 456789 + 987654") == 3108401: {e}')
    
    total += 1
    try:
        result = candidate(s = " 1 + 2 - 3 * (4 / 5) + 6 - 7 * 8 / 9") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 1 + 2 - 3 * (4 / 5) + 6 - 7 * 8 / 9") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "   8 *    5 / 4 + 3 - 1") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   8 *    5 / 4 + 3 - 1") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = " 2000 / 10 + 50 * 2 - 300 ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 2000 / 10 + 50 * 2 - 300 ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = " 1234 + 567 * 89 - 101112 / 1314") == 51621
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 1234 + 567 * 89 - 101112 / 1314") == 51621: {e}')
    
    total += 1
    try:
        result = candidate(s = " (123 + 456) * 789 - 101112 / (13 * 14) ") == 251029
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " (123 + 456) * 789 - 101112 / (13 * 14) ") == 251029: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 * 2 + 3 * 4 + 5 * 6 + 7 * 8 + 9 * 10") == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 * 2 + 3 * 4 + 5 * 6 + 7 * 8 + 9 * 10") == 190: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 / 10 - 90 * 0 + 80 / 8") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 / 10 - 90 * 0 + 80 / 8") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = " 1000000 - 500000 + 250000 * 2 - 125000 ") == 875000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 1000000 - 500000 + 250000 * 2 - 125000 ") == 875000: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000 - 500 * 2 / 5 + 300 / 3") == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000 - 500 * 2 / 5 + 300 / 3") == 900: {e}')
    
    total += 1
    try:
        result = candidate(s = " 1000 + 2000 - (3000 / 4000 + 5000 - 6000 * (7000 / 8000))") == 2750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 1000 + 2000 - (3000 / 4000 + 5000 - 6000 * (7000 / 8000))") == 2750: {e}')
    
    total += 1
    try:
        result = candidate(s = " 200 * 5 + 300 / 100 - 10 ") == 993
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 200 * 5 + 300 / 100 - 10 ") == 993: {e}')
    
    total += 1
    try:
        result = candidate(s = "123 + 456 * 789 - 101112 / 1314") == 359831
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123 + 456 * 789 - 101112 / 1314") == 359831: {e}')
    
    total += 1
    try:
        result = candidate(s = " 5 + 4 - 3 * 2 + 1 / 1") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 5 + 4 - 3 * 2 + 1 / 1") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = " ( 100 + 200 ) * ( 300 - 100 ) / 50") == 60098
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " ( 100 + 200 ) * ( 300 - 100 ) / 50") == 60098: {e}')
    
    total += 1
    try:
        result = candidate(s = "7 * 8 * 9 / 6 + 5 - 3 * 2") == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "7 * 8 * 9 / 6 + 5 - 3 * 2") == 83: {e}')
    
    total += 1
    try:
        result = candidate(s = "300 + 200 * 5 / 10 - 25") == 375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "300 + 200 * 5 / 10 - 25") == 375: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 * 200 / 500 + 200 - 100") == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 * 200 / 500 + 200 - 100") == 140: {e}')
    
    total += 1
    try:
        result = candidate(s = "100000 / 100 - 99999 * 0 + 1") == 1001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100000 / 100 - 99999 * 0 + 1") == 1001: {e}')
    
    total += 1
    try:
        result = candidate(s = "   42   *   (5 - 3) / 2 + 8  ") == 217
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   42   *   (5 - 3) / 2 + 8  ") == 217: {e}')
    
    total += 1
    try:
        result = candidate(s = "   23 + 56 * 99 / 77 - 44   ") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   23 + 56 * 99 / 77 - 44   ") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 * 2 + 12 / 3 - 5") == 199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 * 2 + 12 / 3 - 5") == 199: {e}')
    
    total += 1
    try:
        result = candidate(s = "   123 + 456 - 789 * 0 / 1 + 1000   ") == 1579
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   123 + 456 - 789 * 0 / 1 + 1000   ") == 1579: {e}')
    
    total += 1
    try:
        result = candidate(s = "33 + 22 * 11 - 44 / 11 + 55") == 326
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "33 + 22 * 11 - 44 / 11 + 55") == 326: {e}')
    
    total += 1
    try:
        result = candidate(s = "3 * 3 * 3 * 3 * 3 - 3 * 3 * 3 + 3") == 219
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3 * 3 * 3 * 3 * 3 - 3 * 3 * 3 + 3") == 219: {e}')
    
    total += 1
    try:
        result = candidate(s = "2147483647 - 2147483646 + 1") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2147483647 - 2147483646 + 1") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 + 2 * 6 / ( 1 - 2 ) * 3") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 + 2 * 6 / ( 1 - 2 ) * 3") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "999999 + 1 - 999999 * 0 + 999999 / 1") == 1999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "999999 + 1 - 999999 * 0 + 999999 / 1") == 1999999: {e}')
    
    total += 1
    try:
        result = candidate(s = "12 + 34 * 56 / 78 - 90 + 12") == -42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "12 + 34 * 56 / 78 - 90 + 12") == -42: {e}')
    
    total += 1
    try:
        result = candidate(s = " 2 * (3 + 4 * (5 - 6 / 2)) + 7") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 2 * (3 + 4 * (5 - 6 / 2)) + 7") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "2 + 3 * 5 / 2 - 8 / 4 + 6") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2 + 3 * 5 / 2 - 8 / 4 + 6") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "5 * 5 * 5 * 5 * 5 / 5 + 5 - 5") == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5 * 5 * 5 * 5 * 5 / 5 + 5 - 5") == 625: {e}')
    
    total += 1
    try:
        result = candidate(s = "3 * 3 + 3 / 3 * 3 - 3") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3 * 3 + 3 / 3 * 3 - 3") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = " 100 - 25 * 2 + 50 / 5 - 10") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 100 - 25 * 2 + 50 / 5 - 10") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = " 2 * 3 + ( 2 * ( 1 + 4 ) / 2 ) - 5 ") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 2 * 3 + ( 2 * ( 1 + 4 ) / 2 ) - 5 ") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "333333 + 222222 * 1 - 111111 / 1") == 444444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "333333 + 222222 * 1 - 111111 / 1") == 444444: {e}')
    
    total += 1
    try:
        result = candidate(s = "2222 + 1111 * 2 - 3333 / 11 + 4444") == 8585
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2222 + 1111 * 2 - 3333 / 11 + 4444") == 8585: {e}')
    
    total += 1
    try:
        result = candidate(s = " 1000 - 500 * 2 + 250 / 50 * 20") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 1000 - 500 * 2 + 250 / 50 * 20") == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = " 99 * 100 - 99 * 99 + 99 * 98") == 9801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 99 * 100 - 99 * 99 + 99 * 98") == 9801: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 / 2 + 15 * 3 - 7 * (5 - 3) + 20") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 / 2 + 15 * 3 - 7 * (5 - 3) + 20") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "10000 / 1000 + 200 * 2 - 500") == -90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10000 / 1000 + 200 * 2 - 500") == -90: {e}')
    
    total += 1
    try:
        result = candidate(s = " 33333 + 22222 - 11111 + 44444 * 55555 / 66666") == 81480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 33333 + 22222 - 11111 + 44444 * 55555 / 66666") == 81480: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000 * 2 / 25 + 100 - 50") == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000 * 2 / 25 + 100 - 50") == 130: {e}')
    
    total += 1
    try:
        result = candidate(s = "123456789 + 987654321 * 1 - 123456789 / 1") == 987654321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123456789 + 987654321 * 1 - 123456789 / 1") == 987654321: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 * 2 + 3 * 5 / 15 - 10") == 191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 * 2 + 3 * 5 / 15 - 10") == 191: {e}')
    
    total += 1
    try:
        result = candidate(s = " 2 * ( 3 + 4 * ( 5 - 6 ) / 7 ) - 8 ") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 2 * ( 3 + 4 * ( 5 - 6 ) / 7 ) - 8 ") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000 * 5 / 25 + 20 - 40") == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000 * 5 / 25 + 20 - 40") == 180: {e}')
    
    total += 1
    try:
        result = candidate(s = " 200 + 50 / 5 - 30 * 2 + 10") == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 200 + 50 / 5 - 30 * 2 + 10") == 160: {e}')
    
    total += 1
    try:
        result = candidate(s = "32 / 2 * 2 + 1 - 1") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "32 / 2 * 2 + 1 - 1") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = " 987654321 - 123456789 + 98765 * 43210 / 54321") == 864276095
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 987654321 - 123456789 + 98765 * 43210 / 54321") == 864276095: {e}')
    
    total += 1
    try:
        result = candidate(s = "    1234 + 5678 * 90 / 100 - 12345 / 5    ") == 3875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    1234 + 5678 * 90 / 100 - 12345 / 5    ") == 3875: {e}')
    
    total += 1
    try:
        result = candidate(s = " 3 + 8 * 10 / 5 - 2 ") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 3 + 8 * 10 / 5 - 2 ") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = " 7 + 3 * ( 10 / 2 ) - 5") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 7 + 3 * ( 10 / 2 ) - 5") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "  100 * 2 / 5 + 3 * (20 - 15)  ") == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "  100 * 2 / 5 + 3 * (20 - 15)  ") == 85: {e}')
    
    total += 1
    try:
        result = candidate(s = " 10 * 20 - 5 * 4 + 3 * 2 - 1 / 1 + 8 * 2") == 201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 10 * 20 - 5 * 4 + 3 * 2 - 1 / 1 + 8 * 2") == 201: {e}')
    
    total += 1
    try:
        result = candidate(s = "  8  *  (  4  /  2  )  +  12  -  6") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "  8  *  (  4  /  2  )  +  12  -  6") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = " 99 + 99 * 99 / 99 - 99 ") == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 99 + 99 * 99 / 99 - 99 ") == 99: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 - 50 + 25 - 12 + 6 - 3 + 1") == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 - 50 + 25 - 12 + 6 - 3 + 1") == 67: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000 * 2 + 300 - 50 / 2") == 2275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000 * 2 + 300 - 50 / 2") == 2275: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 + 200 * (300 - 150 / 50) - 400") == 59697
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 + 200 * (300 - 150 / 50) - 400") == 59697: {e}')
    
    total += 1
    try:
        result = candidate(s = "333 * 111 + 222 * 444 / 666 - 777 + 888") == 37222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "333 * 111 + 222 * 444 / 666 - 777 + 888") == 37222: {e}')
    
    total += 1
    try:
        result = candidate(s = "7 + 3 * (10 / 2) - 1") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "7 + 3 * (10 / 2) - 1") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "2 * 3 + 4 * 5 - 6 / 2 + 7") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2 * 3 + 4 * 5 - 6 / 2 + 7") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + 2) * 3 / 4 + 5 - 6") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + 2) * 3 / 4 + 5 - 6") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = " 123 + 456 * 789 / 321 ") == 1243
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 123 + 456 * 789 / 321 ") == 1243: {e}')
    
    total += 1
    try:
        result = candidate(s = "3 + 5 * 2 / 2 - 1") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3 + 5 * 2 / 2 - 1") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "   1000 + 2000 * 3000 - 4000 / 5000 + 6000 - 7000 * 8000 / 9000  ") == 6000778
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   1000 + 2000 * 3000 - 4000 / 5000 + 6000 - 7000 * 8000 / 9000  ") == 6000778: {e}')
    
    total += 1
    try:
        result = candidate(s = " 1000 + 2000 - 3000 * (4000 / 5000) + 6000 - 7000 * (8000 / 9000)") == 378
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 1000 + 2000 - 3000 * (4000 / 5000) + 6000 - 7000 * (8000 / 9000)") == 378: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 * 10 - 9 * 9 + 8 * 8 - 7 * 7 + 6 * 6") == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 * 10 - 9 * 9 + 8 * 8 - 7 * 7 + 6 * 6") == 70: {e}')
    
    total += 1
    try:
        result = candidate(s = " 1000 * 2000 - 3000 + 4000 / 5000 * 6000") == 1997000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 1000 * 2000 - 3000 + 4000 / 5000 * 6000") == 1997000: {e}')
    
    total += 1
    try:
        result = candidate(s = " 2147483647 + 1 * 2 - 3 / 4") == 2147483649
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 2147483647 + 1 * 2 - 3 / 4") == 2147483649: {e}')
    
    total += 1
    try:
        result = candidate(s = " (10 + (20 + (30 + (40 + (50 + (60 + (70 + (80 + (90 + 100)))))))) ") == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " (10 + (20 + (30 + (40 + (50 + (60 + (70 + (80 + (90 + 100)))))))) ") == 550: {e}')
    
    total += 1
    try:
        result = candidate(s = " 100 + 200 - 300 * 400 / 500 + 600 * 700 / 800") == 585
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 100 + 200 - 300 * 400 / 500 + 600 * 700 / 800") == 585: {e}')
    
    total += 1
    try:
        result = candidate(s = " 4 + 5 * 6 / 3 - 7 + 8 * 2") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 4 + 5 * 6 / 3 - 7 + 8 * 2") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = " 1 + 2 * ( 3 + 4 ) / 2 - 1 ") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 1 + 2 * ( 3 + 4 ) / 2 - 1 ") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = " 1234 + 5678 - 91011 * 121314 / 151617") == -65909
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 1234 + 5678 - 91011 * 121314 / 151617") == -65909: {e}')
    
    total += 1
    try:
        result = candidate(s = " 999 + 1 * 1000 - 500 / 2 ") == 1749
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 999 + 1 * 1000 - 500 / 2 ") == 1749: {e}')
    
    total += 1
    try:
        result = candidate(s = " 100 * 2 + 3 - 4 / 2 ") == 201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 100 * 2 + 3 - 4 / 2 ") == 201: {e}')
    
    total += 1
    try:
        result = candidate(s = " 0 + 0 * 0 - 0 / 1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 0 + 0 * 0 - 0 / 1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = " 7 + 14 / 7 - 3 + 6 * 2") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 7 + 14 / 7 - 3 + 6 * 2") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "0 * 1 + 2 - 3 / 4 * 5") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0 * 1 + 2 - 3 / 4 * 5") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = " 123 + 456 * 789 / 101 - 234") == 3451
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 123 + 456 * 789 / 101 - 234") == 3451: {e}')
    
    total += 1
    try:
        result = candidate(s = " 12345 + 67890 - 54321 / 1234 * 5678  ") == -169597
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 12345 + 67890 - 54321 / 1234 * 5678  ") == -169597: {e}')
    
    total += 1
    try:
        result = candidate(s = " 123 + 456 - 789 * 1011 / 1213") == -78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 123 + 456 - 789 * 1011 / 1213") == -78: {e}')
    
    total += 1
    try:
        result = candidate(s = "   3   *   5   /   15   +   10   -   7   ") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   3   *   5   /   15   +   10   -   7   ") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = " 100 - 50 + 25 * 4 / 2 ") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 100 - 50 + 25 * 4 / 2 ") == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 + 20 * (30 / 10) - 5") == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 + 20 * (30 / 10) - 5") == 65: {e}')
    
    total += 1
    try:
        result = candidate(s = " 99999 + 88888 - 77777 * 66666 / 55555") == 95555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 99999 + 88888 - 77777 * 66666 / 55555") == 95555: {e}')
    
    total += 1
    try:
        result = candidate(s = " 100 + 200 * (300 / 50) - 600 + 700 * 800 / 900 ") == 1322
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 100 + 200 * (300 / 50) - 600 + 700 * 800 / 900 ") == 1322: {e}')
    
    total += 1
    try:
        result = candidate(s = "999999 / 3 + 999999 / 3 - 999999 / 3") == 333333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "999999 / 3 + 999999 / 3 - 999999 / 3") == 333333: {e}')
    
    total += 1
    try:
        result = candidate(s = " 1000 / ( 500 / 250 ) - 250 + 125 * ( 500 / 250 )") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 1000 / ( 500 / 250 ) - 250 + 125 * ( 500 / 250 )") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = " 2 * 3 + 4 * 5 - 6 / 3 + 8") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 2 * 3 + 4 * 5 - 6 / 3 + 8") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "987654 * 321 / 1000 + 123456 - 789012 / 3") == 177488
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "987654 * 321 / 1000 + 123456 - 789012 / 3") == 177488: {e}')
    
    total += 1
    try:
        result = candidate(s = " 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 ") == 3628800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 ") == 3628800: {e}')
    
    total += 1
    try:
        result = candidate(s = "   42  *   2   -   5   /   1   +   3   ") == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   42  *   2   -   5   /   1   +   3   ") == 82: {e}')
    
    total += 1
    try:
        result = candidate(s = " 2 * ( 3 + 5 ) * 4") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 2 * ( 3 + 5 ) * 4") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "30 / 5 * 2 - 1 + 4 * 8 - 3") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "30 / 5 * 2 - 1 + 4 * 8 - 3") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = " 1 + (2 + (3 + (4 + (5 + 6))))") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 1 + (2 + (3 + (4 + (5 + 6))))") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = " 123456789 + 987654321 - 111111111 * 222222222 / 333333333") == 1037037036
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 123456789 + 987654321 - 111111111 * 222222222 / 333333333") == 1037037036: {e}')
    
    total += 1
    try:
        result = candidate(s = "123 + 456 * 789 / 101 - 234") == 3451
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123 + 456 * 789 / 101 - 234") == 3451: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = " 1000 / ( 25 / 5 ) + 50 - 20") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 1000 / ( 25 / 5 ) + 50 - 20") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = " 5 + 3 * (2 - 8) + 4 / 2") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 5 + 3 * (2 - 8) + 4 / 2") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "987654321 - 123456789 + 111111111 * 222222222 / 333333333  ") == 938271606
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "987654321 - 123456789 + 111111111 * 222222222 / 333333333  ") == 938271606: {e}')
    
    total += 1
    try:
        result = candidate(s = " 8 / 3 + 4 * ( 5 - 3 ) / 2 ") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 8 / 3 + 4 * ( 5 - 3 ) / 2 ") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = " 5 * 6 + 20 / 4 - 8") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 5 * 6 + 20 / 4 - 8") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = " 3 + 8 * ( 4 - 2 ) / 2") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 3 + 8 * ( 4 - 2 ) / 2") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = " 5 + 3 * ( 20 / 4 ) ") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 5 + 3 * ( 20 / 4 ) ") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000000 + 500000 * 2 - 250000 / 5 + 125000") == 2075000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000000 + 500000 * 2 - 250000 / 5 + 125000") == 2075000: {e}')
    
    total += 1
    try:
        result = candidate(s = "2 + 3 * 4 - 5 / 2 + 6 * 7 - 8 / 4") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2 + 3 * 4 - 5 / 2 + 6 * 7 - 8 / 4") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = " 1000 - 500 + 250 * 2 - 125 ") == 875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 1000 - 500 + 250 * 2 - 125 ") == 875: {e}')
    
    total += 1
    try:
        result = candidate(s = "0 * 0 + 0 / 1 + 100 - 50") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0 * 0 + 0 / 1 + 100 - 50") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = " 10 + 20 + 30 + 40 + 50 - ( 10 * 5 )") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 10 + 20 + 30 + 40 + 50 - ( 10 * 5 )") == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = " 7 * 8 - 3 + 2 * 4 ") == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 7 * 8 - 3 + 2 * 4 ") == 61: {e}')
    
    total += 1
    try:
        result = candidate(s = "9 * 3 + 2 - 1 / 1 + 8 * 2") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "9 * 3 + 2 - 1 / 1 + 8 * 2") == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "50 * 50 - 50 / 50 + 50 * 50 - 50 / 50") == 4998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "50 * 50 - 50 / 50 + 50 * 50 - 50 / 50") == 4998: {e}')
    
    total += 1
    try:
        result = candidate(s = " 3 + (2 * (2 + (2 * (2 + 2))))") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 3 + (2 * (2 + (2 * (2 + 2))))") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 * 2 + 12 / 3 - 50") == 154
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 * 2 + 12 / 3 - 50") == 154: {e}')
    
    total += 1
    try:
        result = candidate(s = "3 + 33 + 333 + 3333 + 33333 + 333333 + 3333333 + 33333333 + 333333333") == 370370367
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3 + 33 + 333 + 3333 + 33333 + 333333 + 3333333 + 33333333 + 333333333") == 370370367: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 + 2 * 3 + 4 / 2 - 5") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 + 2 * 3 + 4 / 2 - 5") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = " 3 + 5 * ( 2 + 8 ) / 4 - 2 ") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 3 + 5 * ( 2 + 8 ) / 4 - 2 ") == 13: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "2 - 3 + 4") == 3
    assert candidate(s = " 1000000000 - 500000000 + 250000000") == 750000000
    assert candidate(s = "30 + 2 * 6 / (3 - 1)") == 33
    assert candidate(s = "100 * ( 2 + 12 ) / 14") == 200
    assert candidate(s = "1 + 1 * 1 + 1") == 3
    assert candidate(s = "2*3+4/5") == 6
    assert candidate(s = "3 + 5 / ( 2 + 3 )") == 8
    assert candidate(s = "0 + 0") == 0
    assert candidate(s = "100*2+12") == 212
    assert candidate(s = "2147483647 + 1 - 1") == 2147483647
    assert candidate(s = "100000 + 100000 - 50000 * 2 + 25000 * 4 / 5") == 120000
    assert candidate(s = "100 * 2 + 12") == 212
    assert candidate(s = " 200 - 3 * 50 + 25") == 75
    assert candidate(s = "10 + 2 * 6") == 22
    assert candidate(s = "3+2*2") == 7
    assert candidate(s = " 30 + 2 * 6 - 12 / 3 ") == 38
    assert candidate(s = "100*(2+12)/14") == 200
    assert candidate(s = " 3+5 / 2 ") == 5
    assert candidate(s = "1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10") == 3628800
    assert candidate(s = "100 * 2 / 25") == 8
    assert candidate(s = " 0 + 0 * 1 / 1") == 0
    assert candidate(s = " 3/2 ") == 1
    assert candidate(s = "3 + 5 - ( 2 + 3 )") == 9
    assert candidate(s = "2147483647 - 2147483646") == 1
    assert candidate(s = "3+5 / 2 * 3") == 9
    assert candidate(s = "3 + 2 * 2 + 1 - 5 / 2") == 6
    assert candidate(s = "10 * 5 + 3") == 53
    assert candidate(s = "3+5-2*3/4") == 7
    assert candidate(s = "3 + 5 / 2 + 3") == 8
    assert candidate(s = "1000 / 10 / 10") == 10
    assert candidate(s = "3 + 5 / 2 - 8 * 3 + 4 / 2") == -17
    assert candidate(s = "1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1") == 10
    assert candidate(s = " 30 / 3 + 10 * 2 - 5") == 25
    assert candidate(s = "100*(2+12)") == 212
    assert candidate(s = "100 * ( 2 + 12 )") == 212
    assert candidate(s = " 1 + 2 * 3 / 4 + 5 * 6 - 7") == 25
    assert candidate(s = "( 2 + 6 ) * 3 + 8") == 28
    assert candidate(s = "(2 + 6 * 3 + 5 - (3 * 14 / 7 + 2) * 5) + 3") == 32
    assert candidate(s = "2147483647 / 1") == 2147483647
    assert candidate(s = "1 - 1 + 1") == 1
    assert candidate(s = "2*3+4/5*6-7+8") == 7
    assert candidate(s = "10 + 2 - 5") == 7
    assert candidate(s = " 30 /3 + 10 * 2 ") == 30
    assert candidate(s = "2 * 3 + 4 / 5") == 6
    assert candidate(s = "3 + 2 * 2 + 1") == 8
    assert candidate(s = "10+2*6") == 22
    assert candidate(s = "3 + ( 2 * 2 )") == 7
    assert candidate(s = "123 + 456 * 789 / 100 - 987") == 2733
    assert candidate(s = "1000 - 500 * 2 + 250 / 5") == 50
    assert candidate(s = " 100000 - 50000 * 2 + 25000 / 5000 * 20000") == 100000
    assert candidate(s = "987654 * 321 / 123 - 456789 + 987654") == 3108401
    assert candidate(s = " 1 + 2 - 3 * (4 / 5) + 6 - 7 * 8 / 9") == 1
    assert candidate(s = "   8 *    5 / 4 + 3 - 1") == 12
    assert candidate(s = " 2000 / 10 + 50 * 2 - 300 ") == 0
    assert candidate(s = " 1234 + 567 * 89 - 101112 / 1314") == 51621
    assert candidate(s = " (123 + 456) * 789 - 101112 / (13 * 14) ") == 251029
    assert candidate(s = "1 * 2 + 3 * 4 + 5 * 6 + 7 * 8 + 9 * 10") == 190
    assert candidate(s = "100 / 10 - 90 * 0 + 80 / 8") == 20
    assert candidate(s = " 1000000 - 500000 + 250000 * 2 - 125000 ") == 875000
    assert candidate(s = "1000 - 500 * 2 / 5 + 300 / 3") == 900
    assert candidate(s = " 1000 + 2000 - (3000 / 4000 + 5000 - 6000 * (7000 / 8000))") == 2750
    assert candidate(s = " 200 * 5 + 300 / 100 - 10 ") == 993
    assert candidate(s = "123 + 456 * 789 - 101112 / 1314") == 359831
    assert candidate(s = " 5 + 4 - 3 * 2 + 1 / 1") == 4
    assert candidate(s = " ( 100 + 200 ) * ( 300 - 100 ) / 50") == 60098
    assert candidate(s = "7 * 8 * 9 / 6 + 5 - 3 * 2") == 83
    assert candidate(s = "300 + 200 * 5 / 10 - 25") == 375
    assert candidate(s = "100 * 200 / 500 + 200 - 100") == 140
    assert candidate(s = "100000 / 100 - 99999 * 0 + 1") == 1001
    assert candidate(s = "   42   *   (5 - 3) / 2 + 8  ") == 217
    assert candidate(s = "   23 + 56 * 99 / 77 - 44   ") == 51
    assert candidate(s = "100 * 2 + 12 / 3 - 5") == 199
    assert candidate(s = "   123 + 456 - 789 * 0 / 1 + 1000   ") == 1579
    assert candidate(s = "33 + 22 * 11 - 44 / 11 + 55") == 326
    assert candidate(s = "3 * 3 * 3 * 3 * 3 - 3 * 3 * 3 + 3") == 219
    assert candidate(s = "2147483647 - 2147483646 + 1") == 2
    assert candidate(s = "10 + 2 * 6 / ( 1 - 2 ) * 3") == 16
    assert candidate(s = "999999 + 1 - 999999 * 0 + 999999 / 1") == 1999999
    assert candidate(s = "12 + 34 * 56 / 78 - 90 + 12") == -42
    assert candidate(s = " 2 * (3 + 4 * (5 - 6 / 2)) + 7") == 30
    assert candidate(s = "2 + 3 * 5 / 2 - 8 / 4 + 6") == 13
    assert candidate(s = "5 * 5 * 5 * 5 * 5 / 5 + 5 - 5") == 625
    assert candidate(s = "3 * 3 + 3 / 3 * 3 - 3") == 9
    assert candidate(s = " 100 - 25 * 2 + 50 / 5 - 10") == 50
    assert candidate(s = " 2 * 3 + ( 2 * ( 1 + 4 ) / 2 ) - 5 ") == 5
    assert candidate(s = "333333 + 222222 * 1 - 111111 / 1") == 444444
    assert candidate(s = "2222 + 1111 * 2 - 3333 / 11 + 4444") == 8585
    assert candidate(s = " 1000 - 500 * 2 + 250 / 50 * 20") == 100
    assert candidate(s = " 99 * 100 - 99 * 99 + 99 * 98") == 9801
    assert candidate(s = "10 / 2 + 15 * 3 - 7 * (5 - 3) + 20") == 32
    assert candidate(s = "10000 / 1000 + 200 * 2 - 500") == -90
    assert candidate(s = " 33333 + 22222 - 11111 + 44444 * 55555 / 66666") == 81480
    assert candidate(s = "1000 * 2 / 25 + 100 - 50") == 130
    assert candidate(s = "123456789 + 987654321 * 1 - 123456789 / 1") == 987654321
    assert candidate(s = "100 * 2 + 3 * 5 / 15 - 10") == 191
    assert candidate(s = " 2 * ( 3 + 4 * ( 5 - 6 ) / 7 ) - 8 ") == 18
    assert candidate(s = "1000 * 5 / 25 + 20 - 40") == 180
    assert candidate(s = " 200 + 50 / 5 - 30 * 2 + 10") == 160
    assert candidate(s = "32 / 2 * 2 + 1 - 1") == 32
    assert candidate(s = " 987654321 - 123456789 + 98765 * 43210 / 54321") == 864276095
    assert candidate(s = "    1234 + 5678 * 90 / 100 - 12345 / 5    ") == 3875
    assert candidate(s = " 3 + 8 * 10 / 5 - 2 ") == 17
    assert candidate(s = " 7 + 3 * ( 10 / 2 ) - 5") == 17
    assert candidate(s = "  100 * 2 / 5 + 3 * (20 - 15)  ") == 85
    assert candidate(s = " 10 * 20 - 5 * 4 + 3 * 2 - 1 / 1 + 8 * 2") == 201
    assert candidate(s = "  8  *  (  4  /  2  )  +  12  -  6") == 22
    assert candidate(s = " 99 + 99 * 99 / 99 - 99 ") == 99
    assert candidate(s = "100 - 50 + 25 - 12 + 6 - 3 + 1") == 67
    assert candidate(s = "1000 * 2 + 300 - 50 / 2") == 2275
    assert candidate(s = "100 + 200 * (300 - 150 / 50) - 400") == 59697
    assert candidate(s = "333 * 111 + 222 * 444 / 666 - 777 + 888") == 37222
    assert candidate(s = "7 + 3 * (10 / 2) - 1") == 21
    assert candidate(s = "2 * 3 + 4 * 5 - 6 / 2 + 7") == 30
    assert candidate(s = "(1 + 2) * 3 / 4 + 5 - 6") == 1
    assert candidate(s = " 123 + 456 * 789 / 321 ") == 1243
    assert candidate(s = "3 + 5 * 2 / 2 - 1") == 7
    assert candidate(s = "   1000 + 2000 * 3000 - 4000 / 5000 + 6000 - 7000 * 8000 / 9000  ") == 6000778
    assert candidate(s = " 1000 + 2000 - 3000 * (4000 / 5000) + 6000 - 7000 * (8000 / 9000)") == 378
    assert candidate(s = "10 * 10 - 9 * 9 + 8 * 8 - 7 * 7 + 6 * 6") == 70
    assert candidate(s = " 1000 * 2000 - 3000 + 4000 / 5000 * 6000") == 1997000
    assert candidate(s = " 2147483647 + 1 * 2 - 3 / 4") == 2147483649
    assert candidate(s = " (10 + (20 + (30 + (40 + (50 + (60 + (70 + (80 + (90 + 100)))))))) ") == 550
    assert candidate(s = " 100 + 200 - 300 * 400 / 500 + 600 * 700 / 800") == 585
    assert candidate(s = " 4 + 5 * 6 / 3 - 7 + 8 * 2") == 23
    assert candidate(s = " 1 + 2 * ( 3 + 4 ) / 2 - 1 ") == 8
    assert candidate(s = " 1234 + 5678 - 91011 * 121314 / 151617") == -65909
    assert candidate(s = " 999 + 1 * 1000 - 500 / 2 ") == 1749
    assert candidate(s = " 100 * 2 + 3 - 4 / 2 ") == 201
    assert candidate(s = " 0 + 0 * 0 - 0 / 1") == 0
    assert candidate(s = " 7 + 14 / 7 - 3 + 6 * 2") == 18
    assert candidate(s = "0 * 1 + 2 - 3 / 4 * 5") == 2
    assert candidate(s = " 123 + 456 * 789 / 101 - 234") == 3451
    assert candidate(s = " 12345 + 67890 - 54321 / 1234 * 5678  ") == -169597
    assert candidate(s = " 123 + 456 - 789 * 1011 / 1213") == -78
    assert candidate(s = "   3   *   5   /   15   +   10   -   7   ") == 4
    assert candidate(s = " 100 - 50 + 25 * 4 / 2 ") == 100
    assert candidate(s = "10 + 20 * (30 / 10) - 5") == 65
    assert candidate(s = " 99999 + 88888 - 77777 * 66666 / 55555") == 95555
    assert candidate(s = " 100 + 200 * (300 / 50) - 600 + 700 * 800 / 900 ") == 1322
    assert candidate(s = "999999 / 3 + 999999 / 3 - 999999 / 3") == 333333
    assert candidate(s = " 1000 / ( 500 / 250 ) - 250 + 125 * ( 500 / 250 )") == 0
    assert candidate(s = " 2 * 3 + 4 * 5 - 6 / 3 + 8") == 32
    assert candidate(s = "987654 * 321 / 1000 + 123456 - 789012 / 3") == 177488
    assert candidate(s = " 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 ") == 3628800
    assert candidate(s = "   42  *   2   -   5   /   1   +   3   ") == 82
    assert candidate(s = " 2 * ( 3 + 5 ) * 4") == 26
    assert candidate(s = "30 / 5 * 2 - 1 + 4 * 8 - 3") == 40
    assert candidate(s = " 1 + (2 + (3 + (4 + (5 + 6))))") == 21
    assert candidate(s = " 123456789 + 987654321 - 111111111 * 222222222 / 333333333") == 1037037036
    assert candidate(s = "123 + 456 * 789 / 101 - 234") == 3451
    assert candidate(s = "1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10") == 55
    assert candidate(s = " 1000 / ( 25 / 5 ) + 50 - 20") == 38
    assert candidate(s = " 5 + 3 * (2 - 8) + 4 / 2") == 5
    assert candidate(s = "987654321 - 123456789 + 111111111 * 222222222 / 333333333  ") == 938271606
    assert candidate(s = " 8 / 3 + 4 * ( 5 - 3 ) / 2 ") == 21
    assert candidate(s = " 5 * 6 + 20 / 4 - 8") == 27
    assert candidate(s = " 3 + 8 * ( 4 - 2 ) / 2") == 34
    assert candidate(s = " 5 + 3 * ( 20 / 4 ) ") == 20
    assert candidate(s = "1000000 + 500000 * 2 - 250000 / 5 + 125000") == 2075000
    assert candidate(s = "2 + 3 * 4 - 5 / 2 + 6 * 7 - 8 / 4") == 52
    assert candidate(s = " 1000 - 500 + 250 * 2 - 125 ") == 875
    assert candidate(s = "0 * 0 + 0 / 1 + 100 - 50") == 50
    assert candidate(s = " 10 + 20 + 30 + 40 + 50 - ( 10 * 5 )") == 100
    assert candidate(s = " 7 * 8 - 3 + 2 * 4 ") == 61
    assert candidate(s = "9 * 3 + 2 - 1 / 1 + 8 * 2") == 44
    assert candidate(s = "50 * 50 - 50 / 50 + 50 * 50 - 50 / 50") == 4998
    assert candidate(s = " 3 + (2 * (2 + (2 * (2 + 2))))") == 13
    assert candidate(s = "100 * 2 + 12 / 3 - 50") == 154
    assert candidate(s = "3 + 33 + 333 + 3333 + 33333 + 333333 + 3333333 + 33333333 + 333333333") == 370370367
    assert candidate(s = "1 + 2 * 3 + 4 / 2 - 5") == 4
    assert candidate(s = " 3 + 5 * ( 2 + 8 ) / 4 - 2 ") == 13


