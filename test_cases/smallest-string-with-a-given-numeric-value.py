def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 7,k = 100) == "aaaszzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 100) == "aaaszzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 26) == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 26) == "z": {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 40) == "aalz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 40) == "aalz": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 73) == "aaszz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 73) == "aaszz": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 260) == "zzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 260) == "zzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 2) == "aa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 2) == "aa": {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 1) == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 1) == "a": {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 26) == "ay"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 26) == "ay": {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 52) == "aaxz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 52) == "aaxz": {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 27) == "aay"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 27) == "aay": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 100) == "aaaaaapzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 100) == "aaaaaapzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 650) == "aaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 650) == "aaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 1000) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 1000) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 161) == "zzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 161) == "zzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 300) == "nzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 300) == "nzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 156) == "zzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 156) == "zzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 131) == "aaaaavzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 131) == "aaaaavzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 67) == "aamzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 67) == "aamzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 350) == "akzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 350) == "akzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 650) == "zzzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 650) == "zzzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 150) == "aaaaaanzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 150) == "aaaaaanzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 145) == "anzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 145) == "anzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 45) == "aaaaoz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 45) == "aaaaoz": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 160) == "zzzzz~"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 160) == "zzzzz~": {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 51) == "axz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 51) == "axz": {e}')
    
    total += 1
    try:
        result = candidate(n = 11,k = 260) == "ayzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,k = 260) == "ayzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 800) == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 800) == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 180) == "aaaaaaaapzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 180) == "aaaaaaaapzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 150) == "aaaqzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 150) == "aaaqzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 104) == "aaawzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 104) == "aaawzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 150) == "aszzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 150) == "aszzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 175) == "arzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 175) == "arzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 150) == "aaaapzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 150) == "aaaapzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 400) == "aaaafzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 400) == "aaaafzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 52) == "aaaaaaaarz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 52) == "aaaaaaaarz": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 180) == "zzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 180) == "zzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 100) == "aatzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 100) == "aatzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 200) == "aaaanzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 200) == "aaaanzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 208) == "zzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 208) == "zzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 25) == "aaw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 25) == "aaw": {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 200) == "aaaaaaaaaaaafzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 200) == "aaaaaaaaaaaafzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 150) == "aaaaaaaaakzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 150) == "aaaaaaaaakzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 2600) == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 2600) == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 78) == "aaawzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 78) == "aaawzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 225) == "aaaaaakzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 225) == "aaaaaakzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 26,k = 676) == "zzzzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 26,k = 676) == "zzzzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 30) == "acz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 30) == "acz": {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 312) == "zzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 312) == "zzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 182) == "aaxzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 182) == "aaxzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 91) == "aaajzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 91) == "aaajzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 130) == "zzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 130) == "zzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 120) == "aaamzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 120) == "aaamzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 234) == "zzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 234) == "zzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 125) == "uzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 125) == "uzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 780) == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 780) == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 520) == "zzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 520) == "zzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 1300) == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 1300) == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 50) == "aavz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 50) == "aavz": {e}')
    
    total += 1
    try:
        result = candidate(n = 11,k = 286) == "zzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,k = 286) == "zzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 200) == "aaaaaaakzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 200) == "aaaaaaakzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 230) == "vzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 230) == "vzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 10) == "aaag"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 10) == "aaag": {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 27) == "az"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 27) == "az": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 42) == "aaaaakz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 42) == "aaaaakz": {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 90) == "lzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 90) == "lzzz": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 7,k = 100) == "aaaszzz"
    assert candidate(n = 1,k = 26) == "z"
    assert candidate(n = 4,k = 40) == "aalz"
    assert candidate(n = 5,k = 73) == "aaszz"
    assert candidate(n = 10,k = 260) == "zzzzzzzzzz"
    assert candidate(n = 2,k = 2) == "aa"
    assert candidate(n = 1,k = 1) == "a"
    assert candidate(n = 2,k = 26) == "ay"
    assert candidate(n = 4,k = 52) == "aaxz"
    assert candidate(n = 3,k = 27) == "aay"
    assert candidate(n = 10,k = 100) == "aaaaaapzzz"
    assert candidate(n = 50,k = 650) == "aaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(n = 100,k = 1000) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(n = 6,k = 161) == "zzzzz"
    assert candidate(n = 12,k = 300) == "nzzzzzzzzzzz"
    assert candidate(n = 6,k = 156) == "zzzzzz"
    assert candidate(n = 10,k = 131) == "aaaaavzzzz"
    assert candidate(n = 5,k = 67) == "aamzz"
    assert candidate(n = 15,k = 350) == "akzzzzzzzzzzzzz"
    assert candidate(n = 25,k = 650) == "zzzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(n = 12,k = 150) == "aaaaaanzzzzz"
    assert candidate(n = 7,k = 145) == "anzzzzz"
    assert candidate(n = 6,k = 45) == "aaaaoz"
    assert candidate(n = 6,k = 160) == "zzzzz~"
    assert candidate(n = 3,k = 51) == "axz"
    assert candidate(n = 11,k = 260) == "ayzzzzzzzzz"
    assert candidate(n = 30,k = 800) == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(n = 15,k = 180) == "aaaaaaaapzzzzzz"
    assert candidate(n = 9,k = 150) == "aaaqzzzzz"
    assert candidate(n = 7,k = 104) == "aaawzzz"
    assert candidate(n = 7,k = 150) == "aszzzzz"
    assert candidate(n = 8,k = 175) == "arzzzzzz"
    assert candidate(n = 10,k = 150) == "aaaapzzzzz"
    assert candidate(n = 20,k = 400) == "aaaafzzzzzzzzzzzzzzz"
    assert candidate(n = 10,k = 52) == "aaaaaaaarz"
    assert candidate(n = 6,k = 180) == "zzzzz"
    assert candidate(n = 6,k = 100) == "aatzzz"
    assert candidate(n = 12,k = 200) == "aaaanzzzzzzz"
    assert candidate(n = 8,k = 208) == "zzzzzzzz"
    assert candidate(n = 3,k = 25) == "aaw"
    assert candidate(n = 20,k = 200) == "aaaaaaaaaaaafzzzzzzz"
    assert candidate(n = 15,k = 150) == "aaaaaaaaakzzzzz"
    assert candidate(n = 100,k = 2600) == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(n = 6,k = 78) == "aaawzz"
    assert candidate(n = 15,k = 225) == "aaaaaakzzzzzzzz"
    assert candidate(n = 26,k = 676) == "zzzzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(n = 3,k = 30) == "acz"
    assert candidate(n = 12,k = 312) == "zzzzzzzzzzzz"
    assert candidate(n = 9,k = 182) == "aaxzzzzzz"
    assert candidate(n = 7,k = 91) == "aaajzzz"
    assert candidate(n = 5,k = 130) == "zzzzz"
    assert candidate(n = 8,k = 120) == "aaamzzzz"
    assert candidate(n = 9,k = 234) == "zzzzzzzzz"
    assert candidate(n = 5,k = 125) == "uzzzz"
    assert candidate(n = 30,k = 780) == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(n = 20,k = 520) == "zzzzzzzzzzzzzzzzzzzz"
    assert candidate(n = 50,k = 1300) == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(n = 4,k = 50) == "aavz"
    assert candidate(n = 11,k = 286) == "zzzzzzzzzzz"
    assert candidate(n = 15,k = 200) == "aaaaaaakzzzzzzz"
    assert candidate(n = 9,k = 230) == "vzzzzzzzz"
    assert candidate(n = 4,k = 10) == "aaag"
    assert candidate(n = 2,k = 27) == "az"
    assert candidate(n = 7,k = 42) == "aaaaakz"
    assert candidate(n = 4,k = 90) == "lzzz"


