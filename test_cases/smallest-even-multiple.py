def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 100: {e}')
    
    total += 1
    try:
        result = candidate(n = 33) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33) == 66: {e}')
    
    total += 1
    try:
        result = candidate(n = 75) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75) == 150: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 150) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150) == 150: {e}')
    
    total += 1
    try:
        result = candidate(n = 45) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45) == 90: {e}')
    
    total += 1
    try:
        result = candidate(n = 119) == 238
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 119) == 238: {e}')
    
    total += 1
    try:
        result = candidate(n = 53) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 53) == 106: {e}')
    
    total += 1
    try:
        result = candidate(n = 43) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 43) == 86: {e}')
    
    total += 1
    try:
        result = candidate(n = 103) == 206
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 103) == 206: {e}')
    
    total += 1
    try:
        result = candidate(n = 145) == 290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 145) == 290: {e}')
    
    total += 1
    try:
        result = candidate(n = 37) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37) == 74: {e}')
    
    total += 1
    try:
        result = candidate(n = 23) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23) == 46: {e}')
    
    total += 1
    try:
        result = candidate(n = 73) == 146
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 73) == 146: {e}')
    
    total += 1
    try:
        result = candidate(n = 133) == 266
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 133) == 266: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 147) == 294
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 147) == 294: {e}')
    
    total += 1
    try:
        result = candidate(n = 131) == 262
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131) == 262: {e}')
    
    total += 1
    try:
        result = candidate(n = 27) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27) == 54: {e}')
    
    total += 1
    try:
        result = candidate(n = 35) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35) == 70: {e}')
    
    total += 1
    try:
        result = candidate(n = 77) == 154
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 77) == 154: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 142) == 142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 142) == 142: {e}')
    
    total += 1
    try:
        result = candidate(n = 55) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55) == 110: {e}')
    
    total += 1
    try:
        result = candidate(n = 65) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65) == 130: {e}')
    
    total += 1
    try:
        result = candidate(n = 97) == 194
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 97) == 194: {e}')
    
    total += 1
    try:
        result = candidate(n = 88) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 88) == 88: {e}')
    
    total += 1
    try:
        result = candidate(n = 29) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29) == 58: {e}')
    
    total += 1
    try:
        result = candidate(n = 135) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 135) == 270: {e}')
    
    total += 1
    try:
        result = candidate(n = 144) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 144) == 144: {e}')
    
    total += 1
    try:
        result = candidate(n = 107) == 214
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 107) == 214: {e}')
    
    total += 1
    try:
        result = candidate(n = 21) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21) == 42: {e}')
    
    total += 1
    try:
        result = candidate(n = 115) == 230
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 115) == 230: {e}')
    
    total += 1
    try:
        result = candidate(n = 87) == 174
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 87) == 174: {e}')
    
    total += 1
    try:
        result = candidate(n = 137) == 274
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 137) == 274: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == 34: {e}')
    
    total += 1
    try:
        result = candidate(n = 42) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 42) == 42: {e}')
    
    total += 1
    try:
        result = candidate(n = 101) == 202
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101) == 202: {e}')
    
    total += 1
    try:
        result = candidate(n = 89) == 178
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 89) == 178: {e}')
    
    total += 1
    try:
        result = candidate(n = 112) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 112) == 112: {e}')
    
    total += 1
    try:
        result = candidate(n = 71) == 142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 71) == 142: {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == 162
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == 162: {e}')
    
    total += 1
    try:
        result = candidate(n = 41) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 41) == 82: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 83) == 166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 83) == 166: {e}')
    
    total += 1
    try:
        result = candidate(n = 121) == 242
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 121) == 242: {e}')
    
    total += 1
    try:
        result = candidate(n = 105) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 105) == 210: {e}')
    
    total += 1
    try:
        result = candidate(n = 79) == 158
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 79) == 158: {e}')
    
    total += 1
    try:
        result = candidate(n = 84) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 84) == 84: {e}')
    
    total += 1
    try:
        result = candidate(n = 63) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63) == 126: {e}')
    
    total += 1
    try:
        result = candidate(n = 61) == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 61) == 122: {e}')
    
    total += 1
    try:
        result = candidate(n = 130) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 130) == 130: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == 98: {e}')
    
    total += 1
    try:
        result = candidate(n = 47) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 47) == 94: {e}')
    
    total += 1
    try:
        result = candidate(n = 113) == 226
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 113) == 226: {e}')
    
    total += 1
    try:
        result = candidate(n = 93) == 186
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 93) == 186: {e}')
    
    total += 1
    try:
        result = candidate(n = 57) == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 57) == 114: {e}')
    
    total += 1
    try:
        result = candidate(n = 111) == 222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111) == 222: {e}')
    
    total += 1
    try:
        result = candidate(n = 123) == 246
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123) == 246: {e}')
    
    total += 1
    try:
        result = candidate(n = 95) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 95) == 190: {e}')
    
    total += 1
    try:
        result = candidate(n = 141) == 282
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 141) == 282: {e}')
    
    total += 1
    try:
        result = candidate(n = 51) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 51) == 102: {e}')
    
    total += 1
    try:
        result = candidate(n = 127) == 254
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 127) == 254: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == 26: {e}')
    
    total += 1
    try:
        result = candidate(n = 69) == 138
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 69) == 138: {e}')
    
    total += 1
    try:
        result = candidate(n = 125) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125) == 250: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 117) == 234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 117) == 234: {e}')
    
    total += 1
    try:
        result = candidate(n = 59) == 118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 59) == 118: {e}')
    
    total += 1
    try:
        result = candidate(n = 67) == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67) == 134: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == 198: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == 64: {e}')
    
    total += 1
    try:
        result = candidate(n = 143) == 286
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 143) == 286: {e}')
    
    total += 1
    try:
        result = candidate(n = 128) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 128) == 128: {e}')
    
    total += 1
    try:
        result = candidate(n = 129) == 258
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 129) == 258: {e}')
    
    total += 1
    try:
        result = candidate(n = 140) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 140) == 140: {e}')
    
    total += 1
    try:
        result = candidate(n = 149) == 298
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 149) == 298: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == 38: {e}')
    
    total += 1
    try:
        result = candidate(n = 39) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 39) == 78: {e}')
    
    total += 1
    try:
        result = candidate(n = 91) == 182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 91) == 182: {e}')
    
    total += 1
    try:
        result = candidate(n = 139) == 278
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 139) == 278: {e}')
    
    total += 1
    try:
        result = candidate(n = 85) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 85) == 170: {e}')
    
    total += 1
    try:
        result = candidate(n = 109) == 218
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 109) == 218: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == 62: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 50: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 6
    assert candidate(n = 100) == 100
    assert candidate(n = 33) == 66
    assert candidate(n = 75) == 150
    assert candidate(n = 6) == 6
    assert candidate(n = 2) == 2
    assert candidate(n = 1) == 2
    assert candidate(n = 7) == 14
    assert candidate(n = 5) == 10
    assert candidate(n = 150) == 150
    assert candidate(n = 45) == 90
    assert candidate(n = 119) == 238
    assert candidate(n = 53) == 106
    assert candidate(n = 43) == 86
    assert candidate(n = 103) == 206
    assert candidate(n = 145) == 290
    assert candidate(n = 37) == 74
    assert candidate(n = 23) == 46
    assert candidate(n = 73) == 146
    assert candidate(n = 133) == 266
    assert candidate(n = 8) == 8
    assert candidate(n = 147) == 294
    assert candidate(n = 131) == 262
    assert candidate(n = 27) == 54
    assert candidate(n = 35) == 70
    assert candidate(n = 77) == 154
    assert candidate(n = 11) == 22
    assert candidate(n = 142) == 142
    assert candidate(n = 55) == 110
    assert candidate(n = 65) == 130
    assert candidate(n = 97) == 194
    assert candidate(n = 88) == 88
    assert candidate(n = 29) == 58
    assert candidate(n = 135) == 270
    assert candidate(n = 144) == 144
    assert candidate(n = 107) == 214
    assert candidate(n = 21) == 42
    assert candidate(n = 115) == 230
    assert candidate(n = 87) == 174
    assert candidate(n = 137) == 274
    assert candidate(n = 17) == 34
    assert candidate(n = 42) == 42
    assert candidate(n = 101) == 202
    assert candidate(n = 89) == 178
    assert candidate(n = 112) == 112
    assert candidate(n = 71) == 142
    assert candidate(n = 81) == 162
    assert candidate(n = 41) == 82
    assert candidate(n = 9) == 18
    assert candidate(n = 83) == 166
    assert candidate(n = 121) == 242
    assert candidate(n = 105) == 210
    assert candidate(n = 79) == 158
    assert candidate(n = 84) == 84
    assert candidate(n = 63) == 126
    assert candidate(n = 61) == 122
    assert candidate(n = 130) == 130
    assert candidate(n = 49) == 98
    assert candidate(n = 47) == 94
    assert candidate(n = 113) == 226
    assert candidate(n = 93) == 186
    assert candidate(n = 57) == 114
    assert candidate(n = 111) == 222
    assert candidate(n = 123) == 246
    assert candidate(n = 95) == 190
    assert candidate(n = 141) == 282
    assert candidate(n = 51) == 102
    assert candidate(n = 127) == 254
    assert candidate(n = 15) == 30
    assert candidate(n = 13) == 26
    assert candidate(n = 69) == 138
    assert candidate(n = 125) == 250
    assert candidate(n = 12) == 12
    assert candidate(n = 117) == 234
    assert candidate(n = 59) == 118
    assert candidate(n = 67) == 134
    assert candidate(n = 99) == 198
    assert candidate(n = 64) == 64
    assert candidate(n = 143) == 286
    assert candidate(n = 128) == 128
    assert candidate(n = 129) == 258
    assert candidate(n = 140) == 140
    assert candidate(n = 149) == 298
    assert candidate(n = 19) == 38
    assert candidate(n = 39) == 78
    assert candidate(n = 91) == 182
    assert candidate(n = 139) == 278
    assert candidate(n = 85) == 170
    assert candidate(n = 109) == 218
    assert candidate(n = 31) == 62
    assert candidate(n = 25) == 50


