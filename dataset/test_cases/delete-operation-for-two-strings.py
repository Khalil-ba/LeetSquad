def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word1 = "abc",word2 = "def") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abc",word2 = "def") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcde",word2 = "fghij") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcde",word2 = "fghij") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == 50: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "sea",word2 = "eat") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "sea",word2 = "eat") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "dcba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "dcba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "leetcode",word2 = "etco") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "leetcode",word2 = "etco") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abc",word2 = "abc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abc",word2 = "abc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "a",word2 = "b") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "a",word2 = "b") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "park",word2 = "spake") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "park",word2 = "spake") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "flaw",word2 = "lawn") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "flaw",word2 = "lawn") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "leetcode",word2 = "etco") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "leetcode",word2 = "etco") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcde",word2 = "ace") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcde",word2 = "ace") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "ultramicroscopicsilicovolcanoconiosis") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "ultramicroscopicsilicovolcanoconiosis") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "qwertyuiop",word2 = "asdfghjklzxcvbnm") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "qwertyuiop",word2 = "asdfghjklzxcvbnm") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "a",word2 = "b") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "a",word2 = "b") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abc",word2 = "abc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abc",word2 = "abc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "sea",word2 = "eat") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "sea",word2 = "eat") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "a",word2 = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "a",word2 = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "intention",word2 = "execution") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "intention",word2 = "execution") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "dcba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "dcba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abc",word2 = "def") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abc",word2 = "def") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccdd",word2 = "ddccbbaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccdd",word2 = "ddccbbaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "algorithm",word2 = "alligator") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "algorithm",word2 = "alligator") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdeabc",word2 = "abcdeabcdeabcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdeabc",word2 = "abcdeabcdeabcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "pississippi") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "pississippi") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefgh",word2 = "hgfedcba") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefgh",word2 = "hgfedcba") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "pseudopseudohypoparathyroidism") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "pseudopseudohypoparathyroidism") == 49: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "interstellar",word2 = "interplanetary") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "interstellar",word2 = "interplanetary") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",word2 = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 808
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",word2 = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 808: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "thisisalongstring",word2 = "thisisanotherrandomstring") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "thisisalongstring",word2 = "thisisanotherrandomstring") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "dynamic",word2 = "programming") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "dynamic",word2 = "programming") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "karolin",word2 = "kathrin") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "karolin",word2 = "kathrin") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "mississipi") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "mississipi") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdefabcde",word2 = "abcde") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdefabcde",word2 = "abcde") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "hippopotomonstrosesquippedaliophobia",word2 = "supercalifragilisticexpialidocious") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "hippopotomonstrosesquippedaliophobia",word2 = "supercalifragilisticexpialidocious") == 50: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "algorithm",word2 = "rhythm") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "algorithm",word2 = "rhythm") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "ababababab",word2 = "bababababa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "ababababab",word2 = "bababababa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "programming",word2 = "program") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "programming",word2 = "program") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacaxabayabacaxabay",word2 = "abayabacaxabayabacaxab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacaxabayabacaxabay",word2 = "abayabacaxabayabacaxab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "flibbertigibbet",word2 = "fribblegibbet") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "flibbertigibbet",word2 = "fribblegibbet") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "longest",word2 = "substring") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "longest",word2 = "substring") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "flaw",word2 = "lawn") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "flaw",word2 = "lawn") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",word2 = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",word2 = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 120: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "flower",word2 = "flow") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "flower",word2 = "flow") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzxyz",word2 = "zyxzyx") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzxyz",word2 = "zyxzyx") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abracadabra",word2 = "abrakadabradabra") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abracadabra",word2 = "abrakadabradabra") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaa",word2 = "bbbbb") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaa",word2 = "bbbbb") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "pneumonoultramicroscopicsilicovolcanoconiosisxyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "pneumonoultramicroscopicsilicovolcanoconiosisxyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "evaporate",word2 = "volatile") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "evaporate",word2 = "volatile") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "racecar",word2 = "civic") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "racecar",word2 = "civic") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacabadabacaba",word2 = "abacabadabacabax") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacabadabacaba",word2 = "abacabadabacabax") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "longest",word2 = "shortest") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "longest",word2 = "shortest") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "abef") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "abef") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "algorithm",word2 = "altruistic") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "algorithm",word2 = "altruistic") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "missisippi") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "missisippi") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "longestcommonsubsequence",word2 = "longestcommonsubstring") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "longestcommonsubsequence",word2 = "longestcommonsubstring") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "kittens",word2 = "sitting") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "kittens",word2 = "sitting") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaaaaaaaaaa",word2 = "bbbbbbbbbbbbbb") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaaaaaaaaaa",word2 = "bbbbbbbbbbbbbb") == 28: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == 50: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "thequickbrownfoxjumpsoverthelazydog",word2 = "packmyboxwithfivedozenliquorjugs") == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "thequickbrownfoxjumpsoverthelazydog",word2 = "packmyboxwithfivedozenliquorjugs") == 43: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaa",word2 = "bbbbbb") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaa",word2 = "bbbbbb") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abracadabra",word2 = "abacaxabay") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abracadabra",word2 = "abacaxabay") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "racecar",word2 = "racecar") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "racecar",word2 = "racecar") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdxyz",word2 = "xyzabcd") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdxyz",word2 = "xyzabcd") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "palindrome",word2 = "madam") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "palindrome",word2 = "madam") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "missisipi") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "missisipi") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "programming",word2 = "prognosis") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "programming",word2 = "prognosis") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "sequence",word2 = "subsequence") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "sequence",word2 = "subsequence") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "floccinaucinihilipilification",word2 = "antidisestablishmentarianism") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "floccinaucinihilipilification",word2 = "antidisestablishmentarianism") == 39: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abracadabra",word2 = "avadakedavra") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abracadabra",word2 = "avadakedavra") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "programming",word2 = "programmer") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "programming",word2 = "programmer") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "misisippi") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "misisippi") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaabbbbb",word2 = "bbbbbbaaaaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaabbbbb",word2 = "bbbbbbaaaaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "dissimilar",word2 = "similarly") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "dissimilar",word2 = "similarly") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "kitten",word2 = "sitting") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "kitten",word2 = "sitting") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "mississsippi") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "mississsippi") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abc",word2 = "xyz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abc",word2 = "xyz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "gumbo",word2 = "gambol") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "gumbo",word2 = "gambol") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "elephant",word2 = "relevant") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "elephant",word2 = "relevant") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcde",word2 = "fghij") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcde",word2 = "fghij") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "supercalifragilisticexpialidocious",word2 = "pneumonoultramicroscopicsilicovolcanoconiosis") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "supercalifragilisticexpialidocious",word2 = "pneumonoultramicroscopicsilicovolcanoconiosis") == 45: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "palindrome",word2 = "emordnilap") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "palindrome",word2 = "emordnilap") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "dynamicprogramming",word2 = "dynamicprogram") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "dynamicprogramming",word2 = "dynamicprogram") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacaxi",word2 = "bacana") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacaxi",word2 = "bacana") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "abcde") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "abcde") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abracadabra",word2 = "abracadabrac") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abracadabra",word2 = "abracadabrac") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefgh",word2 = "efghijkl") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefgh",word2 = "efghijkl") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacaxi",word2 = "bacaxia") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacaxi",word2 = "bacaxia") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefgh",word2 = "fghijklm") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefgh",word2 = "fghijklm") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "abcd") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "abcd") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "qwertyuiopasdfghjklzxcvbnm",word2 = "mnbvcxzlkjhgfdsapoiuytrewq") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "qwertyuiopasdfghjklzxcvbnm",word2 = "mnbvcxzlkjhgfdsapoiuytrewq") == 50: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xylophone",word2 = "balalaika") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xylophone",word2 = "balalaika") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijk",word2 = "kjihgfedcba") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijk",word2 = "kjihgfedcba") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "transformation",word2 = "transfigure") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "transformation",word2 = "transfigure") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacaxi",word2 = "abacaxi") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacaxi",word2 = "abacaxi") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "similarities",word2 = "dissimilarities") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "similarities",word2 = "dissimilarities") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "characters",word2 = "chartreuse") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "characters",word2 = "chartreuse") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "floccinaucinihilipilification",word2 = "supercalifragilisticexpialidocious") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "floccinaucinihilipilification",word2 = "supercalifragilisticexpialidocious") == 37: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "deleting",word2 = "leting") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "deleting",word2 = "leting") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabc",word2 = "cbacbacba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabc",word2 = "cbacbacba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "supercalifragilisticexpialidocious") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "supercalifragilisticexpialidocious") == 45: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "ababababababababababababababababababababababababab",word2 = "bababababababababababababababababababababababababa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "ababababababababababababababababababababababababab",word2 = "bababababababababababababababababababababababababa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "dynamic",word2 = "algorithm") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "dynamic",word2 = "algorithm") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "dabc",word2 = "dcba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "dabc",word2 = "dcba") == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word1 = "abc",word2 = "def") == 6
    assert candidate(word1 = "abcde",word2 = "fghij") == 10
    assert candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == 50
    assert candidate(word1 = "sea",word2 = "eat") == 2
    assert candidate(word1 = "abcd",word2 = "dcba") == 6
    assert candidate(word1 = "leetcode",word2 = "etco") == 4
    assert candidate(word1 = "abc",word2 = "abc") == 0
    assert candidate(word1 = "a",word2 = "b") == 2
    assert candidate(word1 = "park",word2 = "spake") == 3
    assert candidate(word1 = "flaw",word2 = "lawn") == 2
    assert candidate(word1 = "leetcode",word2 = "etco") == 4
    assert candidate(word1 = "abcde",word2 = "ace") == 2
    assert candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "ultramicroscopicsilicovolcanoconiosis") == 8
    assert candidate(word1 = "qwertyuiop",word2 = "asdfghjklzxcvbnm") == 26
    assert candidate(word1 = "a",word2 = "b") == 2
    assert candidate(word1 = "abc",word2 = "abc") == 0
    assert candidate(word1 = "sea",word2 = "eat") == 2
    assert candidate(word1 = "a",word2 = "a") == 0
    assert candidate(word1 = "intention",word2 = "execution") == 8
    assert candidate(word1 = "abcd",word2 = "dcba") == 6
    assert candidate(word1 = "abc",word2 = "def") == 6
    assert candidate(word1 = "aabbccdd",word2 = "ddccbbaa") == 12
    assert candidate(word1 = "algorithm",word2 = "alligator") == 8
    assert candidate(word1 = "abcdabcdeabc",word2 = "abcdeabcdeabcd") == 2
    assert candidate(word1 = "mississippi",word2 = "pississippi") == 2
    assert candidate(word1 = "abcdefgh",word2 = "hgfedcba") == 14
    assert candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "pseudopseudohypoparathyroidism") == 49
    assert candidate(word1 = "interstellar",word2 = "interplanetary") == 10
    assert candidate(word1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",word2 = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 808
    assert candidate(word1 = "thisisalongstring",word2 = "thisisanotherrandomstring") == 12
    assert candidate(word1 = "dynamic",word2 = "programming") == 12
    assert candidate(word1 = "karolin",word2 = "kathrin") == 4
    assert candidate(word1 = "mississippi",word2 = "mississipi") == 1
    assert candidate(word1 = "abcdabcdefabcde",word2 = "abcde") == 10
    assert candidate(word1 = "hippopotomonstrosesquippedaliophobia",word2 = "supercalifragilisticexpialidocious") == 50
    assert candidate(word1 = "algorithm",word2 = "rhythm") == 7
    assert candidate(word1 = "ababababab",word2 = "bababababa") == 2
    assert candidate(word1 = "programming",word2 = "program") == 4
    assert candidate(word1 = "abacaxabayabacaxabay",word2 = "abayabacaxabayabacaxab") == 6
    assert candidate(word1 = "flibbertigibbet",word2 = "fribblegibbet") == 6
    assert candidate(word1 = "longest",word2 = "substring") == 12
    assert candidate(word1 = "flaw",word2 = "lawn") == 2
    assert candidate(word1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",word2 = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 120
    assert candidate(word1 = "flower",word2 = "flow") == 2
    assert candidate(word1 = "xyzxyz",word2 = "zyxzyx") == 6
    assert candidate(word1 = "abracadabra",word2 = "abrakadabradabra") == 7
    assert candidate(word1 = "aaaaa",word2 = "bbbbb") == 10
    assert candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "pneumonoultramicroscopicsilicovolcanoconiosisxyz") == 3
    assert candidate(word1 = "evaporate",word2 = "volatile") == 7
    assert candidate(word1 = "racecar",word2 = "civic") == 8
    assert candidate(word1 = "abacabadabacaba",word2 = "abacabadabacabax") == 1
    assert candidate(word1 = "longest",word2 = "shortest") == 7
    assert candidate(word1 = "abcd",word2 = "abef") == 4
    assert candidate(word1 = "algorithm",word2 = "altruistic") == 9
    assert candidate(word1 = "mississippi",word2 = "missisippi") == 1
    assert candidate(word1 = "longestcommonsubsequence",word2 = "longestcommonsubstring") == 10
    assert candidate(word1 = "kittens",word2 = "sitting") == 6
    assert candidate(word1 = "aaaaaaaaaaaaaa",word2 = "bbbbbbbbbbbbbb") == 28
    assert candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == 50
    assert candidate(word1 = "thequickbrownfoxjumpsoverthelazydog",word2 = "packmyboxwithfivedozenliquorjugs") == 43
    assert candidate(word1 = "aaaaaa",word2 = "bbbbbb") == 12
    assert candidate(word1 = "abracadabra",word2 = "abacaxabay") == 5
    assert candidate(word1 = "racecar",word2 = "racecar") == 0
    assert candidate(word1 = "abcdxyz",word2 = "xyzabcd") == 6
    assert candidate(word1 = "palindrome",word2 = "madam") == 9
    assert candidate(word1 = "mississippi",word2 = "missisipi") == 2
    assert candidate(word1 = "programming",word2 = "prognosis") == 10
    assert candidate(word1 = "sequence",word2 = "subsequence") == 3
    assert candidate(word1 = "floccinaucinihilipilification",word2 = "antidisestablishmentarianism") == 39
    assert candidate(word1 = "abracadabra",word2 = "avadakedavra") == 9
    assert candidate(word1 = "programming",word2 = "programmer") == 5
    assert candidate(word1 = "mississippi",word2 = "misisippi") == 2
    assert candidate(word1 = "aaaaaabbbbb",word2 = "bbbbbbaaaaa") == 12
    assert candidate(word1 = "dissimilar",word2 = "similarly") == 5
    assert candidate(word1 = "kitten",word2 = "sitting") == 5
    assert candidate(word1 = "mississippi",word2 = "mississsippi") == 1
    assert candidate(word1 = "abc",word2 = "xyz") == 6
    assert candidate(word1 = "gumbo",word2 = "gambol") == 3
    assert candidate(word1 = "elephant",word2 = "relevant") == 4
    assert candidate(word1 = "abcde",word2 = "fghij") == 10
    assert candidate(word1 = "supercalifragilisticexpialidocious",word2 = "pneumonoultramicroscopicsilicovolcanoconiosis") == 45
    assert candidate(word1 = "palindrome",word2 = "emordnilap") == 18
    assert candidate(word1 = "dynamicprogramming",word2 = "dynamicprogram") == 4
    assert candidate(word1 = "abacaxi",word2 = "bacana") == 5
    assert candidate(word1 = "abcd",word2 = "abcde") == 1
    assert candidate(word1 = "abracadabra",word2 = "abracadabrac") == 1
    assert candidate(word1 = "abcdefgh",word2 = "efghijkl") == 8
    assert candidate(word1 = "abacaxi",word2 = "bacaxia") == 2
    assert candidate(word1 = "abcdefgh",word2 = "fghijklm") == 10
    assert candidate(word1 = "abcd",word2 = "abcd") == 0
    assert candidate(word1 = "qwertyuiopasdfghjklzxcvbnm",word2 = "mnbvcxzlkjhgfdsapoiuytrewq") == 50
    assert candidate(word1 = "xylophone",word2 = "balalaika") == 16
    assert candidate(word1 = "abcdefghijk",word2 = "kjihgfedcba") == 20
    assert candidate(word1 = "transformation",word2 = "transfigure") == 11
    assert candidate(word1 = "abacaxi",word2 = "abacaxi") == 0
    assert candidate(word1 = "similarities",word2 = "dissimilarities") == 3
    assert candidate(word1 = "characters",word2 = "chartreuse") == 6
    assert candidate(word1 = "floccinaucinihilipilification",word2 = "supercalifragilisticexpialidocious") == 37
    assert candidate(word1 = "deleting",word2 = "leting") == 2
    assert candidate(word1 = "abcabcabc",word2 = "cbacbacba") == 8
    assert candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "supercalifragilisticexpialidocious") == 45
    assert candidate(word1 = "ababababababababababababababababababababababababab",word2 = "bababababababababababababababababababababababababa") == 2
    assert candidate(word1 = "dynamic",word2 = "algorithm") == 12
    assert candidate(word1 = "dabc",word2 = "dcba") == 4


