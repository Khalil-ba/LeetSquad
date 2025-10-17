def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(tiles = "AAAAAAA") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AAAAAAA") == 7: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "QQQ") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "QQQ") == 3: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ABCDEFG") == 13699
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ABCDEFG") == 13699: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ABC") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ABC") == 15: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AAB") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AAB") == 8: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AABBCC") == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AABBCC") == 270: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "XYZ") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "XYZ") == 15: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AAABBC") == 188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AAABBC") == 188: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AB") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AB") == 4: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AAAAAA") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AAAAAA") == 6: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ABCD") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ABCD") == 64: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "V") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "V") == 1: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ABBB") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ABBB") == 13: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AAA") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AAA") == 3: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AABC") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AABC") == 34: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "HHHHHHHH") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "HHHHHHHH") == 8: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "UVWXYZ") == 1956
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "UVWXYZ") == 1956: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ABCDABCD") == 7364
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ABCDABCD") == 7364: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ZZZZZZZ") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ZZZZZZZ") == 7: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "JKJKJKJKJK") == 922
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "JKJKJKJKJK") == 922: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ZWZWZWZW") == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ZWZWZWZW") == 250: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AAAABBBB") == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AAAABBBB") == 250: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AAABBBCCC") == 5247
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AAABBBCCC") == 5247: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AABBCCDDEEFF") == 21295782
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AABBCCDDEEFF") == 21295782: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AAABBBCCCDDD") == 1107696
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AAABBBCCCDDD") == 1107696: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "XYZXYZ") == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "XYZXYZ") == 270: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ABCDEFGH") == 109600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ABCDEFGH") == 109600: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ABACADAE") == 5188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ABACADAE") == 5188: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AABBCD") == 522
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AABBCD") == 522: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "HELLO") == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "HELLO") == 170: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AAAAAAAA") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AAAAAAAA") == 8: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ABCDEABCDE") == 326010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ABCDEABCDE") == 326010: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "QQQQRRRSSSTTTT") == 12743958
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "QQQQRRRSSSTTTT") == 12743958: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AABCCDDEE") == 65201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AABCCDDEE") == 65201: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "PPPPQQRR") == 1350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "PPPPQQRR") == 1350: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AAAAABBCCC") == 8293
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AAAAABBCCC") == 8293: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ABCDABC") == 1840
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ABCDABC") == 1840: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "MISSISSIPPI") == 107898
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "MISSISSIPPI") == 107898: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AABBCCD") == 1840
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AABBCCD") == 1840: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ABCDEFF") == 7012
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ABCDEFF") == 7012: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "REPEAT") == 1010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "REPEAT") == 1010: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "WWWWW") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "WWWWW") == 5: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ZZZZAAAA") == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ZZZZAAAA") == 250: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AABBBCC") == 649
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AABBBCC") == 649: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "QQQQQQQ") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "QQQQQQQ") == 7: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AABBCCDD") == 7364
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AABBCCDD") == 7364: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AAABBCCCC") == 4024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AAABBCCCC") == 4024: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ABCDEFGHII") == 4986850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ABCDEFGHII") == 4986850: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ABCXYZ") == 1956
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ABCXYZ") == 1956: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AAAAABBBCCC") == 29887
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AAAAABBBCCC") == 29887: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "PYTHON") == 1956
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "PYTHON") == 1956: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AABCCD") == 522
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AABCCD") == 522: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ABABABABAB") == 922
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ABABABABAB") == 922: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AABBCCDDEE") == 326010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AABBCCDDEE") == 326010: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AAAABBBCCCDDD") == 3627112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AAAABBBCCCDDD") == 3627112: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AABBCCDE") == 14458
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AABBCCDE") == 14458: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ABCDEF") == 1956
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ABCDEF") == 1956: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "XYZABC") == 1956
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "XYZABC") == 1956: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "SEQUENCES") == 87185
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "SEQUENCES") == 87185: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ABCDE") == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ABCDE") == 325: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AABCDD") == 522
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AABCDD") == 522: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ABCABCABC") == 5247
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ABCABCABC") == 5247: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AAAAABBBB") == 460
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AAAAABBBB") == 460: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ABCDEFGABC") == 1274854
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ABCDEFGABC") == 1274854: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "QWRTYUIOP") == 986409
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "QWRTYUIOP") == 986409: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AAAAABBBBBCCCCC") == 2435199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AAAAABBBBBCCCCC") == 2435199: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "UNIQUE") == 1010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "UNIQUE") == 1010: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "TILES") == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "TILES") == 325: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ABACADAEA") == 9833
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ABACADAEA") == 9833: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "MNOPQRST") == 109600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "MNOPQRST") == 109600: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AAAABBBCCC") == 13298
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AAAABBBCCC") == 13298: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "FFFFFFFFF") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "FFFFFFFFF") == 9: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "ABCDEFGHI") == 986409
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "ABCDEFGHI") == 986409: {e}')
    
    total += 1
    try:
        result = candidate(tiles = "AAAAAABBBB") == 790
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tiles = "AAAAAABBBB") == 790: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(tiles = "AAAAAAA") == 7
    assert candidate(tiles = "QQQ") == 3
    assert candidate(tiles = "ABCDEFG") == 13699
    assert candidate(tiles = "ABC") == 15
    assert candidate(tiles = "AAB") == 8
    assert candidate(tiles = "AABBCC") == 270
    assert candidate(tiles = "XYZ") == 15
    assert candidate(tiles = "AAABBC") == 188
    assert candidate(tiles = "AB") == 4
    assert candidate(tiles = "AAAAAA") == 6
    assert candidate(tiles = "ABCD") == 64
    assert candidate(tiles = "V") == 1
    assert candidate(tiles = "ABBB") == 13
    assert candidate(tiles = "AAA") == 3
    assert candidate(tiles = "AABC") == 34
    assert candidate(tiles = "HHHHHHHH") == 8
    assert candidate(tiles = "UVWXYZ") == 1956
    assert candidate(tiles = "ABCDABCD") == 7364
    assert candidate(tiles = "ZZZZZZZ") == 7
    assert candidate(tiles = "JKJKJKJKJK") == 922
    assert candidate(tiles = "ZWZWZWZW") == 250
    assert candidate(tiles = "AAAABBBB") == 250
    assert candidate(tiles = "AAABBBCCC") == 5247
    assert candidate(tiles = "AABBCCDDEEFF") == 21295782
    assert candidate(tiles = "AAABBBCCCDDD") == 1107696
    assert candidate(tiles = "XYZXYZ") == 270
    assert candidate(tiles = "ABCDEFGH") == 109600
    assert candidate(tiles = "ABACADAE") == 5188
    assert candidate(tiles = "AABBCD") == 522
    assert candidate(tiles = "HELLO") == 170
    assert candidate(tiles = "AAAAAAAA") == 8
    assert candidate(tiles = "ABCDEABCDE") == 326010
    assert candidate(tiles = "QQQQRRRSSSTTTT") == 12743958
    assert candidate(tiles = "AABCCDDEE") == 65201
    assert candidate(tiles = "PPPPQQRR") == 1350
    assert candidate(tiles = "AAAAABBCCC") == 8293
    assert candidate(tiles = "ABCDABC") == 1840
    assert candidate(tiles = "MISSISSIPPI") == 107898
    assert candidate(tiles = "AABBCCD") == 1840
    assert candidate(tiles = "ABCDEFF") == 7012
    assert candidate(tiles = "REPEAT") == 1010
    assert candidate(tiles = "WWWWW") == 5
    assert candidate(tiles = "ZZZZAAAA") == 250
    assert candidate(tiles = "AABBBCC") == 649
    assert candidate(tiles = "QQQQQQQ") == 7
    assert candidate(tiles = "AABBCCDD") == 7364
    assert candidate(tiles = "AAABBCCCC") == 4024
    assert candidate(tiles = "ABCDEFGHII") == 4986850
    assert candidate(tiles = "ABCXYZ") == 1956
    assert candidate(tiles = "AAAAABBBCCC") == 29887
    assert candidate(tiles = "PYTHON") == 1956
    assert candidate(tiles = "AABCCD") == 522
    assert candidate(tiles = "ABABABABAB") == 922
    assert candidate(tiles = "AABBCCDDEE") == 326010
    assert candidate(tiles = "AAAABBBCCCDDD") == 3627112
    assert candidate(tiles = "AABBCCDE") == 14458
    assert candidate(tiles = "ABCDEF") == 1956
    assert candidate(tiles = "XYZABC") == 1956
    assert candidate(tiles = "SEQUENCES") == 87185
    assert candidate(tiles = "ABCDE") == 325
    assert candidate(tiles = "AABCDD") == 522
    assert candidate(tiles = "ABCABCABC") == 5247
    assert candidate(tiles = "AAAAABBBB") == 460
    assert candidate(tiles = "ABCDEFGABC") == 1274854
    assert candidate(tiles = "QWRTYUIOP") == 986409
    assert candidate(tiles = "AAAAABBBBBCCCCC") == 2435199
    assert candidate(tiles = "UNIQUE") == 1010
    assert candidate(tiles = "TILES") == 325
    assert candidate(tiles = "ABACADAEA") == 9833
    assert candidate(tiles = "MNOPQRST") == 109600
    assert candidate(tiles = "AAAABBBCCC") == 13298
    assert candidate(tiles = "FFFFFFFFF") == 9
    assert candidate(tiles = "ABCDEFGHI") == 986409
    assert candidate(tiles = "AAAAAABBBB") == 790


