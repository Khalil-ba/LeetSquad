def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 99: {e}')
    
    total += 1
    try:
        result = candidate(n = 14) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 199: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 199) == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 199) == 198: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 97) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 97) == 96: {e}')
    
    total += 1
    try:
        result = candidate(n = 63) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63) == 62: {e}')
    
    total += 1
    try:
        result = candidate(n = 29) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 45) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45) == 44: {e}')
    
    total += 1
    try:
        result = candidate(n = 135) == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 135) == 134: {e}')
    
    total += 1
    try:
        result = candidate(n = 183) == 182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 183) == 182: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == 48: {e}')
    
    total += 1
    try:
        result = candidate(n = 130) == 129
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 130) == 129: {e}')
    
    total += 1
    try:
        result = candidate(n = 163) == 162
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 163) == 162: {e}')
    
    total += 1
    try:
        result = candidate(n = 111) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111) == 110: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 197) == 196
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 197) == 196: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 49: {e}')
    
    total += 1
    try:
        result = candidate(n = 157) == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 157) == 156: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 123) == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123) == 122: {e}')
    
    total += 1
    try:
        result = candidate(n = 59) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 59) == 58: {e}')
    
    total += 1
    try:
        result = candidate(n = 87) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 87) == 86: {e}')
    
    total += 1
    try:
        result = candidate(n = 173) == 172
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 173) == 172: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == 98: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 177) == 176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 177) == 176: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == 63: {e}')
    
    total += 1
    try:
        result = candidate(n = 33) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 143) == 142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 143) == 142: {e}')
    
    total += 1
    try:
        result = candidate(n = 98) == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98) == 97: {e}')
    
    total += 1
    try:
        result = candidate(n = 73) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 73) == 72: {e}')
    
    total += 1
    try:
        result = candidate(n = 133) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 133) == 132: {e}')
    
    total += 1
    try:
        result = candidate(n = 175) == 174
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 175) == 174: {e}')
    
    total += 1
    try:
        result = candidate(n = 128) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 128) == 127: {e}')
    
    total += 1
    try:
        result = candidate(n = 101) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101) == 100: {e}')
    
    total += 1
    try:
        result = candidate(n = 181) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 181) == 180: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 131) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131) == 130: {e}')
    
    total += 1
    try:
        result = candidate(n = 27) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27) == 26: {e}')
    
    total += 1
    try:
        result = candidate(n = 169) == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 169) == 168: {e}')
    
    total += 1
    try:
        result = candidate(n = 32) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 149) == 148
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 149) == 148: {e}')
    
    total += 1
    try:
        result = candidate(n = 127) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 127) == 126: {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == 80: {e}')
    
    total += 1
    try:
        result = candidate(n = 150) == 149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150) == 149: {e}')
    
    total += 1
    try:
        result = candidate(n = 151) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 151) == 150: {e}')
    
    total += 1
    try:
        result = candidate(n = 198) == 197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 198) == 197: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 189) == 188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 189) == 188: {e}')
    
    total += 1
    try:
        result = candidate(n = 85) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 85) == 84: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 24: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 2
    assert candidate(n = 100) == 99
    assert candidate(n = 14) == 13
    assert candidate(n = 200) == 199
    assert candidate(n = 17) == 16
    assert candidate(n = 2) == 1
    assert candidate(n = 199) == 198
    assert candidate(n = 1) == 0
    assert candidate(n = 7) == 6
    assert candidate(n = 13) == 12
    assert candidate(n = 97) == 96
    assert candidate(n = 63) == 62
    assert candidate(n = 29) == 28
    assert candidate(n = 45) == 44
    assert candidate(n = 135) == 134
    assert candidate(n = 183) == 182
    assert candidate(n = 49) == 48
    assert candidate(n = 130) == 129
    assert candidate(n = 163) == 162
    assert candidate(n = 111) == 110
    assert candidate(n = 10) == 9
    assert candidate(n = 197) == 196
    assert candidate(n = 50) == 49
    assert candidate(n = 157) == 156
    assert candidate(n = 5) == 4
    assert candidate(n = 123) == 122
    assert candidate(n = 59) == 58
    assert candidate(n = 87) == 86
    assert candidate(n = 173) == 172
    assert candidate(n = 4) == 3
    assert candidate(n = 99) == 98
    assert candidate(n = 16) == 15
    assert candidate(n = 177) == 176
    assert candidate(n = 64) == 63
    assert candidate(n = 33) == 32
    assert candidate(n = 143) == 142
    assert candidate(n = 98) == 97
    assert candidate(n = 73) == 72
    assert candidate(n = 133) == 132
    assert candidate(n = 175) == 174
    assert candidate(n = 128) == 127
    assert candidate(n = 101) == 100
    assert candidate(n = 181) == 180
    assert candidate(n = 8) == 7
    assert candidate(n = 131) == 130
    assert candidate(n = 27) == 26
    assert candidate(n = 169) == 168
    assert candidate(n = 32) == 31
    assert candidate(n = 149) == 148
    assert candidate(n = 127) == 126
    assert candidate(n = 81) == 80
    assert candidate(n = 150) == 149
    assert candidate(n = 151) == 150
    assert candidate(n = 198) == 197
    assert candidate(n = 11) == 10
    assert candidate(n = 15) == 14
    assert candidate(n = 189) == 188
    assert candidate(n = 85) == 84
    assert candidate(n = 31) == 30
    assert candidate(n = 25) == 24


