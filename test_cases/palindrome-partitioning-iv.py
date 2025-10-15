def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdfgdcaba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcaba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoon") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoon") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabb") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabb") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "noon") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noon") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "deeee") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deeee") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbdd") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbdd") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamimadam") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamimadam") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaacaab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaacaab") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbddxy") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbddxy") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeffgghhii") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeffgghhii") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggghhhiiii") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggghhhiiii") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "kayakmadamracecar") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "kayakmadamracecar") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelracecar") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelracecar") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "civicnooncivicnoon") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "civicnooncivicnoon") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbaaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbaaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamnoonmadamnoonmadam") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamnoonmadamnoonmadam") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotordetartratedrotor") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotordetartratedrotor") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "tattarrattatmadamracecar") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "tattarrattatmadamracecar") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorlevelrotor") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorlevelrotor") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "deifiedcivicdeified") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deifiedcivicdeified") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorrefer") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorrefer") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamadam") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamadam") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "levellevellevellevellevellevel") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levellevellevellevellevellevel") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "deifieddeifieddeified") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deifieddeifieddeified") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyxabcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxabcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "tacocatdeified") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "tacocatdeified") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "leveloneone") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leveloneone") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggghhhhiiiiijjjjkkkkllllmmmmnnnnoooo") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggghhhhiiiiijjjjkkkkllllmmmmnnnnoooo") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelmadamrotor") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelmadamrotor") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdmadamracecar") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdmadamracecar") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "levellevellevellevel") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levellevellevellevel") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "repaperdeified") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repaperdeified") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoonnoon") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoonnoon") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarlevel") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarlevel") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "revilerleveldeified") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "revilerleveldeified") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "deifieddeifieddeifieddeifieddeified") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deifieddeifieddeifieddeifieddeified") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "kayakracecarkayak") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "kayakracecarkayak") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbcbbaabbcbba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbcbbaabbcbba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelrotorabcddcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelrotorabcddcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeffgghhiiiii") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeffgghhiiiii") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "leveldeifiedlevel") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leveldeifiedlevel") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoonnoonnoonnoon") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoonnoonnoonnoon") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabaabacabaabacabaabacaba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabaabacabaabacabaabacaba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorreferrotorrefer") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorreferrotorrefer") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccbaabccba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccbaabccba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdfgdcabaaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcabaaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaccd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaccd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefffggghhhiiiiijjjjkkkkllllmmmmnnnnooooppppqqqrrrssstttuuuuvvvwwwxxxxyyyyzzzz") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefffggghhhiiiiijjjjkkkkllllmmmmnnnnooooppppqqqrrrssstttuuuuvvvwwwxxxxyyyyzzzz") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "madammadammadam") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madammadammadam") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarracecarracecar") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarracecarracecar") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "madammadam") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madammadam") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aibohphobiamadamaibohphobia") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aibohphobiamadamaibohphobia") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarbanana") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarbanana") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abaabbab") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abaabbab") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarabacaba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarabacaba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeeddcbaabbccdd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeeddcbaabbccdd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "deeeeefeee") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deeeeefeee") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorleveldeifiedleveldeifiedrotor") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorleveldeifiedleveldeifiedrotor") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeeedddccbbaa") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeeedddccbbaa") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccbaabccbaabccbaabccbaabccbaabccbaabccba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccbaabccbaabccbaabccbaabccbaabccbaabccba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "deifiedcivic") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deifiedcivic") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaabcbabcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaabcbabcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "civicracecar") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "civicracecar") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "wasitacaroracatisaw") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "wasitacaroracatisaw") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorcentralpalindromerotor") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorcentralpalindromerotor") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcbaabdcbaabcdcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcbaabdcbaabcdcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "aibohphobia") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aibohphobia") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "leveldeifiedcivic") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leveldeifiedcivic") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "referredder") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "referredder") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "level") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "level") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccdd") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccdd") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorleveltwol") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorleveltwol") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "levellevellevel") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levellevellevel") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorpusher") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorpusher") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabc") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabc") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "referreferrefer") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "referreferrefer") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyzyxyz") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyzyxyz") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamrotorlevel") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamrotorlevel") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "madam") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madam") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "mammadmam") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mammadmam") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarlevelmadam") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarlevelmadam") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "civiccivicciviccivicciviccivic") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "civiccivicciviccivicciviccivic") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "wasitacaroracitisawreferredder") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "wasitacaroracitisawreferredder") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "xxyyxyyxxyyxyyxxyyxyy") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xxyyxyyxxyyxyyxxyyxyy") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababa") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababa") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarracecarracecarracecarracecar") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarracecarracecarracecarracecar") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "referredderreferredderreferredder") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "referredderreferredderreferredder") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelonevenflow") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelonevenflow") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "referreferreferreferreferrefer") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "referreferreferreferreferrefer") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "deifiedrotor") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deifiedrotor") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaababcbcabcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaababcbcabcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelonevenone") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelonevenone") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorrotorrotorrotorrotor") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorrotorrotorrotorrotor") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "detartrated") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "detartrated") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbcbba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbcbba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbabba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbabba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarannakayak") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarannakayak") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "amanaplanacanalpanama") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "amanaplanacanalpanama") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "refermadamrefermadam") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "refermadamrefermadam") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarleveldadlevel") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarleveldadlevel") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaeaeabba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaeaeabba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarracecar") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarracecar") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorreferredder") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorreferredder") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoon") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoon") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelrefercivic") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelrefercivic") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "deified") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deified") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaabba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaabba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelmadamatadammadam") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelmadamatadammadam") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotormadamrotor") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotormadamrotor") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorrotorrotor") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorrotorrotor") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyxyxzyx") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyxyxzyx") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorresistor") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorresistor") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "xylophonelevel") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xylophonelevel") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "deifiedrotordeified") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deifiedrotordeified") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarrotorrotorcarcerac") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarrotorrotorcarcerac") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabcba") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabcba") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoonnoonnoonnoonnoonnoonnoonnoonnoonnoonnoon") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoonnoonnoonnoonnoonnoonnoonnoonnoonnoonnoon") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcddcba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcddcba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "civic") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "civic") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotor") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotor") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "civicnoon") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "civicnoon") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "madamatadammadam") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madamatadammadam") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "repaperrepaperrepaper") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repaperrepaperrepaper") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorracecarracecar") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorracecarracecar") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "civicciviccivic") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "civicciviccivic") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorabanana") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorabanana") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefff") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefff") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "referdeifiedrefer") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "referdeifiedrefer") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorotator") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorotator") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghh") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghh") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "leveltwol") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leveltwol") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorresistorresistor") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorresistorresistor") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelracecarlevel") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelracecarlevel") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotordetartratedleveldeifiedrotor") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotordetartratedleveldeifiedrotor") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "madammadammadammadammadam") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "madammadammadammadammadam") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "deifiedrotorlevel") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "deifiedrotorlevel") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "refercivicrefer") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "refercivicrefer") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccbaabccbaabccbaabccba") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccbaabccbaabccbaabccba") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "leveldeified") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leveldeified") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "rotorlevelmadam") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rotorlevelmadam") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "neveroddoreven") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "neveroddoreven") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "redividerleveldeified") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "redividerleveldeified") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "refer") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "refer") == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abcba") == True
    assert candidate(s = "abcdcba") == True
    assert candidate(s = "aabbaa") == True
    assert candidate(s = "aaaaa") == True
    assert candidate(s = "abacdfgdcaba") == False
    assert candidate(s = "aabbbaa") == True
    assert candidate(s = "noonnoon") == True
    assert candidate(s = "aaa") == True
    assert candidate(s = "aabb") == True
    assert candidate(s = "racecar") == True
    assert candidate(s = "abba") == True
    assert candidate(s = "noon") == True
    assert candidate(s = "deeee") == True
    assert candidate(s = "abc") == True
    assert candidate(s = "abcbdd") == True
    assert candidate(s = "abcd") == False
    assert candidate(s = "aabbcc") == True
    assert candidate(s = "madamimadam") == True
    assert candidate(s = "aabaacaab") == True
    assert candidate(s = "bcbddxy") == False
    assert candidate(s = "aabbccddeeeffgghhii") == False
    assert candidate(s = "aabbccddeeefffggghhhiiii") == False
    assert candidate(s = "kayakmadamracecar") == True
    assert candidate(s = "levelracecar") == False
    assert candidate(s = "civicnooncivicnoon") == False
    assert candidate(s = "aaaaaabbaaaaa") == True
    assert candidate(s = "madamnoonmadamnoonmadam") == True
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == True
    assert candidate(s = "rotordetartratedrotor") == True
    assert candidate(s = "tattarrattatmadamracecar") == True
    assert candidate(s = "abcabcabc") == False
    assert candidate(s = "rotorlevelrotor") == True
    assert candidate(s = "deifiedcivicdeified") == True
    assert candidate(s = "rotorrefer") == False
    assert candidate(s = "madamadam") == True
    assert candidate(s = "aaaabbbbcccc") == True
    assert candidate(s = "levellevellevellevellevellevel") == True
    assert candidate(s = "deifieddeifieddeified") == True
    assert candidate(s = "xyzzyxabcba") == False
    assert candidate(s = "tacocatdeified") == False
    assert candidate(s = "leveloneone") == False
    assert candidate(s = "aabbccddeeefffggghhhhiiiiijjjjkkkkllllmmmmnnnnoooo") == False
    assert candidate(s = "levelmadamrotor") == True
    assert candidate(s = "abccbaabccba") == True
    assert candidate(s = "abcdmadamracecar") == False
    assert candidate(s = "levellevellevellevel") == True
    assert candidate(s = "repaperdeified") == False
    assert candidate(s = "noonnoonnoonnoon") == True
    assert candidate(s = "racecarlevel") == False
    assert candidate(s = "revilerleveldeified") == False
    assert candidate(s = "aabbaabbaa") == True
    assert candidate(s = "deifieddeifieddeifieddeifieddeified") == True
    assert candidate(s = "kayakracecarkayak") == True
    assert candidate(s = "abbbcbbaabbcbba") == False
    assert candidate(s = "levelrotorabcddcba") == True
    assert candidate(s = "aabbccddeeeffgghhiiiii") == False
    assert candidate(s = "leveldeifiedlevel") == True
    assert candidate(s = "noonnoonnoonnoonnoonnoon") == True
    assert candidate(s = "abacabaabacabaabacabaabacaba") == True
    assert candidate(s = "rotorreferrotorrefer") == False
    assert candidate(s = "abccbaabccbaabccba") == True
    assert candidate(s = "abacdfgdcabaaa") == False
    assert candidate(s = "aabbaccd") == False
    assert candidate(s = "aabbccddeeefffggghhhiiiiijjjjkkkkllllmmmmnnnnooooppppqqqrrrssstttuuuuvvvwwwxxxxyyyyzzzz") == False
    assert candidate(s = "madammadammadam") == True
    assert candidate(s = "racecarracecarracecar") == True
    assert candidate(s = "madammadam") == True
    assert candidate(s = "aibohphobiamadamaibohphobia") == True
    assert candidate(s = "racecarbanana") == True
    assert candidate(s = "abaabbab") == True
    assert candidate(s = "racecarabacaba") == False
    assert candidate(s = "abcdeedcba") == True
    assert candidate(s = "aabbccddeeeeddcbaabbccdd") == False
    assert candidate(s = "deeeeefeee") == True
    assert candidate(s = "rotorleveldeifiedleveldeifiedrotor") == False
    assert candidate(s = "aabbccddeeeeedddccbbaa") == False
    assert candidate(s = "abccbaabccbaabccbaabccbaabccbaabccbaabccbaabccba") == True
    assert candidate(s = "deifiedcivic") == False
    assert candidate(s = "abcbaabcbabcba") == True
    assert candidate(s = "civicracecar") == False
    assert candidate(s = "wasitacaroracatisaw") == True
    assert candidate(s = "rotorcentralpalindromerotor") == False
    assert candidate(s = "abcdcbaabdcbaabcdcba") == False
    assert candidate(s = "aibohphobia") == True
    assert candidate(s = "leveldeifiedcivic") == True
    assert candidate(s = "referredder") == False
    assert candidate(s = "level") == True
    assert candidate(s = "aabbccdd") == False
    assert candidate(s = "rotorleveltwol") == False
    assert candidate(s = "levellevellevel") == True
    assert candidate(s = "rotorpusher") == False
    assert candidate(s = "abccbaabc") == False
    assert candidate(s = "referreferrefer") == True
    assert candidate(s = "xyzyzyxyz") == True
    assert candidate(s = "madamrotorlevel") == True
    assert candidate(s = "madam") == True
    assert candidate(s = "mammadmam") == False
    assert candidate(s = "ababababababa") == True
    assert candidate(s = "racecarlevelmadam") == True
    assert candidate(s = "abababab") == False
    assert candidate(s = "civiccivicciviccivicciviccivic") == True
    assert candidate(s = "wasitacaroracitisawreferredder") == False
    assert candidate(s = "xxyyxyyxxyyxyyxxyyxyy") == True
    assert candidate(s = "abababa") == True
    assert candidate(s = "racecarracecarracecarracecarracecar") == True
    assert candidate(s = "referredderreferredderreferredder") == False
    assert candidate(s = "levelonevenflow") == False
    assert candidate(s = "referreferreferreferreferrefer") == True
    assert candidate(s = "deifiedrotor") == False
    assert candidate(s = "abcbaababcbcabcba") == False
    assert candidate(s = "banana") == False
    assert candidate(s = "levelonevenone") == False
    assert candidate(s = "rotorrotorrotorrotorrotor") == True
    assert candidate(s = "aabbccddeeffgg") == False
    assert candidate(s = "detartrated") == True
    assert candidate(s = "abbcbba") == True
    assert candidate(s = "aabbabba") == True
    assert candidate(s = "racecarannakayak") == True
    assert candidate(s = "amanaplanacanalpanama") == True
    assert candidate(s = "refermadamrefermadam") == False
    assert candidate(s = "racecarleveldadlevel") == False
    assert candidate(s = "abbaeaeabba") == True
    assert candidate(s = "racecarracecar") == True
    assert candidate(s = "rotorreferredder") == True
    assert candidate(s = "noonnoonnoon") == True
    assert candidate(s = "levelrefercivic") == True
    assert candidate(s = "deified") == True
    assert candidate(s = "abbaabbaabba") == True
    assert candidate(s = "levelmadamatadammadam") == False
    assert candidate(s = "abcdedcba") == True
    assert candidate(s = "rotormadamrotor") == True
    assert candidate(s = "rotorrotorrotor") == True
    assert candidate(s = "xyxzyxyxzyx") == False
    assert candidate(s = "rotorresistor") == False
    assert candidate(s = "xylophonelevel") == False
    assert candidate(s = "deifiedrotordeified") == True
    assert candidate(s = "racecarrotorrotorcarcerac") == False
    assert candidate(s = "abccbaabcba") == False
    assert candidate(s = "noonnoonnoonnoonnoonnoonnoonnoonnoonnoonnoonnoonnoon") == True
    assert candidate(s = "abcddcba") == True
    assert candidate(s = "civic") == True
    assert candidate(s = "rotor") == True
    assert candidate(s = "civicnoon") == False
    assert candidate(s = "madamatadammadam") == False
    assert candidate(s = "repaperrepaperrepaper") == True
    assert candidate(s = "rotorracecarracecar") == True
    assert candidate(s = "civicciviccivic") == True
    assert candidate(s = "rotorabanana") == False
    assert candidate(s = "aabbccddeeefff") == False
    assert candidate(s = "referdeifiedrefer") == True
    assert candidate(s = "rotorotator") == True
    assert candidate(s = "aabbccddeeffgghh") == False
    assert candidate(s = "leveltwol") == False
    assert candidate(s = "rotorresistorresistor") == False
    assert candidate(s = "levelracecarlevel") == True
    assert candidate(s = "rotordetartratedleveldeifiedrotor") == False
    assert candidate(s = "madammadammadammadammadam") == True
    assert candidate(s = "deifiedrotorlevel") == True
    assert candidate(s = "refercivicrefer") == True
    assert candidate(s = "abccbaabccbaabccbaabccbaabccba") == True
    assert candidate(s = "leveldeified") == False
    assert candidate(s = "rotorlevelmadam") == True
    assert candidate(s = "neveroddoreven") == True
    assert candidate(s = "redividerleveldeified") == True
    assert candidate(s = "refer") == True


