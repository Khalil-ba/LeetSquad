def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(time = "23:32") == "23:33"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:32") == "23:33": {e}')
    
    total += 1
    try:
        result = candidate(time = "04:59") == "05:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "04:59") == "05:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "21:49") == "22:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "21:49") == "22:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "13:31") == "13:33"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "13:31") == "13:33": {e}')
    
    total += 1
    try:
        result = candidate(time = "22:22") == "22:22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "22:22") == "22:22": {e}')
    
    total += 1
    try:
        result = candidate(time = "00:59") == "05:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "00:59") == "05:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "00:00") == "00:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "00:00") == "00:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "23:59") == "22:22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:59") == "22:22": {e}')
    
    total += 1
    try:
        result = candidate(time = "13:58") == "15:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "13:58") == "15:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "04:56") == "05:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "04:56") == "05:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "09:09") == "00:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "09:09") == "00:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "09:19") == "10:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "09:19") == "10:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "12:34") == "12:41"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "12:34") == "12:41": {e}')
    
    total += 1
    try:
        result = candidate(time = "01:01") == "01:10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "01:01") == "01:10": {e}')
    
    total += 1
    try:
        result = candidate(time = "20:40") == "20:42"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "20:40") == "20:42": {e}')
    
    total += 1
    try:
        result = candidate(time = "20:48") == "22:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "20:48") == "22:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "19:34") == "19:39"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "19:34") == "19:39": {e}')
    
    total += 1
    try:
        result = candidate(time = "01:59") == "05:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "01:59") == "05:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "20:45") == "20:50"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "20:45") == "20:50": {e}')
    
    total += 1
    try:
        result = candidate(time = "11:11") == "11:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "11:11") == "11:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "23:19") == "23:21"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:19") == "23:21": {e}')
    
    total += 1
    try:
        result = candidate(time = "13:59") == "15:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "13:59") == "15:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "10:11") == "11:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "10:11") == "11:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "01:23") == "01:30"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "01:23") == "01:30": {e}')
    
    total += 1
    try:
        result = candidate(time = "22:50") == "22:52"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "22:50") == "22:52": {e}')
    
    total += 1
    try:
        result = candidate(time = "20:09") == "20:20"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "20:09") == "20:20": {e}')
    
    total += 1
    try:
        result = candidate(time = "16:59") == "19:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "16:59") == "19:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "05:00") == "05:05"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "05:00") == "05:05": {e}')
    
    total += 1
    try:
        result = candidate(time = "00:10") == "00:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "00:10") == "00:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "08:44") == "08:48"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "08:44") == "08:48": {e}')
    
    total += 1
    try:
        result = candidate(time = "11:59") == "15:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "11:59") == "15:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "10:00") == "10:01"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "10:00") == "10:01": {e}')
    
    total += 1
    try:
        result = candidate(time = "02:25") == "02:50"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "02:25") == "02:50": {e}')
    
    total += 1
    try:
        result = candidate(time = "08:08") == "00:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "08:08") == "00:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "14:37") == "14:41"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "14:37") == "14:41": {e}')
    
    total += 1
    try:
        result = candidate(time = "21:35") == "21:51"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "21:35") == "21:51": {e}')
    
    total += 1
    try:
        result = candidate(time = "20:19") == "20:20"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "20:19") == "20:20": {e}')
    
    total += 1
    try:
        result = candidate(time = "01:00") == "01:01"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "01:00") == "01:01": {e}')
    
    total += 1
    try:
        result = candidate(time = "10:01") == "10:10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "10:01") == "10:10": {e}')
    
    total += 1
    try:
        result = candidate(time = "21:21") == "21:22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "21:21") == "21:22": {e}')
    
    total += 1
    try:
        result = candidate(time = "18:44") == "18:48"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "18:44") == "18:48": {e}')
    
    total += 1
    try:
        result = candidate(time = "23:10") == "23:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:10") == "23:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "15:15") == "15:51"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "15:15") == "15:51": {e}')
    
    total += 1
    try:
        result = candidate(time = "03:30") == "03:33"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "03:30") == "03:33": {e}')
    
    total += 1
    try:
        result = candidate(time = "13:45") == "13:51"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "13:45") == "13:51": {e}')
    
    total += 1
    try:
        result = candidate(time = "14:41") == "14:44"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "14:41") == "14:44": {e}')
    
    total += 1
    try:
        result = candidate(time = "22:13") == "22:21"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "22:13") == "22:21": {e}')
    
    total += 1
    try:
        result = candidate(time = "03:03") == "03:30"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "03:03") == "03:30": {e}')
    
    total += 1
    try:
        result = candidate(time = "00:01") == "00:10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "00:01") == "00:10": {e}')
    
    total += 1
    try:
        result = candidate(time = "02:59") == "05:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "02:59") == "05:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "15:29") == "15:51"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "15:29") == "15:51": {e}')
    
    total += 1
    try:
        result = candidate(time = "03:23") == "03:30"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "03:23") == "03:30": {e}')
    
    total += 1
    try:
        result = candidate(time = "04:20") == "04:22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "04:20") == "04:22": {e}')
    
    total += 1
    try:
        result = candidate(time = "12:59") == "15:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "12:59") == "15:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "18:81") == "11:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "18:81") == "11:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "16:58") == "18:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "16:58") == "18:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "09:59") == "00:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "09:59") == "00:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "02:34") == "02:40"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "02:34") == "02:40": {e}')
    
    total += 1
    try:
        result = candidate(time = "14:55") == "15:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "14:55") == "15:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "23:58") == "22:22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:58") == "22:22": {e}')
    
    total += 1
    try:
        result = candidate(time = "01:34") == "01:40"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "01:34") == "01:40": {e}')
    
    total += 1
    try:
        result = candidate(time = "08:40") == "08:44"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "08:40") == "08:44": {e}')
    
    total += 1
    try:
        result = candidate(time = "14:44") == "11:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "14:44") == "11:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "04:40") == "04:44"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "04:40") == "04:44": {e}')
    
    total += 1
    try:
        result = candidate(time = "17:58") == "18:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "17:58") == "18:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "15:49") == "15:51"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "15:49") == "15:51": {e}')
    
    total += 1
    try:
        result = candidate(time = "20:00") == "20:02"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "20:00") == "20:02": {e}')
    
    total += 1
    try:
        result = candidate(time = "21:59") == "22:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "21:59") == "22:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "06:07") == "07:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "06:07") == "07:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "00:58") == "05:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "00:58") == "05:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "09:41") == "09:44"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "09:41") == "09:44": {e}')
    
    total += 1
    try:
        result = candidate(time = "21:07") == "21:10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "21:07") == "21:10": {e}')
    
    total += 1
    try:
        result = candidate(time = "05:55") == "00:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "05:55") == "00:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "16:16") == "11:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "16:16") == "11:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "07:77") == "00:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "07:77") == "00:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "21:31") == "21:32"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "21:31") == "21:32": {e}')
    
    total += 1
    try:
        result = candidate(time = "09:45") == "09:49"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "09:45") == "09:49": {e}')
    
    total += 1
    try:
        result = candidate(time = "13:39") == "19:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "13:39") == "19:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "12:37") == "13:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "12:37") == "13:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "13:43") == "13:44"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "13:43") == "13:44": {e}')
    
    total += 1
    try:
        result = candidate(time = "17:71") == "11:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "17:71") == "11:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "15:55") == "11:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "15:55") == "11:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "02:45") == "02:50"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "02:45") == "02:50": {e}')
    
    total += 1
    try:
        result = candidate(time = "18:18") == "11:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "18:18") == "11:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "15:51") == "15:55"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "15:51") == "15:55": {e}')
    
    total += 1
    try:
        result = candidate(time = "20:20") == "20:22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "20:20") == "20:22": {e}')
    
    total += 1
    try:
        result = candidate(time = "22:55") == "22:22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "22:55") == "22:22": {e}')
    
    total += 1
    try:
        result = candidate(time = "04:04") == "04:40"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "04:04") == "04:40": {e}')
    
    total += 1
    try:
        result = candidate(time = "06:06") == "00:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "06:06") == "00:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "02:02") == "02:20"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "02:02") == "02:20": {e}')
    
    total += 1
    try:
        result = candidate(time = "09:50") == "09:55"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "09:50") == "09:55": {e}')
    
    total += 1
    try:
        result = candidate(time = "23:23") == "23:32"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:23") == "23:32": {e}')
    
    total += 1
    try:
        result = candidate(time = "09:01") == "09:09"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "09:01") == "09:09": {e}')
    
    total += 1
    try:
        result = candidate(time = "08:88") == "00:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "08:88") == "00:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "23:00") == "23:02"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:00") == "23:02": {e}')
    
    total += 1
    try:
        result = candidate(time = "21:09") == "21:10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "21:09") == "21:10": {e}')
    
    total += 1
    try:
        result = candidate(time = "17:17") == "11:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "17:17") == "11:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "07:08") == "08:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "07:08") == "08:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "23:45") == "23:52"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:45") == "23:52": {e}')
    
    total += 1
    try:
        result = candidate(time = "14:29") == "14:41"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "14:29") == "14:41": {e}')
    
    total += 1
    try:
        result = candidate(time = "11:09") == "11:10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "11:09") == "11:10": {e}')
    
    total += 1
    try:
        result = candidate(time = "21:12") == "21:21"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "21:12") == "21:21": {e}')
    
    total += 1
    try:
        result = candidate(time = "07:07") == "00:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "07:07") == "00:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "23:57") == "22:22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:57") == "22:22": {e}')
    
    total += 1
    try:
        result = candidate(time = "20:05") == "20:20"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "20:05") == "20:20": {e}')
    
    total += 1
    try:
        result = candidate(time = "20:31") == "20:32"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "20:31") == "20:32": {e}')
    
    total += 1
    try:
        result = candidate(time = "16:45") == "16:46"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "16:45") == "16:46": {e}')
    
    total += 1
    try:
        result = candidate(time = "06:59") == "09:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "06:59") == "09:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "14:59") == "15:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "14:59") == "15:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "10:59") == "11:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "10:59") == "11:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "11:10") == "11:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "11:10") == "11:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "01:11") == "10:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "01:11") == "10:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "16:39") == "19:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "16:39") == "19:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "04:45") == "04:50"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "04:45") == "04:50": {e}')
    
    total += 1
    try:
        result = candidate(time = "17:59") == "19:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "17:59") == "19:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "05:05") == "05:50"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "05:05") == "05:50": {e}')
    
    total += 1
    try:
        result = candidate(time = "06:27") == "07:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "06:27") == "07:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "22:59") == "22:22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "22:59") == "22:22": {e}')
    
    total += 1
    try:
        result = candidate(time = "22:23") == "22:32"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "22:23") == "22:32": {e}')
    
    total += 1
    try:
        result = candidate(time = "19:09") == "19:10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "19:09") == "19:10": {e}')
    
    total += 1
    try:
        result = candidate(time = "18:00") == "18:01"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "18:00") == "18:01": {e}')
    
    total += 1
    try:
        result = candidate(time = "14:14") == "14:41"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "14:14") == "14:41": {e}')
    
    total += 1
    try:
        result = candidate(time = "09:99") == "00:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "09:99") == "00:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "19:59") == "11:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "19:59") == "11:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "19:58") == "19:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "19:58") == "19:59": {e}')
    
    total += 1
    try:
        result = candidate(time = "04:44") == "00:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "04:44") == "00:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "08:59") == "09:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "08:59") == "09:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "03:33") == "00:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "03:33") == "00:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "20:59") == "22:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "20:59") == "22:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "05:59") == "09:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "05:59") == "09:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "10:55") == "11:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "10:55") == "11:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "06:66") == "00:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "06:66") == "00:00": {e}')
    
    total += 1
    try:
        result = candidate(time = "10:10") == "10:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "10:10") == "10:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "19:19") == "11:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "19:19") == "11:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "05:35") == "05:50"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "05:35") == "05:50": {e}')
    
    total += 1
    try:
        result = candidate(time = "23:49") == "22:22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "23:49") == "22:22": {e}')
    
    total += 1
    try:
        result = candidate(time = "18:59") == "19:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "18:59") == "19:11": {e}')
    
    total += 1
    try:
        result = candidate(time = "13:32") == "13:33"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "13:32") == "13:33": {e}')
    
    total += 1
    try:
        result = candidate(time = "10:09") == "10:10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = "10:09") == "10:10": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(time = "23:32") == "23:33"
    assert candidate(time = "04:59") == "05:00"
    assert candidate(time = "21:49") == "22:11"
    assert candidate(time = "13:31") == "13:33"
    assert candidate(time = "22:22") == "22:22"
    assert candidate(time = "00:59") == "05:00"
    assert candidate(time = "00:00") == "00:00"
    assert candidate(time = "23:59") == "22:22"
    assert candidate(time = "13:58") == "15:11"
    assert candidate(time = "04:56") == "05:00"
    assert candidate(time = "09:09") == "00:00"
    assert candidate(time = "09:19") == "10:00"
    assert candidate(time = "12:34") == "12:41"
    assert candidate(time = "01:01") == "01:10"
    assert candidate(time = "20:40") == "20:42"
    assert candidate(time = "20:48") == "22:00"
    assert candidate(time = "19:34") == "19:39"
    assert candidate(time = "01:59") == "05:00"
    assert candidate(time = "20:45") == "20:50"
    assert candidate(time = "11:11") == "11:11"
    assert candidate(time = "23:19") == "23:21"
    assert candidate(time = "13:59") == "15:11"
    assert candidate(time = "10:11") == "11:00"
    assert candidate(time = "01:23") == "01:30"
    assert candidate(time = "22:50") == "22:52"
    assert candidate(time = "20:09") == "20:20"
    assert candidate(time = "16:59") == "19:11"
    assert candidate(time = "05:00") == "05:05"
    assert candidate(time = "00:10") == "00:11"
    assert candidate(time = "08:44") == "08:48"
    assert candidate(time = "11:59") == "15:11"
    assert candidate(time = "10:00") == "10:01"
    assert candidate(time = "02:25") == "02:50"
    assert candidate(time = "08:08") == "00:00"
    assert candidate(time = "14:37") == "14:41"
    assert candidate(time = "21:35") == "21:51"
    assert candidate(time = "20:19") == "20:20"
    assert candidate(time = "01:00") == "01:01"
    assert candidate(time = "10:01") == "10:10"
    assert candidate(time = "21:21") == "21:22"
    assert candidate(time = "18:44") == "18:48"
    assert candidate(time = "23:10") == "23:11"
    assert candidate(time = "15:15") == "15:51"
    assert candidate(time = "03:30") == "03:33"
    assert candidate(time = "13:45") == "13:51"
    assert candidate(time = "14:41") == "14:44"
    assert candidate(time = "22:13") == "22:21"
    assert candidate(time = "03:03") == "03:30"
    assert candidate(time = "00:01") == "00:10"
    assert candidate(time = "02:59") == "05:00"
    assert candidate(time = "15:29") == "15:51"
    assert candidate(time = "03:23") == "03:30"
    assert candidate(time = "04:20") == "04:22"
    assert candidate(time = "12:59") == "15:11"
    assert candidate(time = "18:81") == "11:11"
    assert candidate(time = "16:58") == "18:11"
    assert candidate(time = "09:59") == "00:00"
    assert candidate(time = "02:34") == "02:40"
    assert candidate(time = "14:55") == "15:11"
    assert candidate(time = "23:58") == "22:22"
    assert candidate(time = "01:34") == "01:40"
    assert candidate(time = "08:40") == "08:44"
    assert candidate(time = "14:44") == "11:11"
    assert candidate(time = "04:40") == "04:44"
    assert candidate(time = "17:58") == "18:11"
    assert candidate(time = "15:49") == "15:51"
    assert candidate(time = "20:00") == "20:02"
    assert candidate(time = "21:59") == "22:11"
    assert candidate(time = "06:07") == "07:00"
    assert candidate(time = "00:58") == "05:00"
    assert candidate(time = "09:41") == "09:44"
    assert candidate(time = "21:07") == "21:10"
    assert candidate(time = "05:55") == "00:00"
    assert candidate(time = "16:16") == "11:11"
    assert candidate(time = "07:77") == "00:00"
    assert candidate(time = "21:31") == "21:32"
    assert candidate(time = "09:45") == "09:49"
    assert candidate(time = "13:39") == "19:11"
    assert candidate(time = "12:37") == "13:11"
    assert candidate(time = "13:43") == "13:44"
    assert candidate(time = "17:71") == "11:11"
    assert candidate(time = "15:55") == "11:11"
    assert candidate(time = "02:45") == "02:50"
    assert candidate(time = "18:18") == "11:11"
    assert candidate(time = "15:51") == "15:55"
    assert candidate(time = "20:20") == "20:22"
    assert candidate(time = "22:55") == "22:22"
    assert candidate(time = "04:04") == "04:40"
    assert candidate(time = "06:06") == "00:00"
    assert candidate(time = "02:02") == "02:20"
    assert candidate(time = "09:50") == "09:55"
    assert candidate(time = "23:23") == "23:32"
    assert candidate(time = "09:01") == "09:09"
    assert candidate(time = "08:88") == "00:00"
    assert candidate(time = "23:00") == "23:02"
    assert candidate(time = "21:09") == "21:10"
    assert candidate(time = "17:17") == "11:11"
    assert candidate(time = "07:08") == "08:00"
    assert candidate(time = "23:45") == "23:52"
    assert candidate(time = "14:29") == "14:41"
    assert candidate(time = "11:09") == "11:10"
    assert candidate(time = "21:12") == "21:21"
    assert candidate(time = "07:07") == "00:00"
    assert candidate(time = "23:57") == "22:22"
    assert candidate(time = "20:05") == "20:20"
    assert candidate(time = "20:31") == "20:32"
    assert candidate(time = "16:45") == "16:46"
    assert candidate(time = "06:59") == "09:00"
    assert candidate(time = "14:59") == "15:11"
    assert candidate(time = "10:59") == "11:00"
    assert candidate(time = "11:10") == "11:11"
    assert candidate(time = "01:11") == "10:00"
    assert candidate(time = "16:39") == "19:11"
    assert candidate(time = "04:45") == "04:50"
    assert candidate(time = "17:59") == "19:11"
    assert candidate(time = "05:05") == "05:50"
    assert candidate(time = "06:27") == "07:00"
    assert candidate(time = "22:59") == "22:22"
    assert candidate(time = "22:23") == "22:32"
    assert candidate(time = "19:09") == "19:10"
    assert candidate(time = "18:00") == "18:01"
    assert candidate(time = "14:14") == "14:41"
    assert candidate(time = "09:99") == "00:00"
    assert candidate(time = "19:59") == "11:11"
    assert candidate(time = "19:58") == "19:59"
    assert candidate(time = "04:44") == "00:00"
    assert candidate(time = "08:59") == "09:00"
    assert candidate(time = "03:33") == "00:00"
    assert candidate(time = "20:59") == "22:00"
    assert candidate(time = "05:59") == "09:00"
    assert candidate(time = "10:55") == "11:00"
    assert candidate(time = "06:66") == "00:00"
    assert candidate(time = "10:10") == "10:11"
    assert candidate(time = "19:19") == "11:11"
    assert candidate(time = "05:35") == "05:50"
    assert candidate(time = "23:49") == "22:22"
    assert candidate(time = "18:59") == "19:11"
    assert candidate(time = "13:32") == "13:33"
    assert candidate(time = "10:09") == "10:10"


