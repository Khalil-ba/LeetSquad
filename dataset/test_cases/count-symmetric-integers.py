def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(low = 10,high = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10,high = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 9999) == 624
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 9999) == 624: {e}')
    
    total += 1
    try:
        result = candidate(low = 500,high = 1500) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 500,high = 1500) == 20: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000,high = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000,high = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 500,high = 550) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 500,high = 550) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 100) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 100) == 9: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 10000) == 624
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 10000) == 624: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000,high = 10000) == 615
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000,high = 10000) == 615: {e}')
    
    total += 1
    try:
        result = candidate(low = 1200,high = 1230) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1200,high = 1230) == 4: {e}')
    
    total += 1
    try:
        result = candidate(low = 10,high = 1000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10,high = 1000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(low = 9999,high = 10000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 9999,high = 10000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 2500,high = 2600) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 2500,high = 2600) == 8: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000,high = 9999) == 615
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000,high = 9999) == 615: {e}')
    
    total += 1
    try:
        result = candidate(low = 2500,high = 3500) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 2500,high = 3500) == 74: {e}')
    
    total += 1
    try:
        result = candidate(low = 7777,high = 8888) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 7777,high = 8888) == 70: {e}')
    
    total += 1
    try:
        result = candidate(low = 7000,high = 7100) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 7000,high = 7100) == 8: {e}')
    
    total += 1
    try:
        result = candidate(low = 1001,high = 9990) == 614
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1001,high = 9990) == 614: {e}')
    
    total += 1
    try:
        result = candidate(low = 1234,high = 4321) == 216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1234,high = 4321) == 216: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 2000,high = 2999) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 2000,high = 2999) == 69: {e}')
    
    total += 1
    try:
        result = candidate(low = 5000,high = 5500) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5000,high = 5500) == 40: {e}')
    
    total += 1
    try:
        result = candidate(low = 1234,high = 5678) == 326
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1234,high = 5678) == 326: {e}')
    
    total += 1
    try:
        result = candidate(low = 7500,high = 7600) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 7500,high = 7600) == 7: {e}')
    
    total += 1
    try:
        result = candidate(low = 8000,high = 8500) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 8000,high = 8500) == 43: {e}')
    
    total += 1
    try:
        result = candidate(low = 3000,high = 3100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 3000,high = 3100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(low = 3000,high = 3999) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 3000,high = 3999) == 73: {e}')
    
    total += 1
    try:
        result = candidate(low = 999,high = 9999) == 615
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 999,high = 9999) == 615: {e}')
    
    total += 1
    try:
        result = candidate(low = 5000,high = 5050) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5000,high = 5050) == 6: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000,high = 2000) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000,high = 2000) == 63: {e}')
    
    total += 1
    try:
        result = candidate(low = 1111,high = 2222) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1111,high = 2222) == 70: {e}')
    
    total += 1
    try:
        result = candidate(low = 10001,high = 20001) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10001,high = 20001) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 8000,high = 8100) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 8000,high = 8100) == 9: {e}')
    
    total += 1
    try:
        result = candidate(low = 5000,high = 6000) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5000,high = 6000) == 75: {e}')
    
    total += 1
    try:
        result = candidate(low = 2000,high = 3000) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 2000,high = 3000) == 69: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000,high = 1010) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000,high = 1010) == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = 9000,high = 9999) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 9000,high = 9999) == 55: {e}')
    
    total += 1
    try:
        result = candidate(low = 3000,high = 3300) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 3000,high = 3300) == 15: {e}')
    
    total += 1
    try:
        result = candidate(low = 6000,high = 6100) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 6000,high = 6100) == 7: {e}')
    
    total += 1
    try:
        result = candidate(low = 8888,high = 8888) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 8888,high = 8888) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 9876,high = 9885) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 9876,high = 9885) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 999,high = 1001) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 999,high = 1001) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 1111,high = 9999) == 612
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1111,high = 9999) == 612: {e}')
    
    total += 1
    try:
        result = candidate(low = 12345,high = 67890) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 12345,high = 67890) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 9000,high = 9100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 9000,high = 9100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(low = 9900,high = 10100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 9900,high = 10100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000,high = 1100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000,high = 1100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = 8888,high = 9999) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 8888,high = 9999) == 59: {e}')
    
    total += 1
    try:
        result = candidate(low = 1001,high = 1020) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1001,high = 1020) == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = 100100,high = 100200) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100100,high = 100200) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 3000,high = 7000) == 296
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 3000,high = 7000) == 296: {e}')
    
    total += 1
    try:
        result = candidate(low = 1234,high = 8765) == 542
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1234,high = 8765) == 542: {e}')
    
    total += 1
    try:
        result = candidate(low = 999,high = 10001) == 615
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 999,high = 10001) == 615: {e}')
    
    total += 1
    try:
        result = candidate(low = 9876,high = 9876) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 9876,high = 9876) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 100,high = 10000) == 615
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100,high = 10000) == 615: {e}')
    
    total += 1
    try:
        result = candidate(low = 1100,high = 1400) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1100,high = 1400) == 12: {e}')
    
    total += 1
    try:
        result = candidate(low = 1001,high = 1010) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1001,high = 1010) == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = 5000,high = 5100) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5000,high = 5100) == 6: {e}')
    
    total += 1
    try:
        result = candidate(low = 7800,high = 7900) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 7800,high = 7900) == 4: {e}')
    
    total += 1
    try:
        result = candidate(low = 4999,high = 5001) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 4999,high = 5001) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 1001,high = 9999) == 615
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1001,high = 9999) == 615: {e}')
    
    total += 1
    try:
        result = candidate(low = 1001,high = 1099) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1001,high = 1099) == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = 8000,high = 8999) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 8000,high = 8999) == 63: {e}')
    
    total += 1
    try:
        result = candidate(low = 5000,high = 9999) == 335
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5000,high = 9999) == 335: {e}')
    
    total += 1
    try:
        result = candidate(low = 9000,high = 10000) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 9000,high = 10000) == 55: {e}')
    
    total += 1
    try:
        result = candidate(low = 5000,high = 9000) == 280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5000,high = 9000) == 280: {e}')
    
    total += 1
    try:
        result = candidate(low = 5678,high = 8765) == 216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5678,high = 8765) == 216: {e}')
    
    total += 1
    try:
        result = candidate(low = 2000,high = 8000) == 434
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 2000,high = 8000) == 434: {e}')
    
    total += 1
    try:
        result = candidate(low = 10000,high = 10000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10000,high = 10000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 10010,high = 10020) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10010,high = 10020) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 5000,high = 50000) == 335
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5000,high = 50000) == 335: {e}')
    
    total += 1
    try:
        result = candidate(low = 9900,high = 10000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 9900,high = 10000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 4500,high = 4600) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 4500,high = 4600) == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(low = 10,high = 20) == 1
    assert candidate(low = 1,high = 9999) == 624
    assert candidate(low = 500,high = 1500) == 20
    assert candidate(low = 1000,high = 1000) == 0
    assert candidate(low = 500,high = 550) == 0
    assert candidate(low = 1,high = 100) == 9
    assert candidate(low = 1,high = 10000) == 624
    assert candidate(low = 1000,high = 10000) == 615
    assert candidate(low = 1200,high = 1230) == 4
    assert candidate(low = 10,high = 1000) == 9
    assert candidate(low = 9999,high = 10000) == 1
    assert candidate(low = 2500,high = 2600) == 8
    assert candidate(low = 1000,high = 9999) == 615
    assert candidate(low = 2500,high = 3500) == 74
    assert candidate(low = 7777,high = 8888) == 70
    assert candidate(low = 7000,high = 7100) == 8
    assert candidate(low = 1001,high = 9990) == 614
    assert candidate(low = 1234,high = 4321) == 216
    assert candidate(low = 1,high = 10) == 0
    assert candidate(low = 2000,high = 2999) == 69
    assert candidate(low = 5000,high = 5500) == 40
    assert candidate(low = 1234,high = 5678) == 326
    assert candidate(low = 7500,high = 7600) == 7
    assert candidate(low = 8000,high = 8500) == 43
    assert candidate(low = 3000,high = 3100) == 4
    assert candidate(low = 3000,high = 3999) == 73
    assert candidate(low = 999,high = 9999) == 615
    assert candidate(low = 5000,high = 5050) == 6
    assert candidate(low = 1000,high = 2000) == 63
    assert candidate(low = 1111,high = 2222) == 70
    assert candidate(low = 10001,high = 20001) == 0
    assert candidate(low = 8000,high = 8100) == 9
    assert candidate(low = 5000,high = 6000) == 75
    assert candidate(low = 2000,high = 3000) == 69
    assert candidate(low = 1000,high = 1010) == 2
    assert candidate(low = 9000,high = 9999) == 55
    assert candidate(low = 3000,high = 3300) == 15
    assert candidate(low = 6000,high = 6100) == 7
    assert candidate(low = 8888,high = 8888) == 1
    assert candidate(low = 9876,high = 9885) == 0
    assert candidate(low = 999,high = 1001) == 1
    assert candidate(low = 1111,high = 9999) == 612
    assert candidate(low = 12345,high = 67890) == 0
    assert candidate(low = 9000,high = 9100) == 10
    assert candidate(low = 9900,high = 10100) == 1
    assert candidate(low = 1000,high = 1100) == 2
    assert candidate(low = 8888,high = 9999) == 59
    assert candidate(low = 1001,high = 1020) == 2
    assert candidate(low = 100100,high = 100200) == 1
    assert candidate(low = 3000,high = 7000) == 296
    assert candidate(low = 1234,high = 8765) == 542
    assert candidate(low = 999,high = 10001) == 615
    assert candidate(low = 9876,high = 9876) == 0
    assert candidate(low = 100,high = 10000) == 615
    assert candidate(low = 1100,high = 1400) == 12
    assert candidate(low = 1001,high = 1010) == 2
    assert candidate(low = 5000,high = 5100) == 6
    assert candidate(low = 7800,high = 7900) == 4
    assert candidate(low = 4999,high = 5001) == 0
    assert candidate(low = 1001,high = 9999) == 615
    assert candidate(low = 1001,high = 1099) == 2
    assert candidate(low = 8000,high = 8999) == 63
    assert candidate(low = 5000,high = 9999) == 335
    assert candidate(low = 9000,high = 10000) == 55
    assert candidate(low = 5000,high = 9000) == 280
    assert candidate(low = 5678,high = 8765) == 216
    assert candidate(low = 2000,high = 8000) == 434
    assert candidate(low = 10000,high = 10000) == 0
    assert candidate(low = 10010,high = 10020) == 0
    assert candidate(low = 5000,high = 50000) == 335
    assert candidate(low = 9900,high = 10000) == 1
    assert candidate(low = 4500,high = 4600) == 10


