def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(current = "01:59",correct = "02:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "01:59",correct = "02:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "00:01",correct = "00:02") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "00:01",correct = "00:02") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "02:30",correct = "04:35") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "02:30",correct = "04:35") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "12:00",correct = "13:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "12:00",correct = "13:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "00:00",correct = "23:59") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "00:00",correct = "23:59") == 32: {e}')
    
    total += 1
    try:
        result = candidate(current = "23:45",correct = "23:59") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "23:45",correct = "23:59") == 6: {e}')
    
    total += 1
    try:
        result = candidate(current = "00:01",correct = "00:05") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "00:01",correct = "00:05") == 4: {e}')
    
    total += 1
    try:
        result = candidate(current = "01:15",correct = "01:20") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "01:15",correct = "01:20") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "12:45",correct = "15:30") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "12:45",correct = "15:30") == 5: {e}')
    
    total += 1
    try:
        result = candidate(current = "23:00",correct = "23:15") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "23:00",correct = "23:15") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "09:15",correct = "09:15") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "09:15",correct = "09:15") == 0: {e}')
    
    total += 1
    try:
        result = candidate(current = "12:34",correct = "12:59") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "12:34",correct = "12:59") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "11:00",correct = "11:01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "11:00",correct = "11:01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "18:00",correct = "18:14") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "18:00",correct = "18:14") == 6: {e}')
    
    total += 1
    try:
        result = candidate(current = "15:30",correct = "16:45") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "15:30",correct = "16:45") == 2: {e}')
    
    total += 1
    try:
        result = candidate(current = "12:45",correct = "12:45") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "12:45",correct = "12:45") == 0: {e}')
    
    total += 1
    try:
        result = candidate(current = "01:00",correct = "02:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "01:00",correct = "02:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "23:40",correct = "00:05") == -21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "23:40",correct = "00:05") == -21: {e}')
    
    total += 1
    try:
        result = candidate(current = "21:45",correct = "22:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "21:45",correct = "22:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "12:00",correct = "12:15") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "12:00",correct = "12:15") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "09:40",correct = "10:00") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "09:40",correct = "10:00") == 2: {e}')
    
    total += 1
    try:
        result = candidate(current = "05:30",correct = "05:35") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "05:30",correct = "05:35") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "01:59",correct = "03:00") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "01:59",correct = "03:00") == 2: {e}')
    
    total += 1
    try:
        result = candidate(current = "23:59",correct = "23:59") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "23:59",correct = "23:59") == 0: {e}')
    
    total += 1
    try:
        result = candidate(current = "22:45",correct = "23:40") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "22:45",correct = "23:40") == 5: {e}')
    
    total += 1
    try:
        result = candidate(current = "06:40",correct = "06:55") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "06:40",correct = "06:55") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "09:50",correct = "10:10") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "09:50",correct = "10:10") == 2: {e}')
    
    total += 1
    try:
        result = candidate(current = "06:10",correct = "06:25") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "06:10",correct = "06:25") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "06:30",correct = "07:00") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "06:30",correct = "07:00") == 2: {e}')
    
    total += 1
    try:
        result = candidate(current = "05:47",correct = "06:02") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "05:47",correct = "06:02") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "21:30",correct = "01:00") == -19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "21:30",correct = "01:00") == -19: {e}')
    
    total += 1
    try:
        result = candidate(current = "09:47",correct = "18:23") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "09:47",correct = "18:23") == 12: {e}')
    
    total += 1
    try:
        result = candidate(current = "14:20",correct = "14:40") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "14:20",correct = "14:40") == 2: {e}')
    
    total += 1
    try:
        result = candidate(current = "03:33",correct = "04:08") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "03:33",correct = "04:08") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "20:15",correct = "21:10") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "20:15",correct = "21:10") == 5: {e}')
    
    total += 1
    try:
        result = candidate(current = "08:30",correct = "09:40") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "08:30",correct = "09:40") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "05:40",correct = "07:20") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "05:40",correct = "07:20") == 5: {e}')
    
    total += 1
    try:
        result = candidate(current = "17:45",correct = "19:00") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "17:45",correct = "19:00") == 2: {e}')
    
    total += 1
    try:
        result = candidate(current = "19:55",correct = "20:10") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "19:55",correct = "20:10") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "14:50",correct = "15:05") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "14:50",correct = "15:05") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "14:59",correct = "15:10") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "14:59",correct = "15:10") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "05:55",correct = "06:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "05:55",correct = "06:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "01:01",correct = "02:56") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "01:01",correct = "02:56") == 6: {e}')
    
    total += 1
    try:
        result = candidate(current = "08:20",correct = "08:35") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "08:20",correct = "08:35") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "05:00",correct = "09:55") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "05:00",correct = "09:55") == 9: {e}')
    
    total += 1
    try:
        result = candidate(current = "09:30",correct = "20:35") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "09:30",correct = "20:35") == 12: {e}')
    
    total += 1
    try:
        result = candidate(current = "07:30",correct = "07:31") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "07:30",correct = "07:31") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "01:23",correct = "02:18") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "01:23",correct = "02:18") == 5: {e}')
    
    total += 1
    try:
        result = candidate(current = "17:55",correct = "18:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "17:55",correct = "18:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "16:50",correct = "18:25") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "16:50",correct = "18:25") == 4: {e}')
    
    total += 1
    try:
        result = candidate(current = "10:05",correct = "14:40") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "10:05",correct = "14:40") == 7: {e}')
    
    total += 1
    try:
        result = candidate(current = "01:05",correct = "02:10") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "01:05",correct = "02:10") == 2: {e}')
    
    total += 1
    try:
        result = candidate(current = "03:15",correct = "03:30") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "03:15",correct = "03:30") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "20:30",correct = "22:35") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "20:30",correct = "22:35") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "18:10",correct = "19:10") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "18:10",correct = "19:10") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "03:00",correct = "07:15") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "03:00",correct = "07:15") == 5: {e}')
    
    total += 1
    try:
        result = candidate(current = "03:14",correct = "06:09") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "03:14",correct = "06:09") == 7: {e}')
    
    total += 1
    try:
        result = candidate(current = "07:45",correct = "08:30") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "07:45",correct = "08:30") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "09:14",correct = "09:44") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "09:14",correct = "09:44") == 2: {e}')
    
    total += 1
    try:
        result = candidate(current = "01:01",correct = "04:04") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "01:01",correct = "04:04") == 6: {e}')
    
    total += 1
    try:
        result = candidate(current = "13:59",correct = "14:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "13:59",correct = "14:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "02:22",correct = "02:27") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "02:22",correct = "02:27") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "05:30",correct = "05:45") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "05:30",correct = "05:45") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "11:20",correct = "12:55") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "11:20",correct = "12:55") == 4: {e}')
    
    total += 1
    try:
        result = candidate(current = "17:30",correct = "18:05") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "17:30",correct = "18:05") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "11:59",correct = "12:04") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "11:59",correct = "12:04") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "08:37",correct = "09:02") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "08:37",correct = "09:02") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "16:00",correct = "16:16") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "16:00",correct = "16:16") == 2: {e}')
    
    total += 1
    try:
        result = candidate(current = "18:34",correct = "19:50") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "18:34",correct = "19:50") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "19:10",correct = "21:25") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "19:10",correct = "21:25") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "05:05",correct = "11:10") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "05:05",correct = "11:10") == 7: {e}')
    
    total += 1
    try:
        result = candidate(current = "13:20",correct = "17:50") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "13:20",correct = "17:50") == 6: {e}')
    
    total += 1
    try:
        result = candidate(current = "20:59",correct = "21:59") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "20:59",correct = "21:59") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "04:30",correct = "06:10") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "04:30",correct = "06:10") == 5: {e}')
    
    total += 1
    try:
        result = candidate(current = "16:25",correct = "17:00") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "16:25",correct = "17:00") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "08:59",correct = "09:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "08:59",correct = "09:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "03:23",correct = "03:58") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "03:23",correct = "03:58") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "14:45",correct = "20:30") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "14:45",correct = "20:30") == 8: {e}')
    
    total += 1
    try:
        result = candidate(current = "19:47",correct = "21:00") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "19:47",correct = "21:00") == 6: {e}')
    
    total += 1
    try:
        result = candidate(current = "00:01",correct = "23:59") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "00:01",correct = "23:59") == 31: {e}')
    
    total += 1
    try:
        result = candidate(current = "22:25",correct = "22:40") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "22:25",correct = "22:40") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "17:30",correct = "20:00") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "17:30",correct = "20:00") == 4: {e}')
    
    total += 1
    try:
        result = candidate(current = "14:10",correct = "15:35") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "14:10",correct = "15:35") == 4: {e}')
    
    total += 1
    try:
        result = candidate(current = "00:01",correct = "00:06") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "00:01",correct = "00:06") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "01:15",correct = "02:45") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "01:15",correct = "02:45") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "13:47",correct = "18:23") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "13:47",correct = "18:23") == 8: {e}')
    
    total += 1
    try:
        result = candidate(current = "09:00",correct = "09:09") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "09:00",correct = "09:09") == 5: {e}')
    
    total += 1
    try:
        result = candidate(current = "06:55",correct = "07:10") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "06:55",correct = "07:10") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "13:45",correct = "15:30") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "13:45",correct = "15:30") == 4: {e}')
    
    total += 1
    try:
        result = candidate(current = "13:45",correct = "15:10") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "13:45",correct = "15:10") == 4: {e}')
    
    total += 1
    try:
        result = candidate(current = "09:55",correct = "11:40") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "09:55",correct = "11:40") == 4: {e}')
    
    total += 1
    try:
        result = candidate(current = "20:15",correct = "21:25") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "20:15",correct = "21:25") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "11:59",correct = "12:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "11:59",correct = "12:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "17:31",correct = "20:00") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "17:31",correct = "20:00") == 9: {e}')
    
    total += 1
    try:
        result = candidate(current = "01:01",correct = "22:59") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "01:01",correct = "22:59") == 29: {e}')
    
    total += 1
    try:
        result = candidate(current = "12:25",correct = "14:15") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "12:25",correct = "14:15") == 5: {e}')
    
    total += 1
    try:
        result = candidate(current = "10:30",correct = "10:55") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "10:30",correct = "10:55") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "13:25",correct = "13:40") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "13:25",correct = "13:40") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "16:10",correct = "16:55") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "16:10",correct = "16:55") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "07:40",correct = "07:55") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "07:40",correct = "07:55") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "05:20",correct = "06:50") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "05:20",correct = "06:50") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "08:30",correct = "20:45") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "08:30",correct = "20:45") == 13: {e}')
    
    total += 1
    try:
        result = candidate(current = "14:15",correct = "14:15") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "14:15",correct = "14:15") == 0: {e}')
    
    total += 1
    try:
        result = candidate(current = "13:45",correct = "14:10") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "13:45",correct = "14:10") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "09:05",correct = "09:10") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "09:05",correct = "09:10") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "17:00",correct = "18:30") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "17:00",correct = "18:30") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "20:50",correct = "21:50") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "20:50",correct = "21:50") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "12:45",correct = "13:30") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "12:45",correct = "13:30") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "18:44",correct = "19:59") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "18:44",correct = "19:59") == 2: {e}')
    
    total += 1
    try:
        result = candidate(current = "05:20",correct = "05:25") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "05:20",correct = "05:25") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "05:45",correct = "10:30") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "05:45",correct = "10:30") == 7: {e}')
    
    total += 1
    try:
        result = candidate(current = "03:00",correct = "04:59") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "03:00",correct = "04:59") == 10: {e}')
    
    total += 1
    try:
        result = candidate(current = "10:10",correct = "11:55") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "10:10",correct = "11:55") == 4: {e}')
    
    total += 1
    try:
        result = candidate(current = "04:59",correct = "05:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "04:59",correct = "05:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "01:45",correct = "02:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "01:45",correct = "02:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "00:59",correct = "01:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "00:59",correct = "01:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "13:12",correct = "13:57") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "13:12",correct = "13:57") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "19:50",correct = "21:00") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "19:50",correct = "21:00") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "10:10",correct = "10:55") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "10:10",correct = "10:55") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "09:01",correct = "09:16") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "09:01",correct = "09:16") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "22:15",correct = "23:00") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "22:15",correct = "23:00") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "17:00",correct = "19:45") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "17:00",correct = "19:45") == 5: {e}')
    
    total += 1
    try:
        result = candidate(current = "06:30",correct = "08:45") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "06:30",correct = "08:45") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "22:00",correct = "23:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "22:00",correct = "23:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "14:45",correct = "15:05") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "14:45",correct = "15:05") == 2: {e}')
    
    total += 1
    try:
        result = candidate(current = "04:55",correct = "05:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "04:55",correct = "05:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "10:05",correct = "10:10") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "10:05",correct = "10:10") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "13:47",correct = "15:12") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "13:47",correct = "15:12") == 4: {e}')
    
    total += 1
    try:
        result = candidate(current = "09:45",correct = "11:20") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "09:45",correct = "11:20") == 4: {e}')
    
    total += 1
    try:
        result = candidate(current = "17:40",correct = "18:20") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "17:40",correct = "18:20") == 4: {e}')
    
    total += 1
    try:
        result = candidate(current = "22:15",correct = "22:50") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "22:15",correct = "22:50") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "23:40",correct = "00:15") == -21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "23:40",correct = "00:15") == -21: {e}')
    
    total += 1
    try:
        result = candidate(current = "08:00",correct = "08:05") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "08:00",correct = "08:05") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "14:05",correct = "14:14") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "14:05",correct = "14:14") == 5: {e}')
    
    total += 1
    try:
        result = candidate(current = "00:05",correct = "01:05") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "00:05",correct = "01:05") == 1: {e}')
    
    total += 1
    try:
        result = candidate(current = "01:23",correct = "05:47") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "01:23",correct = "05:47") == 10: {e}')
    
    total += 1
    try:
        result = candidate(current = "22:15",correct = "23:45") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "22:15",correct = "23:45") == 3: {e}')
    
    total += 1
    try:
        result = candidate(current = "20:30",correct = "22:45") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(current = "20:30",correct = "22:45") == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(current = "01:59",correct = "02:00") == 1
    assert candidate(current = "00:01",correct = "00:02") == 1
    assert candidate(current = "02:30",correct = "04:35") == 3
    assert candidate(current = "12:00",correct = "13:00") == 1
    assert candidate(current = "00:00",correct = "23:59") == 32
    assert candidate(current = "23:45",correct = "23:59") == 6
    assert candidate(current = "00:01",correct = "00:05") == 4
    assert candidate(current = "01:15",correct = "01:20") == 1
    assert candidate(current = "12:45",correct = "15:30") == 5
    assert candidate(current = "23:00",correct = "23:15") == 1
    assert candidate(current = "09:15",correct = "09:15") == 0
    assert candidate(current = "12:34",correct = "12:59") == 3
    assert candidate(current = "11:00",correct = "11:01") == 1
    assert candidate(current = "18:00",correct = "18:14") == 6
    assert candidate(current = "15:30",correct = "16:45") == 2
    assert candidate(current = "12:45",correct = "12:45") == 0
    assert candidate(current = "01:00",correct = "02:00") == 1
    assert candidate(current = "23:40",correct = "00:05") == -21
    assert candidate(current = "21:45",correct = "22:00") == 1
    assert candidate(current = "12:00",correct = "12:15") == 1
    assert candidate(current = "09:40",correct = "10:00") == 2
    assert candidate(current = "05:30",correct = "05:35") == 1
    assert candidate(current = "01:59",correct = "03:00") == 2
    assert candidate(current = "23:59",correct = "23:59") == 0
    assert candidate(current = "22:45",correct = "23:40") == 5
    assert candidate(current = "06:40",correct = "06:55") == 1
    assert candidate(current = "09:50",correct = "10:10") == 2
    assert candidate(current = "06:10",correct = "06:25") == 1
    assert candidate(current = "06:30",correct = "07:00") == 2
    assert candidate(current = "05:47",correct = "06:02") == 1
    assert candidate(current = "21:30",correct = "01:00") == -19
    assert candidate(current = "09:47",correct = "18:23") == 12
    assert candidate(current = "14:20",correct = "14:40") == 2
    assert candidate(current = "03:33",correct = "04:08") == 3
    assert candidate(current = "20:15",correct = "21:10") == 5
    assert candidate(current = "08:30",correct = "09:40") == 3
    assert candidate(current = "05:40",correct = "07:20") == 5
    assert candidate(current = "17:45",correct = "19:00") == 2
    assert candidate(current = "19:55",correct = "20:10") == 1
    assert candidate(current = "14:50",correct = "15:05") == 1
    assert candidate(current = "14:59",correct = "15:10") == 3
    assert candidate(current = "05:55",correct = "06:00") == 1
    assert candidate(current = "01:01",correct = "02:56") == 6
    assert candidate(current = "08:20",correct = "08:35") == 1
    assert candidate(current = "05:00",correct = "09:55") == 9
    assert candidate(current = "09:30",correct = "20:35") == 12
    assert candidate(current = "07:30",correct = "07:31") == 1
    assert candidate(current = "01:23",correct = "02:18") == 5
    assert candidate(current = "17:55",correct = "18:00") == 1
    assert candidate(current = "16:50",correct = "18:25") == 4
    assert candidate(current = "10:05",correct = "14:40") == 7
    assert candidate(current = "01:05",correct = "02:10") == 2
    assert candidate(current = "03:15",correct = "03:30") == 1
    assert candidate(current = "20:30",correct = "22:35") == 3
    assert candidate(current = "18:10",correct = "19:10") == 1
    assert candidate(current = "03:00",correct = "07:15") == 5
    assert candidate(current = "03:14",correct = "06:09") == 7
    assert candidate(current = "07:45",correct = "08:30") == 3
    assert candidate(current = "09:14",correct = "09:44") == 2
    assert candidate(current = "01:01",correct = "04:04") == 6
    assert candidate(current = "13:59",correct = "14:00") == 1
    assert candidate(current = "02:22",correct = "02:27") == 1
    assert candidate(current = "05:30",correct = "05:45") == 1
    assert candidate(current = "11:20",correct = "12:55") == 4
    assert candidate(current = "17:30",correct = "18:05") == 3
    assert candidate(current = "11:59",correct = "12:04") == 1
    assert candidate(current = "08:37",correct = "09:02") == 3
    assert candidate(current = "16:00",correct = "16:16") == 2
    assert candidate(current = "18:34",correct = "19:50") == 3
    assert candidate(current = "19:10",correct = "21:25") == 3
    assert candidate(current = "05:05",correct = "11:10") == 7
    assert candidate(current = "13:20",correct = "17:50") == 6
    assert candidate(current = "20:59",correct = "21:59") == 1
    assert candidate(current = "04:30",correct = "06:10") == 5
    assert candidate(current = "16:25",correct = "17:00") == 3
    assert candidate(current = "08:59",correct = "09:00") == 1
    assert candidate(current = "03:23",correct = "03:58") == 3
    assert candidate(current = "14:45",correct = "20:30") == 8
    assert candidate(current = "19:47",correct = "21:00") == 6
    assert candidate(current = "00:01",correct = "23:59") == 31
    assert candidate(current = "22:25",correct = "22:40") == 1
    assert candidate(current = "17:30",correct = "20:00") == 4
    assert candidate(current = "14:10",correct = "15:35") == 4
    assert candidate(current = "00:01",correct = "00:06") == 1
    assert candidate(current = "01:15",correct = "02:45") == 3
    assert candidate(current = "13:47",correct = "18:23") == 8
    assert candidate(current = "09:00",correct = "09:09") == 5
    assert candidate(current = "06:55",correct = "07:10") == 1
    assert candidate(current = "13:45",correct = "15:30") == 4
    assert candidate(current = "13:45",correct = "15:10") == 4
    assert candidate(current = "09:55",correct = "11:40") == 4
    assert candidate(current = "20:15",correct = "21:25") == 3
    assert candidate(current = "11:59",correct = "12:00") == 1
    assert candidate(current = "17:31",correct = "20:00") == 9
    assert candidate(current = "01:01",correct = "22:59") == 29
    assert candidate(current = "12:25",correct = "14:15") == 5
    assert candidate(current = "10:30",correct = "10:55") == 3
    assert candidate(current = "13:25",correct = "13:40") == 1
    assert candidate(current = "16:10",correct = "16:55") == 3
    assert candidate(current = "07:40",correct = "07:55") == 1
    assert candidate(current = "05:20",correct = "06:50") == 3
    assert candidate(current = "08:30",correct = "20:45") == 13
    assert candidate(current = "14:15",correct = "14:15") == 0
    assert candidate(current = "13:45",correct = "14:10") == 3
    assert candidate(current = "09:05",correct = "09:10") == 1
    assert candidate(current = "17:00",correct = "18:30") == 3
    assert candidate(current = "20:50",correct = "21:50") == 1
    assert candidate(current = "12:45",correct = "13:30") == 3
    assert candidate(current = "18:44",correct = "19:59") == 2
    assert candidate(current = "05:20",correct = "05:25") == 1
    assert candidate(current = "05:45",correct = "10:30") == 7
    assert candidate(current = "03:00",correct = "04:59") == 10
    assert candidate(current = "10:10",correct = "11:55") == 4
    assert candidate(current = "04:59",correct = "05:00") == 1
    assert candidate(current = "01:45",correct = "02:00") == 1
    assert candidate(current = "00:59",correct = "01:00") == 1
    assert candidate(current = "13:12",correct = "13:57") == 3
    assert candidate(current = "19:50",correct = "21:00") == 3
    assert candidate(current = "10:10",correct = "10:55") == 3
    assert candidate(current = "09:01",correct = "09:16") == 1
    assert candidate(current = "22:15",correct = "23:00") == 3
    assert candidate(current = "17:00",correct = "19:45") == 5
    assert candidate(current = "06:30",correct = "08:45") == 3
    assert candidate(current = "22:00",correct = "23:00") == 1
    assert candidate(current = "14:45",correct = "15:05") == 2
    assert candidate(current = "04:55",correct = "05:00") == 1
    assert candidate(current = "10:05",correct = "10:10") == 1
    assert candidate(current = "13:47",correct = "15:12") == 4
    assert candidate(current = "09:45",correct = "11:20") == 4
    assert candidate(current = "17:40",correct = "18:20") == 4
    assert candidate(current = "22:15",correct = "22:50") == 3
    assert candidate(current = "23:40",correct = "00:15") == -21
    assert candidate(current = "08:00",correct = "08:05") == 1
    assert candidate(current = "14:05",correct = "14:14") == 5
    assert candidate(current = "00:05",correct = "01:05") == 1
    assert candidate(current = "01:23",correct = "05:47") == 10
    assert candidate(current = "22:15",correct = "23:45") == 3
    assert candidate(current = "20:30",correct = "22:45") == 3


