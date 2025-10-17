def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arriveAlice = "03-10",leaveAlice = "05-20",arriveBob = "04-01",leaveBob = "04-30") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "03-10",leaveAlice = "05-20",arriveBob = "04-01",leaveBob = "04-30") == 30: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "06-15",leaveAlice = "06-20",arriveBob = "06-18",leaveBob = "06-25") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "06-15",leaveAlice = "06-20",arriveBob = "06-18",leaveBob = "06-25") == 3: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "10-01",leaveAlice = "10-31",arriveBob = "11-01",leaveBob = "12-31") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "10-01",leaveAlice = "10-31",arriveBob = "11-01",leaveBob = "12-31") == 0: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "01-01",leaveAlice = "12-31",arriveBob = "01-01",leaveBob = "12-31") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "01-01",leaveAlice = "12-31",arriveBob = "01-01",leaveBob = "12-31") == 365: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "08-15",leaveAlice = "08-18",arriveBob = "08-16",leaveBob = "08-19") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "08-15",leaveAlice = "08-18",arriveBob = "08-16",leaveBob = "08-19") == 3: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "12-20",leaveAlice = "12-31",arriveBob = "12-25",leaveBob = "12-30") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "12-20",leaveAlice = "12-31",arriveBob = "12-25",leaveBob = "12-30") == 6: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "05-24",leaveAlice = "07-24",arriveBob = "07-25",leaveBob = "08-25") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "05-24",leaveAlice = "07-24",arriveBob = "07-25",leaveBob = "08-25") == 0: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "07-20",leaveAlice = "08-15",arriveBob = "07-25",leaveBob = "08-10") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "07-20",leaveAlice = "08-15",arriveBob = "07-25",leaveBob = "08-10") == 17: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "07-01",leaveAlice = "08-01",arriveBob = "07-15",leaveBob = "07-30") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "07-01",leaveAlice = "08-01",arriveBob = "07-15",leaveBob = "07-30") == 16: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "07-10",leaveAlice = "07-20",arriveBob = "07-15",leaveBob = "07-25") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "07-10",leaveAlice = "07-20",arriveBob = "07-15",leaveBob = "07-25") == 6: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "01-01",leaveAlice = "01-31",arriveBob = "01-01",leaveBob = "01-31") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "01-01",leaveAlice = "01-31",arriveBob = "01-01",leaveBob = "01-31") == 31: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "03-10",leaveAlice = "03-10",arriveBob = "03-10",leaveBob = "03-10") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "03-10",leaveAlice = "03-10",arriveBob = "03-10",leaveBob = "03-10") == 1: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "06-15",leaveAlice = "06-15",arriveBob = "06-15",leaveBob = "06-15") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "06-15",leaveAlice = "06-15",arriveBob = "06-15",leaveBob = "06-15") == 1: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "01-01",leaveAlice = "01-31",arriveBob = "01-15",leaveBob = "01-20") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "01-01",leaveAlice = "01-31",arriveBob = "01-15",leaveBob = "01-20") == 6: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "03-14",leaveAlice = "03-14",arriveBob = "03-14",leaveBob = "03-14") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "03-14",leaveAlice = "03-14",arriveBob = "03-14",leaveBob = "03-14") == 1: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "06-01",leaveAlice = "06-30",arriveBob = "05-25",leaveBob = "06-10") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "06-01",leaveAlice = "06-30",arriveBob = "05-25",leaveBob = "06-10") == 10: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "10-01",leaveAlice = "10-20",arriveBob = "09-25",leaveBob = "10-25") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "10-01",leaveAlice = "10-20",arriveBob = "09-25",leaveBob = "10-25") == 20: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "11-15",leaveAlice = "12-31",arriveBob = "12-01",leaveBob = "12-31") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "11-15",leaveAlice = "12-31",arriveBob = "12-01",leaveBob = "12-31") == 31: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "04-10",leaveAlice = "06-10",arriveBob = "05-01",leaveBob = "06-30") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "04-10",leaveAlice = "06-10",arriveBob = "05-01",leaveBob = "06-30") == 41: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "01-10",leaveAlice = "02-20",arriveBob = "02-15",leaveBob = "03-25") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "01-10",leaveAlice = "02-20",arriveBob = "02-15",leaveBob = "03-25") == 6: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "09-15",leaveAlice = "09-15",arriveBob = "09-15",leaveBob = "09-15") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "09-15",leaveAlice = "09-15",arriveBob = "09-15",leaveBob = "09-15") == 1: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "12-20",leaveAlice = "12-31",arriveBob = "12-15",leaveBob = "01-10") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "12-20",leaveAlice = "12-31",arriveBob = "12-15",leaveBob = "01-10") == 0: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "05-05",leaveAlice = "07-05",arriveBob = "05-05",leaveBob = "05-05") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "05-05",leaveAlice = "07-05",arriveBob = "05-05",leaveBob = "05-05") == 1: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "02-28",leaveAlice = "03-15",arriveBob = "03-01",leaveBob = "03-31") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "02-28",leaveAlice = "03-15",arriveBob = "03-01",leaveBob = "03-31") == 15: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "08-15",leaveAlice = "09-15",arriveBob = "09-15",leaveBob = "10-15") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "08-15",leaveAlice = "09-15",arriveBob = "09-15",leaveBob = "10-15") == 1: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "03-05",leaveAlice = "03-20",arriveBob = "03-15",leaveBob = "03-25") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "03-05",leaveAlice = "03-20",arriveBob = "03-15",leaveBob = "03-25") == 6: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "03-15",leaveAlice = "03-20",arriveBob = "03-10",leaveBob = "03-14") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "03-15",leaveAlice = "03-20",arriveBob = "03-10",leaveBob = "03-14") == 0: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "06-01",leaveAlice = "06-30",arriveBob = "06-15",leaveBob = "06-25") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "06-01",leaveAlice = "06-30",arriveBob = "06-15",leaveBob = "06-25") == 11: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "02-28",leaveAlice = "03-10",arriveBob = "03-01",leaveBob = "03-15") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "02-28",leaveAlice = "03-10",arriveBob = "03-01",leaveBob = "03-15") == 10: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "01-15",leaveAlice = "01-15",arriveBob = "01-15",leaveBob = "01-15") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "01-15",leaveAlice = "01-15",arriveBob = "01-15",leaveBob = "01-15") == 1: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "01-01",leaveAlice = "01-31",arriveBob = "01-15",leaveBob = "02-14") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "01-01",leaveAlice = "01-31",arriveBob = "01-15",leaveBob = "02-14") == 17: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "12-15",leaveAlice = "12-15",arriveBob = "12-16",leaveBob = "12-16") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "12-15",leaveAlice = "12-15",arriveBob = "12-16",leaveBob = "12-16") == 0: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "11-11",leaveAlice = "11-11",arriveBob = "11-11",leaveBob = "11-11") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "11-11",leaveAlice = "11-11",arriveBob = "11-11",leaveBob = "11-11") == 1: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "11-20",leaveAlice = "12-15",arriveBob = "11-25",leaveBob = "12-25") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "11-20",leaveAlice = "12-15",arriveBob = "11-25",leaveBob = "12-25") == 21: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "11-11",leaveAlice = "11-25",arriveBob = "11-20",leaveBob = "12-10") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "11-11",leaveAlice = "11-25",arriveBob = "11-20",leaveBob = "12-10") == 6: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "04-30",leaveAlice = "05-30",arriveBob = "04-15",leaveBob = "05-15") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "04-30",leaveAlice = "05-30",arriveBob = "04-15",leaveBob = "05-15") == 16: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "07-20",leaveAlice = "08-10",arriveBob = "07-25",leaveBob = "08-05") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "07-20",leaveAlice = "08-10",arriveBob = "07-25",leaveBob = "08-05") == 12: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "08-05",leaveAlice = "10-10",arriveBob = "09-01",leaveBob = "10-05") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "08-05",leaveAlice = "10-10",arriveBob = "09-01",leaveBob = "10-05") == 35: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "08-15",leaveAlice = "09-20",arriveBob = "09-05",leaveBob = "10-05") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "08-15",leaveAlice = "09-20",arriveBob = "09-05",leaveBob = "10-05") == 16: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "01-15",leaveAlice = "03-20",arriveBob = "02-10",leaveBob = "04-15") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "01-15",leaveAlice = "03-20",arriveBob = "02-10",leaveBob = "04-15") == 39: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "10-20",leaveAlice = "11-10",arriveBob = "11-05",leaveBob = "12-15") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "10-20",leaveAlice = "11-10",arriveBob = "11-05",leaveBob = "12-15") == 6: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "06-30",leaveAlice = "07-01",arriveBob = "06-29",leaveBob = "07-02") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "06-30",leaveAlice = "07-01",arriveBob = "06-29",leaveBob = "07-02") == 2: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "02-28",leaveAlice = "03-01",arriveBob = "03-01",leaveBob = "03-02") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "02-28",leaveAlice = "03-01",arriveBob = "03-01",leaveBob = "03-02") == 1: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "04-01",leaveAlice = "04-30",arriveBob = "03-20",leaveBob = "04-25") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "04-01",leaveAlice = "04-30",arriveBob = "03-20",leaveBob = "04-25") == 25: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "09-10",leaveAlice = "10-10",arriveBob = "09-15",leaveBob = "09-20") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "09-10",leaveAlice = "10-10",arriveBob = "09-15",leaveBob = "09-20") == 6: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "05-10",leaveAlice = "05-10",arriveBob = "05-10",leaveBob = "05-10") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "05-10",leaveAlice = "05-10",arriveBob = "05-10",leaveBob = "05-10") == 1: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "07-20",leaveAlice = "07-25",arriveBob = "07-20",leaveBob = "07-25") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "07-20",leaveAlice = "07-25",arriveBob = "07-20",leaveBob = "07-25") == 6: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "08-01",leaveAlice = "08-31",arriveBob = "07-20",leaveBob = "08-10") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "08-01",leaveAlice = "08-31",arriveBob = "07-20",leaveBob = "08-10") == 10: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "06-15",leaveAlice = "06-20",arriveBob = "06-21",leaveBob = "06-25") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "06-15",leaveAlice = "06-20",arriveBob = "06-21",leaveBob = "06-25") == 0: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "12-15",leaveAlice = "12-20",arriveBob = "12-15",leaveBob = "12-20") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "12-15",leaveAlice = "12-20",arriveBob = "12-15",leaveBob = "12-20") == 6: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "11-01",leaveAlice = "11-30",arriveBob = "10-25",leaveBob = "11-25") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "11-01",leaveAlice = "11-30",arriveBob = "10-25",leaveBob = "11-25") == 25: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "07-31",leaveAlice = "07-31",arriveBob = "08-01",leaveBob = "08-01") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "07-31",leaveAlice = "07-31",arriveBob = "08-01",leaveBob = "08-01") == 0: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "08-01",leaveAlice = "08-31",arriveBob = "07-25",leaveBob = "08-15") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "08-01",leaveAlice = "08-31",arriveBob = "07-25",leaveBob = "08-15") == 15: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "02-14",leaveAlice = "03-14",arriveBob = "03-01",leaveBob = "04-01") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "02-14",leaveAlice = "03-14",arriveBob = "03-01",leaveBob = "04-01") == 14: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "08-10",leaveAlice = "09-10",arriveBob = "09-05",leaveBob = "09-20") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "08-10",leaveAlice = "09-10",arriveBob = "09-05",leaveBob = "09-20") == 6: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "01-01",leaveAlice = "01-31",arriveBob = "02-01",leaveBob = "02-28") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "01-01",leaveAlice = "01-31",arriveBob = "02-01",leaveBob = "02-28") == 0: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "03-15",leaveAlice = "03-31",arriveBob = "04-01",leaveBob = "04-10") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "03-15",leaveAlice = "03-31",arriveBob = "04-01",leaveBob = "04-10") == 0: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "01-01",leaveAlice = "12-31",arriveBob = "06-15",leaveBob = "06-15") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "01-01",leaveAlice = "12-31",arriveBob = "06-15",leaveBob = "06-15") == 1: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "11-15",leaveAlice = "11-30",arriveBob = "12-01",leaveBob = "12-31") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "11-15",leaveAlice = "11-30",arriveBob = "12-01",leaveBob = "12-31") == 0: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "09-01",leaveAlice = "11-15",arriveBob = "10-01",leaveBob = "10-31") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "09-01",leaveAlice = "11-15",arriveBob = "10-01",leaveBob = "10-31") == 31: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "04-15",leaveAlice = "06-20",arriveBob = "05-01",leaveBob = "07-15") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "04-15",leaveAlice = "06-20",arriveBob = "05-01",leaveBob = "07-15") == 51: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "08-20",leaveAlice = "09-20",arriveBob = "09-10",leaveBob = "10-10") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "08-20",leaveAlice = "09-20",arriveBob = "09-10",leaveBob = "10-10") == 11: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "07-10",leaveAlice = "08-10",arriveBob = "07-20",leaveBob = "08-20") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "07-10",leaveAlice = "08-10",arriveBob = "07-20",leaveBob = "08-20") == 22: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "05-10",leaveAlice = "06-10",arriveBob = "05-20",leaveBob = "06-20") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "05-10",leaveAlice = "06-10",arriveBob = "05-20",leaveBob = "06-20") == 22: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "06-01",leaveAlice = "06-10",arriveBob = "06-05",leaveBob = "06-05") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "06-01",leaveAlice = "06-10",arriveBob = "06-05",leaveBob = "06-05") == 1: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "11-10",leaveAlice = "11-10",arriveBob = "11-11",leaveBob = "11-11") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "11-10",leaveAlice = "11-10",arriveBob = "11-11",leaveBob = "11-11") == 0: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "09-01",leaveAlice = "10-31",arriveBob = "08-01",leaveBob = "09-15") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "09-01",leaveAlice = "10-31",arriveBob = "08-01",leaveBob = "09-15") == 15: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "12-15",leaveAlice = "12-31",arriveBob = "12-10",leaveBob = "12-15") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "12-15",leaveAlice = "12-31",arriveBob = "12-10",leaveBob = "12-15") == 1: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "07-01",leaveAlice = "07-31",arriveBob = "06-25",leaveBob = "07-25") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "07-01",leaveAlice = "07-31",arriveBob = "06-25",leaveBob = "07-25") == 25: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "03-10",leaveAlice = "04-10",arriveBob = "04-05",leaveBob = "05-10") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "03-10",leaveAlice = "04-10",arriveBob = "04-05",leaveBob = "05-10") == 6: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "03-31",leaveAlice = "03-31",arriveBob = "04-01",leaveBob = "04-01") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "03-31",leaveAlice = "03-31",arriveBob = "04-01",leaveBob = "04-01") == 0: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "09-10",leaveAlice = "10-10",arriveBob = "09-15",leaveBob = "10-15") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "09-10",leaveAlice = "10-10",arriveBob = "09-15",leaveBob = "10-15") == 26: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "05-25",leaveAlice = "06-05",arriveBob = "05-26",leaveBob = "06-04") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "05-25",leaveAlice = "06-05",arriveBob = "05-26",leaveBob = "06-04") == 10: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "10-15",leaveAlice = "10-20",arriveBob = "09-25",leaveBob = "10-16") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "10-15",leaveAlice = "10-20",arriveBob = "09-25",leaveBob = "10-16") == 2: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "09-01",leaveAlice = "10-31",arriveBob = "08-15",leaveBob = "09-15") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "09-01",leaveAlice = "10-31",arriveBob = "08-15",leaveBob = "09-15") == 15: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "03-01",leaveAlice = "03-31",arriveBob = "02-28",leaveBob = "03-10") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "03-01",leaveAlice = "03-31",arriveBob = "02-28",leaveBob = "03-10") == 10: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "06-01",leaveAlice = "08-31",arriveBob = "07-01",leaveBob = "07-31") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "06-01",leaveAlice = "08-31",arriveBob = "07-01",leaveBob = "07-31") == 31: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "07-25",leaveAlice = "08-25",arriveBob = "07-26",leaveBob = "07-27") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "07-25",leaveAlice = "08-25",arriveBob = "07-26",leaveBob = "07-27") == 2: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "06-01",leaveAlice = "08-31",arriveBob = "07-01",leaveBob = "09-30") == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "06-01",leaveAlice = "08-31",arriveBob = "07-01",leaveBob = "09-30") == 62: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "02-15",leaveAlice = "03-15",arriveBob = "03-10",leaveBob = "04-10") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "02-15",leaveAlice = "03-15",arriveBob = "03-10",leaveBob = "04-10") == 6: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "04-30",leaveAlice = "05-01",arriveBob = "04-29",leaveBob = "05-02") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "04-30",leaveAlice = "05-01",arriveBob = "04-29",leaveBob = "05-02") == 2: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "09-01",leaveAlice = "09-15",arriveBob = "08-20",leaveBob = "09-10") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "09-01",leaveAlice = "09-15",arriveBob = "08-20",leaveBob = "09-10") == 10: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "03-15",leaveAlice = "03-15",arriveBob = "03-15",leaveBob = "03-15") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "03-15",leaveAlice = "03-15",arriveBob = "03-15",leaveBob = "03-15") == 1: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "05-05",leaveAlice = "05-05",arriveBob = "05-04",leaveBob = "05-06") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "05-05",leaveAlice = "05-05",arriveBob = "05-04",leaveBob = "05-06") == 1: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "08-25",leaveAlice = "09-05",arriveBob = "09-01",leaveBob = "09-10") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "08-25",leaveAlice = "09-05",arriveBob = "09-01",leaveBob = "09-10") == 5: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "07-05",leaveAlice = "08-10",arriveBob = "08-05",leaveBob = "09-15") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "07-05",leaveAlice = "08-10",arriveBob = "08-05",leaveBob = "09-15") == 6: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "09-10",leaveAlice = "11-20",arriveBob = "10-01",leaveBob = "10-31") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "09-10",leaveAlice = "11-20",arriveBob = "10-01",leaveBob = "10-31") == 31: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "09-15",leaveAlice = "10-15",arriveBob = "10-01",leaveBob = "11-01") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "09-15",leaveAlice = "10-15",arriveBob = "10-01",leaveBob = "11-01") == 15: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "12-15",leaveAlice = "12-31",arriveBob = "12-20",leaveBob = "01-15") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "12-15",leaveAlice = "12-31",arriveBob = "12-20",leaveBob = "01-15") == 0: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "05-05",leaveAlice = "07-10",arriveBob = "06-01",leaveBob = "06-30") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "05-05",leaveAlice = "07-10",arriveBob = "06-01",leaveBob = "06-30") == 30: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "03-15",leaveAlice = "05-15",arriveBob = "04-01",leaveBob = "04-30") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "03-15",leaveAlice = "05-15",arriveBob = "04-01",leaveBob = "04-30") == 30: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "11-10",leaveAlice = "11-20",arriveBob = "11-21",leaveBob = "11-30") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "11-10",leaveAlice = "11-20",arriveBob = "11-21",leaveBob = "11-30") == 0: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "02-20",leaveAlice = "03-10",arriveBob = "03-05",leaveBob = "04-01") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "02-20",leaveAlice = "03-10",arriveBob = "03-05",leaveBob = "04-01") == 6: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "01-05",leaveAlice = "01-10",arriveBob = "01-08",leaveBob = "01-15") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "01-05",leaveAlice = "01-10",arriveBob = "01-08",leaveBob = "01-15") == 3: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "01-29",leaveAlice = "02-02",arriveBob = "02-01",leaveBob = "02-28") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "01-29",leaveAlice = "02-02",arriveBob = "02-01",leaveBob = "02-28") == 2: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "10-10",leaveAlice = "10-20",arriveBob = "09-30",leaveBob = "10-10") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "10-10",leaveAlice = "10-20",arriveBob = "09-30",leaveBob = "10-10") == 1: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "04-01",leaveAlice = "04-30",arriveBob = "04-10",leaveBob = "04-20") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "04-01",leaveAlice = "04-30",arriveBob = "04-10",leaveBob = "04-20") == 11: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "05-15",leaveAlice = "06-15",arriveBob = "06-10",leaveBob = "07-10") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "05-15",leaveAlice = "06-15",arriveBob = "06-10",leaveBob = "07-10") == 6: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "02-28",leaveAlice = "03-01",arriveBob = "02-28",leaveBob = "03-01") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "02-28",leaveAlice = "03-01",arriveBob = "02-28",leaveBob = "03-01") == 2: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "01-10",leaveAlice = "02-10",arriveBob = "02-01",leaveBob = "03-10") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "01-10",leaveAlice = "02-10",arriveBob = "02-01",leaveBob = "03-10") == 10: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "11-01",leaveAlice = "11-30",arriveBob = "11-15",leaveBob = "12-15") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "11-01",leaveAlice = "11-30",arriveBob = "11-15",leaveBob = "12-15") == 16: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "05-01",leaveAlice = "05-31",arriveBob = "04-30",leaveBob = "05-10") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "05-01",leaveAlice = "05-31",arriveBob = "04-30",leaveBob = "05-10") == 10: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "12-10",leaveAlice = "12-31",arriveBob = "12-20",leaveBob = "01-10") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "12-10",leaveAlice = "12-31",arriveBob = "12-20",leaveBob = "01-10") == 0: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "07-20",leaveAlice = "08-20",arriveBob = "08-01",leaveBob = "08-19") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "07-20",leaveAlice = "08-20",arriveBob = "08-01",leaveBob = "08-19") == 19: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "01-10",leaveAlice = "02-10",arriveBob = "01-15",leaveBob = "03-15") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "01-10",leaveAlice = "02-10",arriveBob = "01-15",leaveBob = "03-15") == 27: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "05-10",leaveAlice = "05-15",arriveBob = "05-12",leaveBob = "05-20") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "05-10",leaveAlice = "05-15",arriveBob = "05-12",leaveBob = "05-20") == 4: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "02-28",leaveAlice = "03-05",arriveBob = "03-01",leaveBob = "03-10") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "02-28",leaveAlice = "03-05",arriveBob = "03-01",leaveBob = "03-10") == 5: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "02-28",leaveAlice = "03-01",arriveBob = "02-29",leaveBob = "03-02") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "02-28",leaveAlice = "03-01",arriveBob = "02-29",leaveBob = "03-02") == 1: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "11-25",leaveAlice = "12-10",arriveBob = "12-01",leaveBob = "12-15") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "11-25",leaveAlice = "12-10",arriveBob = "12-01",leaveBob = "12-15") == 10: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "04-10",leaveAlice = "04-30",arriveBob = "04-15",leaveBob = "05-15") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "04-10",leaveAlice = "04-30",arriveBob = "04-15",leaveBob = "05-15") == 16: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "07-10",leaveAlice = "07-20",arriveBob = "07-20",leaveBob = "07-30") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "07-10",leaveAlice = "07-20",arriveBob = "07-20",leaveBob = "07-30") == 1: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "11-11",leaveAlice = "11-30",arriveBob = "11-15",leaveBob = "11-25") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "11-11",leaveAlice = "11-30",arriveBob = "11-15",leaveBob = "11-25") == 11: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "03-20",leaveAlice = "03-31",arriveBob = "04-01",leaveBob = "04-10") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "03-20",leaveAlice = "03-31",arriveBob = "04-01",leaveBob = "04-10") == 0: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "09-15",leaveAlice = "10-15",arriveBob = "10-10",leaveBob = "11-10") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "09-15",leaveAlice = "10-15",arriveBob = "10-10",leaveBob = "11-10") == 6: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "11-01",leaveAlice = "11-15",arriveBob = "10-25",leaveBob = "11-10") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "11-01",leaveAlice = "11-15",arriveBob = "10-25",leaveBob = "11-10") == 10: {e}')
    
    total += 1
    try:
        result = candidate(arriveAlice = "07-20",leaveAlice = "08-20",arriveBob = "07-15",leaveBob = "07-25") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arriveAlice = "07-20",leaveAlice = "08-20",arriveBob = "07-15",leaveBob = "07-25") == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arriveAlice = "03-10",leaveAlice = "05-20",arriveBob = "04-01",leaveBob = "04-30") == 30
    assert candidate(arriveAlice = "06-15",leaveAlice = "06-20",arriveBob = "06-18",leaveBob = "06-25") == 3
    assert candidate(arriveAlice = "10-01",leaveAlice = "10-31",arriveBob = "11-01",leaveBob = "12-31") == 0
    assert candidate(arriveAlice = "01-01",leaveAlice = "12-31",arriveBob = "01-01",leaveBob = "12-31") == 365
    assert candidate(arriveAlice = "08-15",leaveAlice = "08-18",arriveBob = "08-16",leaveBob = "08-19") == 3
    assert candidate(arriveAlice = "12-20",leaveAlice = "12-31",arriveBob = "12-25",leaveBob = "12-30") == 6
    assert candidate(arriveAlice = "05-24",leaveAlice = "07-24",arriveBob = "07-25",leaveBob = "08-25") == 0
    assert candidate(arriveAlice = "07-20",leaveAlice = "08-15",arriveBob = "07-25",leaveBob = "08-10") == 17
    assert candidate(arriveAlice = "07-01",leaveAlice = "08-01",arriveBob = "07-15",leaveBob = "07-30") == 16
    assert candidate(arriveAlice = "07-10",leaveAlice = "07-20",arriveBob = "07-15",leaveBob = "07-25") == 6
    assert candidate(arriveAlice = "01-01",leaveAlice = "01-31",arriveBob = "01-01",leaveBob = "01-31") == 31
    assert candidate(arriveAlice = "03-10",leaveAlice = "03-10",arriveBob = "03-10",leaveBob = "03-10") == 1
    assert candidate(arriveAlice = "06-15",leaveAlice = "06-15",arriveBob = "06-15",leaveBob = "06-15") == 1
    assert candidate(arriveAlice = "01-01",leaveAlice = "01-31",arriveBob = "01-15",leaveBob = "01-20") == 6
    assert candidate(arriveAlice = "03-14",leaveAlice = "03-14",arriveBob = "03-14",leaveBob = "03-14") == 1
    assert candidate(arriveAlice = "06-01",leaveAlice = "06-30",arriveBob = "05-25",leaveBob = "06-10") == 10
    assert candidate(arriveAlice = "10-01",leaveAlice = "10-20",arriveBob = "09-25",leaveBob = "10-25") == 20
    assert candidate(arriveAlice = "11-15",leaveAlice = "12-31",arriveBob = "12-01",leaveBob = "12-31") == 31
    assert candidate(arriveAlice = "04-10",leaveAlice = "06-10",arriveBob = "05-01",leaveBob = "06-30") == 41
    assert candidate(arriveAlice = "01-10",leaveAlice = "02-20",arriveBob = "02-15",leaveBob = "03-25") == 6
    assert candidate(arriveAlice = "09-15",leaveAlice = "09-15",arriveBob = "09-15",leaveBob = "09-15") == 1
    assert candidate(arriveAlice = "12-20",leaveAlice = "12-31",arriveBob = "12-15",leaveBob = "01-10") == 0
    assert candidate(arriveAlice = "05-05",leaveAlice = "07-05",arriveBob = "05-05",leaveBob = "05-05") == 1
    assert candidate(arriveAlice = "02-28",leaveAlice = "03-15",arriveBob = "03-01",leaveBob = "03-31") == 15
    assert candidate(arriveAlice = "08-15",leaveAlice = "09-15",arriveBob = "09-15",leaveBob = "10-15") == 1
    assert candidate(arriveAlice = "03-05",leaveAlice = "03-20",arriveBob = "03-15",leaveBob = "03-25") == 6
    assert candidate(arriveAlice = "03-15",leaveAlice = "03-20",arriveBob = "03-10",leaveBob = "03-14") == 0
    assert candidate(arriveAlice = "06-01",leaveAlice = "06-30",arriveBob = "06-15",leaveBob = "06-25") == 11
    assert candidate(arriveAlice = "02-28",leaveAlice = "03-10",arriveBob = "03-01",leaveBob = "03-15") == 10
    assert candidate(arriveAlice = "01-15",leaveAlice = "01-15",arriveBob = "01-15",leaveBob = "01-15") == 1
    assert candidate(arriveAlice = "01-01",leaveAlice = "01-31",arriveBob = "01-15",leaveBob = "02-14") == 17
    assert candidate(arriveAlice = "12-15",leaveAlice = "12-15",arriveBob = "12-16",leaveBob = "12-16") == 0
    assert candidate(arriveAlice = "11-11",leaveAlice = "11-11",arriveBob = "11-11",leaveBob = "11-11") == 1
    assert candidate(arriveAlice = "11-20",leaveAlice = "12-15",arriveBob = "11-25",leaveBob = "12-25") == 21
    assert candidate(arriveAlice = "11-11",leaveAlice = "11-25",arriveBob = "11-20",leaveBob = "12-10") == 6
    assert candidate(arriveAlice = "04-30",leaveAlice = "05-30",arriveBob = "04-15",leaveBob = "05-15") == 16
    assert candidate(arriveAlice = "07-20",leaveAlice = "08-10",arriveBob = "07-25",leaveBob = "08-05") == 12
    assert candidate(arriveAlice = "08-05",leaveAlice = "10-10",arriveBob = "09-01",leaveBob = "10-05") == 35
    assert candidate(arriveAlice = "08-15",leaveAlice = "09-20",arriveBob = "09-05",leaveBob = "10-05") == 16
    assert candidate(arriveAlice = "01-15",leaveAlice = "03-20",arriveBob = "02-10",leaveBob = "04-15") == 39
    assert candidate(arriveAlice = "10-20",leaveAlice = "11-10",arriveBob = "11-05",leaveBob = "12-15") == 6
    assert candidate(arriveAlice = "06-30",leaveAlice = "07-01",arriveBob = "06-29",leaveBob = "07-02") == 2
    assert candidate(arriveAlice = "02-28",leaveAlice = "03-01",arriveBob = "03-01",leaveBob = "03-02") == 1
    assert candidate(arriveAlice = "04-01",leaveAlice = "04-30",arriveBob = "03-20",leaveBob = "04-25") == 25
    assert candidate(arriveAlice = "09-10",leaveAlice = "10-10",arriveBob = "09-15",leaveBob = "09-20") == 6
    assert candidate(arriveAlice = "05-10",leaveAlice = "05-10",arriveBob = "05-10",leaveBob = "05-10") == 1
    assert candidate(arriveAlice = "07-20",leaveAlice = "07-25",arriveBob = "07-20",leaveBob = "07-25") == 6
    assert candidate(arriveAlice = "08-01",leaveAlice = "08-31",arriveBob = "07-20",leaveBob = "08-10") == 10
    assert candidate(arriveAlice = "06-15",leaveAlice = "06-20",arriveBob = "06-21",leaveBob = "06-25") == 0
    assert candidate(arriveAlice = "12-15",leaveAlice = "12-20",arriveBob = "12-15",leaveBob = "12-20") == 6
    assert candidate(arriveAlice = "11-01",leaveAlice = "11-30",arriveBob = "10-25",leaveBob = "11-25") == 25
    assert candidate(arriveAlice = "07-31",leaveAlice = "07-31",arriveBob = "08-01",leaveBob = "08-01") == 0
    assert candidate(arriveAlice = "08-01",leaveAlice = "08-31",arriveBob = "07-25",leaveBob = "08-15") == 15
    assert candidate(arriveAlice = "02-14",leaveAlice = "03-14",arriveBob = "03-01",leaveBob = "04-01") == 14
    assert candidate(arriveAlice = "08-10",leaveAlice = "09-10",arriveBob = "09-05",leaveBob = "09-20") == 6
    assert candidate(arriveAlice = "01-01",leaveAlice = "01-31",arriveBob = "02-01",leaveBob = "02-28") == 0
    assert candidate(arriveAlice = "03-15",leaveAlice = "03-31",arriveBob = "04-01",leaveBob = "04-10") == 0
    assert candidate(arriveAlice = "01-01",leaveAlice = "12-31",arriveBob = "06-15",leaveBob = "06-15") == 1
    assert candidate(arriveAlice = "11-15",leaveAlice = "11-30",arriveBob = "12-01",leaveBob = "12-31") == 0
    assert candidate(arriveAlice = "09-01",leaveAlice = "11-15",arriveBob = "10-01",leaveBob = "10-31") == 31
    assert candidate(arriveAlice = "04-15",leaveAlice = "06-20",arriveBob = "05-01",leaveBob = "07-15") == 51
    assert candidate(arriveAlice = "08-20",leaveAlice = "09-20",arriveBob = "09-10",leaveBob = "10-10") == 11
    assert candidate(arriveAlice = "07-10",leaveAlice = "08-10",arriveBob = "07-20",leaveBob = "08-20") == 22
    assert candidate(arriveAlice = "05-10",leaveAlice = "06-10",arriveBob = "05-20",leaveBob = "06-20") == 22
    assert candidate(arriveAlice = "06-01",leaveAlice = "06-10",arriveBob = "06-05",leaveBob = "06-05") == 1
    assert candidate(arriveAlice = "11-10",leaveAlice = "11-10",arriveBob = "11-11",leaveBob = "11-11") == 0
    assert candidate(arriveAlice = "09-01",leaveAlice = "10-31",arriveBob = "08-01",leaveBob = "09-15") == 15
    assert candidate(arriveAlice = "12-15",leaveAlice = "12-31",arriveBob = "12-10",leaveBob = "12-15") == 1
    assert candidate(arriveAlice = "07-01",leaveAlice = "07-31",arriveBob = "06-25",leaveBob = "07-25") == 25
    assert candidate(arriveAlice = "03-10",leaveAlice = "04-10",arriveBob = "04-05",leaveBob = "05-10") == 6
    assert candidate(arriveAlice = "03-31",leaveAlice = "03-31",arriveBob = "04-01",leaveBob = "04-01") == 0
    assert candidate(arriveAlice = "09-10",leaveAlice = "10-10",arriveBob = "09-15",leaveBob = "10-15") == 26
    assert candidate(arriveAlice = "05-25",leaveAlice = "06-05",arriveBob = "05-26",leaveBob = "06-04") == 10
    assert candidate(arriveAlice = "10-15",leaveAlice = "10-20",arriveBob = "09-25",leaveBob = "10-16") == 2
    assert candidate(arriveAlice = "09-01",leaveAlice = "10-31",arriveBob = "08-15",leaveBob = "09-15") == 15
    assert candidate(arriveAlice = "03-01",leaveAlice = "03-31",arriveBob = "02-28",leaveBob = "03-10") == 10
    assert candidate(arriveAlice = "06-01",leaveAlice = "08-31",arriveBob = "07-01",leaveBob = "07-31") == 31
    assert candidate(arriveAlice = "07-25",leaveAlice = "08-25",arriveBob = "07-26",leaveBob = "07-27") == 2
    assert candidate(arriveAlice = "06-01",leaveAlice = "08-31",arriveBob = "07-01",leaveBob = "09-30") == 62
    assert candidate(arriveAlice = "02-15",leaveAlice = "03-15",arriveBob = "03-10",leaveBob = "04-10") == 6
    assert candidate(arriveAlice = "04-30",leaveAlice = "05-01",arriveBob = "04-29",leaveBob = "05-02") == 2
    assert candidate(arriveAlice = "09-01",leaveAlice = "09-15",arriveBob = "08-20",leaveBob = "09-10") == 10
    assert candidate(arriveAlice = "03-15",leaveAlice = "03-15",arriveBob = "03-15",leaveBob = "03-15") == 1
    assert candidate(arriveAlice = "05-05",leaveAlice = "05-05",arriveBob = "05-04",leaveBob = "05-06") == 1
    assert candidate(arriveAlice = "08-25",leaveAlice = "09-05",arriveBob = "09-01",leaveBob = "09-10") == 5
    assert candidate(arriveAlice = "07-05",leaveAlice = "08-10",arriveBob = "08-05",leaveBob = "09-15") == 6
    assert candidate(arriveAlice = "09-10",leaveAlice = "11-20",arriveBob = "10-01",leaveBob = "10-31") == 31
    assert candidate(arriveAlice = "09-15",leaveAlice = "10-15",arriveBob = "10-01",leaveBob = "11-01") == 15
    assert candidate(arriveAlice = "12-15",leaveAlice = "12-31",arriveBob = "12-20",leaveBob = "01-15") == 0
    assert candidate(arriveAlice = "05-05",leaveAlice = "07-10",arriveBob = "06-01",leaveBob = "06-30") == 30
    assert candidate(arriveAlice = "03-15",leaveAlice = "05-15",arriveBob = "04-01",leaveBob = "04-30") == 30
    assert candidate(arriveAlice = "11-10",leaveAlice = "11-20",arriveBob = "11-21",leaveBob = "11-30") == 0
    assert candidate(arriveAlice = "02-20",leaveAlice = "03-10",arriveBob = "03-05",leaveBob = "04-01") == 6
    assert candidate(arriveAlice = "01-05",leaveAlice = "01-10",arriveBob = "01-08",leaveBob = "01-15") == 3
    assert candidate(arriveAlice = "01-29",leaveAlice = "02-02",arriveBob = "02-01",leaveBob = "02-28") == 2
    assert candidate(arriveAlice = "10-10",leaveAlice = "10-20",arriveBob = "09-30",leaveBob = "10-10") == 1
    assert candidate(arriveAlice = "04-01",leaveAlice = "04-30",arriveBob = "04-10",leaveBob = "04-20") == 11
    assert candidate(arriveAlice = "05-15",leaveAlice = "06-15",arriveBob = "06-10",leaveBob = "07-10") == 6
    assert candidate(arriveAlice = "02-28",leaveAlice = "03-01",arriveBob = "02-28",leaveBob = "03-01") == 2
    assert candidate(arriveAlice = "01-10",leaveAlice = "02-10",arriveBob = "02-01",leaveBob = "03-10") == 10
    assert candidate(arriveAlice = "11-01",leaveAlice = "11-30",arriveBob = "11-15",leaveBob = "12-15") == 16
    assert candidate(arriveAlice = "05-01",leaveAlice = "05-31",arriveBob = "04-30",leaveBob = "05-10") == 10
    assert candidate(arriveAlice = "12-10",leaveAlice = "12-31",arriveBob = "12-20",leaveBob = "01-10") == 0
    assert candidate(arriveAlice = "07-20",leaveAlice = "08-20",arriveBob = "08-01",leaveBob = "08-19") == 19
    assert candidate(arriveAlice = "01-10",leaveAlice = "02-10",arriveBob = "01-15",leaveBob = "03-15") == 27
    assert candidate(arriveAlice = "05-10",leaveAlice = "05-15",arriveBob = "05-12",leaveBob = "05-20") == 4
    assert candidate(arriveAlice = "02-28",leaveAlice = "03-05",arriveBob = "03-01",leaveBob = "03-10") == 5
    assert candidate(arriveAlice = "02-28",leaveAlice = "03-01",arriveBob = "02-29",leaveBob = "03-02") == 1
    assert candidate(arriveAlice = "11-25",leaveAlice = "12-10",arriveBob = "12-01",leaveBob = "12-15") == 10
    assert candidate(arriveAlice = "04-10",leaveAlice = "04-30",arriveBob = "04-15",leaveBob = "05-15") == 16
    assert candidate(arriveAlice = "07-10",leaveAlice = "07-20",arriveBob = "07-20",leaveBob = "07-30") == 1
    assert candidate(arriveAlice = "11-11",leaveAlice = "11-30",arriveBob = "11-15",leaveBob = "11-25") == 11
    assert candidate(arriveAlice = "03-20",leaveAlice = "03-31",arriveBob = "04-01",leaveBob = "04-10") == 0
    assert candidate(arriveAlice = "09-15",leaveAlice = "10-15",arriveBob = "10-10",leaveBob = "11-10") == 6
    assert candidate(arriveAlice = "11-01",leaveAlice = "11-15",arriveBob = "10-25",leaveBob = "11-10") == 10
    assert candidate(arriveAlice = "07-20",leaveAlice = "08-20",arriveBob = "07-15",leaveBob = "07-25") == 6


