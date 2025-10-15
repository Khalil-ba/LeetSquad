def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "aab") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aab") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabacabadabaeabafabagabahabaiabajabakabalabamabanabaoabapabaqabarabasabataabuabavabawabaxabayabajabaz") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabacabadabaeabafabagabahabaiabajabakabalabamabanabaoabapabaqabarabasabataabuabavabawabaxabayabajabaz") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccddddeeeeeffffffggggggghhhhhhhhiiiiiiiii") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccddddeeeeeffffffggggggghhhhhhhhiiiiiiiii") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzz") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzz") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "ceabaacb") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ceabaacb") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhii") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhii") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzyyyyyyyyyxxxxxxxwwwwwwvvvvuuuuutttttsssssrrrrqqqqppppooooonnnnmmmmlllkkkjjjiii") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzyyyyyyyyyxxxxxxxwwwwwwvvvvuuuuutttttsssssrrrrqqqqppppooooonnnnmmmmlllkkkjjjiii") == 41: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggg") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggg") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffhhhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffhhhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzz") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzz") == 47: {e}')
    
    total += 1
    try:
        result = candidate(s = "pppppppppooooooonnnnnmmmllllllkkkkjjjjiiiiiiiihhhhhhhggggggg") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pppppppppooooooonnnnnmmmllllllkkkkjjjjiiiiiiiihhhhhhhggggggg") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbccccddddeeeee") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbccccddddeeeee") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzyyyyyyyxxxxxxxwwwwwwvvvvuuuutttssrrqponmlkjihgfedcba") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzyyyyyyyxxxxxxxwwwwwwvvvvuuuutttssrrqponmlkjihgfedcba") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccddddeeeeeffffffggggggghhhhhhhhiiiiiiiiijjjjjjjjjj") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccddddeeeeeffffffggggggghhhhhhhhiiiiiiiiijjjjjjjjjj") == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "aab") == 0
    assert candidate(s = "aabacabadabaeabafabagabahabaiabajabakabalabamabanabaoabapabaqabarabasabataabuabavabawabaxabayabajabaz") == 22
    assert candidate(s = "abcabcabc") == 3
    assert candidate(s = "aabbbcccddddeeeeeffffffggggggghhhhhhhhiiiiiiiii") == 2
    assert candidate(s = "zzzzzzzzzz") == 0
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzz") == 24
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 25
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 49
    assert candidate(s = "ceabaacb") == 2
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 0
    assert candidate(s = "aaabbbcc") == 2
    assert candidate(s = "aabbccddeeffgghhii") == 15
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba") == 25
    assert candidate(s = "a") == 0
    assert candidate(s = "zzzzzzzzzzyyyyyyyyyxxxxxxxwwwwwwvvvvuuuuutttttsssssrrrrqqqqppppooooonnnnmmmmlllkkkjjjiii") == 41
    assert candidate(s = "aabbccddeeefffggg") == 11
    assert candidate(s = "aabbccddeeefffhhhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 48
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzz") == 47
    assert candidate(s = "pppppppppooooooonnnnnmmmllllllkkkkjjjjiiiiiiiihhhhhhhggggggg") == 15
    assert candidate(s = "aabbbccccddddeeeee") == 3
    assert candidate(s = "abababababababababab") == 1
    assert candidate(s = "zzzzzzzzzzzyyyyyyyxxxxxxxwwwwwwvvvvuuuutttssrrqponmlkjihgfedcba") == 24
    assert candidate(s = "aabbbcccddddeeeeeffffffggggggghhhhhhhhiiiiiiiiijjjjjjjjjj") == 2


