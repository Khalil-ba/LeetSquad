def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(celsius = 122.11) == [395.26, 251.798]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 122.11) == [395.26, 251.798]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 1000.0) == [1273.15, 1832.0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 1000.0) == [1273.15, 1832.0]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 0.0) == [273.15, 32.0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 0.0) == [273.15, 32.0]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 500.0) == [773.15, 932.0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 500.0) == [773.15, 932.0]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 100.0) == [373.15, 212.0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 100.0) == [373.15, 212.0]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 500.75) == [773.9, 933.35]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 500.75) == [773.9, 933.35]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 36.5) == [309.65, 97.7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 36.5) == [309.65, 97.7]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 25.0) == [298.15, 77.0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 25.0) == [298.15, 77.0]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 273.15) == [546.3, 523.67]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 273.15) == [546.3, 523.67]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 42.876543) == [316.02654299999995, 109.1777774]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 42.876543) == [316.02654299999995, 109.1777774]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 12.34) == [285.48999999999995, 54.212]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 12.34) == [285.48999999999995, 54.212]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 37.0) == [310.15, 98.60000000000001]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 37.0) == [310.15, 98.60000000000001]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 25.55555) == [298.70554999999996, 77.99999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 25.55555) == [298.70554999999996, 77.99999]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 150.75) == [423.9, 303.35]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 150.75) == [423.9, 303.35]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = -0.01) == [273.14, 31.982]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = -0.01) == [273.14, 31.982]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 234.56) == [507.71, 454.208]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 234.56) == [507.71, 454.208]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 750.5) == [1023.65, 1382.9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 750.5) == [1023.65, 1382.9]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 77.77777) == [350.92777, 171.999986]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 77.77777) == [350.92777, 171.999986]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 456.78) == [729.93, 854.204]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 456.78) == [729.93, 854.204]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 750.25) == [1023.4, 1382.45]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 750.25) == [1023.4, 1382.45]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 999.0) == [1272.15, 1830.2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 999.0) == [1272.15, 1830.2]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 499.99) == [773.14, 931.9820000000001]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 499.99) == [773.14, 931.9820000000001]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 60.0) == [333.15, 140.0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 60.0) == [333.15, 140.0]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 23.45) == [296.59999999999997, 74.21000000000001]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 23.45) == [296.59999999999997, 74.21000000000001]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 450.0) == [723.15, 842.0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 450.0) == [723.15, 842.0]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 150.67) == [423.81999999999994, 303.20599999999996]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 150.67) == [423.81999999999994, 303.20599999999996]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 1.0) == [274.15, 33.8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 1.0) == [274.15, 33.8]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 500.01) == [773.16, 932.018]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 500.01) == [773.16, 932.018]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 800.25) == [1073.4, 1472.45]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 800.25) == [1073.4, 1472.45]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 550.89) == [824.04, 1023.602]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 550.89) == [824.04, 1023.602]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 999.99) == [1273.1399999999999, 1831.982]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 999.99) == [1273.1399999999999, 1831.982]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 1.23456) == [274.38455999999996, 34.222208]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 1.23456) == [274.38455999999996, 34.222208]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 0.99) == [274.14, 33.782]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 0.99) == [274.14, 33.782]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 678.9) == [952.05, 1254.02]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 678.9) == [952.05, 1254.02]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 300.12) == [573.27, 572.216]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 300.12) == [573.27, 572.216]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 0.01) == [273.15999999999997, 32.018]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 0.01) == [273.15999999999997, 32.018]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 777.77) == [1050.92, 1431.986]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 777.77) == [1050.92, 1431.986]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 89.67) == [362.82, 193.406]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 89.67) == [362.82, 193.406]: {e}')
    
    total += 1
    try:
        result = candidate(celsius = 150.0) == [423.15, 302.0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(celsius = 150.0) == [423.15, 302.0]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(celsius = 122.11) == [395.26, 251.798]
    assert candidate(celsius = 1000.0) == [1273.15, 1832.0]
    assert candidate(celsius = 0.0) == [273.15, 32.0]
    assert candidate(celsius = 500.0) == [773.15, 932.0]
    assert candidate(celsius = 100.0) == [373.15, 212.0]
    assert candidate(celsius = 500.75) == [773.9, 933.35]
    assert candidate(celsius = 36.5) == [309.65, 97.7]
    assert candidate(celsius = 25.0) == [298.15, 77.0]
    assert candidate(celsius = 273.15) == [546.3, 523.67]
    assert candidate(celsius = 42.876543) == [316.02654299999995, 109.1777774]
    assert candidate(celsius = 12.34) == [285.48999999999995, 54.212]
    assert candidate(celsius = 37.0) == [310.15, 98.60000000000001]
    assert candidate(celsius = 25.55555) == [298.70554999999996, 77.99999]
    assert candidate(celsius = 150.75) == [423.9, 303.35]
    assert candidate(celsius = -0.01) == [273.14, 31.982]
    assert candidate(celsius = 234.56) == [507.71, 454.208]
    assert candidate(celsius = 750.5) == [1023.65, 1382.9]
    assert candidate(celsius = 77.77777) == [350.92777, 171.999986]
    assert candidate(celsius = 456.78) == [729.93, 854.204]
    assert candidate(celsius = 750.25) == [1023.4, 1382.45]
    assert candidate(celsius = 999.0) == [1272.15, 1830.2]
    assert candidate(celsius = 499.99) == [773.14, 931.9820000000001]
    assert candidate(celsius = 60.0) == [333.15, 140.0]
    assert candidate(celsius = 23.45) == [296.59999999999997, 74.21000000000001]
    assert candidate(celsius = 450.0) == [723.15, 842.0]
    assert candidate(celsius = 150.67) == [423.81999999999994, 303.20599999999996]
    assert candidate(celsius = 1.0) == [274.15, 33.8]
    assert candidate(celsius = 500.01) == [773.16, 932.018]
    assert candidate(celsius = 800.25) == [1073.4, 1472.45]
    assert candidate(celsius = 550.89) == [824.04, 1023.602]
    assert candidate(celsius = 999.99) == [1273.1399999999999, 1831.982]
    assert candidate(celsius = 1.23456) == [274.38455999999996, 34.222208]
    assert candidate(celsius = 0.99) == [274.14, 33.782]
    assert candidate(celsius = 678.9) == [952.05, 1254.02]
    assert candidate(celsius = 300.12) == [573.27, 572.216]
    assert candidate(celsius = 0.01) == [273.15999999999997, 32.018]
    assert candidate(celsius = 777.77) == [1050.92, 1431.986]
    assert candidate(celsius = 89.67) == [362.82, 193.406]
    assert candidate(celsius = 150.0) == [423.15, 302.0]


