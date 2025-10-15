def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3,k = 1) == "123"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 1) == "123": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 40320) == "87654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 40320) == "87654321": {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 9) == "2314"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 9) == "2314": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 362880) == "987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 362880) == "987654321": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 10) == "13452"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 10) == "13452": {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 3) == "213"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 3) == "213": {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 1) == "12"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 1) == "12": {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 2) == "21"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 2) == "21": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 720) == "654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 720) == "654321": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 5040) == "7654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 5040) == "7654321": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 1) == "12345"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 1) == "12345": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 120) == "54321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 120) == "54321": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 362879) == "987654312"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 362879) == "987654312": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 60) == "32541"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 60) == "32541": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 25921) == "62134578"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 25921) == "62134578": {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 11) == "2413"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 11) == "2413": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 181440) == "549876321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 181440) == "549876321": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 399) == "425316"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 399) == "425316": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 1) == "1234567"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 1) == "1234567": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 30240) == "68754321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 30240) == "68754321": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 359) == "365412"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 359) == "365412": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 119) == "54312"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 119) == "54312": {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 19) == "4123"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 19) == "4123": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 719) == "654312"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 719) == "654312": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 1) == "12345678"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 1) == "12345678": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 20161) == "51234678"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 20161) == "51234678": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 123456) == "416589732"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 123456) == "416589732": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 40321) == "1234567"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 40321) == "1234567": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 20160) == "48765321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 20160) == "48765321": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 100) == "162453"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 100) == "162453": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 360) == "365421"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 360) == "365421": {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 15) == "3214"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 15) == "3214": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 270000) == "764985321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 270000) == "764985321": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 100000) == "358926471"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 100000) == "358926471": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 2521) == "4512367"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 2521) == "4512367": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 3500) == "5716243"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 3500) == "5716243": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 50000) == "239574186"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 50000) == "239574186": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 326592) == "917548632"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 326592) == "917548632": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 5041) == "123456"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 5041) == "123456": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 274567) == "784315269"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 274567) == "784315269": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 391) == "423156"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 391) == "423156": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 500) == "516243"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 500) == "516243": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 1) == "123456"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 1) == "123456": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 25000) == "58624371"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 25000) == "58624371": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 12345) == "35184627"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 12345) == "35184627": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 181441) == "561234789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 181441) == "561234789": {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 24) == "4321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 24) == "4321": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 5000) == "7642153"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 5000) == "7642153": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 1000) == "2436571"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 1000) == "2436571": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 24) == "15432"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 24) == "15432": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 2520) == "4376521"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 2520) == "4376521": {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 4) == "1342"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 4) == "1342": {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 10) == "2341"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 10) == "2341": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 100) == "51342"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 100) == "51342": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 98765) == "357214968"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 98765) == "357214968": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 5039) == "7654312"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 5039) == "7654312": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 397) == "425136"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 397) == "425136": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 361) == "412356"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 361) == "412356": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3,k = 1) == "123"
    assert candidate(n = 8,k = 40320) == "87654321"
    assert candidate(n = 4,k = 9) == "2314"
    assert candidate(n = 9,k = 362880) == "987654321"
    assert candidate(n = 5,k = 10) == "13452"
    assert candidate(n = 3,k = 3) == "213"
    assert candidate(n = 2,k = 1) == "12"
    assert candidate(n = 2,k = 2) == "21"
    assert candidate(n = 6,k = 720) == "654321"
    assert candidate(n = 7,k = 5040) == "7654321"
    assert candidate(n = 5,k = 1) == "12345"
    assert candidate(n = 5,k = 120) == "54321"
    assert candidate(n = 9,k = 362879) == "987654312"
    assert candidate(n = 5,k = 60) == "32541"
    assert candidate(n = 8,k = 25921) == "62134578"
    assert candidate(n = 4,k = 11) == "2413"
    assert candidate(n = 9,k = 181440) == "549876321"
    assert candidate(n = 6,k = 399) == "425316"
    assert candidate(n = 7,k = 1) == "1234567"
    assert candidate(n = 8,k = 30240) == "68754321"
    assert candidate(n = 6,k = 359) == "365412"
    assert candidate(n = 5,k = 119) == "54312"
    assert candidate(n = 4,k = 19) == "4123"
    assert candidate(n = 6,k = 719) == "654312"
    assert candidate(n = 8,k = 1) == "12345678"
    assert candidate(n = 8,k = 20161) == "51234678"
    assert candidate(n = 9,k = 123456) == "416589732"
    assert candidate(n = 8,k = 40321) == "1234567"
    assert candidate(n = 8,k = 20160) == "48765321"
    assert candidate(n = 6,k = 100) == "162453"
    assert candidate(n = 6,k = 360) == "365421"
    assert candidate(n = 4,k = 15) == "3214"
    assert candidate(n = 9,k = 270000) == "764985321"
    assert candidate(n = 9,k = 100000) == "358926471"
    assert candidate(n = 7,k = 2521) == "4512367"
    assert candidate(n = 7,k = 3500) == "5716243"
    assert candidate(n = 9,k = 50000) == "239574186"
    assert candidate(n = 9,k = 326592) == "917548632"
    assert candidate(n = 7,k = 5041) == "123456"
    assert candidate(n = 9,k = 274567) == "784315269"
    assert candidate(n = 6,k = 391) == "423156"
    assert candidate(n = 6,k = 500) == "516243"
    assert candidate(n = 6,k = 1) == "123456"
    assert candidate(n = 8,k = 25000) == "58624371"
    assert candidate(n = 8,k = 12345) == "35184627"
    assert candidate(n = 9,k = 181441) == "561234789"
    assert candidate(n = 4,k = 24) == "4321"
    assert candidate(n = 7,k = 5000) == "7642153"
    assert candidate(n = 7,k = 1000) == "2436571"
    assert candidate(n = 5,k = 24) == "15432"
    assert candidate(n = 7,k = 2520) == "4376521"
    assert candidate(n = 4,k = 4) == "1342"
    assert candidate(n = 4,k = 10) == "2341"
    assert candidate(n = 5,k = 100) == "51342"
    assert candidate(n = 9,k = 98765) == "357214968"
    assert candidate(n = 7,k = 5039) == "7654312"
    assert candidate(n = 6,k = 397) == "425136"
    assert candidate(n = 6,k = 361) == "412356"


