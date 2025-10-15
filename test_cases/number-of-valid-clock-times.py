def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(time = "23:?0") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:?0") == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = "23:5?") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:5?") == 10: {e}')
    
    total += 1
    try:
        result = candidate(time = "09:5?") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "09:5?") == 10: {e}')
    
    total += 1
    try:
        result = candidate(time = "23:?9") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:?9") == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:?0") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:?0") == 60: {e}')
    
    total += 1
    try:
        result = candidate(time = "00:??") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "00:??") == 60: {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:?5") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:?5") == 60: {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:0?") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:0?") == 100: {e}')
    
    total += 1
    try:
        result = candidate(time = "?3:59") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?3:59") == 3: {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:2?") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:2?") == 100: {e}')
    
    total += 1
    try:
        result = candidate(time = "09:?9") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "09:?9") == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = "??:??") == 1440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "??:??") == 1440: {e}')
    
    total += 1
    try:
        result = candidate(time = "00:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "00:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(time = "23:59") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:59") == 1: {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:30") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:30") == 10: {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:45") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:45") == 4: {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:5?") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:5?") == 100: {e}')
    
    total += 1
    try:
        result = candidate(time = "12:??") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "12:??") == 60: {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:4?") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:4?") == 40: {e}')
    
    total += 1
    try:
        result = candidate(time = "1??:3?") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1??:3?") == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = "?3:21") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?3:21") == 3: {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:45") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:45") == 10: {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:?1") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:?1") == 60: {e}')
    
    total += 1
    try:
        result = candidate(time = "12:?5") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "12:?5") == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:3?") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:3?") == 100: {e}')
    
    total += 1
    try:
        result = candidate(time = "09:??") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "09:??") == 60: {e}')
    
    total += 1
    try:
        result = candidate(time = "12:?3") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "12:?3") == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = "??:59") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "??:59") == 24: {e}')
    
    total += 1
    try:
        result = candidate(time = "?5:00") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?5:00") == 2: {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:3?") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:3?") == 40: {e}')
    
    total += 1
    try:
        result = candidate(time = "??:45") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "??:45") == 24: {e}')
    
    total += 1
    try:
        result = candidate(time = "?4:??") == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?4:??") == 120: {e}')
    
    total += 1
    try:
        result = candidate(time = "19:?5") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "19:?5") == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:15") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:15") == 4: {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:?3") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:?3") == 24: {e}')
    
    total += 1
    try:
        result = candidate(time = "???:30") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "???:30") == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = "23:?5") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:?5") == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = "23:?7") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:?7") == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = "??:2?") == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "??:2?") == 240: {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:??:") == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:??:") == 600: {e}')
    
    total += 1
    try:
        result = candidate(time = "??:00") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "??:00") == 24: {e}')
    
    total += 1
    try:
        result = candidate(time = "19:?7") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "19:?7") == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:59") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:59") == 4: {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:1?") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:1?") == 40: {e}')
    
    total += 1
    try:
        result = candidate(time = "19:?1") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "19:?1") == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = "22:?8") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "22:?8") == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = "?4:3?") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?4:3?") == 20: {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:?9") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:?9") == 60: {e}')
    
    total += 1
    try:
        result = candidate(time = "?3:?1") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?3:?1") == 18: {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:??") == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:??") == 600: {e}')
    
    total += 1
    try:
        result = candidate(time = "??:3?") == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "??:3?") == 240: {e}')
    
    total += 1
    try:
        result = candidate(time = "??:?1") == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "??:?1") == 144: {e}')
    
    total += 1
    try:
        result = candidate(time = "12:?7") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "12:?7") == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:35") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:35") == 4: {e}')
    
    total += 1
    try:
        result = candidate(time = "0??:59") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0??:59") == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:?0") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:?0") == 24: {e}')
    
    total += 1
    try:
        result = candidate(time = "09:?5") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "09:?5") == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = "???:??") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "???:??") == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = "?0:5?") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?0:5?") == 30: {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:3?") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:3?") == 100: {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:?9") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:?9") == 60: {e}')
    
    total += 1
    try:
        result = candidate(time = "12:?9") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "12:?9") == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = "?3:45") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?3:45") == 3: {e}')
    
    total += 1
    try:
        result = candidate(time = "19:??") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "19:??") == 60: {e}')
    
    total += 1
    try:
        result = candidate(time = "19:?4") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "19:?4") == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = "23:?4") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:?4") == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = "?1:??") == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?1:??") == 180: {e}')
    
    total += 1
    try:
        result = candidate(time = "?3:?0") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?3:?0") == 18: {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:?5") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:?5") == 60: {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:4?") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:4?") == 100: {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:5?") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:5?") == 40: {e}')
    
    total += 1
    try:
        result = candidate(time = "??:10") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "??:10") == 24: {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:?3") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:?3") == 60: {e}')
    
    total += 1
    try:
        result = candidate(time = "19:?0") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "19:?0") == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:?5") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:?5") == 24: {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:40") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:40") == 4: {e}')
    
    total += 1
    try:
        result = candidate(time = "19:?9") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "19:?9") == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:0?") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:0?") == 100: {e}')
    
    total += 1
    try:
        result = candidate(time = "???:00") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "???:00") == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:22") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:22") == 4: {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:5?") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:5?") == 100: {e}')
    
    total += 1
    try:
        result = candidate(time = "1??:0?") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1??:0?") == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:30") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:30") == 10: {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:?4") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:?4") == 24: {e}')
    
    total += 1
    try:
        result = candidate(time = "21:??") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "21:??") == 60: {e}')
    
    total += 1
    try:
        result = candidate(time = "20:?7") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "20:?7") == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = "?4:?3") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?4:?3") == 12: {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:00") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:00") == 4: {e}')
    
    total += 1
    try:
        result = candidate(time = "09:4?") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "09:4?") == 10: {e}')
    
    total += 1
    try:
        result = candidate(time = "?9:??") == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?9:??") == 120: {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:?7") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:?7") == 60: {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:59") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:59") == 10: {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:??") == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:??") == 600: {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:?0") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:?0") == 60: {e}')
    
    total += 1
    try:
        result = candidate(time = "?4:5?") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?4:5?") == 20: {e}')
    
    total += 1
    try:
        result = candidate(time = "?2:??") == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?2:??") == 180: {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:59") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:59") == 10: {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:1?") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:1?") == 100: {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:??:") == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:??:") == 240: {e}')
    
    total += 1
    try:
        result = candidate(time = "1??:??") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1??:??") == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = "?:09") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?:09") == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = "?9:0?") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?9:0?") == 20: {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:?2") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:?2") == 24: {e}')
    
    total += 1
    try:
        result = candidate(time = "?1:?2") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?1:?2") == 18: {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:?9") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:?9") == 24: {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:19") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:19") == 10: {e}')
    
    total += 1
    try:
        result = candidate(time = "??:0?") == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "??:0?") == 240: {e}')
    
    total += 1
    try:
        result = candidate(time = "?4:?9") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?4:?9") == 12: {e}')
    
    total += 1
    try:
        result = candidate(time = "20:??") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "20:??") == 60: {e}')
    
    total += 1
    try:
        result = candidate(time = "??:30") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "??:30") == 24: {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:??:") == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:??:") == 600: {e}')
    
    total += 1
    try:
        result = candidate(time = "?4:2?") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?4:2?") == 20: {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:23") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:23") == 10: {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:2?") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:2?") == 40: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(time = "23:?0") == 6
    assert candidate(time = "23:5?") == 10
    assert candidate(time = "09:5?") == 10
    assert candidate(time = "23:?9") == 6
    assert candidate(time = "1?:?0") == 60
    assert candidate(time = "00:??") == 60
    assert candidate(time = "1?:?5") == 60
    assert candidate(time = "0?:0?") == 100
    assert candidate(time = "?3:59") == 3
    assert candidate(time = "1?:2?") == 100
    assert candidate(time = "09:?9") == 6
    assert candidate(time = "??:??") == 1440
    assert candidate(time = "00:00") == 1
    assert candidate(time = "23:59") == 1
    assert candidate(time = "1?:30") == 10
    assert candidate(time = "2?:45") == 4
    assert candidate(time = "1?:5?") == 100
    assert candidate(time = "12:??") == 60
    assert candidate(time = "2?:4?") == 40
    assert candidate(time = "1??:3?") == 0
    assert candidate(time = "?3:21") == 3
    assert candidate(time = "1?:45") == 10
    assert candidate(time = "1?:?1") == 60
    assert candidate(time = "12:?5") == 6
    assert candidate(time = "1?:3?") == 100
    assert candidate(time = "09:??") == 60
    assert candidate(time = "12:?3") == 6
    assert candidate(time = "??:59") == 24
    assert candidate(time = "?5:00") == 2
    assert candidate(time = "2?:3?") == 40
    assert candidate(time = "??:45") == 24
    assert candidate(time = "?4:??") == 120
    assert candidate(time = "19:?5") == 6
    assert candidate(time = "2?:15") == 4
    assert candidate(time = "2?:?3") == 24
    assert candidate(time = "???:30") == 0
    assert candidate(time = "23:?5") == 6
    assert candidate(time = "23:?7") == 6
    assert candidate(time = "??:2?") == 240
    assert candidate(time = "0?:??:") == 600
    assert candidate(time = "??:00") == 24
    assert candidate(time = "19:?7") == 6
    assert candidate(time = "2?:59") == 4
    assert candidate(time = "2?:1?") == 40
    assert candidate(time = "19:?1") == 6
    assert candidate(time = "22:?8") == 6
    assert candidate(time = "?4:3?") == 20
    assert candidate(time = "0?:?9") == 60
    assert candidate(time = "?3:?1") == 18
    assert candidate(time = "1?:??") == 600
    assert candidate(time = "??:3?") == 240
    assert candidate(time = "??:?1") == 144
    assert candidate(time = "12:?7") == 6
    assert candidate(time = "2?:35") == 4
    assert candidate(time = "0??:59") == 0
    assert candidate(time = "2?:?0") == 24
    assert candidate(time = "09:?5") == 6
    assert candidate(time = "???:??") == 0
    assert candidate(time = "?0:5?") == 30
    assert candidate(time = "0?:3?") == 100
    assert candidate(time = "1?:?9") == 60
    assert candidate(time = "12:?9") == 6
    assert candidate(time = "?3:45") == 3
    assert candidate(time = "19:??") == 60
    assert candidate(time = "19:?4") == 6
    assert candidate(time = "23:?4") == 6
    assert candidate(time = "?1:??") == 180
    assert candidate(time = "?3:?0") == 18
    assert candidate(time = "0?:?5") == 60
    assert candidate(time = "0?:4?") == 100
    assert candidate(time = "2?:5?") == 40
    assert candidate(time = "??:10") == 24
    assert candidate(time = "0?:?3") == 60
    assert candidate(time = "19:?0") == 6
    assert candidate(time = "2?:?5") == 24
    assert candidate(time = "2?:40") == 4
    assert candidate(time = "19:?9") == 6
    assert candidate(time = "1?:0?") == 100
    assert candidate(time = "???:00") == 0
    assert candidate(time = "2?:22") == 4
    assert candidate(time = "0?:5?") == 100
    assert candidate(time = "1??:0?") == 0
    assert candidate(time = "0?:30") == 10
    assert candidate(time = "2?:?4") == 24
    assert candidate(time = "21:??") == 60
    assert candidate(time = "20:?7") == 6
    assert candidate(time = "?4:?3") == 12
    assert candidate(time = "2?:00") == 4
    assert candidate(time = "09:4?") == 10
    assert candidate(time = "?9:??") == 120
    assert candidate(time = "1?:?7") == 60
    assert candidate(time = "0?:59") == 10
    assert candidate(time = "0?:??") == 600
    assert candidate(time = "0?:?0") == 60
    assert candidate(time = "?4:5?") == 20
    assert candidate(time = "?2:??") == 180
    assert candidate(time = "1?:59") == 10
    assert candidate(time = "0?:1?") == 100
    assert candidate(time = "2?:??:") == 240
    assert candidate(time = "1??:??") == 0
    assert candidate(time = "?:09") == 0
    assert candidate(time = "?9:0?") == 20
    assert candidate(time = "2?:?2") == 24
    assert candidate(time = "?1:?2") == 18
    assert candidate(time = "2?:?9") == 24
    assert candidate(time = "0?:19") == 10
    assert candidate(time = "??:0?") == 240
    assert candidate(time = "?4:?9") == 12
    assert candidate(time = "20:??") == 60
    assert candidate(time = "??:30") == 24
    assert candidate(time = "1?:??:") == 600
    assert candidate(time = "?4:2?") == 20
    assert candidate(time = "1?:23") == 10
    assert candidate(time = "2?:2?") == 40


