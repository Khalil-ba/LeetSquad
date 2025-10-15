def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 1000000000) == [23658, 42269]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000) == [23658, 42269]: {e}')
    
    total += 1
    try:
        result = candidate(num = 999) == [25, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999) == [25, 40]: {e}')
    
    total += 1
    try:
        result = candidate(num = 8) == [3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8) == [3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(num = 1) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(num = 100) == [6, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100) == [6, 17]: {e}')
    
    total += 1
    try:
        result = candidate(num = 123) == [5, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123) == [5, 25]: {e}')
    
    total += 1
    try:
        result = candidate(num = 100000000) == [7122, 14041]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100000000) == [7122, 14041]: {e}')
    
    total += 1
    try:
        result = candidate(num = 111111111) == [9352, 11881]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111111111) == [9352, 11881]: {e}')
    
    total += 1
    try:
        result = candidate(num = 555555555) == [1457, 381301]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 555555555) == [1457, 381301]: {e}')
    
    total += 1
    try:
        result = candidate(num = 456789) == [170, 2687]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 456789) == [170, 2687]: {e}')
    
    total += 1
    try:
        result = candidate(num = 888888888) == [21847, 40687]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 888888888) == [21847, 40687]: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999998) == [31250, 32000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999998) == [31250, 32000]: {e}')
    
    total += 1
    try:
        result = candidate(num = 4) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(num = 234567890) == [13707, 17113]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 234567890) == [13707, 17113]: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999997) == [2997, 333667]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999997) == [2997, 333667]: {e}')
    
    total += 1
    try:
        result = candidate(num = 1048575) == [1024, 1024]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1048575) == [1024, 1024]: {e}')
    
    total += 1
    try:
        result = candidate(num = 800000000) == [20201, 39602]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 800000000) == [20201, 39602]: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789) == [370, 333667]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789) == [370, 333667]: {e}')
    
    total += 1
    try:
        result = candidate(num = 300000000) == [49, 6122449]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 300000000) == [49, 6122449]: {e}')
    
    total += 1
    try:
        result = candidate(num = 104729) == [30, 3491]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 104729) == [30, 3491]: {e}')
    
    total += 1
    try:
        result = candidate(num = 65535) == [256, 256]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 65535) == [256, 256]: {e}')
    
    total += 1
    try:
        result = candidate(num = 500000000) == [11829, 42269]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 500000000) == [11829, 42269]: {e}')
    
    total += 1
    try:
        result = candidate(num = 499999999) == [20000, 25000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 499999999) == [20000, 25000]: {e}')
    
    total += 1
    try:
        result = candidate(num = 135792468) == [7810, 17387]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 135792468) == [7810, 17387]: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000001) == [23658, 42269]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000001) == [23658, 42269]: {e}')
    
    total += 1
    try:
        result = candidate(num = 77777777) == [7213, 10783]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 77777777) == [7213, 10783]: {e}')
    
    total += 1
    try:
        result = candidate(num = 2000000000) == [38038, 52579]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2000000000) == [38038, 52579]: {e}')
    
    total += 1
    try:
        result = candidate(num = 100000001) == [7122, 14041]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100000001) == [7122, 14041]: {e}')
    
    total += 1
    try:
        result = candidate(num = 499999) == [625, 800]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 499999) == [625, 800]: {e}')
    
    total += 1
    try:
        result = candidate(num = 319912345) == [12039, 26573]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 319912345) == [12039, 26573]: {e}')
    
    total += 1
    try:
        result = candidate(num = 345678901) == [10853, 31851]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 345678901) == [10853, 31851]: {e}')
    
    total += 1
    try:
        result = candidate(num = 456789123) == [17525, 26065]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 456789123) == [17525, 26065]: {e}')
    
    total += 1
    try:
        result = candidate(num = 789012345) == [24293, 32479]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 789012345) == [24293, 32479]: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321) == [1402, 704461]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321) == [1402, 704461]: {e}')
    
    total += 1
    try:
        result = candidate(num = 1048576) == [17, 61681]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1048576) == [17, 61681]: {e}')
    
    total += 1
    try:
        result = candidate(num = 2) == [2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2) == [2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(num = 8675309) == [2653, 3270]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8675309) == [2653, 3270]: {e}')
    
    total += 1
    try:
        result = candidate(num = 600000001) == [98, 6122449]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 600000001) == [98, 6122449]: {e}')
    
    total += 1
    try:
        result = candidate(num = 1122334455) == [8, 140291807]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1122334455) == [8, 140291807]: {e}')
    
    total += 1
    try:
        result = candidate(num = 42424242) == [124, 342131]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 42424242) == [124, 342131]: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999999) == [31250, 32000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999999) == [31250, 32000]: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000) == [101, 9901]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000) == [101, 9901]: {e}')
    
    total += 1
    try:
        result = candidate(num = 49) == [5, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 49) == [5, 10]: {e}')
    
    total += 1
    try:
        result = candidate(num = 750000000) == [4727, 158663]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 750000000) == [4727, 158663]: {e}')
    
    total += 1
    try:
        result = candidate(num = 876543210) == [12652, 69281]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 876543210) == [12652, 69281]: {e}')
    
    total += 1
    try:
        result = candidate(num = 500000001) == [3362, 148721]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 500000001) == [3362, 148721]: {e}')
    
    total += 1
    try:
        result = candidate(num = 65536) == [198, 331]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 65536) == [198, 331]: {e}')
    
    total += 1
    try:
        result = candidate(num = 314159) == [560, 561]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 314159) == [560, 561]: {e}')
    
    total += 1
    try:
        result = candidate(num = 271828182) == [11, 24711653]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 271828182) == [11, 24711653]: {e}')
    
    total += 1
    try:
        result = candidate(num = 678901234) == [22686, 29926]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 678901234) == [22686, 29926]: {e}')
    
    total += 1
    try:
        result = candidate(num = 2147483647) == [32768, 65536]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2147483647) == [32768, 65536]: {e}')
    
    total += 1
    try:
        result = candidate(num = 3) == [2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3) == [2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(num = 15) == [4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 15) == [4, 4]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 1000000000) == [23658, 42269]
    assert candidate(num = 999) == [25, 40]
    assert candidate(num = 8) == [3, 3]
    assert candidate(num = 1) == [1, 2]
    assert candidate(num = 100) == [6, 17]
    assert candidate(num = 123) == [5, 25]
    assert candidate(num = 100000000) == [7122, 14041]
    assert candidate(num = 111111111) == [9352, 11881]
    assert candidate(num = 555555555) == [1457, 381301]
    assert candidate(num = 456789) == [170, 2687]
    assert candidate(num = 888888888) == [21847, 40687]
    assert candidate(num = 999999998) == [31250, 32000]
    assert candidate(num = 4) == [2, 3]
    assert candidate(num = 234567890) == [13707, 17113]
    assert candidate(num = 999999997) == [2997, 333667]
    assert candidate(num = 1048575) == [1024, 1024]
    assert candidate(num = 800000000) == [20201, 39602]
    assert candidate(num = 123456789) == [370, 333667]
    assert candidate(num = 300000000) == [49, 6122449]
    assert candidate(num = 104729) == [30, 3491]
    assert candidate(num = 65535) == [256, 256]
    assert candidate(num = 500000000) == [11829, 42269]
    assert candidate(num = 499999999) == [20000, 25000]
    assert candidate(num = 135792468) == [7810, 17387]
    assert candidate(num = 1000000001) == [23658, 42269]
    assert candidate(num = 77777777) == [7213, 10783]
    assert candidate(num = 2000000000) == [38038, 52579]
    assert candidate(num = 100000001) == [7122, 14041]
    assert candidate(num = 499999) == [625, 800]
    assert candidate(num = 319912345) == [12039, 26573]
    assert candidate(num = 345678901) == [10853, 31851]
    assert candidate(num = 456789123) == [17525, 26065]
    assert candidate(num = 789012345) == [24293, 32479]
    assert candidate(num = 987654321) == [1402, 704461]
    assert candidate(num = 1048576) == [17, 61681]
    assert candidate(num = 2) == [2, 2]
    assert candidate(num = 8675309) == [2653, 3270]
    assert candidate(num = 600000001) == [98, 6122449]
    assert candidate(num = 1122334455) == [8, 140291807]
    assert candidate(num = 42424242) == [124, 342131]
    assert candidate(num = 999999999) == [31250, 32000]
    assert candidate(num = 1000000) == [101, 9901]
    assert candidate(num = 49) == [5, 10]
    assert candidate(num = 750000000) == [4727, 158663]
    assert candidate(num = 876543210) == [12652, 69281]
    assert candidate(num = 500000001) == [3362, 148721]
    assert candidate(num = 65536) == [198, 331]
    assert candidate(num = 314159) == [560, 561]
    assert candidate(num = 271828182) == [11, 24711653]
    assert candidate(num = 678901234) == [22686, 29926]
    assert candidate(num = 2147483647) == [32768, 65536]
    assert candidate(num = 3) == [2, 2]
    assert candidate(num = 15) == [4, 4]


