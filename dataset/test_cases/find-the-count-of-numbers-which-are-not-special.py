def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(l = 100,r = 200) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 100,r = 200) == 99: {e}')
    
    total += 1
    try:
        result = candidate(l = 5,r = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 5,r = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(l = 20,r = 50) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 20,r = 50) == 29: {e}')
    
    total += 1
    try:
        result = candidate(l = 1,r = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 1,r = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(l = 100,r = 150) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 100,r = 150) == 50: {e}')
    
    total += 1
    try:
        result = candidate(l = 4,r = 16) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 4,r = 16) == 11: {e}')
    
    total += 1
    try:
        result = candidate(l = 10,r = 20) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 10,r = 20) == 11: {e}')
    
    total += 1
    try:
        result = candidate(l = 1000,r = 10000) == 8987
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 1000,r = 10000) == 8987: {e}')
    
    total += 1
    try:
        result = candidate(l = 25,r = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 25,r = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(l = 100000,r = 200000) == 99980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 100000,r = 200000) == 99980: {e}')
    
    total += 1
    try:
        result = candidate(l = 250000,r = 250100) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 250000,r = 250100) == 101: {e}')
    
    total += 1
    try:
        result = candidate(l = 1000000,r = 1000010) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 1000000,r = 1000010) == 11: {e}')
    
    total += 1
    try:
        result = candidate(l = 999999999,r = 1000000000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 999999999,r = 1000000000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(l = 1,r = 100000000) == 99998771
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 1,r = 100000000) == 99998771: {e}')
    
    total += 1
    try:
        result = candidate(l = 100000,r = 150000) == 49990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 100000,r = 150000) == 49990: {e}')
    
    total += 1
    try:
        result = candidate(l = 1000000000,r = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 1000000000,r = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(l = 500000,r = 501000) == 1001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 500000,r = 501000) == 1001: {e}')
    
    total += 1
    try:
        result = candidate(l = 3,r = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 3,r = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(l = 1,r = 1000000) == 999832
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 1,r = 1000000) == 999832: {e}')
    
    total += 1
    try:
        result = candidate(l = 5000,r = 6000) == 999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 5000,r = 6000) == 999: {e}')
    
    total += 1
    try:
        result = candidate(l = 10000,r = 11000) == 999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 10000,r = 11000) == 999: {e}')
    
    total += 1
    try:
        result = candidate(l = 2,r = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 2,r = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(l = 5000,r = 7000) == 1997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 5000,r = 7000) == 1997: {e}')
    
    total += 1
    try:
        result = candidate(l = 1000000,r = 1500000) == 499969
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 1000000,r = 1500000) == 499969: {e}')
    
    total += 1
    try:
        result = candidate(l = 8,r = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 8,r = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(l = 1000000,r = 10000000) == 8999723
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 1000000,r = 10000000) == 8999723: {e}')
    
    total += 1
    try:
        result = candidate(l = 300000000,r = 400000000) == 99999729
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 300000000,r = 400000000) == 99999729: {e}')
    
    total += 1
    try:
        result = candidate(l = 500000,r = 1000000) == 499959
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 500000,r = 1000000) == 499959: {e}')
    
    total += 1
    try:
        result = candidate(l = 4,r = 1000000) == 999829
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 4,r = 1000000) == 999829: {e}')
    
    total += 1
    try:
        result = candidate(l = 10000000,r = 10001000) == 1001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 10000000,r = 10001000) == 1001: {e}')
    
    total += 1
    try:
        result = candidate(l = 25,r = 50) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 25,r = 50) == 24: {e}')
    
    total += 1
    try:
        result = candidate(l = 1,r = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 1,r = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(l = 999999,r = 1000000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 999999,r = 1000000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(l = 999900,r = 1000000) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 999900,r = 1000000) == 101: {e}')
    
    total += 1
    try:
        result = candidate(l = 50,r = 100) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 50,r = 100) == 51: {e}')
    
    total += 1
    try:
        result = candidate(l = 8,r = 100) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 8,r = 100) == 90: {e}')
    
    total += 1
    try:
        result = candidate(l = 16,r = 25) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 16,r = 25) == 9: {e}')
    
    total += 1
    try:
        result = candidate(l = 1000000,r = 1001000) == 1001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 1000000,r = 1001000) == 1001: {e}')
    
    total += 1
    try:
        result = candidate(l = 16,r = 256) == 237
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 16,r = 256) == 237: {e}')
    
    total += 1
    try:
        result = candidate(l = 999,r = 1001) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 999,r = 1001) == 3: {e}')
    
    total += 1
    try:
        result = candidate(l = 123456,r = 789012) == 665473
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 123456,r = 789012) == 665473: {e}')
    
    total += 1
    try:
        result = candidate(l = 10000,r = 10100) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 10000,r = 10100) == 101: {e}')
    
    total += 1
    try:
        result = candidate(l = 999999950,r = 1000000000) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 999999950,r = 1000000000) == 51: {e}')
    
    total += 1
    try:
        result = candidate(l = 50000,r = 60000) == 9996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 50000,r = 60000) == 9996: {e}')
    
    total += 1
    try:
        result = candidate(l = 123456,r = 123486) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 123456,r = 123486) == 31: {e}')
    
    total += 1
    try:
        result = candidate(l = 49,r = 50) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 49,r = 50) == 1: {e}')
    
    total += 1
    try:
        result = candidate(l = 97,r = 101) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 97,r = 101) == 5: {e}')
    
    total += 1
    try:
        result = candidate(l = 10000,r = 100000) == 89961
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 10000,r = 100000) == 89961: {e}')
    
    total += 1
    try:
        result = candidate(l = 3000000,r = 3000100) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 3000000,r = 3000100) == 101: {e}')
    
    total += 1
    try:
        result = candidate(l = 500,r = 500) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 500,r = 500) == 1: {e}')
    
    total += 1
    try:
        result = candidate(l = 100000000,r = 100010000) == 10001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 100000000,r = 100010000) == 10001: {e}')
    
    total += 1
    try:
        result = candidate(l = 1234567,r = 8765432) == 7530626
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 1234567,r = 8765432) == 7530626: {e}')
    
    total += 1
    try:
        result = candidate(l = 150,r = 250) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 150,r = 250) == 100: {e}')
    
    total += 1
    try:
        result = candidate(l = 2,r = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 2,r = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(l = 8000000,r = 8000100) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 8000000,r = 8000100) == 101: {e}')
    
    total += 1
    try:
        result = candidate(l = 25,r = 36) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 25,r = 36) == 11: {e}')
    
    total += 1
    try:
        result = candidate(l = 987654,r = 987674) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 987654,r = 987674) == 21: {e}')
    
    total += 1
    try:
        result = candidate(l = 500,r = 1500) == 997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 500,r = 1500) == 997: {e}')
    
    total += 1
    try:
        result = candidate(l = 5000,r = 50000) == 44972
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 5000,r = 50000) == 44972: {e}')
    
    total += 1
    try:
        result = candidate(l = 2000000,r = 2000050) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 2000000,r = 2000050) == 51: {e}')
    
    total += 1
    try:
        result = candidate(l = 500000,r = 500010) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 500000,r = 500010) == 11: {e}')
    
    total += 1
    try:
        result = candidate(l = 1,r = 100) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 1,r = 100) == 96: {e}')
    
    total += 1
    try:
        result = candidate(l = 500000,r = 600000) == 99990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 500000,r = 600000) == 99990: {e}')
    
    total += 1
    try:
        result = candidate(l = 1,r = 1000) == 989
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 1,r = 1000) == 989: {e}')
    
    total += 1
    try:
        result = candidate(l = 1000,r = 2000) == 998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 1000,r = 2000) == 998: {e}')
    
    total += 1
    try:
        result = candidate(l = 14,r = 28) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 14,r = 28) == 14: {e}')
    
    total += 1
    try:
        result = candidate(l = 100000000,r = 1000000000) == 899997829
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 100000000,r = 1000000000) == 899997829: {e}')
    
    total += 1
    try:
        result = candidate(l = 1000000,r = 1000100) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 1000000,r = 1000100) == 101: {e}')
    
    total += 1
    try:
        result = candidate(l = 500000000,r = 600000000) == 99999786
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 500000000,r = 600000000) == 99999786: {e}')
    
    total += 1
    try:
        result = candidate(l = 101,r = 200) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 101,r = 200) == 98: {e}')
    
    total += 1
    try:
        result = candidate(l = 100,r = 1000) == 894
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 100,r = 1000) == 894: {e}')
    
    total += 1
    try:
        result = candidate(l = 81,r = 81) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 81,r = 81) == 1: {e}')
    
    total += 1
    try:
        result = candidate(l = 49,r = 64) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 49,r = 64) == 15: {e}')
    
    total += 1
    try:
        result = candidate(l = 8,r = 25) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 8,r = 25) == 16: {e}')
    
    total += 1
    try:
        result = candidate(l = 5000,r = 7500) == 2497
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 5000,r = 7500) == 2497: {e}')
    
    total += 1
    try:
        result = candidate(l = 25,r = 49) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 25,r = 49) == 23: {e}')
    
    total += 1
    try:
        result = candidate(l = 1000,r = 1500) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(l = 1000,r = 1500) == 500: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(l = 100,r = 200) == 99
    assert candidate(l = 5,r = 7) == 3
    assert candidate(l = 20,r = 50) == 29
    assert candidate(l = 1,r = 10) == 8
    assert candidate(l = 100,r = 150) == 50
    assert candidate(l = 4,r = 16) == 11
    assert candidate(l = 10,r = 20) == 11
    assert candidate(l = 1000,r = 10000) == 8987
    assert candidate(l = 25,r = 25) == 0
    assert candidate(l = 100000,r = 200000) == 99980
    assert candidate(l = 250000,r = 250100) == 101
    assert candidate(l = 1000000,r = 1000010) == 11
    assert candidate(l = 999999999,r = 1000000000) == 2
    assert candidate(l = 1,r = 100000000) == 99998771
    assert candidate(l = 100000,r = 150000) == 49990
    assert candidate(l = 1000000000,r = 1000000000) == 1
    assert candidate(l = 500000,r = 501000) == 1001
    assert candidate(l = 3,r = 3) == 1
    assert candidate(l = 1,r = 1000000) == 999832
    assert candidate(l = 5000,r = 6000) == 999
    assert candidate(l = 10000,r = 11000) == 999
    assert candidate(l = 2,r = 2) == 1
    assert candidate(l = 5000,r = 7000) == 1997
    assert candidate(l = 1000000,r = 1500000) == 499969
    assert candidate(l = 8,r = 8) == 1
    assert candidate(l = 1000000,r = 10000000) == 8999723
    assert candidate(l = 300000000,r = 400000000) == 99999729
    assert candidate(l = 500000,r = 1000000) == 499959
    assert candidate(l = 4,r = 1000000) == 999829
    assert candidate(l = 10000000,r = 10001000) == 1001
    assert candidate(l = 25,r = 50) == 24
    assert candidate(l = 1,r = 3) == 3
    assert candidate(l = 999999,r = 1000000) == 2
    assert candidate(l = 999900,r = 1000000) == 101
    assert candidate(l = 50,r = 100) == 51
    assert candidate(l = 8,r = 100) == 90
    assert candidate(l = 16,r = 25) == 9
    assert candidate(l = 1000000,r = 1001000) == 1001
    assert candidate(l = 16,r = 256) == 237
    assert candidate(l = 999,r = 1001) == 3
    assert candidate(l = 123456,r = 789012) == 665473
    assert candidate(l = 10000,r = 10100) == 101
    assert candidate(l = 999999950,r = 1000000000) == 51
    assert candidate(l = 50000,r = 60000) == 9996
    assert candidate(l = 123456,r = 123486) == 31
    assert candidate(l = 49,r = 50) == 1
    assert candidate(l = 97,r = 101) == 5
    assert candidate(l = 10000,r = 100000) == 89961
    assert candidate(l = 3000000,r = 3000100) == 101
    assert candidate(l = 500,r = 500) == 1
    assert candidate(l = 100000000,r = 100010000) == 10001
    assert candidate(l = 1234567,r = 8765432) == 7530626
    assert candidate(l = 150,r = 250) == 100
    assert candidate(l = 2,r = 3) == 2
    assert candidate(l = 8000000,r = 8000100) == 101
    assert candidate(l = 25,r = 36) == 11
    assert candidate(l = 987654,r = 987674) == 21
    assert candidate(l = 500,r = 1500) == 997
    assert candidate(l = 5000,r = 50000) == 44972
    assert candidate(l = 2000000,r = 2000050) == 51
    assert candidate(l = 500000,r = 500010) == 11
    assert candidate(l = 1,r = 100) == 96
    assert candidate(l = 500000,r = 600000) == 99990
    assert candidate(l = 1,r = 1000) == 989
    assert candidate(l = 1000,r = 2000) == 998
    assert candidate(l = 14,r = 28) == 14
    assert candidate(l = 100000000,r = 1000000000) == 899997829
    assert candidate(l = 1000000,r = 1000100) == 101
    assert candidate(l = 500000000,r = 600000000) == 99999786
    assert candidate(l = 101,r = 200) == 98
    assert candidate(l = 100,r = 1000) == 894
    assert candidate(l = 81,r = 81) == 1
    assert candidate(l = 49,r = 64) == 15
    assert candidate(l = 8,r = 25) == 16
    assert candidate(l = 5000,r = 7500) == 2497
    assert candidate(l = 25,r = 49) == 23
    assert candidate(l = 1000,r = 1500) == 500


