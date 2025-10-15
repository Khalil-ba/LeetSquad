def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(text = "ababab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ababab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "ab") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ab") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "abbbabbb") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abbbabbb") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 51: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcd") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcd") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacaba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacaba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "abc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "leetcodeleetcode") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "leetcodeleetcode") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "banana") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "banana") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzxyzxyzxyz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzxyzxyzxyz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefg") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefg") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "racecar racecar") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "racecar racecar") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "abababab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abababab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeff") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeff") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "mississippi") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "mississippi") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "ababababab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ababababab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyxyxyxyxyxyxyxyxyxyxyxy") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyxyxyxyxyxyxyxyxyxyxyxy") == 11: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacaxiabacaxiabacaxi") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacaxiabacaxiabacaxi") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabcabcabcabcabc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabcabcabcabcabc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdeabcdeabcdeabcde") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdeabcdeabcdeabcde") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 33: {e}')
    
    total += 1
    try:
        result = candidate(text = "repeatedrepeatedrepeatedrepeated") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "repeatedrepeatedrepeatedrepeated") == 9: {e}')
    
    total += 1
    try:
        result = candidate(text = "tattattattattattat") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "tattattattattattat") == 8: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaabaaaabaaaa") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaabaaaabaaaa") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "racecaracecaracecar") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "racecaracecaracecar") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcababcababcab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcababcababcab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeffaabbccddeeff") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeffaabbccddeeff") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyxyxyxyxyxyxyxyxyxyxy") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyxyxyxyxyxyxyxyxyxyxy") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacabaabacaba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacabaabacaba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "leetcodeleetcodeleetcodeleetcode") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "leetcodeleetcodeleetcodeleetcode") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "thisisaverylongstringthatrepeatstitselfthisisaverylongstringthatrepeatstitself") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "thisisaverylongstringthatrepeatstitselfthisisaverylongstringthatrepeatstitself") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaabaaaab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaabaaaab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabcabcabcabc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabcabcabcabc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaaaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaaaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 20: {e}')
    
    total += 1
    try:
        result = candidate(text = "abababababab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abababababab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaabcabcabcabcabc") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaabcabcabcabcabc") == 8: {e}')
    
    total += 1
    try:
        result = candidate(text = "qwertyqwertyqwerty") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "qwertyqwertyqwerty") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeffaabbccddeeffaabbccddeeff") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeffaabbccddeeffaabbccddeeff") == 18: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzxyzxyzxyzxyzxyz") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzxyzxyzxyzxyzxyz") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 27: {e}')
    
    total += 1
    try:
        result = candidate(text = "abababababababababababababababababababababababababababababababababab") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abababababababababababababababababababababababababababababababababab") == 33: {e}')
    
    total += 1
    try:
        result = candidate(text = "leetcodeisgoodandleetcodeisgood") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "leetcodeisgoodandleetcodeisgood") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "supercalifragilisticexpialidocioussupercalifragilisticexpialidocious") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "supercalifragilisticexpialidocioussupercalifragilisticexpialidocious") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacabacabacabac") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacabacabacabac") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "patternpatternpatternpattern") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "patternpatternpatternpattern") == 9: {e}')
    
    total += 1
    try:
        result = candidate(text = "mississippimississippi") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "mississippimississippi") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdabcdabcdabcd") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdabcdabcdabcd") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "zxcvbnmlkjhgfdsazxcvbnmlkjhgfdsa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zxcvbnmlkjhgfdsazxcvbnmlkjhgfdsa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefgabcdefgabcdefg") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefgabcdefgabcdefg") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "abracadabraabracadabra") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abracadabraabracadabra") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "hellohellohellohellohello") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "hellohellohellohellohello") == 11: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzzzzzzzzzzzzzzzzzz") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzzzzzzzzzzzzzzzzzz") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzzzzzzzzzzzzzz") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzzzzzzzzzzzzzz") == 8: {e}')
    
    total += 1
    try:
        result = candidate(text = "abababa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abababa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "ababababababab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ababababababab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaaaaaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaaaaaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdabcdeabcd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdabcdeabcd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "racecar") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "racecar") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefghabcdefgh") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefghabcdefgh") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy") == 32: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzxyzxyzxyzxyzxyzxyzxyz") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzxyzxyzxyzxyzxyzxyzxyz") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 30: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabcabc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabcabc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefghijabcdefghijabcdefghij") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefghijabcdefghijabcdefghij") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "pneumonoultramicroscopicsilicovolcanoconiosis") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "pneumonoultramicroscopicsilicovolcanoconiosis") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "abracadabrabracadabra") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abracadabrabracadabra") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacabadabacabadabacaba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacabadabacabadabacaba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaabbbbbaaaaabbbbb") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaabbbbbaaaaabbbbb") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "noonnoonnoonnoon") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "noonnoonnoonnoon") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacabadabacaba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacabadabacaba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyxyxyxyxyxyxyxy") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyxyxyxyxyxyxyxy") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "abracadabraabracadabraabracadabraabracadabraabracadabraabracadabra") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abracadabraabracadabraabracadabraabracadabraabracadabraabracadabra") == 25: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 43: {e}')
    
    total += 1
    try:
        result = candidate(text = "abababababababab") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abababababababab") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaaaaaaabaaaaaaaaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaaaaaaabaaaaaaaaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaabbbbcccc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaabbbbcccc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "noonnoonnoonnoonnoon") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "noonnoonnoonnoonnoon") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcxyzabcxyzabcxyz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcxyzabcxyzabcxyz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabca") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabca") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(text = "uniqueuniqueuniqueunique") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "uniqueuniqueuniqueunique") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "racecaracecar") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "racecaracecar") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefabcdefabcdef") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefabcdefabcdef") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "bananabananaananabanana") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bananabananaananabanana") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 32: {e}')
    
    total += 1
    try:
        result = candidate(text = "bananaabanana") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bananaabanana") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaabbbbccccddddeeeeffff") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaabbbbccccddddeeeeffff") == 12: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 27: {e}')
    
    total += 1
    try:
        result = candidate(text = "hellohellohellohellohellohellohellohellohellohello") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "hellohellohellohellohellohellohellohellohellohello") == 22: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(text = "ababab") == 2
    assert candidate(text = "") == 0
    assert candidate(text = "abcabcabc") == 3
    assert candidate(text = "aaaa") == 2
    assert candidate(text = "ab") == 0
    assert candidate(text = "abbbabbb") == 2
    assert candidate(text = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 51
    assert candidate(text = "abcd") == 0
    assert candidate(text = "abacaba") == 0
    assert candidate(text = "abc") == 0
    assert candidate(text = "leetcodeleetcode") == 2
    assert candidate(text = "banana") == 2
    assert candidate(text = "xyzxyzxyzxyz") == 4
    assert candidate(text = "abcdefg") == 0
    assert candidate(text = "racecar racecar") == 0
    assert candidate(text = "a") == 0
    assert candidate(text = "abababab") == 3
    assert candidate(text = "aabbccddeeff") == 6
    assert candidate(text = "mississippi") == 4
    assert candidate(text = "ababababab") == 4
    assert candidate(text = "xyxyxyxyxyxyxyxyxyxyxyxy") == 11
    assert candidate(text = "abacaxiabacaxiabacaxi") == 7
    assert candidate(text = "abcabcabcabcabcabcabc") == 9
    assert candidate(text = "abcdeabcdeabcdeabcde") == 6
    assert candidate(text = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 33
    assert candidate(text = "repeatedrepeatedrepeatedrepeated") == 9
    assert candidate(text = "tattattattattattat") == 8
    assert candidate(text = "aaaaabaaaabaaaa") == 7
    assert candidate(text = "racecaracecaracecar") == 6
    assert candidate(text = "abcababcababcab") == 6
    assert candidate(text = "aabbccddeeffaabbccddeeff") == 7
    assert candidate(text = "xyxyxyxyxyxyxyxyxyxyxy") == 10
    assert candidate(text = "abacabaabacaba") == 3
    assert candidate(text = "leetcodeleetcodeleetcodeleetcode") == 10
    assert candidate(text = "thisisaverylongstringthatrepeatstitselfthisisaverylongstringthatrepeatstitself") == 2
    assert candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 26
    assert candidate(text = "aaaabaaaab") == 3
    assert candidate(text = "abcabcabcabcabcabc") == 7
    assert candidate(text = "aaaaaaa") == 3
    assert candidate(text = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghij") == 20
    assert candidate(text = "abababababab") == 5
    assert candidate(text = "aaaaabcabcabcabcabc") == 8
    assert candidate(text = "qwertyqwertyqwerty") == 6
    assert candidate(text = "aabbccddeeffaabbccddeeffaabbccddeeff") == 18
    assert candidate(text = "xyzxyzxyzxyzxyzxyz") == 7
    assert candidate(text = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 27
    assert candidate(text = "abababababababababababababababababababababababababababababababababab") == 33
    assert candidate(text = "leetcodeisgoodandleetcodeisgood") == 2
    assert candidate(text = "supercalifragilisticexpialidocioussupercalifragilisticexpialidocious") == 2
    assert candidate(text = "abacabacabacabac") == 5
    assert candidate(text = "patternpatternpatternpattern") == 9
    assert candidate(text = "mississippimississippi") == 5
    assert candidate(text = "abcdabcdabcdabcd") == 5
    assert candidate(text = "zxcvbnmlkjhgfdsazxcvbnmlkjhgfdsa") == 1
    assert candidate(text = "abcdefgabcdefgabcdefg") == 7
    assert candidate(text = "abracadabraabracadabra") == 3
    assert candidate(text = "hellohellohellohellohello") == 11
    assert candidate(text = "zzzzzzzzzzzzzzzzzzzz") == 10
    assert candidate(text = "zzzzzzzzzzzzzzzz") == 8
    assert candidate(text = "abababa") == 2
    assert candidate(text = "ababababababab") == 6
    assert candidate(text = "aaaaaaaaaa") == 5
    assert candidate(text = "abcdabcdeabcd") == 1
    assert candidate(text = "racecar") == 0
    assert candidate(text = "abcdefghabcdefgh") == 1
    assert candidate(text = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy") == 32
    assert candidate(text = "xyzxyzxyzxyzxyzxyzxyzxyz") == 10
    assert candidate(text = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 30
    assert candidate(text = "abcabcabcabc") == 4
    assert candidate(text = "abcdefghijabcdefghijabcdefghij") == 10
    assert candidate(text = "pneumonoultramicroscopicsilicovolcanoconiosis") == 0
    assert candidate(text = "aaaaa") == 2
    assert candidate(text = "abracadabrabracadabra") == 4
    assert candidate(text = "aaaaaa") == 3
    assert candidate(text = "abacabadabacabadabacaba") == 8
    assert candidate(text = "aaaaabbbbbaaaaabbbbb") == 5
    assert candidate(text = "noonnoonnoonnoon") == 7
    assert candidate(text = "abacabadabacaba") == 0
    assert candidate(text = "xyxyxyxyxyxyxyxy") == 7
    assert candidate(text = "abracadabraabracadabraabracadabraabracadabraabracadabraabracadabra") == 25
    assert candidate(text = "abcabcabcabcabc") == 6
    assert candidate(text = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 43
    assert candidate(text = "abababababababab") == 7
    assert candidate(text = "aaaaaaaaaabaaaaaaaaaa") == 5
    assert candidate(text = "aaaabbbbcccc") == 6
    assert candidate(text = "noonnoonnoonnoonnoon") == 10
    assert candidate(text = "abcxyzabcxyzabcxyz") == 6
    assert candidate(text = "abcabca") == 2
    assert candidate(text = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz") == 52
    assert candidate(text = "uniqueuniqueuniqueunique") == 7
    assert candidate(text = "racecaracecar") == 2
    assert candidate(text = "abcdefabcdefabcdef") == 6
    assert candidate(text = "bananabananaananabanana") == 7
    assert candidate(text = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 32
    assert candidate(text = "bananaabanana") == 3
    assert candidate(text = "aaaabbbbccccddddeeeeffff") == 12
    assert candidate(text = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 27
    assert candidate(text = "hellohellohellohellohellohellohellohellohellohello") == 22


