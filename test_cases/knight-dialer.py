def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 46: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 540641702
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 540641702: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 267287516
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 267287516: {e}')
    
    total += 1
    try:
        result = candidate(n = 2500) == 851996060
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2500) == 851996060: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 406880451
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 406880451: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 84202957
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 84202957: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 88106097
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 88106097: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 14912
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 14912: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 240: {e}')
    
    total += 1
    try:
        result = candidate(n = 3131) == 136006598
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3131) == 136006598: {e}')
    
    total += 1
    try:
        result = candidate(n = 4000) == 315083963
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4000) == 315083963: {e}')
    
    total += 1
    try:
        result = candidate(n = 1600) == 585618181
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1600) == 585618181: {e}')
    
    total += 1
    try:
        result = candidate(n = 4750) == 955420830
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4750) == 955420830: {e}')
    
    total += 1
    try:
        result = candidate(n = 4600) == 152432289
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4600) == 152432289: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000) == 71794716
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000) == 71794716: {e}')
    
    total += 1
    try:
        result = candidate(n = 3750) == 17358003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3750) == 17358003: {e}')
    
    total += 1
    try:
        result = candidate(n = 2400) == 248946071
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2400) == 248946071: {e}')
    
    total += 1
    try:
        result = candidate(n = 3333) == 857043783
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3333) == 857043783: {e}')
    
    total += 1
    try:
        result = candidate(n = 3500) == 624537543
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3500) == 624537543: {e}')
    
    total += 1
    try:
        result = candidate(n = 3000) == 447863713
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3000) == 447863713: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 986742198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 986742198: {e}')
    
    total += 1
    try:
        result = candidate(n = 1200) == 823605881
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1200) == 823605881: {e}')
    
    total += 1
    try:
        result = candidate(n = 4900) == 790356323
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4900) == 790356323: {e}')
    
    total += 1
    try:
        result = candidate(n = 2750) == 49052199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2750) == 49052199: {e}')
    
    total += 1
    try:
        result = candidate(n = 1800) == 159765442
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1800) == 159765442: {e}')
    
    total += 1
    try:
        result = candidate(n = 2800) == 779464575
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2800) == 779464575: {e}')
    
    total += 1
    try:
        result = candidate(n = 250) == 296754066
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250) == 296754066: {e}')
    
    total += 1
    try:
        result = candidate(n = 4250) == 12437801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4250) == 12437801: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 58689536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 58689536: {e}')
    
    total += 1
    try:
        result = candidate(n = 1250) == 926597988
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1250) == 926597988: {e}')
    
    total += 1
    try:
        result = candidate(n = 3132) == 915594565
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3132) == 915594565: {e}')
    
    total += 1
    try:
        result = candidate(n = 800) == 709497038
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800) == 709497038: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 944000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 944000: {e}')
    
    total += 1
    try:
        result = candidate(n = 4999) == 659158877
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4999) == 659158877: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 38950354
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 38950354: {e}')
    
    total += 1
    try:
        result = candidate(n = 400) == 23117445
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400) == 23117445: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234) == 758728301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234) == 758728301: {e}')
    
    total += 1
    try:
        result = candidate(n = 750) == 185434245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750) == 185434245: {e}')
    
    total += 1
    try:
        result = candidate(n = 4500) == 756988614
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4500) == 756988614: {e}')
    
    total += 1
    try:
        result = candidate(n = 1500) == 487569438
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1500) == 487569438: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 46
    assert candidate(n = 100) == 540641702
    assert candidate(n = 50) == 267287516
    assert candidate(n = 2500) == 851996060
    assert candidate(n = 5000) == 406880451
    assert candidate(n = 2) == 20
    assert candidate(n = 1) == 10
    assert candidate(n = 500) == 84202957
    assert candidate(n = 1000) == 88106097
    assert candidate(n = 10) == 14912
    assert candidate(n = 5) == 240
    assert candidate(n = 3131) == 136006598
    assert candidate(n = 4000) == 315083963
    assert candidate(n = 1600) == 585618181
    assert candidate(n = 4750) == 955420830
    assert candidate(n = 4600) == 152432289
    assert candidate(n = 2000) == 71794716
    assert candidate(n = 3750) == 17358003
    assert candidate(n = 2400) == 248946071
    assert candidate(n = 3333) == 857043783
    assert candidate(n = 3500) == 624537543
    assert candidate(n = 3000) == 447863713
    assert candidate(n = 30) == 986742198
    assert candidate(n = 1200) == 823605881
    assert candidate(n = 4900) == 790356323
    assert candidate(n = 2750) == 49052199
    assert candidate(n = 1800) == 159765442
    assert candidate(n = 2800) == 779464575
    assert candidate(n = 250) == 296754066
    assert candidate(n = 4250) == 12437801
    assert candidate(n = 20) == 58689536
    assert candidate(n = 1250) == 926597988
    assert candidate(n = 3132) == 915594565
    assert candidate(n = 800) == 709497038
    assert candidate(n = 15) == 944000
    assert candidate(n = 4999) == 659158877
    assert candidate(n = 200) == 38950354
    assert candidate(n = 400) == 23117445
    assert candidate(n = 1234) == 758728301
    assert candidate(n = 750) == 185434245
    assert candidate(n = 4500) == 756988614
    assert candidate(n = 1500) == 487569438


