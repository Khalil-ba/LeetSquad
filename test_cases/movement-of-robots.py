def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4],s = "RLRL",d = 5) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4],s = "RLRL",d = 5) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 1, 4],s = "RLR",d = 4) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 1, 4],s = "RLR",d = 4) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -1, 0, 3, 7],s = "RLLLR",d = 5) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -1, 0, 3, 7],s = "RLLLR",d = 5) == 82: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30],s = "LLL",d = 1) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30],s = "LLL",d = 1) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4],s = "RRRRR",d = 1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4],s = "RRRRR",d = 1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-2, 0, 2],s = "RLL",d = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2, 0, 2],s = "RLL",d = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, -1, 0],s = "LRR",d = 5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, -1, 0],s = "LRR",d = 5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 0],s = "RLR",d = 10) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 0],s = "RLR",d = 10) == 80: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-2, 0, 2],s = "RLL",d = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2, 0, 2],s = "RLL",d = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30],s = "RRR",d = 1) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30],s = "RRR",d = 1) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4],s = "LRRL",d = 5) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4],s = "LRRL",d = 5) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 0],s = "RLR",d = 5) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 0],s = "RLR",d = 5) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0],s = "RL",d = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0],s = "RL",d = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 1, 3],s = "RRL",d = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 1, 3],s = "RRL",d = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0],s = "RL",d = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0],s = "RL",d = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0],s = "RRLL",d = 1) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0],s = "RRLL",d = 1) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1],s = "RRR",d = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1],s = "RRR",d = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20],s = "RLRL",d = 10) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20],s = "RLRL",d = 10) == 220: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, 0, 5, 10],s = "RRRLL",d = 7) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, 0, 5, 10],s = "RRRLL",d = 7) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3],s = "RLRLRL",d = 15) == 314
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3],s = "RLRLRL",d = 15) == 314: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],s = "RLRLRLRLRL",d = 5) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],s = "RLRLRLRLRL",d = 5) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5],s = "RLLRL",d = 3) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5],s = "RLLRL",d = 3) == 76: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, 0, 5, 10, 15, 20, 25, 30],s = "LRRLLRRLL",d = 10) == 680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, 0, 5, 10, 15, 20, 25, 30],s = "LRRLLRRLL",d = 10) == 680: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],s = "RLRLR",d = 2) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],s = "RLRLR",d = 2) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5],s = "RRRRR",d = 3) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5],s = "RRRRR",d = 3) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, 0, 1000000000],s = "RLR",d = 500000000) == 999999979
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, 0, 1000000000],s = "RLR",d = 500000000) == 999999979: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],s = "RRRRRRRRRR",d = 5) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],s = "RRRRRRRRRR",d = 5) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, -800, -600, -400, -200, 200, 400, 600, 800, 1000],s = "RRRRRRRRRR",d = 300) == 38000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, -800, -600, -400, -200, 200, 400, 600, 800, 1000],s = "RRRRRRRRRR",d = 300) == 38000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-20, -10, 0, 10, 20],s = "LRRLL",d = 15) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-20, -10, 0, 10, 20],s = "LRRLL",d = 15) == 220: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, -1, 0, 1, 5, 10],s = "LRRLLRR",d = 7) == 304
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, -1, 0, 1, 5, 10],s = "LRRLLRR",d = 7) == 304: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, -500, 0, 500, 1000],s = "RLRLR",d = 500) == 12000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, -500, 0, 500, 1000],s = "RLRLR",d = 500) == 12000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],s = "RRRRRRRRRRRRRRRRRRRR",d = 2) == 1330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],s = "RRRRRRRRRRRRRRRRRRRR",d = 2) == 1330: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],s = "RRRRR",d = 1) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],s = "RRRRR",d = 1) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, 0, 5, 10],s = "LRLRL",d = 5) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, 0, 5, 10],s = "LRLRL",d = 5) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, 0, 5, 10],s = "RLRLR",d = 7) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, 0, 5, 10],s = "RLRLR",d = 7) == 136: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, 0, 5, 10],s = "RLRRL",d = 3) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, 0, 5, 10],s = "RLRRL",d = 3) == 92: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 0, 5, 10],s = "RLRR",d = 20) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 0, 5, 10],s = "RLRR",d = 20) == 160: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-500, -300, -100, 100, 300, 500],s = "LLRRLR",d = 10) == 7100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-500, -300, -100, 100, 300, 500],s = "LLRRLR",d = 10) == 7100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-2, -1, 0, 1, 2],s = "RLRLR",d = 7) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2, -1, 0, 1, 2],s = "RLRLR",d = 7) == 94: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-20, -10, 0, 10, 20, 30, 40, 50, 60, 70],s = "LRRLLRRLLR",d = 15) == 1840
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-20, -10, 0, 10, 20, 30, 40, 50, 60, 70],s = "LRRLLRRLLR",d = 15) == 1840: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, -25, 0, 25, 50],s = "LRRRL",d = 25) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, -25, 0, 25, 50],s = "LRRRL",d = 25) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9],s = "RRRRRRRRRR",d = 2) == 330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9],s = "RRRRRRRRRR",d = 2) == 330: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, -6, -3, 0, 3, 6, 9],s = "RRRRRRR",d = 4) == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, -6, -3, 0, 3, 6, 9],s = "RRRRRRR",d = 4) == 168: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5],s = "RLRLRLRLRL",d = 3) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5],s = "RLRLRLRLRL",d = 3) == 80: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],s = "RRRRRRRRRR",d = 1) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],s = "RRRRRRRRRR",d = 1) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18],s = "LRLRLRLRLR",d = 5) == 468
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18],s = "LRLRLRLRLR",d = 5) == 468: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-20, -15, -10, -5, 0, 5, 10, 15, 20],s = "RLRLRLRLR",d = 3) == 608
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-20, -15, -10, -5, 0, 5, 10, 15, 20],s = "RLRLRLRLR",d = 3) == 608: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5],s = "RRRRRR",d = 10) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5],s = "RRRRRR",d = 10) == 35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],s = "RRRRRRRRRL",d = 1) == 149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],s = "RRRRRRRRRL",d = 1) == 149: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],s = "LLLLL",d = 50) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],s = "LLLLL",d = 50) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104, 105],s = "LLLLLR",d = 5) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104, 105],s = "LLLLLR",d = 5) == 85: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],s = "RRRRRRRRRR",d = 1) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],s = "RRRRRRRRRR",d = 1) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, -7, -5, -3, -1],s = "RRRRR",d = 6) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, -7, -5, -3, -1],s = "RRRRR",d = 6) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, -20, -10, 0, 10, 20, 50],s = "LRRLLRR",d = 10) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, -20, -10, 0, 10, 20, 50],s = "LRRLLRR",d = 10) == 900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],s = "RLRLRLRLRL",d = 20) == 1110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],s = "RLRLRLRLRL",d = 20) == 1110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],s = "RRRRRRRRRR",d = 10) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],s = "RRRRRRRRRR",d = 10) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 2, 3, 4, 5],s = "LLLLLL",d = 3) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 2, 3, 4, 5],s = "LLLLLL",d = 3) == 74: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],s = "LRLRLRLRLRL",d = 1) == 230
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],s = "LRLRLRLRLRL",d = 1) == 230: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, -30, -10, 10, 30, 50],s = "LLRRLL",d = 15) == 720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, -30, -10, 10, 30, 50],s = "LLRRLL",d = 15) == 720: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -8, -6, -4, -2, 2, 4, 6, 8, 10],s = "LLLLLLLLLL",d = 3) == 380
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -8, -6, -4, -2, 2, 4, 6, 8, 10],s = "LLLLLLLLLL",d = 3) == 380: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-20, -15, -10, -5, 0, 5, 10, 15, 20],s = "RRRRLLLLL",d = 3) == 482
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-20, -15, -10, -5, 0, 5, 10, 15, 20],s = "RRRRLLLLL",d = 3) == 482: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],s = "RRRRRRRRRRLLLLLLLLLL",d = 5) == 1101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],s = "RRRRRRRRRRLLLLLLLLLL",d = 5) == 1101: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -200, -300, -400, -500],s = "LLLLL",d = 100) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -200, -300, -400, -500],s = "LLLLL",d = 100) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4],s = "RLRLRLRL",d = 1) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4],s = "RLRLRLRL",d = 1) == 68: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],s = "LLLLL",d = 2) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],s = "LLLLL",d = 2) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],s = "RLRLRLRLRL",d = 4) == 390
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],s = "RLRLRLRLRL",d = 4) == 390: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-300, -200, -100, 0, 100, 200, 300],s = "LRRLLRR",d = 100) == 6600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-300, -200, -100, 0, 100, 200, 300],s = "LRRLLRR",d = 100) == 6600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],s = "RRRRRRRRRR",d = 2) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],s = "RRRRRRRRRR",d = 2) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, 1000000000],s = "RL",d = 1000000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, 1000000000],s = "RL",d = 1000000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],s = "LLLLL",d = 5) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],s = "LLLLL",d = 5) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, 0, 5, 10],s = "RRLRR",d = 7) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, 0, 5, 10],s = "RRLRR",d = 7) == 126: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, -500, 0, 500, 1000],s = "RLLRL",d = 1000) == 14000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, -500, 0, 500, 1000],s = "RLLRL",d = 1000) == 14000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],s = "LLLLLLLLLL",d = 1) == 330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],s = "LLLLLLLLLL",d = 1) == 330: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 1, 6],s = "RRLLR",d = 7) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 1, 6],s = "RRLLR",d = 7) == 98: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],s = "RRRRRRRRRR",d = 2) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],s = "RRRRRRRRRR",d = 2) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, -6, -3, 0, 3, 6, 9],s = "RLRLRLR",d = 6) == 234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, -6, -3, 0, 3, 6, 9],s = "RLRLRLR",d = 6) == 234: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -3, 1, 4, 7],s = "LRRRL",d = 2) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -3, 1, 4, 7],s = "LRRRL",d = 2) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],s = "RRRRRRRRRRRR",d = 3) == 286
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],s = "RRRRRRRRRRRR",d = 3) == 286: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, 0, 5, 10, 15, 20],s = "RRRLLLL",d = 7) == 146
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, 0, 5, 10, 15, 20],s = "RRRLLLL",d = 7) == 146: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-19, -17, -15, -13, -11, -9, -7, -5, -3, -1],s = "RRRRRRRRRR",d = 2) == 330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-19, -17, -15, -13, -11, -9, -7, -5, -3, -1],s = "RRRRRRRRRR",d = 2) == 330: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-20, -15, -10, -5, 0, 5, 10, 15, 20],s = "RRRRLLLL",d = 20) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-20, -15, -10, -5, 0, 5, 10, 15, 20],s = "RRRRLLLL",d = 20) == 600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-500000000, -250000000, 0, 250000000, 500000000],s = "RLLLR",d = 500000000) == 999999951
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-500000000, -250000000, 0, 250000000, 500000000],s = "RLLLR",d = 500000000) == 999999951: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, 0, 1000000000],s = "RL",d = 500000000) == 999999986
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, 0, 1000000000],s = "RL",d = 500000000) == 999999986: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 10, 20, 30, 40],s = "LLLLL",d = 5) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 10, 20, 30, 40],s = "LLLLL",d = 5) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],s = "LRRLLRRLL",d = 10) == 531
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],s = "LRRLLRRLL",d = 10) == 531: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-500, -300, -100, 100, 300, 500],s = "RLLRLR",d = 200) == 8200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-500, -300, -100, 100, 300, 500],s = "RLLRLR",d = 200) == 8200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, 1000000000],s = "LR",d = 500000000) == 999999986
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, 1000000000],s = "LR",d = 500000000) == 999999986: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],s = "RLLLLRLLLL",d = 5) == 406
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],s = "RLLLLRLLLL",d = 5) == 406: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-500, -400, -300, -200, -100],s = "RRRRR",d = 100) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-500, -400, -300, -200, -100],s = "RRRRR",d = 100) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20],s = "RRRR",d = 5) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20],s = "RRRR",d = 5) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -50, 0, 50, 100, 150, 200],s = "RLLRLLR",d = 150) == 4900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -50, 0, 50, 100, 150, 200],s = "RLLRLLR",d = 150) == 4900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, -6, -3, 0, 3, 6, 9],s = "LRRLRL",d = 15) == 396
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, -6, -3, 0, 3, 6, 9],s = "LRRLRL",d = 15) == 396: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9],s = "LRLRLRLRLR",d = 10) == 710
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9],s = "LRLRLRLRLR",d = 10) == 710: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -2, 2, -3, 3],s = "RLRLRL",d = 5) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -2, 2, -3, 3],s = "RLRLRL",d = 5) == 62: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],s = "LLLLL",d = 10) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],s = "LLLLL",d = 10) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, 1000000000],s = "LR",d = 1000000000) == 999999979
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, 1000000000],s = "LR",d = 1000000000) == 999999979: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-20, -15, -10, -5, 0, 5, 10, 15, 20],s = "LRRRLRRRL",d = 7) == 652
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-20, -15, -10, -5, 0, 5, 10, 15, 20],s = "LRRRLRRRL",d = 7) == 652: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45],s = "LRRLL",d = 10) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45],s = "LRRLL",d = 10) == 180: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, -20, -10, 0, 10, 20, 50],s = "LRLRLRL",d = 30) == 1140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, -20, -10, 0, 10, 20, 50],s = "LRLRLRL",d = 30) == 1140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-20, -10, 0, 10, 20],s = "LRLLR",d = 3) == 212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-20, -10, 0, 10, 20],s = "LRLLR",d = 3) == 212: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, 0, 5, 10, 15],s = "RLRLRL",d = 1) == 169
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, 0, 5, 10, 15],s = "RLRLRL",d = 1) == 169: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],s = "RRRRR",d = 50) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],s = "RRRRR",d = 50) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600],s = "LLLLLR",d = 150) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600],s = "LLLLLR",d = 150) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-500, -400, -300, -200, -100],s = "RRRRR",d = 15) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-500, -400, -300, -200, -100],s = "RRRRR",d = 15) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -2, -1, 0, 1, 2, 3],s = "LLRLRLR",d = 1) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -2, -1, 0, 1, 2, 3],s = "LLRLRLR",d = 1) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, 0, 1000000000],s = "RLR",d = 1000000000) == 999999965
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, 0, 1000000000],s = "RLR",d = 1000000000) == 999999965: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000, 0, 1000000],s = "RLR",d = 1000000) == 6000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000, 0, 1000000],s = "RLR",d = 1000000) == 6000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [250, 500, 750, 1000, 1250],s = "LLLLL",d = 250) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [250, 500, 750, 1000, 1250],s = "LLLLL",d = 250) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],s = "LLLLLLLLLL",d = 500) == 16500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],s = "LLLLLLLLLL",d = 500) == 16500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-25, -15, -5, 5, 15, 25],s = "RLRRRL",d = 10) == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-25, -15, -5, 5, 15, 25],s = "RLRRRL",d = 10) == 350: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [-1, 2, -3, 4],s = "RLRL",d = 5) == 24
    assert candidate(nums = [-5, 1, 4],s = "RLR",d = 4) == 22
    assert candidate(nums = [-5, -1, 0, 3, 7],s = "RLLLR",d = 5) == 82
    assert candidate(nums = [-10, -20, -30],s = "LLL",d = 1) == 40
    assert candidate(nums = [0, 1, 2, 3, 4],s = "RRRRR",d = 1) == 20
    assert candidate(nums = [-2, 0, 2],s = "RLL",d = 3) == 8
    assert candidate(nums = [2, -1, 0],s = "LRR",d = 5) == 16
    assert candidate(nums = [10, -10, 0],s = "RLR",d = 10) == 80
    assert candidate(nums = [-2, 0, 2],s = "RLL",d = 3) == 8
    assert candidate(nums = [10, 20, 30],s = "RRR",d = 1) == 40
    assert candidate(nums = [-1, 2, -3, 4],s = "LRRL",d = 5) == 42
    assert candidate(nums = [10, -10, 0],s = "RLR",d = 5) == 60
    assert candidate(nums = [1, 0],s = "RL",d = 2) == 5
    assert candidate(nums = [-5, 1, 3],s = "RRL",d = 4) == 12
    assert candidate(nums = [1, 0],s = "RL",d = 2) == 5
    assert candidate(nums = [0, 0, 0, 0],s = "RRLL",d = 1) == 8
    assert candidate(nums = [3, 2, 1],s = "RRR",d = 1) == 4
    assert candidate(nums = [10, -10, 20, -20],s = "RLRL",d = 10) == 220
    assert candidate(nums = [-10, -5, 0, 5, 10],s = "RRRLL",d = 7) == 50
    assert candidate(nums = [1, -1, 2, -2, 3, -3],s = "RLRLRL",d = 15) == 314
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],s = "RLRLRLRLRL",d = 5) == 165
    assert candidate(nums = [-1, 2, -3, 4, -5],s = "RLLRL",d = 3) == 76
    assert candidate(nums = [-10, -5, 0, 5, 10, 15, 20, 25, 30],s = "LRRLLRRLL",d = 10) == 680
    assert candidate(nums = [1, 2, 3, 4, 5],s = "RLRLR",d = 2) == 34
    assert candidate(nums = [0, 1, 2, 3, 4, 5],s = "RRRRR",d = 3) == 26
    assert candidate(nums = [-1000000000, 0, 1000000000],s = "RLR",d = 500000000) == 999999979
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],s = "RRRRRRRRRR",d = 5) == 165
    assert candidate(nums = [-1000, -800, -600, -400, -200, 200, 400, 600, 800, 1000],s = "RRRRRRRRRR",d = 300) == 38000
    assert candidate(nums = [-20, -10, 0, 10, 20],s = "LRRLL",d = 15) == 220
    assert candidate(nums = [-10, -5, -1, 0, 1, 5, 10],s = "LRRLLRR",d = 7) == 304
    assert candidate(nums = [-1000, -500, 0, 500, 1000],s = "RLRLR",d = 500) == 12000
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],s = "RRRRRRRRRRRRRRRRRRRR",d = 2) == 1330
    assert candidate(nums = [100, 200, 300, 400, 500],s = "RRRRR",d = 1) == 2000
    assert candidate(nums = [-10, -5, 0, 5, 10],s = "LRLRL",d = 5) == 120
    assert candidate(nums = [-10, -5, 0, 5, 10],s = "RLRLR",d = 7) == 136
    assert candidate(nums = [-10, -5, 0, 5, 10],s = "RLRRL",d = 3) == 92
    assert candidate(nums = [-5, 0, 5, 10],s = "RLRR",d = 20) == 160
    assert candidate(nums = [-500, -300, -100, 100, 300, 500],s = "LLRRLR",d = 10) == 7100
    assert candidate(nums = [-2, -1, 0, 1, 2],s = "RLRLR",d = 7) == 94
    assert candidate(nums = [-20, -10, 0, 10, 20, 30, 40, 50, 60, 70],s = "LRRLLRRLLR",d = 15) == 1840
    assert candidate(nums = [-50, -25, 0, 25, 50],s = "LRRRL",d = 25) == 550
    assert candidate(nums = [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9],s = "RRRRRRRRRR",d = 2) == 330
    assert candidate(nums = [-9, -6, -3, 0, 3, 6, 9],s = "RRRRRRR",d = 4) == 168
    assert candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5],s = "RLRLRLRLRL",d = 3) == 80
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],s = "RRRRRRRRRR",d = 1) == 165
    assert candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18],s = "LRLRLRLRLR",d = 5) == 468
    assert candidate(nums = [-20, -15, -10, -5, 0, 5, 10, 15, 20],s = "RLRLRLRLR",d = 3) == 608
    assert candidate(nums = [0, 1, 2, 3, 4, 5],s = "RRRRRR",d = 10) == 35
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],s = "RRRRRRRRRL",d = 1) == 149
    assert candidate(nums = [100, 200, 300, 400, 500],s = "LLLLL",d = 50) == 2000
    assert candidate(nums = [100, 101, 102, 103, 104, 105],s = "LLLLLR",d = 5) == 85
    assert candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],s = "RRRRRRRRRR",d = 1) == 210
    assert candidate(nums = [-9, -7, -5, -3, -1],s = "RRRRR",d = 6) == 40
    assert candidate(nums = [-50, -20, -10, 0, 10, 20, 50],s = "LRRLLRR",d = 10) == 900
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],s = "RLRLRLRLRL",d = 20) == 1110
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],s = "RRRRRRRRRR",d = 10) == 165
    assert candidate(nums = [-1, 0, 1, 2, 3, 4, 5],s = "LLLLLL",d = 3) == 74
    assert candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],s = "LRLRLRLRLRL",d = 1) == 230
    assert candidate(nums = [-50, -30, -10, 10, 30, 50],s = "LLRRLL",d = 15) == 720
    assert candidate(nums = [-10, -8, -6, -4, -2, 2, 4, 6, 8, 10],s = "LLLLLLLLLL",d = 3) == 380
    assert candidate(nums = [-20, -15, -10, -5, 0, 5, 10, 15, 20],s = "RRRRLLLLL",d = 3) == 482
    assert candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],s = "RRRRRRRRRRLLLLLLLLLL",d = 5) == 1101
    assert candidate(nums = [-100, -200, -300, -400, -500],s = "LLLLL",d = 100) == 2000
    assert candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4],s = "RLRLRLRL",d = 1) == 68
    assert candidate(nums = [1, 3, 5, 7, 9],s = "LLLLL",d = 2) == 40
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],s = "RLRLRLRLRL",d = 4) == 390
    assert candidate(nums = [-300, -200, -100, 0, 100, 200, 300],s = "LRRLLRR",d = 100) == 6600
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],s = "RRRRRRRRRR",d = 2) == 165
    assert candidate(nums = [-1000000000, 1000000000],s = "RL",d = 1000000000) == 0
    assert candidate(nums = [10, 20, 30, 40, 50],s = "LLLLL",d = 5) == 200
    assert candidate(nums = [-10, -5, 0, 5, 10],s = "RRLRR",d = 7) == 126
    assert candidate(nums = [-1000, -500, 0, 500, 1000],s = "RLLRL",d = 1000) == 14000
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],s = "LLLLLLLLLL",d = 1) == 330
    assert candidate(nums = [5, 3, 8, 1, 6],s = "RRLLR",d = 7) == 98
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],s = "RRRRRRRRRR",d = 2) == 165
    assert candidate(nums = [-9, -6, -3, 0, 3, 6, 9],s = "RLRLRLR",d = 6) == 234
    assert candidate(nums = [-5, -3, 1, 4, 7],s = "LRRRL",d = 2) == 64
    assert candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],s = "RRRRRRRRRRRR",d = 3) == 286
    assert candidate(nums = [-10, -5, 0, 5, 10, 15, 20],s = "RRRLLLL",d = 7) == 146
    assert candidate(nums = [-19, -17, -15, -13, -11, -9, -7, -5, -3, -1],s = "RRRRRRRRRR",d = 2) == 330
    assert candidate(nums = [-20, -15, -10, -5, 0, 5, 10, 15, 20],s = "RRRRLLLL",d = 20) == 600
    assert candidate(nums = [-500000000, -250000000, 0, 250000000, 500000000],s = "RLLLR",d = 500000000) == 999999951
    assert candidate(nums = [-1000000000, 0, 1000000000],s = "RL",d = 500000000) == 999999986
    assert candidate(nums = [0, 10, 20, 30, 40],s = "LLLLL",d = 5) == 200
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],s = "LRRLLRRLL",d = 10) == 531
    assert candidate(nums = [-500, -300, -100, 100, 300, 500],s = "RLLRLR",d = 200) == 8200
    assert candidate(nums = [-1000000000, 1000000000],s = "LR",d = 500000000) == 999999986
    assert candidate(nums = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],s = "RLLLLRLLLL",d = 5) == 406
    assert candidate(nums = [-500, -400, -300, -200, -100],s = "RRRRR",d = 100) == 2000
    assert candidate(nums = [5, 10, 15, 20],s = "RRRR",d = 5) == 50
    assert candidate(nums = [-100, -50, 0, 50, 100, 150, 200],s = "RLLRLLR",d = 150) == 4900
    assert candidate(nums = [-9, -6, -3, 0, 3, 6, 9],s = "LRRLRL",d = 15) == 396
    assert candidate(nums = [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9],s = "LRLRLRLRLR",d = 10) == 710
    assert candidate(nums = [-1, 1, -2, 2, -3, 3],s = "RLRLRL",d = 5) == 62
    assert candidate(nums = [100, 200, 300, 400, 500],s = "LLLLL",d = 10) == 2000
    assert candidate(nums = [-1000000000, 1000000000],s = "LR",d = 1000000000) == 999999979
    assert candidate(nums = [-20, -15, -10, -5, 0, 5, 10, 15, 20],s = "LRRRLRRRL",d = 7) == 652
    assert candidate(nums = [5, 15, 25, 35, 45],s = "LRRLL",d = 10) == 180
    assert candidate(nums = [-50, -20, -10, 0, 10, 20, 50],s = "LRLRLRL",d = 30) == 1140
    assert candidate(nums = [-20, -10, 0, 10, 20],s = "LRLLR",d = 3) == 212
    assert candidate(nums = [-10, -5, 0, 5, 10, 15],s = "RLRLRL",d = 1) == 169
    assert candidate(nums = [100, 200, 300, 400, 500],s = "RRRRR",d = 50) == 2000
    assert candidate(nums = [100, 200, 300, 400, 500, 600],s = "LLLLLR",d = 150) == 5000
    assert candidate(nums = [-500, -400, -300, -200, -100],s = "RRRRR",d = 15) == 2000
    assert candidate(nums = [-3, -2, -1, 0, 1, 2, 3],s = "LLRLRLR",d = 1) == 72
    assert candidate(nums = [-1000000000, 0, 1000000000],s = "RLR",d = 1000000000) == 999999965
    assert candidate(nums = [-1000000, 0, 1000000],s = "RLR",d = 1000000) == 6000000
    assert candidate(nums = [250, 500, 750, 1000, 1250],s = "LLLLL",d = 250) == 5000
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],s = "LLLLLLLLLL",d = 500) == 16500
    assert candidate(nums = [-25, -15, -5, 5, 15, 25],s = "RLRRRL",d = 10) == 350


