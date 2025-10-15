def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "s-123-p") == "p-123-s"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "s-123-p") == "p-123-s": {e}')
    
    total += 1
    try:
        result = candidate(s = "Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!": {e}')
    
    total += 1
    try:
        result = candidate(s = "-a-b-") == "-b-a-"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "-a-b-") == "-b-a-": {e}')
    
    total += 1
    try:
        result = candidate(s = "a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a-bC-dEf-ghIj") == "j-Ih-gfE-dCba": {e}')
    
    total += 1
    try:
        result = candidate(s = "A-b-C-d-E") == "E-d-C-b-A"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "A-b-C-d-E") == "E-d-C-b-A": {e}')
    
    total += 1
    try:
        result = candidate(s = "12345") == "12345"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "12345") == "12345": {e}')
    
    total += 1
    try:
        result = candidate(s = "!@#$%^&*()") == "!@#$%^&*()"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "!@#$%^&*()") == "!@#$%^&*()": {e}')
    
    total += 1
    try:
        result = candidate(s = "ab-cd") == "dc-ba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab-cd") == "dc-ba": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg") == "gfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg") == "gfedcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "!@#$%^&*()_+-=[]{}|\:;'<>,.?/1234567890") == "!@#$%^&*()_+-=[]{}|\:;'<>,.?/1234567890"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "!@#$%^&*()_+-=[]{}|\:;'<>,.?/1234567890") == "!@#$%^&*()_+-=[]{}|\:;'<>,.?/1234567890": {e}')
    
    total += 1
    try:
        result = candidate(s = "P@y-P@l") == "l@P-y@P"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "P@y-P@l") == "l@P-y@P": {e}')
    
    total += 1
    try:
        result = candidate(s = "UPPERlower123") == "rewolREPPU123"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "UPPERlower123") == "rewolREPPU123": {e}')
    
    total += 1
    try:
        result = candidate(s = "a-bC-dEf-ghIj-kLmNoP-qRsTuV-wXyZ") == "Z-yX-wVu-TsRq-PoNmLk-jIhgfE-dCba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a-bC-dEf-ghIj-kLmNoP-qRsTuV-wXyZ") == "Z-yX-wVu-TsRq-PoNmLk-jIhgfE-dCba": {e}')
    
    total += 1
    try:
        result = candidate(s = "!a-bC-dEf-ghIj!") == "!j-Ih-gfE-dCba!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "!a-bC-dEf-ghIj!") == "!j-Ih-gfE-dCba!": {e}')
    
    total += 1
    try:
        result = candidate(s = "a-zA-Z0-9") == "Z-Az-a0-9"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a-zA-Z0-9") == "Z-Az-a0-9": {e}')
    
    total += 1
    try:
        result = candidate(s = "No lemon, no melon") == "no lemon, no meloN"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "No lemon, no melon") == "no lemon, no meloN": {e}')
    
    total += 1
    try:
        result = candidate(s = "Z-y-x-W-v-U-t-S-r-Q-p-O-n-M-l-K-j-I-h-G-f-E-d-C-b-A") == "A-b-C-d-E-f-G-h-I-j-K-l-M-n-O-p-Q-r-S-t-U-v-W-x-y-Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Z-y-x-W-v-U-t-S-r-Q-p-O-n-M-l-K-j-I-h-G-f-E-d-C-b-A") == "A-b-C-d-E-f-G-h-I-j-K-l-M-n-O-p-Q-r-S-t-U-v-W-x-y-Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "M-r-2-0-D-1-E-3-N-o-5-r-7-L-8-e-9-t-0-s-1-w-2-e-3-r-4-q-5-u-6-i-7-o-8-n-9-D-0") == "D-n-2-0-o-1-i-3-u-q-5-r-7-e-8-w-9-s-0-t-1-e-2-L-3-r-4-o-5-N-6-E-7-D-8-r-9-M-0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "M-r-2-0-D-1-E-3-N-o-5-r-7-L-8-e-9-t-0-s-1-w-2-e-3-r-4-q-5-u-6-i-7-o-8-n-9-D-0") == "D-n-2-0-o-1-i-3-u-q-5-r-7-e-8-w-9-s-0-t-1-e-2-L-3-r-4-o-5-N-6-E-7-D-8-r-9-M-0": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == "ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == "ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "Reverse!This@String#With$Non%Letters^In&It*") == "tInIsre!tteL@noNhti#Wgni$rtS%sihTesr^ev&eR*"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Reverse!This@String#With$Non%Letters^In&It*") == "tInIsre!tteL@noNhti#Wgni$rtS%sihTesr^ev&eR*": {e}')
    
    total += 1
    try:
        result = candidate(s = "a!b@c#d$e%f^g&h*i(j)k-l+m,n/o\p;q:r<s>t?u.v[w]x{y}z|") == "z!y@x#w$v%u^t&s*r(q)p-o+n,m/l\k;j:i<h>g?f.e[d]c{b}a|"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a!b@c#d$e%f^g&h*i(j)k-l+m,n/o\p;q:r<s>t?u.v[w]x{y}z|") == "z!y@x#w$v%u^t&s*r(q)p-o+n,m/l\k;j:i<h>g?f.e[d]c{b}a|": {e}')
    
    total += 1
    try:
        result = candidate(s = "Hello, World!") == "dlroW, olleH!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Hello, World!") == "dlroW, olleH!": {e}')
    
    total += 1
    try:
        result = candidate(s = "1234567890qwertyuiopasdfghjklzxcvbnm-=-+=!@#$%^&*()") == "1234567890mnbvcxzlkjhgfdsapoiuytrewq-=-+=!@#$%^&*()"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1234567890qwertyuiopasdfghjklzxcvbnm-=-+=!@#$%^&*()") == "1234567890mnbvcxzlkjhgfdsapoiuytrewq-=-+=!@#$%^&*()": {e}')
    
    total += 1
    try:
        result = candidate(s = "Python3.9") == "nohtyP3.9"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Python3.9") == "nohtyP3.9": {e}')
    
    total += 1
    try:
        result = candidate(s = "aAaAaAaAaA") == "AaAaAaAaAa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aAaAaAaAaA") == "AaAaAaAaAa": {e}')
    
    total += 1
    try:
        result = candidate(s = "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z") == "z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z") == "z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a": {e}')
    
    total += 1
    try:
        result = candidate(s = "A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z") == "Z-Y-X-W-V-U-T-S-R-Q-P-O-N-M-L-K-J-I-H-G-F-E-D-C-B-A"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z") == "Z-Y-X-W-V-U-T-S-R-Q-P-O-N-M-L-K-J-I-H-G-F-E-D-C-B-A": {e}')
    
    total += 1
    try:
        result = candidate(s = "Ae-IoU-aeiou-1-2-3-4-5-6-7-8-9-0") == "uo-iea-UoIeA-1-2-3-4-5-6-7-8-9-0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Ae-IoU-aeiou-1-2-3-4-5-6-7-8-9-0") == "uo-iea-UoIeA-1-2-3-4-5-6-7-8-9-0": {e}')
    
    total += 1
    try:
        result = candidate(s = "P3r#G4m!n@G") == "G3n#m4G!r@P"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "P3r#G4m!n@G") == "G3n#m4G!r@P": {e}')
    
    total += 1
    try:
        result = candidate(s = "--aZ--") == "--Za--"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "--aZ--") == "--Za--": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz-ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "ZYXWVUTSRQPONMLKJIHGFEDCBA-zyxwvutsrqponmlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz-ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "ZYXWVUTSRQPONMLKJIHGFEDCBA-zyxwvutsrqponmlkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "A man, a plan, a canal: Panama") == "a man, a Plan, a canal: panamA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "A man, a plan, a canal: Panama") == "a man, a Plan, a canal: panamA": {e}')
    
    total += 1
    try:
        result = candidate(s = "Z-y-x-W-v-U-t-S-r-Q-p-O-n-M-l-K-j-I-h-G-f-E-d-C-b-A-1-2-3") == "A-b-C-d-E-f-G-h-I-j-K-l-M-n-O-p-Q-r-S-t-U-v-W-x-y-Z-1-2-3"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Z-y-x-W-v-U-t-S-r-Q-p-O-n-M-l-K-j-I-h-G-f-E-d-C-b-A-1-2-3") == "A-b-C-d-E-f-G-h-I-j-K-l-M-n-O-p-Q-r-S-t-U-v-W-x-y-Z-1-2-3": {e}')
    
    total += 1
    try:
        result = candidate(s = "No'Matter'How'Hard'You'Try") == "yr'TuoYdr'aHw'oHre'tta'MoN"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "No'Matter'How'Hard'You'Try") == "yr'TuoYdr'aHw'oHre'tta'MoN": {e}')
    
    total += 1
    try:
        result = candidate(s = "aA-bB-cC-dD-eE-fF-gG-hH-iI-jJ-kK-lL-mM-nN-oO-pP-qQ-rR-sS-tT-uU-vV-wW-xX-yY-zZ") == "Zz-Yy-Xx-Ww-Vv-Uu-Tt-Ss-Rr-Qq-Pp-Oo-Nn-Mm-Ll-Kk-Jj-Ii-Hh-Gg-Ff-Ee-Dd-Cc-Bb-Aa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aA-bB-cC-dD-eE-fF-gG-hH-iI-jJ-kK-lL-mM-nN-oO-pP-qQ-rR-sS-tT-uU-vV-wW-xX-yY-zZ") == "Zz-Yy-Xx-Ww-Vv-Uu-Tt-Ss-Rr-Qq-Pp-Oo-Nn-Mm-Ll-Kk-Jj-Ii-Hh-Gg-Ff-Ee-Dd-Cc-Bb-Aa": {e}')
    
    total += 1
    try:
        result = candidate(s = "aBcDeFgHiJkLmNoPqRsTuVwXyZ") == "ZyXwVuTsRqPoNmLkJiHgFeDcBa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aBcDeFgHiJkLmNoPqRsTuVwXyZ") == "ZyXwVuTsRqPoNmLkJiHgFeDcBa": {e}')
    
    total += 1
    try:
        result = candidate(s = "a-bC-dEf-ghIj-kLmNoP") == "P-oN-mLk-jIhg-fEdCba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a-bC-dEf-ghIj-kLmNoP") == "P-oN-mLk-jIhg-fEdCba": {e}')
    
    total += 1
    try:
        result = candidate(s = "7_28hT!@#%$q9") == "7_28qT!@#%$h9"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "7_28hT!@#%$q9") == "7_28qT!@#%$h9": {e}')
    
    total += 1
    try:
        result = candidate(s = "---abcXYZ---") == "---ZYXcba---"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "---abcXYZ---") == "---ZYXcba---": {e}')
    
    total += 1
    try:
        result = candidate(s = "H2O-is-a-good-solvent") == "t2n-ev-l-osdo-ogasiOH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "H2O-is-a-good-solvent") == "t2n-ev-l-osdo-ogasiOH": {e}')
    
    total += 1
    try:
        result = candidate(s = "123-abc-456-def-789") == "123-fed-456-cba-789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123-abc-456-def-789") == "123-fed-456-cba-789": {e}')
    
    total += 1
    try:
        result = candidate(s = "Hello-World!!!") == "dlroW-olleH!!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Hello-World!!!") == "dlroW-olleH!!!": {e}')
    
    total += 1
    try:
        result = candidate(s = "N0-Sc3n4r10-1-f0r-R3v3rs1ng") == "g0-ns3r4v10-1-R0r-f3r3nc1SN"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "N0-Sc3n4r10-1-f0r-R3v3rs1ng") == "g0-ns3r4v10-1-R0r-f3r3nc1SN": {e}')
    
    total += 1
    try:
        result = candidate(s = "1234567890qwertyuiopasdfghjklzxcvbnm") == "1234567890mnbvcxzlkjhgfdsapoiuytrewq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1234567890qwertyuiopasdfghjklzxcvbnm") == "1234567890mnbvcxzlkjhgfdsapoiuytrewq": {e}')
    
    total += 1
    try:
        result = candidate(s = "A1B!C2@D3#E4$F5%G6^H7&I8*J9(L0)") == "L1J!I2@H3#G4$F5%E6^D7&C8*B9(A0)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "A1B!C2@D3#E4$F5%G6^H7&I8*J9(L0)") == "L1J!I2@H3#G4$F5%E6^D7&C8*B9(A0)": {e}')
    
    total += 1
    try:
        result = candidate(s = "mIxEd-CaSe-123-!@#") == "eSaCd-ExIm-123-!@#"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mIxEd-CaSe-123-!@#") == "eSaCd-ExIm-123-!@#": {e}')
    
    total += 1
    try:
        result = candidate(s = "12345!@#$%") == "12345!@#$%"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "12345!@#$%") == "12345!@#$%": {e}')
    
    total += 1
    try:
        result = candidate(s = "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z!@#$%^&*()") == "z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a!@#$%^&*()"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z!@#$%^&*()") == "z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a!@#$%^&*()": {e}')
    
    total += 1
    try:
        result = candidate(s = "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z-0-9-8-7-6-5-4-3-2-1") == "z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a-0-9-8-7-6-5-4-3-2-1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z-0-9-8-7-6-5-4-3-2-1") == "z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a-0-9-8-7-6-5-4-3-2-1": {e}')
    
    total += 1
    try:
        result = candidate(s = "--a--b--") == "--b--a--"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "--a--b--") == "--b--a--": {e}')
    
    total += 1
    try:
        result = candidate(s = "rE9-!vA5#xY2$") == "Yx9-!Av5#Er2$"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "rE9-!vA5#xY2$") == "Yx9-!Av5#Er2$": {e}')
    
    total += 1
    try:
        result = candidate(s = "7_8A-9B-10C-11D") == "7_8D-9C-10B-11A"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "7_8A-9B-10C-11D") == "7_8D-9C-10B-11A": {e}')
    
    total += 1
    try:
        result = candidate(s = "NoLettersHere123") == "ereHsretteLoN123"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "NoLettersHere123") == "ereHsretteLoN123": {e}')
    
    total += 1
    try:
        result = candidate(s = "a1B2C3D4E5F6G7H8I9J0") == "J1I2H3G4F5E6D7C8B9a0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a1B2C3D4E5F6G7H8I9J0") == "J1I2H3G4F5E6D7C8B9a0": {e}')
    
    total += 1
    try:
        result = candidate(s = "T1h2i3s4I5s6t7h8e9F1i2n3a4l5T6e7s8t9C0a5s6e7") == "e1s2a3C4t5s6e7T8l9a1n2i3F4e5h6t7s8I9s0i5h6T7"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "T1h2i3s4I5s6t7h8e9F1i2n3a4l5T6e7s8t9C0a5s6e7") == "e1s2a3C4t5s6e7T8l9a1n2i3F4e5h6t7s8I9s0i5h6T7": {e}')
    
    total += 1
    try:
        result = candidate(s = "P@y-2-P@l-1-O!n-0-G!a-5-p%e+L-4-5-h%6-.") == "h@L-2-e@p-1-a!G-0-n!O-5-l%P+y-4-5-P%6-."
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "P@y-2-P@l-1-O!n-0-G!a-5-p%e+L-4-5-h%6-.") == "h@L-2-e@p-1-a!G-0-n!O-5-l%P+y-4-5-P%6-.": {e}')
    
    total += 1
    try:
        result = candidate(s = "z-a-y-b-x-c-w-d-v-e-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a") == "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-e-v-d-w-c-x-b-y-a-z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "z-a-y-b-x-c-w-d-v-e-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a") == "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-e-v-d-w-c-x-b-y-a-z": {e}')
    
    total += 1
    try:
        result = candidate(s = "M-2y-3r-4o-5p") == "p-2o-3r-4y-5M"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "M-2y-3r-4o-5p") == "p-2o-3r-4y-5M": {e}')
    
    total += 1
    try:
        result = candidate(s = "M-i-c-r-o-s-o-f-t-2-0-2-3") == "t-f-o-s-o-r-c-i-M-2-0-2-3"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "M-i-c-r-o-s-o-f-t-2-0-2-3") == "t-f-o-s-o-r-c-i-M-2-0-2-3": {e}')
    
    total += 1
    try:
        result = candidate(s = "A1B2C3D4E5") == "E1D2C3B4A5"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "A1B2C3D4E5") == "E1D2C3B4A5": {e}')
    
    total += 1
    try:
        result = candidate(s = "p-yt_h-nm_g-f_d-c_b-a") == "a-bc_d-fg_m-n_h-t_y-p"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "p-yt_h-nm_g-f_d-c_b-a") == "a-bc_d-fg_m-n_h-t_y-p": {e}')
    
    total += 1
    try:
        result = candidate(s = "a1B2C3d4E5f6G7H8") == "H1G2f3E4d5C6B7a8"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a1B2C3d4E5f6G7H8") == "H1G2f3E4d5C6B7a8": {e}')
    
    total += 1
    try:
        result = candidate(s = "123abc-456def-789ghi") == "123ihg-456fed-789cba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123abc-456def-789ghi") == "123ihg-456fed-789cba": {e}')
    
    total += 1
    try:
        result = candidate(s = "x-89y-76z-54w-32v-10u") == "u-89v-76w-54z-32y-10x"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "x-89y-76z-54w-32v-10u") == "u-89v-76w-54z-32y-10x": {e}')
    
    total += 1
    try:
        result = candidate(s = "a-bC-dEf-ghIj-kLmNoP-qRstUv-wXyz") == "z-yX-wvU-tsRq-PoNmLk-jIhgfE-dCba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a-bC-dEf-ghIj-kLmNoP-qRstUv-wXyz") == "z-yX-wvU-tsRq-PoNmLk-jIhgfE-dCba": {e}')
    
    total += 1
    try:
        result = candidate(s = "12345-abc-67890") == "12345-cba-67890"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "12345-abc-67890") == "12345-cba-67890": {e}')
    
    total += 1
    try:
        result = candidate(s = "!@#$%^&*()_+") == "!@#$%^&*()_+"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "!@#$%^&*()_+") == "!@#$%^&*()_+": {e}')
    
    total += 1
    try:
        result = candidate(s = "Z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a-Z") == "Z-a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a-Z") == "Z-a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "a1B2c3D4e5F6g7h8i9j0") == "j1i2h3g4F5e6D7c8B9a0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a1B2c3D4e5F6g7h8i9j0") == "j1i2h3g4F5e6D7c8B9a0": {e}')
    
    total += 1
    try:
        result = candidate(s = "12345-abc!def@gh#ij$kl%mn^op&q*r(s)t+u-v+w,x-y.z/") == "12345-zyx!wvu@ts#rq$po%nm^lk&j*i(h)g+f-e+d,c-b.a/"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "12345-abc!def@gh#ij$kl%mn^op&q*r(s)t+u-v+w,x-y.z/") == "12345-zyx!wvu@ts#rq$po%nm^lk&j*i(h)g+f-e+d,c-b.a/": {e}')
    
    total += 1
    try:
        result = candidate(s = "Zebra-123-Quokka") == "akkou-123-QarbeZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Zebra-123-Quokka") == "akkou-123-QarbeZ": {e}')
    
    total += 1
    try:
        result = candidate(s = "-a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z-") == "-z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a-"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "-a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z-") == "-z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a-": {e}')
    
    total += 1
    try:
        result = candidate(s = "NoChangeHere") == "ereHegnahCoN"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "NoChangeHere") == "ereHegnahCoN": {e}')
    
    total += 1
    try:
        result = candidate(s = "1234567890") == "1234567890"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1234567890") == "1234567890": {e}')
    
    total += 1
    try:
        result = candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "zZyYxXwWvVuUtTsSrRqQpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "zZyYxXwWvVuUtTsSrRqQpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA": {e}')
    
    total += 1
    try:
        result = candidate(s = "--hello-+++world---") == "--dlrow-+++olleh---"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "--hello-+++world---") == "--dlrow-+++olleh---": {e}')
    
    total += 1
    try:
        result = candidate(s = "M4ng0_Le3t!") == "t4eL0_gn3M!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "M4ng0_Le3t!") == "t4eL0_gn3M!": {e}')
    
    total += 1
    try:
        result = candidate(s = "The quick brown fox jumps over the lazy dog. 123") == "god yzale htrev osp mujxo fnwo rbk ciuq ehT. 123"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "The quick brown fox jumps over the lazy dog. 123") == "god yzale htrev osp mujxo fnwo rbk ciuq ehT. 123": {e}')
    
    total += 1
    try:
        result = candidate(s = "Z-a-Y-b-X-c-W-d-V-e-U-f-T-g-S-h-R-i-Q-j-P-k-L-m-N-o-M-l-K-j-I-h-G-f-E-d-C-b-A") == "A-b-C-d-E-f-G-h-I-j-K-l-M-o-N-m-L-k-P-j-Q-i-R-h-S-g-T-f-U-e-V-d-W-c-X-b-Y-a-Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Z-a-Y-b-X-c-W-d-V-e-U-f-T-g-S-h-R-i-Q-j-P-k-L-m-N-o-M-l-K-j-I-h-G-f-E-d-C-b-A") == "A-b-C-d-E-f-G-h-I-j-K-l-M-o-N-m-L-k-P-j-Q-i-R-h-S-g-T-f-U-e-V-d-W-c-X-b-Y-a-Z": {e}')
    
    total += 1
    try:
        result = candidate(s = "12345abc!@#def$%^ghi&*()") == "12345ihg!@#fed$%^cba&*()"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "12345abc!@#def$%^ghi&*()") == "12345ihg!@#fed$%^cba&*()": {e}')
    
    total += 1
    try:
        result = candidate(s = "a-bC-dEf-ghIj-klMnOp-QrStUv-WxYz") == "z-Yx-WvU-tSrQ-pOnMlk-jIhgfE-dCba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a-bC-dEf-ghIj-klMnOp-QrStUv-WxYz") == "z-Yx-WvU-tSrQ-pOnMlk-jIhgfE-dCba": {e}')
    
    total += 1
    try:
        result = candidate(s = "a!b@c#d$e%f^g&h*i(j)k_l+m-n+o*p*q*r-s*t*u*v*w*x*y*z") == "z!y@x#w$v%u^t&s*r(q)p_o+n-m+l*k*j*i-h*g*f*e*d*c*b*a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a!b@c#d$e%f^g&h*i(j)k_l+m-n+o*p*q*r-s*t*u*v*w*x*y*z") == "z!y@x#w$v%u^t&s*r(q)p_o+n-m+l*k*j*i-h*g*f*e*d*c*b*a": {e}')
    
    total += 1
    try:
        result = candidate(s = "---") == "---"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "---") == "---": {e}')
    
    total += 1
    try:
        result = candidate(s = "sToP-If-YoU-CaN") == "NaCU-oY-fIP-oTs"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "sToP-If-YoU-CaN") == "NaCU-oY-fIP-oTs": {e}')
    
    total += 1
    try:
        result = candidate(s = "Test1ng-Leet=code-Q!!@#") == "Qedo1ct-eeLg=ntse-T!!@#"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Test1ng-Leet=code-Q!!@#") == "Qedo1ct-eeLg=ntse-T!!@#": {e}')
    
    total += 1
    try:
        result = candidate(s = "123-abc-456-def") == "123-fed-456-cba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123-abc-456-def") == "123-fed-456-cba": {e}')
    
    total += 1
    try:
        result = candidate(s = "H-e-l-l-o-,-W-o-r-l-d-!") == "d-l-r-o-W-,-o-l-l-e-H-!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "H-e-l-l-o-,-W-o-r-l-d-!") == "d-l-r-o-W-,-o-l-l-e-H-!": {e}')
    
    total += 1
    try:
        result = candidate(s = "!@#$%^&*()_+-=[]{}|;':,.<>?") == "!@#$%^&*()_+-=[]{}|;':,.<>?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "!@#$%^&*()_+-=[]{}|;':,.<>?") == "!@#$%^&*()_+-=[]{}|;':,.<>?": {e}')
    
    total += 1
    try:
        result = candidate(s = "a-bC-dEf-ghIj-kLmNoP-qRsTuVwXyZ") == "Z-yX-wVu-TsRq-PoNmLk-jIhgfEdCba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a-bC-dEf-ghIj-kLmNoP-qRsTuVwXyZ") == "Z-yX-wVu-TsRq-PoNmLk-jIhgfEdCba": {e}')
    
    total += 1
    try:
        result = candidate(s = "A-man,a-plan,a-canal-Panama!") == "a-man,a-Plan,a-canal-panamA!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "A-man,a-plan,a-canal-Panama!") == "a-man,a-Plan,a-canal-panamA!": {e}')
    
    total += 1
    try:
        result = candidate(s = "123--abcXYZ!") == "123--ZYXcba!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123--abcXYZ!") == "123--ZYXcba!": {e}')
    
    total += 1
    try:
        result = candidate(s = "Python3.8") == "nohtyP3.8"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Python3.8") == "nohtyP3.8": {e}')
    
    total += 1
    try:
        result = candidate(s = "M-k-e-e-t-i-n-g-2-0-2-3") == "g-n-i-t-e-e-k-M-2-0-2-3"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "M-k-e-e-t-i-n-g-2-0-2-3") == "g-n-i-t-e-e-k-M-2-0-2-3": {e}')
    
    total += 1
    try:
        result = candidate(s = "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z-A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z") == "Z-Y-X-W-V-U-T-S-R-Q-P-O-N-M-L-K-J-I-H-G-F-E-D-C-B-A-z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z-A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z") == "Z-Y-X-W-V-U-T-S-R-Q-P-O-N-M-L-K-J-I-H-G-F-E-D-C-B-A-z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a": {e}')
    
    total += 1
    try:
        result = candidate(s = "a-zA-Z0-9!@#$%^&*()_+=-") == "Z-Az-a0-9!@#$%^&*()_+=-"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a-zA-Z0-9!@#$%^&*()_+=-") == "Z-Az-a0-9!@#$%^&*()_+=-": {e}')
    
    total += 1
    try:
        result = candidate(s = "A1B2C3D4E5F6G7H8I9J0") == "J1I2H3G4F5E6D7C8B9A0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "A1B2C3D4E5F6G7H8I9J0") == "J1I2H3G4F5E6D7C8B9A0": {e}')
    
    total += 1
    try:
        result = candidate(s = "Reverse-This-String-123") == "gnirtSs-ihTe-sreveR-123"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Reverse-This-String-123") == "gnirtSs-ihTe-sreveR-123": {e}')
    
    total += 1
    try:
        result = candidate(s = "M-I-L-O-N") == "N-O-L-I-M"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "M-I-L-O-N") == "N-O-L-I-M": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "s-123-p") == "p-123-s"
    assert candidate(s = "Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"
    assert candidate(s = "-a-b-") == "-b-a-"
    assert candidate(s = "a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
    assert candidate(s = "A-b-C-d-E") == "E-d-C-b-A"
    assert candidate(s = "12345") == "12345"
    assert candidate(s = "!@#$%^&*()") == "!@#$%^&*()"
    assert candidate(s = "ab-cd") == "dc-ba"
    assert candidate(s = "abcdefg") == "gfedcba"
    assert candidate(s = "!@#$%^&*()_+-=[]{}|\:;'<>,.?/1234567890") == "!@#$%^&*()_+-=[]{}|\:;'<>,.?/1234567890"
    assert candidate(s = "P@y-P@l") == "l@P-y@P"
    assert candidate(s = "UPPERlower123") == "rewolREPPU123"
    assert candidate(s = "a-bC-dEf-ghIj-kLmNoP-qRsTuV-wXyZ") == "Z-yX-wVu-TsRq-PoNmLk-jIhgfE-dCba"
    assert candidate(s = "!a-bC-dEf-ghIj!") == "!j-Ih-gfE-dCba!"
    assert candidate(s = "a-zA-Z0-9") == "Z-Az-a0-9"
    assert candidate(s = "No lemon, no melon") == "no lemon, no meloN"
    assert candidate(s = "Z-y-x-W-v-U-t-S-r-Q-p-O-n-M-l-K-j-I-h-G-f-E-d-C-b-A") == "A-b-C-d-E-f-G-h-I-j-K-l-M-n-O-p-Q-r-S-t-U-v-W-x-y-Z"
    assert candidate(s = "M-r-2-0-D-1-E-3-N-o-5-r-7-L-8-e-9-t-0-s-1-w-2-e-3-r-4-q-5-u-6-i-7-o-8-n-9-D-0") == "D-n-2-0-o-1-i-3-u-q-5-r-7-e-8-w-9-s-0-t-1-e-2-L-3-r-4-o-5-N-6-E-7-D-8-r-9-M-0"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == "ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba"
    assert candidate(s = "Reverse!This@String#With$Non%Letters^In&It*") == "tInIsre!tteL@noNhti#Wgni$rtS%sihTesr^ev&eR*"
    assert candidate(s = "a!b@c#d$e%f^g&h*i(j)k-l+m,n/o\p;q:r<s>t?u.v[w]x{y}z|") == "z!y@x#w$v%u^t&s*r(q)p-o+n,m/l\k;j:i<h>g?f.e[d]c{b}a|"
    assert candidate(s = "Hello, World!") == "dlroW, olleH!"
    assert candidate(s = "1234567890qwertyuiopasdfghjklzxcvbnm-=-+=!@#$%^&*()") == "1234567890mnbvcxzlkjhgfdsapoiuytrewq-=-+=!@#$%^&*()"
    assert candidate(s = "Python3.9") == "nohtyP3.9"
    assert candidate(s = "aAaAaAaAaA") == "AaAaAaAaAa"
    assert candidate(s = "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z") == "z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a"
    assert candidate(s = "A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z") == "Z-Y-X-W-V-U-T-S-R-Q-P-O-N-M-L-K-J-I-H-G-F-E-D-C-B-A"
    assert candidate(s = "Ae-IoU-aeiou-1-2-3-4-5-6-7-8-9-0") == "uo-iea-UoIeA-1-2-3-4-5-6-7-8-9-0"
    assert candidate(s = "P3r#G4m!n@G") == "G3n#m4G!r@P"
    assert candidate(s = "--aZ--") == "--Za--"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz-ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "ZYXWVUTSRQPONMLKJIHGFEDCBA-zyxwvutsrqponmlkjihgfedcba"
    assert candidate(s = "A man, a plan, a canal: Panama") == "a man, a Plan, a canal: panamA"
    assert candidate(s = "Z-y-x-W-v-U-t-S-r-Q-p-O-n-M-l-K-j-I-h-G-f-E-d-C-b-A-1-2-3") == "A-b-C-d-E-f-G-h-I-j-K-l-M-n-O-p-Q-r-S-t-U-v-W-x-y-Z-1-2-3"
    assert candidate(s = "No'Matter'How'Hard'You'Try") == "yr'TuoYdr'aHw'oHre'tta'MoN"
    assert candidate(s = "aA-bB-cC-dD-eE-fF-gG-hH-iI-jJ-kK-lL-mM-nN-oO-pP-qQ-rR-sS-tT-uU-vV-wW-xX-yY-zZ") == "Zz-Yy-Xx-Ww-Vv-Uu-Tt-Ss-Rr-Qq-Pp-Oo-Nn-Mm-Ll-Kk-Jj-Ii-Hh-Gg-Ff-Ee-Dd-Cc-Bb-Aa"
    assert candidate(s = "aBcDeFgHiJkLmNoPqRsTuVwXyZ") == "ZyXwVuTsRqPoNmLkJiHgFeDcBa"
    assert candidate(s = "a-bC-dEf-ghIj-kLmNoP") == "P-oN-mLk-jIhg-fEdCba"
    assert candidate(s = "7_28hT!@#%$q9") == "7_28qT!@#%$h9"
    assert candidate(s = "---abcXYZ---") == "---ZYXcba---"
    assert candidate(s = "H2O-is-a-good-solvent") == "t2n-ev-l-osdo-ogasiOH"
    assert candidate(s = "123-abc-456-def-789") == "123-fed-456-cba-789"
    assert candidate(s = "Hello-World!!!") == "dlroW-olleH!!!"
    assert candidate(s = "N0-Sc3n4r10-1-f0r-R3v3rs1ng") == "g0-ns3r4v10-1-R0r-f3r3nc1SN"
    assert candidate(s = "1234567890qwertyuiopasdfghjklzxcvbnm") == "1234567890mnbvcxzlkjhgfdsapoiuytrewq"
    assert candidate(s = "A1B!C2@D3#E4$F5%G6^H7&I8*J9(L0)") == "L1J!I2@H3#G4$F5%E6^D7&C8*B9(A0)"
    assert candidate(s = "mIxEd-CaSe-123-!@#") == "eSaCd-ExIm-123-!@#"
    assert candidate(s = "12345!@#$%") == "12345!@#$%"
    assert candidate(s = "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z!@#$%^&*()") == "z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a!@#$%^&*()"
    assert candidate(s = "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z-0-9-8-7-6-5-4-3-2-1") == "z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a-0-9-8-7-6-5-4-3-2-1"
    assert candidate(s = "--a--b--") == "--b--a--"
    assert candidate(s = "rE9-!vA5#xY2$") == "Yx9-!Av5#Er2$"
    assert candidate(s = "7_8A-9B-10C-11D") == "7_8D-9C-10B-11A"
    assert candidate(s = "NoLettersHere123") == "ereHsretteLoN123"
    assert candidate(s = "a1B2C3D4E5F6G7H8I9J0") == "J1I2H3G4F5E6D7C8B9a0"
    assert candidate(s = "T1h2i3s4I5s6t7h8e9F1i2n3a4l5T6e7s8t9C0a5s6e7") == "e1s2a3C4t5s6e7T8l9a1n2i3F4e5h6t7s8I9s0i5h6T7"
    assert candidate(s = "P@y-2-P@l-1-O!n-0-G!a-5-p%e+L-4-5-h%6-.") == "h@L-2-e@p-1-a!G-0-n!O-5-l%P+y-4-5-P%6-."
    assert candidate(s = "z-a-y-b-x-c-w-d-v-e-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a") == "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-e-v-d-w-c-x-b-y-a-z"
    assert candidate(s = "M-2y-3r-4o-5p") == "p-2o-3r-4y-5M"
    assert candidate(s = "M-i-c-r-o-s-o-f-t-2-0-2-3") == "t-f-o-s-o-r-c-i-M-2-0-2-3"
    assert candidate(s = "A1B2C3D4E5") == "E1D2C3B4A5"
    assert candidate(s = "p-yt_h-nm_g-f_d-c_b-a") == "a-bc_d-fg_m-n_h-t_y-p"
    assert candidate(s = "a1B2C3d4E5f6G7H8") == "H1G2f3E4d5C6B7a8"
    assert candidate(s = "123abc-456def-789ghi") == "123ihg-456fed-789cba"
    assert candidate(s = "x-89y-76z-54w-32v-10u") == "u-89v-76w-54z-32y-10x"
    assert candidate(s = "a-bC-dEf-ghIj-kLmNoP-qRstUv-wXyz") == "z-yX-wvU-tsRq-PoNmLk-jIhgfE-dCba"
    assert candidate(s = "12345-abc-67890") == "12345-cba-67890"
    assert candidate(s = "!@#$%^&*()_+") == "!@#$%^&*()_+"
    assert candidate(s = "Z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a-Z") == "Z-a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-Z"
    assert candidate(s = "a1B2c3D4e5F6g7h8i9j0") == "j1i2h3g4F5e6D7c8B9a0"
    assert candidate(s = "12345-abc!def@gh#ij$kl%mn^op&q*r(s)t+u-v+w,x-y.z/") == "12345-zyx!wvu@ts#rq$po%nm^lk&j*i(h)g+f-e+d,c-b.a/"
    assert candidate(s = "Zebra-123-Quokka") == "akkou-123-QarbeZ"
    assert candidate(s = "-a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z-") == "-z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a-"
    assert candidate(s = "NoChangeHere") == "ereHegnahCoN"
    assert candidate(s = "1234567890") == "1234567890"
    assert candidate(s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == "zZyYxXwWvVuUtTsSrRqQpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA"
    assert candidate(s = "--hello-+++world---") == "--dlrow-+++olleh---"
    assert candidate(s = "M4ng0_Le3t!") == "t4eL0_gn3M!"
    assert candidate(s = "The quick brown fox jumps over the lazy dog. 123") == "god yzale htrev osp mujxo fnwo rbk ciuq ehT. 123"
    assert candidate(s = "Z-a-Y-b-X-c-W-d-V-e-U-f-T-g-S-h-R-i-Q-j-P-k-L-m-N-o-M-l-K-j-I-h-G-f-E-d-C-b-A") == "A-b-C-d-E-f-G-h-I-j-K-l-M-o-N-m-L-k-P-j-Q-i-R-h-S-g-T-f-U-e-V-d-W-c-X-b-Y-a-Z"
    assert candidate(s = "12345abc!@#def$%^ghi&*()") == "12345ihg!@#fed$%^cba&*()"
    assert candidate(s = "a-bC-dEf-ghIj-klMnOp-QrStUv-WxYz") == "z-Yx-WvU-tSrQ-pOnMlk-jIhgfE-dCba"
    assert candidate(s = "a!b@c#d$e%f^g&h*i(j)k_l+m-n+o*p*q*r-s*t*u*v*w*x*y*z") == "z!y@x#w$v%u^t&s*r(q)p_o+n-m+l*k*j*i-h*g*f*e*d*c*b*a"
    assert candidate(s = "---") == "---"
    assert candidate(s = "sToP-If-YoU-CaN") == "NaCU-oY-fIP-oTs"
    assert candidate(s = "Test1ng-Leet=code-Q!!@#") == "Qedo1ct-eeLg=ntse-T!!@#"
    assert candidate(s = "123-abc-456-def") == "123-fed-456-cba"
    assert candidate(s = "H-e-l-l-o-,-W-o-r-l-d-!") == "d-l-r-o-W-,-o-l-l-e-H-!"
    assert candidate(s = "!@#$%^&*()_+-=[]{}|;':,.<>?") == "!@#$%^&*()_+-=[]{}|;':,.<>?"
    assert candidate(s = "a-bC-dEf-ghIj-kLmNoP-qRsTuVwXyZ") == "Z-yX-wVu-TsRq-PoNmLk-jIhgfEdCba"
    assert candidate(s = "A-man,a-plan,a-canal-Panama!") == "a-man,a-Plan,a-canal-panamA!"
    assert candidate(s = "123--abcXYZ!") == "123--ZYXcba!"
    assert candidate(s = "Python3.8") == "nohtyP3.8"
    assert candidate(s = "M-k-e-e-t-i-n-g-2-0-2-3") == "g-n-i-t-e-e-k-M-2-0-2-3"
    assert candidate(s = "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z-A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z") == "Z-Y-X-W-V-U-T-S-R-Q-P-O-N-M-L-K-J-I-H-G-F-E-D-C-B-A-z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a"
    assert candidate(s = "a-zA-Z0-9!@#$%^&*()_+=-") == "Z-Az-a0-9!@#$%^&*()_+=-"
    assert candidate(s = "A1B2C3D4E5F6G7H8I9J0") == "J1I2H3G4F5E6D7C8B9A0"
    assert candidate(s = "Reverse-This-String-123") == "gnirtSs-ihTe-sreveR-123"
    assert candidate(s = "M-I-L-O-N") == "N-O-L-I-M"


