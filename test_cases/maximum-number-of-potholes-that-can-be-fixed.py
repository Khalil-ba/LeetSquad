def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(road = "xxxx",budget = 6) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxx",budget = 6) == 4: {e}')
    
    total += 1
    try:
        result = candidate(road = "..",budget = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "..",budget = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.xxx...x",budget = 14) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.xxx...x",budget = 14) == 6: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxx.xxxx",budget = 12) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxx.xxxx",budget = 12) == 8: {e}')
    
    total += 1
    try:
        result = candidate(road = "xx.xx.xx.xx",budget = 15) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xx.xx.xx.xx",budget = 15) == 8: {e}')
    
    total += 1
    try:
        result = candidate(road = "x",budget = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x",budget = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x",budget = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x",budget = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxx.xxx.xx",budget = 15) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxx.xxx.xx",budget = 15) == 8: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x.x.x.x",budget = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x.x.x.x",budget = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.xxxxx.x",budget = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.xxxxx.x",budget = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x",budget = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x",budget = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x",budget = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x",budget = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxx",budget = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxx",budget = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x",budget = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x",budget = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxx",budget = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxx",budget = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(road = "x...x...x...x",budget = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x...x...x...x",budget = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxx...xxx",budget = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxx...xxx",budget = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x",budget = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x",budget = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxx",budget = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxx",budget = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(road = "...",budget = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "...",budget = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(road = "...",budget = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "...",budget = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x",budget = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x",budget = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(road = ".x.x.x.x.",budget = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = ".x.x.x.x.",budget = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(road = "...",budget = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "...",budget = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxx",budget = 20) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxx",budget = 20) == 9: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.xxxxx.x",budget = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.xxxxx.x",budget = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxx",budget = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxx",budget = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(road = "........",budget = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "........",budget = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(road = "..xxxxx",budget = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "..xxxxx",budget = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxx",budget = 100) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxx",budget = 100) == 9: {e}')
    
    total += 1
    try:
        result = candidate(road = "...xxx...xxxx...xxxxx...xxxxxx",budget = 35) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "...xxx...xxxx...xxxxx...xxxxxx",budget = 35) == 18: {e}')
    
    total += 1
    try:
        result = candidate(road = "............",budget = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "............",budget = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxxxxxxxxxxxxxxxx",budget = 50) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxxxxxxxxxxxxxxxx",budget = 50) == 23: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 50) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 50) == 21: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 40) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 40) == 20: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x.x.x.x",budget = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x.x.x.x",budget = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 30) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 30) == 15: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx",budget = 50) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx",budget = 50) == 28: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxx...xxxxxxxxx...xxxxxxxxx",budget = 30) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxx...xxxxxxxxx...xxxxxxxxx",budget = 30) == 27: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxx...xxxxx",budget = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxx...xxxxx",budget = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxx",budget = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxx",budget = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxxxx",budget = 15) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxxxx",budget = 15) == 11: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxxx.xxxxxxxxx.xxxxx",budget = 40) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxxx.xxxxxxxxx.xxxxx",budget = 40) == 24: {e}')
    
    total += 1
    try:
        result = candidate(road = "xx..xx..xx",budget = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xx..xx..xx",budget = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x.x.x.x",budget = 50) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x.x.x.x",budget = 50) == 10: {e}')
    
    total += 1
    try:
        result = candidate(road = "...xxxxxxx....xxxxx...",budget = 20) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "...xxxxxxx....xxxxx...",budget = 20) == 12: {e}')
    
    total += 1
    try:
        result = candidate(road = "xx.xx.xx.xx.xx.xx.xx",budget = 20) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xx.xx.xx.xx.xx.xx.xx",budget = 20) == 13: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxx...xxxxxxxxx",budget = 30) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxx...xxxxxxxxx",budget = 30) == 18: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x.x.x.x.x",budget = 30) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x.x.x.x.x",budget = 30) == 11: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.xxxx.xxxxxx.xxxxxxxx",budget = 30) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.xxxx.xxxxxx.xxxxxxxx",budget = 30) == 19: {e}')
    
    total += 1
    try:
        result = candidate(road = "....xxxxx.....xxxxx.....xxxxx....",budget = 40) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "....xxxxx.....xxxxx.....xxxxx....",budget = 40) == 15: {e}')
    
    total += 1
    try:
        result = candidate(road = "xx..xx...xx....xx.....xx......xx.......xx........xx.........xx..........xx",budget = 50) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xx..xx...xx....xx.....xx......xx.......xx........xx.........xx..........xx",budget = 50) == 20: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxxxxxxxxxxxxx",budget = 30) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxxxxxxxxxxxxx",budget = 30) == 20: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 40) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 40) == 20: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxx.xxxx.xxxx",budget = 25) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxx.xxxx.xxxx",budget = 25) == 12: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 30) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 30) == 15: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x",budget = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x",budget = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxx.xxxxx.xxxxx",budget = 20) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxx.xxxxx.xxxxx",budget = 20) == 15: {e}')
    
    total += 1
    try:
        result = candidate(road = "...........................",budget = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "...........................",budget = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 40) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 40) == 17: {e}')
    
    total += 1
    try:
        result = candidate(road = "...x...x...x...x...x...",budget = 12) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "...x...x...x...x...x...",budget = 12) == 5: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x...x...x...x...x...x...x...x...x...x",budget = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x...x...x...x...x...x...x...x...x...x",budget = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x...x.x.x.x...x.x.x",budget = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x...x.x.x.x...x.x.x",budget = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x.x.x.x",budget = 25) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x.x.x.x",budget = 25) == 10: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.xxxxx.xxxxx.x",budget = 25) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.xxxxx.xxxxx.x",budget = 25) == 12: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxx.xxxxx.xxxxx.xxxxx",budget = 25) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxx.xxxxx.xxxxx.xxxxx",budget = 25) == 19: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x...x.x...x.x...x",budget = 12) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x...x.x...x.x...x",budget = 12) == 6: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxxxxxxxx",budget = 100) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxxxxxxxx",budget = 100) == 15: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxxxxxx........x....x.......xxxxxxx",budget = 30) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxxxxxx........x....x.......xxxxxxx",budget = 30) == 22: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxxxx...xxxxxxxxxxx...xxxxxxxxxxx",budget = 70) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxxxx...xxxxxxxxxxx...xxxxxxxxxxx",budget = 70) == 33: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxxx",budget = 15) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxxx",budget = 15) == 10: {e}')
    
    total += 1
    try:
        result = candidate(road = "........x........x........x",budget = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "........x........x........x",budget = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.xxxxx.x",budget = 12) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.xxxxx.x",budget = 12) == 7: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxx.xxxxx.xxxxx.xxxxx.xxxxx",budget = 80) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxx.xxxxx.xxxxx.xxxxx.xxxxx",budget = 80) == 25: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxx.xxxx.xxxx.xxxx.xxxx",budget = 25) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxx.xxxx.xxxx.xxxx.xxxx",budget = 25) == 20: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxxxxxxxx",budget = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxxxxxxxx",budget = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x",budget = 12) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x",budget = 12) == 6: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxx..xxx..xx",budget = 15) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxx..xxx..xx",budget = 15) == 9: {e}')
    
    total += 1
    try:
        result = candidate(road = "x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x",budget = 50) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x",budget = 50) == 22: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 25) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 25) == 12: {e}')
    
    total += 1
    try:
        result = candidate(road = "x",budget = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x",budget = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(road = "x......x......x......x......x......x......x",budget = 35) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x......x......x......x......x......x......x",budget = 35) == 7: {e}')
    
    total += 1
    try:
        result = candidate(road = "....",budget = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "....",budget = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(road = "...xxx.xxxx...xx.xx.xxxxx",budget = 25) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "...xxx.xxxx...xx.xx.xxxxx",budget = 25) == 16: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxx...xxxx...xxxx",budget = 25) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxx...xxxx...xxxx",budget = 25) == 12: {e}')
    
    total += 1
    try:
        result = candidate(road = "x..x...x...x..x",budget = 12) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x..x...x...x..x",budget = 12) == 5: {e}')
    
    total += 1
    try:
        result = candidate(road = "...xxxxxx...",budget = 8) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "...xxxxxx...",budget = 8) == 6: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 100) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 100) == 19: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x...x..x...x...x..x...x",budget = 30) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x...x..x...x...x..x...x",budget = 30) == 8: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxx.xxxxx.xxxxx.xxxxx.xxxxx",budget = 30) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxx.xxxxx.xxxxx.xxxxx.xxxxx",budget = 30) == 25: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x",budget = 21) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x",budget = 21) == 7: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.xxxx.xxxx.xxxxx",budget = 20) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.xxxx.xxxx.xxxxx",budget = 20) == 14: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxxxxxxxx",budget = 20) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxxxxxxxx",budget = 20) == 15: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x.x.x",budget = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x.x.x",budget = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x",budget = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x",budget = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(road = "...xxxxx...",budget = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "...xxxxx...",budget = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(road = "...",budget = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "...",budget = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(road = "x..xx..xx..x",budget = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x..xx..xx..x",budget = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxx.xxxxx.xxxxx",budget = 40) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxx.xxxxx.xxxxx",budget = 40) == 16: {e}')
    
    total += 1
    try:
        result = candidate(road = "x....x...x....x...x",budget = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x....x...x....x...x",budget = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.xxxxx.xxxxx.xxxxx.xxxxx",budget = 30) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.xxxxx.xxxxx.xxxxx.xxxxx",budget = 30) == 21: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 60) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 60) == 30: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.xxxxxx.xxxxxx.xxxxxx",budget = 60) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.xxxxxx.xxxxxx.xxxxxx",budget = 60) == 19: {e}')
    
    total += 1
    try:
        result = candidate(road = ".x.x.x.x.x.x.x.x.x.",budget = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = ".x.x.x.x.x.x.x.x.x.",budget = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(road = "x...x...x...x...x",budget = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x...x...x...x...x",budget = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x.x.x",budget = 18) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x.x.x",budget = 18) == 9: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",budget = 100) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",budget = 100) == 29: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxx.xxxxx",budget = 15) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxx.xxxxx",budget = 15) == 9: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 30) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 30) == 15: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxxxxxxxx",budget = 25) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxxxxxxxx",budget = 25) == 15: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxx....xxx....xx",budget = 20) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxx....xxx....xx",budget = 20) == 9: {e}')
    
    total += 1
    try:
        result = candidate(road = "........x....x........x....x........",budget = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "........x....x........x....x........",budget = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxx...xxx.xx.x.x",budget = 20) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxx...xxx.xx.x.x",budget = 20) == 14: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxx",budget = 9) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxx",budget = 9) == 8: {e}')
    
    total += 1
    try:
        result = candidate(road = "............",budget = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "............",budget = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(road = "...x...x...x...x...x...x",budget = 20) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "...x...x...x...x...x...x",budget = 20) == 6: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxx...xxx",budget = 11) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxx...xxx",budget = 11) == 7: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxxxxxxxxxxxxxx",budget = 25) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxxxxxxxxxxxxxx",budget = 25) == 19: {e}')
    
    total += 1
    try:
        result = candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 60) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 60) == 28: {e}')
    
    total += 1
    try:
        result = candidate(road = "................x............x............x............x............x............x............",budget = 20) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "................x............x............x............x............x............x............",budget = 20) == 6: {e}')
    
    total += 1
    try:
        result = candidate(road = "...x....x....x....x....x",budget = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "...x....x....x....x....x",budget = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(road = ".............x.............",budget = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = ".............x.............",budget = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(road = "xxxxxxx...xxxxx....xxx",budget = 25) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xxxxxxx...xxxxx....xxx",budget = 25) == 15: {e}')
    
    total += 1
    try:
        result = candidate(road = "x..xx..x",budget = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x..xx..x",budget = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(road = "xx..xx..xx..xx..xx..xx..xx..xx",budget = 20) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "xx..xx..xx..xx..xx..xx..xx..xx",budget = 20) == 13: {e}')
    
    total += 1
    try:
        result = candidate(road = "x..x..x..x..x..x",budget = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = "x..x..x..x..x..x",budget = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(road = ".x.x.x.x.x.x.x.x.x.x",budget = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(road = ".x.x.x.x.x.x.x.x.x.x",budget = 15) == 7: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(road = "xxxx",budget = 6) == 4
    assert candidate(road = "..",budget = 5) == 0
    assert candidate(road = "x.x.xxx...x",budget = 14) == 6
    assert candidate(road = "xxxx.xxxx",budget = 12) == 8
    assert candidate(road = "xx.xx.xx.xx",budget = 15) == 8
    assert candidate(road = "x",budget = 2) == 1
    assert candidate(road = "x.x.x.x",budget = 6) == 3
    assert candidate(road = "xxx.xxx.xx",budget = 15) == 8
    assert candidate(road = "x.x.x.x.x.x.x.x.x.x",budget = 20) == 10
    assert candidate(road = "x.xxxxx.x",budget = 15) == 7
    assert candidate(road = "x.x.x.x.x",budget = 15) == 5
    assert candidate(road = "x.x.x.x",budget = 8) == 4
    assert candidate(road = "xxxxx",budget = 10) == 5
    assert candidate(road = "x.x.x",budget = 5) == 2
    assert candidate(road = "xxxxxxxxx",budget = 10) == 9
    assert candidate(road = "x...x...x...x",budget = 10) == 4
    assert candidate(road = "xxx...xxx",budget = 10) == 6
    assert candidate(road = "x.x.x.x.x",budget = 6) == 3
    assert candidate(road = "xxxxx",budget = 6) == 5
    assert candidate(road = "...",budget = 10) == 0
    assert candidate(road = "...",budget = 0) == 0
    assert candidate(road = "x.x.x.x.x",budget = 7) == 3
    assert candidate(road = ".x.x.x.x.",budget = 8) == 4
    assert candidate(road = "...",budget = 1) == 0
    assert candidate(road = "xxxxxxxxx",budget = 20) == 9
    assert candidate(road = "x.xxxxx.x",budget = 10) == 7
    assert candidate(road = "xxxx",budget = 10) == 4
    assert candidate(road = "........",budget = 10) == 0
    assert candidate(road = "..xxxxx",budget = 4) == 3
    assert candidate(road = "xxxxxxxxx",budget = 100) == 9
    assert candidate(road = "...xxx...xxxx...xxxxx...xxxxxx",budget = 35) == 18
    assert candidate(road = "............",budget = 100) == 0
    assert candidate(road = "xxxxxxxxxxxxxxxxxxxxxxx",budget = 50) == 23
    assert candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 50) == 21
    assert candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 40) == 20
    assert candidate(road = "x.x.x.x.x.x.x.x.x.x",budget = 10) == 5
    assert candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 30) == 15
    assert candidate(road = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx",budget = 50) == 28
    assert candidate(road = "xxxxxxxxx...xxxxxxxxx...xxxxxxxxx",budget = 30) == 27
    assert candidate(road = "xxxxx...xxxxx",budget = 20) == 10
    assert candidate(road = "xxxxxx",budget = 10) == 6
    assert candidate(road = "xxxxxxxxxxx",budget = 15) == 11
    assert candidate(road = "xxxxxxxxxx.xxxxxxxxx.xxxxx",budget = 40) == 24
    assert candidate(road = "xx..xx..xx",budget = 10) == 6
    assert candidate(road = "x.x.x.x.x.x.x.x.x.x",budget = 50) == 10
    assert candidate(road = "...xxxxxxx....xxxxx...",budget = 20) == 12
    assert candidate(road = "xx.xx.xx.xx.xx.xx.xx",budget = 20) == 13
    assert candidate(road = "xxxxxxxxx...xxxxxxxxx",budget = 30) == 18
    assert candidate(road = "x.x.x.x.x.x.x.x.x.x.x",budget = 30) == 11
    assert candidate(road = "x.xxxx.xxxxxx.xxxxxxxx",budget = 30) == 19
    assert candidate(road = "....xxxxx.....xxxxx.....xxxxx....",budget = 40) == 15
    assert candidate(road = "xx..xx...xx....xx.....xx......xx.......xx........xx.........xx..........xx",budget = 50) == 20
    assert candidate(road = "xxxxxxxxxxxxxxxxxxxx",budget = 30) == 20
    assert candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 40) == 20
    assert candidate(road = "xxxx.xxxx.xxxx",budget = 25) == 12
    assert candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 30) == 15
    assert candidate(road = "x.x.x.x.x.x",budget = 15) == 6
    assert candidate(road = "xxxxx.xxxxx.xxxxx",budget = 20) == 15
    assert candidate(road = "...........................",budget = 50) == 0
    assert candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 40) == 17
    assert candidate(road = "...x...x...x...x...x...",budget = 12) == 5
    assert candidate(road = "x.x...x...x...x...x...x...x...x...x...x",budget = 20) == 10
    assert candidate(road = "x.x...x.x.x.x...x.x.x",budget = 15) == 7
    assert candidate(road = "x.x.x.x.x.x.x.x.x.x",budget = 25) == 10
    assert candidate(road = "x.xxxxx.xxxxx.x",budget = 25) == 12
    assert candidate(road = "xxxx.xxxxx.xxxxx.xxxxx",budget = 25) == 19
    assert candidate(road = "x.x...x.x...x.x...x",budget = 12) == 6
    assert candidate(road = "xxxxxxxxxxxxxxx",budget = 100) == 15
    assert candidate(road = "xxxxxxxxxxxxx........x....x.......xxxxxxx",budget = 30) == 22
    assert candidate(road = "xxxxxxxxxxx...xxxxxxxxxxx...xxxxxxxxxxx",budget = 70) == 33
    assert candidate(road = "xxxxxxxxxx",budget = 15) == 10
    assert candidate(road = "........x........x........x",budget = 3) == 1
    assert candidate(road = "x.xxxxx.x",budget = 12) == 7
    assert candidate(road = "xxxxx.xxxxx.xxxxx.xxxxx.xxxxx",budget = 80) == 25
    assert candidate(road = "xxxx.xxxx.xxxx.xxxx.xxxx",budget = 25) == 20
    assert candidate(road = "xxxxxxxxxxxxxxx",budget = 10) == 9
    assert candidate(road = "x.x.x.x.x.x",budget = 12) == 6
    assert candidate(road = "xxxx..xxx..xx",budget = 15) == 9
    assert candidate(road = "x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x...x",budget = 50) == 22
    assert candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 25) == 12
    assert candidate(road = "x",budget = 1) == 0
    assert candidate(road = "x......x......x......x......x......x......x",budget = 35) == 7
    assert candidate(road = "....",budget = 1) == 0
    assert candidate(road = "...xxx.xxxx...xx.xx.xxxxx",budget = 25) == 16
    assert candidate(road = "xxxx...xxxx...xxxx",budget = 25) == 12
    assert candidate(road = "x..x...x...x..x",budget = 12) == 5
    assert candidate(road = "...xxxxxx...",budget = 8) == 6
    assert candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 100) == 19
    assert candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 20) == 10
    assert candidate(road = "x.x...x..x...x...x..x...x",budget = 30) == 8
    assert candidate(road = "xxxxx.xxxxx.xxxxx.xxxxx.xxxxx",budget = 30) == 25
    assert candidate(road = "x.x.x.x.x.x.x",budget = 21) == 7
    assert candidate(road = "x.xxxx.xxxx.xxxxx",budget = 20) == 14
    assert candidate(road = "xxxxxxxxxxxxxxx",budget = 20) == 15
    assert candidate(road = "x.x.x.x.x.x.x.x.x",budget = 10) == 5
    assert candidate(road = "x.x.x.x.x",budget = 10) == 5
    assert candidate(road = "...xxxxx...",budget = 10) == 5
    assert candidate(road = "...",budget = 3) == 0
    assert candidate(road = "x..xx..xx..x",budget = 15) == 6
    assert candidate(road = "xxxxxx.xxxxx.xxxxx",budget = 40) == 16
    assert candidate(road = "x....x...x....x...x",budget = 15) == 5
    assert candidate(road = "x.xxxxx.xxxxx.xxxxx.xxxxx",budget = 30) == 21
    assert candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 60) == 30
    assert candidate(road = "x.xxxxxx.xxxxxx.xxxxxx",budget = 60) == 19
    assert candidate(road = ".x.x.x.x.x.x.x.x.x.",budget = 10) == 5
    assert candidate(road = "x...x...x...x...x",budget = 15) == 5
    assert candidate(road = "x.x.x.x.x.x.x.x.x",budget = 18) == 9
    assert candidate(road = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",budget = 100) == 29
    assert candidate(road = "xxxx.xxxxx",budget = 15) == 9
    assert candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 30) == 15
    assert candidate(road = "xxxxxxxxxxxxxxx",budget = 25) == 15
    assert candidate(road = "xxxx....xxx....xx",budget = 20) == 9
    assert candidate(road = "........x....x........x....x........",budget = 10) == 4
    assert candidate(road = "xxxxxxx...xxx.xx.x.x",budget = 20) == 14
    assert candidate(road = "xxxxxxxxx",budget = 9) == 8
    assert candidate(road = "............",budget = 5) == 0
    assert candidate(road = "...x...x...x...x...x...x",budget = 20) == 6
    assert candidate(road = "xxxx...xxx",budget = 11) == 7
    assert candidate(road = "xxxxxxxxxxxxxxxxxxx",budget = 25) == 19
    assert candidate(road = "x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x",budget = 60) == 28
    assert candidate(road = "................x............x............x............x............x............x............",budget = 20) == 6
    assert candidate(road = "...x....x....x....x....x",budget = 15) == 5
    assert candidate(road = ".............x.............",budget = 5) == 1
    assert candidate(road = "xxxxxxx...xxxxx....xxx",budget = 25) == 15
    assert candidate(road = "x..xx..x",budget = 8) == 4
    assert candidate(road = "xx..xx..xx..xx..xx..xx..xx..xx",budget = 20) == 13
    assert candidate(road = "x..x..x..x..x..x",budget = 15) == 6
    assert candidate(road = ".x.x.x.x.x.x.x.x.x.x",budget = 15) == 7


