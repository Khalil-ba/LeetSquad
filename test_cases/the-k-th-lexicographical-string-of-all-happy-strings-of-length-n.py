def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 10,k = 101) == "abacbabcab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 101) == "abacbabcab": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 1) == "ababa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 1) == "ababa": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 100) == "abacbabacb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 100) == "abacbabacb": {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 4) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 4) == "": {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 5) == "ca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 5) == "ca": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 25) == "bcaba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 25) == "bcaba": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 20) == "babcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 20) == "babcb": {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 3) == "c"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 3) == "c": {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 9) == "cab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 9) == "cab": {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 6) == "cb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 6) == "cb": {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 15) == "bcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 15) == "bcba": {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 1) == "ab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 1) == "ab": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 15) == "acbca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 15) == "acbca": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 30) == "bcbac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 30) == "bcbac": {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 12) == "cbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 12) == "cbc": {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 3) == "ba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 3) == "ba": {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 20) == "cacb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 20) == "cacb": {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 1) == "aba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 1) == "aba": {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 10) == "babc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 10) == "babc": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 30) == "ababcbcac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 30) == "ababcbcac": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 1024) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 1024) == "": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 33) == "abcababa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 33) == "abcababa": {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 13) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 13) == "": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 50) == "acbabac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 50) == "acbabac": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 1023) == "bcbcbcbcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 1023) == "bcbcbcbcba": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 127) == "bcbcbca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 127) == "bcbcbca": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 300) == "babcacacb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 300) == "babcacacb": {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 1) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 1) == "a": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 123) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 123) == "": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 1) == "abababa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 1) == "abababa": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 200) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 200) == "": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 27) == "acbaca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 27) == "acbaca": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 175) == "acacacbca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 175) == "acacacbca": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 10) == "abababcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 10) == "abababcabc": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 3) == "ababababca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 3) == "ababababca": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 1) == "ababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 1) == "ababababab": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 150) == "acabcacac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 150) == "acabcacac": {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 25) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 25) == "": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 150) == "babcacac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 150) == "babcacac": {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 7) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 7) == "": {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 15) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 15) == "": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 70) == "cabcac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 70) == "cabcac": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 30) == "acbcac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 30) == "acbcac": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 2048) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 2048) == "": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 123) == "bcbcaca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 123) == "bcbcaca": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 512) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 512) == "": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 100) == "bcabacb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 100) == "bcabacb": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 512) == "acbcbcbcbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 512) == "acbcbcbcbc": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 10) == "acabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 10) == "acabc": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 500) == "acbcbcabcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 500) == "acbcbcabcb": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 256) == "bcbcbcbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 256) == "bcbcbcbc": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 511) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 511) == "": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 64) == "bcbcbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 64) == "bcbcbc": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 200) == "bcabacbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 200) == "bcabacbc": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 2048) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 2048) == "": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 85) == "bacacab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 85) == "bacacab": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 255) == "bcbcbcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 255) == "bcbcbcba": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 123) == "abacbcbaca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 123) == "abacbcbaca": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 128) == "bcbcbcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 128) == "bcbcbcb": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 128) == "acbcbcbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 128) == "acbcbcbc": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 31) == "bcbca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 31) == "bcbca": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 42) == "bacabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 42) == "bacabc": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 64) == "ababcbcbcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 64) == "ababcbcbcb": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 63) == "bcbcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 63) == "bcbcba": {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 2) == "b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 2) == "b": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 100) == "abcbabacb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 100) == "abcbabacb": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 512) == "bcbcbcbcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 512) == "bcbcbcbcb": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 125) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 125) == "": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 1023) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 1023) == "": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 125) == "abacbcbcab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 125) == "abacbcbcab": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 100) == "acbabacb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 100) == "acbabacb": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 50) == "abacbabac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 50) == "abacbabac": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 5) == "abacab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 5) == "abacab": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 64) == "abcbcbcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 64) == "abcbcbcb": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 500) == "bcbcbabcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 500) == "bcbcbabcb": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 243) == "acbcbabca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 243) == "acbcbabca": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 200) == "abcbabacbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 200) == "abcbabacbc": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 1024) == "bcbcbcbcbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 1024) == "bcbcbcbcbc": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 10,k = 101) == "abacbabcab"
    assert candidate(n = 5,k = 1) == "ababa"
    assert candidate(n = 10,k = 100) == "abacbabacb"
    assert candidate(n = 1,k = 4) == ""
    assert candidate(n = 2,k = 5) == "ca"
    assert candidate(n = 5,k = 25) == "bcaba"
    assert candidate(n = 5,k = 20) == "babcb"
    assert candidate(n = 1,k = 3) == "c"
    assert candidate(n = 3,k = 9) == "cab"
    assert candidate(n = 2,k = 6) == "cb"
    assert candidate(n = 4,k = 15) == "bcba"
    assert candidate(n = 2,k = 1) == "ab"
    assert candidate(n = 5,k = 15) == "acbca"
    assert candidate(n = 5,k = 30) == "bcbac"
    assert candidate(n = 3,k = 12) == "cbc"
    assert candidate(n = 2,k = 3) == "ba"
    assert candidate(n = 4,k = 20) == "cacb"
    assert candidate(n = 3,k = 1) == "aba"
    assert candidate(n = 4,k = 10) == "babc"
    assert candidate(n = 9,k = 30) == "ababcbcac"
    assert candidate(n = 9,k = 1024) == ""
    assert candidate(n = 8,k = 33) == "abcababa"
    assert candidate(n = 3,k = 13) == ""
    assert candidate(n = 7,k = 50) == "acbabac"
    assert candidate(n = 10,k = 1023) == "bcbcbcbcba"
    assert candidate(n = 7,k = 127) == "bcbcbca"
    assert candidate(n = 9,k = 300) == "babcacacb"
    assert candidate(n = 1,k = 1) == "a"
    assert candidate(n = 6,k = 123) == ""
    assert candidate(n = 7,k = 1) == "abababa"
    assert candidate(n = 7,k = 200) == ""
    assert candidate(n = 6,k = 27) == "acbaca"
    assert candidate(n = 9,k = 175) == "acacacbca"
    assert candidate(n = 10,k = 10) == "abababcabc"
    assert candidate(n = 10,k = 3) == "ababababca"
    assert candidate(n = 10,k = 1) == "ababababab"
    assert candidate(n = 9,k = 150) == "acabcacac"
    assert candidate(n = 4,k = 25) == ""
    assert candidate(n = 8,k = 150) == "babcacac"
    assert candidate(n = 2,k = 7) == ""
    assert candidate(n = 3,k = 15) == ""
    assert candidate(n = 6,k = 70) == "cabcac"
    assert candidate(n = 6,k = 30) == "acbcac"
    assert candidate(n = 9,k = 2048) == ""
    assert candidate(n = 7,k = 123) == "bcbcaca"
    assert candidate(n = 8,k = 512) == ""
    assert candidate(n = 7,k = 100) == "bcabacb"
    assert candidate(n = 10,k = 512) == "acbcbcbcbc"
    assert candidate(n = 5,k = 10) == "acabc"
    assert candidate(n = 10,k = 500) == "acbcbcabcb"
    assert candidate(n = 8,k = 256) == "bcbcbcbc"
    assert candidate(n = 8,k = 511) == ""
    assert candidate(n = 6,k = 64) == "bcbcbc"
    assert candidate(n = 8,k = 200) == "bcabacbc"
    assert candidate(n = 10,k = 2048) == ""
    assert candidate(n = 7,k = 85) == "bacacab"
    assert candidate(n = 8,k = 255) == "bcbcbcba"
    assert candidate(n = 10,k = 123) == "abacbcbaca"
    assert candidate(n = 7,k = 128) == "bcbcbcb"
    assert candidate(n = 8,k = 128) == "acbcbcbc"
    assert candidate(n = 5,k = 31) == "bcbca"
    assert candidate(n = 6,k = 42) == "bacabc"
    assert candidate(n = 10,k = 64) == "ababcbcbcb"
    assert candidate(n = 6,k = 63) == "bcbcba"
    assert candidate(n = 1,k = 2) == "b"
    assert candidate(n = 9,k = 100) == "abcbabacb"
    assert candidate(n = 9,k = 512) == "bcbcbcbcb"
    assert candidate(n = 5,k = 125) == ""
    assert candidate(n = 9,k = 1023) == ""
    assert candidate(n = 10,k = 125) == "abacbcbcab"
    assert candidate(n = 8,k = 100) == "acbabacb"
    assert candidate(n = 9,k = 50) == "abacbabac"
    assert candidate(n = 6,k = 5) == "abacab"
    assert candidate(n = 8,k = 64) == "abcbcbcb"
    assert candidate(n = 9,k = 500) == "bcbcbabcb"
    assert candidate(n = 9,k = 243) == "acbcbabca"
    assert candidate(n = 10,k = 200) == "abcbabacbc"
    assert candidate(n = 10,k = 1024) == "bcbcbcbcbc"


