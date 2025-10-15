def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(loginTime = "11:59",logoutTime = "12:01") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "11:59",logoutTime = "12:01") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "14:30",logoutTime = "15:30") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "14:30",logoutTime = "15:30") == 4: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "00:01",logoutTime = "00:14") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "00:01",logoutTime = "00:14") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "14:20",logoutTime = "15:50") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "14:20",logoutTime = "15:50") == 5: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "00:00",logoutTime = "23:59") == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "00:00",logoutTime = "23:59") == 95: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "18:14",logoutTime = "18:46") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "18:14",logoutTime = "18:46") == 2: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "14:30",logoutTime = "14:45") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "14:30",logoutTime = "14:45") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "23:45",logoutTime = "00:15") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "23:45",logoutTime = "00:15") == 2: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "22:15",logoutTime = "23:45") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "22:15",logoutTime = "23:45") == 6: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "15:30",logoutTime = "15:30") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "15:30",logoutTime = "15:30") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "14:20",logoutTime = "14:59") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "14:20",logoutTime = "14:59") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "05:45",logoutTime = "06:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "05:45",logoutTime = "06:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "09:31",logoutTime = "10:14") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "09:31",logoutTime = "10:14") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "00:01",logoutTime = "23:59") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "00:01",logoutTime = "23:59") == 94: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "07:45",logoutTime = "08:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "07:45",logoutTime = "08:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "11:59",logoutTime = "12:00") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "11:59",logoutTime = "12:00") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "23:45",logoutTime = "00:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "23:45",logoutTime = "00:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "05:00",logoutTime = "06:00") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "05:00",logoutTime = "06:00") == 4: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "01:10",logoutTime = "01:55") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "01:10",logoutTime = "01:55") == 2: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "01:15",logoutTime = "01:45") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "01:15",logoutTime = "01:45") == 2: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "07:15",logoutTime = "07:30") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "07:15",logoutTime = "07:30") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "01:05",logoutTime = "01:40") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "01:05",logoutTime = "01:40") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "21:30",logoutTime = "03:00") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "21:30",logoutTime = "03:00") == 22: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "13:00",logoutTime = "13:01") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "13:00",logoutTime = "13:01") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "12:00",logoutTime = "12:15") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "12:00",logoutTime = "12:15") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "05:30",logoutTime = "06:00") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "05:30",logoutTime = "06:00") == 2: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "08:45",logoutTime = "09:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "08:45",logoutTime = "09:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "01:00",logoutTime = "02:30") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "01:00",logoutTime = "02:30") == 6: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "18:15",logoutTime = "18:44") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "18:15",logoutTime = "18:44") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "10:15",logoutTime = "11:14") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "10:15",logoutTime = "11:14") == 3: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "19:10",logoutTime = "20:50") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "19:10",logoutTime = "20:50") == 6: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "07:00",logoutTime = "07:01") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "07:00",logoutTime = "07:01") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "12:16",logoutTime = "12:44") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "12:16",logoutTime = "12:44") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "20:44",logoutTime = "21:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "20:44",logoutTime = "21:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "12:30",logoutTime = "14:45") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "12:30",logoutTime = "14:45") == 9: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "11:15",logoutTime = "11:16") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "11:15",logoutTime = "11:16") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "14:30",logoutTime = "14:30") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "14:30",logoutTime = "14:30") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "18:45",logoutTime = "19:45") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "18:45",logoutTime = "19:45") == 4: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "18:00",logoutTime = "07:00") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "18:00",logoutTime = "07:00") == 52: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "07:15",logoutTime = "07:15") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "07:15",logoutTime = "07:15") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "08:15",logoutTime = "08:30") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "08:15",logoutTime = "08:30") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "02:10",logoutTime = "05:50") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "02:10",logoutTime = "05:50") == 14: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "08:25",logoutTime = "09:50") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "08:25",logoutTime = "09:50") == 5: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "01:00",logoutTime = "01:14") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "01:00",logoutTime = "01:14") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "12:30",logoutTime = "13:15") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "12:30",logoutTime = "13:15") == 3: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "03:45",logoutTime = "05:10") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "03:45",logoutTime = "05:10") == 5: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "06:30",logoutTime = "06:30") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "06:30",logoutTime = "06:30") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "17:45",logoutTime = "18:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "17:45",logoutTime = "18:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "20:00",logoutTime = "20:14") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "20:00",logoutTime = "20:14") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "23:59",logoutTime = "00:01") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "23:59",logoutTime = "00:01") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "07:07",logoutTime = "07:32") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "07:07",logoutTime = "07:32") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "06:59",logoutTime = "07:01") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "06:59",logoutTime = "07:01") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "14:23",logoutTime = "14:24") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "14:23",logoutTime = "14:24") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "12:10",logoutTime = "12:20") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "12:10",logoutTime = "12:20") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "05:00",logoutTime = "05:00") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "05:00",logoutTime = "05:00") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "02:30",logoutTime = "02:31") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "02:30",logoutTime = "02:31") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "20:00",logoutTime = "04:00") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "20:00",logoutTime = "04:00") == 32: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "21:15",logoutTime = "21:45") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "21:15",logoutTime = "21:45") == 2: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "00:45",logoutTime = "01:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "00:45",logoutTime = "01:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "21:10",logoutTime = "21:14") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "21:10",logoutTime = "21:14") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "12:45",logoutTime = "13:45") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "12:45",logoutTime = "13:45") == 4: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "00:10",logoutTime = "01:05") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "00:10",logoutTime = "01:05") == 3: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "14:00",logoutTime = "14:14") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "14:00",logoutTime = "14:14") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "17:10",logoutTime = "18:55") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "17:10",logoutTime = "18:55") == 6: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "06:30",logoutTime = "07:30") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "06:30",logoutTime = "07:30") == 4: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "00:44",logoutTime = "00:59") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "00:44",logoutTime = "00:59") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "16:00",logoutTime = "16:01") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "16:00",logoutTime = "16:01") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "09:00",logoutTime = "21:15") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "09:00",logoutTime = "21:15") == 49: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "15:10",logoutTime = "15:15") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "15:10",logoutTime = "15:15") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "14:00",logoutTime = "18:30") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "14:00",logoutTime = "18:30") == 18: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "20:00",logoutTime = "21:00") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "20:00",logoutTime = "21:00") == 4: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "11:10",logoutTime = "11:10") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "11:10",logoutTime = "11:10") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "11:45",logoutTime = "12:44") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "11:45",logoutTime = "12:44") == 3: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "07:45",logoutTime = "08:15") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "07:45",logoutTime = "08:15") == 2: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "10:00",logoutTime = "10:14") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "10:00",logoutTime = "10:14") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "07:05",logoutTime = "08:10") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "07:05",logoutTime = "08:10") == 3: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "08:45",logoutTime = "09:15") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "08:45",logoutTime = "09:15") == 2: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "16:45",logoutTime = "17:45") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "16:45",logoutTime = "17:45") == 4: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "07:01",logoutTime = "07:14") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "07:01",logoutTime = "07:14") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "11:46",logoutTime = "12:44") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "11:46",logoutTime = "12:44") == 2: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "09:00",logoutTime = "16:45") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "09:00",logoutTime = "16:45") == 31: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "13:30",logoutTime = "14:00") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "13:30",logoutTime = "14:00") == 2: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "20:00",logoutTime = "20:15") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "20:00",logoutTime = "20:15") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "00:00",logoutTime = "04:00") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "00:00",logoutTime = "04:00") == 16: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "00:00",logoutTime = "00:15") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "00:00",logoutTime = "00:15") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "07:07",logoutTime = "07:47") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "07:07",logoutTime = "07:47") == 2: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "13:46",logoutTime = "13:47") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "13:46",logoutTime = "13:47") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "13:15",logoutTime = "14:15") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "13:15",logoutTime = "14:15") == 4: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "14:16",logoutTime = "15:14") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "14:16",logoutTime = "15:14") == 2: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "21:00",logoutTime = "21:59") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "21:00",logoutTime = "21:59") == 3: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "07:00",logoutTime = "07:14") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "07:00",logoutTime = "07:14") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "01:01",logoutTime = "24:00") == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "01:01",logoutTime = "24:00") == 91: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "17:15",logoutTime = "17:45") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "17:15",logoutTime = "17:45") == 2: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "12:00",logoutTime = "12:00") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "12:00",logoutTime = "12:00") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "03:45",logoutTime = "04:15") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "03:45",logoutTime = "04:15") == 2: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "04:45",logoutTime = "05:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "04:45",logoutTime = "05:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "00:00",logoutTime = "23:45") == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "00:00",logoutTime = "23:45") == 95: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "02:20",logoutTime = "02:25") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "02:20",logoutTime = "02:25") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "09:45",logoutTime = "10:45") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "09:45",logoutTime = "10:45") == 4: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "22:00",logoutTime = "01:30") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "22:00",logoutTime = "01:30") == 14: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "07:07",logoutTime = "07:45") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "07:07",logoutTime = "07:45") == 2: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "22:45",logoutTime = "23:59") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "22:45",logoutTime = "23:59") == 4: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "05:00",logoutTime = "24:00") == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "05:00",logoutTime = "24:00") == 76: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "02:30",logoutTime = "03:30") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "02:30",logoutTime = "03:30") == 4: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "13:23",logoutTime = "14:22") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "13:23",logoutTime = "14:22") == 3: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "16:20",logoutTime = "18:55") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "16:20",logoutTime = "18:55") == 9: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "00:00",logoutTime = "00:14") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "00:00",logoutTime = "00:14") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "08:20",logoutTime = "09:20") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "08:20",logoutTime = "09:20") == 3: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "12:05",logoutTime = "12:20") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "12:05",logoutTime = "12:20") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "03:33",logoutTime = "04:48") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "03:33",logoutTime = "04:48") == 4: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "23:00",logoutTime = "23:15") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "23:00",logoutTime = "23:15") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "13:46",logoutTime = "14:14") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "13:46",logoutTime = "14:14") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "15:00",logoutTime = "15:15") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "15:00",logoutTime = "15:15") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "13:15",logoutTime = "13:30") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "13:15",logoutTime = "13:30") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "15:00",logoutTime = "16:00") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "15:00",logoutTime = "16:00") == 4: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "03:00",logoutTime = "03:01") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "03:00",logoutTime = "03:01") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "09:00",logoutTime = "09:00") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "09:00",logoutTime = "09:00") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "00:00",logoutTime = "24:00") == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "00:00",logoutTime = "24:00") == 96: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "19:40",logoutTime = "20:05") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "19:40",logoutTime = "20:05") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "16:00",logoutTime = "17:00") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "16:00",logoutTime = "17:00") == 4: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "12:46",logoutTime = "13:14") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "12:46",logoutTime = "13:14") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "03:45",logoutTime = "03:45") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "03:45",logoutTime = "03:45") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "00:15",logoutTime = "00:30") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "00:15",logoutTime = "00:30") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "08:30",logoutTime = "09:00") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "08:30",logoutTime = "09:00") == 2: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "23:15",logoutTime = "00:14") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "23:15",logoutTime = "00:14") == 3: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "05:55",logoutTime = "06:05") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "05:55",logoutTime = "06:05") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "00:15",logoutTime = "23:59") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "00:15",logoutTime = "23:59") == 94: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "10:00",logoutTime = "10:00") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "10:00",logoutTime = "10:00") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "01:59",logoutTime = "02:01") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "01:59",logoutTime = "02:01") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "06:59",logoutTime = "07:00") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "06:59",logoutTime = "07:00") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "23:40",logoutTime = "00:10") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "23:40",logoutTime = "00:10") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "09:00",logoutTime = "09:59") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "09:00",logoutTime = "09:59") == 3: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "06:30",logoutTime = "07:00") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "06:30",logoutTime = "07:00") == 2: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "01:45",logoutTime = "02:44") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "01:45",logoutTime = "02:44") == 3: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "18:00",logoutTime = "18:00") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "18:00",logoutTime = "18:00") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "01:14",logoutTime = "01:46") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "01:14",logoutTime = "01:46") == 2: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "23:55",logoutTime = "00:05") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "23:55",logoutTime = "00:05") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "09:00",logoutTime = "18:45") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "09:00",logoutTime = "18:45") == 39: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "01:46",logoutTime = "02:14") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "01:46",logoutTime = "02:14") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "09:10",logoutTime = "09:20") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "09:10",logoutTime = "09:20") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "09:00",logoutTime = "09:14") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "09:00",logoutTime = "09:14") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "18:25",logoutTime = "19:50") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "18:25",logoutTime = "19:50") == 5: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "23:00",logoutTime = "23:45") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "23:00",logoutTime = "23:45") == 3: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "07:05",logoutTime = "08:05") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "07:05",logoutTime = "08:05") == 3: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "23:30",logoutTime = "00:30") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "23:30",logoutTime = "00:30") == 4: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "10:00",logoutTime = "24:00") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "10:00",logoutTime = "24:00") == 56: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "06:30",logoutTime = "09:15") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "06:30",logoutTime = "09:15") == 11: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "06:45",logoutTime = "07:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "06:45",logoutTime = "07:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "00:30",logoutTime = "00:45") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "00:30",logoutTime = "00:45") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "21:00",logoutTime = "22:15") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "21:00",logoutTime = "22:15") == 5: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "14:45",logoutTime = "15:00") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "14:45",logoutTime = "15:00") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "00:05",logoutTime = "00:30") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "00:05",logoutTime = "00:30") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "11:59",logoutTime = "12:14") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "11:59",logoutTime = "12:14") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "18:45",logoutTime = "19:10") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "18:45",logoutTime = "19:10") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "13:30",logoutTime = "16:45") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "13:30",logoutTime = "16:45") == 13: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "09:44",logoutTime = "09:45") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "09:44",logoutTime = "09:45") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "08:29",logoutTime = "08:40") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "08:29",logoutTime = "08:40") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "14:30",logoutTime = "16:30") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "14:30",logoutTime = "16:30") == 8: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "01:05",logoutTime = "02:30") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "01:05",logoutTime = "02:30") == 5: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "00:00",logoutTime = "01:00") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "00:00",logoutTime = "01:00") == 4: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "05:15",logoutTime = "05:15") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "05:15",logoutTime = "05:15") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "13:20",logoutTime = "13:59") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "13:20",logoutTime = "13:59") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "09:59",logoutTime = "10:00") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "09:59",logoutTime = "10:00") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "10:10",logoutTime = "11:09") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "10:10",logoutTime = "11:09") == 3: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "01:10",logoutTime = "01:40") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "01:10",logoutTime = "01:40") == 1: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "13:00",logoutTime = "13:14") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "13:00",logoutTime = "13:14") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "23:01",logoutTime = "23:14") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "23:01",logoutTime = "23:14") == 0: {e}')
    
    total += 1
    try:
        result = candidate(loginTime = "19:15",logoutTime = "20:00") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(loginTime = "19:15",logoutTime = "20:00") == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(loginTime = "11:59",logoutTime = "12:01") == 0
    assert candidate(loginTime = "14:30",logoutTime = "15:30") == 4
    assert candidate(loginTime = "00:01",logoutTime = "00:14") == 0
    assert candidate(loginTime = "14:20",logoutTime = "15:50") == 5
    assert candidate(loginTime = "00:00",logoutTime = "23:59") == 95
    assert candidate(loginTime = "18:14",logoutTime = "18:46") == 2
    assert candidate(loginTime = "14:30",logoutTime = "14:45") == 1
    assert candidate(loginTime = "23:45",logoutTime = "00:15") == 2
    assert candidate(loginTime = "22:15",logoutTime = "23:45") == 6
    assert candidate(loginTime = "15:30",logoutTime = "15:30") == 0
    assert candidate(loginTime = "14:20",logoutTime = "14:59") == 1
    assert candidate(loginTime = "05:45",logoutTime = "06:00") == 1
    assert candidate(loginTime = "09:31",logoutTime = "10:14") == 1
    assert candidate(loginTime = "00:01",logoutTime = "23:59") == 94
    assert candidate(loginTime = "07:45",logoutTime = "08:00") == 1
    assert candidate(loginTime = "11:59",logoutTime = "12:00") == 0
    assert candidate(loginTime = "23:45",logoutTime = "00:00") == 1
    assert candidate(loginTime = "05:00",logoutTime = "06:00") == 4
    assert candidate(loginTime = "01:10",logoutTime = "01:55") == 2
    assert candidate(loginTime = "01:15",logoutTime = "01:45") == 2
    assert candidate(loginTime = "07:15",logoutTime = "07:30") == 1
    assert candidate(loginTime = "01:05",logoutTime = "01:40") == 1
    assert candidate(loginTime = "21:30",logoutTime = "03:00") == 22
    assert candidate(loginTime = "13:00",logoutTime = "13:01") == 0
    assert candidate(loginTime = "12:00",logoutTime = "12:15") == 1
    assert candidate(loginTime = "05:30",logoutTime = "06:00") == 2
    assert candidate(loginTime = "08:45",logoutTime = "09:00") == 1
    assert candidate(loginTime = "01:00",logoutTime = "02:30") == 6
    assert candidate(loginTime = "18:15",logoutTime = "18:44") == 1
    assert candidate(loginTime = "10:15",logoutTime = "11:14") == 3
    assert candidate(loginTime = "19:10",logoutTime = "20:50") == 6
    assert candidate(loginTime = "07:00",logoutTime = "07:01") == 0
    assert candidate(loginTime = "12:16",logoutTime = "12:44") == 0
    assert candidate(loginTime = "20:44",logoutTime = "21:00") == 1
    assert candidate(loginTime = "12:30",logoutTime = "14:45") == 9
    assert candidate(loginTime = "11:15",logoutTime = "11:16") == 0
    assert candidate(loginTime = "14:30",logoutTime = "14:30") == 0
    assert candidate(loginTime = "18:45",logoutTime = "19:45") == 4
    assert candidate(loginTime = "18:00",logoutTime = "07:00") == 52
    assert candidate(loginTime = "07:15",logoutTime = "07:15") == 0
    assert candidate(loginTime = "08:15",logoutTime = "08:30") == 1
    assert candidate(loginTime = "02:10",logoutTime = "05:50") == 14
    assert candidate(loginTime = "08:25",logoutTime = "09:50") == 5
    assert candidate(loginTime = "01:00",logoutTime = "01:14") == 0
    assert candidate(loginTime = "12:30",logoutTime = "13:15") == 3
    assert candidate(loginTime = "03:45",logoutTime = "05:10") == 5
    assert candidate(loginTime = "06:30",logoutTime = "06:30") == 0
    assert candidate(loginTime = "17:45",logoutTime = "18:00") == 1
    assert candidate(loginTime = "20:00",logoutTime = "20:14") == 0
    assert candidate(loginTime = "23:59",logoutTime = "00:01") == 0
    assert candidate(loginTime = "07:07",logoutTime = "07:32") == 1
    assert candidate(loginTime = "06:59",logoutTime = "07:01") == 0
    assert candidate(loginTime = "14:23",logoutTime = "14:24") == 0
    assert candidate(loginTime = "12:10",logoutTime = "12:20") == 0
    assert candidate(loginTime = "05:00",logoutTime = "05:00") == 0
    assert candidate(loginTime = "02:30",logoutTime = "02:31") == 0
    assert candidate(loginTime = "20:00",logoutTime = "04:00") == 32
    assert candidate(loginTime = "21:15",logoutTime = "21:45") == 2
    assert candidate(loginTime = "00:45",logoutTime = "01:00") == 1
    assert candidate(loginTime = "21:10",logoutTime = "21:14") == 0
    assert candidate(loginTime = "12:45",logoutTime = "13:45") == 4
    assert candidate(loginTime = "00:10",logoutTime = "01:05") == 3
    assert candidate(loginTime = "14:00",logoutTime = "14:14") == 0
    assert candidate(loginTime = "17:10",logoutTime = "18:55") == 6
    assert candidate(loginTime = "06:30",logoutTime = "07:30") == 4
    assert candidate(loginTime = "00:44",logoutTime = "00:59") == 0
    assert candidate(loginTime = "16:00",logoutTime = "16:01") == 0
    assert candidate(loginTime = "09:00",logoutTime = "21:15") == 49
    assert candidate(loginTime = "15:10",logoutTime = "15:15") == 0
    assert candidate(loginTime = "14:00",logoutTime = "18:30") == 18
    assert candidate(loginTime = "20:00",logoutTime = "21:00") == 4
    assert candidate(loginTime = "11:10",logoutTime = "11:10") == 0
    assert candidate(loginTime = "11:45",logoutTime = "12:44") == 3
    assert candidate(loginTime = "07:45",logoutTime = "08:15") == 2
    assert candidate(loginTime = "10:00",logoutTime = "10:14") == 0
    assert candidate(loginTime = "07:05",logoutTime = "08:10") == 3
    assert candidate(loginTime = "08:45",logoutTime = "09:15") == 2
    assert candidate(loginTime = "16:45",logoutTime = "17:45") == 4
    assert candidate(loginTime = "07:01",logoutTime = "07:14") == 0
    assert candidate(loginTime = "11:46",logoutTime = "12:44") == 2
    assert candidate(loginTime = "09:00",logoutTime = "16:45") == 31
    assert candidate(loginTime = "13:30",logoutTime = "14:00") == 2
    assert candidate(loginTime = "20:00",logoutTime = "20:15") == 1
    assert candidate(loginTime = "00:00",logoutTime = "04:00") == 16
    assert candidate(loginTime = "00:00",logoutTime = "00:15") == 1
    assert candidate(loginTime = "07:07",logoutTime = "07:47") == 2
    assert candidate(loginTime = "13:46",logoutTime = "13:47") == 0
    assert candidate(loginTime = "13:15",logoutTime = "14:15") == 4
    assert candidate(loginTime = "14:16",logoutTime = "15:14") == 2
    assert candidate(loginTime = "21:00",logoutTime = "21:59") == 3
    assert candidate(loginTime = "07:00",logoutTime = "07:14") == 0
    assert candidate(loginTime = "01:01",logoutTime = "24:00") == 91
    assert candidate(loginTime = "17:15",logoutTime = "17:45") == 2
    assert candidate(loginTime = "12:00",logoutTime = "12:00") == 0
    assert candidate(loginTime = "03:45",logoutTime = "04:15") == 2
    assert candidate(loginTime = "04:45",logoutTime = "05:00") == 1
    assert candidate(loginTime = "00:00",logoutTime = "23:45") == 95
    assert candidate(loginTime = "02:20",logoutTime = "02:25") == 0
    assert candidate(loginTime = "09:45",logoutTime = "10:45") == 4
    assert candidate(loginTime = "22:00",logoutTime = "01:30") == 14
    assert candidate(loginTime = "07:07",logoutTime = "07:45") == 2
    assert candidate(loginTime = "22:45",logoutTime = "23:59") == 4
    assert candidate(loginTime = "05:00",logoutTime = "24:00") == 76
    assert candidate(loginTime = "02:30",logoutTime = "03:30") == 4
    assert candidate(loginTime = "13:23",logoutTime = "14:22") == 3
    assert candidate(loginTime = "16:20",logoutTime = "18:55") == 9
    assert candidate(loginTime = "00:00",logoutTime = "00:14") == 0
    assert candidate(loginTime = "08:20",logoutTime = "09:20") == 3
    assert candidate(loginTime = "12:05",logoutTime = "12:20") == 0
    assert candidate(loginTime = "03:33",logoutTime = "04:48") == 4
    assert candidate(loginTime = "23:00",logoutTime = "23:15") == 1
    assert candidate(loginTime = "13:46",logoutTime = "14:14") == 0
    assert candidate(loginTime = "15:00",logoutTime = "15:15") == 1
    assert candidate(loginTime = "13:15",logoutTime = "13:30") == 1
    assert candidate(loginTime = "15:00",logoutTime = "16:00") == 4
    assert candidate(loginTime = "03:00",logoutTime = "03:01") == 0
    assert candidate(loginTime = "09:00",logoutTime = "09:00") == 0
    assert candidate(loginTime = "00:00",logoutTime = "24:00") == 96
    assert candidate(loginTime = "19:40",logoutTime = "20:05") == 1
    assert candidate(loginTime = "16:00",logoutTime = "17:00") == 4
    assert candidate(loginTime = "12:46",logoutTime = "13:14") == 0
    assert candidate(loginTime = "03:45",logoutTime = "03:45") == 0
    assert candidate(loginTime = "00:15",logoutTime = "00:30") == 1
    assert candidate(loginTime = "08:30",logoutTime = "09:00") == 2
    assert candidate(loginTime = "23:15",logoutTime = "00:14") == 3
    assert candidate(loginTime = "05:55",logoutTime = "06:05") == 0
    assert candidate(loginTime = "00:15",logoutTime = "23:59") == 94
    assert candidate(loginTime = "10:00",logoutTime = "10:00") == 0
    assert candidate(loginTime = "01:59",logoutTime = "02:01") == 0
    assert candidate(loginTime = "06:59",logoutTime = "07:00") == 0
    assert candidate(loginTime = "23:40",logoutTime = "00:10") == 1
    assert candidate(loginTime = "09:00",logoutTime = "09:59") == 3
    assert candidate(loginTime = "06:30",logoutTime = "07:00") == 2
    assert candidate(loginTime = "01:45",logoutTime = "02:44") == 3
    assert candidate(loginTime = "18:00",logoutTime = "18:00") == 0
    assert candidate(loginTime = "01:14",logoutTime = "01:46") == 2
    assert candidate(loginTime = "23:55",logoutTime = "00:05") == 0
    assert candidate(loginTime = "09:00",logoutTime = "18:45") == 39
    assert candidate(loginTime = "01:46",logoutTime = "02:14") == 0
    assert candidate(loginTime = "09:10",logoutTime = "09:20") == 0
    assert candidate(loginTime = "09:00",logoutTime = "09:14") == 0
    assert candidate(loginTime = "18:25",logoutTime = "19:50") == 5
    assert candidate(loginTime = "23:00",logoutTime = "23:45") == 3
    assert candidate(loginTime = "07:05",logoutTime = "08:05") == 3
    assert candidate(loginTime = "23:30",logoutTime = "00:30") == 4
    assert candidate(loginTime = "10:00",logoutTime = "24:00") == 56
    assert candidate(loginTime = "06:30",logoutTime = "09:15") == 11
    assert candidate(loginTime = "06:45",logoutTime = "07:00") == 1
    assert candidate(loginTime = "00:30",logoutTime = "00:45") == 1
    assert candidate(loginTime = "21:00",logoutTime = "22:15") == 5
    assert candidate(loginTime = "14:45",logoutTime = "15:00") == 1
    assert candidate(loginTime = "00:05",logoutTime = "00:30") == 1
    assert candidate(loginTime = "11:59",logoutTime = "12:14") == 0
    assert candidate(loginTime = "18:45",logoutTime = "19:10") == 1
    assert candidate(loginTime = "13:30",logoutTime = "16:45") == 13
    assert candidate(loginTime = "09:44",logoutTime = "09:45") == 0
    assert candidate(loginTime = "08:29",logoutTime = "08:40") == 0
    assert candidate(loginTime = "14:30",logoutTime = "16:30") == 8
    assert candidate(loginTime = "01:05",logoutTime = "02:30") == 5
    assert candidate(loginTime = "00:00",logoutTime = "01:00") == 4
    assert candidate(loginTime = "05:15",logoutTime = "05:15") == 0
    assert candidate(loginTime = "13:20",logoutTime = "13:59") == 1
    assert candidate(loginTime = "09:59",logoutTime = "10:00") == 0
    assert candidate(loginTime = "10:10",logoutTime = "11:09") == 3
    assert candidate(loginTime = "01:10",logoutTime = "01:40") == 1
    assert candidate(loginTime = "13:00",logoutTime = "13:14") == 0
    assert candidate(loginTime = "23:01",logoutTime = "23:14") == 0
    assert candidate(loginTime = "19:15",logoutTime = "20:00") == 3


