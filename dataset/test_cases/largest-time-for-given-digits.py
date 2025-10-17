def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [2, 9, 0, 3]) == "23:09"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 9, 0, 3]) == "23:09": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 9, 6, 0]) == "19:06"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 9, 6, 0]) == "19:06": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 2, 6, 6]) == "06:26"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 2, 6, 6]) == "06:26": {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 2, 4, 4]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 2, 4, 4]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 9, 6]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 9, 6]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 5, 9]) == "23:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 5, 9]) == "23:59": {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 2, 0, 0]) == "20:40"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 2, 0, 0]) == "20:40": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 9, 9, 9]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 9, 9, 9]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 1, 6, 0]) == "19:06"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 1, 6, 0]) == "19:06": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 9, 6, 3]) == "19:36"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 9, 6, 3]) == "19:36": {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 0, 6, 6]) == "06:26"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 0, 6, 6]) == "06:26": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4]) == "23:41"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4]) == "23:41": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 4, 0, 0]) == "04:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 4, 0, 0]) == "04:00": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 5, 9]) == "19:50"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 5, 9]) == "19:50": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 1, 0]) == "10:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 1, 0]) == "10:00": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 9, 5, 7]) == "09:57"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 9, 5, 7]) == "09:57": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0]) == "00:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0]) == "00:00": {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 9, 5, 6]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 9, 5, 6]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 9, 6, 8]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 9, 6, 8]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 6, 3, 2]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 6, 3, 2]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 0, 7, 0]) == "07:50"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 0, 7, 0]) == "07:50": {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 0, 7, 0]) == "07:30"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 0, 7, 0]) == "07:30": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7]) == "17:53"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7]) == "17:53": {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 9, 9, 0]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 9, 9, 0]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 0, 4, 3]) == "09:43"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 0, 4, 3]) == "09:43": {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 0, 8, 7]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 0, 8, 7]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 9, 8, 8]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 9, 8, 8]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 8, 9]) == "19:28"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 8, 9]) == "19:28": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 3]) == "23:31"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 3]) == "23:31": {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 2, 6, 9]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 2, 6, 9]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 3, 4]) == "23:42"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 3, 4]) == "23:42": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 3, 3]) == "23:32"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 3, 3]) == "23:32": {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 4, 9, 1]) == "19:43"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 4, 9, 1]) == "19:43": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 9, 3, 4]) == "23:49"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 9, 3, 4]) == "23:49": {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 0, 9, 2]) == "20:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 0, 9, 2]) == "20:59": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 9, 5, 1]) == "21:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 9, 5, 1]) == "21:59": {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 6, 6, 6]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 6, 6, 6]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 0, 6]) == "20:46"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 0, 6]) == "20:46": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 2, 2]) == "22:22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 2, 2]) == "22:22": {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 5, 9, 8]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 5, 9, 8]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 9, 1, 0]) == "19:30"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 9, 1, 0]) == "19:30": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 4, 4]) == "22:44"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 4, 4]) == "22:44": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3]) == "23:10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3]) == "23:10": {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 1, 4, 0]) == "14:40"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 1, 4, 0]) == "14:40": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1]) == "11:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1]) == "11:11": {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 4, 2, 1]) == "21:48"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 4, 2, 1]) == "21:48": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 4, 2, 3]) == "23:40"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 4, 2, 3]) == "23:40": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 9, 0, 5]) == "20:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 9, 0, 5]) == "20:59": {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 8, 4, 1]) == "18:43"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 8, 4, 1]) == "18:43": {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 8, 4, 7]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 8, 4, 7]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 0, 3]) == "23:30"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 0, 3]) == "23:30": {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 5, 0, 7]) == "07:53"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 5, 0, 7]) == "07:53": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 0, 0]) == "23:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 0, 0]) == "23:00": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 0, 0]) == "20:40"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 0, 0]) == "20:40": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 5, 9]) == "21:59"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 5, 9]) == "21:59": {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 9, 4, 0]) == "09:43"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 9, 4, 0]) == "09:43": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 9, 9]) == "19:19"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 9, 9]) == "19:19": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 8, 8, 8]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 8, 8, 8]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 8, 4, 6]) == "18:46"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 8, 4, 6]) == "18:46": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 7, 6]) == "17:06"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 7, 6]) == "17:06": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 0, 6, 4]) == "20:46"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 0, 6, 4]) == "20:46": {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 8, 5, 8]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 8, 5, 8]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 4, 5]) == "23:54"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 4, 5]) == "23:54": {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 7, 7, 9]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 7, 7, 9]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 2]) == "21:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 2]) == "21:11": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 7, 6, 0]) == "07:26"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 7, 6, 0]) == "07:26": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 2, 6, 4]) == "20:46"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 2, 6, 4]) == "20:46": {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 1, 4, 2]) == "21:44"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 1, 4, 2]) == "21:44": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 1, 2]) == "21:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 1, 2]) == "21:00": {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 9, 5, 9]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 9, 5, 9]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 6, 8]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 6, 8]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 7, 6, 6]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 7, 6, 6]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 1, 3, 5]) == "15:43"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 1, 3, 5]) == "15:43": {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 5, 9, 0]) == "09:58"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 5, 9, 0]) == "09:58": {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 6, 4, 0]) == "07:46"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 6, 4, 0]) == "07:46": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 2, 3]) == "23:32"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 2, 3]) == "23:32": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 9, 0, 9]) == "09:09"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 9, 0, 9]) == "09:09": {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 9, 5, 2]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 9, 5, 2]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 0, 0, 0]) == "10:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 0, 0, 0]) == "10:00": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 3, 5, 5]) == "05:53"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 3, 5, 5]) == "05:53": {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 8, 4, 5]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 8, 4, 5]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 5, 9, 6]) == "09:56"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 5, 9, 6]) == "09:56": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 1]) == "10:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 1]) == "10:00": {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 8, 5, 9]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 8, 5, 9]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1]) == "11:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1]) == "11:11": {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 8, 8, 8]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 8, 8, 8]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 8, 7, 7]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 8, 7, 7]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 8, 5, 4]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 8, 5, 4]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 6, 9, 0]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 6, 9, 0]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 2, 2]) == "22:22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 2, 2]) == "22:22": {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 8, 6, 1]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 8, 6, 1]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 3, 6, 0]) == "06:53"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 3, 6, 0]) == "06:53": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 3, 5, 9]) == "09:53"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 3, 5, 9]) == "09:53": {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 0, 7, 0]) == "07:30"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 0, 7, 0]) == "07:30": {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 9, 6, 4]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 9, 6, 4]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 9, 3, 5]) == "09:53"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 9, 3, 5]) == "09:53": {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 7, 7, 7]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 7, 7, 7]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 3, 2]) == "23:32"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 3, 2]) == "23:32": {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 9, 6, 3]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 9, 6, 3]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 9, 1, 1]) == "19:10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 9, 1, 1]) == "19:10": {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 0, 5, 2]) == "20:55"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 0, 5, 2]) == "20:55": {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 5, 5, 9]) == "09:55"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 5, 5, 9]) == "09:55": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 8, 9]) == "19:28"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 8, 9]) == "19:28": {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 1, 1]) == "22:11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 1, 1]) == "22:11": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 0]) == "23:10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 0]) == "23:10": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 4, 0, 0]) == "04:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 4, 0, 0]) == "04:00": {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 0, 1]) == "13:30"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 0, 1]) == "13:30": {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 1, 4, 2]) == "21:46"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 1, 4, 2]) == "21:46": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 4, 4, 5]) == "05:44"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 4, 4, 5]) == "05:44": {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 0, 0, 0]) == "09:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 0, 0, 0]) == "09:00": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 1, 1]) == "11:00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 1, 1]) == "11:00": {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 9, 0]) == "21:09"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 9, 0]) == "21:09": {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 4, 5]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 4, 5]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 9, 9, 9]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 9, 9, 9]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 2, 8, 9]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 2, 8, 9]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 9, 9, 9]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 9, 9, 9]) == "": {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 7, 7]) == "17:07"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 7, 7]) == "17:07": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [2, 9, 0, 3]) == "23:09"
    assert candidate(arr = [1, 9, 6, 0]) == "19:06"
    assert candidate(arr = [0, 2, 6, 6]) == "06:26"
    assert candidate(arr = [4, 2, 4, 4]) == ""
    assert candidate(arr = [2, 2, 9, 6]) == ""
    assert candidate(arr = [2, 3, 5, 9]) == "23:59"
    assert candidate(arr = [4, 2, 0, 0]) == "20:40"
    assert candidate(arr = [1, 9, 9, 9]) == ""
    assert candidate(arr = [9, 1, 6, 0]) == "19:06"
    assert candidate(arr = [1, 9, 6, 3]) == "19:36"
    assert candidate(arr = [5, 5, 5, 5]) == ""
    assert candidate(arr = [2, 0, 6, 6]) == "06:26"
    assert candidate(arr = [1, 2, 3, 4]) == "23:41"
    assert candidate(arr = [0, 4, 0, 0]) == "04:00"
    assert candidate(arr = [0, 1, 5, 9]) == "19:50"
    assert candidate(arr = [0, 0, 1, 0]) == "10:00"
    assert candidate(arr = [0, 9, 5, 7]) == "09:57"
    assert candidate(arr = [0, 0, 0, 0]) == "00:00"
    assert candidate(arr = [3, 9, 5, 6]) == ""
    assert candidate(arr = [1, 9, 6, 8]) == ""
    assert candidate(arr = [9, 6, 3, 2]) == ""
    assert candidate(arr = [5, 0, 7, 0]) == "07:50"
    assert candidate(arr = [3, 0, 7, 0]) == "07:30"
    assert candidate(arr = [1, 3, 5, 7]) == "17:53"
    assert candidate(arr = [9, 9, 9, 0]) == ""
    assert candidate(arr = [9, 0, 4, 3]) == "09:43"
    assert candidate(arr = [9, 0, 8, 7]) == ""
    assert candidate(arr = [9, 9, 8, 8]) == ""
    assert candidate(arr = [1, 2, 8, 9]) == "19:28"
    assert candidate(arr = [1, 2, 3, 3]) == "23:31"
    assert candidate(arr = [4, 2, 6, 9]) == ""
    assert candidate(arr = [2, 2, 3, 4]) == "23:42"
    assert candidate(arr = [2, 2, 3, 3]) == "23:32"
    assert candidate(arr = [3, 4, 9, 1]) == "19:43"
    assert candidate(arr = [2, 9, 3, 4]) == "23:49"
    assert candidate(arr = [5, 0, 9, 2]) == "20:59"
    assert candidate(arr = [2, 9, 5, 1]) == "21:59"
    assert candidate(arr = [6, 6, 6, 6]) == ""
    assert candidate(arr = [2, 4, 0, 6]) == "20:46"
    assert candidate(arr = [2, 2, 2, 2]) == "22:22"
    assert candidate(arr = [4, 5, 9, 8]) == ""
    assert candidate(arr = [3, 9, 1, 0]) == "19:30"
    assert candidate(arr = [2, 2, 4, 4]) == "22:44"
    assert candidate(arr = [0, 1, 2, 3]) == "23:10"
    assert candidate(arr = [4, 1, 4, 0]) == "14:40"
    assert candidate(arr = [1, 1, 1, 1]) == "11:11"
    assert candidate(arr = [8, 4, 2, 1]) == "21:48"
    assert candidate(arr = [0, 4, 2, 3]) == "23:40"
    assert candidate(arr = [2, 9, 0, 5]) == "20:59"
    assert candidate(arr = [3, 8, 4, 1]) == "18:43"
    assert candidate(arr = [3, 8, 4, 7]) == ""
    assert candidate(arr = [2, 3, 0, 3]) == "23:30"
    assert candidate(arr = [3, 5, 0, 7]) == "07:53"
    assert candidate(arr = [2, 3, 0, 0]) == "23:00"
    assert candidate(arr = [2, 4, 0, 0]) == "20:40"
    assert candidate(arr = [1, 2, 5, 9]) == "21:59"
    assert candidate(arr = [3, 9, 4, 0]) == "09:43"
    assert candidate(arr = [1, 1, 9, 9]) == "19:19"
    assert candidate(arr = [1, 8, 8, 8]) == ""
    assert candidate(arr = [1, 8, 4, 6]) == "18:46"
    assert candidate(arr = [1, 0, 7, 6]) == "17:06"
    assert candidate(arr = [2, 0, 6, 4]) == "20:46"
    assert candidate(arr = [5, 8, 5, 8]) == ""
    assert candidate(arr = [2, 3, 4, 5]) == "23:54"
    assert candidate(arr = [8, 7, 7, 9]) == ""
    assert candidate(arr = [1, 1, 1, 2]) == "21:11"
    assert candidate(arr = [2, 7, 6, 0]) == "07:26"
    assert candidate(arr = [0, 2, 6, 4]) == "20:46"
    assert candidate(arr = [4, 1, 4, 2]) == "21:44"
    assert candidate(arr = [0, 0, 1, 2]) == "21:00"
    assert candidate(arr = [5, 9, 5, 9]) == ""
    assert candidate(arr = [2, 3, 6, 8]) == ""
    assert candidate(arr = [0, 7, 6, 6]) == ""
    assert candidate(arr = [4, 1, 3, 5]) == "15:43"
    assert candidate(arr = [8, 5, 9, 0]) == "09:58"
    assert candidate(arr = [7, 6, 4, 0]) == "07:46"
    assert candidate(arr = [2, 3, 2, 3]) == "23:32"
    assert candidate(arr = [0, 9, 0, 9]) == "09:09"
    assert candidate(arr = [7, 9, 5, 2]) == ""
    assert candidate(arr = [1, 0, 0, 0]) == "10:00"
    assert candidate(arr = [0, 3, 5, 5]) == "05:53"
    assert candidate(arr = [3, 8, 4, 5]) == ""
    assert candidate(arr = [0, 5, 9, 6]) == "09:56"
    assert candidate(arr = [0, 0, 0, 1]) == "10:00"
    assert candidate(arr = [5, 8, 5, 9]) == ""
    assert candidate(arr = [1, 1, 1, 1]) == "11:11"
    assert candidate(arr = [8, 8, 8, 8]) == ""
    assert candidate(arr = [2, 4, 6, 8]) == ""
    assert candidate(arr = [3, 3, 3, 3]) == ""
    assert candidate(arr = [1, 8, 7, 7]) == ""
    assert candidate(arr = [6, 8, 5, 4]) == ""
    assert candidate(arr = [6, 6, 9, 0]) == ""
    assert candidate(arr = [2, 2, 2, 2]) == "22:22"
    assert candidate(arr = [7, 8, 6, 1]) == ""
    assert candidate(arr = [5, 3, 6, 0]) == "06:53"
    assert candidate(arr = [0, 3, 5, 9]) == "09:53"
    assert candidate(arr = [3, 0, 7, 0]) == "07:30"
    assert candidate(arr = [5, 9, 6, 4]) == ""
    assert candidate(arr = [0, 9, 3, 5]) == "09:53"
    assert candidate(arr = [7, 7, 7, 7]) == ""
    assert candidate(arr = [2, 3, 3, 2]) == "23:32"
    assert candidate(arr = [5, 9, 6, 3]) == ""
    assert candidate(arr = [0, 9, 1, 1]) == "19:10"
    assert candidate(arr = [5, 0, 5, 2]) == "20:55"
    assert candidate(arr = [3, 3, 3, 3]) == ""
    assert candidate(arr = [0, 5, 5, 9]) == "09:55"
    assert candidate(arr = [1, 2, 8, 9]) == "19:28"
    assert candidate(arr = [2, 2, 1, 1]) == "22:11"
    assert candidate(arr = [1, 2, 3, 0]) == "23:10"
    assert candidate(arr = [0, 4, 0, 0]) == "04:00"
    assert candidate(arr = [3, 3, 0, 1]) == "13:30"
    assert candidate(arr = [6, 1, 4, 2]) == "21:46"
    assert candidate(arr = [0, 4, 4, 5]) == "05:44"
    assert candidate(arr = [9, 0, 0, 0]) == "09:00"
    assert candidate(arr = [0, 0, 1, 1]) == "11:00"
    assert candidate(arr = [5, 6, 7, 8]) == ""
    assert candidate(arr = [1, 2, 9, 0]) == "21:09"
    assert candidate(arr = [3, 3, 4, 5]) == ""
    assert candidate(arr = [9, 9, 9, 9]) == ""
    assert candidate(arr = [5, 2, 8, 9]) == ""
    assert candidate(arr = [9, 8, 7, 6]) == ""
    assert candidate(arr = [9, 9, 9, 9]) == ""
    assert candidate(arr = [0, 1, 7, 7]) == "17:07"


