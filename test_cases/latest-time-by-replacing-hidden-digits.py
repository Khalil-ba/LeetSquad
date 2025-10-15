def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(time = "?3:?0") == "23:50"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?3:?0") == "23:50": {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:22") == "19:22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:22") == "19:22": {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:??") == "19:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:??") == "19:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:59") == "09:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:59") == "09:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "23:?9") == "23:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:?9") == "23:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "00:?0") == "00:50"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "00:?0") == "00:50": {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:5?") == "23:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:5?") == "23:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:?0") == "23:50"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:?0") == "23:50": {e}')
    
    total += 1
    try:
        result = candidate(time = "?:?:??") == "2:?:9?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?:?:??") == "2:?:9?": {e}')
    
    total += 1
    try:
        result = candidate(time = "00:??") == "00:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "00:??") == "00:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:?5") == "19:55"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:?5") == "19:55": {e}')
    
    total += 1
    try:
        result = candidate(time = "?9:5?") == "19:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?9:5?") == "19:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "??:??") == "23:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "??:??") == "23:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "12:3?") == "12:39"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "12:3?") == "12:39": {e}')
    
    total += 1
    try:
        result = candidate(time = "??:00") == "23:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "??:00") == "23:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:3?") == "09:39"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:3?") == "09:39": {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:?9") == "19:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:?9") == "19:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "00:?5") == "00:55"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "00:?5") == "00:55": {e}')
    
    total += 1
    try:
        result = candidate(time = "?9:59") == "19:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?9:59") == "19:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:59") == "23:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:59") == "23:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "12:?5") == "12:55"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "12:?5") == "12:55": {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:3?") == "19:39"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:3?") == "19:39": {e}')
    
    total += 1
    try:
        result = candidate(time = "20:??") == "20:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "20:??") == "20:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "?4:2?") == "14:29"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?4:2?") == "14:29": {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:3?") == "23:39"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:3?") == "23:39": {e}')
    
    total += 1
    try:
        result = candidate(time = "??:45") == "23:45"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "??:45") == "23:45": {e}')
    
    total += 1
    try:
        result = candidate(time = "23:?0") == "23:50"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:?0") == "23:50": {e}')
    
    total += 1
    try:
        result = candidate(time = "??:09") == "23:09"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "??:09") == "23:09": {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:2?") == "09:29"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:2?") == "09:29": {e}')
    
    total += 1
    try:
        result = candidate(time = "?4:?4") == "14:54"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?4:?4") == "14:54": {e}')
    
    total += 1
    try:
        result = candidate(time = "23:?5") == "23:55"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:?5") == "23:55": {e}')
    
    total += 1
    try:
        result = candidate(time = "23:?7") == "23:57"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:?7") == "23:57": {e}')
    
    total += 1
    try:
        result = candidate(time = "20:?9") == "20:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "20:?9") == "20:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "?3:?2") == "23:52"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?3:?2") == "23:52": {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:?4") == "09:54"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:?4") == "09:54": {e}')
    
    total += 1
    try:
        result = candidate(time = "?3:?8") == "23:58"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?3:?8") == "23:58": {e}')
    
    total += 1
    try:
        result = candidate(time = "???:59") == "23?:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "???:59") == "23?:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "2??:5?") == "23?:5?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2??:5?") == "23?:5?": {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:1?") == "23:19"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:1?") == "23:19": {e}')
    
    total += 1
    try:
        result = candidate(time = "22:?8") == "22:58"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "22:?8") == "22:58": {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:?9") == "09:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:?9") == "09:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:??") == "23:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:??") == "23:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:?2") == "09:52"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:?2") == "09:52": {e}')
    
    total += 1
    try:
        result = candidate(time = "02:?7") == "02:57"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "02:?7") == "02:57": {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:?8") == "19:58"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:?8") == "19:58": {e}')
    
    total += 1
    try:
        result = candidate(time = "09:?5") == "09:55"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "09:?5") == "09:55": {e}')
    
    total += 1
    try:
        result = candidate(time = "???:??") == "23?:9?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "???:??") == "23?:9?": {e}')
    
    total += 1
    try:
        result = candidate(time = "09:?3") == "09:53"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "09:?3") == "09:53": {e}')
    
    total += 1
    try:
        result = candidate(time = "?2:?7") == "22:57"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?2:?7") == "22:57": {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:4?") == "19:49"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:4?") == "19:49": {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:0?") == "23:09"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:0?") == "23:09": {e}')
    
    total += 1
    try:
        result = candidate(time = "??:59") == "23:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "??:59") == "23:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "23:?4") == "23:54"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:?4") == "23:54": {e}')
    
    total += 1
    try:
        result = candidate(time = "2??:3?") == "23?:3?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2??:3?") == "23?:3?": {e}')
    
    total += 1
    try:
        result = candidate(time = "0??:30") == "09?:30"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0??:30") == "09?:30": {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:?5") == "09:55"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:?5") == "09:55": {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:4?") == "09:49"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:4?") == "09:49": {e}')
    
    total += 1
    try:
        result = candidate(time = "09:5?") == "09:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "09:5?") == "09:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:?0") == "19:50"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:?0") == "19:50": {e}')
    
    total += 1
    try:
        result = candidate(time = "00:?9") == "00:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "00:?9") == "00:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:?5") == "23:55"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:?5") == "23:55": {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:5?") == "19:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:5?") == "19:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "19:?9") == "19:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "19:?9") == "19:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:?4") == "19:54"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:?4") == "19:54": {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:0?") == "19:09"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:0?") == "19:09": {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:4?") == "23:49"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:4?") == "23:49": {e}')
    
    total += 1
    try:
        result = candidate(time = "?0:?5") == "20:55"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?0:?5") == "20:55": {e}')
    
    total += 1
    try:
        result = candidate(time = "??:?9") == "23:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "??:?9") == "23:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "???:00") == "23?:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "???:00") == "23?:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "?9:?8") == "19:58"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?9:?8") == "19:58": {e}')
    
    total += 1
    try:
        result = candidate(time = "?3:?9") == "23:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?3:?9") == "23:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:5?") == "09:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:5?") == "09:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:?4") == "23:54"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:?4") == "23:54": {e}')
    
    total += 1
    try:
        result = candidate(time = "?9:?9") == "19:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?9:?9") == "19:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:00") == "23:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:00") == "23:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "?2:3?") == "22:39"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?2:3?") == "22:39": {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:??") == "09:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:??") == "09:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "?4:?8") == "14:58"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?4:?8") == "14:58": {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:?0") == "09:50"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:?0") == "09:50": {e}')
    
    total += 1
    try:
        result = candidate(time = "20:?4") == "20:54"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "20:?4") == "20:54": {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:59") == "19:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:59") == "19:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:0?") == "09:09"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:0?") == "09:09": {e}')
    
    total += 1
    try:
        result = candidate(time = "23:??") == "23:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:??") == "23:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "?0:?0") == "20:50"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?0:?0") == "20:50": {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:1?") == "09:19"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:1?") == "09:19": {e}')
    
    total += 1
    try:
        result = candidate(time = "1?:2?") == "19:29"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "1?:2?") == "19:29": {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:?8") == "09:58"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:?8") == "09:58": {e}')
    
    total += 1
    try:
        result = candidate(time = "19:?8") == "19:58"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "19:?8") == "19:58": {e}')
    
    total += 1
    try:
        result = candidate(time = "?2:?5") == "22:55"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?2:?5") == "22:55": {e}')
    
    total += 1
    try:
        result = candidate(time = "0?:45") == "09:45"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "0?:45") == "09:45": {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:?9") == "23:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:?9") == "23:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "?3:5?") == "23:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "?3:5?") == "23:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "23:?8") == "23:58"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:?8") == "23:58": {e}')
    
    total += 1
    try:
        result = candidate(time = "09:??") == "09:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "09:??") == "09:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:?8") == "23:58"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:?8") == "23:58": {e}')
    
    total += 1
    try:
        result = candidate(time = "2?:2?") == "23:29"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "2?:2?") == "23:29": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(time = "?3:?0") == "23:50"
    assert candidate(time = "1?:22") == "19:22"
    assert candidate(time = "1?:??") == "19:59"
    assert candidate(time = "0?:59") == "09:59"
    assert candidate(time = "23:?9") == "23:59"
    assert candidate(time = "00:?0") == "00:50"
    assert candidate(time = "2?:5?") == "23:59"
    assert candidate(time = "2?:?0") == "23:50"
    assert candidate(time = "?:?:??") == "2:?:9?"
    assert candidate(time = "00:??") == "00:59"
    assert candidate(time = "1?:?5") == "19:55"
    assert candidate(time = "?9:5?") == "19:59"
    assert candidate(time = "??:??") == "23:59"
    assert candidate(time = "12:3?") == "12:39"
    assert candidate(time = "??:00") == "23:00"
    assert candidate(time = "0?:3?") == "09:39"
    assert candidate(time = "1?:?9") == "19:59"
    assert candidate(time = "00:?5") == "00:55"
    assert candidate(time = "?9:59") == "19:59"
    assert candidate(time = "2?:59") == "23:59"
    assert candidate(time = "12:?5") == "12:55"
    assert candidate(time = "1?:3?") == "19:39"
    assert candidate(time = "20:??") == "20:59"
    assert candidate(time = "?4:2?") == "14:29"
    assert candidate(time = "2?:3?") == "23:39"
    assert candidate(time = "??:45") == "23:45"
    assert candidate(time = "23:?0") == "23:50"
    assert candidate(time = "??:09") == "23:09"
    assert candidate(time = "0?:2?") == "09:29"
    assert candidate(time = "?4:?4") == "14:54"
    assert candidate(time = "23:?5") == "23:55"
    assert candidate(time = "23:?7") == "23:57"
    assert candidate(time = "20:?9") == "20:59"
    assert candidate(time = "?3:?2") == "23:52"
    assert candidate(time = "0?:?4") == "09:54"
    assert candidate(time = "?3:?8") == "23:58"
    assert candidate(time = "???:59") == "23?:59"
    assert candidate(time = "2??:5?") == "23?:5?"
    assert candidate(time = "2?:1?") == "23:19"
    assert candidate(time = "22:?8") == "22:58"
    assert candidate(time = "0?:?9") == "09:59"
    assert candidate(time = "2?:??") == "23:59"
    assert candidate(time = "0?:?2") == "09:52"
    assert candidate(time = "02:?7") == "02:57"
    assert candidate(time = "1?:?8") == "19:58"
    assert candidate(time = "09:?5") == "09:55"
    assert candidate(time = "???:??") == "23?:9?"
    assert candidate(time = "09:?3") == "09:53"
    assert candidate(time = "?2:?7") == "22:57"
    assert candidate(time = "1?:4?") == "19:49"
    assert candidate(time = "2?:0?") == "23:09"
    assert candidate(time = "??:59") == "23:59"
    assert candidate(time = "23:?4") == "23:54"
    assert candidate(time = "2??:3?") == "23?:3?"
    assert candidate(time = "0??:30") == "09?:30"
    assert candidate(time = "0?:?5") == "09:55"
    assert candidate(time = "0?:4?") == "09:49"
    assert candidate(time = "09:5?") == "09:59"
    assert candidate(time = "1?:?0") == "19:50"
    assert candidate(time = "00:?9") == "00:59"
    assert candidate(time = "2?:?5") == "23:55"
    assert candidate(time = "1?:5?") == "19:59"
    assert candidate(time = "19:?9") == "19:59"
    assert candidate(time = "1?:?4") == "19:54"
    assert candidate(time = "1?:0?") == "19:09"
    assert candidate(time = "2?:4?") == "23:49"
    assert candidate(time = "?0:?5") == "20:55"
    assert candidate(time = "??:?9") == "23:59"
    assert candidate(time = "???:00") == "23?:00"
    assert candidate(time = "?9:?8") == "19:58"
    assert candidate(time = "?3:?9") == "23:59"
    assert candidate(time = "0?:5?") == "09:59"
    assert candidate(time = "2?:?4") == "23:54"
    assert candidate(time = "?9:?9") == "19:59"
    assert candidate(time = "2?:00") == "23:00"
    assert candidate(time = "?2:3?") == "22:39"
    assert candidate(time = "0?:??") == "09:59"
    assert candidate(time = "?4:?8") == "14:58"
    assert candidate(time = "0?:?0") == "09:50"
    assert candidate(time = "20:?4") == "20:54"
    assert candidate(time = "1?:59") == "19:59"
    assert candidate(time = "0?:0?") == "09:09"
    assert candidate(time = "23:??") == "23:59"
    assert candidate(time = "?0:?0") == "20:50"
    assert candidate(time = "0?:1?") == "09:19"
    assert candidate(time = "1?:2?") == "19:29"
    assert candidate(time = "0?:?8") == "09:58"
    assert candidate(time = "19:?8") == "19:58"
    assert candidate(time = "?2:?5") == "22:55"
    assert candidate(time = "0?:45") == "09:45"
    assert candidate(time = "2?:?9") == "23:59"
    assert candidate(time = "?3:5?") == "23:59"
    assert candidate(time = "23:?8") == "23:58"
    assert candidate(time = "09:??") == "09:59"
    assert candidate(time = "2?:?8") == "23:58"
    assert candidate(time = "2?:2?") == "23:29"


