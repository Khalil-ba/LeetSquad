def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word1 = "a",word2 = "b") == "ab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "a",word2 = "b") == "ab": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "pq") == "apbqcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "pq") == "apbqcd": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "ab",word2 = "pqrs") == "apbqrs"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "ab",word2 = "pqrs") == "apbqrs": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "",word2 = "uvw") == "uvw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "",word2 = "uvw") == "uvw": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "x",word2 = "y") == "xy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "x",word2 = "y") == "xy": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "hello",word2 = "world") == "hweolrllod"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "hello",word2 = "world") == "hweolrllod": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "a",word2 = "bcd") == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "a",word2 = "bcd") == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcde",word2 = "fgh") == "afbgchde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcde",word2 = "fgh") == "afbgchde": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abc",word2 = "pqr") == "apbqcr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abc",word2 = "pqr") == "apbqcr": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "e") == "aebcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "e") == "aebcd": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyz",word2 = "") == "xyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyz",word2 = "") == "xyz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "") == "abcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "") == "abcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "a",word2 = "bcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "a",word2 = "bcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "thisisateststring",word2 = "anotheronehere") == "tahniostihseartoensethsetrreing"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "thisisateststring",word2 = "anotheronehere") == "tahniostihseartoensethsetrreing": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccdd",word2 = "eeffgg") == "aeaebfbfcgcgdd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccdd",word2 = "eeffgg") == "aeaebfbfcgcgdd": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "complex",word2 = "strings") == "csotmrpilnegxs"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "complex",word2 = "strings") == "csotmrpilnegxs": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyz",word2 = "abcde") == "xaybzcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyz",word2 = "abcde") == "xaybzcde": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefgh",word2 = "ijkl") == "aibjckdlefgh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefgh",word2 = "ijkl") == "aibjckdlefgh": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijk",word2 = "lmnopqrstuvwxyz") == "albmcndoepfqgrhsitjukvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijk",word2 = "lmnopqrstuvwxyz") == "albmcndoepfqgrhsitjukvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghij",word2 = "klmnopqrstuvwxyz") == "akblcmdneofpgqhrisjtuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghij",word2 = "klmnopqrstuvwxyz") == "akblcmdneofpgqhrisjtuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijklmnopqrstuvwxy",word2 = "z") == "azbcdefghijklmnopqrstuvwxy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijklmnopqrstuvwxy",word2 = "z") == "azbcdefghijklmnopqrstuvwxy": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "quick",word2 = "brownfox") == "qburiocwknfox"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "quick",word2 = "brownfox") == "qburiocwknfox": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "onetwothreefour",word2 = "five") == "ofnievtewothreefour"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "onetwothreefour",word2 = "five") == "ofnievtewothreefour": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "overlap",word2 = "lapping") == "olvaeprplianpg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "overlap",word2 = "lapping") == "olvaeprplianpg": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "",word2 = "") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "",word2 = "") == "": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "python",word2 = "java") == "pjyatvhaon"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "python",word2 = "java") == "pjyatvhaon": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefgh",word2 = "ijklmnopqrstuv") == "aibjckdlemfngohpqrstuv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefgh",word2 = "ijklmnopqrstuv") == "aibjckdlemfngohpqrstuv": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "different",word2 = "length") == "dliefnfgetrhent"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "different",word2 = "length") == "dliefnfgetrhent": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghij",word2 = "klmnopqrst") == "akblcmdneofpgqhrisjt"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghij",word2 = "klmnopqrst") == "akblcmdneofpgqhrisjt": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdabcd",word2 = "zyxwzyxwzyxw") == "azbycxdwazbycxdwazbycxdw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdabcd",word2 = "zyxwzyxwzyxw") == "azbycxdwazbycxdwazbycxdw": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "longerfirstword",word2 = "short") == "lsohnogretrfirstword"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "longerfirstword",word2 = "short") == "lsohnogretrfirstword": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefg",word2 = "hijklmnop") == "ahbicjdkelfmgnop"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefg",word2 = "hijklmnop") == "ahbicjdkelfmgnop": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdef",word2 = "ghijklmnopqrstuvwxyz") == "agbhcidjekflmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdef",word2 = "ghijklmnopqrstuvwxyz") == "agbhcidjekflmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyz",word2 = "abcdefg") == "xaybzcdefg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyz",word2 = "abcdefg") == "xaybzcdefg": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdabcd",word2 = "efghefghefghefgh") == "aebfcgdhaebfcgdhaebfcgdhefgh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdabcd",word2 = "efghefghefghefgh") == "aebfcgdhaebfcgdhaebfcgdhefgh": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "short",word2 = "longersecondword") == "slhoonrgtersecondword"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "short",word2 = "longersecondword") == "slhoonrgtersecondword": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "",word2 = "notempty") == "notempty"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "",word2 = "notempty") == "notempty": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "notempty",word2 = "") == "notempty"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "notempty",word2 = "") == "notempty": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "",word2 = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "",word2 = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeff",word2 = "gggghhhhiiii") == "agagbgbgchchdhdheieififi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeff",word2 = "gggghhhhiiii") == "agagbgbgchchdhdheieififi": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "",word2 = "abcde") == "abcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "",word2 = "abcde") == "abcde": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "a1b2c3d4",word2 = "e5f6g7") == "ae15bf26cg37d4"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "a1b2c3d4",word2 = "e5f6g7") == "ae15bf26cg37d4": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "oddlength",word2 = "evenlengths") == "oedvdelnelnegntghths"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "oddlength",word2 = "evenlengths") == "oedvdelnelnegntghths": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "same",word2 = "size") == "ssaimzee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "same",word2 = "size") == "ssaimzee": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefg",word2 = "hijklmnopqrstuvwxyz") == "ahbicjdkelfmgnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefg",word2 = "hijklmnopqrstuvwxyz") == "ahbicjdkelfmgnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijj",word2 = "kkllmmnnooppqqrrssttuuvvwwxxyyzz") == "akakblblcmcmdndneoeofpfpgqgqhrhrisisjtjtuuvvwwxxyyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijj",word2 = "kkllmmnnooppqqrrssttuuvvwwxxyyzz") == "akakblblcmcmdndneoeofpfpgqgqhrhrisisjtjtuuvvwwxxyyzz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "hello",word2 = "worldwide") == "hweolrllodwide"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "hello",word2 = "worldwide") == "hweolrllodwide": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzxyzxyz",word2 = "abcabcabc") == "xaybzcxaybzcxaybzc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzxyzxyz",word2 = "abcabcabc") == "xaybzcxaybzcxaybzc": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdxyz",word2 = "efghwvu") == "aebfcgdhxwyvzu"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdxyz",word2 = "efghwvu") == "aebfcgdhxwyvzu": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "short",word2 = "averylongstring") == "sahvoerrtylongstring"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "short",word2 = "averylongstring") == "sahvoerrtylongstring": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "hello",word2 = "worldthisisaverylongstring") == "hweolrllodthisisaverylongstring"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "hello",word2 = "worldthisisaverylongstring") == "hweolrllodthisisaverylongstring": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefg",word2 = "hijkl") == "ahbicjdkelfg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefg",word2 = "hijkl") == "ahbicjdkelfg": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdef",word2 = "ghijklmnop") == "agbhcidjekflmnop"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdef",word2 = "ghijklmnop") == "agbhcidjekflmnop": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdabcd",word2 = "xyzxyzxyzxyz") == "axbyczdxaybzcxdyazbxcydz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdabcd",word2 = "xyzxyzxyzxyz") == "axbyczdxaybzcxdyazbxcydz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "averyveryverylongword",word2 = "short") == "asvheorrytveryverylongword"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "averyveryverylongword",word2 = "short") == "asvheorrytveryverylongword": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "longerword",word2 = "short") == "lsohnogretrword"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "longerword",word2 = "short") == "lsohnogretrword": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "hello",word2 = "world!") == "hweolrllod!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "hello",word2 = "world!") == "hweolrllod!": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "nonempty",word2 = "") == "nonempty"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "nonempty",word2 = "") == "nonempty": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "longstringwithmorecharacters",word2 = "shortstr") == "lsohnogrsttsrtirngwithmorecharacters"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "longstringwithmorecharacters",word2 = "shortstr") == "lsohnogrsttsrtirngwithmorecharacters": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdef",word2 = "zyxwvu") == "azbycxdwevfu"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdef",word2 = "zyxwvu") == "azbycxdwevfu": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "onlyone",word2 = "") == "onlyone"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "onlyone",word2 = "") == "onlyone": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyz",word2 = "uvw") == "xuyvzw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyz",word2 = "uvw") == "xuyvzw": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeff",word2 = "zzzzyyyxxww") == "azazbzbzcycydydxexewfwf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeff",word2 = "zzzzyyyxxww") == "azazbzbzcycydydxexewfwf": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefgh",word2 = "ijklmnop") == "aibjckdlemfngohp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefgh",word2 = "ijklmnop") == "aibjckdlemfngohp": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "onetwothree",word2 = "four") == "ofnoeutrwothree"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "onetwothree",word2 = "four") == "ofnoeutrwothree": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcc",word2 = "ddeeff") == "adadbebecfcf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcc",word2 = "ddeeff") == "adadbebecfcf": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijj",word2 = "zzzzzzzzzz") == "azazbzbzczczdzdzezezffgghhiijj"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijj",word2 = "zzzzzzzzzz") == "azazbzbzczczdzdzezezffgghhiijj": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacaxi",word2 = "manga") == "ambaancgaaxi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacaxi",word2 = "manga") == "ambaancgaaxi": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "onetwothreefour",word2 = "fivesix") == "ofnievtewsoitxhreefour"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "onetwothreefour",word2 = "fivesix") == "ofnievtewsoitxhreefour": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "one",word2 = "twothreefour") == "otnweothreefour"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "one",word2 = "twothreefour") == "otnweothreefour": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "alphanumeric123",word2 = "characters!@#") == "aclhpahraancutmeerrsi!c@1#23"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "alphanumeric123",word2 = "characters!@#") == "aclhpahraancutmeerrsi!c@1#23": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "",word2 = "nonempty") == "nonempty"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "",word2 = "nonempty") == "nonempty": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyz",word2 = "wvutsrqponmlkjihgfedcba") == "xwyvzutsrqponmlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyz",word2 = "wvutsrqponmlkjihgfedcba") == "xwyvzutsrqponmlkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcde",word2 = "") == "abcde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcde",word2 = "") == "abcde": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "short",word2 = "averyverylongwordindeed") == "sahvoerrtyverylongwordindeed"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "short",word2 = "averyverylongwordindeed") == "sahvoerrtyverylongwordindeed": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xy",word2 = "abcdefghijk") == "xaybcdefghijk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xy",word2 = "abcdefghijk") == "xaybcdefghijk": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "onetwothree",word2 = "fourfivesix") == "ofnoeutrwfoitvherseiex"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "onetwothree",word2 = "fourfivesix") == "ofnoeutrwfoitvherseiex": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "python",word2 = "programming") == "ppyrtohgornamming"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "python",word2 = "programming") == "ppyrtohgornamming": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "verylongwordthatgoesonandone",word2 = "short") == "vsehroyrltongwordthatgoesonandone"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "verylongwordthatgoesonandone",word2 = "short") == "vsehroyrltongwordthatgoesonandone": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyz",word2 = "abcdef") == "xaybzcdef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyz",word2 = "abcdef") == "xaybzcdef": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "merge",word2 = "these") == "mtehregsee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "merge",word2 = "these") == "mtehregsee": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "z") == "azbcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "z") == "azbcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzlmnop",word2 = "qrstuvwx") == "xqyrzsltmunvowpx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzlmnop",word2 = "qrstuvwx") == "xqyrzsltmunvowpx": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefgh",word2 = "ijklmno") == "aibjckdlemfngoh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefgh",word2 = "ijklmno") == "aibjckdlemfngoh": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "short",word2 = "averyveryverylongword") == "sahvoerrtyveryverylongword"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "short",word2 = "averyveryverylongword") == "sahvoerrtyveryverylongword": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "averyverylongwordindeed",word2 = "short") == "asvheorrytverylongwordindeed"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "averyverylongwordindeed",word2 = "short") == "asvheorrytverylongwordindeed": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "equal",word2 = "equal") == "eeqquuaall"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "equal",word2 = "equal") == "eeqquuaall": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "ab",word2 = "cd") == "acbd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "ab",word2 = "cd") == "acbd": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "short",word2 = "averylongstringthatweneedtocheck") == "sahvoerrtylongstringthatweneedtocheck"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "short",word2 = "averylongstringthatweneedtocheck") == "sahvoerrtylongstringthatweneedtocheck": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "same",word2 = "same") == "ssaammee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "same",word2 = "same") == "ssaammee": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "") == "abcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "") == "abcd": {e}')
    
    total += 1
    try:
        result = candidate(word1 = "thisisaverylongstring",word2 = "hello") == "thheilsliosaverylongstring"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "thisisaverylongstring",word2 = "hello") == "thheilsliosaverylongstring": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word1 = "a",word2 = "b") == "ab"
    assert candidate(word1 = "abcd",word2 = "pq") == "apbqcd"
    assert candidate(word1 = "ab",word2 = "pqrs") == "apbqrs"
    assert candidate(word1 = "",word2 = "uvw") == "uvw"
    assert candidate(word1 = "x",word2 = "y") == "xy"
    assert candidate(word1 = "hello",word2 = "world") == "hweolrllod"
    assert candidate(word1 = "a",word2 = "bcd") == "abcd"
    assert candidate(word1 = "abcde",word2 = "fgh") == "afbgchde"
    assert candidate(word1 = "abc",word2 = "pqr") == "apbqcr"
    assert candidate(word1 = "abcd",word2 = "e") == "aebcd"
    assert candidate(word1 = "xyz",word2 = "") == "xyz"
    assert candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "") == "abcdefghijklmnopqrstuvwxyz"
    assert candidate(word1 = "a",word2 = "bcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz"
    assert candidate(word1 = "thisisateststring",word2 = "anotheronehere") == "tahniostihseartoensethsetrreing"
    assert candidate(word1 = "aabbccdd",word2 = "eeffgg") == "aeaebfbfcgcgdd"
    assert candidate(word1 = "complex",word2 = "strings") == "csotmrpilnegxs"
    assert candidate(word1 = "xyz",word2 = "abcde") == "xaybzcde"
    assert candidate(word1 = "abcdefgh",word2 = "ijkl") == "aibjckdlefgh"
    assert candidate(word1 = "abcdefghijk",word2 = "lmnopqrstuvwxyz") == "albmcndoepfqgrhsitjukvwxyz"
    assert candidate(word1 = "abcdefghij",word2 = "klmnopqrstuvwxyz") == "akblcmdneofpgqhrisjtuvwxyz"
    assert candidate(word1 = "abcdefghijklmnopqrstuvwxy",word2 = "z") == "azbcdefghijklmnopqrstuvwxy"
    assert candidate(word1 = "quick",word2 = "brownfox") == "qburiocwknfox"
    assert candidate(word1 = "onetwothreefour",word2 = "five") == "ofnievtewothreefour"
    assert candidate(word1 = "overlap",word2 = "lapping") == "olvaeprplianpg"
    assert candidate(word1 = "",word2 = "") == ""
    assert candidate(word1 = "python",word2 = "java") == "pjyatvhaon"
    assert candidate(word1 = "abcdefgh",word2 = "ijklmnopqrstuv") == "aibjckdlemfngohpqrstuv"
    assert candidate(word1 = "different",word2 = "length") == "dliefnfgetrhent"
    assert candidate(word1 = "abcdefghij",word2 = "klmnopqrst") == "akblcmdneofpgqhrisjt"
    assert candidate(word1 = "abcdabcdabcd",word2 = "zyxwzyxwzyxw") == "azbycxdwazbycxdwazbycxdw"
    assert candidate(word1 = "longerfirstword",word2 = "short") == "lsohnogretrfirstword"
    assert candidate(word1 = "abcdefg",word2 = "hijklmnop") == "ahbicjdkelfmgnop"
    assert candidate(word1 = "abcdef",word2 = "ghijklmnopqrstuvwxyz") == "agbhcidjekflmnopqrstuvwxyz"
    assert candidate(word1 = "xyz",word2 = "abcdefg") == "xaybzcdefg"
    assert candidate(word1 = "abcdabcdabcd",word2 = "efghefghefghefgh") == "aebfcgdhaebfcgdhaebfcgdhefgh"
    assert candidate(word1 = "short",word2 = "longersecondword") == "slhoonrgtersecondword"
    assert candidate(word1 = "",word2 = "notempty") == "notempty"
    assert candidate(word1 = "notempty",word2 = "") == "notempty"
    assert candidate(word1 = "",word2 = "abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz"
    assert candidate(word1 = "aabbccddeeff",word2 = "gggghhhhiiii") == "agagbgbgchchdhdheieififi"
    assert candidate(word1 = "",word2 = "abcde") == "abcde"
    assert candidate(word1 = "a1b2c3d4",word2 = "e5f6g7") == "ae15bf26cg37d4"
    assert candidate(word1 = "oddlength",word2 = "evenlengths") == "oedvdelnelnegntghths"
    assert candidate(word1 = "same",word2 = "size") == "ssaimzee"
    assert candidate(word1 = "abcdefg",word2 = "hijklmnopqrstuvwxyz") == "ahbicjdkelfmgnopqrstuvwxyz"
    assert candidate(word1 = "aabbccddeeffgghhiijj",word2 = "kkllmmnnooppqqrrssttuuvvwwxxyyzz") == "akakblblcmcmdndneoeofpfpgqgqhrhrisisjtjtuuvvwwxxyyzz"
    assert candidate(word1 = "hello",word2 = "worldwide") == "hweolrllodwide"
    assert candidate(word1 = "xyzxyzxyz",word2 = "abcabcabc") == "xaybzcxaybzcxaybzc"
    assert candidate(word1 = "abcdxyz",word2 = "efghwvu") == "aebfcgdhxwyvzu"
    assert candidate(word1 = "short",word2 = "averylongstring") == "sahvoerrtylongstring"
    assert candidate(word1 = "hello",word2 = "worldthisisaverylongstring") == "hweolrllodthisisaverylongstring"
    assert candidate(word1 = "abcdefg",word2 = "hijkl") == "ahbicjdkelfg"
    assert candidate(word1 = "abcdef",word2 = "ghijklmnop") == "agbhcidjekflmnop"
    assert candidate(word1 = "abcdabcdabcd",word2 = "xyzxyzxyzxyz") == "axbyczdxaybzcxdyazbxcydz"
    assert candidate(word1 = "averyveryverylongword",word2 = "short") == "asvheorrytveryverylongword"
    assert candidate(word1 = "longerword",word2 = "short") == "lsohnogretrword"
    assert candidate(word1 = "hello",word2 = "world!") == "hweolrllod!"
    assert candidate(word1 = "nonempty",word2 = "") == "nonempty"
    assert candidate(word1 = "longstringwithmorecharacters",word2 = "shortstr") == "lsohnogrsttsrtirngwithmorecharacters"
    assert candidate(word1 = "abcdef",word2 = "zyxwvu") == "azbycxdwevfu"
    assert candidate(word1 = "onlyone",word2 = "") == "onlyone"
    assert candidate(word1 = "xyz",word2 = "uvw") == "xuyvzw"
    assert candidate(word1 = "aabbccddeeff",word2 = "zzzzyyyxxww") == "azazbzbzcycydydxexewfwf"
    assert candidate(word1 = "abcdefgh",word2 = "ijklmnop") == "aibjckdlemfngohp"
    assert candidate(word1 = "onetwothree",word2 = "four") == "ofnoeutrwothree"
    assert candidate(word1 = "aabbcc",word2 = "ddeeff") == "adadbebecfcf"
    assert candidate(word1 = "aabbccddeeffgghhiijj",word2 = "zzzzzzzzzz") == "azazbzbzczczdzdzezezffgghhiijj"
    assert candidate(word1 = "abacaxi",word2 = "manga") == "ambaancgaaxi"
    assert candidate(word1 = "onetwothreefour",word2 = "fivesix") == "ofnievtewsoitxhreefour"
    assert candidate(word1 = "one",word2 = "twothreefour") == "otnweothreefour"
    assert candidate(word1 = "alphanumeric123",word2 = "characters!@#") == "aclhpahraancutmeerrsi!c@1#23"
    assert candidate(word1 = "",word2 = "nonempty") == "nonempty"
    assert candidate(word1 = "xyz",word2 = "wvutsrqponmlkjihgfedcba") == "xwyvzutsrqponmlkjihgfedcba"
    assert candidate(word1 = "abcde",word2 = "") == "abcde"
    assert candidate(word1 = "short",word2 = "averyverylongwordindeed") == "sahvoerrtyverylongwordindeed"
    assert candidate(word1 = "xy",word2 = "abcdefghijk") == "xaybcdefghijk"
    assert candidate(word1 = "onetwothree",word2 = "fourfivesix") == "ofnoeutrwfoitvherseiex"
    assert candidate(word1 = "python",word2 = "programming") == "ppyrtohgornamming"
    assert candidate(word1 = "verylongwordthatgoesonandone",word2 = "short") == "vsehroyrltongwordthatgoesonandone"
    assert candidate(word1 = "xyz",word2 = "abcdef") == "xaybzcdef"
    assert candidate(word1 = "merge",word2 = "these") == "mtehregsee"
    assert candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "z") == "azbcdefghijklmnopqrstuvwxyz"
    assert candidate(word1 = "xyzlmnop",word2 = "qrstuvwx") == "xqyrzsltmunvowpx"
    assert candidate(word1 = "abcdefgh",word2 = "ijklmno") == "aibjckdlemfngoh"
    assert candidate(word1 = "short",word2 = "averyveryverylongword") == "sahvoerrtyveryverylongword"
    assert candidate(word1 = "averyverylongwordindeed",word2 = "short") == "asvheorrytverylongwordindeed"
    assert candidate(word1 = "equal",word2 = "equal") == "eeqquuaall"
    assert candidate(word1 = "ab",word2 = "cd") == "acbd"
    assert candidate(word1 = "short",word2 = "averylongstringthatweneedtocheck") == "sahvoerrtylongstringthatweneedtocheck"
    assert candidate(word1 = "same",word2 = "same") == "ssaammee"
    assert candidate(word1 = "abcd",word2 = "") == "abcd"
    assert candidate(word1 = "thisisaverylongstring",word2 = "hello") == "thheilsliosaverylongstring"


