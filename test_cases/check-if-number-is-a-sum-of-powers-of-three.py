def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 59049) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 59049) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 729) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 729) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 243) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 243) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 21) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4782969) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4782969) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 19683) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19683) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1594323) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1594323) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 40) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 59048) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 59048) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1093) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1093) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 27) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 6561) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6561) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 3645) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3645) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2187) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2187) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 177147) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 177147) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 91) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 91) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 531441) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 531441) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000001) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000001) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 98415) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98415) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 89076) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 89076) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999999) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999999) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 98416) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98416) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 39856) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 39856) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1640261) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1640261) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 59050) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 59050) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 9876543) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9876543) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 32804) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32804) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 819) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 819) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 14348907) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14348907) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 9841) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9841) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 810000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 810000) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 8191) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8191) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 72900) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 72900) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 524880) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524880) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 7290) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7290) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 59250) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 59250) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 109355) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 109355) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 10935) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10935) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 98414) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98414) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2391484) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2391484) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 88572) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 88572) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 32805) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32805) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 88573) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 88573) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1049755) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1049755) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 590490) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 590490) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 98411) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98411) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 6560) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6560) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4100) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4100) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 19684) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19684) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 531442) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 531442) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 49308) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49308) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 39858) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 39858) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 59047) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 59047) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 99018) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99018) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 98409) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98409) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 58324) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 58324) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 48619) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 48619) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 69192) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 69192) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 369059) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 369059) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4052555) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4052555) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1291401) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1291401) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 98413) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98413) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 3486784400) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3486784400) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 14348908) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14348908) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 131220) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131220) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 437400) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 437400) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4000000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4000000) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 981) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 981) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 97656) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 97656) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 3986) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3986) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 19682) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19682) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 797162) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 797162) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 656100) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 656100) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 3486784401) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3486784401) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 45927) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45927) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 79134) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 79134) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 3125) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3125) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2097152) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2097152) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 98410) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98410) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 728997) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 728997) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 405224) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 405224) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 31259) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31259) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 119050) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 119050) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 104976) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 104976) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 546789) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 546789) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 39366) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 39366) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 40000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40000) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 29524) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29524) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 98412) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98412) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 400) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 32806) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32806) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 3188646) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3188646) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 59049) == True
    assert candidate(n = 3) == True
    assert candidate(n = 729) == True
    assert candidate(n = 12) == True
    assert candidate(n = 243) == True
    assert candidate(n = 21) == False
    assert candidate(n = 4782969) == True
    assert candidate(n = 19683) == True
    assert candidate(n = 1594323) == True
    assert candidate(n = 40) == True
    assert candidate(n = 59048) == False
    assert candidate(n = 1093) == True
    assert candidate(n = 10000000) == False
    assert candidate(n = 100000) == False
    assert candidate(n = 27) == True
    assert candidate(n = 6561) == True
    assert candidate(n = 3645) == False
    assert candidate(n = 2187) == True
    assert candidate(n = 177147) == True
    assert candidate(n = 91) == True
    assert candidate(n = 81) == True
    assert candidate(n = 531441) == True
    assert candidate(n = 1000000) == False
    assert candidate(n = 1000001) == False
    assert candidate(n = 9) == True
    assert candidate(n = 98415) == False
    assert candidate(n = 1) == True
    assert candidate(n = 10) == True
    assert candidate(n = 89076) == False
    assert candidate(n = 9999999) == False
    assert candidate(n = 98416) == False
    assert candidate(n = 39856) == False
    assert candidate(n = 1640261) == False
    assert candidate(n = 59050) == True
    assert candidate(n = 9876543) == False
    assert candidate(n = 32804) == False
    assert candidate(n = 819) == True
    assert candidate(n = 14348907) == True
    assert candidate(n = 9841) == True
    assert candidate(n = 8) == False
    assert candidate(n = 810000) == False
    assert candidate(n = 8191) == False
    assert candidate(n = 72900) == False
    assert candidate(n = 524880) == False
    assert candidate(n = 7290) == True
    assert candidate(n = 11) == False
    assert candidate(n = 1048575) == False
    assert candidate(n = 59250) == False
    assert candidate(n = 109355) == False
    assert candidate(n = 10935) == False
    assert candidate(n = 98414) == False
    assert candidate(n = 2391484) == True
    assert candidate(n = 88572) == True
    assert candidate(n = 32805) == False
    assert candidate(n = 88573) == True
    assert candidate(n = 50000) == False
    assert candidate(n = 1049755) == False
    assert candidate(n = 590490) == True
    assert candidate(n = 4) == True
    assert candidate(n = 98411) == False
    assert candidate(n = 6560) == False
    assert candidate(n = 4100) == False
    assert candidate(n = 19684) == True
    assert candidate(n = 531442) == True
    assert candidate(n = 49308) == False
    assert candidate(n = 39858) == False
    assert candidate(n = 59047) == False
    assert candidate(n = 99018) == False
    assert candidate(n = 98409) == False
    assert candidate(n = 58324) == False
    assert candidate(n = 48619) == False
    assert candidate(n = 69192) == False
    assert candidate(n = 369059) == False
    assert candidate(n = 4052555) == False
    assert candidate(n = 1291401) == False
    assert candidate(n = 98413) == False
    assert candidate(n = 3486784400) == False
    assert candidate(n = 14348908) == True
    assert candidate(n = 131220) == False
    assert candidate(n = 437400) == False
    assert candidate(n = 2) == False
    assert candidate(n = 4000000) == False
    assert candidate(n = 981) == True
    assert candidate(n = 97656) == False
    assert candidate(n = 3986) == False
    assert candidate(n = 19682) == False
    assert candidate(n = 797162) == False
    assert candidate(n = 656100) == False
    assert candidate(n = 3486784401) == True
    assert candidate(n = 45927) == False
    assert candidate(n = 79134) == False
    assert candidate(n = 1234567) == False
    assert candidate(n = 3125) == False
    assert candidate(n = 2097152) == False
    assert candidate(n = 98410) == False
    assert candidate(n = 99999) == False
    assert candidate(n = 728997) == False
    assert candidate(n = 405224) == False
    assert candidate(n = 31259) == False
    assert candidate(n = 119050) == False
    assert candidate(n = 104976) == False
    assert candidate(n = 546789) == False
    assert candidate(n = 39366) == False
    assert candidate(n = 40000) == False
    assert candidate(n = 29524) == True
    assert candidate(n = 98412) == False
    assert candidate(n = 400) == False
    assert candidate(n = 32806) == False
    assert candidate(n = 3188646) == False
    assert candidate(n = 123456) == False


