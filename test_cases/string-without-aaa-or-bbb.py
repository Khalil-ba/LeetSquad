def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(a = 0,b = 5) == "bbbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 0,b = 5) == "bbbbb": {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 10) == "abababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 10) == "abababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 6,b = 4) == "aabaababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 6,b = 4) == "aabaababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = 7) == "ababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 7) == "ababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 4,b = 1) == "aabaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 4,b = 1) == "aabaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = 2) == "aabaabaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 2) == "aabaabaaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 4,b = 6) == "bbabbaabab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 4,b = 6) == "bbabbaabab": {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 2) == "bba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 2) == "bba": {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 5) == "ababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 5) == "ababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 0) == "aaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 0) == "aaaaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 0,b = 0) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 0,b = 0) == "": {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 2) == "aabaaba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 2) == "aabaaba": {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 2) == "abab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 2) == "abab": {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 7) == "bbabbabbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 7) == "bbabbabbb": {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 3) == "ababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 3) == "ababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 33,b = 67) == "bbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 33,b = 67) == "bbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbab": {e}')
    
    total += 1
    try:
        result = candidate(a = 15,b = 5) == "aabaabaabaabaabaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 15,b = 5) == "aabaabaabaabaabaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 30,b = 70) == "bbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbbbbbbbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 30,b = 70) == "bbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbbbbbbbbb": {e}')
    
    total += 1
    try:
        result = candidate(a = 33,b = 34) == "bbaabababababababababababababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 33,b = 34) == "bbaabababababababababababababababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 30,b = 25) == "aabaabaabaabaababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 30,b = 25) == "aabaabaabaabaababababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 100,b = 100) == "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100,b = 100) == "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 0,b = 100) == "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 0,b = 100) == "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb": {e}')
    
    total += 1
    try:
        result = candidate(a = 27,b = 3) == "aabaabaabaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 27,b = 3) == "aabaabaabaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 100,b = 0) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100,b = 0) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 8,b = 1) == "aabaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 8,b = 1) == "aabaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 100) == "bbabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 100) == "bbabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb": {e}')
    
    total += 1
    try:
        result = candidate(a = 100,b = 1) == "aabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100,b = 1) == "aabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 30,b = 30) == "abababababababababababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 30,b = 30) == "abababababababababababababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 30,b = 10) == "aabaabaabaabaabaabaabaabaabaabaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 30,b = 10) == "aabaabaabaabaabaabaabaabaabaabaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 20,b = 30) == "bbabbabbabbabbabbabbabbabbabbaabababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20,b = 30) == "bbabbabbabbabbabbabbabbabbabbaabababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 25,b = 25) == "ababababababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 25,b = 25) == "ababababababababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 20,b = 20) == "abababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20,b = 20) == "abababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 50,b = 51) == "bbaababababababababababababababababababababababababababababababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 50,b = 51) == "bbaababababababababababababababababababababababababababababababababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 33,b = 33) == "ababababababababababababababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 33,b = 33) == "ababababababababababababababababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 90) == "bbabbabbabbabbabbabbabbabbabbabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 90) == "bbabbabbabbabbabbabbabbabbabbabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb": {e}')
    
    total += 1
    try:
        result = candidate(a = 15,b = 15) == "ababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 15,b = 15) == "ababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 85,b = 15) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 85,b = 15) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 99,b = 1) == "aabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 99,b = 1) == "aabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 45,b = 55) == "bbabbabbabbabbabbabbabbabbabbaababababababababababababababababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 45,b = 55) == "bbabbabbabbabbabbabbabbabbabbaababababababababababababababababababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 99) == "bbabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 99) == "bbabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb": {e}')
    
    total += 1
    try:
        result = candidate(a = 49,b = 1) == "aabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 49,b = 1) == "aabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 35,b = 40) == "bbabbabbabbabbaabababababababababababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 35,b = 40) == "bbabbabbabbabbaabababababababababababababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 70,b = 30) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 70,b = 30) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = 3) == "aabaabaaba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 3) == "aabaabaaba": {e}')
    
    total += 1
    try:
        result = candidate(a = 25,b = 30) == "bbabbabbabbabbaabababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 25,b = 30) == "bbabbabbabbabbaabababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 75,b = 25) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 75,b = 25) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 34,b = 33) == "aababababababababababababababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 34,b = 33) == "aababababababababababababababababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 51,b = 50) == "aabababababababababababababababababababababababababababababababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 51,b = 50) == "aabababababababababababababababababababababababababababababababababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 49) == "bbabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 49) == "bbabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb": {e}')
    
    total += 1
    try:
        result = candidate(a = 90,b = 10) == "aabaabaabaabaabaabaabaabaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 90,b = 10) == "aabaabaabaabaabaabaabaabaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 80,b = 20) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 80,b = 20) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 30,b = 20) == "aabaabaabaabaabaabaabaabaabaababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 30,b = 20) == "aabaabaabaabaabaabaabaabaabaababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 40,b = 60) == "bbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbaabababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 40,b = 60) == "bbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbaabababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 50,b = 50) == "abababababababababababababababababababababababababababababababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 50,b = 50) == "abababababababababababababababababababababababababababababababababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 7) == "bbabbabbab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 7) == "bbabbabbab": {e}')
    
    total += 1
    try:
        result = candidate(a = 60,b = 40) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 60,b = 40) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaababababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 8,b = 25) == "bbabbabbabbabbabbabbabbabbbbbbbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 8,b = 25) == "bbabbabbabbabbabbabbabbabbbbbbbbb": {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 8) == "bbabbbbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 8) == "bbabbbbbb": {e}')
    
    total += 1
    try:
        result = candidate(a = 20,b = 15) == "aabaabaabaabaababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20,b = 15) == "aabaabaabaabaababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 15,b = 35) == "bbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 15,b = 35) == "bbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbbbb": {e}')
    
    total += 1
    try:
        result = candidate(a = 25,b = 75) == "bbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbbbbbbbbbbbbbbbbbbbbbbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 25,b = 75) == "bbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbbbbbbbbbbbbbbbbbbbbbbbb": {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 10) == "bbabbabbabbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 10) == "bbabbabbabbbb": {e}')
    
    total += 1
    try:
        result = candidate(a = 20,b = 80) == "bbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20,b = 80) == "bbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb": {e}')
    
    total += 1
    try:
        result = candidate(a = 55,b = 45) == "aabaabaabaabaabaabaabaabaabaabababababababababababababababababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 55,b = 45) == "aabaabaabaabaabaabaabaabaabaabababababababababababababababababababababababababababababababababababab": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(a = 0,b = 5) == "bbbbb"
    assert candidate(a = 10,b = 10) == "abababababababababab"
    assert candidate(a = 6,b = 4) == "aabaababab"
    assert candidate(a = 7,b = 7) == "ababababababab"
    assert candidate(a = 4,b = 1) == "aabaa"
    assert candidate(a = 7,b = 2) == "aabaabaaa"
    assert candidate(a = 4,b = 6) == "bbabbaabab"
    assert candidate(a = 1,b = 2) == "bba"
    assert candidate(a = 5,b = 5) == "ababababab"
    assert candidate(a = 5,b = 0) == "aaaaa"
    assert candidate(a = 0,b = 0) == ""
    assert candidate(a = 5,b = 2) == "aabaaba"
    assert candidate(a = 2,b = 2) == "abab"
    assert candidate(a = 2,b = 7) == "bbabbabbb"
    assert candidate(a = 3,b = 3) == "ababab"
    assert candidate(a = 33,b = 67) == "bbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbab"
    assert candidate(a = 15,b = 5) == "aabaabaabaabaabaaaaa"
    assert candidate(a = 30,b = 70) == "bbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbbbbbbbbb"
    assert candidate(a = 33,b = 34) == "bbaabababababababababababababababababababababababababababababababab"
    assert candidate(a = 30,b = 25) == "aabaabaabaabaababababababababababababababababababababab"
    assert candidate(a = 100,b = 100) == "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab"
    assert candidate(a = 0,b = 100) == "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    assert candidate(a = 27,b = 3) == "aabaabaabaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(a = 100,b = 0) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(a = 8,b = 1) == "aabaaaaaa"
    assert candidate(a = 1,b = 100) == "bbabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    assert candidate(a = 100,b = 1) == "aabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(a = 30,b = 30) == "abababababababababababababababababababababababababababababab"
    assert candidate(a = 30,b = 10) == "aabaabaabaabaabaabaabaabaabaabaaaaaaaaaa"
    assert candidate(a = 20,b = 30) == "bbabbabbabbabbabbabbabbabbabbaabababababababababab"
    assert candidate(a = 25,b = 25) == "ababababababababababababababababababababababababab"
    assert candidate(a = 20,b = 20) == "abababababababababababababababababababab"
    assert candidate(a = 50,b = 51) == "bbaababababababababababababababababababababababababababababababababababababababababababababababababab"
    assert candidate(a = 33,b = 33) == "ababababababababababababababababababababababababababababababababab"
    assert candidate(a = 10,b = 90) == "bbabbabbabbabbabbabbabbabbabbabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    assert candidate(a = 15,b = 15) == "ababababababababababababababab"
    assert candidate(a = 85,b = 15) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(a = 99,b = 1) == "aabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(a = 45,b = 55) == "bbabbabbabbabbabbabbabbabbabbaababababababababababababababababababababababababababababababababababab"
    assert candidate(a = 1,b = 99) == "bbabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    assert candidate(a = 49,b = 1) == "aabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(a = 35,b = 40) == "bbabbabbabbabbaabababababababababababababababababababababababababababababab"
    assert candidate(a = 70,b = 30) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaaaaaaaaaa"
    assert candidate(a = 7,b = 3) == "aabaabaaba"
    assert candidate(a = 25,b = 30) == "bbabbabbabbabbaabababababababababababababababababababab"
    assert candidate(a = 75,b = 25) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(a = 34,b = 33) == "aababababababababababababababababababababababababababababababababab"
    assert candidate(a = 51,b = 50) == "aabababababababababababababababababababababababababababababababababababababababababababababababababab"
    assert candidate(a = 1,b = 49) == "bbabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    assert candidate(a = 90,b = 10) == "aabaabaabaabaabaabaabaabaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(a = 80,b = 20) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert candidate(a = 30,b = 20) == "aabaabaabaabaabaabaabaabaabaababababababababababab"
    assert candidate(a = 40,b = 60) == "bbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbaabababababababababababababababababababab"
    assert candidate(a = 50,b = 50) == "abababababababababababababababababababababababababababababababababababababababababababababababababab"
    assert candidate(a = 3,b = 7) == "bbabbabbab"
    assert candidate(a = 60,b = 40) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaababababababababababababababababababababab"
    assert candidate(a = 8,b = 25) == "bbabbabbabbabbabbabbabbabbbbbbbbb"
    assert candidate(a = 1,b = 8) == "bbabbbbbb"
    assert candidate(a = 20,b = 15) == "aabaabaabaabaababababababababababab"
    assert candidate(a = 15,b = 35) == "bbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbbbb"
    assert candidate(a = 25,b = 75) == "bbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbbbbbbbbbbbbbbbbbbbbbbbb"
    assert candidate(a = 3,b = 10) == "bbabbabbabbbb"
    assert candidate(a = 20,b = 80) == "bbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    assert candidate(a = 55,b = 45) == "aabaabaabaabaabaabaabaabaabaabababababababababababababababababababababababababababababababababababab"


