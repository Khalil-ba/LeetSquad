def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 45) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 729) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 729) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 19683) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19683) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 244) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 244) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = -1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -1) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = -27) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -27) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = -2147483648) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -2147483648) == False: {e}')
    
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
        result = candidate(n = 2187) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2187) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = -81) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -81) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = -243) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -243) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = -3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -3) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 243) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 243) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 59049) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 59049) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 14124) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14124) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 239148450531289) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 239148450531289) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 32805) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32805) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483646) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483646) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 797161567330890596) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 797161567330890596) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 12157665459056928802) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12157665459056928802) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4096) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4096) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = -9) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -9) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 82) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 82) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 387420489) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 387420489) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1594323) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1594323) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 28) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 12157665459056928801) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12157665459056928801) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = -19683) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -19683) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = -162) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -162) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 59050) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 59050) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1162261469) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1162261469) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = -6561) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -6561) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 80) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 14348907) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14348907) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741824) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741824) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 282429536481) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 282429536481) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 231) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 231) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4052555153018976267) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4052555153018976267) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 3645) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3645) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = -59049) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -59049) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1594322) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1594322) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 177147) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 177147) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = -45) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -45) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1162261467) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1162261467) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2188) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2188) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 531441) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 531441) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 24) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 129140163) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 129140163) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 43046721) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 43046721) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = -1046527) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -1046527) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1162261468) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1162261468) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1162261466) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1162261466) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 3486784401) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3486784401) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1111111111) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111111111) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2125764400) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2125764400) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == True
    assert candidate(n = 45) == False
    assert candidate(n = 729) == True
    assert candidate(n = 2147483647) == False
    assert candidate(n = 19683) == True
    assert candidate(n = 100) == False
    assert candidate(n = 244) == False
    assert candidate(n = 10) == False
    assert candidate(n = -1) == False
    assert candidate(n = -27) == False
    assert candidate(n = 0) == False
    assert candidate(n = -2147483648) == False
    assert candidate(n = 27) == True
    assert candidate(n = 6561) == True
    assert candidate(n = 2187) == True
    assert candidate(n = 1000000000) == False
    assert candidate(n = 81) == True
    assert candidate(n = -81) == False
    assert candidate(n = -243) == False
    assert candidate(n = 9) == True
    assert candidate(n = -3) == False
    assert candidate(n = 1) == True
    assert candidate(n = 243) == True
    assert candidate(n = 59049) == True
    assert candidate(n = 14124) == False
    assert candidate(n = 239148450531289) == False
    assert candidate(n = 32805) == False
    assert candidate(n = 2147483646) == False
    assert candidate(n = 797161567330890596) == False
    assert candidate(n = 12157665459056928802) == False
    assert candidate(n = 4096) == False
    assert candidate(n = -9) == False
    assert candidate(n = 82) == False
    assert candidate(n = 387420489) == True
    assert candidate(n = 1594323) == True
    assert candidate(n = 1000) == False
    assert candidate(n = 5) == False
    assert candidate(n = 28) == False
    assert candidate(n = 12157665459056928801) == True
    assert candidate(n = -19683) == False
    assert candidate(n = -162) == False
    assert candidate(n = 4) == False
    assert candidate(n = 59050) == False
    assert candidate(n = 2) == False
    assert candidate(n = 1162261469) == False
    assert candidate(n = -6561) == False
    assert candidate(n = 80) == False
    assert candidate(n = 14348907) == True
    assert candidate(n = 1073741824) == False
    assert candidate(n = 282429536481) == True
    assert candidate(n = 100000) == False
    assert candidate(n = 231) == False
    assert candidate(n = 4052555153018976267) == True
    assert candidate(n = 3645) == False
    assert candidate(n = -59049) == False
    assert candidate(n = 18) == False
    assert candidate(n = 500) == False
    assert candidate(n = 1594322) == False
    assert candidate(n = 20) == False
    assert candidate(n = 177147) == True
    assert candidate(n = -45) == False
    assert candidate(n = 19) == False
    assert candidate(n = 1162261467) == True
    assert candidate(n = 2188) == False
    assert candidate(n = 531441) == True
    assert candidate(n = 24) == False
    assert candidate(n = 129140163) == True
    assert candidate(n = 43046721) == True
    assert candidate(n = -1046527) == False
    assert candidate(n = 1162261468) == False
    assert candidate(n = 1162261466) == False
    assert candidate(n = 3486784401) == True
    assert candidate(n = 200) == False
    assert candidate(n = 6) == False
    assert candidate(n = 1111111111) == False
    assert candidate(n = 2125764400) == False


