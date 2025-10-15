def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(corridor = "PPPPSSPPPPSSPPPP") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPPPSSPPPPSSPPPP") == 5: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSSSSSSS") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSSSSSSS") == 1: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SPSPSPSP") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SPSPSPSP") == 2: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSPPSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSPPSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PSSPSPSPPS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PSSPSPSPPS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SS") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SS") == 1: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPPP") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPPP") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSS") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSS") == 3: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSPPSSSS") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSPPSSSS") == 3: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPSSP") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPSSP") == 2: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPSSPSS") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPSSPSS") == 4: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPPPPSSPPPPSS") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPPPPSSPPPPSS") == 30: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPSPSPSPS") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPSPSPSPS") == 4: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSS") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSS") == 1: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSPPPSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSPPPSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSPPS") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSPPS") == 1: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPSSPPSSPP") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPSSPPSSPP") == 3: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSPPSS") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSPPSS") == 9: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSPS") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSPS") == 3: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSPPS") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSPPS") == 3: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "S") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "S") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPSPSP") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPSPSP") == 1: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SPPSPPSPPS") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SPPSPPSPPS") == 3: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPSPSPSPSPSPSPSPSP") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPSPSPSPSPSPSPSPSP") == 8: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSPSSSSPPSSPPSSSSPPSSSSPPSSSSSSSSSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSPSSSSPPSSPPSSSSPPSSSSPPSSSSSSSSSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SPPSPSPSPSPSPSPSPS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SPPSPSPSPSPSPSPSPS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPSSPSSPSSPSSPSSPSS") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPSSPSSPSSPSSPSSPSS") == 64: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPSSPPSPSSPPSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPSSPPSPSSPPSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSSSSSSSPPSSSSSSSSPPSSSSSSSSSS") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSSSSSSSPPSSSSSSSSPPSSSSSSSSSS") == 27: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSPPSSPPSS") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSPPSSPPSS") == 27: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SPSSPSSPSSPSSPSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SPSSPSSPSSPSSPSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPPPPPSSPPPPSSPPPP") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPPPPPSSPPPPSSPPPP") == 5: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPPPPPSSPPPPSSPPPPSSPPSS") == 525
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPPPPPSSPPPPSSPPPPSSPPSS") == 525: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPSSPPSSPPSSPPSS") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPSSPPSSPPSSPPSS") == 27: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPPPSSPPPPSSPPPPSSPPPPSSPPPPSSPPPP") == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPPPSSPPPPSSPPPPSSPPPPSSPPPPSSPPPP") == 625: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSPSPSPSPSPSSSSPSPS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSPSPSPSPSPSSSSPSPS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSPSPSSSSPPPPSS") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSPSPSSSSPPPPSS") == 30: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSSSSSSSSSSSSS") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSSSSSSSSSSSSS") == 3: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPPPPPPPPPPPPPPPPP") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPPPPPPPPPPPPPPPPP") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SPPSPSPSPSPSPSPSPSPS") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SPPSPSPSPSPSPSPSPSPS") == 16: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SPSPPSPSPPSPSPPSPSPP") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SPSPPSPSPPSPSPPSPSPP") == 27: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPSSPPSSPPSSPP") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPSSPPSSPPSSPP") == 9: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPSPSPSPSPS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPSPSPSPSPS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSPSSSPSSSPSSSPSS") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSPSSSPSSSPSSSPSS") == 4: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPSSPPSSSSSSSSSSSS") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPSSPPSSSSSSSSSSSS") == 3: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPPPPPPPSSPPPPSS") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPPPPPPPSSPPPPSS") == 45: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSSSSSPPSS") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSSSSSPPSS") == 9: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPPPPPSSPPPPPSS") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPPPPPSSPPPPPSS") == 42: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSPPPPSSPPSSPPSSSSPPPPSSSSSS") == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSPPPPSSPPSSPPSSSSPPPPSSSSSS") == 225: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPPPSSPPSS") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPPPSSPPSS") == 15: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSPPPPSSPPPPSSSSPPPPSS") == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSPPPPSSPPPPSSSSPPPPSS") == 125: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPPPSSPPPPSSPPPPSSPPPPSS") == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPPPSSPPPPSSPPPPSSPPPPSS") == 625: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSPSSSSSSSSSSPPSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSPSSSSSSSSSSPPSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SPPSPPSPPSPPS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SPPSPPSPPSPPS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPSPPSPSPSPSPPPSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPSPPSPSPSPSPPPSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSS") == 177147
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSS") == 177147: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPPPPPSPPPPSPPPPSPPPPS") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPPPPPSPPPPSPPPPSPPPPS") == 5: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSSSSSSSSSSSSS") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSSSSSSSSSSSSS") == 1: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSPSSPPSPSSPPSPSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSPSSPPSPSSPPSPSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPSSPPSSPPSS") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPSSPPSSPPSS") == 9: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSPSPSPSPSPSPSPSPSPSPSPSPSPSPSPSPSPSPSPS") == 1536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSPSPSPSPSPSPSPSPSPSPSPSPSPSPSPSPSPSPSPS") == 1536: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSPSSPPSSPPSSSSPPSSPPSSPPSSSSPPSSSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSPSSPPSSPPSSSSPPSSPPSSPPSSSSPPSSSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSSSSSSSSSSSSSSSSSSSSSSS") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSSSSSSSSSSSSSSSSSSSSSSS") == 1: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSPPSSPPSSPPSSSSPPSSSSPPSSSS") == 729
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSPPSSPPSSPPSSSSPPSSSSPPSSSS") == 729: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSPPPSPSPPS") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSPPPSPSPPS") == 6: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPPPSSPPPPSSPPSSPPPPSS") == 375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPPPSSPPPPSSPPSSPPPPSS") == 375: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPPPPPSPPPPPSSSSPP") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPPPPPSPPPPPSSSSPP") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPSSSSPPPPSS") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPSSSSPPPPSS") == 5: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSPPPSSSSPPSPSS") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSPPPSSSSPPSPSS") == 6: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPPPPPSSPPSS") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPPPPPSSPPSS") == 3: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSPSSPPSPSSPPSPSSPPSPSS") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSPSSPPSPSSPPSPSSPPSPSS") == 36: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSPSSSPSSSPSSSPSSSPSSSPSSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSPSSSPSSSPSSSPSSSPSSSPSSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSPSSSSPPSSPPSSSSPPSSSSPPSSSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSPSSSSPPSSPPSSSSPPSSSSPPSSSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SPPPPPPPPPPP") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SPPPPPPPPPPP") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPPPSPSPPPPSPSPPPPSP") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPPPSPSPPPPSPSPPPPSP") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPSSPPSSPPSSPPSSPPSSPPSSPPSS") == 729
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPSSPPSSPPSSPPSSPPSSPPSSPPSS") == 729: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPPPPPPPPPPPPPPPPPPP") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPPPPPPPPPPPPPPPPPPP") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPSSPSSPSSPSSPSSPSSPSS") == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPSSPSSPSSPSSPSSPSSPSS") == 128: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPPPSPSPPPSS") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPPPSPSPPPSS") == 20: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPSSPSSPPSSPSSPPSSPSSPPSS") == 216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPSSPSSPPSSPSSPPSSPSSPPSS") == 216: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPPSSPPPSSPPPSS") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPPSSPPPSSPPPSS") == 64: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPSSSPSSPSSPSSPSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPSSSPSSPSSPSSPSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSPPSSPPSSPPSSPPSSPPSS") == 729
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSPPSSPPSSPPSSPPSSPPSS") == 729: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPSSPPPPSSPPPPSS") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPSSPPPPSSPPPPSS") == 25: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SPSSSPSSSPSSSPSSSPSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SPSSSPSSSPSSSPSSSPSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PSPSPSPSPSPSPSPSPS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PSPSPSPSPSPSPSPSPS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSPSPSPSSP") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSPSPSPSSP") == 12: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSSSSSSSSSSSSSSS") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSSSSSSSSSSSSSSS") == 1: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSPPSSPPSPSSPPSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSPPSSPPSPSSPPSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSPSPPPSSSPPSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSPSPPPSSSPPSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSSSPPSSSSPPS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSSSPPSSSSPPS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPPPPPSSSSSSSSSS") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPPPPPSSSSSSSSSS") == 7: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPPPSSPPPPSSSSPPPPSSSSPPPPSSSS") == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPPPSSPPPPSSSSPPPPSSSSPPPPSSSS") == 625: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSSSSSSSPPPPPPSS") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSSSSSSSPPPPPPSS") == 7: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSPPSSSSSSPPSSSS") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSPPSSSSSSPPSSSS") == 9: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPSSPSSPSSPSSPSSPSSPSSPSSPS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPSSPSSPSSPSSPSSPSSPSSPSSPS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSPSPSPPSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSPSPSPPSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPSSPPPPSSPPSSPP") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPSSPPPPSSPPSSPP") == 15: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SPSSSPSSSPSSSPSS") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SPSSSPSSSPSSSPSS") == 4: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PSPPSPSPSPSPSPSPSPSP") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PSPPSPSPSPSPSPSPSPSP") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSSSPPSSSSSSPPSSSSSSPPSSSSSS") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSSSPPSSSSSSPPSSSSSSPPSSSSSS") == 27: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSPSSPPSSPSSPPSS") == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSPSSPPSSPSSPPSS") == 108: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSPSPSPSPSPSPSPSPSPSP") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSPSPSPSPSPSPSPSPSPSP") == 16: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPPPPPSSPPPP") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPPPPPSSPPPP") == 1: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSS") == 19683
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSS") == 19683: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSPSSPSPSSPSPSSPSPSS") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSPSSPSPSSPSPSSPSPSS") == 24: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSPPSSSPPPSSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSPPSSSPPPSSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSSSSSSSSS") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSSSSSSSSS") == 1: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSSPPPSSSSSPPPSSSS") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSSPPPSSSSSPPPSSSS") == 4: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSSSSSPPPPPPPPSSSSSSSSPPPPPPPPSSSS") == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSSSSSPPPPPPPPSSSSSSSSPPPPPPPPSSSS") == 81: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSSS") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSSS") == 1: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPPPPPSSSSSSPPSSPP") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPPPPPSSSSSSPPSSPP") == 21: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPSPSPSPSPSPSPSPSPSPSPSPSPSPS") == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPSPSPSPSPSPSPSPSPSPSPSPSPSPS") == 128: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSPPSSPPSSPPSS") == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSPPSSPPSSPPSS") == 81: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSPPPPSSSSPPPPSSSS") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSPPPPSSSSPPPPSSSS") == 25: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPSPPSSPSPPSSPSPPSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPSPPSSPSPPSSPSPPSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SPSPSP") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SPSPSP") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPPPSPSSPPPSS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPPPSPSSPPPSS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSPSPSPSPS") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSPSPSPSPS") == 4: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPPPPP") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPPPPP") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPPPPPPPPPSSPPPPSSPPSS") == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPPPPPPPPPSSPPPPSSPPSS") == 165: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSS") == 6561
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSS") == 6561: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPPPSSPPPPSSPPSS") == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPPPSSPPPPSSPPSS") == 75: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSSSSSSSSSSSSSSSSS") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSSSSSSSSSSSSSSSSS") == 1: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSPPPPSSSSPPSSSS") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSPPPPSSSSPPSSSS") == 15: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPPPPPPPPPPPPPPP") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPPPPPPPPPPPPPPP") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSPSPSPSPSPSPSPSPSS") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSPSPSPSPSPSPSPSPSS") == 16: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSPSSSSPPSPSSSS") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSPSSSSPPSPSSSS") == 6: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPSSPSSPSSPSSPSS") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPSSPSSPSSPSSPSS") == 32: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSPPSSPPSSPPSSPP") == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSPPSSPPSSPPSSPP") == 81: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPPPSSPPPPSSPPPPSSPPPPSSPPPPSS") == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPPPSSPPPPSSPPPPSSPPPPSSPPPPSS") == 625: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSPPSSPPSSPPSSPPSSPPSSPPSS") == 2187
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSPPSSPPSSPPSSPPSSPPSSPPSS") == 2187: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSPPSSSSPPSSSS") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSPPSSSSPPSSSS") == 9: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSSSSSPPPPSSSSPPPPSSSSSSPPPP") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSSSSSPPPPSSSSPPPPSSSSSSPPPP") == 25: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSPPSSPPSSPPSSPPSS") == 243
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSPPSSPPSSPPSSPPSS") == 243: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSPPSSPPSSSS") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSPPSSPPSSSS") == 27: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPSPSPSPSPSPSPS") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPSPSPSPSPSPSPS") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSPSPSPSPSS") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSPSPSPSPSS") == 12: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SPSPSPSPSPSPSPSPSPSP") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SPSPSPSPSPSPSPSPSPSP") == 16: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSSSPPPPSSSSSSSS") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSSSPPPPSSSSSSSS") == 15: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPPPSSPPSSPPSSPPPP") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPPPSSPPSSPPSSPPPP") == 9: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SPSPPSPSPPSPSPPSPSPPSP") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SPSPPSPSPPSPSPPSPSPPSP") == 0: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "PPSPSPSPSPSPPSPSPS") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "PPSPSPSPSPSPPSPSPS") == 8: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SPSPSPSPPSPS") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SPSPSPSPPSPS") == 6: {e}')
    
    total += 1
    try:
        result = candidate(corridor = "SSPPSSPPSSPPSSSSPPSSPPSSSSPPSS") == 729
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(corridor = "SSPPSSPPSSPPSSSSPPSSPPSSSSPPSS") == 729: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(corridor = "PPPPSSPPPPSSPPPP") == 5
    assert candidate(corridor = "SSSSSSSSSS") == 1
    assert candidate(corridor = "SPSPSPSP") == 2
    assert candidate(corridor = "SSSPPSS") == 0
    assert candidate(corridor = "PSSPSPSPPS") == 0
    assert candidate(corridor = "SS") == 1
    assert candidate(corridor = "PPPP") == 0
    assert candidate(corridor = "SSPPSS") == 3
    assert candidate(corridor = "SSSSPPSSSS") == 3
    assert candidate(corridor = "SSPSSP") == 2
    assert candidate(corridor = "SSPSSPSS") == 4
    assert candidate(corridor = "SSPPPPPSSPPPPSS") == 30
    assert candidate(corridor = "SSPSPSPSPS") == 4
    assert candidate(corridor = "SSSS") == 1
    assert candidate(corridor = "SSSPPPSS") == 0
    assert candidate(corridor = "SSSPPS") == 1
    assert candidate(corridor = "PPSSPPSSPP") == 3
    assert candidate(corridor = "SSPPSSPPSS") == 9
    assert candidate(corridor = "SSPPSPS") == 3
    assert candidate(corridor = "SSPPSPPS") == 3
    assert candidate(corridor = "S") == 0
    assert candidate(corridor = "PPSPSP") == 1
    assert candidate(corridor = "SPPSPPSPPS") == 3
    assert candidate(corridor = "PPSPSPSPSPSPSPSPSP") == 8
    assert candidate(corridor = "SSSPSSSSPPSSPPSSSSPPSSSSPPSSSSSSSSSS") == 0
    assert candidate(corridor = "SPPSPSPSPSPSPSPSPS") == 0
    assert candidate(corridor = "SSPSSPSSPSSPSSPSSPSS") == 64
    assert candidate(corridor = "PPSSPPSPSSPPSS") == 0
    assert candidate(corridor = "SSPPSSSSSSSSPPSSSSSSSSPPSSSSSSSSSS") == 27
    assert candidate(corridor = "SSPPSSPPSSPPSS") == 27
    assert candidate(corridor = "SPSSPSSPSSPSSPSS") == 0
    assert candidate(corridor = "PPPPPPSSPPPPSSPPPP") == 5
    assert candidate(corridor = "SSPPPPPPSSPPPPSSPPPPSSPPSS") == 525
    assert candidate(corridor = "PPSSPPSSPPSSPPSS") == 27
    assert candidate(corridor = "PPPPSSPPPPSSPPPPSSPPPPSSPPPPSSPPPP") == 625
    assert candidate(corridor = "SSSPSPSPSPSPSSSSPSPS") == 0
    assert candidate(corridor = "SSPPSPSPSSSSPPPPSS") == 30
    assert candidate(corridor = "SSPPSSSSSSSSSSSSSS") == 3
    assert candidate(corridor = "PPPPPPPPPPPPPPPPPP") == 0
    assert candidate(corridor = "SPPSPSPSPSPSPSPSPSPS") == 16
    assert candidate(corridor = "SPSPPSPSPPSPSPPSPSPP") == 27
    assert candidate(corridor = "PPSSPPSSPPSSPP") == 9
    assert candidate(corridor = "SSPSPSPSPSPS") == 0
    assert candidate(corridor = "SSSPSSSPSSSPSSSPSS") == 4
    assert candidate(corridor = "PPSSPPSSSSSSSSSSSS") == 3
    assert candidate(corridor = "SSPPPPPPPPSSPPPPSS") == 45
    assert candidate(corridor = "SSPPSSSSSSPPSS") == 9
    assert candidate(corridor = "SSPPPPPPSSPPPPPSS") == 42
    assert candidate(corridor = "SSSSPPPPSSPPSSPPSSSSPPPPSSSSSS") == 225
    assert candidate(corridor = "SSPPPPSSPPSS") == 15
    assert candidate(corridor = "SSSSPPPPSSPPPPSSSSPPPPSS") == 125
    assert candidate(corridor = "SSPPPPSSPPPPSSPPPPSSPPPPSS") == 625
    assert candidate(corridor = "SSPPSPSSSSSSSSSSPPSS") == 0
    assert candidate(corridor = "SPPSPPSPPSPPS") == 0
    assert candidate(corridor = "SSPSPPSPSPSPSPPPSS") == 0
    assert candidate(corridor = "SSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSS") == 177147
    assert candidate(corridor = "PPPPPPSPPPPSPPPPSPPPPS") == 5
    assert candidate(corridor = "SSSSSSSSSSSSSSSS") == 1
    assert candidate(corridor = "SSPPSPSSPPSPSSPPSPSS") == 0
    assert candidate(corridor = "PPSSPPSSPPSS") == 9
    assert candidate(corridor = "SSPPSPSPSPSPSPSPSPSPSPSPSPSPSPSPSPSPSPSPSPS") == 1536
    assert candidate(corridor = "SSSPSSPPSSPPSSSSPPSSPPSSPPSSSSPPSSSS") == 0
    assert candidate(corridor = "SSSSSSSSSSSSSSSSSSSSSSSSSS") == 1
    assert candidate(corridor = "SSPPSSPPSSPPSSPPSSSSPPSSSSPPSSSS") == 729
    assert candidate(corridor = "SSPPSPPPSPSPPS") == 6
    assert candidate(corridor = "SSPPPPSSPPPPSSPPSSPPPPSS") == 375
    assert candidate(corridor = "SSPPPPPPSPPPPPSSSSPP") == 0
    assert candidate(corridor = "PPSSSSPPPPSS") == 5
    assert candidate(corridor = "SSPPSPPPSSSSPPSPSS") == 6
    assert candidate(corridor = "PPPPPPSSPPSS") == 3
    assert candidate(corridor = "SSPPSPSSPPSPSSPPSPSSPPSPSS") == 36
    assert candidate(corridor = "SSSPSSSPSSSPSSSPSSSPSSSPSSS") == 0
    assert candidate(corridor = "SSSPSSSSPPSSPPSSSSPPSSSSPPSSSS") == 0
    assert candidate(corridor = "SPPPPPPPPPPP") == 0
    assert candidate(corridor = "PPPPSPSPPPPSPSPPPPSP") == 0
    assert candidate(corridor = "PPSSPPSSPPSSPPSSPPSSPPSSPPSS") == 729
    assert candidate(corridor = "PPPPPPPPPPPPPPPPPPPP") == 0
    assert candidate(corridor = "SSPSSPSSPSSPSSPSSPSSPSS") == 128
    assert candidate(corridor = "SSPPPPSPSPPPSS") == 20
    assert candidate(corridor = "PPSSPSSPPSSPSSPPSSPSSPPSS") == 216
    assert candidate(corridor = "SSPPPSSPPPSSPPPSS") == 64
    assert candidate(corridor = "SSPSSSPSSPSSPSSPSS") == 0
    assert candidate(corridor = "SSPPSSPPSSPPSSPPSSPPSSPPSS") == 729
    assert candidate(corridor = "PPSSPPPPSSPPPPSS") == 25
    assert candidate(corridor = "SPSSSPSSSPSSSPSSSPSS") == 0
    assert candidate(corridor = "PSPSPSPSPSPSPSPSPS") == 0
    assert candidate(corridor = "SSPPSSPSPSPSSP") == 12
    assert candidate(corridor = "SSSSSSSSSSSSSSSSSS") == 1
    assert candidate(corridor = "SSPPSSPPSSPPSPSSPPSS") == 0
    assert candidate(corridor = "SSPPSPSPPPSSSPPSS") == 0
    assert candidate(corridor = "SSPPSSSSPPSSSSPPS") == 0
    assert candidate(corridor = "SSPPPPPPSSSSSSSSSS") == 7
    assert candidate(corridor = "SSPPPPSSPPPPSSSSPPPPSSSSPPPPSSSS") == 625
    assert candidate(corridor = "SSSSSSSSSSPPPPPPSS") == 7
    assert candidate(corridor = "SSSSPPSSSSSSPPSSSS") == 9
    assert candidate(corridor = "SSPSSPSSPSSPSSPSSPSSPSSPSSPS") == 0
    assert candidate(corridor = "SSPPSPSPSPPSS") == 0
    assert candidate(corridor = "PPSSPPPPSSPPSSPP") == 15
    assert candidate(corridor = "SPSSSPSSSPSSSPSS") == 4
    assert candidate(corridor = "PSPPSPSPSPSPSPSPSPSP") == 0
    assert candidate(corridor = "SSSSSSPPSSSSSSPPSSSSSSPPSSSSSS") == 27
    assert candidate(corridor = "SSPPSSPSSPPSSPSSPPSS") == 108
    assert candidate(corridor = "SSSPSPSPSPSPSPSPSPSPSP") == 16
    assert candidate(corridor = "PPPPPPSSPPPP") == 1
    assert candidate(corridor = "PPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSS") == 19683
    assert candidate(corridor = "SSPPSPSSPSPSSPSPSSPSPSS") == 24
    assert candidate(corridor = "SSSPPSSSPPPSSS") == 0
    assert candidate(corridor = "SSSSSSSSSSSS") == 1
    assert candidate(corridor = "SSSSSPPPSSSSSPPPSSSS") == 4
    assert candidate(corridor = "SSSSSSSSPPPPPPPPSSSSSSSSPPPPPPPPSSSS") == 81
    assert candidate(corridor = "SSSSSS") == 1
    assert candidate(corridor = "SSPPPPPPSSSSSSPPSSPP") == 21
    assert candidate(corridor = "SSPSPSPSPSPSPSPSPSPSPSPSPSPSPS") == 128
    assert candidate(corridor = "SSPPSSPPSSPPSSPPSS") == 81
    assert candidate(corridor = "SSSSPPPPSSSSPPPPSSSS") == 25
    assert candidate(corridor = "SSPSPPSSPSPPSSPSPPSS") == 0
    assert candidate(corridor = "SPSPSP") == 0
    assert candidate(corridor = "SSPPPPSPSSPPPSS") == 0
    assert candidate(corridor = "SSSSPSPSPSPS") == 4
    assert candidate(corridor = "PPPPPP") == 0
    assert candidate(corridor = "SSPPPPPPPPPPSSPPPPSSPPSS") == 165
    assert candidate(corridor = "SSPPSSPPSSPPSSPPSSPPSSPPSSPPSSPPSS") == 6561
    assert candidate(corridor = "SSPPPPSSPPPPSSPPSS") == 75
    assert candidate(corridor = "SSSSSSSSSSSSSSSSSSSS") == 1
    assert candidate(corridor = "SSSSPPPPSSSSPPSSSS") == 15
    assert candidate(corridor = "PPPPPPPPPPPPPPPP") == 0
    assert candidate(corridor = "SSSPSPSPSPSPSPSPSPSS") == 16
    assert candidate(corridor = "SSPPSPSSSSPPSPSSSS") == 6
    assert candidate(corridor = "SSPSSPSSPSSPSSPSS") == 32
    assert candidate(corridor = "SSPPSSPPSSPPSSPPSSPP") == 81
    assert candidate(corridor = "PPPPSSPPPPSSPPPPSSPPPPSSPPPPSS") == 625
    assert candidate(corridor = "SSPPSSPPSSPPSSPPSSPPSSPPSSPPSS") == 2187
    assert candidate(corridor = "SSSSPPSSSSPPSSSS") == 9
    assert candidate(corridor = "SSSSSSPPPPSSSSPPPPSSSSSSPPPP") == 25
    assert candidate(corridor = "SSPPSSPPSSPPSSPPSSPPSS") == 243
    assert candidate(corridor = "SSPPSSPPSSPPSSSS") == 27
    assert candidate(corridor = "SSPSPSPSPSPSPSPS") == 0
    assert candidate(corridor = "SSPPSPSPSPSPSS") == 12
    assert candidate(corridor = "SPSPSPSPSPSPSPSPSPSP") == 16
    assert candidate(corridor = "SSPPSSSSPPPPSSSSSSSS") == 15
    assert candidate(corridor = "PPPPSSPPSSPPSSPPPP") == 9
    assert candidate(corridor = "SPSPPSPSPPSPSPPSPSPPSP") == 0
    assert candidate(corridor = "PPSPSPSPSPSPPSPSPS") == 8
    assert candidate(corridor = "SPSPSPSPPSPS") == 6
    assert candidate(corridor = "SSPPSSPPSSPPSSSSPPSSPPSSSSPPSS") == 729


